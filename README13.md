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
| 42f9b9c9-6fe0-3862-831f-c855c8020628 | -2.8713 | -53.997799 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fa21197-b114-3ce0-bb0e-fad3c76771ab | -2.8429 | -54.054798 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4da6793b-3330-3e24-8dd8-0564d4be813b | -2.7638 | -54.115799 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36fa97fb-963c-3b0d-964e-248b102d60a9 | -3.1146 | -53.247501 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b5071eb-3b8d-34d7-8e0f-e234056482b3 | -3.7147 | -51.798901 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 030d1898-ed69-3e3e-9fdb-ba55ad6ebc4f | -2.587 | -53.650501 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c25fec83-d39b-3ce1-9c19-849b496f4d65 | -2.6105 | -51.792999 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ba3d51a-b9f5-3062-adba-fdc79cbcf8fa | -3.2626 | -53.630199 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84188979-cb5a-3a72-8518-a1117dfcabb1 | -4.7694 | -44.440102 | 2024-11-28 00:38:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d90aef7-953c-3d04-9314-0ff5bf4ac8c1 | -2.9228 | -51.715801 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b938df7-3f72-314b-995f-7b2de6b7dde3 | -3.2802 | -53.2966 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b2b5956-08da-3c4b-a2f0-e6c5f9f638bf | -2.8579 | -46.862202 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cef4940e-cbe9-3cee-b53e-17bd2b9ed404 | -2.9901 | -53.884899 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08b439fa-4bd8-3062-88e2-a46e554ff10e | -2.9663 | -51.000301 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7007731-856e-317f-90ea-30e730b1ee7e | -21.1376 | -47.849098 | 2024-11-28 00:38:00 | METOP-B | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0322696b-8cb0-3edc-920f-4b86b2549b44 | -3.2473 | -53.929298 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bbcba8e-a938-3e1a-b9bb-83de5a23560c | -3.6956 | -43.4226 | 2024-11-28 00:38:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 686b18f2-b644-3f8a-98f0-304fb5d2f513 | -2.2683 | -53.470699 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d11df953-452a-315e-b21a-ba79b36b69a3 | -2.181 | -52.1264 | 2024-11-28 00:38:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 076866bc-877c-3335-b5f8-a89dd9450c7e | -3.6968 | -50.227699 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f770413-3f5c-380a-9421-7a4fb688909a | -3.0617 | -51.0574 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bf94688-05ac-38f6-86cf-f3b660832d22 | -3.0852 | -50.256599 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43798d01-8941-30a8-af56-c8a6ad780d22 | -3.281 | -50.617802 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df026be2-1bc1-3565-81ce-a13ced78a26a | -3.7128 | -47.134998 | 2024-11-28 00:38:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a85a639-bd5f-3a42-b7a5-6e1d3074165b | -3.4682 | -50.535 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51bfde1a-b7ab-3f49-a414-6f7b87c2590e | -3.3197 | -53.747101 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c7cb102-8a00-389f-851d-abe50f4431b6 | -2.5429 | -46.921101 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55e13b0e-863d-3b26-85f0-354b2febf004 | -3.5117 | -50.3195 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 566001c0-0332-3e5d-992c-d59904594ec4 | -3.0678 | -53.680599 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e48d6d1d-7bad-34f0-be89-060aa5f51a8e | -2.2772 | -51.233299 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b439281-4021-38cd-ade9-830f29c2c768 | -2.0066 | -51.1758 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a871403a-f6f5-314a-970e-a734d3a5cb2a | -2.2668 | -53.463902 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 519f1d80-297a-3a23-b527-74bf5bc49609 | -2.8894 | -53.986599 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3c31368-121c-3f6d-a9e2-a038d05dd1aa | -2.8424 | -54.098499 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d96d7af1-9606-3a59-929e-3c56442cf3d3 | -2.8391 | -46.825901 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 497fb672-559c-3be5-a95a-aa6b709ac307 | -2.6148 | -51.948399 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49439d25-b66c-3f36-8c73-b22557a3d721 | -3.3333 | -52.755199 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c631b8ef-f3ab-3932-953a-399c5c0746f7 | -2.1636 | -48.706402 | 2024-11-28 00:38:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f15adcf-b1df-3d72-b28b-5e3e78eaea06 | -3.4213 | -50.2397 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14420be6-d454-33f8-a4f5-eec0fbe6ad4c | -3.5336 | -51.138199 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9141e14f-0e15-3124-8e11-1b710db081aa | -3.0039 | -53.3507 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51e9198f-1e86-342d-bab6-fff1cc3bbe2b | -3.2498 | -50.616699 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 146a3be5-0b2a-37ed-bb89-6a966f0fed91 | -3.0459 | -48.516399 | 2024-11-28 00:38:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6f0d520-f3c4-30e1-a2d5-38c3a2bda1e5 | -2.8382 | -54.0341 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cee20e17-8b99-38d1-9bcb-984865848237 | -2.8804 | -46.870602 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68243d1b-2fbd-38ce-b7c6-e53e70f11c6f | -2.0471 | -52.126701 | 2024-11-28 00:38:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08349063-8346-3959-a8b9-7ebd19099f1b | -3.2767 | -50.553699 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6b604cd-8f1b-3fcd-a3ce-aa4ec5ed814d | -2.2461 | -48.528301 | 2024-11-28 00:38:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b9ade6b-28d0-3e80-a6a5-4d11d8a96c08 | -3.5686 | -51.563801 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2d4e65c-9463-3202-810e-b3ae373caad9 | -2.8676 | -54.027599 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdc76a9f-7cab-3427-919e-5b2428fadadd | -2.6563 | -51.767799 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc601d90-2901-38ce-a71a-2fa075d796ed | -3.0759 | -53.2132 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d069bc-be98-376a-be40-3bcf6848c407 | -4.2275 | -50.881199 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b94ad786-29ad-3348-818d-721e5ee20262 | -2.8263 | -54.072899 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc37c4f6-d269-38f0-928c-ed5f72c05aef | -3.2382 | -54.164001 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaadf8c6-c0be-31f6-8b46-8237cca1e7a2 | -2.9788 | -53.880199 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c59dd7fd-f203-3bfb-adeb-e38e7912b480 | -2.7458 | -54.126999 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 057b0c76-5a1d-39b5-becc-c2bdabeb2a60 | -2.45 | -50.4081 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f45f479-8ac4-3a05-be49-88af9bcd2059 | -2.8558 | -54.066399 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c0e4c73-2a54-397d-8a41-1195aed4c34e | -3.6045 | -50.364799 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c342ae89-1745-3cfa-9d44-fa875398e20c | -2.8449 | -54.018101 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8ba0613-9180-3db4-abb4-b3c6868a3dcc | -2.8646 | -46.847198 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad80fe78-d04e-3010-959e-d874661fa04a | -2.8489 | -46.823601 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25a0d5b9-8560-3e75-9e7a-09d22e354d7e | -3.6521 | -51.386799 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56c68a3d-206e-3b35-addf-ed3ebc873a93 | -3.0701 | -53.278801 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ea9962d-36fc-31cf-82c6-89950419b6d1 | -2.8616 | -46.834301 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4374f64-414f-3354-ada7-82379cd923ef | -2.2426 | -53.676601 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e40f211-acea-3dd5-a172-c549b79c3f5f | -2.8409 | -54.091599 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7fc7789-c4a3-3427-9f18-6ff51f7a465f | -2.9689 | -53.882301 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb2a12d7-a387-36d0-8d85-a41b7e93d861 | -3.5315 | -53.772499 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 162e64b0-97b6-3adb-b0fd-44ec5da32e0c | -2.1659 | -48.7164 | 2024-11-28 00:38:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be91e58c-ff2c-368e-8993-13cb18c42b76 | -2.9458 | -51.590302 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecb736d9-e52f-3e3c-b0f8-f86b6f4794ad | -5.9778 | -45.365601 | 2024-11-28 00:38:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36a84e4e-e58c-3edc-b08b-4c33de60fc3c | -3.0054 | -53.357498 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 870ea399-d65b-3b69-8646-2e5226499378 | -3.5353 | -50.197201 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb71bc1f-a45e-3736-a3a3-7a3b163fd2db | -3.5179 | -50.301498 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca949f9-aef3-3d18-8035-b75e3b474fa5 | -6.1273 | -46.5947 | 2024-11-28 00:38:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60053b4c-5902-3bf6-8cee-740b79721326 | -3.1985 | -46.605099 | 2024-11-28 00:38:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 22ccda7e-50ac-39ca-99ec-e25a0e4d043e | -3.7882 | -50.131599 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1e91843-48cf-3f21-ba7d-27864c1b8454 | -3.8178 | -52.3452 | 2024-11-28 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebc5002f-a035-30f5-8a32-74410a955bfb | -18.790001 | -55.823799 | 2024-11-28 00:38:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a9e28df5-1329-3c5c-8326-e32d4093d10f | -2.7093 | -52.001301 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65633adb-51ad-3dcf-a072-104707b79a3c | -2.7654 | -54.1227 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf08cc6-98dd-3bd3-a003-2f94213b0de5 | -5.7607 | -46.264801 | 2024-11-28 00:38:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da9c5b99-26b2-3828-8d1c-8eb14dd9e3a1 | -3.0943 | -53.294899 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecb46a91-0216-345b-a370-a66292f6e3ae | -2.3568 | -53.909599 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7768082-bb42-3ef3-92ea-c15f7fb69e1e | -6.4846 | -47.4953 | 2024-11-28 00:38:00 | METOP-B | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ccd03635-7670-3fbd-a756-d8cc6059fc67 | -1.4082 | -46.628799 | 2024-11-28 00:38:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62ba16bb-16af-37c9-905b-d96dc39cbbb4 | -2.2925 | -47.1259 | 2024-11-28 00:38:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8662a984-77b5-38b8-901b-2c74e8fa0e00 | -2.6465 | -51.77 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed788312-7471-391d-ad3f-e44976994abc | -2.3584 | -53.916401 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6abfddc0-ad1b-3f6e-941e-bdaf4f8f28cb | -3.1608 | -50.587898 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88d7776a-dd1e-3cd5-9c7d-d98b3d374826 | -2.8191 | -54.132702 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2e6375b-8f98-39fe-a3ab-0886aa8ec157 | -3.4442 | -54.5317 | 2024-11-28 00:38:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06cc7cf6-4561-3bba-a6fb-2a3b20b83f6e | -2.6078 | -54.063301 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19ce1f2c-e58b-30ed-94b4-6e6ce565f57a | -4.7375 | -46.506199 | 2024-11-28 00:38:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f23e3850-fe59-3ec9-b385-3662004e602b | -3.5082 | -53.806499 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9dee404-718a-32c8-9695-2a86213d9bb1 | -3.5113 | -53.820301 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c7d0c3a-ad81-362f-8e64-9b923377d314 | -3.5197 | -50.309399 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f59f188b-39b5-3a7b-b532-4d69ef9102ae | -3.974 | -48.079601 | 2024-11-28 00:38:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
