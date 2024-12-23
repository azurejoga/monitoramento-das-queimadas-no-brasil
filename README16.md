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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12889266-7c8c-31c9-9008-60637b420608 | -2.62516 | -54.02175 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41f8a290-7065-39c0-a020-595fd10a064e | -2.81767 | -48.08408 | 2024-12-23 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0859e6ed-922d-384b-ab20-6fa4ee0f22f1 | -1.08638 | -53.22464 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91648793-aabf-359b-a589-fafe65e9feac | -2.59264 | -46.86124 | 2024-12-23 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65f04fea-623f-3cf7-b27d-5e8035e0cbb4 | -2.8416 | -53.98476 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e538950e-392c-3dde-a3ec-05f4e69c8ca6 | -1.68023 | -54.45558 | 2024-12-23 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c662092b-370a-3872-92f9-cea15f065348 | -4.15125 | -43.65501 | 2024-12-23 04:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5d7fb94-ac67-3a9c-b9e7-95f75cf33338 | -0.20807 | -51.59761 | 2024-12-23 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c40d3f41-12fc-3a7c-9b8b-55b32c5b1822 | -2.98913 | -52.8534 | 2024-12-23 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c378abe5-1ee8-36b1-a550-b65c407277a9 | -2.52323 | -54.21656 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df7c6228-a375-3f2a-a2c6-9fc37983af5a | -2.36802 | -53.94994 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 649ab713-7f93-30cf-a0c2-d9405adbe7ba | -1.62949 | -45.84413 | 2024-12-23 04:53:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecc7d3e3-a91d-3f46-aecb-e68bba4c0b0b | 0.65192 | -59.74431 | 2024-12-23 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1f84204-b622-381a-ae81-79f0ce8b936a | -0.96469 | -46.84711 | 2024-12-23 04:53:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5450b77a-d8a9-3d3a-a0e6-343bac43948f | -3.90701 | -46.99511 | 2024-12-23 04:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2099d61-9db2-33dc-be07-2599cc9287c0 | -2.68605 | -51.86557 | 2024-12-23 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99aef8a7-9e4d-36e8-a280-c42931f21dac | -2.55175 | -54.77074 | 2024-12-23 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a037a83-bca6-3837-9099-c4b8392f6c83 | -0.21141 | -51.59812 | 2024-12-23 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8134c77a-faeb-3a5f-b020-410d27500ac9 | -3.77637 | -46.82722 | 2024-12-23 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 378a06b9-426a-3607-848f-ae8162a95fde | -3.10123 | -54.59971 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5db997be-1a09-3758-a631-8222ea97cab7 | -3.34974 | -47.11534 | 2024-12-23 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a35e6b8c-a048-33e8-bab9-23cbfdd57cc6 | -1.09601 | -54.22207 | 2024-12-23 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 248a3053-0e81-3a61-adcb-9f33cc7041a4 | -3.09787 | -54.59919 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1539e60f-4dd6-3247-a033-714d4a77f957 | -2.93427 | -52.81271 | 2024-12-23 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 440d748d-bf37-34d9-bef3-5610f97716c9 | -2.11382 | -45.4984 | 2024-12-23 04:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0255215b-b964-36a6-9fed-e89b0a831421 | -1.37637 | -55.13658 | 2024-12-23 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd0d8c21-5869-38ff-9359-539d207de78b | -2.40041 | -53.74549 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2234c12-623f-34f7-aafd-0446bfb71f56 | -2.57646 | -53.68394 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81cff7b3-7236-39a5-9239-ec09391a01dd | -2.12843 | -50.70052 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b7a903a-b26f-3853-b4a6-860e4a6fb31d | -2.62669 | -52.41325 | 2024-12-23 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a4d26e9-5920-3adc-af06-5198fd4a5ef4 | -2.54035 | -54.21235 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f26e9e5-0721-3d21-91ba-01c08167d547 | -2.89627 | -54.26117 | 2024-12-23 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ce111da-ad9f-3a72-b80e-de19c0aa8e94 | -2.81711 | -48.0877 | 2024-12-23 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73cf5f25-06e9-37c5-b4fc-24c5bd22b1d6 | -2.81943 | -52.98206 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc800b43-e59e-3f5d-a84d-7bbeced2bea1 | -2.67357 | -54.59872 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 747d81b1-d1a7-34aa-9f37-5f511f6d2c1d | -1.27458 | -52.69842 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 874b5fe6-23ff-3d21-9aa4-5b39f0e40318 | -1.57088 | -54.76785 | 2024-12-23 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8146f7fb-ea3c-32d7-bc36-e852814078f3 | -3.78621 | -47.11214 | 2024-12-23 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deaf7a0a-c578-38aa-903c-4ab46a6e8dbc | -2.48816 | -54.17884 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dba2dbc-88ad-3de7-a9ef-741a0991d6f6 | -3.10067 | -54.60327 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13e030d9-e008-3f57-aceb-49c3905f58d1 | -2.10883 | -53.50489 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7f3fc45-e7f6-37c3-bf6a-a8e4c6fd3495 | -4.04724 | -47.02245 | 2024-12-23 04:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab356556-83a9-3493-b41b-69163a6f4590 | -3.75129 | -47.19538 | 2024-12-23 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c944c68-189e-3d35-b9be-094eade948ef | -3.18815 | -50.56102 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0762266c-a6b5-3842-a71f-f12c4777fe6d | -2.49685 | -51.80728 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec39aefa-a025-3ac0-8800-d40e95af3775 | -3.04175 | -52.71265 | 2024-12-23 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14f7d1c1-f646-3906-bce7-ebb897a03742 | -3.03591 | -53.89431 | 2024-12-23 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfc4a0cc-304f-35c8-9392-e97b0e43f3ad | -3.43546 | -51.10932 | 2024-12-23 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2de93ed7-3388-3466-bc4b-19ddf96da680 | -4.15634 | -43.65972 | 2024-12-23 04:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0dddd7f-277e-3e60-8100-ebead673415f | -1.06304 | -53.60978 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 782a3e52-6b5d-3e27-bba7-fe0543689a0d | -3.33278 | -53.10819 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31b10d65-e305-3c75-b10f-57e7432ad5dc | -4.05174 | -47.02298 | 2024-12-23 04:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 017ba539-99fe-3433-9392-899738d4f0d7 | -1.63417 | -45.84484 | 2024-12-23 04:53:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77d3bbc8-0dd9-3ba4-83cf-0460dc8ca631 | -2.40373 | -53.74601 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ed870b7b-c3f9-383d-90c8-a95a5941e875 | -3.18753 | -50.56501 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70ad3934-f5c7-3a28-84aa-0f747703d6ba | -3.33609 | -53.10871 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d826c5db-f462-3034-b50a-3b7e237559e5 | -2.04243 | -52.11126 | 2024-12-23 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7a7782e-c148-3897-ae23-ebea4f4e42e5 | -1.68086 | -47.07732 | 2024-12-23 04:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03b9ee03-3854-3539-bd9d-e860b03fbec9 | -4.37771 | -44.00307 | 2024-12-23 04:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ec10eda-b23d-3094-a76a-018df8689a14 | -2.12085 | -50.70331 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5271ee50-9bfa-3504-9c28-30201e338142 | -2.98214 | -54.12783 | 2024-12-23 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 95ed4963-5cc6-3904-a460-1642d00ca3d3 | -3.50799 | -47.19926 | 2024-12-23 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7693d7d-6018-3e7f-b963-7da8ab22c382 | -2.99103 | -51.44284 | 2024-12-23 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 266375a7-ee55-3ac8-9d1d-94d3bc467069 | -3.00663 | -48.12632 | 2024-12-23 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b3fed02-7caf-354f-a4f7-5b4fc1075111 | -2.83649 | -52.57026 | 2024-12-23 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a180fd3-0ae6-3106-b75a-fd20b1c72fb5 | -3.50865 | -47.19492 | 2024-12-23 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57bbf6c1-737a-3501-a0c1-6216ed848838 | -2.13192 | -50.70105 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c19a199d-4127-3312-aa7c-b5c99eefefa5 | -1.54543 | -55.06254 | 2024-12-23 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ef278bc-c847-370b-9e48-819b9bd98b53 | -2.3817 | -53.77765 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91aafaf9-79af-37f3-a8a8-f36137632cb1 | -2.53701 | -54.15067 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe193cef-e6bd-3f58-88cf-cc11a37b5876 | -1.25394 | -54.68891 | 2024-12-23 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb837a13-a873-3d7d-988d-ba4b1d4bbb4b | -3.10236 | -54.549 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4aacab13-c386-3661-8910-fcbae5071e7b | -3.00718 | -48.12269 | 2024-12-23 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a82b6c64-5ecc-33fe-9808-8df1dac8d035 | -1.06636 | -53.61029 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3991325a-9eff-3160-a0ea-4dc0abda8a69 | -1.14974 | -53.59876 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11c090bd-561c-308e-96c1-77ae6383d945 | -2.56301 | -45.56365 | 2024-12-23 04:53:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcdf12ae-96d8-3135-b561-27e949aae025 | -2.53368 | -54.15014 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bb085ca-a8aa-37eb-b216-6d6e0f630a64 | -0.21365 | -51.60567 | 2024-12-23 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b21e159-0325-3787-8394-1d24cf4e1da4 | 0.06473 | -51.10667 | 2024-12-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fb240fc-bda5-3b7d-9bcc-0a61a6f7091f | -2.56834 | -53.9947 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e5b0ade-3e14-39ea-b537-fac9e3dc21a4 | -4.37163 | -44.00594 | 2024-12-23 04:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4bf5be2-dbbe-3c89-a27a-0ffbf2f6863f | -1.06913 | -53.61428 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f721586-88d2-36de-ba9d-78dbebf2faed | -4.1507 | -43.65887 | 2024-12-23 04:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce452a90-2990-39f7-80c4-05b44498d57e | -2.58197 | -49.05649 | 2024-12-23 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 165117db-fe3c-35fc-aeca-2f2a6fa9047a | -2.76658 | -52.648 | 2024-12-23 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71140ae6-20a3-3010-80a7-b0befe8917e1 | -0.20751 | -51.60112 | 2024-12-23 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b17b8b2-e896-3536-818f-db7a3135d93a | -3.18291 | -50.5479 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea0bd029-ff7f-3305-a528-e55b0c8c20d6 | -2.94016 | -53.05772 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c339c129-5a50-36f5-bfd3-9bb763ed504e | -3.7544 | -47.20475 | 2024-12-23 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0e32331-581d-3324-8496-ac82c39bcb9b | -1.19749 | -54.11431 | 2024-12-23 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cb96b04-3b39-3b02-888c-6792af4592e2 | -3.1018 | -54.55254 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae53b50e-ee57-3c39-9f49-3d00f9e39bcf | -2.49404 | -51.80318 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea96f5df-b0fb-3c10-9b2a-494675d71ad9 | -0.96037 | -46.84645 | 2024-12-23 04:53:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f699702-be83-3462-85d7-98822e0e28e0 | -2.58399 | -51.92292 | 2024-12-23 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48360566-8760-3386-bb6d-29bec10b1601 | -2.9407 | -53.05427 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 451384b7-162b-375f-87e2-0eb6c5e58c12 | -1.06859 | -53.61774 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39f619a1-be87-3224-92cc-77dbe43e6056 | -2.67693 | -54.59925 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1918167c-f36a-3a0f-9716-ec0184d30c1c | -2.79504 | -52.94302 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc20b671-1085-313e-b69c-c9be73239cdd | -1.09806 | -53.66844 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0414fbb5-cd59-3304-9a44-0f2403a5cb74 | -1.49441 | -55.53826 | 2024-12-23 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
