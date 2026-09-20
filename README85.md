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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5b4cdfe-0e90-371c-af6f-2f7f8f2fe077 | -3.36245 | -50.4485 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 51457dc9-c3c3-3ba5-86bf-538ae75a58ec | -8.22595 | -62.8412 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f0b7b04c-64f5-30c2-a238-08dfd9e7e45c | -3.01153 | -54.17915 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e100ee70-acc7-3700-bea7-fb8063d58588 | -2.89306 | -57.82556 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43cf9d95-fcee-3bb9-a708-f052aa9fd2fe | -6.62373 | -57.98025 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ad2338f-9ec1-3d17-96fd-f38cff9d06fb | -2.8204 | -54.71709 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67d42cd8-9c61-35f0-bbf0-d1e70f877bfb | -3.35704 | -50.44815 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f75239f2-e549-3aaa-a0fa-32080d06557b | -2.61553 | -54.75146 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e42b309-9b5d-3e8c-9609-4a98cb4b3fca | -3.34952 | -59.82716 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7db6a86a-f56b-3e00-a50a-3c961ff6fa52 | -8.77105 | -48.72372 | 2026-09-20 05:23:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9fcd5db9-eafa-3322-9afa-959c4e521be3 | -9.18997 | -60.76511 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd73cd70-b4bd-36de-9cc9-e9c30d0b43c8 | -10.78096 | -50.87796 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 666f05b9-9253-36b1-bd25-a36e4763b80e | -8.76422 | -48.67014 | 2026-09-20 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 658576c8-3aba-35bd-88d1-510ce1def6c4 | -3.73952 | -51.82057 | 2026-09-20 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| c2bb4562-a3eb-3f0b-a1ef-3f2f6b4081ae | -3.7602 | -55.95979 | 2026-09-20 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2f94839-7c72-32dd-9895-145d1a8c0de2 | -6.4354 | -59.97618 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1a64067-5d61-36bc-9263-c87f7b5bdfde | -2.45302 | -49.21786 | 2026-09-20 05:23:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 91127ac0-afc5-32de-8372-85e46eb5b348 | -6.44976 | -58.15298 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53076d6e-1d7a-30f8-beae-56413c2c094e | -8.17521 | -54.77573 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcc94ca7-b08c-346f-b89d-a72b18923465 | 4.35847 | -60.31976 | 2026-09-20 05:23:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fe987a0-4b3b-3c31-b6c5-87c9bae947ed | -6.35727 | -58.30734 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 926364cf-41ac-3c9a-8b71-425fd21a7649 | -2.71725 | -57.96308 | 2026-09-20 05:23:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5879cdb-64a8-3e85-bc52-b7f7d76749f6 | -2.82751 | -50.47302 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c9b5d1e-0135-3f9c-8548-c64f3b4ce133 | -3.08602 | -61.18642 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7cd332b-b316-38dc-81a5-4a7ee2f68387 | -9.17287 | -51.513 | 2026-09-20 05:23:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 179088e3-7380-3afd-b53f-55d7e211118e | 0.01108 | -60.60725 | 2026-09-20 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1dc077a-fa9b-3bfb-893d-f5875e4239fb | -6.13486 | -59.94013 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f376ecb-b468-3273-8911-320bde47f8d6 | -6.20119 | -57.78035 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab9a5f1e-8d52-37d0-8131-739eb2db0fa4 | -6.15342 | -62.61883 | 2026-09-20 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa550d11-4728-30f9-b939-3df76bc32a5f | -3.90217 | -49.0722 | 2026-09-20 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5d943ee1-84dd-3439-b128-3d739e1376f8 | -3.0514 | -61.27544 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55c0346d-4bc9-30b8-996c-150e6474780d | -6.13378 | -59.94709 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92b18613-1293-369f-9ea0-cb2828f6e1e1 | -3.08483 | -61.08513 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48a841a8-e63b-3887-b791-4527c04f5cc8 | -3.34302 | -57.86146 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3da209ba-4965-334f-9553-6c6f7ec413d9 | -3.11232 | -61.40511 | 2026-09-20 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af5fcd94-6034-338f-891f-4181a6a6c8a9 | -1.42873 | -60.23315 | 2026-09-20 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baadb417-deca-3fe1-8e47-824c3e241745 | -8.17443 | -54.74912 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c006911e-69cb-358b-a344-34d16ae480cc | -1.25566 | -55.76561 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 340f220e-2afd-343a-98ad-868ff079bbdc | -3.77929 | -49.76885 | 2026-09-20 05:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 36cce3dd-22f0-31bb-b50e-86cfbeabbd4b | -7.00287 | -62.95136 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a827d38d-cae5-3e9b-ba84-8e1d4af2af01 | -8.22815 | -62.84907 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2000e1f-b1bc-316a-a25b-165883d6ef30 | -3.03634 | -61.24038 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7a61ba7-68ae-3bfc-b33e-8d819b4d288d | -2.79473 | -59.89456 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce586223-4641-3d22-b398-81368f211fb8 | -2.58802 | -59.41188 | 2026-09-20 05:23:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c11e4249-5cc0-369f-bb17-24d2caeb253f | -3.35812 | -59.86357 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33e7115c-eff8-3940-9c17-275cd4f6ac18 | -7.57108 | -57.67423 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c6bf9f3-29dc-326f-81c2-ab085274e733 | -10.30877 | -50.25377 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 96f899f1-b786-34c9-a202-dee3f8156495 | -2.98216 | -54.77727 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9d984f4-ab98-32aa-858d-a23b12b8412b | -9.19814 | -60.22456 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10dd5f4f-fbc1-3d9f-904d-18e62293ed24 | -3.48001 | -58.36685 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f91dfea-6bab-3e30-a897-c6cfb7027b22 | -7.60275 | -55.70902 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 512980ab-18e9-347e-8a5e-29bf3d5783e7 | -8.17081 | -54.77508 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08307053-e027-3117-958e-3473bcb7f21d | -3.20071 | -61.12812 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b18399e-31f4-3e00-85de-fc2539c77514 | -3.16577 | -48.6104 | 2026-09-20 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0adb1dc6-fb02-306b-85a9-056ff3440844 | -10.3149 | -50.25458 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 725b9fa1-12a3-3e3c-98ce-1a1c8a5e3b62 | -9.66148 | -54.32221 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c792a00-4bc5-307f-9562-cb9bdf556c34 | -8.61621 | -54.60669 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db410b0f-86fe-3576-983c-7b9c4cb53d6d | -8.17123 | -54.73986 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 564f4d7c-0705-3a4f-9b9a-1d9cefdd4443 | -3.14144 | -57.67317 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1df61d1-610e-33c2-935d-49a1c0ff1670 | -2.79526 | -59.89113 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d69faf1-1dee-3a44-90f3-8b95c13190a4 | -1.25395 | -55.76698 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c34a3e3-9465-31f4-909f-76352b878828 | -3.36135 | -50.45579 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c9e0378-4562-3354-9836-d7de9da40291 | -5.10088 | -47.5107 | 2026-09-20 05:23:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4153061f-42e1-3cb3-94b4-c9ba37a6fa67 | 3.6775 | -61.86863 | 2026-09-20 05:23:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f67ec29-24f7-30b1-b391-60309761a604 | -10.20901 | -53.92198 | 2026-09-20 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d122e73c-851c-3009-82cc-9334afbb29c0 | -1.2594 | -55.76612 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97e026d3-ccf0-365d-a5b4-1d1280bb51aa | -3.45295 | -58.39973 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d68de5e-cd4e-3b40-ad9f-84e8e24b309a | -7.31681 | -55.6167 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b262deab-cd33-33e4-938a-1653cbd1a9aa | -6.45253 | -59.97528 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c35762e1-0af1-3cb2-a1c4-497aea0c2672 | -9.19339 | -60.76567 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4395df89-ed97-3d38-b39c-74bb4f10b6a5 | -3.06536 | -61.07848 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a3d1d0b-7893-3615-a558-70da8361ca60 | -9.2733 | -48.24073 | 2026-09-20 05:23:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd2530ed-2a43-3127-b04a-066638abe059 | -10.3186 | -50.22599 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 40d11f4b-afe8-3c7e-b422-142fd6345058 | -3.42622 | -58.18993 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2c894a6-b333-3d97-86e7-c05bf480cd54 | -6.44801 | -58.16479 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86cf5d2a-08eb-380b-a513-13303e5e497e | -7.60223 | -55.71267 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce7b0f06-8323-3e13-aeb5-6109ce33b138 | -3.4535 | -58.21673 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24a519b2-604b-3e7b-8035-4943bc7e0c34 | -10.78466 | -50.8775 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d3683bca-2057-3fa8-b643-bc27f7b58ab8 | -2.61094 | -54.75448 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3a7985e2-83be-3a95-be8e-dbec3a47191f | -3.33623 | -59.80401 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b951608c-ee53-33e5-8e93-ca77281ea183 | -8.18004 | -54.74111 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 555aeae4-65e1-3877-8c9b-afa932bdc05d | -6.44257 | -59.97373 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03ec5ec6-a0bb-35c4-94e3-b0aba403c1e9 | -8.17883 | -54.74979 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bb5c26e-b059-3119-9b13-355772aa078f | -8.4201 | -54.72787 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0f1e1fb-f5af-3733-8abe-711e0c950626 | -7.589 | -55.68812 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f12f19d5-edb2-3afe-84a7-2ef1820f4f47 | -6.92461 | -63.06738 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf5ae69-eab8-3897-b35b-2a9b036f6fff | -1.43367 | -55.23787 | 2026-09-20 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c8ce3ae-7709-3337-a517-e110cb7462b9 | -8.22461 | -50.65127 | 2026-09-20 05:23:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcef422b-ba4d-3cbb-acde-024bcfce466e | -2.81633 | -54.71644 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb1e0797-c196-373d-ba70-72b715767504 | -2.4584 | -49.21133 | 2026-09-20 05:23:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bfb11e70-7d2a-3b2f-ad36-71ba297ce3c0 | -8.17641 | -54.76713 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5fd2f892-d623-3318-b66e-59717f536a43 | -1.22221 | -55.72522 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42316050-ed51-31dd-b125-85b43763d7d1 | -2.31191 | -48.40161 | 2026-09-20 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ada3543-8abc-37e6-83cf-9b8b4284036e | -3.1394 | -61.23436 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8fa219f4-a69b-3a69-a381-047faf8488ce | -3.59598 | -54.55039 | 2026-09-20 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ba0e405-dacf-3a6d-9556-868113eb88b0 | -2.65392 | -59.42626 | 2026-09-20 05:23:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99e519b1-55b5-32a8-947f-4ab0b76b1d8a | -10.29621 | -50.20366 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bff7c033-e803-337e-b62b-601806aa3694 | -3.45576 | -57.95112 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 165b7de4-c003-3a01-8e2f-913e2f2ae7ea | -2.68844 | -58.30629 | 2026-09-20 05:23:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb7df30e-7a9b-362a-ab80-a2256d7b4cf1 | -8.17761 | -54.75851 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README86.md)
