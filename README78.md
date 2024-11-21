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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 751a2e14-b747-35af-8332-88d0ba1e9191 | -3.54213 | -50.52475 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| b415641e-908a-3243-a121-681513a33731 | -5.10127 | -43.16519 | 2024-11-21 05:20:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 98f3f41c-f72a-3eb1-9bd1-a7bb94059bfb | -4.15404 | -42.01646 | 2024-11-21 05:20:00 | AQUA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 76ab5318-bfb5-3fc4-98c3-ac10dbfaa4cf | -4.47897 | -44.74646 | 2024-11-21 05:20:00 | AQUA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc1bf319-f9d1-3b65-a003-36928c692703 | -6.81595 | -46.76678 | 2024-11-21 05:20:00 | AQUA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 223fe885-3422-38c9-b9f3-97149238d920 | -4.23727 | -46.10915 | 2024-11-21 05:20:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb318496-568b-3c03-9789-0ef359d2f22a | -3.30193 | -50.36449 | 2024-11-21 05:20:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| bd0a801d-2add-3a85-bfd7-59b302f96f5a | -3.7449 | -47.35372 | 2024-11-21 05:20:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bf38bd53-2a2a-338d-bdaf-f92d2fdb5d72 | -4.38876 | -45.5894 | 2024-11-21 05:20:00 | AQUA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d7d9eb72-4d8a-3283-b260-4a739798f288 | -6.18221 | -43.40446 | 2024-11-21 05:20:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6fb899e7-7001-3390-8428-5b7279fdcaca | -6.20538 | -46.22559 | 2024-11-21 05:20:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 095b8f81-3113-3a45-8138-130253232e1f | -6.82496 | -46.76814 | 2024-11-21 05:20:00 | AQUA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9ad8517c-2f30-3642-b306-03915393327f | -10.69369 | -48.80298 | 2024-11-21 05:22:00 | AQUA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0a480d8b-e07b-38e5-b8ed-13e1421c1c13 | -10.70319 | -48.80447 | 2024-11-21 05:22:00 | AQUA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f076e917-bfa2-3fb3-95c6-8974962c6db2 | -3.295 | -53.8597 | 2024-11-21 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e19293a8-ec10-36c5-88fd-853bd92e475a | -3.2767 | -53.84 | 2024-11-21 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 4751b25b-fdd7-3c0a-9012-ebbf0781fd75 | -3.2951 | -53.8395 | 2024-11-21 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| cda07c09-dc4a-3a8d-8b3d-d6d75a11ca36 | -4.2388 | -46.1197 | 2024-11-21 05:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8603c5a7-ec8a-328d-9904-2ea78c34be8d | -2.0259 | -54.5289 | 2024-11-21 05:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 942a4b69-fb24-341d-baee-f4c8f43593f6 | -4.5799 | -48.0349 | 2024-11-21 05:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7e5ff653-a043-395a-ab6c-6df47acd681b | -4.58 | -48.0132 | 2024-11-21 05:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f1beb08b-02d0-3c3a-9bff-970f7b6d0430 | -4.58 | -48.0132 | 2024-11-21 05:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| cc748da6-88f4-3d9e-8949-ba18f5ef2821 | -4.5799 | -48.0349 | 2024-11-21 05:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| afeaa07a-1c0f-3e34-8fe1-7c6e3f9fb0cc | -3.295 | -53.8597 | 2024-11-21 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| a570fb4a-d537-3328-bc91-ac646c51f19f | -3.2951 | -53.8395 | 2024-11-21 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| a58b4f72-965f-3c64-81ce-d471d6acaa8e | -2.0259 | -54.5289 | 2024-11-21 05:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a19d1c2d-5f21-33a3-9b50-91faf11ecc84 | -4.2575 | -46.1188 | 2024-11-21 05:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 152ad165-ca4f-344a-9fd1-f0a57b695668 | -3.2767 | -53.84 | 2024-11-21 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d12b6049-2c4c-3480-aa59-86958b5cf64e | -2.37125 | -53.83727 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05469ecd-03dd-36b2-9abd-964f102ab0f4 | -1.72763 | -52.7057 | 2024-11-21 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 851e3718-ec27-374f-b4a6-968096a7c934 | -2.71674 | -53.17426 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5a9f09d-131b-3114-b3d0-d73d1ff09a76 | -2.01041 | -54.52588 | 2024-11-21 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5b0ea649-4828-3dc4-addc-a4b20adcf596 | -2.91019 | -53.06087 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca4a6bc7-2ebe-37c0-aed0-65960041c8c5 | -2.41572 | -54.63811 | 2024-11-21 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 78ce4b3b-2866-3b6f-8b35-483148332898 | -1.96549 | -52.99995 | 2024-11-21 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e49b51e8-d0b2-3485-abe4-e58837439648 | -2.36468 | -53.83623 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a0dde45-d2e1-3156-85bf-461dfcb0abba | -2.92314 | -53.06913 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39c32043-3fb9-3003-8671-54b0577b6f2e | -2.06473 | -53.43299 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8f82116a-e464-381c-9da8-5d98bdfd4e96 | -2.01597 | -54.53163 | 2024-11-21 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 952fc654-3fef-305f-8938-a3ed40be1c3d | -1.97792 | -53.32942 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4cde941-4979-3b9b-8900-c1e81b21b63b | -2.91596 | -53.06658 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 60a015c5-8c17-31e1-8b2b-5999802c8272 | -2.14803 | -53.773 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 47e8bbfb-ba32-3c12-95f7-d1b793aa085b | -2.02228 | -54.53231 | 2024-11-21 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 7db778c5-6fb5-382c-80b5-a2d9ebced8e8 | -2.21072 | -53.71462 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80c97fe7-dd7b-3bee-9d0f-0e4ff39b2ebf | -1.55371 | -53.43771 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c2955b7-bfe1-3d0e-b7f6-8e5fe8c4c845 | 4.31187 | -61.25814 | 2024-11-21 05:48:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 685297a8-8184-30fe-bd37-412cd489b789 | -2.19956 | -53.65408 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e89b3d1a-84c4-3f60-8b9d-094e39008adb | 4.33191 | -61.17168 | 2024-11-21 05:48:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d65dddc9-d5d4-3696-b209-b2199b62e35b | -1.19855 | -53.67716 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c48ad89-da56-3bd5-940b-47cf0172e71d | -1.46336 | -55.455 | 2024-11-21 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fb9d245-1ed4-3371-9ff9-e62dcac55269 | -3.09898 | -53.2188 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0817e985-8e95-3cb1-9aad-5487337b42f9 | -0.83162 | -52.87356 | 2024-11-21 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 53bd20c6-6f48-3afc-9869-ef2d59123e8c | -1.78488 | -53.61574 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4fbd6b26-390a-3819-b1f4-fae1f10e8b6d | -1.46327 | -52.67649 | 2024-11-21 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a0b01f56-44f7-3478-a65b-3605ec190562 | -1.55282 | -53.44362 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f11d1c2-747d-33ba-8391-f347ccd3b70f | -1.73266 | -52.38924 | 2024-11-21 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 853868bb-d838-3ebf-9f19-f0b944c0acd3 | -1.12651 | -53.40705 | 2024-11-21 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ef1a48f-52f6-3dd3-9af3-d5c467e782b1 | -3.11217 | -53.17663 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc97f5c4-3272-363a-91aa-f378e0442994 | -1.61325 | -55.40927 | 2024-11-21 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ce733b8-6c3d-33fc-9e4b-017a253a7526 | -3.09988 | -53.21261 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 6224d0d0-a97e-346c-896d-f0600969b646 | -1.58716 | -52.92883 | 2024-11-21 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c05a8983-83e2-38da-941d-33264f00060b | -2.20312 | -53.65993 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 87907f66-ca08-3d3e-bcca-14cc0ec6ecf8 | -1.52914 | -55.3789 | 2024-11-21 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5e5baf00-4349-3f4b-868d-3315e60fc8cb | -1.72864 | -52.69912 | 2024-11-21 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5333483e-d5ac-31e1-aac6-c1c57b40c342 | -2.20398 | -53.65396 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 073d10ba-3308-3c30-851a-71185fe96cfe | -2.19646 | -53.65913 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b5c590cf-2ac4-3a86-a4fc-396c443921a2 | -1.13976 | -53.66839 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ff43efc-7818-33af-a351-5fb5c121c553 | -2.79143 | -52.55114 | 2024-11-21 05:48:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b6c26646-486d-3542-b896-92e51f55d4c2 | -2.20803 | -53.71967 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e2853e46-2279-36ea-9eb8-b0c28ed9cf12 | -1.72784 | -52.69738 | 2024-11-21 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c3cf641-0d8c-33a1-ae96-ba1ae33bdfda | -1.64201 | -52.61044 | 2024-11-21 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eaa2f153-e3f5-3cb8-b003-53894e315105 | -2.01115 | -54.52085 | 2024-11-21 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 73743e3d-3745-329c-90b7-4846b4865026 | -1.46226 | -52.68315 | 2024-11-21 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d032b9f0-9eb6-38ef-89cf-992c89ec95e5 | -1.78717 | -53.614 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 733f041d-d071-32bd-9e37-b3ceeba6b728 | -2.78764 | -52.55273 | 2024-11-21 05:48:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8df13fcf-474a-3237-80a8-b64e44fd62ce | -2.85116 | -54.00327 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8a182deb-35e5-3f11-9abb-53be8d6b1fe4 | -1.649 | -52.61159 | 2024-11-21 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2648ac9a-14d0-3433-85e3-c29d29402399 | -1.5275 | -55.3777 | 2024-11-21 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1cdc40d-700e-37c0-be30-e4f58043c4e4 | -2.91615 | -53.06849 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee325751-4b74-3b92-ad34-0ace7768e6e9 | -2.71742 | -53.17309 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7136bf46-0b5f-3171-bddf-9b0ddfd37ff6 | -1.19167 | -53.7224 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c23393f-9f69-3863-8e04-4c97806f689f | -1.65221 | -55.25657 | 2024-11-21 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a3f637e-93a4-3044-a4ac-1318f8dbb4f4 | 4.31122 | -61.25409 | 2024-11-21 05:48:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a30e97-ccba-3485-956d-30c706ce3474 | -1.36739 | -55.70009 | 2024-11-21 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a0ef930-2165-3542-812a-bcaae8621dd2 | -2.20982 | -53.72051 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fe81556a-a1cd-396b-b131-282eb610cf4a | -1.78318 | -53.59581 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 687d3fd6-918d-3740-a672-a55d29809581 | -2.33691 | -53.93331 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b67ed0e-7c26-3329-9fc5-033922ce5ae6 | -1.78231 | -53.60153 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 22d35413-41dd-37e1-b06e-1c7288feb2b4 | -2.61498 | -54.5403 | 2024-11-21 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec1c9ff1-2197-34e3-b28c-60e87795f5cc | -2.19732 | -53.65317 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e632bd41-f93a-3462-a03c-84ebd1aa68dc | -2.01746 | -54.52155 | 2024-11-21 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f576640c-d95f-3458-a03c-69162dfd0c9b | -1.73974 | -52.3904 | 2024-11-21 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f077fe2-3857-3c61-8607-a1e4738be713 | -2.02155 | -54.53723 | 2024-11-21 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 2129be73-fef4-3f20-94cb-760cd7ea21b3 | -2.61573 | -54.53503 | 2024-11-21 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1ec46b0-b5b7-3750-ac8d-3bc1a7ec79c9 | 4.31693 | -61.26634 | 2024-11-21 05:48:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38d0448e-f4e3-35d3-ac3b-ba18ac990aac | -1.78077 | -53.5975 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7812789c-e521-3026-94c6-300962f6c172 | -1.464 | -55.45076 | 2024-11-21 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1973604-b8c4-3384-bbe0-43e3e9fdd001 | -1.96456 | -53.00615 | 2024-11-21 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a52b3fd2-ce25-31b2-80f2-20cead08d41d | -2.19866 | -53.66006 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| e68578d8-2cc8-3c8f-bee7-41eabeb1ac80 | -3.09925 | -53.16851 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README79.md)
