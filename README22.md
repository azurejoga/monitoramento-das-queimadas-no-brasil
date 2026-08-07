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
| 215558fb-3491-3b6b-a196-2a5d58e89bc0 | -7.03775 | -56.50929 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4025116f-057d-36a7-816d-dcc86949006f | -11.14405 | -44.48738 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bed3c9b0-b9f7-3da2-a833-95ca2291b557 | -12.86937 | -52.81738 | 2026-08-07 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1460d0b3-e92a-3788-bf0f-f60d2ee9e944 | -6.7227 | -58.93076 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85ca37fa-dd01-3460-a93b-88f0fb1c8455 | -11.7266 | -56.84483 | 2026-08-07 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a99e8da7-dc94-3449-a78c-96e21863da63 | -13.78333 | -49.72229 | 2026-08-07 05:04:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 026201f9-292a-3ea7-a6bb-2064770fe050 | -12.14153 | -48.26603 | 2026-08-07 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18886dc0-0936-3353-bb67-c4f988536dd9 | -9.48812 | -57.32053 | 2026-08-07 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e02cf1ba-d125-37c2-8a59-56e6f5a273f5 | -10.94028 | -57.17376 | 2026-08-07 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb94f807-b786-364a-b24d-97f31e4477b0 | -12.00112 | -45.13335 | 2026-08-07 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d356f0da-4598-3085-9b00-9876733d9113 | -14.26807 | -45.29948 | 2026-08-07 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62616fab-b682-3c44-824d-1c93bee520e6 | -11.19794 | -54.8502 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bbad280-3a74-3d98-82bc-f22f8252099f | -6.53664 | -55.17463 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce4839ed-e02d-3192-85b4-3db519e185d0 | -11.15607 | -54.8577 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56fa3df7-fa46-322a-ac41-712b42d88771 | -11.12513 | -54.90334 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9bb8a81-324f-336e-ba27-5c0e49f8b591 | -5.98028 | -52.15393 | 2026-08-07 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9b9fe3a-465a-3b4f-8723-8ea6aa0c025e | -11.13121 | -54.90791 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef6bdb1e-f260-3a55-aa66-432359e948c1 | -12.55653 | -46.94281 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0ac21cb3-b6b8-3d3d-a6f8-4503ecb965b4 | -11.18649 | -54.85897 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfd118fa-0527-3f4e-907a-0aeb4f9620e7 | -12.42461 | -50.54964 | 2026-08-07 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efc866e6-9a15-36b1-8d74-3aa562f97e41 | -6.64407 | -56.4278 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f95c62c-0b2c-3403-bd6d-ad0f3265c19f | -14.43129 | -45.67795 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed3fdb01-55cf-359d-92ad-21ddf57411ad | -11.18759 | -54.85191 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17ea0015-2493-3d0a-a7a9-370e89d83a52 | -11.17819 | -54.84679 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8228e441-a26e-36e7-92a5-f30a59896e00 | -11.24716 | -54.83998 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ec7d97a-0af0-3016-95de-e62d1517254f | -13.9601 | -47.36557 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6909ab0-472f-3e89-b88b-951706583d7e | -6.71882 | -58.93011 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bd945eb-f952-3ccf-988d-261f15c071c6 | -13.96555 | -47.38375 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09238e8f-ed2e-3cdf-8f02-587bf4f98f10 | -6.60772 | -56.34918 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78c34c95-ba58-3e92-9dd1-921feb2ce16f | -11.12181 | -54.9028 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a986e8eb-71f5-31ec-b7aa-25105094b0a0 | -10.93235 | -57.17678 | 2026-08-07 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a0dbc493-3018-333d-87aa-37984f9decd5 | -12.63175 | -46.89155 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d757cf1-5454-3271-9a78-5aad6401a3aa | -8.33521 | -46.39432 | 2026-08-07 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14af5a39-0456-345c-83cc-32cd489e032f | -6.71209 | -58.94217 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb5b0328-62fe-36b3-bc1a-16642ce5f4cf | -13.77501 | -47.18027 | 2026-08-07 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 008807a9-8158-3acc-b024-30f98b5f1a9b | -12.57273 | -46.89733 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e08b093b-cc95-3cba-9771-199fbbe45e12 | -6.73237 | -58.5808 | 2026-08-07 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5da8a0ac-84c4-374f-9a66-8f6959c36ee5 | -6.55244 | -56.25694 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07c5756e-5557-3991-8fd0-96e535ab9f0a | -11.1481 | -44.47766 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 285a550d-91ed-3be0-b84f-be9d0e8e14be | -13.93443 | -47.36187 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0dad94a7-52e9-37cb-bc13-16516ab0225a | -6.55304 | -56.25325 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebe754bb-07d4-3bd5-8627-015a4fd939e2 | -8.79011 | -47.4259 | 2026-08-07 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42a871a3-1e27-3e54-a079-07376685fb29 | -11.19534 | -54.84591 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ee97ae2e-cd34-388f-865b-6f0fa162b4c3 | -8.49329 | -54.77259 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1cb1971b-3929-36d3-8f47-12842f8fe511 | -11.15167 | -54.90756 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03fb2970-5d5a-3806-b808-726246813fff | -11.4559 | -44.56207 | 2026-08-07 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f617d25-100c-3b69-8674-ea1b0b81d8e9 | -6.54387 | -55.15069 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79e58785-203c-3196-b9fe-e2f5c07e0ddc | -14.42692 | -45.66473 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 350c1c5c-3e20-37b5-92b8-182ec83c63ce | -12.8622 | -52.81629 | 2026-08-07 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adcf0a8f-e64e-302d-b6ae-1e3815b62a94 | -6.54661 | -55.17621 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2214e4c-ffcc-3485-8336-9e0b396c0a55 | -6.54606 | -55.1797 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8774062-ce19-35a8-a45a-c9d585d64737 | -13.93916 | -47.36583 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a24a31ca-2ecc-3d93-818b-d699ee4f325d | -7.03433 | -56.50874 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5591e1f4-3d20-361a-928a-79c06a4e1d3a | -6.54775 | -55.14774 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a0de43c-9174-30f2-9671-ed03c405ae8e | -11.13808 | -44.48652 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| def4ba25-8dbb-38ff-8b88-71b869bde3d6 | -7.23912 | -60.64546 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cffbfd5b-89a6-398f-ac69-83deee510d11 | -13.95963 | -47.36931 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51d11902-5285-30c2-82e3-3673d278385a | -6.95054 | -56.37679 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8a2603f6-51c4-3abd-9f8e-e27a1b1144d8 | -6.53729 | -56.5456 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e249c0c-42ab-3314-89de-b38f1367d2e9 | -13.00419 | -42.67335 | 2026-08-07 05:04:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 927e37f2-1dfd-3381-af96-bacafdd7a211 | -11.19368 | -54.8565 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19479aa9-c424-3895-9695-f9f701e75f58 | -8.53522 | -49.55769 | 2026-08-07 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d267b0b7-f84f-335e-a72c-83780ac09664 | -8.02403 | -55.11732 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bbe75aa-a54b-3454-b2ee-28bea682f43e | -6.72704 | -58.58937 | 2026-08-07 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 778baeb6-bb0c-3c6e-9243-db45213cd87e | -11.19903 | -54.84313 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a7d2ec4-6287-3fd7-89c9-921f002b973c | -6.53324 | -56.54882 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6e62faf-65e3-37f6-9009-f1713d6f2acf | -12.51824 | -55.7845 | 2026-08-07 05:04:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 67c6a80a-db27-3ce4-8763-f012e9c0ebfb | -6.72536 | -58.93433 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1b10b1e-8c0f-3b34-9e03-caac7e983a5f | -11.14393 | -54.91354 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69fee9cf-f491-3164-ab05-e4330afc420e | -6.54055 | -55.15017 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7fc3508-6d49-3eb9-affa-875759f7d260 | -12.51493 | -55.78395 | 2026-08-07 05:04:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f887037-37b9-323c-a4e8-566ea39d3c1b | -11.12458 | -54.90685 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a9d2f65-3838-3c75-8b42-09e1b6c695ae | -11.14835 | -54.90703 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 401ed323-64fc-364b-859b-c651b61ab267 | -14.42113 | -45.66405 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe4636ca-b1d1-3305-9be0-e7bda56676cc | -12.86517 | -52.82102 | 2026-08-07 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eda5b709-ee58-3e11-bc0c-f1b7b32e0e23 | -11.13066 | -54.91143 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1867a2be-d371-3250-8099-89fc420d13c2 | -12.3308 | -53.16491 | 2026-08-07 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 177f54dc-f487-340a-9b07-475a1af00802 | -10.63596 | -47.48843 | 2026-08-07 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3df75f3-ac4f-3e3a-9fe2-9b5b0f39405a | -9.28872 | -60.94485 | 2026-08-07 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f9ec4eb-6206-35f4-915d-436a63942b55 | -6.86321 | -56.56986 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e607814-d18d-3902-bfa4-e8ee363550e9 | -9.18315 | -58.07164 | 2026-08-07 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb9f3e9a-8a11-35d3-986e-72e64d748b2d | -6.60359 | -56.3525 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da1424e6-4d24-3d45-8fb5-92fc18f739f2 | -6.85425 | -46.00454 | 2026-08-07 05:04:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b79be8e-eabb-3b35-a845-302808c8027b | -6.54903 | -56.25639 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2b35908-1043-395e-bbf9-83b6c001f0cc | -11.18095 | -54.85086 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70df104f-6709-38f5-9ec5-3895b359c60a | -12.63225 | -46.89198 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a77082c5-b022-3893-bec2-98a667aba72a | -11.31859 | -45.20919 | 2026-08-07 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aa4db96-aa86-3335-9b66-77463900f16d | -6.64308 | -56.41225 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3fd1a13-efff-371a-a04f-2875e98b9cb4 | -12.87295 | -52.81792 | 2026-08-07 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8bbccc6-5409-3971-b292-460921f7b1ce | -11.12955 | -54.89682 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b0593f8-2239-3f6b-92b8-7d71798513c1 | -14.26857 | -45.2951 | 2026-08-07 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29dd3fe0-45f3-3e3c-a5b4-57c1e6639c4b | -14.41973 | -45.67647 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f09d561-b153-3d86-b017-d5ddf88ddd68 | -6.70579 | -58.95615 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b702396-414a-34fe-b77f-b80cb0851f12 | -11.14105 | -44.48577 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f329079b-b8e7-3445-b7dd-362154eef5f0 | -11.14503 | -54.90651 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 380e192f-84f9-375a-a1a8-21d79f19d976 | -6.41728 | -55.79079 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad562aa8-c18e-371a-bf02-6cd15c51c3f1 | -14.42066 | -45.66822 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 116fd883-d0be-337d-ba84-beebc3b53fe5 | -6.85888 | -46.00851 | 2026-08-07 05:04:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f4816ffe-94e2-3a34-9290-217ba502f799 | -6.54426 | -55.29797 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16c50e43-27c9-3776-b880-dac11e14608f | -6.95067 | -59.5188 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README23.md)
