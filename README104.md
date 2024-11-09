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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c961d6cb-027f-34df-ad4b-2fdf055caa34 | -3.04919 | -50.37809 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d13cd91c-623c-33b1-a372-407df14dd9b1 | -3.21265 | -50.38329 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 230419b2-7bfb-344e-9743-8c68da3ccbbe | -2.22473 | -46.54681 | 2024-11-09 05:20:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2084272-228e-3484-9410-7d9390eb3552 | -4.22243 | -50.64843 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ac6cdbb-ff20-39fb-8284-d48c9461b444 | -2.91956 | -49.35926 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3526a35e-3499-39d9-8a4b-869d493265bf | -3.38897 | -51.46421 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40f9e90f-fa58-33ae-a31a-bf38ba839fd1 | -3.35599 | -53.78804 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9bee159-e0b5-31d3-8fbf-b52bf04803fa | -1.1411 | -53.65227 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70e2ac8e-b91d-39cd-b4ac-21d004bbe0e0 | -3.53972 | -51.10335 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d1474e5-8b95-3967-aa5d-5c840c005175 | -4.25033 | -47.56939 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0c658289-08df-34f5-b129-24891ade38bd | -2.62023 | -51.29597 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6673bf4b-553a-3426-94fc-1e7844c00d3c | -3.12265 | -50.15569 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 666d14d4-4372-394f-bef0-c6b30f7d6cfe | -2.87533 | -51.3061 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ad13883-859d-3a60-9b7e-2ec2edbfa354 | -2.57856 | -49.13527 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 19c8d7a1-6ba5-3113-86d9-ec8363dabdde | -1.05505 | -51.74855 | 2024-11-09 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcf5b85d-d65f-3dcf-bb3e-d2c457dfaa3a | -2.03736 | -59.9723 | 2024-11-09 05:20:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fed5f37-2ca4-367a-829b-59e45463a08c | -3.11141 | -53.7132 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1976f476-f1aa-3143-b4e7-ef222a64b2d1 | -1.68651 | -54.25875 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6979efb6-fbee-3b7d-9213-f8d52957379a | -3.59083 | -47.35614 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 217843ce-f44d-3673-a12b-75a72b332f01 | -2.24207 | -53.77645 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7f1c5b94-2726-36f5-9c30-891d8b18126b | -2.31477 | -53.86778 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f1b6ca8-22ea-3993-98fb-1ae710aa63fc | -2.98535 | -51.46091 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d78a1580-5a63-377e-867a-39c67967cee8 | 0.84602 | -50.17077 | 2024-11-09 05:20:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 389fea49-954c-32d4-8577-3b2c09156beb | -3.0511 | -50.37544 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f3305b8-a520-32ae-b1bd-bce6f3443b82 | -3.63591 | -50.18723 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 23709a52-6f83-3d5b-8403-d894c2b48394 | -2.86099 | -50.32495 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b5d6a01-b196-3896-936f-30ffa5581fd5 | -1.14784 | -53.66385 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 26272970-f78f-3841-8bd2-bb5d6c96e57f | -3.01922 | -53.87147 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bf85f24-e9ef-3de6-ac6a-c4334f3a63a5 | -2.86338 | -54.09846 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2434987a-91dc-3ede-961a-b4f57dd95470 | -3.58755 | -47.35207 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 94e937a5-a785-337f-b7a7-21827426b942 | -2.18657 | -53.63354 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54a5d3b8-2d57-3219-bf56-b75ad7c0a4ce | -2.24633 | -53.77707 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c10b4cb4-a0da-3cf1-812b-0c22b3d7a22f | -4.08408 | -48.85942 | 2024-11-09 05:20:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03b86d03-e82a-31c6-af11-3b9cdcb68c70 | -3.1018 | -53.98081 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 405a74af-6d0f-350b-86dc-a550c99d3620 | -2.72206 | -54.14866 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f5f2682-7f9d-3d7b-94e9-e76e92e9a9c8 | -2.97377 | -51.43509 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89710137-4993-34fa-a0ef-736d3e269b5f | -1.41246 | -55.38364 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 151c5574-77aa-373b-8c06-27ffc6c27815 | -0.22274 | -51.64897 | 2024-11-09 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2c7f05f2-4565-3888-9d3b-844f328bdfd4 | -4.06577 | -50.01151 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8c8dfad-284e-3881-aa83-7d79536aa7b5 | -2.48043 | -54.05453 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 502608bd-86bd-328b-a869-0414637c0fc8 | -3.58386 | -50.27328 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3b14d94-3f0f-3c74-94dc-de635ae85023 | -3.10275 | -53.71187 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c0ebfc9-5111-3594-8511-8a9e21ad217d | -2.81713 | -54.09153 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33063326-9fc1-318e-ad4c-56bfb14f4feb | -2.87538 | -51.47549 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77bc4f8a-3b2d-3064-af28-b4d2a1c0e8d2 | -1.62587 | -52.2426 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82db6eec-ea5d-3594-8003-d40fca141a31 | -2.6179 | -51.74915 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f23b580f-3308-3b87-8dde-e24db43dcd7d | -3.12013 | -51.1087 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af11fb39-983a-3de1-85fb-18ac9d0fcf0a | -3.89362 | -50.23829 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd3b34bc-1f3a-3bc1-9fea-2ea7ed0c0d91 | 1.32568 | -50.72898 | 2024-11-09 05:20:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeca3cae-1917-3395-b77b-e4e1c3693bb4 | -4.39474 | -50.97604 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f5144b-4c09-3808-a2e2-28f71940ce85 | -3.03156 | -50.31058 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a5b43bfa-0d36-3357-bf0a-6e5f9f98dba1 | -3.84757 | -50.04335 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb02d916-8561-3a3d-a58b-b4990baa8567 | -3.09795 | -53.32516 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 98c56c70-e2b6-3732-ae9c-e6c591a6717b | -2.21516 | -53.72342 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| efed17d5-42aa-3d2a-ac9c-be8f4a03de3c | -3.14623 | -52.97599 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 6fc5a59b-7db6-314c-8b37-2885d673a36c | -2.83823 | -52.90307 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4695de0-d410-3352-89ae-46cef3566378 | -2.60829 | -51.30629 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5738ff79-4d8a-3387-8e50-c30dd88351a3 | -0.08384 | -51.40546 | 2024-11-09 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e5fae0d-fa80-39a4-8288-bb8533f2c4ef | -5.11347 | -47.14735 | 2024-11-09 05:20:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3161e729-beaa-3a4e-a67d-e3ec689130b9 | -3.11636 | -53.70972 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6285f888-47b7-3e16-9421-0194b6e07913 | -2.31137 | -50.67062 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4fae2678-4f77-3417-80f7-e9c2abfaa169 | -0.64253 | -52.38379 | 2024-11-09 05:20:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 073c7eda-8e4c-321c-8b57-b8752d2254ec | -3.48976 | -54.57816 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb7d8ddd-1396-3457-9fac-183e8a2ae931 | -2.97216 | -47.92957 | 2024-11-09 05:20:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 89699420-85f8-362a-bb12-a34ae1a7627f | -3.38194 | -52.35293 | 2024-11-09 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8879f476-52bc-3660-a208-5466b0bd76ed | -3.78629 | -51.32793 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 983e758e-a43a-3dd8-bef3-b4f7daa91f6a | -4.21009 | -48.55021 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f7397cc7-a782-3ccc-bbe8-d305c94b7dce | -2.08134 | -52.05072 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b8385a5-fb55-318b-9728-da481537e6ae | -3.02227 | -51.19845 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45c1b699-a2c1-34e8-9b63-ee09167692ac | -3.9585 | -48.17035 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d78ac076-3af9-354f-bd90-e80cbb3157e0 | -2.54611 | -58.06614 | 2024-11-09 05:20:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a769f41-18db-3ffd-854a-413bcb7189a9 | -3.32635 | -49.91291 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4bca9a68-65de-30d2-8b68-b724cde37438 | -3.02698 | -51.01535 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82f70f00-5177-35cb-883a-e3547e2f54f4 | -2.24268 | -53.77248 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e36222d8-b410-3d10-8c69-761f6ee34a49 | -2.79607 | -54.00175 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1ffb7d9-711f-3c3b-b786-b343f05a8623 | -3.58978 | -50.27472 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 246b863f-c0f0-310d-9271-3bf0f276b50a | -2.72167 | -51.70986 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f145fbc-4430-3e19-84f8-68e99bb92277 | -3.11978 | -48.64251 | 2024-11-09 05:20:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3de2b345-08f4-3f46-b42c-f55536d19827 | -2.61297 | -51.74841 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9390739-e72a-3398-8b0b-1b3aa26424a0 | -4.21609 | -48.68473 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14271f67-2478-3c27-898f-b92e017c31d9 | -3.03263 | -50.30347 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7368636a-b32f-3dec-8a2c-aec5718fb168 | -1.19816 | -53.92046 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72bc94a2-efbd-3709-a60b-bfaadc9c5932 | -4.82861 | -47.32153 | 2024-11-09 05:20:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d85f9dc-02c8-3c1b-8272-d16ada0b03ea | -3.79128 | -51.29361 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 303b2dc8-bc54-3952-bcf8-2f6ef3bd6af7 | -3.2516 | -51.13297 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3272ebb5-62e6-3373-a92a-9f417fefa408 | -2.99039 | -51.46172 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90faa16a-026c-355f-98a7-a0c1292c08ec | -2.92114 | -51.68013 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33e7a91f-765e-3131-9dbf-6de8ef7d32a9 | -3.07133 | -50.57596 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7cf26839-9faf-3533-a6b2-1371de7ce42e | -2.06522 | -53.28078 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf863a14-6620-39ac-8601-24e2b3c604f5 | -2.23356 | -53.77516 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| bf49279d-2d54-34a7-aac9-9bf0cab16943 | -1.41316 | -55.37901 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c45f628-0fb7-3204-b3f5-1e6bba59ba85 | -3.04973 | -50.3746 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 722722e9-9dc4-33d7-8cb1-45947694c9ba | -3.64848 | -50.13994 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 647032c6-b025-349b-a00a-b9461caab6d1 | -3.35373 | -50.26974 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 712d6201-5eea-39c5-9b6e-fc4eb93e1a68 | -2.87079 | -51.47176 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d774d63e-d2a7-346c-a28c-618c87749679 | -3.01339 | -53.4374 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45ca09ba-d3c3-3fa0-8ccf-c713966548fc | -3.23747 | -50.45193 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d6c3b5a-ed19-3d54-a4fb-07855121315a | 0.50347 | -50.69142 | 2024-11-09 05:20:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6517949-5331-36e5-a389-673085b74a41 | -3.02938 | -53.27531 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28dff7fc-39f0-3233-ad68-a26528a6a1f6 | -1.14493 | -53.65499 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README105.md)
