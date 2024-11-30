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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c288ea6-89c6-34a5-9249-b7fe0032fe01 | -3.6758 | -47.1176 | 2024-11-30 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c8961518-b69a-3897-bed1-595fb56cd622 | -17.6651 | -57.585 | 2024-11-30 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 611c4190-02ad-3264-9b24-51d7af322364 | -1.0022 | -51.7235 | 2024-11-30 03:10:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 606a40d1-0657-3df7-9748-4b41a0353575 | -4.8713 | -41.2915 | 2024-11-30 03:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 167.1 |
| 4a4c1805-4b50-347e-b753-856b1041f87b | -4.8711 | -41.3157 | 2024-11-30 03:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| e75be45b-f910-3b79-93eb-a53625900766 | -1.6938 | -46.7833 | 2024-11-30 03:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| e23e1aa1-a17a-33ee-91f7-9aa37cacf632 | -3.259 | -53.6388 | 2024-11-30 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 8008e5dc-b063-360d-847b-807e7517fb2e | -1.2015 | -53.8782 | 2024-11-30 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3430f6a9-d913-35ed-b577-6b764c32a2e4 | -3.4975 | -53.8137 | 2024-11-30 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| caec0028-f577-3e3c-b46f-ea6270265cf4 | -3.4976 | -53.7935 | 2024-11-30 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 81016a95-6cb1-3b64-945a-08b92db045b3 | -3.0171 | -45.0974 | 2024-11-30 03:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 6af51997-970a-3fbf-9b80-c717868dce16 | -3.4791 | -53.8142 | 2024-11-30 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 43aeb20e-0594-3154-984a-b9b2eed6917b | -17.6654 | -57.5645 | 2024-11-30 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 80c50d13-a823-3c6b-9c44-f46b6da55e74 | -4.8901 | -41.2902 | 2024-11-30 03:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |
| bac3c691-9eb8-3b74-81f5-c1a5d8235873 | -3.0171 | -45.0974 | 2024-11-30 03:20:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 570d0118-8085-322b-8660-80304a78a491 | -2.1351 | -54.8861 | 2024-11-30 03:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 902c6e22-5026-3879-abe0-af5928d9bd0f | -1.2015 | -53.8581 | 2024-11-30 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 98bf1a1a-2c4d-3050-88a9-53ac3f847704 | -4.8715 | -41.2674 | 2024-11-30 03:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 2d93a7f3-09bd-3c11-b7de-34bc1e53bc9f | -3.017 | -45.12 | 2024-11-30 03:20:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 921f3042-c389-3188-9e14-7f31adb9b21d | -3.2591 | -53.6186 | 2024-11-30 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2a96f5c7-07fb-3bef-b4b3-fee013758f6c | -1.0022 | -51.7235 | 2024-11-30 03:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 38.2 |
| bfdc7d9f-f67d-3d59-87be-c2b525923bdf | -1.0733 | -53.6378 | 2024-11-30 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0b9d3288-2883-3c70-a42d-a6ed88247d2f | -3.4975 | -53.8137 | 2024-11-30 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1a439678-e3e0-333c-b0e7-a0465820c559 | -3.2406 | -53.6393 | 2024-11-30 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| de7ca31e-2718-3b3d-a44e-b7896b217e7a | -1.6938 | -46.7833 | 2024-11-30 03:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| fa79233f-4440-373a-8f15-0c0375ee7b49 | -3.0356 | -45.1193 | 2024-11-30 03:20:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 93fa58a1-9af0-3c55-a189-6a4d505e0f82 | -1.2015 | -53.8782 | 2024-11-30 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 7d367835-3e0d-3e50-86fe-9a8cc120de77 | -3.4791 | -53.8142 | 2024-11-30 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 790ffbeb-e712-3fa7-8824-dd0bf7d24a11 | -4.8713 | -41.2915 | 2024-11-30 03:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| ea85b80b-2444-3af5-8bed-dcef643d1c98 | -1.6419 | -53.8731 | 2024-11-30 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 6071099d-3f6a-30f3-8669-73447ee0d2c0 | -4.8711 | -41.3157 | 2024-11-30 03:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 4df4229f-6267-34bd-9650-b9b2b39602b5 | -3.6758 | -47.1176 | 2024-11-30 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 52fa48a3-7fa9-337e-b6d6-dce2f3d3f8c7 | -3.4976 | -53.7935 | 2024-11-30 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 87caff0a-0267-359b-93a2-794bbf94e926 | -3.259 | -53.6388 | 2024-11-30 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 1c664fb1-35bc-37ae-aeb8-4fa731897354 | -4.8901 | -41.2902 | 2024-11-30 03:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| c8a765a2-1c16-37e2-86a4-ad0b18e2a7bf | -4.87636 | -41.30259 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ddebfa1b-5894-3f0c-8921-37d9ba7d7fc0 | -3.99317 | -41.52189 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 91b6f199-fbf0-3395-8615-7ca791ecc4e5 | -6.91182 | -43.54602 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 71a573ee-c00f-3bcf-ac6d-8e81a3db2189 | -7.2158 | -39.05871 | 2024-11-30 03:21:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| afe9c074-f6b1-3402-9787-34f0c4af3a74 | -4.88102 | -41.30485 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 428cc5dd-e784-36ad-a455-2f073b4fcfb9 | -4.86897 | -41.30869 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c9a444a5-632c-387f-b2d6-a346550f897e | -3.96788 | -41.51772 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 698745dc-f026-3c0d-a13f-1c4c7f0fc1e9 | -4.87312 | -41.2783 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 54a2ba5b-65a6-30f3-9e50-bdc989dacbd1 | -4.8564 | -41.30083 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 42040901-c9c5-3765-9b2e-e8220072eb94 | -3.98164 | -41.52591 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| aa7471d9-1f3e-3aff-8014-a1f2a8c14736 | -4.6843 | -42.37424 | 2024-11-30 03:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6842b597-ddd3-349f-9e4c-2512a40acf13 | -3.98686 | -41.52079 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c31ab94c-be8f-3387-a1dc-127ec47c5959 | -4.87192 | -41.29162 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| a89ce2db-08bf-3c86-a19a-7ad6b4609370 | -6.66691 | -34.97355 | 2024-11-30 03:21:00 | NPP-375D | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3f17c279-e7ed-39b0-8ed6-6a372cd20a96 | -3.97332 | -41.52394 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d2499f86-9951-3a4a-a1e5-fc49fe4f4c87 | -4.85647 | -41.27128 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f3e66f5c-2627-33f8-b4d8-23220ba2e32b | -4.87659 | -41.29424 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 111ae90f-e585-3530-8d3f-b30b311a9ba2 | -3.97172 | -41.50851 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 85d73dfe-a114-33ef-bba9-dd4393067c8b | -7.21126 | -39.77394 | 2024-11-30 03:21:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8512e9f2-a8ca-3e95-a3b9-93d36aa6725f | -4.84806 | -41.31967 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 3e436591-01da-3213-bfa0-9a8043717935 | -4.87217 | -41.31885 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b87ca477-2900-31a8-baef-2f43dbe8cbb1 | -4.87114 | -41.29615 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 62b6315a-b08f-30f9-aba3-cf900d69088a | -4.68187 | -42.37367 | 2024-11-30 03:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e23e03bb-ab55-3375-b50c-d2e1ea89ab55 | -6.68421 | -39.2634 | 2024-11-30 03:21:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5de56197-8ef2-30e3-91e2-6055aeccb8a6 | -3.96806 | -41.52907 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3a2079b2-c394-3586-8117-760225e748b0 | -4.86163 | -41.30692 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 47abbd4b-3d9a-30ed-a541-ebe9a4d920eb | -4.86525 | -41.2936 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 81ddf91b-0f74-3106-bb87-749e4d762385 | -3.99067 | -41.51167 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 12c2b091-fc9a-393f-bc52-022e0f9b3887 | -4.04061 | -41.90678 | 2024-11-30 03:21:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9ce6ccf9-7921-37fb-b1b2-134969243239 | -7.093 | -34.98786 | 2024-11-30 03:21:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7a9b9ca8-ff51-323e-bf4d-2e5772274c68 | -4.87464 | -41.26986 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 81193424-795c-38f0-8a3a-198150046c2f | -3.97594 | -41.50853 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| db219dbc-8ba6-35c5-8a0e-c1d956e75480 | -6.28694 | -39.59376 | 2024-11-30 03:21:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cf49d9ef-36b6-3ccc-8db5-2163f0ce92a7 | -5.98551 | -39.95495 | 2024-11-30 03:21:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7c90a6e0-11cc-3d9b-a261-bc81cca64810 | -6.91297 | -43.53983 | 2024-11-30 03:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| ce15ea35-bd17-3bd8-81ca-cfac6d6697b1 | -6.91271 | -43.54701 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 5bec8597-4b5d-3586-a0d2-8fdc3fec1d72 | -7.50302 | -34.88635 | 2024-11-30 03:21:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 807cd491-210a-3767-a507-9576aa429c78 | -6.67994 | -39.7061 | 2024-11-30 03:21:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a5d72257-d740-37a5-a94a-0875eac3be91 | -4.87285 | -41.31506 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 71830e14-d5ea-3440-95df-cb33d7540c91 | -6.90949 | -43.55865 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 64949d35-fd15-3fea-88b3-47ed7e78575f | -6.99537 | -35.2544 | 2024-11-30 03:21:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 872dc32c-a763-3bf9-90dc-33f598a341ec | -4.87063 | -41.29217 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0810943d-e43c-317a-8aa3-00d5f96e92c8 | -6.90834 | -43.56487 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a3ccb833-f48e-351c-8cfe-aa3d74cda207 | -4.86314 | -41.29855 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| deff1543-1dab-3e88-b211-7d959c3577e2 | -4.87432 | -41.27771 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 5a9e00de-0dbd-324a-a7ec-3e980f8da6c9 | -7.16004 | -38.7122 | 2024-11-30 03:21:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 6b8a807b-0c52-3835-83a3-dc022838f8bb | -4.88265 | -41.29573 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 910fab0c-3659-39a0-8573-7e30b14dc194 | -3.97531 | -41.52492 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7078ac09-0378-3946-b1d8-058fb8da7f22 | -3.99156 | -41.50661 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2fcc707d-5dc8-379b-8b83-69204378ef2d | -4.69087 | -42.37547 | 2024-11-30 03:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 55945477-4306-39a3-b3ed-5158481fc6dc | -7.21522 | -39.06196 | 2024-11-30 03:21:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d54be834-db62-340c-a1e7-7e7a67bf5809 | -4.85372 | -41.31562 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 6318841e-3661-3667-bc2c-3fe069b03687 | -4.86905 | -41.30094 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| ebd1e9dd-ee34-37b5-bf11-8c76adb64c57 | -4.86239 | -41.30274 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f3a6f750-2650-3e79-ba9a-0b3772ee6293 | -4.87493 | -41.31086 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 8f817bee-d44d-34c3-a47a-40490c73d087 | -3.97081 | -41.51364 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| cb5e861c-23d3-3a5b-8cbc-5983017004dc | -4.87039 | -41.30051 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 148c0564-4f4c-3afa-9bd1-0b81b1e19998 | -6.91515 | -43.56614 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| f9884b57-d4af-3910-a487-09a100cac6fd | -7.16066 | -38.70964 | 2024-11-30 03:21:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b495eb8d-e6fb-3006-81c0-9ad8a693deaf | -4.87354 | -41.3112 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 398019a9-e24a-3a7d-8d65-0fa18df89945 | -4.69296 | -42.38741 | 2024-11-30 03:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b0b9345c-4bfc-3ceb-93e0-326ca4444154 | -6.91711 | -43.56082 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 0f1a6b47-1047-384b-ba98-5ad5e8c24dcc | -8.27766 | -35.33005 | 2024-11-30 03:21:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15dc8fbb-507b-3398-b281-3a27c7face24 | -4.87949 | -41.28443 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 1ff10f83-7f87-3ef8-9e1b-47402efe456a | -4.85471 | -41.31017 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |


[Clique aqui para ver as próximas entradas](README14.md)
