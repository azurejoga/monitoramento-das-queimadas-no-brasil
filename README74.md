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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fbe257c-d357-37b6-bd27-5ffee54e743f | -8.72245 | -69.63855 | 2026-08-30 06:14:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6908f4cd-44a7-3465-8ca5-f45c8ed050a6 | -8.95364 | -62.38062 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d43534ea-fd81-3a4e-93bc-181f459fafbf | -7.4614 | -70.1326 | 2026-08-30 06:14:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 594ab2c9-14b6-3bdb-940b-e476eb8a5582 | -8.54578 | -71.43617 | 2026-08-30 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dc7b6c5-feaa-362a-9b9d-9f93c82a36c5 | -8.72667 | -70.78122 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de8aacfd-1fd6-3641-8789-eda82632284a | -9.04843 | -65.41012 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a341d048-72f3-3c22-a0e3-cb72d5d01942 | -9.84939 | -60.27245 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5864bf38-99cd-3e2b-be2b-7e146dc99d61 | -8.25293 | -62.76181 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f505f4d8-d0a8-3836-b1eb-ab9753ec0710 | -9.01679 | -65.40083 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd0b989b-7bb3-345d-b1b4-3b0031d681b6 | -7.30158 | -60.60225 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cee2961-6283-38f0-85f0-8e3194a3f235 | -10.48166 | -59.6044 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b61a51f-8b38-3b78-b2a3-0def6251af0d | -8.79632 | -68.74413 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ca86a46-5d24-38a8-a4d0-96299aeb9dfb | -8.2104 | -70.15625 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 308ad567-629d-33d5-abca-a88d511e7f81 | -9.23335 | -65.88426 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 062c1c70-06c0-3567-855b-1d4f7db893d8 | -8.24746 | -62.7611 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9df560a-e067-3cd1-9b5b-3aa653e36038 | -10.5709 | -59.61472 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 659b3e93-bfc9-320b-ae02-97489228da3b | -7.23731 | -60.62106 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 77528754-a403-3712-afaa-c5d995f5956c | -7.69653 | -61.15312 | 2026-08-30 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 393910cf-305e-36ee-9335-0e74070a5f10 | -8.63277 | -66.54369 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fccf7e8-f8ee-3699-9b79-6e67457a91c6 | -9.0491 | -65.40532 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46e23a36-9a35-3cd2-840a-4daef4ed5dbd | -8.9588 | -62.4078 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f70cffec-be98-39cc-b391-fa76ef802146 | -8.60314 | -70.21812 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9aaacd97-bb6c-3ba9-abda-83efc80930c2 | -7.31336 | -60.60869 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a1c31fb-df8e-387f-b5b8-defcda40a3aa | -9.01217 | -65.4002 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 232c4b65-91ec-35ac-9ed6-6d6a3f3e1491 | -8.94231 | -62.37909 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2097716-0db2-314c-ac82-a6ca6c75ddfa | -8.66819 | -66.50813 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7c5c1c8-8a3c-39a1-8e19-8c9311c9b757 | -9.01745 | -65.39603 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48eebb91-3413-3343-9c83-8bdc3d4884b9 | -8.25423 | -62.75815 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19833b5f-4285-35a4-ab01-734f00db8b89 | -9.88723 | -60.28911 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2521be5b-a164-34a2-8077-66b085eb477e | -9.84319 | -60.27626 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 362f5768-ccfb-37ef-b54e-b0b68a4f0ba7 | -9.88858 | -64.98722 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73e14d1e-59b8-30e9-bf12-b638f26cf3d7 | -8.93028 | -67.36957 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50cd97a3-11f3-305b-8147-39625a483073 | -7.55566 | -61.32054 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| da6ad068-204a-3608-863a-345a08489e24 | -8.96038 | -62.39618 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b3085ac-5963-3a1a-ae79-944841b0f194 | -9.89445 | -60.28438 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b518cb60-4b7f-3414-8ea3-d013dbc7eea5 | -8.95473 | -62.3954 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab5e3e07-e752-3a40-9ebe-04a69dc97370 | -9.88929 | -60.27215 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 98681475-5715-333b-bb37-62ad990e28f7 | -8.92227 | -66.99255 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4cd4e41-40cc-3db4-8910-1cbf637df814 | -8.63333 | -66.53971 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5694581b-8348-3289-b9e9-1b72665d0734 | -9.06896 | -60.49186 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a629351-c1c1-34e6-b823-f5029087c524 | -9.71009 | -60.74713 | 2026-08-30 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54f61bb4-8674-3235-a88a-fec715468195 | -9.09453 | -65.48145 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dcc899b2-595d-3621-ae27-8add88245bf3 | -11.7831 | -51.0365 | 2026-08-30 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| dda59b50-6c91-399d-8ff3-861f2e3e97d9 | -11.8021 | -51.0343 | 2026-08-30 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 177.8 |
| d21db7f4-e01f-3be9-9a99-1645735a2c86 | -4.9604 | -55.8424 | 2026-08-30 06:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 5e7a5670-ac3a-3781-8297-cb0ef6ec3694 | -9.8927 | -60.2752 | 2026-08-30 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7a2e6970-c41e-36d5-9499-45f9d59f3b55 | -4.9604 | -55.8424 | 2026-08-30 06:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 8bd5dc58-9362-3c28-8e17-80897e20f3f3 | -11.8021 | -51.0343 | 2026-08-30 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4cde5b79-7392-361c-b3db-a88088f5a5ea | -9.8927 | -60.2752 | 2026-08-30 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a21f3c46-5ef6-3363-bdb3-74932ba7323b | -9.8927 | -60.2752 | 2026-08-30 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| af22732d-e15d-3950-88b1-14d9c092a53f | -4.9604 | -55.8424 | 2026-08-30 06:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| e869f47b-42a7-3006-9170-5c5e9a313671 | -9.8927 | -60.2752 | 2026-08-30 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 50f1ff9a-c209-3316-b543-d81816c2abf3 | -14.4197 | -52.5413 | 2026-08-30 06:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| c0c73489-55f6-3b14-a1e0-0c93dbd10ee2 | -4.9604 | -55.8424 | 2026-08-30 06:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f82cc22d-e622-3b51-a624-d9ab83d1fe21 | -9.8927 | -60.2752 | 2026-08-30 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 5d600657-b085-3d16-89d0-b46c0f89e47c | -4.9604 | -55.8424 | 2026-08-30 07:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 72b2aee7-04b5-37dc-ac0f-a3adf837766d | -4.9604 | -55.8424 | 2026-08-30 07:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 33b28c50-cf0f-3ef7-8fd4-3d027239d64d | -9.8927 | -60.2752 | 2026-08-30 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 27936687-de03-34ff-96fd-e885aabc0503 | -4.9604 | -55.8424 | 2026-08-30 07:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| d2855fc9-7490-3c9c-9577-9d9b354e36e8 | -9.8927 | -60.2752 | 2026-08-30 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 79064a70-7093-325a-9fb8-0398f85577cb | -14.4387 | -52.56 | 2026-08-30 07:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 663a8925-68fc-3db7-85e1-795d2c9bb103 | -9.8927 | -60.2752 | 2026-08-30 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 51dc1537-64e7-329f-9527-cce457a56399 | -4.9604 | -55.8424 | 2026-08-30 07:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 80da701a-c400-3286-b9c1-3709e74aa06c | -4.9604 | -55.8424 | 2026-08-30 07:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 4ad9cd90-5971-352b-a794-a3097c938cc4 | -7.5137 | -55.3051 | 2026-08-30 07:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| fe69aeb3-5a6b-39dd-b982-33b2ac39b182 | -7.5136 | -55.3251 | 2026-08-30 07:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a2b7af26-ee98-3b96-a65a-8db28d873455 | -7.5321 | -55.3241 | 2026-08-30 07:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 8a4b9c3a-b0d1-3b5f-aabb-e19d03683743 | -14.4197 | -52.5413 | 2026-08-30 07:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 01b72fad-09a6-372d-a0bc-5c937bc8b06b | -9.8927 | -60.2752 | 2026-08-30 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| e8ab3fc5-92bd-3100-8f3d-6a5245fc96b8 | -4.95269 | -55.84247 | 2026-08-30 07:48:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| dd315d50-69b9-338f-bd6a-270c857b953f | -3.62303 | -60.54309 | 2026-08-30 07:48:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4e1e7f27-b6d8-3a4d-b2dc-25d2b67b5858 | -3.63111 | -60.55532 | 2026-08-30 07:48:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 6934f040-384a-3dee-b05c-73fd5ba8f542 | -3.62141 | -60.55392 | 2026-08-30 07:48:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 05501bd9-866c-3af5-9dc2-0a0323b732d2 | -4.95806 | -55.82376 | 2026-08-30 07:48:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 1ff864f8-2ee9-3b96-8f6f-75ced2c0dc5c | -4.15512 | -60.68992 | 2026-08-30 07:48:00 | AQUA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6e66248e-01b6-37de-8928-6fa2300fb1f7 | 0.14328 | -60.39749 | 2026-08-30 07:48:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5a83bc4d-3463-383a-9683-983d952dc114 | -4.95456 | -55.84983 | 2026-08-30 07:48:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 74b89071-571e-309f-a157-dfe244ce4f16 | -14.4197 | -52.5413 | 2026-08-30 07:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 750c4e2c-cdf7-3de4-ba0e-202fa97640c7 | -7.5136 | -55.3251 | 2026-08-30 07:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 1f5ab2e2-de7f-3f77-adaf-6dd2121d6cf0 | -9.8927 | -60.2752 | 2026-08-30 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b203b04a-0322-356b-a90e-60f60079f565 | -11.8211 | -51.0322 | 2026-08-30 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f716dc38-15df-3285-b97a-15db0d6733d8 | -4.9604 | -55.8424 | 2026-08-30 07:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| bbfb0ae0-cbf5-3db8-af0b-008cdee0898a | -7.5321 | -55.3241 | 2026-08-30 07:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| b71a3c10-dd1a-384b-99a0-55ca9ca864da | -7.23115 | -60.62192 | 2026-08-30 07:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1d5df1d1-ab85-3b57-bfd1-ce79bff85505 | -6.85899 | -59.4674 | 2026-08-30 07:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 4ba223ea-c8eb-3c33-8d33-758fefd4bfa1 | -7.51968 | -55.30082 | 2026-08-30 07:50:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| f19253ce-a979-3da7-8dfc-c68c42e56f53 | -5.48749 | -57.1451 | 2026-08-30 07:50:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| a1175394-9d43-35ce-8d9d-cd1aa145c711 | -7.24027 | -60.61759 | 2026-08-30 07:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 66813646-0bb1-320e-9619-0c11ca00b622 | -7.56092 | -61.31099 | 2026-08-30 07:50:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 6dc6b494-ff51-3fe4-8c1f-c8373366517a | -7.52427 | -55.29633 | 2026-08-30 07:50:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a41be388-8f85-396d-a573-9280861762b5 | -7.23858 | -60.62966 | 2026-08-30 07:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| b4673db4-87b5-3343-a88d-ce63b382b22f | -5.88491 | -57.75681 | 2026-08-30 07:50:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| bf7b1223-d3b5-3f7b-9cd3-947d3b87a167 | -5.88224 | -57.77545 | 2026-08-30 07:50:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 4e83f571-5b65-3438-a855-1323815b3f50 | -5.49044 | -57.12417 | 2026-08-30 07:50:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 83887b94-211f-3f9d-ab1c-cda1cdcc4b36 | -5.87223 | -57.77892 | 2026-08-30 07:50:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| cd4469ab-e06e-333e-9384-5245528fa825 | -7.51999 | -55.32782 | 2026-08-30 07:50:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 07eb3faf-4c06-3833-bf70-5be2aa6ac2cc | -7.40021 | -60.58405 | 2026-08-30 07:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d86de4bd-847f-3d58-b579-5cd3fca4089b | -7.55932 | -61.32204 | 2026-08-30 07:50:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| bfbb7f87-e88d-3eea-a240-7ae9f5e010d5 | -5.4744 | -57.14342 | 2026-08-30 07:50:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8171607d-d928-394e-832f-52784a093c3e | -7.55116 | -61.30961 | 2026-08-30 07:50:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |


[Clique aqui para ver as próximas entradas](README75.md)
