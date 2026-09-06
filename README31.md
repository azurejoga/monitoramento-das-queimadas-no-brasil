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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13de30d6-22c9-395c-807c-4ce7b5fa3bf4 | -3.76271 | -61.75931 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71802487-7893-32c9-a668-4c937be35785 | -3.84087 | -59.59291 | 2026-09-06 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f99f21f9-b9f4-3c8d-928e-94c0bf26b289 | -6.87838 | -55.61613 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfe151df-567b-3558-b2d9-d8c15beb352b | -3.7644 | -61.77066 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 164bec61-3aa8-34f3-bbd3-4e4e7695634a | -6.05852 | -57.79177 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d645cd5f-5b33-3fa3-bd65-35e42cd9fe61 | -6.06654 | -57.79731 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 361894f0-a65b-3681-9e68-caecee87e4f6 | -6.44161 | -58.15525 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 787be75f-7bb7-33ba-990b-0ffdf4f25558 | -5.32996 | -56.02793 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c863640-71f6-3552-a76e-4c6c89784275 | -6.06104 | -57.80481 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 079fddf8-8037-308d-afd2-5a01a6c67b00 | -6.84359 | -59.43015 | 2026-09-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60cf6f23-3703-31d0-874c-bcab9313acd4 | -4.67773 | -55.63999 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24624b37-d91e-3ca0-b31b-6d6b26e9b2c3 | -5.65976 | -60.24261 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6d34267-2e03-37a1-ae4c-31a38c6e1c13 | -7.27332 | -55.14856 | 2026-09-06 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fe2941b-4628-34b4-ab2e-9873b0ccff21 | -5.8478 | -60.25827 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4322b596-8a3f-36f5-8e52-bfcdf7200763 | -5.55583 | -60.23712 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdc40eaa-ea96-37c8-b9f5-fb6da4e14032 | -5.36193 | -56.04008 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 993d7421-4bdd-38fb-8e1b-18677df4e8ec | -5.57096 | -60.16391 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 601c8b3f-4842-3689-985f-967bbeb1160e | -5.13786 | -56.2682 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1affed8e-0f53-3437-aadf-c51cfa9c923c | -5.36346 | -56.02951 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f01dc3ff-6cf2-355d-a2d9-af4069fc6dc6 | -7.09704 | -56.50894 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d384584-35d1-37ea-9a86-2e0b23526df0 | -6.87542 | -55.61115 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 451dd551-b1e0-37fe-b84b-d98304183470 | -6.20499 | -57.77028 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 032201a8-3556-3bae-ae89-cecd29db7196 | -5.59526 | -60.24611 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f702ccef-4f55-3281-a441-35c8c97ac399 | -3.7785 | -61.76915 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da978060-a5aa-3caf-9441-073fd039e5a4 | -6.09052 | -55.59625 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 727fcc38-dbea-38e6-a96f-dda5fa85440f | -4.47227 | -55.09336 | 2026-09-06 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8cfbeb5-c680-3d2a-879f-acabb9ae69f0 | -5.33372 | -56.03071 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2eabf33f-2591-30c8-a81e-e9c85367289d | -5.14472 | -55.95339 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f0acc1a-c701-3df3-ad01-bb514d808dad | -3.92925 | -59.3424 | 2026-09-06 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3110ba35-5ee1-3f3a-a405-7cdbf6f46d4f | -4.66295 | -55.63823 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7e3eb588-92eb-33ef-8708-71dc416b4f77 | -6.88007 | -55.61483 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 849bedac-51e1-37e1-9b2a-1ce67dcd1414 | -5.59591 | -60.2418 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e7616cb-0832-33e0-aad0-4edbce0b408f | -5.3571 | -56.03939 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9bc0d67f-3165-3119-adaa-adeb58e134d7 | -3.54262 | -59.93084 | 2026-09-06 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4d5d2bd-4999-3d06-a2c0-e19ef71e884d | -5.83373 | -60.25163 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b908874b-2979-3e99-bc95-365d4d50efa3 | -3.83059 | -60.76885 | 2026-09-06 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0a24a14-7e94-3bd8-8b1c-4554a066eefa | -5.34413 | -56.02686 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a17ed30-052e-3ad1-87e8-5d62540a84ef | -6.00071 | -57.78214 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f302acf9-1af3-3878-a155-6fe7846340ed | -3.76666 | -61.75622 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12936d92-8639-35fe-9b14-dd0707fd880c | -5.36269 | -56.0348 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a67cfafe-874d-3157-a1f4-3bd744448aee | -3.7801 | -58.85368 | 2026-09-06 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d701c615-cea6-35a1-b9e8-6a9259ed6c26 | -6.835 | -59.434 | 2026-09-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e07ac61c-1819-32d4-8fb3-80c59754ca6f | -5.34744 | -56.03808 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c54dd8b-6e60-3cb5-97eb-fa075ea7d704 | -5.13985 | -60.36605 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a394628-9c2e-3d30-a3de-0d6d1ea18118 | -4.24494 | -62.23638 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3111bca5-6e68-3b55-971b-e842db28cfbc | -5.44303 | -60.11956 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e5f4f23-510c-3db0-8fcf-bbd8811f12b4 | -8.5028 | -54.65265 | 2026-09-06 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e021d1e-c2b1-3248-99d3-834878554294 | -8.50245 | -54.65094 | 2026-09-06 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30c6e2c1-e375-3420-bf3e-87d71389efd5 | -3.76778 | -61.77118 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe2917d9-557d-3535-88f7-6d288ee030f2 | -7.78974 | -70.04923 | 2026-09-06 05:42:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e17df438-77d6-33d0-a647-679a5bb628c0 | -5.6524 | -60.24147 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0008047e-9b62-3788-9e71-b1ba5b28ef72 | -5.13622 | -60.36546 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7f00c4f-88c5-3fd9-bdbd-c654fbfb3041 | -3.78789 | -58.85488 | 2026-09-06 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a57c963-4ee4-3e92-a322-78624f9122c0 | -6.63749 | -59.44143 | 2026-09-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e14f0e7-b7a3-3018-bdfd-58ef8ca0d368 | -5.84478 | -60.25333 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 928a9ac3-5f1c-331a-9426-97fa628205d3 | -6.951 | -59.73577 | 2026-09-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26e0f3fc-5644-32c2-85e1-531376b17dfd | -5.13238 | -56.27254 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 765475d8-e7d3-3c9c-b1dd-408b9ec4541e | -5.36752 | -56.03547 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7500276e-49ea-3cb6-a207-3ff1cfffb81c | -5.35863 | -56.02884 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b6b3a468-5830-37ac-97b5-99aa0832db49 | -6.87412 | -55.62015 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac8e932d-1752-332b-b40d-4dfbda4e9a74 | -6.87964 | -55.61779 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a202f29d-3162-3e50-afc2-4d25ac891c40 | -4.47183 | -55.09634 | 2026-09-06 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1dbed44-010a-3299-8a14-bd7c6c007dc1 | -6.09554 | -55.59702 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8171ed2e-0c71-3738-ad41-ba23759b4804 | -3.7706 | -61.77532 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef4e6782-10c7-3101-b64f-6e9ed2d4b324 | -5.25127 | -59.9815 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19abbdf6-73ed-3fdc-9c65-f43f649b8da5 | -3.84019 | -59.59737 | 2026-09-06 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6453b0d-17be-39f7-8572-984a55a7a31d | -3.7661 | -61.75983 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11ef16f9-00d7-3ba7-9857-c3b76f68cd19 | -7.79328 | -70.05387 | 2026-09-06 05:42:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d06d1c41-4efe-3ef8-9a4b-6cad7420f082 | -4.67285 | -55.63913 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c73a5aa-c7a1-36fe-8d48-cd0503ba9770 | -6.09134 | -55.59051 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31bf247b-073a-3262-9d18-01abf9107e1b | -6.8699 | -55.61347 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8a7555a-1489-344c-abe0-e378d7ebf53b | -4.47272 | -55.0904 | 2026-09-06 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07208371-3a74-3589-aae5-5733769bab57 | -6.95416 | -59.74113 | 2026-09-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf3bf676-cbb9-3efd-9427-ff19b832a5a0 | -4.92223 | -55.81137 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc3b4afb-af0a-390d-925c-16f4e1426899 | -5.57164 | -60.15953 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d09033a9-64fd-3ac8-95f2-05dcd5d5c90d | -5.36676 | -56.04075 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 63a9767d-a6e6-375f-b8f9-9f38a87b6efe | -7.55889 | -61.35601 | 2026-09-06 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcb56df4-ed71-35f7-b867-06291da61fc0 | -5.17294 | -56.06356 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b2f90a2-1fb6-3a0c-9fde-0471ae967bdb | -5.84847 | -60.25391 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6aeecffd-1d8f-3cfb-b7b4-e2944b85eef6 | -5.57385 | -60.1629 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 172a4797-10ff-38ee-9434-c17b02173523 | -5.59959 | -60.24234 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20452ece-c971-3d50-b12f-93fbc0dc31cf | -3.76553 | -61.76345 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32b6bb3f-46fe-3630-b031-17fcc98892e8 | -3.77793 | -61.77276 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17cbb9c5-548b-3631-8fdc-0856db309f03 | -5.36599 | -56.04602 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 595ce204-a931-3755-a8af-1c6988f3ed63 | -6.6414 | -59.44198 | 2026-09-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3f3c89a-4403-3d50-8088-11813af8fb49 | -5.83307 | -60.256 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab395f09-1088-351e-b92e-46cb544a5d0f | -5.14259 | -56.26891 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 38a2b3e1-feac-3bdd-b006-28441a8d7799 | -5.17371 | -56.05834 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ae51893-1ae0-3ddb-aff3-568fae62b8bf | -6.51659 | -58.29413 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 024bff1d-65b6-3d53-8259-c2c1d57a88fb | -7.1004 | -56.51991 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4919761-d205-3db8-b7c5-e0998f62cd57 | -5.36117 | -56.04535 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89e0db88-c88a-3baf-aae0-e01549c22acd | -6.9503 | -59.74059 | 2026-09-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba270ab1-8502-396e-a219-26f071980ae1 | -6.87629 | -55.60508 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da290f77-e09e-3999-9188-b2f0bff5bb8e | -5.25196 | -59.97707 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7e72dc8-ddec-38d2-a633-0c224a92709e | -3.76496 | -61.76705 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37380a26-e287-3d3e-bb9f-b886d0590902 | -6.87498 | -55.61415 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e9798bf-f4a3-30ea-8447-609a7a0c5df6 | -5.55547 | -60.23569 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f60c9e17-e251-3563-8c8a-cac1380b2afb | -4.47737 | -55.09398 | 2026-09-06 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 007afabc-3290-3990-bb27-ab8611bc1960 | -5.36016 | -56.01825 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fbb98959-c0ed-3e04-8a09-628493a58f4d | -5.29696 | -56.01779 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README32.md)
