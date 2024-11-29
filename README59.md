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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbeea844-d81f-30e8-93d3-c96ddd3a59f1 | -3.77674 | -46.6926 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3dea4c23-f476-3361-84a2-071c9a93a3c3 | -2.97369 | -53.29129 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 13b856b0-ecb3-3b53-a2b1-73d5a775a6c5 | -2.59128 | -47.47626 | 2024-11-29 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 741707c3-9b32-3a58-8887-6694c6c74079 | -2.84484 | -54.07359 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35494cd2-3690-32ce-9de7-a3d76c16f1bf | -1.19014 | -51.76803 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ef85aa0-8650-3432-92d2-71d7caf4cdf3 | -2.83506 | -51.83948 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 354c27f7-bc57-35ef-bb74-e741b36fa496 | -4.23092 | -46.88347 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a98ef10a-afad-3983-9373-e51c959c5639 | -3.09094 | -53.28117 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b78a877-8a96-3f24-88e9-d0a0f90a3447 | -3.04438 | -48.49232 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff1ff5c3-307f-3859-9686-9dfca83bc0b2 | -3.93597 | -46.72054 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8afdd04-a6f0-391d-8765-f15986764bcf | -2.86212 | -53.98461 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d9e00fa-2e51-3e36-a8de-7c433b93ea3c | -2.53539 | -53.98615 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ad1a5bb-2f7d-3269-94f1-443e1e6a83c4 | -3.1696 | -46.29884 | 2024-11-29 04:57:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73123ebb-1ece-33e9-b9e1-bd7340f22b2e | -2.74628 | -54.16005 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5e45b34-2bbd-3366-97fa-5bff007c8a3e | -2.58861 | -53.97332 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0eaa0be3-64c2-3948-b79a-a6e5df069ad9 | -1.09416 | -53.36952 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ee2ebe6-e086-3889-a3ef-42e7b5fb4726 | 0.03432 | -51.10948 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| bf9e5bb2-67a0-339f-ab6a-797a674b771a | 1.22149 | -55.94313 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5627655-4a54-3d55-a3be-4a4da79d4b7b | -1.46683 | -52.68168 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 030cca0b-88ed-35f3-956f-efc18d53de9e | -2.84153 | -54.07308 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 53b52915-a4d5-33f4-9211-e309f9e9b077 | -1.44153 | -54.52055 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce0b5f35-b5e5-35e7-83ec-43d66e8372d8 | -2.85141 | -46.82041 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75e0e066-0fd6-338a-be0b-4616e7aaa9ab | -3.24587 | -53.64008 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba4dd67e-16d1-3a55-8b1e-13a83b070794 | -3.69202 | -47.12995 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe638a48-60e2-3199-920f-59b973f3e4b0 | -1.49206 | -51.99343 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c572a155-1291-3b51-b5d2-e84f4a16ad9c | -2.53948 | -54.04678 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23f87a3a-81c8-3aa8-9620-3e77676622af | -1.32706 | -51.9206 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b9e860a-af6d-3cb0-9cbf-288e3d62b2b8 | -0.81615 | -51.61858 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ef85b7a-84fe-369c-b106-58649e0ec745 | -2.2085 | -52.10664 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c223c6e6-9e7c-32c7-b84a-cb63f3108477 | -2.86851 | -45.53913 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60ee6ba6-9aa7-39a8-8a68-312cdcdcc5c5 | -2.38419 | -54.47392 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af01db5f-ef6d-3de1-b74a-3b2d62f32327 | -4.39622 | -47.22849 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b27058a0-0387-3a6e-85e4-70de7c7e1f00 | -2.89287 | -55.2247 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fdc69b4-cb62-3a9a-96cc-6a01044367d8 | -1.15426 | -51.69958 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f1d108b-43e3-3be1-a2a8-4a602ab28224 | -1.10395 | -53.61353 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd3706ca-7dd2-3bbe-977e-9f54f43aca27 | -1.59895 | -52.29192 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e0dd1046-a9ce-313f-a9bc-abe61ba5cbaa | -3.50827 | -53.79052 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 078c0d52-17b8-36cd-bd5d-c37b737d97bb | -2.96857 | -53.89201 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ba9fc4e-5a85-3760-911c-2813feed04b1 | 1.28624 | -55.94646 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 160fdbf0-3b05-3004-9fb8-2eea60a32079 | -4.78827 | -46.11427 | 2024-11-29 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| aa913bc6-6bf1-3350-b488-e8246e5522f3 | -2.70124 | -52.0013 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ff28bdf-36db-37be-9708-c67460a55ea8 | -3.11142 | -54.00272 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 433c5f4c-42d5-3513-a02e-09fbae076260 | -3.04867 | -48.51878 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6612cce7-1b4f-3a22-b746-6f907b41f695 | -3.57038 | -53.26099 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd67aef0-39a6-3d3c-a549-7c6976cd5b3f | -1.10469 | -53.38869 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0164725a-e258-3ac8-a38a-5b24440f39c7 | -2.82622 | -54.10602 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ae1b28d-64b6-3b7f-9b1e-78c5f039b1ad | -3.28286 | -53.01035 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45666a73-19c1-3ac2-8935-dd6394788df6 | -2.52947 | -54.02406 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a6d62dd-907b-3950-b577-37b00a964edb | -4.13098 | -54.89787 | 2024-11-29 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8a69d66-b184-3766-8dff-a9279ebe149e | -2.5818 | -49.99754 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f3dc0ffa-2f1a-3f1b-b1ff-7cc05e8faae7 | -0.98172 | -53.72123 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a181fb8a-cd4b-34e7-8ee1-cfaf8e75ac74 | -1.35965 | -54.63393 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e54ad33-1ddb-3335-9b9c-1c73ddd37991 | -1.75449 | -46.25228 | 2024-11-29 04:57:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbb30e47-0ba5-3f1c-aa87-4626dc95b486 | -4.08348 | -46.82951 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1854b954-19a1-3572-8fcb-732e1961a700 | -1.91959 | -52.89703 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ead885f-9d0b-32c9-abc8-b866aaa47fba | -2.82668 | -54.08138 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80a6d4c7-0f5a-3c1e-807e-e0fc351f97fe | -0.07514 | -49.66059 | 2024-11-29 04:57:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 713932ce-77db-37ca-9d1a-1198f3dd8db2 | -2.14021 | -54.90224 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 178611bf-6ebe-3b5c-a705-7671f0bfdd48 | -3.42465 | -53.88947 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e90ed296-da4f-3d6b-8a04-46455a73a971 | -4.22792 | -46.53839 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd46e4aa-88a9-36e6-9043-7c52b6e04486 | -4.07173 | -46.82141 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 635dafe8-6523-31b2-ab1c-7b0e7dec4f9c | -1.79125 | -52.73921 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8059ef6-cdfc-3d3c-b93f-2c478b3b38c0 | -1.62924 | -53.86518 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75191e5e-44f7-3ee9-bb75-44e883339288 | -2.96612 | -45.22955 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9adaedbe-20a1-30dc-a823-09a80f22fc51 | -3.51157 | -53.79103 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec5a4bb2-4f15-3d67-8443-8e5e499dca40 | -3.97937 | -46.7381 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 52f4f39e-9d88-3b09-ab4f-95713c86c5fb | -3.09425 | -53.28167 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d834afe7-e6ba-3f80-91ec-85fb9e443e55 | -2.86894 | -45.53629 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38143375-7d13-3789-8a28-9c2309f447ea | -2.58479 | -51.93933 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb55548b-21ae-3e59-933b-85f162b54959 | -2.65825 | -48.78557 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c5b758c5-03c5-345b-95ff-4e1e930ddc02 | -1.447 | -55.1582 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b94f0b2-1bfc-33a7-9f42-f45e2e886458 | -1.23436 | -53.36313 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 993fa5f7-e9b5-3e42-a261-a11bf5683cdc | -1.2458 | -51.78764 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f454a19d-d49e-32e2-a5d3-0707c65721ea | -1.80916 | -53.58339 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85ebd445-57bd-355f-8080-1162220b412f | -2.85157 | -49.49927 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6acfeb02-e136-30b1-9e7a-31cf467543d4 | -2.62059 | -53.9853 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b94f926-9399-3389-b681-b1276a1331dd | -1.6826 | -45.79074 | 2024-11-29 04:57:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f82b770-3259-33b2-862f-b7cad1aa3131 | -2.86014 | -54.04069 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7afc6eb1-de39-35fc-83c6-bc1f9c7961ef | -3.25602 | -53.70863 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40d28e27-21ff-3ba4-89e4-925889a5b3f8 | -3.41296 | -50.16815 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efed1ad7-43b2-3481-9b95-ecc58fd0d467 | -2.20684 | -54.52122 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08d09f73-c6c2-37ae-9d81-b5b2af660b1f | -3.36182 | -50.40698 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c83faa7-ba59-3490-8225-4dcfdc3e549f | -3.47281 | -50.53861 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d207a1fe-1371-3435-9a35-d0273177d8c6 | -2.51216 | -54.11322 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a77acce-6cc1-3ac0-b76e-b56cacecdf66 | -4.17381 | -48.6242 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e7d7d685-aed4-3d3b-b410-4d29af5cf3d5 | -3.51542 | -51.32122 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73613c10-8b55-3bae-a367-e045f0f229b3 | -4.04563 | -46.83752 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9201f212-5bc1-3776-a222-47de4b6d785f | -2.1128 | -50.5977 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4fe1b41-425d-3fb7-b179-763c62f6bb98 | -1.07168 | -53.38361 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd3ec4f0-2077-3151-be6c-003110cd1ded | -2.20151 | -53.75083 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d49347f0-76f4-36f2-950c-980375c4ca0d | -1.16094 | -53.68203 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a57dab51-6078-3f0d-a121-fc0ee2ffe1ac | -3.23873 | -53.92755 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3662c4f1-76d3-3c49-ad38-ba84e80696f4 | -2.84422 | -54.05586 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aeefabc5-871a-310f-984a-ef4e39b21f72 | -3.26366 | -54.11451 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0629a2db-5b99-3975-804c-f66452c6d66a | -2.7465 | -54.07176 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fde170e8-7886-36d2-9784-935aa368fdc7 | -1.69394 | -52.20546 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed91b012-933d-3653-a8eb-2c1dbd8b2530 | -3.41858 | -53.88501 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 181e8cdf-f51b-3516-89f0-c4b6bd45de7a | -1.66055 | -52.72562 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9a7210d-fc29-3b8d-a32d-ca9ce5ffbd9d | -3.15193 | -50.86236 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80270a80-c36c-32f4-8bc3-f307a5ad3d87 | -3.59819 | -49.99027 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README60.md)
