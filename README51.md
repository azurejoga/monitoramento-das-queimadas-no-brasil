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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50e8b2aa-8116-3d63-9831-8e53637eab8f | -3.25156 | -53.61856 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b788aa21-b10a-3e1e-ba0a-94eae48a375d | -1.81749 | -53.04528 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa17bc00-52c6-3869-89da-9cde4ee9dda1 | -2.37746 | -53.66645 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37cb276a-683e-39b0-9b3b-ac531a1f1274 | -2.87753 | -54.0166 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1175451-c4f5-32bc-8ee5-09c68688a645 | -3.03544 | -53.42844 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e83cbe3c-4d75-3b00-99c2-1028c042ce67 | -2.7573 | -54.02362 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f072647a-d47b-3b23-b2f5-e01656b78d2d | -1.17064 | -53.42028 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5355f708-0c61-3613-9f9b-f55d0e0bd883 | -2.87242 | -53.98318 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a84a4b35-5cc2-3f89-862b-356ff46686f1 | -3.19744 | -50.65086 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b11367d1-dce9-3dbe-9aec-9e192fa552d3 | -2.81331 | -53.0492 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1f2f3ee3-82f2-3cc9-ba9f-4d64e1fa7fde | -4.05082 | -47.00465 | 2024-12-04 05:03:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd2f7e5d-ddc7-3262-a157-2e2e45775307 | -3.29071 | -53.82409 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddab5450-7459-38d7-aa02-2ebfa6f449f6 | -0.72364 | -52.45287 | 2024-12-04 05:03:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1995ec08-21eb-3ed8-a2bd-ad18cac90d20 | -3.33636 | -51.21047 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8741707-9dff-3a15-8537-73b322d0e0db | -1.74681 | -52.61518 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| fa7fd29e-bf13-3efb-ad69-e97d49e0cc2e | -2.88532 | -54.01056 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45e685a9-c6ad-3594-97eb-41d85cc41d5b | -3.82068 | -51.66452 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a8fb1c6b-8cf4-3827-beb9-d11fb61190e6 | -2.74773 | -54.17342 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dc94ca5-b7c2-31ee-bd09-1ec7934656f9 | -1.94916 | -54.23524 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42893521-6e29-30d5-921e-326ef4a3eb99 | -3.6637 | -50.19021 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e594dac-8b84-332a-879d-79fac82b9bf0 | -2.93162 | -51.44983 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7ffff3e-cbec-38bd-97d6-ff7f5fa5ddc4 | -3.05976 | -54.50706 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90f9cf14-a5db-362f-b40a-97237b68de38 | -3.49422 | -53.81455 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b5ea479-18fd-3991-91d2-9e92148552a3 | -3.37922 | -52.78745 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acbaf944-a93b-3e72-98e6-413e4c897a72 | -1.99556 | -52.91628 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16e80891-7cb0-3596-bff7-f41c71af478d | -2.79181 | -54.00003 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a205f858-f795-3bd9-9503-ecc454e65bdb | -1.94675 | -53.34623 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| febfac28-14b8-3004-8141-4c41b3007d3b | -3.09291 | -54.05291 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 277cea3a-71c2-32b6-b48b-924e4bf659f8 | -3.1017 | -53.75101 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| addaacb4-0cca-3f1c-bd8f-d16d71061d13 | -3.24736 | -53.86924 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d4734e5-ea9a-367e-be76-4c66a0176d88 | -4.1092 | -48.24842 | 2024-12-04 05:03:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89ab2d78-fa61-346f-8435-9085c8baf619 | -3.32699 | -53.70024 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6479cffd-49b1-349f-a948-667da291791c | -3.32628 | -50.21835 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f58e6b6-5041-3e9b-a5d6-550be39afbbb | -1.61399 | -53.83288 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a731b583-be75-32f8-9096-4978696042e1 | -2.77654 | -50.30057 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3371994a-bd5a-3f64-8ba0-7c343038c27b | -3.28199 | -53.28395 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fd4d984-7fc7-31af-a3e3-21c53e77e8dd | -3.20607 | -50.64708 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| bb182516-b0dd-3bf1-84b6-5b6243185404 | -2.63281 | -54.01484 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad75f03d-558a-30a2-a6db-5c19480f503d | -2.86693 | -54.01858 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 261a9869-f1a1-3cf6-b5b7-80535729e2a6 | -3.01726 | -54.0597 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1179ec05-2740-393c-8e2b-29b3ce805616 | -3.55621 | -51.52334 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eeb89268-c4f8-39b0-ba20-de88dd6bceb0 | -1.38412 | -53.55828 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3e13efbc-a64f-36d1-a96a-f68d01be62cc | -3.72317 | -50.54317 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5acc688-a1a7-3712-88e6-e8a18216bbeb | -2.82085 | -54.07297 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1b0a53a-a42d-3426-895c-14df542af71c | -3.1091 | -54.05906 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f5d0ee42-810a-3137-ac98-9d49359c934c | -2.47043 | -54.0118 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39045952-fb9c-3bf2-886b-4c41d5479517 | -2.45464 | -53.71528 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92a49029-721a-3cf2-9ddc-be935e0e0708 | -2.83402 | -46.75402 | 2024-12-04 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af3f569a-c381-38b5-912a-7936d3c1607a | -3.46616 | -52.24207 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 959ca221-261e-3258-89e7-8b2e8f09c199 | -0.85932 | -52.70762 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60f053f7-f9ba-3fbe-b94f-32e92e891c99 | -2.81845 | -53.06155 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6374d3bb-b262-36e3-a067-f038d615693b | -3.92923 | -52.39214 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07e182e1-f00e-3bdf-913c-f5e42b0ce249 | -1.48044 | -54.4282 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04d57918-8035-3079-9837-7434f0c52310 | -2.86141 | -54.2303 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3c2f3231-609f-3e54-86f6-6f304457ed6b | -2.6258 | -54.08225 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4a84e62-2a76-3ba9-aa2b-b37660a4c50b | -2.79319 | -53.04224 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c62c4772-01e7-36aa-9c3b-e0903d8d9f61 | -3.30095 | -53.66651 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 581f8ea8-c974-3c41-b9ad-692a13d83d0a | -2.35786 | -53.92549 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd65aad0-0e82-3ebd-95f0-6e6e2b82299d | -1.69886 | -52.61271 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c8b9e000-03d3-3616-a4cf-92b4f7360880 | -1.76301 | -52.62551 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 4d3dcc8f-97a8-3253-941d-d9c286a97480 | -1.7474 | -52.61135 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 528c1273-5e69-313d-ac3e-50782e8ab8ff | -1.75836 | -52.63263 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bc6f5b0f-c160-32e5-b2af-44943dd5e217 | -3.36833 | -51.1047 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65d9a99e-6dbb-3563-8319-7530ea43168d | -3.10691 | -50.31881 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbd68dd4-785c-391f-9819-9a29acb8b8e6 | -3.74781 | -52.43668 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a32f2a7-0711-3e3f-95b2-3d7adc9a4afb | -1.26704 | -54.11554 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6aec770-86da-357d-8205-a35ab96d755f | -3.11812 | -54.61246 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e70a9a80-e76d-310e-ac77-94be9ac31a63 | -3.0909 | -53.70871 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70c87ba5-c869-3773-8720-16691051ac69 | -2.62859 | -54.08629 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d8436bb-0866-37b7-84e4-8ff5d9d23f9a | -2.88929 | -51.80152 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38f30d79-783b-35ec-91e3-9feeafcdd6c3 | -1.37078 | -52.11329 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bf72d37-e426-328a-8f74-4193437f6bbe | -2.65702 | -54.10138 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa522b15-6080-3200-833e-1934610b1816 | -2.87083 | -54.01556 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 333fbd3c-6066-3c0c-9818-ee04186b0cbe | -1.41416 | -54.52387 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a9ae917-c0c8-33ab-bc2f-4e1d136cd875 | -1.38492 | -53.66401 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08eb8b7a-497a-3a57-9983-8f511c1205ac | -3.10457 | -54.02204 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d52c43d3-597d-3b1b-aa36-957cd7dc9932 | -6.27912 | -44.7397 | 2024-12-04 05:05:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 797331f1-d907-3073-a777-48c1fac7bc4b | -5.37436 | -60.0995 | 2024-12-04 05:05:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e40b969-9ae6-3826-bc6e-76c83495d8cc | -3.41291 | -63.49744 | 2024-12-04 05:05:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2dbd631-8062-3d55-bd00-2ca7424d4514 | -6.98182 | -60.10485 | 2024-12-04 05:05:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2959dd8-b48e-3273-bc48-be9377166891 | -5.58347 | -45.15247 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f08b3496-fa3e-3dbd-817c-8516c78eb71e | -5.62717 | -44.83607 | 2024-12-04 05:05:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 60b12d48-6c34-3385-a8a3-24de457d3d5c | -5.63254 | -44.84175 | 2024-12-04 05:05:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccdb9cd1-7a9a-3f0c-9aca-c6e07daff841 | -5.57223 | -45.14647 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2f0efba-bb02-3be9-8550-6a6414eb535a | -5.57934 | -45.1387 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84d99d50-d6dd-3b85-ae20-09e70a91bc3a | -10.17079 | -51.52403 | 2024-12-04 05:05:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a0ac9f6-cb7f-3fae-a064-4e96c48aa3b4 | -10.17952 | -51.52153 | 2024-12-04 05:05:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5387f2a7-247d-3119-bea3-03b99c562054 | -5.57403 | -45.13343 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d814c4c6-cc71-38dc-82a3-047aaf831545 | -7.56569 | -47.58622 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a0172e0-5aa3-344d-9b82-a9dd8afbbef0 | -5.57755 | -45.15165 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cba7c899-6ec0-3b86-a63f-9f5e7d9b12b7 | -5.58406 | -45.14818 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59cc4a65-6860-30b9-b7c1-2f8e80c93368 | -5.57874 | -45.14304 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| daed6c23-624a-3e9a-b0e7-847edc63681a | -5.62053 | -44.83958 | 2024-12-04 05:05:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a6e85bcb-3dc8-334c-b04f-e94477cca49a | -10.17027 | -51.52778 | 2024-12-04 05:05:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b82501bf-15a2-3655-bfeb-230b523a2512 | -6.25073 | -43.56143 | 2024-12-04 05:05:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| addeba23-3008-3c66-a802-7189ff661833 | -5.57343 | -45.13778 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f317c91-955b-3d2e-b599-fa80a2115bc3 | -5.62653 | -44.84068 | 2024-12-04 05:05:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e5b7aaed-b9c3-3181-8a69-cf7201b06782 | -5.37051 | -60.09888 | 2024-12-04 05:05:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5c83950-f87b-34c9-aea1-ee2abdf7f1e1 | -5.57283 | -45.14213 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57ab1a78-57ab-35cf-a8c2-ad7b51da3181 | -7.56051 | -47.58549 | 2024-12-04 05:05:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README52.md)
