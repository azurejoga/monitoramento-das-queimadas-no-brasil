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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dd1e263-b051-3def-9980-6bd1f3d8cd0b | -12.61869 | -44.25307 | 2025-10-30 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c6029ebf-5ad7-3314-9842-12c6be3f2926 | -14.12756 | -44.06688 | 2025-10-30 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fc90b1d-0d7c-38e8-bf98-c8be9b6f4301 | -18.04795 | -43.14909 | 2025-10-30 03:38:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 312d87bc-9f34-3d04-a3e1-7cf6f34b9ce7 | -13.59962 | -42.29105 | 2025-10-30 03:38:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54033866-bb64-3ed6-b336-5397d92c9fa2 | -18.2363 | -42.37304 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b631d502-9f56-35eb-b6b5-4d51de1353b5 | -18.54811 | -41.57546 | 2025-10-30 03:38:00 | NOAA-21 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 401af9e4-6cdb-3caf-b8c4-fea581f36a16 | -18.68064 | -41.67372 | 2025-10-30 03:38:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 239c39c1-f004-342e-8bea-8a7a6434249a | -12.88364 | -48.63374 | 2025-10-30 03:38:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 60b5a465-198d-310f-86e3-afe62f141942 | -13.51723 | -47.33398 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 527f8b8a-4451-3408-acf9-5e27a39bc352 | -13.32704 | -47.46523 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6e2c0716-b668-3081-83b9-6d089e19e0d8 | -18.56556 | -42.40853 | 2025-10-30 03:38:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 15fc3395-2f14-37b3-8c4e-8d348ddeb829 | -14.36604 | -43.5621 | 2025-10-30 03:38:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaa95d74-410f-3493-bfb7-337991feb4d0 | -14.75941 | -44.96279 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9207fba-021f-3e01-b728-0b6f5dec7954 | -15.26628 | -43.6974 | 2025-10-30 03:38:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1c056f6-446c-365a-ad35-c8262e5445fa | -18.04094 | -42.0874 | 2025-10-30 03:38:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dd88dfed-3fc0-3578-93b6-c579d5a10e27 | -13.71823 | -48.75976 | 2025-10-30 03:38:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c941beee-50fa-36bf-85a1-9aabba62bb57 | -13.36437 | -43.08614 | 2025-10-30 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a1e312f0-9430-3cab-8fc9-3f4c462bb8b0 | -11.29611 | -47.54782 | 2025-10-30 03:38:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d0f5600-1c18-3640-a01d-fe67be531a7a | -14.78793 | -44.98704 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fb98357-9268-3317-bad1-5a2b542b6082 | -18.35659 | -42.24327 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1a151777-1d46-3866-b034-b478180ae035 | -18.35579 | -42.24751 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 41842357-4d3a-30cb-8eea-3d8990ade52d | -18.2451 | -42.62225 | 2025-10-30 03:38:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 731df354-11b1-3e23-bd7b-b60f29f4743f | -13.61194 | -47.59494 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3899fea0-495c-3e7a-8449-d44cfacf49c6 | -14.71579 | -45.09705 | 2025-10-30 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7efa6f2e-cdb0-3f65-95ec-4de8e79831a2 | -14.78193 | -44.98928 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c49e1d6e-9128-3fd9-9e38-0bb33c51c4cf | -13.71572 | -48.77122 | 2025-10-30 03:38:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 450cab16-3be9-37cf-8ef7-ace0d222187a | -12.69216 | -46.33186 | 2025-10-30 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7344dbc5-495b-3a1f-83a8-8905d42b0481 | -14.78485 | -44.99029 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37305b39-f44f-37c5-85f4-1755d98f6e96 | -15.09653 | -41.98594 | 2025-10-30 03:38:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60b4d84f-d77f-3c03-a66c-0693d3d6ef72 | -12.58227 | -44.96892 | 2025-10-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9b5074ac-8a56-3d4a-b30e-f365ae86cf84 | -15.09216 | -41.98512 | 2025-10-30 03:38:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1d4f4fc1-d0cb-3b3f-af61-eb491a84d78b | -16.81041 | -41.22768 | 2025-10-30 03:38:00 | NOAA-21 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7ad21cea-200b-34b1-8e05-3b3a4674c318 | -18.04502 | -42.0887 | 2025-10-30 03:38:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7844c211-3d0e-37f0-a2e7-ab22f3b7feca | -17.70903 | -41.15188 | 2025-10-30 03:38:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 18feb8a2-ed1d-3912-9f2a-c6fedeb64639 | -13.26864 | -47.74905 | 2025-10-30 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 050b8179-f2d1-384a-a28e-f4b561b2a443 | -15.61512 | -43.98724 | 2025-10-30 03:38:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c5ee5f0-586c-3fbf-9941-188bf05b2f6f | -13.43499 | -47.36823 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 72ce19d2-b489-3e87-802d-62eddef4394d | -12.31444 | -48.0638 | 2025-10-30 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8ade53fe-f986-3d4a-9b13-6789e172bbe2 | -17.95376 | -43.00011 | 2025-10-30 03:38:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| eb356b66-9e25-3d53-a22c-0b71b22b96a8 | -14.22933 | -44.31843 | 2025-10-30 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4d4dbfc-7371-3fe6-a4d0-64a884296d10 | -13.52893 | -44.34395 | 2025-10-30 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d704f7c4-53dc-3049-b413-e3d4fcbce704 | -12.69446 | -46.32764 | 2025-10-30 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fb8a83c6-7f1f-369f-bce5-55daa7f07a00 | -13.88538 | -43.93326 | 2025-10-30 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52d5d676-70f4-374d-bf51-b646d8230a98 | -16.62341 | -42.85683 | 2025-10-30 03:38:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9fc5127-e319-391c-8fa0-7f6432f3af7e | -16.13969 | -42.21441 | 2025-10-30 03:38:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1cc26cfc-165e-32e1-8caa-1879cbff5955 | -12.69314 | -46.32693 | 2025-10-30 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a91fcda7-7495-35bf-838d-e13579fa407e | -12.68712 | -46.3257 | 2025-10-30 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ca15878-6872-3a56-ab2a-5ff77624fb6c | -13.30538 | -47.70115 | 2025-10-30 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 16338f96-bb4a-373b-a078-db6ecb240a84 | -18.2494 | -42.6231 | 2025-10-30 03:38:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0f13e121-158b-3c28-8d92-0b63409f7a1e | -17.14835 | -41.93487 | 2025-10-30 03:38:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 11399673-4ba1-3602-84c0-996c50c7b57a | -13.13366 | -42.50229 | 2025-10-30 03:38:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d4a2bb17-06c8-3e2f-8f4d-7a40052b831e | -16.33877 | -45.05935 | 2025-10-30 03:38:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d2d4d94-7842-30b8-ab1d-b6080de92c8d | -13.31678 | -47.48275 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6abdca9-4e81-382b-bcb1-5f4e17afd660 | -13.27456 | -47.72039 | 2025-10-30 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f58811ae-adfc-3cb7-bdad-4b61876fa4d3 | -12.18858 | -46.71451 | 2025-10-30 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2a09acf4-c2f7-36d4-bb7a-9c9068bab828 | -19.47086 | -41.55555 | 2025-10-30 03:38:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 819713bf-3325-3a4a-8118-bdf49b069571 | -12.85073 | -48.62052 | 2025-10-30 03:38:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7cbc7890-cc0b-3f4e-8eb5-4c3afbbce4e5 | -13.35849 | -43.09061 | 2025-10-30 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| eea9f027-8076-3ae4-98be-27c9bb5610b0 | -12.84965 | -48.62503 | 2025-10-30 03:38:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 153ef4e7-de56-38a9-a96e-5bce6daad95c | -14.57379 | -40.72308 | 2025-10-30 03:38:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab33a5b7-86e0-3e94-bb2e-c79624972830 | -18.55209 | -41.57638 | 2025-10-30 03:38:00 | NOAA-21 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| af85092d-931e-3418-800b-2c46d4618091 | -13.42898 | -47.36537 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 912777ed-31dc-3462-92d5-7d82724c30f2 | -14.28256 | -42.33474 | 2025-10-30 03:38:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2e3cc6bc-aa95-3f9c-b2bc-9c272f211095 | -13.41475 | -43.74716 | 2025-10-30 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5920f0a2-fc09-3206-bb71-b952658403d1 | -18.23208 | -42.37207 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b4cf4f68-888d-3a2e-ae4f-850ce33c5a08 | -12.85745 | -48.62261 | 2025-10-30 03:38:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 830e8177-e9a3-330f-b487-721d57e69bdd | -13.82343 | -42.5125 | 2025-10-30 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2270a87d-c563-3b55-af92-b479e176fc8d | -16.03757 | -43.72616 | 2025-10-30 03:38:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f6dd231-b38a-3287-b606-50c764fd08eb | -12.81228 | -43.45483 | 2025-10-30 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb66619a-c3ce-3de2-91b2-a9b74eaa8162 | -18.12943 | -42.60924 | 2025-10-30 03:38:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 457417fa-4b07-3358-b197-50cec28c4d18 | -15.61017 | -43.98631 | 2025-10-30 03:38:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de8a0234-fde3-315a-9b4b-c2a0fd4848fa | -12.26838 | -46.76868 | 2025-10-30 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 004ee3e5-8e62-3f78-b578-6ddcab78eb37 | -13.48113 | -40.41004 | 2025-10-30 03:38:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dc2accf2-f85b-30be-8e56-34e0ccfa9d76 | -18.57829 | -43.08785 | 2025-10-30 03:38:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e8f42ee7-435e-3ab1-a5c6-209b14bbc751 | -14.03496 | -42.29303 | 2025-10-30 03:38:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c3adff89-54bd-36a3-b71e-e0c63aeb7db5 | -12.91504 | -45.04792 | 2025-10-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8c1d56f2-f5cd-34d3-a86b-c4de2cb9eb63 | -14.76801 | -44.9754 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f68632f7-45e1-3e12-9d22-c8df492fc845 | -14.78556 | -44.98682 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc727cac-6f22-3eb3-a2c6-3ff47171eb07 | -14.7601 | -44.95935 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b4a6b98-258d-3e58-ae86-49c7a8cdbca9 | -18.81237 | -43.33886 | 2025-10-30 03:38:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0e0f3e90-9678-3f68-8fef-2a89113a71e8 | -18.35993 | -42.24867 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ddb99f1c-4261-390b-8aa5-bd4e6398be21 | -14.76336 | -44.97087 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a359ed98-60ef-3c46-a9da-3b230c86ca2d | -12.70532 | -46.2971 | 2025-10-30 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4033b337-b479-351f-91fd-49be41fb6fae | -13.31792 | -47.47723 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a665ed6c-1b16-3ef2-9339-9dadc8f54156 | -18.35325 | -42.23785 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e67192e3-e4a8-319d-a9cb-984906db80d8 | -15.86081 | -44.89226 | 2025-10-30 03:38:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98de0b5a-47d7-31db-aac4-b06d4686729f | -14.7773 | -44.9846 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c56683a9-5a10-3a14-a29a-70dafa67a0f9 | -12.61933 | -44.24977 | 2025-10-30 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5470625d-b69b-31ed-b323-9e53d66e91e6 | -13.37197 | -47.38524 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 587aa855-9b0b-3f7f-8b1e-e9cf445c35bd | -13.07175 | -48.21248 | 2025-10-30 03:38:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 567a6c74-4b9b-3f87-b34a-529d67ce3cf5 | -13.30052 | -47.06602 | 2025-10-30 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32de4f51-e660-30ca-9f15-a4132bec04fb | -13.27568 | -47.74773 | 2025-10-30 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ed164e2-7818-3efa-bc8b-781bd1159591 | -12.71176 | -46.30445 | 2025-10-30 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 88fa4ba1-ab9b-3a69-ac47-ef07e1fd2c2c | -15.09133 | -41.98953 | 2025-10-30 03:38:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e69188f7-d4ba-369e-83cf-cc3e7889a474 | -14.97357 | -43.38972 | 2025-10-30 03:38:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fbb3246f-ba05-3e1d-a1d3-86f7287fe3b0 | -14.76405 | -44.96739 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab6858d9-fb28-3abe-93f6-712d23b97458 | -12.81812 | -43.45452 | 2025-10-30 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce5d5d53-cf9e-3fd2-a904-55665c5754c9 | -12.26939 | -46.76366 | 2025-10-30 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d5f9a7e-9bb3-3a27-a895-9268b09bbf6b | -15.55768 | -42.9792 | 2025-10-30 03:38:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8171e22b-1fbb-3d92-aa5b-6312bd8fe9aa | -15.85495 | -44.89447 | 2025-10-30 03:38:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README18.md)
