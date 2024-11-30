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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df0c1e56-2c15-3f34-a667-275907484b53 | -2.75907 | -54.08476 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d79e5c4-4725-3ecd-aefb-f7c36be00b5d | -0.27783 | -51.63278 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e64ee4d-9a53-37a2-8db1-d565e41fba7a | -1.22739 | -51.73735 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c1a20af-f9f9-3293-8ca4-1de7beac6bb9 | -2.88772 | -54.16527 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49043f4e-9227-3c13-914b-a89fb3f0c3ae | -2.46314 | -53.70402 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5a8477b-216f-3b9a-a390-6f5db35a3343 | -4.91056 | -49.90359 | 2024-11-30 05:01:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31cbbb31-27d7-3ae8-9cdb-5c62eb5bb0d8 | -1.50249 | -54.95045 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 98945dc8-d0fb-3f9f-acb1-95205e44cd89 | -0.26219 | -51.49936 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e126486-3a1b-309c-a29e-b25804148d1a | -1.00624 | -51.7215 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 331aee25-13d9-3e75-8198-354e8bef04cd | 3.18467 | -61.03549 | 2024-11-30 05:01:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22216d97-f8a8-384a-ad52-05586ac91c96 | -2.67182 | -53.04153 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2886969-edf5-3d4a-8679-4c87bc341a46 | -2.67825 | -46.10172 | 2024-11-30 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4599674f-891c-3d5f-b2d3-31afddff8543 | -3.48798 | -53.8068 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 6c08aa95-45b9-352a-9fda-dd305533f648 | -1.39621 | -53.62622 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 232a4d96-145a-304d-97a9-da2cc86e9df5 | -2.22851 | -46.39277 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c83f8041-c516-335f-a27c-24b42c0eb467 | 1.37804 | -50.94621 | 2024-11-30 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd694d34-1c5b-367c-ad1e-d671a589c98c | -2.26728 | -53.46235 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06107b71-281c-33e3-a50c-01ec02af88a5 | -1.86701 | -52.94287 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38f5cba9-9b14-3183-9dad-554ba5a02dc7 | -2.47889 | -50.36484 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c51ddb0-b7e7-37b2-9c74-54b3c0cf5f98 | -3.69247 | -50.08797 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08aea3c2-cc5b-39ea-816c-38de9c6be5fe | -2.58581 | -51.92301 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7567ab5-934c-3ec0-b00d-3366b0bbad06 | -1.61413 | -52.00885 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01506eed-715a-3f3c-8508-55a0e50175d6 | -2.6164 | -54.21546 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2e8bef4-6376-3060-876b-86d992cb8814 | -1.58062 | -52.27076 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7abce94-2044-3c43-8fa7-d35ebb5dee13 | -3.36078 | -49.10067 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c60df6d7-b8b4-3932-9a1c-ddce80cc9dda | -3.60272 | -49.97303 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ebe5cade-eef8-3c38-bd73-276779f00f14 | -3.31189 | -50.0317 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b1257ac-1250-3b6e-8876-7bb3f4adb9d4 | -1.07155 | -53.62641 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4ac8b98-c7c9-3899-a641-b3d7463cd34e | -2.60269 | -54.06345 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0885924-ad34-3593-917a-636d4bb3139c | -2.61973 | -54.21598 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0a6928a-d3fa-3b0c-aa44-c6da43ee2a5d | -3.23377 | -53.91686 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f09bf684-104a-36f4-a37c-fc714377358d | -2.65337 | -54.08913 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7af9d2f-4427-3bd0-b983-f045bdd0fd7e | -1.58785 | -52.08519 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6142af24-52ab-3d77-af6f-974ea767f8cb | -2.73615 | -54.03463 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8eeb383b-460b-3a44-9927-672e191c699b | -3.82472 | -46.55231 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2d384b8-e9a1-3157-a7a5-42fa494b92f9 | -2.84117 | -54.1188 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7cefbb9-8cdf-3731-be28-f227f3a319e4 | -2.45192 | -54.01522 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ceecf12-a3b2-3a51-945b-4dc403b68e9b | -1.43799 | -54.52042 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73ba058b-c180-3557-9edf-4e0102154c94 | -1.70674 | -52.64574 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 589c40a5-4cd9-3e04-a376-0fb6b597d7f1 | -3.27854 | -53.6727 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62650c36-ed9c-34b5-bc47-a1d2bacb7330 | -2.98546 | -53.2881 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b4bedee-10d0-3973-924b-069897701329 | -1.55089 | -52.27797 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 66c33bdf-c100-3bb5-946d-f9b811e07235 | -2.58334 | -54.0997 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1562972-8966-33cb-ac7f-5022b2dc2a7b | -2.62496 | -54.07407 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91dd25e5-dcfc-3cbc-8d5c-2d449d03e883 | -3.107 | -53.18276 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf8fb533-5fe1-3f47-9915-93c788bec89c | -1.96941 | -48.43388 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 012f383c-8eb2-311a-b216-c88ec5cfb533 | -1.37301 | -52.55421 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2f6a488-73b7-3b7e-af71-79984c0a1db3 | -2.86577 | -53.31857 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d18ddfb-0b26-364c-8820-a79bf5adc433 | -2.8002 | -53.04571 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1021cf7d-f8c6-350a-90ea-daeb9934065b | -1.07434 | -53.63043 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d2a8d787-75e3-3d27-94c1-ad907d52208a | -3.69906 | -51.80334 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6359d2ac-5499-325e-8f18-717cf441ee21 | -2.88439 | -54.16474 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 130c5392-df26-3afe-be9e-2deb3d30454f | -3.70774 | -45.68707 | 2024-11-30 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5da4ed70-591e-3ab0-978c-effeb595d41b | -3.14541 | -53.83453 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| de2f8f4b-85b9-311d-8a3b-d4d9ee053015 | -3.03904 | -50.977 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0453e08d-ff04-3d55-b0ba-653533146b87 | -2.26424 | -50.35846 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b90a964-c666-3d18-a40a-93ec4726961e | -1.09412 | -53.39572 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acb4d717-e41a-3583-960d-1efac3b0921e | -1.35151 | -55.02589 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24943e72-9c8d-372a-8dd1-4e8b7e93b1d2 | -3.97863 | -41.5116 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 99e9131c-433d-3ac7-8f9c-5a958904c254 | -3.76703 | -50.1721 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d69aba22-c4cd-37ad-8114-fde62c12152b | -2.6178 | -51.8106 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a7cc6a86-1c75-3f0c-9cb2-07a2ab47ac4a | -3.49704 | -52.91252 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 446efda7-3d30-32b8-8780-d45b4e374ae3 | -1.29118 | -51.72661 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4038afd9-29ac-34e8-b6dd-d61659675a5c | -1.14787 | -53.54468 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8096dd41-3b22-36c1-9220-29a70d2e28cd | -1.42068 | -55.27456 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e28a69a-2b64-3b27-b760-c262febe5de0 | -3.91778 | -53.66688 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c54ddc5-6cd7-36ac-a81f-9139a716fa16 | -1.15984 | -53.68669 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| add09dd5-9839-3013-ad42-37d21a5ebb62 | -3.09417 | -54.03935 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c841544b-02f9-3880-a26e-fe3334445537 | -3.20245 | -53.42151 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a1935d2-f7f9-3895-ad2e-184066ec656b | -1.64484 | -53.87236 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| f7579ccd-293e-3d45-803d-a80c14e36e6e | -1.42397 | -55.25372 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e4ae03c-0ed5-3165-b97b-834078a4de92 | -3.37508 | -50.77155 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efb1ee67-5e36-3dc1-b79d-e8c10ff3b05e | -3.06053 | -53.68266 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c392afab-6dcc-345b-a64a-4d9edc427c69 | -1.16929 | -53.67007 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2b6bc93-d375-3bc3-ae99-a4f1e68937be | -3.33348 | -50.05297 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c318df0-6c58-3547-a935-d5d5db5a5a48 | -3.28191 | -50.62737 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f0769a9-6762-38a9-bb76-351c5e7c860a | -3.06815 | -50.32721 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f004e163-5246-3546-bbc4-fc5e6b0162e1 | -1.57599 | -53.75085 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff4cc736-57a1-3f3b-af18-98e3003d9d85 | -3.27145 | -50.56581 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d39a336-be0f-3ede-a652-09d0cdacd066 | -3.27476 | -54.69826 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44a5b6aa-6259-37c0-ab6a-c72b86069ccf | -2.25016 | -53.68161 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b08c911-1a0b-38db-8618-90c0295a9912 | -3.60051 | -49.98738 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 0eff90e7-66ee-3e98-86ac-a9de1669973a | -1.11963 | -53.61567 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c5b9250-f9c2-3648-875d-9365739de641 | -1.12026 | -54.06809 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c5f7062-2a35-3f8b-ae34-ef00225fbddd | -1.10923 | -53.38714 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ceef2cbf-d952-340a-b361-ac9969549c26 | -2.96682 | -53.94431 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea88dec8-f258-376a-a5aa-0792b1a86bfe | -1.18559 | -54.01817 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de07541d-0e5b-3c71-8273-d0533fca4295 | -3.17524 | -53.64234 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34a94568-febf-3dbd-bf89-f92046334c62 | -1.14329 | -54.11414 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2fb9fb7-0eda-343f-a79d-c73b0342724a | -2.32747 | -50.66705 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ede6634-876f-3db1-ac65-306528e4b5cb | -2.44905 | -53.96825 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d251bf6-291f-328a-a18c-3f6d51af8b87 | -2.57454 | -54.32986 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26ed9f34-c089-32c9-a4a8-469fa9ffb1d4 | -2.38177 | -47.87892 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be23c76b-3384-3289-9d25-b1eb5e578e2c | -3.24387 | -53.62368 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| adc101ae-25cf-34bc-bc9b-aa39e6c9ee7d | -2.41939 | -53.89546 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4466cc47-83ab-3677-96a2-e25e4f1aa3dd | -2.19997 | -48.33322 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45a85ec1-fa98-34cd-bd60-bdf462a8ba2e | -2.82618 | -52.96985 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 693f16de-9f81-38da-b496-808b30278bf7 | -2.98818 | -53.35938 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04e4ad21-a3c1-316b-ae82-1deb5356b2e4 | -2.66669 | -53.02945 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7748c201-1456-3841-a612-1b7b3cc7ce53 | -3.02456 | -53.42017 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README117.md)
