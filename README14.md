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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd6a4aae-9f90-34e0-8a07-cdfa4844db8e | -8.1424 | -61.209 | 2025-08-29 01:21:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35f3731c-98b0-3723-abb9-06b01e6c6971 | -8.1905 | -61.369801 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 676d823f-da51-3513-a949-1fd49a8adbbc | -9.179 | -65.781799 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a673495c-1733-3a0f-bec5-9482f99db19b | -14.2612 | -58.4884 | 2025-08-29 01:21:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9dfed98f-b351-382f-8e10-8f8fd002dd00 | -10.8548 | -60.8111 | 2025-08-29 01:21:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5683dada-b148-391a-af66-9fa0b5ce4e14 | -9.2295 | -60.877499 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d059a93-b8c3-3e3e-8967-1f2599a43bb7 | -9.8117 | -61.201302 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27b94c1e-d29c-396b-8320-d0d8b1d31e3b | -9.1919 | -65.793404 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a96d80e8-aa76-3d6b-a5cc-e316015bf8b2 | -28.735701 | -55.648701 | 2025-08-29 01:21:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 9598b5aa-bc7e-3c68-a4ea-beff2629af00 | -8.96 | -65.954399 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f41129d-5c68-327d-a340-3b6584c9ec92 | -9.1413 | -65.797501 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 265fc13f-1d89-322d-a9bb-970c6a1c3875 | -9.1414 | -65.289597 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4816e08-d62e-3e85-9ac5-4c12de4b219f | -9.1429 | -65.804398 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9f49ae3-f9c3-3491-8ac7-3fd09dea1ef7 | -10.3613 | -57.800201 | 2025-08-29 01:21:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db59c913-d3d5-3f81-b54b-e7736fe43ef7 | -9.4654 | -60.567101 | 2025-08-29 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 066c59e8-dd01-3676-ac88-ac0cfda68fb1 | -9.1512 | -65.795303 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd030dd3-f2a6-32ba-88b6-86a6b45ad0a8 | -9.1383 | -65.783699 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b05cb4c-a949-3249-9779-ccb26bdbc5ec | -9.1269 | -65.7789 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af1e6368-ed28-3cca-b383-3dc3addeb325 | -9.5583 | -65.682404 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 81684564-06ed-384a-b6c2-a6bf8aa0d3d3 | -9.1321 | -65.755997 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebf828b5-3e5c-3d93-a009-392d2ffd9cbf | -10.3687 | -57.829899 | 2025-08-29 01:21:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e75da5d-a165-3ecf-9674-54d748653b65 | -9.1806 | -65.788696 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7a9410cb-25ac-39cf-a8a6-94206db21f3b | -9.1336 | -65.762901 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a51378e8-cd3b-325f-b4d1-7b18a940537e | -10.4369 | -64.360298 | 2025-08-29 01:21:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e4d6ac66-2814-3b6f-9386-2e150b33f0e5 | -11.3835 | -63.260601 | 2025-08-29 01:21:00 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d5ab91e-1097-340b-84b8-a5162ec98139 | -12.447 | -63.905201 | 2025-08-29 01:21:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b41fa2f0-e65c-3494-8361-608a1cccf916 | -8.9585 | -65.947502 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d245e4f0-e05c-3869-a588-d5d0dd8932ec | -10.9421 | -63.631302 | 2025-08-29 01:21:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d8ec438e-5df1-3840-b01a-cd08ca97c5ed | -10.8743 | -60.8064 | 2025-08-29 01:21:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed881f4-db2f-316f-8c56-97f751046031 | -9.463 | -60.5569 | 2025-08-29 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d0b9a8e-0328-3f84-8d53-46497e1cd670 | -9.7804 | -64.236603 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b278da5-6a60-3280-9adb-c2ec63f8fbc8 | -9.4557 | -60.5695 | 2025-08-29 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4c2de1a-616e-3a42-8ace-4c775d5f7027 | -8.1131 | -61.216 | 2025-08-29 01:21:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af595262-7045-350c-9302-7d65c0942c8d | -9.1177 | -65.737396 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d23a264-eb74-38fe-bf7d-2bec791f1ad7 | -9.1934 | -65.8004 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3b1dc19-e743-370d-bf88-7a98f7f04cfc | -8.9668 | -65.938301 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4f5414c-85c4-3c83-9601-6298cc9549f3 | -14.3287 | -53.327999 | 2025-08-29 01:21:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 720569d8-1a56-35f8-b637-b5f7dde271fc | -9.1666 | -59.535099 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cebdfb5d-e00a-3701-8749-c51bf2e723cb | -10.4596 | -57.946999 | 2025-08-29 01:21:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85438251-856a-3b37-92a1-219764a42678 | -9.1125 | -65.760399 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc32512-27ca-3701-9be6-6cb1d7cc868f | -9.1187 | -65.788002 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b300d17-3825-37e1-893e-333112609b8a | -9.795 | -64.255501 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1495b5fa-5bee-3db3-8d97-5ad5be511de9 | -8.2917 | -61.405602 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0751da4-2b80-38bb-9cb6-4ce554424df8 | -10.3747 | -57.812599 | 2025-08-29 01:21:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb871de-976b-3e58-abb7-9ad7c2c85873 | -8.1883 | -61.360298 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a39e5800-8854-36d5-9465-f781d07fe840 | -9.1162 | -65.730499 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c623c233-d497-3142-9868-01de396be3f5 | -8.1829 | -61.3815 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a2188a6-7e96-358b-9cde-77bf4f79f7f8 | -13.0332 | -56.928799 | 2025-08-29 01:21:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed916f2e-736e-3d4c-8989-816ca2201086 | -9.1398 | -65.790604 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8d82e0e-0097-371e-af5b-238f7f5d9f8d | -9.7918 | -64.241402 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bc08c1e7-b83d-3b56-bdc1-83943efd39bb | -12.4404 | -63.9216 | 2025-08-29 01:21:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1d3d2a74-aeb0-3126-ae50-7794227eebb9 | -12.4502 | -63.9193 | 2025-08-29 01:21:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c89771c3-0482-336c-bf21-bd5127b06576 | -9.4532 | -60.559299 | 2025-08-29 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30a5a7f3-90c9-33c4-833d-4a107720c397 | -9.114 | -65.767303 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36d95398-812b-3a81-83aa-984bf7545b13 | -9.1677 | -65.7771 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3f3ae43-c271-35f4-b1d6-76901cab2142 | -9.1655 | -59.573101 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7eff86db-a603-39e7-9df9-280f37e0e637 | -9.1254 | -65.772003 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d4b3175-9cca-3cf2-9dfe-9ff80ba25173 | -8.9616 | -65.961304 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e0e28cf-cc5f-3723-88ab-e1a7670388b3 | -9.1752 | -59.570702 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb0550f2-2a1b-38ec-9595-32851739fd3e | -12.4388 | -63.914501 | 2025-08-29 01:21:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| af2cb849-0d93-3908-aa16-dd674e23047c | -7.0833 | -63.1712 | 2025-08-29 01:21:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dee1cbc7-5410-3fd2-829c-26726e26ea61 | -9.1202 | -65.794998 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2f54ee6-8143-3b34-b255-80961c09a566 | -8.3038 | -61.4128 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 805b0462-9b7e-372e-993c-88b1f4a92ec6 | -8.1927 | -61.3792 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c622f98f-9091-3366-bd7a-c1cf3c59b4a5 | -12.4486 | -63.9123 | 2025-08-29 01:21:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 909115e4-b0af-3f12-a86a-709dc1b04d8e | -9.4605 | -60.5467 | 2025-08-29 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8680dcd-4fc6-39a1-9722-61cb01ea4300 | -8.9714 | -65.959099 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c939cde1-6380-37a0-8833-ff13b9fd26dc | -14.2641 | -58.500099 | 2025-08-29 01:21:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9fb043f1-0c4b-3469-8d08-0f70eda29617 | -10.3006 | -64.487099 | 2025-08-29 01:21:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e1406c3c-424f-3b08-a23c-c59e2b9fef7b | -8.9683 | -65.945297 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 039526a1-74f5-3b70-ae35-3a69d020be8d | -7.6081 | -63.346199 | 2025-08-29 01:21:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f3ab855-3bc9-3034-a32b-55f4e31a28e3 | -13.0196 | -56.916 | 2025-08-29 01:21:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48276c79-6744-38f9-b616-d4131f2adcc0 | -8.5872 | -63.930302 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0193ef52-eaf0-3da3-b1e1-ad6b740d0939 | -8.3474 | -62.9291 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c385180-e777-317b-9bbe-83b7d57c973b | -12.4356 | -63.900398 | 2025-08-29 01:21:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6b676ae1-e81b-330e-935e-9c7fe81a9f38 | -8.3572 | -62.9268 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a143c0c0-53f0-33f0-b73c-7459cb1c55d6 | -8.1326 | -61.2113 | 2025-08-29 01:21:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c6771bb-cb5e-308d-b954-9cc8f10c8f8d | -14.2515 | -58.490898 | 2025-08-29 01:21:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5535a5f-fc46-300d-94c3-3c2c989d84d6 | -9.1661 | -65.770103 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b7a0fdf0-65ae-3ef9-be50-f1e31d3058a5 | -8.8674 | -68.492798 | 2025-08-29 01:21:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02a4f4cc-828f-3952-9c5b-a7cef67f31ff | -9.782 | -64.243599 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6cdb5efb-b611-381c-8473-927190e710b7 | -8.704 | -62.464401 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 40870d38-ea0b-340b-89b2-ac7a37ca3a7e | -8.5434 | -70.722099 | 2025-08-29 01:21:00 | METOP-B | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 77ba3714-a54e-3f89-86c8-cbc95e6232f2 | -13.0156 | -56.900501 | 2025-08-29 01:21:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6588ca3-ba60-3cca-bc0f-5ef0742c2faf | -10.456 | -57.932499 | 2025-08-29 01:21:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98d769cd-3202-39d2-843b-3e5d03c510eb | -9.1904 | -65.786499 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c4991fc-f6bf-38e0-98c7-b32ead3d8390 | -9.662 | -64.9468 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f6bdd521-c009-3bfe-95a4-768b01dd7ec4 | -9.424 | -60.566299 | 2025-08-29 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9adbcfa4-e190-3f8b-a8fe-031ec2980b25 | -8.2895 | -61.396198 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b467a562-76ba-3031-9d20-ad3b41e6664d | -9.13 | -65.792801 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2247a35-5a2f-3f6a-a154-4a178f9db62d | -13.0293 | -56.913399 | 2025-08-29 01:21:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f928fea-4911-3053-a215-63afbd351112 | -10.299 | -64.480103 | 2025-08-29 01:21:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bbb11dc7-031a-30b6-b839-01c53174bad5 | -9.1579 | -65.779297 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9285076-524d-3a5f-a3a6-535bea2a56f0 | -9.2175 | -60.869999 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2add396e-8c32-3bd9-b177-15bc472f459e | -9.0238 | -65.685898 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8fd2dda-8b2c-326a-98f2-e2c04866439d | -8.2819 | -61.407902 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c2a29e6-f03c-3c1e-b308-8437f23dd180 | -9.7737 | -64.252899 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 786b1f7a-9b71-33cb-b158-fa82e6aa165f | -10.4694 | -57.9445 | 2025-08-29 01:21:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5cf8dbb7-6914-3622-b5d6-303b297d91a9 | -8.2993 | -61.393902 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9c8eec8-8441-3a18-ad30-2e3f181774be | -9.1238 | -65.765099 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
