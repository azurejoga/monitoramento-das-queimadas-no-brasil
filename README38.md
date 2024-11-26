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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 484004cd-e29e-3c57-8467-4ee5df6feff0 | -2.18567 | -53.66199 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28e4fd96-30c2-3e1e-aa95-f285446dd60f | -3.95074 | -49.9493 | 2024-11-26 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e5f1ebf-fbbf-3caf-ad2c-0a05604256bb | -3.99647 | -48.07597 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf482e0d-ac04-3854-99c9-9e666168518a | -3.49918 | -53.79937 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4bf7509-c379-30b8-878a-19c25fb6f50b | -2.59733 | -54.00529 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37eff4fc-d104-3085-9931-3eee815f41c1 | -2.70041 | -51.98613 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f1ba728b-2877-3c4b-83d4-7c66daab8e39 | -3.3037 | -50.41027 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edd5fff5-8dee-3c00-9bca-085d5c83796b | -3.98463 | -48.05949 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| bec19ead-71cc-3f95-ba71-5b607072bcd8 | -3.54506 | -50.18895 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3050b75a-5766-3706-b768-921e671b4b79 | -3.34148 | -50.04834 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f97027e8-3901-37c6-98b7-0cf6680845a2 | -2.62901 | -51.77185 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b5fbf9d-5c7a-338f-a368-d38e2b95f451 | -2.3851 | -53.71095 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9955b2c-ac8e-34f0-b25b-b98ff26b6399 | -3.40228 | -49.56698 | 2024-11-26 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 923d35f2-985f-3b5a-911a-4d286982ef9a | -3.04574 | -53.7217 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4f4af57-dddc-30a4-bb6e-acc24536de06 | -3.31658 | -53.28877 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38c1038f-3807-389e-83f9-c876a60d4cc0 | -3.32819 | -50.21988 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 470ac942-bc68-37bd-a8ab-bcedabb82c96 | -3.31965 | -53.70218 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaac9721-43a1-397b-8484-f610ac58fbb4 | -2.58339 | -53.96384 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a34ec55c-5446-3011-b12f-2b7dd47cfbc3 | -2.76946 | -52.90876 | 2024-11-26 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 69c3ca96-ab8b-314a-9f4e-9cdfd3c4f84c | -3.50759 | -53.8115 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5fd13080-94fc-36f8-a54d-a099f47cd01d | -3.0586 | -53.27606 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 53af2278-7ab7-3a7f-bff3-72fde1c9de86 | -3.48373 | -50.80975 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63522075-bf5a-39f6-8908-c879f56e3d5d | -2.25024 | -53.4691 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07e0a427-77e3-3b53-b47d-9d446c983129 | -3.18908 | -48.43308 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df08a53a-ea17-3fa7-bacb-57a73790e702 | -3.42762 | -49.99673 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dadb53ce-3daa-3744-b03f-23fc2441c77f | -3.91196 | -42.41419 | 2024-11-26 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d1a7a142-f6cf-363f-8302-76898db96d1c | -4.53852 | -43.29222 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 219fe93a-ecb0-3532-92fc-be7aae3adb71 | -3.55045 | -50.20754 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5398b7ca-16c2-3997-88ad-76c858199f5c | -2.46551 | -53.69398 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39dae604-ff4d-3ffb-b86f-e43ed098cf00 | -4.53777 | -43.29763 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e65ea6a9-3c17-36fd-a551-c2f87d0fc22a | -3.49642 | -53.81703 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49496cd7-fb4e-3550-9648-03afb3413ff8 | -5.65252 | -46.64922 | 2024-11-26 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e72fadb2-fd3f-3d4b-bf84-b181ac3cf162 | -3.1788 | -48.44059 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 522fe415-5555-384c-a615-597126a027f0 | -4.11079 | -48.85315 | 2024-11-26 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d1132ed-af31-3915-95f5-c6ec5f251901 | -3.49977 | -53.81755 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d413cf66-3a54-3dc4-9f15-c8d9577b1078 | -4.42869 | -48.70739 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd81d36f-1eaf-32f6-b2e5-8c29489c9332 | -2.40732 | -53.67835 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b8e6c87-f3f6-3341-b9ac-35d311c9c0f3 | -2.61154 | -54.06444 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 674a50b5-99e8-36a5-ad9f-8301d9bcafbd | -2.59787 | -54.0018 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 625af25a-568b-363a-b74e-959755783d81 | -1.99084 | -53.29751 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2d408d0-8e0f-36e2-8b7e-316eeef18f0b | -1.70663 | -55.75567 | 2024-11-26 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23784c38-a0bb-3c7f-947c-882421280004 | -2.80403 | -53.02366 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 495ff6ec-520d-370f-9c3c-bfb80c8341d6 | -2.77004 | -52.90503 | 2024-11-26 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5808c0a2-4e28-341a-b493-03f429c3db31 | -3.18547 | -53.25367 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9a84a73-cff8-3132-920d-c06b5f2a08d4 | -4.38802 | -47.77522 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31ffefc2-f1bc-3a71-bae7-58d985d4a07b | -2.07087 | -52.28605 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00e179a4-64a3-393a-889c-3bd7338e1593 | -2.62966 | -51.76772 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8ed3c95-03a7-33f5-8942-d590613667fb | -2.23689 | -53.61937 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a62179ad-4f0a-3acc-b98c-a1328cd83d95 | -5.47842 | -51.17131 | 2024-11-26 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a76b3cd7-9cba-39bc-9514-8b424b95665b | -3.9633 | -48.05481 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fd7c380-b172-34cf-a20c-737984644013 | -3.91444 | -42.42613 | 2024-11-26 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2246970c-41bf-333b-a523-de0d843d8f75 | -2.2698 | -51.91599 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04ef6fbc-c37f-38c5-8487-23ce261db62d | -3.18841 | -48.43756 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edec1d69-6678-330d-8694-e55397328696 | -4.02668 | -45.54627 | 2024-11-26 05:01:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed9ebee0-6f38-3d32-b59d-c554b416c812 | -2.23933 | -53.66296 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d326d438-74f9-318e-98d1-7161c7e77bff | -5.27825 | -45.12557 | 2024-11-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae5f1459-f568-3849-b25e-2ba651d0e87d | -3.98317 | -48.06948 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a5723237-d706-3050-8675-4573941ee11b | -2.80688 | -53.02787 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b06af18f-9f0f-35a8-a3c9-892f194410ed | -5.75472 | -46.26147 | 2024-11-26 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fef39beb-fa9e-33fe-89c6-ce3b4ef2c4d0 | -3.24203 | -50.15376 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 829ea6b4-0558-34d5-8004-325e712c76b2 | -3.50032 | -53.81402 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d3f2577d-3488-3023-862d-9ae184dad9a7 | -2.61001 | -53.96795 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa2d6566-d59e-35ac-b91b-0d5b5bd4cd51 | -2.40343 | -53.68135 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c47b3fc6-7515-3c81-96ab-e6e49b4575a6 | -6.11091 | -46.92892 | 2024-11-26 05:01:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec1aae05-2a14-334e-bf96-b89d920054a8 | -3.97922 | -48.06399 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| bf2951f4-63fd-36bf-a2c3-4ce4442abbe7 | -3.34496 | -50.5078 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c466306-0a51-389f-909d-78fc8e87c712 | -2.99654 | -51.45687 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d86098ec-2eb4-36cc-a186-2003b49b23c7 | -2.77554 | -48.58239 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1661e82-e544-3ff6-a377-6cb5fcc39d37 | -2.01529 | -53.00559 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ea7d9db-fa88-354c-89e3-fc0e4f527c00 | -2.2536 | -53.46962 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5e42980-86b9-3b44-9dd4-e35a212c9670 | -3.97777 | -48.07395 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 26a47aa1-9129-3924-9216-997b42f20e63 | -3.89072 | -50.07259 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 123c92a9-796c-381e-b4bd-bb9f4d795a17 | -2.57969 | -51.92311 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 761bd2ad-96a2-3122-9c77-f74e10b84b40 | -2.5947 | -54.06538 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2eeeec1f-d020-3533-b11d-0ef282b4de07 | -6.11135 | -46.92581 | 2024-11-26 05:01:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce92e4f7-03a0-336c-84b2-d0dadc7681f8 | -4.24142 | -48.67014 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64a13427-25f8-365b-b92a-3964efdd7123 | -2.70271 | -51.99474 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66d204b1-330e-3177-adeb-92c63343740b | -8.26349 | -49.54788 | 2024-11-26 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8a54f54-5578-352d-8df1-f11eda3f78be | -3.24889 | -53.2933 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92684c73-0889-38cd-81d5-bfaa6ec52b6b | -2.8086 | -53.01677 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e43aa369-7d93-327f-b8c3-443b8dfe7e09 | -3.94426 | -47.99179 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3629ad71-aa26-3993-844a-ea91528da582 | -3.17499 | -48.43549 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d288ec66-4a01-30eb-bebc-782a73941a4d | -3.96794 | -48.05553 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 522235d4-5b1e-3146-8cd6-0f95a0c6cf28 | -3.18327 | -48.44128 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a65c30b7-3cd9-3e6a-be94-3cd301f647cf | -3.80854 | -51.3733 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7ff14e5-b814-3b32-b6a7-35cb20de26d5 | -2.57896 | -53.9703 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e593eff3-c9bc-373e-be7b-73e0b983bf53 | -2.21257 | -53.79546 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0d52290-386e-30f9-acd3-38dd7ae2d125 | -3.33089 | -53.71838 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1ff2d5f-b4f6-3e5c-8c38-a4db09e852f6 | -1.8863 | -53.31481 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26921630-9b53-3d59-ba9a-dea8e7cc33ce | -2.40677 | -53.68187 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7e94503-dce8-3cdc-9902-80bfc66a3253 | -3.17341 | -45.26059 | 2024-11-26 05:01:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9090f5a-0e4e-3ea6-a2f0-4512aa4191e4 | -2.37358 | -50.40599 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2088e1ce-18de-3be6-b646-472ef9d33ec2 | -4.24077 | -48.67454 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 052a8a85-330d-3823-a1f4-25247de7cb18 | -3.96989 | -48.06284 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 2211ebdd-d212-3c6d-aa78-1b072299e734 | -3.28647 | -51.11506 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebb4cd1a-4596-3d56-aff7-97df175a00b5 | -1.93746 | -52.09911 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60f34607-14ce-3414-b844-b72fd15e9b96 | -3.27142 | -53.82199 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 924da2f7-87b2-3fba-85eb-07a05484d566 | -2.69688 | -51.3631 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f6e1aa1-8c6b-3464-b8bc-13cf67bd4c67 | -4.53999 | -43.2815 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1658060a-7adb-3910-8a99-4f4028eb8726 | -6.69163 | -43.06463 | 2024-11-26 05:01:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README39.md)
