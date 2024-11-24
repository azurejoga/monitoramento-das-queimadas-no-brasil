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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b83958b-dc49-3d5e-accd-b4db5be67c2b | -2.70327 | -48.65792 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ccb69bc-7aad-3614-be65-105ee4aeec84 | -3.00279 | -52.51204 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9e8bc70-8bc2-3925-a2ad-6ec43a8f91bd | -1.12178 | -53.58255 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ee618c3b-6ac4-3403-b568-ccbda1584ab6 | -2.22215 | -47.76819 | 2024-11-24 04:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9e28b7b-2a7e-366d-a1dd-67667c40858e | -3.69598 | -50.21643 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22c9fa99-1b73-3581-ab71-74fbe907bc95 | -2.74769 | -54.07053 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 189f5aa4-ba7b-38d5-93e3-afb1628c8f27 | -1.77319 | -52.71737 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c39e34c-2352-314d-ac0a-0f40aaef5368 | -2.22863 | -46.11363 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 75258b00-944f-364b-8ed0-57f25450357c | -3.63369 | -50.68682 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cf6fc8a-f7dc-3bbc-bec6-796d0759bd3d | -0.9129 | -51.65025 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb1c0018-86ec-341f-9752-c50a90b2a3c2 | -1.35946 | -51.37922 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b334140-3d70-32f9-8ce1-14b718e90062 | -2.99281 | -53.35775 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25fccd09-b553-382f-b0d5-2449abb8dec9 | -1.25078 | -53.36281 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff6cb881-2cd5-316f-a53a-f0aacc591521 | -2.54924 | -48.29218 | 2024-11-24 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19119113-5167-34e2-a3f5-8bb2a6f34861 | -3.70948 | -51.79891 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83d7252a-8214-3e67-b6cb-d602a9dd0458 | -2.16302 | -50.4595 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2c82e29-a508-3213-8db5-35f5bab52658 | -2.80444 | -54.02215 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e205b421-6022-31e7-900d-7e3f1ca2afeb | -5.10442 | -43.14693 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6b0290a-cbdb-3dc4-8679-cbf57dc1808f | -3.67253 | -50.25482 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5030a6d-e28c-3f57-9a60-ba4b6d544efb | -1.75754 | -52.66501 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45a2a39f-391b-308a-890b-7a74c8153680 | -1.7201 | -52.49146 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1cda21-4237-3903-9bf3-0cb691b78e0b | -4.93607 | -50.61423 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de0aac03-0f71-3155-be72-68155149d5d7 | -0.05018 | -50.81182 | 2024-11-24 04:53:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50b2c0a5-6aee-35b0-8519-b2836cfef984 | -3.10897 | -54.00463 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3b77d5ad-a2c9-3f55-a972-6d6829d947fa | -3.25087 | -54.23985 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b23c2a62-a41c-3c7a-aac8-08d7982e7ab6 | -4.23271 | -44.63227 | 2024-11-24 04:53:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f5d2e24-ff4e-3a8a-bbf6-915d54ff66a2 | -0.97421 | -51.7123 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed89533a-1ec0-3c8f-93be-c1f7a9e98351 | -3.85149 | -52.19438 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2819365-01c6-3f2e-a77a-cd4b93d914c3 | -4.30074 | -48.18756 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93b87ab1-3ca3-38e4-ad36-f668b20b3203 | -0.81313 | -51.61324 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de948349-fdf6-3a8f-a6c7-6435c52532b6 | -3.67775 | -54.58432 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0b48510f-c356-3829-86ed-966260c3edab | -2.3613 | -47.56821 | 2024-11-24 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6d27564-0a69-3f2b-8177-35342966e35c | -2.15105 | -50.61776 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee50c460-b6bd-3b6f-aa75-88079edf9380 | -2.60021 | -46.26028 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2679d54b-af6b-3750-99b5-5cae35452e89 | -1.44396 | -52.45236 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff6171cc-c375-3e11-93bd-2a6df6a9005e | -1.52759 | -51.56688 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 393e4b5f-c9b1-3882-b731-a26ebb1a15cd | -3.29872 | -50.36082 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b818dec5-0101-3dd8-8128-84f288fc9617 | -2.29193 | -49.05115 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c1750ff-afcd-35e0-ab07-ac18371da4fa | -3.34941 | -51.13831 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 879d7905-1486-39a7-a82c-f35181bc4a72 | -3.26459 | -53.70708 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebdf8ca5-d736-3fd2-9436-7fa8a0856ae0 | -2.27325 | -48.43191 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f6488b6b-c7b0-3f2f-b4ef-b6ba9716572f | -3.23323 | -53.3877 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6be9907c-8aa4-3a07-bed5-55f39462361a | -1.20711 | -51.74487 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a36dd77b-2690-3368-9a75-4f79f251d320 | -3.47879 | -51.99174 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ab034c76-0b94-360f-891a-593a9d7fa70b | -1.38024 | -52.42406 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a663c8c-9f1f-33d2-94ce-b8328598e10e | -3.10214 | -54.0036 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb1ff7f2-cdfe-33d9-ba62-e6e8638a8fca | -2.15495 | -50.61472 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c5ab87d-e931-39ca-bce2-ce1a50ca6239 | -3.12262 | -54.18519 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79788c69-58cd-33bc-b278-def41256f379 | -3.82432 | -52.41188 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5ede1d69-c7b8-3a80-beaa-a4389880c086 | -1.97159 | -53.10412 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6ffee6a-23e5-3299-8163-e2e1dbe5ff2c | -4.54939 | -44.01654 | 2024-11-24 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e15de7c-bf93-3a03-b7e0-38b7738056cf | -3.26007 | -53.71377 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a55ba264-81c1-3859-aaab-48e319704911 | -2.6611 | -51.71628 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3499ef0-e051-3249-a93c-171231f0d654 | -3.93885 | -48.14499 | 2024-11-24 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61ebbadd-f3e8-38b8-b0c1-2ceb0eced56a | -0.25547 | -51.56434 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b25fbe3b-a6df-3a1f-824e-8102039871a4 | -3.09432 | -51.3132 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f3231e1-dadf-3a83-b747-09b0b964e059 | -2.58313 | -54.04603 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 657c78be-e7d3-3547-8b3e-047fe3287e94 | -0.96072 | -51.64707 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93a253c9-8bb8-362e-83a4-a4318be3f440 | -0.98358 | -51.71725 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fc35861-9c6d-3005-ae6b-335f3564347b | -1.6203 | -52.6076 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 87dc6858-d452-350c-bc04-f38e26855f9f | -3.18851 | -54.32645 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d0644df-aed7-3877-832b-67689ba16bea | -1.45303 | -53.39441 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1828fd92-0cfe-3e98-8d24-5fb34c3b61e5 | -3.02207 | -51.36256 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cd9f1bf-6cda-3b82-8b96-5d52d1d558e0 | -3.27926 | -53.41647 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d901923-89b2-37ea-b042-50a5a8eab905 | -3.77667 | -50.99076 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eab80b8e-7b3b-35f7-84f8-d9a5237ef753 | -1.36634 | -55.63217 | 2024-11-24 04:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99b6eb05-9ad5-35c6-9329-d12def9acb6a | -3.50711 | -53.80029 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c3f5f8e-4143-340a-b60e-db9f88e2a6e5 | -3.24115 | -54.23454 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f528808d-78a6-37eb-8dd9-dda774008d7c | -2.14303 | -50.71435 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c15bc653-ee3a-353a-b425-6b6833d06dad | -3.18337 | -54.31408 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49737dcb-2679-307f-bb8a-5ada2b8a2d89 | -1.52563 | -51.62276 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a7711629-2e80-3276-988f-245d23b1a7cd | -0.82101 | -52.82776 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb3ff192-2c99-3cda-8ac4-2d1254882cd6 | -2.05569 | -50.73009 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3147b282-5a11-383d-adad-0fb00e590607 | -1.25615 | -51.78123 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a456710-9dd3-3e59-813a-d9e0c9d090d2 | -3.24968 | -54.24739 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d88dc8c9-3aae-327e-8b11-fba3f1ae2c2a | -1.51749 | -54.19056 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f0222bd6-c93b-3608-81aa-c235bb1cfd3a | -2.20407 | -50.82829 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd9fe586-4235-362b-880d-7dd5a320b740 | -3.98727 | -48.92957 | 2024-11-24 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8be25ea6-4cc5-3bf6-9514-0928d5d7b8d7 | -3.70482 | -47.60827 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e6a920ae-67f1-30e0-ba18-63a9ea297395 | -2.58715 | -54.0428 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 689a4a8c-1bde-3596-9545-b4565902df77 | -2.11749 | -50.12698 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21805236-4094-3a39-b7f0-af4da827321e | -3.51492 | -53.81649 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3692bcdf-733c-3e60-9fee-34dd564f0a9e | -4.36249 | -48.09013 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b101186-378d-3929-9f69-bad2590b0217 | -2.26428 | -49.56073 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32a7a87f-e2a2-358c-86de-de3743a92e86 | -2.9183 | -45.36311 | 2024-11-24 04:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 604e3701-728d-36a1-9715-27622c15daa1 | -1.34234 | -52.5142 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66b90581-ce4d-38a1-be33-0db070890f7b | -1.69918 | -48.46268 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12b6b894-27cd-3acf-8837-dd28f7c97230 | -1.30825 | -51.75064 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 603045ac-5cf0-3882-9ca5-b188df743829 | -2.66762 | -49.85688 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 063a1159-c36c-37c8-b13a-713aa36a6160 | -3.43861 | -50.01733 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f76ba4c9-7394-338b-811e-7b3a8d2d5da9 | -1.38765 | -52.33323 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 988e2b2e-9922-30f2-ad5c-ce3efabe1949 | -1.23582 | -52.58675 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc803ba0-b061-3fc4-834f-afbe8ee2d548 | -2.5427 | -53.99009 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f8f3f0f-dbb0-3f25-bf19-2ffb093f3e7a | -2.85702 | -54.00031 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09c703d9-d9c1-3847-9f84-76f6e131b813 | -3.47549 | -51.99123 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8f6eea03-d8ca-332b-8708-6662afcba434 | -1.22599 | -51.80117 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e4c487a-5c82-3050-b4a9-e52715955511 | -1.96947 | -48.3861 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 14879455-0869-38dd-a3da-3d7be7e27b87 | -3.79058 | -50.9674 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7025935c-2191-360d-b8f5-afed912551a1 | -1.11424 | -52.29742 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1593c3cb-bfd0-30fc-be57-d7857282c1cf | -3.50991 | -53.80447 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README41.md)
