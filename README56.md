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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da0099eb-3245-39e5-8eaf-4e4e6237c202 | -5.4314 | -60.18552 | 2024-12-03 05:22:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70ac0b79-d479-31c7-8821-f0af024ca70a | -3.65652 | -58.58224 | 2024-12-03 05:22:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed37dea2-687c-3f10-8ba2-a425b0965b57 | -3.42132 | -54.02758 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f726442b-237d-3523-a95c-70d2025357c6 | -2.61644 | -60.02586 | 2024-12-03 05:22:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aeae085-8c5a-3034-a80e-09ee12c6a4de | 4.09421 | -61.19957 | 2024-12-03 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b05157b-dec5-30a0-aaf0-3370b77f5213 | -1.07854 | -53.4504 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| afe32fd3-7d3a-35a6-bd5d-d926606209f3 | -1.08224 | -53.45523 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 79fd6f7d-6423-37a4-b5d4-c5b50bd33319 | -1.08657 | -53.45597 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 6ce9a7a9-063d-35b6-ae5d-934e92e7b973 | 1.10406 | -55.99028 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa2b2c5a-be19-3cc9-982b-fcc4d95fcca8 | 0.9183 | -59.70119 | 2024-12-03 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0de4310-a34d-3db5-8a1d-81544de3086d | 4.29231 | -60.8814 | 2024-12-03 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a4020524-9f06-3165-9969-c9a8c14ec85d | -4.04661 | -54.22856 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 921be28b-004e-33f4-8d45-a57c34676b35 | -1.79621 | -46.65633 | 2024-12-03 05:22:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e0a6508-bcab-3a3d-b19f-1f12eb85e075 | 1.67959 | -55.99151 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de16a038-2882-3ddf-9390-8c8eb3e9132d | 1.42868 | -60.80145 | 2024-12-03 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57db4b62-a80e-3f78-bca1-8f35eac48dc7 | -4.04107 | -54.23606 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bd99d0e5-15fb-3bf8-9ddb-7287db55268f | -3.35872 | -59.53944 | 2024-12-03 05:22:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb46c291-1253-392b-b726-d3c031d03c96 | -4.03884 | -54.23874 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de894085-d038-3b46-9f20-40b22c1a8045 | -4.90154 | -47.14346 | 2024-12-03 05:22:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 19372635-9a29-3dfa-8ea0-34514ea50ef4 | -4.91667 | -60.1717 | 2024-12-03 05:22:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 610e5b6b-5c17-364b-8cb9-71fb3d8a7888 | -4.18088 | -51.18438 | 2024-12-03 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 802488c6-6588-3f6f-bcf7-a8e46a8e4a77 | -4.046 | -54.23256 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d71221ad-072d-3b72-816f-9462b30e955c | -3.79705 | -58.9701 | 2024-12-03 05:22:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f67c22c-b046-376e-a647-1885314d58fb | -1.07356 | -53.45384 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b19b9dc9-c47f-3336-a197-c948ce550d4c | 0.85353 | -59.76411 | 2024-12-03 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 503c663b-dcb0-3f21-afee-533008350953 | -3.5125 | -53.83192 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a917dcf-26d6-3eb2-8234-4ae40a6348f5 | 4.06896 | -60.67909 | 2024-12-03 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a1b68cb-d83b-3c64-bd5e-768ed96a0704 | 2.72993 | -60.39148 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.5 |
| a0a4a002-01d8-3576-a203-ad1edf15fc2d | 1.10638 | -55.98147 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fcbc0e5-e712-3dea-97be-d1afeab32222 | 4.09774 | -61.19901 | 2024-12-03 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2a43e8f-bde6-3a21-b4cb-1b56a8213f47 | -3.49744 | -53.84266 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a54c6e68-65c3-3695-b0bb-1c4ab280166d | 1.31071 | -60.40626 | 2024-12-03 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab8e1691-2105-3c9d-b92e-8cd1b9366454 | -3.51237 | -54.55547 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0553378e-73ea-30a7-9a06-ff2a96e32733 | -3.3419 | -54.63142 | 2024-12-03 05:22:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40f36a70-c01d-3276-a2d2-c70dbdff3a00 | -0.61789 | -51.69281 | 2024-12-03 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d563b274-5306-3923-8fc4-4ae7e473e9fc | 1.10682 | -56.03203 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75840704-e510-3bba-a77f-3a383d813504 | -5.43193 | -60.18207 | 2024-12-03 05:22:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdb28ebd-5487-3657-bd6e-cd258ed9b5f0 | -4.17789 | -57.54391 | 2024-12-03 05:22:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a51755d-f1a5-3962-b0cf-e3ff7a315dcc | 1.00122 | -59.46625 | 2024-12-03 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e514b84c-d494-37a0-81e3-06a175a0378b | -3.43576 | -54.11003 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35aa5cb9-7ed7-394b-bd77-e07c1d1306cb | -4.03939 | -54.23488 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| beb19c62-53cc-39de-921f-5fbb0bba64d6 | 1.10547 | -55.98734 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 54063fbe-7020-36e0-bfdb-c95d1a3e382e | 1.13162 | -55.9664 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c860117-aeba-31a0-8dc3-a8bc739e7049 | 1.12214 | -55.97632 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50f2c2d3-2fbb-39cd-be26-68cebad95156 | 1.08801 | -56.00552 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24dc284e-cdbf-3761-89df-b023b7944911 | -4.03735 | -54.23154 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa156263-ebde-3b4f-afbb-33b3f89f115e | -3.65313 | -58.58173 | 2024-12-03 05:22:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e21fb283-2d23-3832-920c-a2338c994579 | 2.73614 | -60.38681 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 237337f7-7287-34fd-9c18-86c35fa3fa9e | -1.08351 | -53.44699 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4effd2c7-1a72-3167-a0be-4ee893fe025a | 1.11494 | -55.97742 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45b3596b-376e-32ee-967d-88de882827d2 | -0.85902 | -52.70819 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 409ecffd-91cc-3d6c-aed7-74f971eaba45 | 2.73332 | -60.39095 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 6df3b51b-1a16-3888-ad9b-8c2c4cdf8e24 | 1.46028 | -55.8641 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19883fa3-ec79-347b-986e-296779399fbf | 1.46093 | -55.86824 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ee4b73d-2ea7-3130-ba7c-d1ae2f094149 | 1.10701 | -55.98559 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c6b20df7-e244-3803-aec0-6917534cdb1c | -3.47109 | -59.53902 | 2024-12-03 05:22:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 963037f8-5e3c-3f10-8d3d-776310c39442 | -4.04167 | -54.2321 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df83bb80-c7e3-3331-ac4b-e9cc3589bfdc | -0.84798 | -48.72277 | 2024-12-03 05:22:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c304ce2-13da-3c1b-96f3-29839ad8006b | -3.7965 | -58.97364 | 2024-12-03 05:22:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e853c38f-41cf-352e-bb61-b009c184959f | 1.10841 | -55.98265 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66808d71-4a50-303d-9c6f-18890f0dc8a4 | 1.10998 | -55.98091 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b8ab773-f73d-350c-8950-ec1633794501 | -3.37977 | -59.55684 | 2024-12-03 05:22:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87937ced-55e5-36c1-a0e6-7f481b746c4a | 2.42342 | -60.65456 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3512b9ad-7850-3d42-8300-c73274550e2f | -3.47055 | -59.54248 | 2024-12-03 05:22:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01477c25-9439-338d-bec6-269dc390008d | -0.61386 | -51.68665 | 2024-12-03 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f61ea68f-c82d-313e-94a4-ab116714df39 | 1.00176 | -59.46968 | 2024-12-03 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45082e7d-fae5-3860-9aa3-9f4d9a6d3b37 | -4.04372 | -54.23535 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c75a12f4-b53b-3347-ac9a-643ab83186df | -1.07917 | -53.4463 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 956f67b7-7f3b-32a3-878d-bc6af87da15a | 1.11204 | -56.02841 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43da1965-b162-384b-b21d-39fd408ce579 | 0.61636 | -59.63897 | 2024-12-03 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94c48108-a35f-3a18-8b0a-584471eb4a6b | 1.13954 | -59.54641 | 2024-12-03 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bd2f7f8-1d21-3e85-893b-6d4675ec47c2 | -4.0443 | -54.2314 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87eaecbb-f3a4-3208-8085-c7012019f725 | 0.59585 | -60.46604 | 2024-12-03 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8015fcd0-8ceb-3a11-9caa-4914bbe41829 | -2.94717 | -60.02145 | 2024-12-03 05:22:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9b4ae18-1944-3686-81d1-1fe14ea46fc1 | -3.42113 | -53.9984 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f9af341-f88d-36f3-9dea-18d3f96912b1 | 0.74488 | -59.85223 | 2024-12-03 05:22:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f8f93a5-097a-3d4c-a85d-3ad4c6f876d4 | 1.11103 | -56.03556 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8effc3d4-c52c-347c-bb4f-4d790e0da038 | 2.73727 | -60.39406 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 856e81c3-38a4-33f9-827b-3322ede219d9 | 1.10481 | -55.98321 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27d0816c-3f6f-3b3e-b075-d6531db6c8c3 | -3.89992 | -53.43555 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d407e750-77f0-356d-9f2d-3b7eee74a2a5 | -3.67342 | -54.58236 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a8b062e-1eb6-3a40-98ee-f756780bc860 | 1.11138 | -56.02433 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c34eae2-e060-3bd4-84bb-cfab8724e581 | -1.0742 | -53.44971 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03da9c95-b2d8-3598-8485-c6e807a5f96e | -1.26123 | -51.58662 | 2024-12-03 05:22:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 359f4f4c-ab91-3931-9a44-56e3fbc548a8 | 2.57749 | -60.69926 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff5d21a6-2b52-3d1e-a0e9-cf7c2c5fbf73 | -0.97632 | -53.09263 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c9a2a33-f8a6-3bde-bd97-7df730a27562 | -1.7288 | -47.05796 | 2024-12-03 05:22:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e79e0b1e-7fdf-3b3f-b5bd-b9c6993f7d59 | -1.08287 | -53.4511 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2c6a86c7-95fb-34bf-b90f-15fa87aff769 | 3.07433 | -60.52998 | 2024-12-03 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2155cdd-293f-3499-8147-2d7776ed868b | 1.05948 | -60.60209 | 2024-12-03 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d94e65d0-a1af-3ab2-88eb-8039b9c32970 | 0.83888 | -59.99758 | 2024-12-03 05:22:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 88edf0b9-aded-37f3-b18b-a84851861999 | 2.5735 | -60.69608 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3a215b8-76df-31da-8f13-2da73d572764 | 1.3051 | -60.4144 | 2024-12-03 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed5cd35c-ca4d-37cd-bf67-89e41309d025 | -3.86157 | -52.2691 | 2024-12-03 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f416d734-c9e4-321f-ab14-ece6c78bc8cc | 0.64987 | -59.6585 | 2024-12-03 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6a5e81a-de05-3a7c-bddf-be713b28e263 | -1.0779 | -53.45453 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c71ab80c-0441-3541-809f-0cdc2beb8a85 | 1.45668 | -55.86467 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e707b3fe-9da8-3448-8fa5-6fab3d3f0bcd | -1.07725 | -53.45874 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b31b155b-b08e-39a2-a422-ac86530090cd | -0.84269 | -48.71745 | 2024-12-03 05:22:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08843068-6766-366e-bbee-1073e038aaaf | -3.49113 | -53.97509 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README57.md)
