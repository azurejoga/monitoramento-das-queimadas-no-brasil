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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e4dba3c-7ee3-34cb-910e-9d65a83aa054 | -10.90772 | -56.85326 | 2026-06-19 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 692ac62b-2d7c-32c3-ad2a-5b6a7e2238bd | -12.15403 | -48.4496 | 2026-06-19 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 732c2354-4d87-37c9-8db4-504f8bf76be0 | -10.91495 | -56.85433 | 2026-06-19 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| defcb1eb-17c9-3a03-8242-0ae37e525d14 | -11.51913 | -54.25899 | 2026-06-19 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4544382-16bd-3fc1-a710-f489bb7df4e3 | -11.33484 | -48.00714 | 2026-06-19 05:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f5a0af9-c200-3171-968c-a65dc056b872 | -10.53856 | -47.70946 | 2026-06-19 05:23:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db797758-dd00-387e-8f87-b29a74f930fb | -9.21109 | -64.08583 | 2026-06-19 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16c8cf0f-0bbc-38b2-ae60-157a9c783235 | -14.20959 | -54.71303 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10da6e81-e1bc-3750-97c4-2096657420a8 | -18.97955 | -52.45179 | 2026-06-19 05:23:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4dd2cdc-6f30-3eba-ae16-ddfabc5dbd3a | -12.91977 | -49.48038 | 2026-06-19 05:23:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c76194c-07cd-3d90-93d0-0bef6a4ad565 | -14.20814 | -54.71093 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 240f5304-4e51-3f39-a942-cab26c0a78af | -10.55392 | -46.34 | 2026-06-19 05:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b598f1b6-5bdf-3a0f-8207-3335dc197847 | -10.04923 | -48.09928 | 2026-06-19 05:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1443ad00-3d69-349b-87b8-8ce6d8c46696 | -11.35875 | -55.82175 | 2026-06-19 05:23:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbc1701d-be83-3865-a562-a0da20fabf7a | -11.25961 | -53.95651 | 2026-06-19 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eeda442-c5bd-3365-9421-b565a6a3ecae | -9.74657 | -47.8748 | 2026-06-19 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bd9c832-3e2b-3d46-b155-beb7bc1387f3 | -12.13453 | -48.26778 | 2026-06-19 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 19456cfd-9df3-3638-98b5-c6da56b7ba48 | -10.57489 | -57.32135 | 2026-06-19 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a9f9af3-3d67-3105-b623-9cb5e77a86ee | -18.97586 | -52.45064 | 2026-06-19 05:23:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cc5ca77-8bf3-347c-878f-0dc6c7a39481 | -10.71112 | -56.23269 | 2026-06-19 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2ea7487-910a-3408-8088-5959562c8398 | -10.16155 | -56.6208 | 2026-06-19 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13557fee-2228-31a9-92ad-6bc59fe96f14 | -10.91133 | -56.85379 | 2026-06-19 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07556af9-cea5-3126-927c-10a441ddb74f | -12.14093 | -48.26841 | 2026-06-19 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7766cda7-66cd-337e-84d9-ebdb65aaa686 | -11.65659 | -51.35637 | 2026-06-19 05:23:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bea1bc58-311a-3f65-9b12-b8bcc2bff4dd | -12.13602 | -48.26925 | 2026-06-19 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d0b1473-6971-3300-afd2-15a52397de16 | -10.90275 | -54.13725 | 2026-06-19 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c62ebb43-a191-3f4f-9344-4d2d2d2c5e9e | -10.69529 | -49.60664 | 2026-06-19 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15b27fca-3bd8-3ba0-ad32-1eb52c7f245d | -10.12557 | -52.17688 | 2026-06-19 05:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f097cc3-e6a7-35b3-b675-e0cf93f98923 | -11.48083 | -57.11208 | 2026-06-19 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f5efafd-4671-3422-a957-72a7b9f074a1 | -11.78526 | -57.00291 | 2026-06-19 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f278ee57-d0c0-3318-95b4-f7efc37a4105 | -10.06371 | -48.08551 | 2026-06-19 05:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 726dff4e-7597-3069-a6cd-e3d19d267ccb | -12.14711 | -48.45393 | 2026-06-19 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 783d58aa-b950-3b26-8d1f-bde8f50cd685 | -11.6671 | -56.76337 | 2026-06-19 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 702cf0cb-03bc-3a2a-bc68-5f87ec0f81ab | -10.55552 | -46.32661 | 2026-06-19 05:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a19a3c8-3c40-3fb2-9c2f-d75851ef9fbb | -13.50028 | -56.57721 | 2026-06-19 05:23:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e00951f-793e-3c2f-ad36-f69d10d5bf65 | -11.48021 | -57.11623 | 2026-06-19 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17d51cd0-c6fe-3665-a0cb-017829f59481 | -14.2135 | -54.70325 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c682d23-3b01-3602-9a0d-fc586b02dbbf | -10.53787 | -47.71527 | 2026-06-19 05:23:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fb490cb-ea63-35ed-9821-767a37d8665d | -13.93497 | -53.55966 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1b4337a2-6e1a-386a-9c52-2074c616d1aa | -10.54508 | -47.71004 | 2026-06-19 05:23:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae638df3-0b9f-3397-bfd0-33ab49d0e072 | -10.71964 | -56.04277 | 2026-06-19 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94637efe-d8d9-3bc4-a923-0f3210760718 | -10.69478 | -49.61075 | 2026-06-19 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bb063fb-6353-361e-8e00-525c0d458f4c | -10.55472 | -46.33331 | 2026-06-19 05:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0484029d-a498-32c6-9d50-a5472472efb6 | -10.15318 | -56.62181 | 2026-06-19 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65f58734-0aab-3c19-ae95-78662caabacb | -11.62684 | -55.18353 | 2026-06-19 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1fd6e9c9-015d-395c-9a3c-04c67535a998 | -14.20529 | -54.71249 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8269189-e9c8-3d1c-a167-c4ee62605ee7 | -12.13659 | -48.26419 | 2026-06-19 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 280a16e4-6a00-344b-8234-062f16284056 | -12.9168 | -49.48127 | 2026-06-19 05:23:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7375e6e1-ec2e-32b2-9084-3c131bfb82ff | -10.16217 | -56.61656 | 2026-06-19 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad15c91a-ab37-30e9-a310-24c3063e07c2 | -11.31134 | -51.41426 | 2026-06-19 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfb4ae16-b74e-3e30-b8ad-298eac310858 | -11.48145 | -57.10792 | 2026-06-19 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c835ff88-a90d-3cf8-9cdf-3f29898416f6 | -11.78588 | -56.99868 | 2026-06-19 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9415d342-c92d-3f67-94b5-d6ebf6a1cf88 | -10.06309 | -48.09061 | 2026-06-19 05:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b766a5de-75be-3e2c-8cd8-79135b13eb2b | -10.5531 | -46.3311 | 2026-06-19 05:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f78143ea-5917-3cdb-8b08-53db3e64e1b5 | -10.15793 | -56.62024 | 2026-06-19 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 849f00ab-4858-3814-8c05-bad837903f43 | -11.72385 | -54.49282 | 2026-06-19 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c80e349-4637-3307-bd73-fd511acf7d9a | -12.13019 | -48.26345 | 2026-06-19 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9a3a654e-ce66-3785-8f0d-d85592cf470d | -11.51193 | -56.11985 | 2026-06-19 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29c01448-203f-3e5e-88b6-33776b601caf | -9.75289 | -47.87592 | 2026-06-19 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0255427-0249-38eb-8796-d4c300f552b0 | -11.52339 | -54.25963 | 2026-06-19 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8d70c09-5cc4-3127-9508-031db65b5cc4 | -10.04982 | -48.09452 | 2026-06-19 05:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f54754e-b4e2-3f47-8b9d-33a1514f0e88 | -13.93901 | -53.55785 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 576653f3-dc46-355c-adc1-2827a2f70898 | -10.71522 | -60.75587 | 2026-06-19 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25c012de-96b7-320e-aea3-8b02ab8051c1 | -21.26972 | -56.03464 | 2026-06-19 05:23:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc34bf52-568d-3fae-acc1-1e1cee5d2d61 | -10.16106 | -56.61869 | 2026-06-19 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be005f6b-e1b7-3307-bf62-9ba91d0692a5 | -11.61425 | -55.32948 | 2026-06-19 05:23:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1dad929-c38a-3a6a-b9a4-86c70c175ad5 | -13.93777 | -53.5677 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d02e13b3-c30f-3f96-aa7b-920f6c13a869 | -12.13078 | -48.25822 | 2026-06-19 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d65b7bb-19c2-3f1f-93f1-78009ede9786 | -13.49453 | -47.50399 | 2026-06-19 05:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67d757e8-1ee7-372e-8bda-741caf8a53d8 | -10.57428 | -57.32532 | 2026-06-19 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22b537c9-428e-3166-8a3e-c34fe108d67c | -11.33548 | -48.00166 | 2026-06-19 05:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d408e985-1248-3585-95c7-e4a954ee3fde | -13.93839 | -53.56277 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4c6abbe9-31a7-388d-9de6-b0c2b37a4257 | -11.62283 | -55.18295 | 2026-06-19 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 563fbc74-5b42-38bf-9696-4de63df4f8b2 | -19.92511 | -56.86395 | 2026-06-19 05:23:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 652fc745-3885-39e4-8791-f6e23ae41b39 | -12.27006 | -58.18724 | 2026-06-19 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e6d1a91-147c-3804-94d8-13a7526b403b | -12.91926 | -49.48487 | 2026-06-19 05:23:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ea33c5d-9411-3ce8-ba38-04cd82fa6270 | -18.97425 | -52.4509 | 2026-06-19 05:23:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 773cddcb-826c-38c1-abfb-7de6fcccade8 | -10.06252 | -48.09527 | 2026-06-19 05:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7412298-c427-3a19-8405-1920d74eccf0 | -10.14956 | -56.62128 | 2026-06-19 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c418f7f-cf32-3eb3-ab55-92517dac379f | -12.55074 | -54.59029 | 2026-06-19 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| baca1f81-9eb2-3b04-b138-505052cd760e | -11.31295 | -51.41508 | 2026-06-19 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92165119-2aa8-3f58-9fbf-6bd13ac7afe6 | -14.20761 | -54.71505 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a062e2d-af24-3883-af7a-6972b8ff03d4 | -11.91523 | -55.91526 | 2026-06-19 05:23:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d13da730-8ceb-38d8-be40-79b181254017 | -10.69453 | -49.60791 | 2026-06-19 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a824e0e7-0e21-3c42-8a53-84c6c6ca12dc | -10.05612 | -48.09531 | 2026-06-19 05:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 91533db1-4bf0-3091-9753-2f03cf547468 | -11.30779 | -51.41438 | 2026-06-19 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69fed4a6-e5a5-3469-bc2e-683a1194d8d9 | -9.21025 | -64.09066 | 2026-06-19 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10a27df2-3a89-3596-8177-2500e2645e31 | -11.78226 | -56.9981 | 2026-06-19 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 55ce09ab-4de5-3c2e-a49b-366cd671e8ec | -10.72358 | -60.74637 | 2026-06-19 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f1d24b1-4082-33c0-86a8-a1ab4ab86738 | -13.93432 | -53.56457 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2985a312-c432-3a9e-b7a9-762f4f340884 | -14.21782 | -54.70376 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51192941-8823-3193-8e19-dad5268bf1a5 | -13.49717 | -56.57192 | 2026-06-19 05:23:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82da596c-45c2-32b1-adf5-398a8bb773a2 | -10.12586 | -52.18074 | 2026-06-19 05:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7528d62-b323-3526-9697-b05421abe243 | -13.93377 | -53.56211 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 52f505ce-ab39-38ce-83fe-dd144893d646 | -13.48704 | -47.50947 | 2026-06-19 05:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bfefc43-c72b-35d3-b290-2ac4d8861e79 | -11.66181 | -51.357 | 2026-06-19 05:23:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de685006-c2af-3349-9c7c-14435dd46eaf | -13.94302 | -53.56342 | 2026-06-19 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8e81150-e431-30a1-a1ac-cf5b9666d3f4 | -12.13514 | -48.26268 | 2026-06-19 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9ed6aa1f-e57b-3f73-af55-4bc58564d41d | -10.55385 | -46.32451 | 2026-06-19 05:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 450af04f-a905-336e-b454-4697b6c9cf5c | -12.54704 | -54.58573 | 2026-06-19 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README12.md)
