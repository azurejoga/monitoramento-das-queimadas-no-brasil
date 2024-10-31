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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1969fce-0b35-3e1e-88d2-b23b547398a1 | -1.47825 | -53.54284 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 511207ee-9e6d-3f44-a1ab-e5aded7ad7f8 | -1.38975 | -53.61297 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 84820eee-1e3b-3f3e-9092-0c4e7c529c01 | -1.38748 | -53.6051 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| deab4f62-fe79-3e22-95d6-0b9fa8cb4400 | -1.38633 | -53.61234 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f8bc2846-ef90-3dbb-9015-ac10e8f532d1 | -1.38406 | -53.60448 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae2963ad-7152-35d6-a8ff-a033bd1e1cb4 | -1.20616 | -53.77914 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 78366309-5880-3794-820e-9945bb8850e9 | -1.20557 | -53.78294 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 611027a4-e9a8-3ba6-9468-d5f4a6b15784 | -1.19258 | -53.6408 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 852721e3-105d-3e8e-bead-bda243b91d1c | -1.19199 | -53.64452 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6a34ce2-b2e0-3cc1-8e5b-ea9ff6988858 | -1.16589 | -53.38898 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80181a66-094b-3d74-a501-3453519f0961 | -1.16306 | -53.38476 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee4c586f-d5b9-3953-97ab-f76d9720c4db | -1.16248 | -53.38843 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e558e36a-9649-34e0-b242-f5ef29b32027 | -1.15506 | -53.39107 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54c8ba3f-2d36-3445-be9e-1706e65fb7cf | -1.15337 | -53.37955 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fec6aaa2-98c8-39e1-b60c-eb9d237641e1 | -1.15222 | -53.38687 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 59125716-29c1-336f-a474-deb7d2342839 | -1.15164 | -53.39056 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2337ddc-60fc-3d62-9555-356216baf604 | -1.14879 | -53.38641 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| da037573-a112-36c3-8bcf-d98fe5e0928d | -1.14803 | -53.63789 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc33383a-4d94-3a07-843a-9ceb9e7e069e | -1.14458 | -53.63737 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1685a529-7818-3d3a-b81a-c5fa2e0cac25 | -1.13406 | -54.1003 | 2024-10-31 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1417d55d-4ab1-3add-9329-460ba8844480 | -1.13366 | -54.08005 | 2024-10-31 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10822625-9736-3fe5-8895-7075ab8ece2f | -1.13344 | -54.10422 | 2024-10-31 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 700b5f80-c41c-3f66-8e07-9972fcb42d66 | -1.13077 | -54.07557 | 2024-10-31 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9502f050-bc1f-334b-af78-f5b6e929da06 | -1.13054 | -54.09973 | 2024-10-31 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45ccee17-7a96-34f0-82de-1c3de9a086f2 | -1.13015 | -54.07947 | 2024-10-31 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fd2ff2f-8483-31d9-9daa-b56cc0976794 | -1.12979 | -53.44024 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41094659-b3dd-3b84-b53f-70557bbc321b | -1.12636 | -53.43969 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79471421-eadb-33ca-b007-84bc324564db | -1.09212 | -53.65629 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f4b7365-4e97-33ed-bf66-d3cb90b2160a | -1.08927 | -53.65194 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0bb7ede-f64a-394a-b750-05de7905329d | -1.08867 | -53.6557 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e99eb2ed-4c2d-36a9-8116-6b5cf88b902a | -1.08808 | -53.65947 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b57cc77-7ae9-35a1-9815-0a7fe78ff49f | -1.08582 | -53.65136 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85ffe229-2ab1-39ca-89aa-65d74ec6aa76 | -1.08523 | -53.65511 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cdb1e66-707e-340f-b76c-617b7f9e2502 | -1.08463 | -53.65888 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c47e3fe-f1f4-36b1-9274-71adf914cb5d | -1.08237 | -53.65081 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfca1d0c-ee50-3271-a6fe-ae57e65c8b6f | -1.08178 | -53.65453 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c69e6059-abaa-3a76-8f9f-243c47769954 | -1.07833 | -53.65399 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91e27ff6-aa7e-3d55-ba01-a528c4aaeb6a | -1.06736 | -53.65623 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11084803-45fa-3f36-b765-e8682b26dbd3 | -1.06677 | -53.65996 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d196b04-12b6-3029-b31f-a44019421d65 | -1.03748 | -53.73249 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8da9e303-86f8-3368-ba85-65da4b21a5f0 | -1.03635 | -53.36518 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6b096a3-4a51-3ba9-82d0-ede6390be288 | -1.03519 | -53.7325 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 226d1f66-5259-3c93-b3e1-98ffa29471e3 | -1.034 | -53.73204 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e301f99d-3688-3cd0-abc4-2be87e586161 | -0.98212 | -53.70884 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10be05b9-a4bf-30da-92a2-1a23b12703d2 | -0.97808 | -53.712 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53fa31c8-564c-3908-8d1d-c18669ebe053 | -0.88063 | -53.68629 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6746fea-bb15-3064-919e-82a244ca7971 | -0.88002 | -53.69016 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ecc35c9-f7ee-310e-99d9-b2ac93fe3592 | -0.87654 | -53.68971 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d70db92-db54-3e2f-b01e-d075dbce8377 | -1.47466 | -56.00871 | 2024-10-31 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 080ac64b-7281-3986-bb7e-47ad066d6066 | -1.47077 | -56.00808 | 2024-10-31 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb773cea-a02c-34a5-b33d-796ab06309f0 | 1.76105 | -55.85318 | 2024-10-31 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b3eb89d-0117-377c-920f-743f9462e766 | 1.76051 | -55.84966 | 2024-10-31 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3567939-c684-3024-a231-a7c06b7a1b6b | 1.69124 | -55.88849 | 2024-10-31 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a284899-b8d8-3948-b01c-b391dc778707 | 1.67101 | -55.81252 | 2024-10-31 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cfa9cfe-d3a5-31f6-a201-a31955a05421 | 1.67045 | -55.80902 | 2024-10-31 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e48acf95-3443-3475-91f6-5e9e020fdf5e | 1.66131 | -55.80319 | 2024-10-31 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4357bc92-dd06-3f46-89e9-b241cfbb50a6 | 1.6573 | -55.80383 | 2024-10-31 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51250721-1cd4-3aa9-be8c-0ced650062b6 | -11.29263 | -41.86167 | 2024-10-31 04:49:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65a231f3-b7d7-3251-8896-6dc3b5653fa0 | -11.29204 | -41.86674 | 2024-10-31 04:49:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 182ff519-b0f8-3fe2-9023-e7cab195cac6 | -11.29018 | -41.85977 | 2024-10-31 04:49:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 95b7f3e7-5f4c-3129-899e-922bcef09ce3 | -11.28956 | -41.86481 | 2024-10-31 04:49:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| adddc00b-1b63-3492-89e3-4565fb7eb39f | -11.28894 | -41.86988 | 2024-10-31 04:49:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 566886e0-ba3f-3eca-812f-6540fc06b25e | -4.84814 | -42.47584 | 2024-10-31 04:49:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5cb1edb2-ee8f-39b6-ace2-5eb97881c24a | -4.84202 | -42.47873 | 2024-10-31 04:49:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4375a3e2-6662-399f-8b23-143a933e060a | -4.64954 | -43.11767 | 2024-10-31 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4526207b-bcae-3602-9679-64013beeb709 | -4.64906 | -43.12103 | 2024-10-31 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5027c490-64de-3005-8686-b9dd2004da03 | -4.64858 | -43.12437 | 2024-10-31 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3273963-523f-3188-976d-d14a80aba2f1 | -4.6442 | -43.11689 | 2024-10-31 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed0ee407-7644-3dbe-bd15-9f1eada8e83f | -4.64372 | -43.12025 | 2024-10-31 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3eb1b5ed-177d-336d-aabe-04210e386ae3 | -5.97018 | -42.60927 | 2024-10-31 04:49:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79988c62-6f87-3d42-9966-43fea50f5d19 | -5.96664 | -42.60865 | 2024-10-31 04:49:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 25eea540-64e8-3b0b-851c-5303635ad637 | -5.96455 | -42.60848 | 2024-10-31 04:49:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f4ba2892-9e2e-3a42-9958-bca8eb1ae7b1 | -5.96101 | -42.60789 | 2024-10-31 04:49:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4afc8ea1-d5b4-32ea-bfbe-760cf370f7d7 | -5.95892 | -42.6077 | 2024-10-31 04:49:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0b61bc4b-9bed-3c2b-9cf7-d753f5d8a716 | -6.20082 | -43.42585 | 2024-10-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dc9a31f-260a-32ad-9699-795dbe210e5a | -6.19543 | -43.42539 | 2024-10-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14ec877e-bbd6-3322-a0b4-be3ee324604a | -6.19496 | -43.4288 | 2024-10-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81ffcdd6-ff5e-379c-8c7b-acacd7fbd899 | -5.45953 | -43.17487 | 2024-10-31 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6c09db2-9757-390b-87e4-b38b6c335fca | -5.44406 | -43.26103 | 2024-10-31 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4997b0f3-2131-33ab-93b6-61e9a6c1ca0e | -5.44358 | -43.26435 | 2024-10-31 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed78df9a-110f-37b5-8131-fd2db9eabff8 | -5.44204 | -43.26168 | 2024-10-31 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5346cf1e-6b0a-316b-985a-620ec28e24a9 | -5.44158 | -43.26502 | 2024-10-31 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62c76eee-c75f-3a0a-b571-a18c1212de3b | -7.34448 | -43.54488 | 2024-10-31 04:49:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7e3282fe-d261-3439-9ec5-bcd73fcabeef | -7.34202 | -43.54354 | 2024-10-31 04:49:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5e420637-9f27-3eb4-84c3-29df707b5d55 | -7.3415 | -43.54719 | 2024-10-31 04:49:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7d7c7857-ffc9-319b-970d-2b16a4928869 | -6.69598 | -43.05693 | 2024-10-31 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ad1cefa8-43b5-3c72-ab49-fe16696fe04a | -4.27233 | -43.42845 | 2024-10-31 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db1a3428-895d-37d6-b42e-5a34f38b59d8 | -4.27187 | -43.43164 | 2024-10-31 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 532941af-4005-3334-9e0b-425770ac3c73 | -4.27141 | -43.43483 | 2024-10-31 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f0e435ea-b8f5-3ee0-9e80-37aa6ce0b856 | -4.27095 | -43.43801 | 2024-10-31 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b054564-a9f6-33eb-9b80-90b456908764 | -4.26713 | -43.42769 | 2024-10-31 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97569caa-ce78-3b91-9e70-68f010763535 | -4.26668 | -43.43086 | 2024-10-31 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf72a3e4-bb98-3469-9e7f-ec9d5f20bc80 | -4.26621 | -43.43407 | 2024-10-31 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a501789b-2039-3540-a622-cb8fda3bad0d | -4.26575 | -43.43728 | 2024-10-31 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9ea824b-054e-3bcb-99d7-74dcc5de81aa | -4.26057 | -43.43646 | 2024-10-31 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a86495e-8efe-3fab-b9d7-2dc3334ecc4c | -4.26012 | -43.43957 | 2024-10-31 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51db4d4b-2e3f-371c-8d8d-9f68dc78fa92 | -4.25405 | -43.44496 | 2024-10-31 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c0c205b-783c-34e7-b001-7fbc602ab69d | -4.69619 | -44.38483 | 2024-10-31 04:49:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ef886f2-2f35-3f99-b2e5-a986d8354eea | -4.59997 | -44.30676 | 2024-10-31 04:49:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cce16150-baec-3fae-8fa8-afc53b7fc907 | -4.30389 | -44.49635 | 2024-10-31 04:49:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README34.md)
