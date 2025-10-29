# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4541355e-b3c5-3818-84bb-c62dd107e26e | -5.41516 | -45.22002 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83869ff7-6a7a-3ec0-b435-05438b8dd2ff | -7.08802 | -47.2524 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2177524d-d2eb-323e-a7d3-2c4d6b6a897c | -5.57662 | -46.5317 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28599f3f-82df-393f-ad10-7b073f0cf2c5 | -7.80293 | -46.45551 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 04919387-9d7d-38eb-bf5f-88427cebc795 | -7.29945 | -44.98806 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74c1982c-bc9b-38a2-921e-89c0f643dafd | -5.04859 | -44.06941 | 2025-10-29 03:53:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 616f4e1c-6e2c-3476-b41d-fe2ce6832191 | -4.5105 | -45.99516 | 2025-10-29 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81fa692c-8eb1-32c1-aa3c-a271d757fa57 | -6.13424 | -41.83438 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 81d45aad-f9e0-3e4b-9961-616aa3057e7a | -6.72024 | -43.57741 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 43c0d3ae-c886-3eb9-a015-253655e6ee95 | -7.34053 | -42.47018 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 0dc64473-1d8e-35b3-95e3-dc3f43d35323 | -3.03642 | -49.51861 | 2025-10-29 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f858f090-d6c5-3f52-b4ec-7458ab6372f6 | -7.80782 | -46.45626 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 80bd62e9-8405-30ec-83df-86f9d346a75a | -8.19165 | -44.45026 | 2025-10-29 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 660d41d4-dcac-3614-9e42-0729e0ff566b | -7.59779 | -46.79835 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16e63652-fbd9-3722-85b7-df20eb19eae4 | -4.7998 | -37.82788 | 2025-10-29 03:53:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c0529ad3-aa36-37f8-9407-fab21976c1df | -5.19395 | -45.62299 | 2025-10-29 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cc83ac2-1a0c-3697-b0ec-174f7644d000 | -6.47324 | -42.23761 | 2025-10-29 03:53:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 73cc30a0-686f-3fe8-a714-7a4b6c6e8b54 | -13.65887 | -48.4481 | 2025-10-29 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 904c3974-ce61-354f-b17e-ce92f8977ac7 | -12.86055 | -43.71545 | 2025-10-29 03:55:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 432e2fe1-24ea-3169-b091-8342e03a72b9 | -13.62915 | -47.01763 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49892464-0580-369a-8c92-c4e20ead6b15 | -9.39607 | -44.55844 | 2025-10-29 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eeb7a94d-d88a-32ac-9e7c-ee3ce201d2ea | -13.64826 | -48.44917 | 2025-10-29 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 017ed06b-402a-3ae1-ba1a-2a063c30f30f | -12.35971 | -50.15623 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 125ca0b9-9165-379f-8af5-8b8fffadd3f9 | -9.49328 | -47.001 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29f377a1-acbd-3fc0-ac3e-87f8baf86edb | -13.64709 | -47.02412 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa9494ca-5351-379a-a68a-a5eefb214c80 | -10.50591 | -47.7268 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2473d529-2555-344e-b987-5b3f57b9077b | -15.57541 | -43.54544 | 2025-10-29 03:55:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b9f641c-91f1-39e5-bd22-080c80e3f5c8 | -11.13929 | -44.94014 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbc35afb-0b9b-3969-87e0-bb2c06ad076e | -13.88906 | -48.51381 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28695472-11ef-37af-9d2a-a46b4bef3fa1 | -10.52388 | -47.74289 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe4cf759-950b-3e5d-b201-bbeac8bb3a5a | -13.67899 | -47.66151 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 333ebf61-3a7f-398b-a8c9-cba9b3120d4e | -12.10459 | -44.59869 | 2025-10-29 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 05dced09-a39a-334e-96ee-68856bc95cf5 | -14.12213 | -44.18838 | 2025-10-29 03:55:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbbf9506-5eb7-3a42-9dc8-bd9438be2bac | -15.43803 | -44.18803 | 2025-10-29 03:55:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bf61c56-7fe7-3276-b99b-85497cfa7e1b | -9.90343 | -44.91522 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f3d63a04-23df-3024-9642-f7be593783d7 | -16.592 | -43.51551 | 2025-10-29 03:55:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac8dc77c-0b9f-3182-83f4-566f992e3215 | -13.04863 | -43.82191 | 2025-10-29 03:55:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 91428f8b-520d-3134-9b63-4406eff8900a | -14.59927 | -48.40688 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d530062-c0a5-3194-99a2-cab1e340f2dd | -12.70053 | -46.30923 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b51ad7e5-3aa9-3319-bba7-3a8a57549919 | -15.17529 | -47.20908 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08611548-332c-3b81-ae77-2117f4631e51 | -9.3947 | -44.55857 | 2025-10-29 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b490945b-d80a-3d9c-b188-0d69e101e708 | -10.6558 | -48.00215 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8f5ba2a3-d8bf-3376-8b40-77d274f45ef3 | -10.0832 | -45.3309 | 2025-10-29 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50f6c343-b31e-3dab-a847-04cff7c30c80 | -13.23365 | -48.56544 | 2025-10-29 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70c6d004-f420-3747-9c06-0c95ecbcaa33 | -14.48051 | -45.25913 | 2025-10-29 03:55:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35c2740f-cde9-3146-9687-164268c79274 | -16.21769 | -44.83049 | 2025-10-29 03:55:00 | NOAA-21 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d2d9628-a1c4-3221-910f-8324dccd507d | -11.27922 | -47.54374 | 2025-10-29 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a425e66-84ee-3d8d-b9b8-f41f7a31a123 | -13.86967 | -48.48249 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a10072c6-b972-32b0-87d3-13cdff664c2e | -9.29003 | -47.02706 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 809955e6-1f40-3967-bbaf-28de109676b2 | -10.66819 | -44.80191 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1915d8cf-c07c-34c1-9935-d500f7ac9bd6 | -15.74907 | -44.59554 | 2025-10-29 03:55:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6904f5f8-2f0a-3e8b-b600-de0ffe0bdb3d | -14.59816 | -48.41259 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73b45f19-8084-383c-bcf8-07c188f16340 | -10.7695 | -47.8897 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 680a0ee1-3a0b-34ec-a312-4f8b0af9c82b | -10.95999 | -47.61885 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5e2c2c1-1f38-3448-b9fc-3b1fadf2ea3b | -13.81999 | -41.69165 | 2025-10-29 03:55:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 8950ecd9-bf4e-32ca-af97-1396f60d1a8b | -13.54811 | -47.32844 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d70c51b4-b038-3b16-bdbf-402c4d7971a3 | -13.94232 | -48.48059 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 515e5658-e28b-3f76-b275-5c5311f75ae3 | -12.69352 | -46.32238 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 98e332a4-eea6-3f73-a2d7-0dae43569821 | -13.17725 | -48.44738 | 2025-10-29 03:55:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53a2aa9d-c72f-3c37-8287-db01e8b97d47 | -12.41169 | -44.71025 | 2025-10-29 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7db9db5-7d6a-3d01-ab70-bb6131eff5da | -9.48942 | -47.01022 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c7c3eff4-f659-39ed-8c09-4de429e46080 | -10.85816 | -50.1428 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a07bd7c-473d-3067-a6c2-fcd29c591671 | -12.20122 | -46.49525 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f9f120a-092b-36be-83ac-7d957f02bc37 | -13.53694 | -47.13117 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1aef4ea6-b105-3392-9342-e416171ff7e4 | -15.18466 | -44.06015 | 2025-10-29 03:55:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f767061-a329-3129-926c-f247087f3b0d | -14.66235 | -50.18562 | 2025-10-29 03:55:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6021d39d-6e0e-3cd5-b8cf-310da0e5e32f | -9.4973 | -46.99434 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd087c18-b2de-3db1-a062-a8352b80a109 | -9.92723 | -47.66691 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b59b4d70-b28c-360e-9f59-435f45876e42 | -12.95398 | -42.48014 | 2025-10-29 03:55:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e3060c0e-40bf-3c84-9d29-0968714df780 | -13.57307 | -49.60859 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5d389413-2740-3d8a-aa59-aca93faa657a | -13.74086 | -48.3978 | 2025-10-29 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a1eafbb-5a66-3998-9f6c-810f4ffeb00e | -13.86254 | -48.49261 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3fc497a0-c81b-34c6-a984-ddf07c95d788 | -10.85779 | -47.896 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94c4f242-d317-3e1a-8648-2f06d4493863 | -10.77863 | -45.11142 | 2025-10-29 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c934200-4eb4-389b-8273-4b22c36ba817 | -10.12635 | -44.8363 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a72dc59c-58c9-37b9-9517-592c24f5c43e | -12.21399 | -46.5345 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a54e0ab-63a7-36b7-8b09-eecc6f7ed201 | -13.56627 | -47.33474 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6612fee-d2a9-34f4-b826-f92433d5fcb9 | -13.70542 | -47.67834 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52b27a63-0a51-37a1-bc3e-11e52c0d97d0 | -14.60184 | -48.41983 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 31e7814c-50b8-38c5-b11b-5e040328fa84 | -12.70849 | -46.3157 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f71a3a8-0bf9-370e-9408-ebeb9a20258a | -10.75478 | -44.74589 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8804fd16-b2f6-3af4-9674-08f2a939b9ea | -12.86421 | -48.6286 | 2025-10-29 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3d8da32-dda3-3cfc-a879-f1373ed23c5a | -13.22634 | -47.07167 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fe686908-1e37-3e50-b11a-6291d9e3dcce | -13.03927 | -46.73129 | 2025-10-29 03:55:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8bf979c9-dca3-3972-adf6-f2c0235f134e | -15.40158 | -42.92429 | 2025-10-29 03:55:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 725a6a70-d72b-3b69-953a-ed133ebb0d42 | -15.33487 | -42.01405 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 422469eb-5076-3e52-a1be-af81e4dbcf31 | -10.85599 | -47.89525 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3c314b3-4c3b-35bf-a400-f267fafa4f0c | -13.93884 | -48.44514 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2c8dd158-838f-3c77-a3a9-1f8009cabfd2 | -12.39558 | -46.64992 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92458204-7e35-3e9f-a4ef-61f009548f7c | -13.56942 | -47.16168 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96544ace-a558-327d-a981-b3e50b0d97ba | -10.98702 | -47.72483 | 2025-10-29 03:55:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c88a945-25d8-39fd-b954-24747984d282 | -13.32646 | -47.43726 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45dcee9e-ab9f-3dba-ad14-ae5c1c91aba5 | -10.62241 | -47.88223 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ad820d6-67ac-39eb-b864-21b5afa3724e | -10.65388 | -48.01233 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b4f1a7c-4b3a-3644-b422-e0ef64cbf79b | -12.29313 | -47.0047 | 2025-10-29 03:55:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 17008a9b-3448-3cd4-a870-7b873d92bde5 | -12.98149 | -48.38974 | 2025-10-29 03:55:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1863560-d242-3c26-835c-454950aabeb1 | -13.32473 | -47.44626 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 994239ea-9fe3-3a78-9a6e-16ba5e58adde | -10.54127 | -45.05013 | 2025-10-29 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a63e9a0-4272-3bea-a621-0671c9ccca5d | -11.58482 | -47.95652 | 2025-10-29 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c031aa94-5851-3430-8216-6573170c8bfe | -13.22724 | -47.06688 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README14.md)
