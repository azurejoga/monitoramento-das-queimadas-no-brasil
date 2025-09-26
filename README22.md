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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 051a1f48-95df-340c-8ff0-50ec169fc761 | -14.13425 | -51.20515 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d3bad1b-78cf-3153-8f15-97f79091f873 | -13.25992 | -50.66605 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d54f5aa1-930d-3a44-a8f1-9048c4ee2975 | -12.34056 | -47.99041 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6bda144-8d5c-3cb3-b312-0d0b7ec768db | -13.71304 | -42.68915 | 2025-09-26 04:17:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 29f04abb-8d22-3aad-9a68-e9e2be086642 | -12.87051 | -47.09587 | 2025-09-26 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d4b17b74-b339-328b-86d8-dae6b25e24e0 | -14.87963 | -45.54443 | 2025-09-26 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be4a3139-647f-3dfd-87f4-40052d333bbe | -14.15263 | -46.97805 | 2025-09-26 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b86f9c8-4a98-3caf-b8f0-39529e196559 | -14.94465 | -47.50097 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4aa2ff2-4cbc-3863-84c7-1e06fcd32481 | -15.92683 | -57.49439 | 2025-09-26 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 204b384c-4fc7-3a7f-9a1c-7139c5543161 | -15.0275 | -46.94286 | 2025-09-26 04:17:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75bd79f3-83c5-3cb2-be8e-4cb0f7575d5e | -12.05917 | -44.8492 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 660b2f3c-6f68-361b-a1f7-215a82978a6d | -14.82432 | -52.92271 | 2025-09-26 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a28c0516-105c-35d1-9e96-437e74490469 | -11.4223 | -44.96108 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ac5b12d-a12a-3bcf-850e-3b17af22a790 | -12.05476 | -44.85569 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e2117c1-dcde-3738-9624-ba9c38522245 | -13.24576 | -50.69653 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19f13be7-7394-37c6-89c0-fe54a0471443 | -12.05254 | -44.86976 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 403a0c81-a8b0-3089-abe4-36a3abeedbba | -11.25373 | -45.54605 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb2e2fa4-a07a-3e0d-9505-202140a0d3ea | -11.41819 | -44.964 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 536c92b6-fd51-38e1-bd1f-e2a9057466dd | -11.95757 | -47.87889 | 2025-09-26 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ea75a9d6-5630-3c13-a7c2-5ad5a247dc04 | -12.62099 | -48.13377 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 94d4e6c1-4751-3115-8633-b9e115b14565 | -15.13062 | -46.42054 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99280c66-83b6-3410-bfcc-c783c65036ba | -15.26012 | -46.44242 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ab51e2c-1001-3a8b-a3bb-7152b79cccdc | -13.94477 | -44.09923 | 2025-09-26 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 888cad09-dc88-3ed8-a301-02300bba5a96 | -21.00069 | -50.00507 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e4c5ed4a-53fd-3c9c-8c67-12b6b29072db | -11.24312 | -45.548 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4a10e3a3-5508-39fd-960d-2f5620c2ad94 | -11.07311 | -48.36113 | 2025-09-26 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97dcea98-10b6-383d-88ca-600fcd3fb088 | -15.51543 | -50.43689 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f1def52a-efea-3e53-9036-2641476fd6d8 | -13.84775 | -45.61281 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e764c99d-f285-3caf-b4e4-497dea283af1 | -13.84387 | -45.61581 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8d6cfcf-8560-3c27-b17e-27d77cfc0938 | -11.42227 | -44.98263 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e88aec1-a55b-36d1-90b3-bd464a2f34dc | -13.28435 | -50.69992 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8eb1871-3a08-38c4-a306-3a67317fe33e | -11.67744 | -44.4424 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8173448f-9cd9-3cef-869f-663dabaacf9b | -12.87446 | -44.70539 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b18e5c2-d852-3e1d-90bb-cbe5d1f4716c | -15.26778 | -51.4657 | 2025-09-26 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb5f73d3-d6bb-37bd-b72f-febc7198d832 | -11.00905 | -44.34474 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0e7c387-751a-3207-8627-ee8aede10746 | -22.60242 | -49.03323 | 2025-09-26 04:17:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ed357d28-f4be-3a1e-aa43-ec413238262c | -13.94777 | -49.25654 | 2025-09-26 04:17:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38b448a5-7aa9-3e8c-9ba8-6ffed104d737 | -11.38347 | -44.94751 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c517ffea-fca9-34a5-a28c-d838b3bc3d3c | -11.42669 | -44.97618 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| acbdd2f6-a60b-3d7f-82d4-260b7a554d17 | -15.26754 | -46.41777 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e668200-f154-3c83-b27f-45788bf680b8 | -11.63881 | -45.37449 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d82071b5-7420-3a62-afb3-44ae11e445ac | -11.43999 | -44.93515 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 175b397c-e742-35fb-a2c8-0c5c111197c1 | -14.96217 | -46.76289 | 2025-09-26 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68b06b58-9f64-3418-a729-7ba08e65746d | -14.57518 | -51.40753 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec898c19-8442-3254-a30b-5bc4e96cd042 | -14.03601 | -45.498 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 986d5a45-389a-330a-97fb-5ba4bd29ef2e | -14.34278 | -44.49604 | 2025-09-26 04:17:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cec8136-5ea4-386a-9cd2-3bfcc2d00710 | -11.38733 | -44.94455 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcc64dd9-b282-38c0-9b89-f2fa1cd9ec35 | -16.89675 | -47.97036 | 2025-09-26 04:17:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22e463f9-7a3d-33bb-afa1-b20519307a6f | -11.0217 | -44.35035 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da1732f6-da83-37e0-b8e5-da26bbc040ea | -20.99192 | -50.0126 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 45e479ba-32c5-3dca-9824-e5a90e1cfa3f | -14.75933 | -48.35946 | 2025-09-26 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d96af36-b3a4-3e0d-9516-025e1d6d58be | -11.41438 | -44.92368 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76b8284a-208e-3200-a4dc-b7a1d5eab955 | -11.9612 | -47.87951 | 2025-09-26 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6f52c206-1fe3-3507-bfec-9dcee07a3675 | -11.24865 | -45.5563 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| a2448dab-4856-370e-9f59-5f3b268409a6 | -21.01193 | -50.02583 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dde8ff18-c9d2-33ea-9df4-dab9de030709 | -15.38844 | -46.11098 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2551f96-3105-3278-bd8e-bbe9e97769ac | -16.85153 | -50.51932 | 2025-09-26 04:17:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 77f3c072-3627-3961-acb8-ee809880d471 | -11.61197 | -44.42421 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f6582934-d9f2-3694-a25a-7a46e26f7771 | -14.9481 | -47.50161 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43682421-32c2-388e-9f89-e4d0144ae00a | -11.61859 | -44.42935 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dacbebfb-da92-3bd2-8e37-fedaf2f06504 | -11.60923 | -44.4417 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b12af8b-3ccc-3dfd-ad90-535d87a1a02d | -22.41366 | -50.64077 | 2025-09-26 04:17:00 | NOAA-21 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e0e0f502-56c6-30de-b7fb-d31365ba90f3 | -11.96194 | -47.87514 | 2025-09-26 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 93b382ab-f0f9-3ae0-b822-44a05b0e1c34 | -15.37636 | -48.6006 | 2025-09-26 04:17:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 773fcd3c-4ab5-3cbd-972f-d801248b07c3 | -13.8538 | -45.61747 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eefcfb3f-cb25-3bf1-8f7d-f2747ff9ac0a | -16.51406 | -50.10201 | 2025-09-26 04:17:00 | NOAA-21 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22132a04-fb42-3fe7-ad2b-167783c6a957 | -22.17067 | -48.79684 | 2025-09-26 04:17:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f50a51db-06c1-3b5f-99f1-9a52762d3efa | -11.23193 | -45.55356 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a389db3a-3b73-3136-b813-c6974daa0051 | -11.22684 | -45.56381 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 916d93fe-b248-39e0-b729-9a111bae1c3e | -13.2473 | -50.66369 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81838f0d-065c-3098-8029-2b12c84487e4 | -12.3741 | -44.14149 | 2025-09-26 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e81a52f4-7323-3874-ad05-9561f6b1979e | -11.24036 | -45.54386 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 63686b34-6f50-3bfc-922b-10ec20fe08c5 | -11.61474 | -44.43232 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| de7cc4ff-80be-3a65-8b3a-af13755ae817 | -20.99271 | -50.00812 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e3032cec-49e0-3238-b699-1a7d049361f4 | -15.89538 | -59.33555 | 2025-09-26 04:17:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c4f76dd-9de6-3baa-9971-f4358591ca4f | -11.98001 | -46.61176 | 2025-09-26 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 582b105f-7375-3cb2-bae5-f4c1e71561de | -15.51423 | -50.42102 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6813d84-6fa9-3f87-8749-8ec7f4bf5da5 | -15.90232 | -59.33675 | 2025-09-26 04:17:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89a62641-f440-3eb5-8dc9-0db98f7d5d26 | -21.0055 | -50.02001 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2cd6eb46-4ea7-3b13-908d-5a60248b7fc2 | -16.85438 | -50.5036 | 2025-09-26 04:17:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c8b6fd34-77a8-3b7b-81f5-009a18ee7805 | -11.4278 | -44.96915 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4495f214-d401-3751-9221-91f2b6443187 | -12.56808 | -45.84475 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45a44a0b-163c-350b-b179-7bd9f0409573 | -11.24138 | -45.55881 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c95d885a-623d-3923-b1b6-cccd1c92fa88 | -15.07328 | -44.98291 | 2025-09-26 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fffdbe33-5a6c-3b7c-913f-5fe9b8687f99 | -11.60977 | -44.4382 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5200ecc8-7c73-3e3d-962c-2fde29d6ab3c | -15.2642 | -46.41722 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 489fc63b-e299-3fac-9f7e-c89ae7138513 | -16.85928 | -50.49901 | 2025-09-26 04:17:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 21512b91-5bc9-39c7-ae34-505f50d33dd1 | -12.13344 | -47.95105 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df9b0552-f472-3e7a-b427-29083d6b23a4 | -13.85769 | -45.61446 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa4e3c98-393d-3587-81c7-e7b98e6d5716 | -14.11266 | -51.15349 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5572edb-2969-3a28-a06d-4750be0b5a72 | -15.51286 | -50.42846 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ed71c12-a75a-30b4-87d5-3823fb4776ce | -11.01565 | -44.3458 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8737f18-77b0-3713-b9dd-4e60b966c7ab | -12.37083 | -44.16258 | 2025-09-26 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39c46ceb-ba66-3462-87be-2502b55e0a76 | -15.88866 | -59.3334 | 2025-09-26 04:17:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fee8045-78d2-3201-8abe-cd899173e7cb | -15.36795 | -43.74227 | 2025-09-26 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 18cb26dc-15da-3aeb-9fe1-63748c4d9b38 | -16.85831 | -50.50434 | 2025-09-26 04:17:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 1ac0bd05-42ff-360d-913c-1a42b7d3f32e | -11.38402 | -44.94402 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3512cc1-bd9a-305b-81b2-95feb8a5558e | -21.01679 | -51.10884 | 2025-09-26 04:17:00 | NOAA-21 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1dee7ab0-6ec2-3fe3-a944-e702882a9d60 | -11.61584 | -44.42532 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a9f56ac-556a-3b14-8802-bb91075473da | -13.24658 | -50.66769 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README23.md)
