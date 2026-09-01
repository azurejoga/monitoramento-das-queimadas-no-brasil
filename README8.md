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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 691d48c3-90c1-3c54-aa3f-e2e79f0451e2 | -3.08386 | -59.13649 | 2026-09-01 00:26:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f9b4a8d0-967c-3bd8-a817-9a8a59b85cfb | -5.88746 | -52.16327 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| f389e256-ad09-3d9a-bc94-87347bf18f92 | -5.49041 | -57.13855 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7e6689dc-a726-3b49-adff-4d3570e5f631 | -7.30019 | -60.56344 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| b56c6c3b-52b1-3dc7-b639-a5d626904f4f | -7.00566 | -52.90173 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 80075c41-6740-3da8-83c5-7a6b4f0b700e | -7.27771 | -60.66518 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| e0da5058-a200-399f-80b0-87078f797441 | -8.58763 | -54.77386 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| b02aec93-b03b-3791-bbec-a95acce7e99d | -8.24278 | -54.94681 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7e984fd3-b73f-3d1a-ad39-1579226d1b06 | -7.29613 | -49.84334 | 2026-09-01 00:26:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fcd223a8-ef62-3050-8753-d861c43d70ed | -4.9562 | -55.85235 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9b4b1fd2-7de2-353f-9494-6c1298e17d39 | -7.40764 | -49.73402 | 2026-09-01 00:26:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 5394db60-d7e8-3542-8773-e625bd0edc41 | -3.62538 | -60.54845 | 2026-09-01 00:26:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2fd6144d-6128-38dc-ab7a-cff580356889 | -3.0871 | -59.14079 | 2026-09-01 00:26:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 42b8345b-2a64-35cf-a36a-263f2d7ea7f2 | -6.60089 | -58.5865 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 3ec1f182-4bab-3ef8-a82b-d0bc334b396b | -6.93524 | -55.64298 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dc5d1b9e-c4d3-3485-b716-b0ee7da9781d | -7.57364 | -60.46081 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 19466250-5030-3675-b4d2-0bdcd597b1af | -4.27473 | -56.13057 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8fc723e1-4564-38cc-a4e1-10eedcc9fba3 | -7.6372 | -55.30062 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c6b10f6a-bebb-3b2a-a889-e725aef921f3 | -5.25596 | -55.89015 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0ab7fbb1-c919-3a7f-b57c-670aa96ee44c | -7.85981 | -61.15434 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1065036d-ac50-39f0-9ac4-f250deb431cd | -6.95691 | -55.65206 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 167db2a4-2378-35f8-8d88-1c4a865b46bd | -5.24958 | -55.90891 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| b6c07c21-80a7-30df-b7a3-e1be1d4effa2 | -6.17992 | -57.74151 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| de23ea86-fadc-3a6d-b83d-55e8edab80ac | -2.66813 | -59.37522 | 2026-09-01 00:26:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5d4cf56a-79ac-3b6d-af3c-965360e748b5 | -5.48205 | -57.1455 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f22ea797-2b49-3ba7-9e9f-e484a8a8a1a1 | -8.61624 | -54.85097 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 428ee34c-626b-3f4f-95c3-1f4699685a0b | -6.73627 | -56.34099 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b722891a-73e2-39af-bb48-16cc8fe3ed6f | -5.88899 | -52.24638 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 81d6f14d-4a2d-3659-adac-57e4ca51937c | -4.36885 | -47.79789 | 2026-09-01 00:26:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 8ce877aa-7bf3-38ba-8069-f76a4dc7ef0e | -6.62837 | -53.18063 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a505ee91-b2e1-356a-b788-fd367bcacded | -6.79977 | -59.38998 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d70d6ed6-b90e-36af-a79d-a7cffbccb203 | -6.9557 | -55.64325 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 160.2 |
| dcb7281c-1045-38e8-974e-608368e6205a | -5.95945 | -57.68282 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 9f3a5543-3b28-3a70-9302-00613d08d946 | -6.61222 | -58.59639 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0555a4ca-6b16-3c58-9e62-84633bde092d | -6.81363 | -59.4473 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 898e39e7-f1bb-3437-b579-bdf6f9d170f5 | -6.60234 | -58.59775 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 95801225-385a-3787-bda3-c96f4eb28f5c | -7.87251 | -61.75864 | 2026-09-01 00:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4cc568f6-7c78-3e53-b003-00dab0dce1bf | -6.82315 | -58.87959 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 21975021-a444-30a9-830a-d0b73d8dc235 | -6.77338 | -59.43276 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6f276f14-40e1-3c20-bcda-b32cb76159c0 | -9.47017 | -57.01651 | 2026-09-01 00:26:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| e0658384-9545-36d2-adb8-c9e2a1dcc7de | -6.78923 | -55.64297 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| edb1ad7c-aa73-37cf-92e4-30f108fe06b3 | -7.2874 | -49.83474 | 2026-09-01 00:26:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 48fc7d82-1474-307b-84e3-66978e6d9d73 | -6.92403 | -55.6266 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| a8f68b65-3762-3be0-81a7-5915ace8a694 | -6.78526 | -55.67941 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 84926c8a-37ec-3e28-a677-228f690d77c0 | -8.61747 | -54.85982 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 27fa4c12-8ce2-3585-88ce-a83063264b2b | -6.88933 | -59.4053 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 763ff902-2eb2-3a22-b7dd-4173151318a7 | -4.97377 | -55.84989 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 83454dd0-09d6-32f2-a02a-79d8f01d24c1 | -7.35878 | -60.58233 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 05b5e241-582d-32c4-a110-f10e739f4952 | -7.28677 | -52.3548 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ba2d2906-c017-3452-95a5-a65494f2edeb | -6.24161 | -55.48788 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 548de243-42b3-3a98-8a54-4a33e9c0d187 | -5.88167 | -52.06038 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5f74e254-17f4-3883-a6fb-111ec2252f91 | -6.97841 | -59.59394 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 94c3a2d7-d8ac-3935-96ba-e8882d151d7e | -7.53869 | -61.38288 | 2026-09-01 00:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 78f45c41-b208-3376-b0b4-2d5652dfbe58 | -6.25192 | -55.43269 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 79b849bb-af06-321a-bfa4-8013e4b231e0 | -7.41956 | -49.73225 | 2026-09-01 00:26:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6d1fea4e-1cc3-3019-ac2e-1900c15dc396 | -6.93645 | -55.65179 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b6d3c74c-48ae-3341-86d4-3483eaccfddf | -7.41324 | -55.16185 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 89d7b112-c0e9-3d5b-8e3d-dd6dce715484 | -6.13066 | -57.84613 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 54f441d9-294c-3b96-9a6c-d121305089e1 | -6.81364 | -59.57395 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 2df69292-9543-3f97-847e-75abae5ca6f0 | -7.86294 | -61.1483 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ca1fd5df-a70e-30ee-9b6c-6b555ab05c9f | -7.00712 | -52.91209 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3b90b278-ed83-36a8-a416-4c7846203b46 | -6.86094 | -59.48075 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 68025cd2-7c5f-3d35-ad02-11e7a02c8380 | -7.3355 | -60.58544 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 21b8e0e5-fecc-3102-8314-854269f81783 | -6.51019 | -55.23413 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c159c287-f1f8-3f55-8c6a-90ec6817e5fb | -4.22537 | -59.86529 | 2026-09-01 00:26:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3bf6085b-688c-3d7c-a592-c08321fb3e72 | -7.5838 | -61.33914 | 2026-09-01 00:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 40c32a71-3d34-3b4d-a3c8-441e53064d78 | -6.60185 | -58.60347 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| e029b122-327b-3f30-8459-733b4a8ca0cb | -8.59028 | -54.72829 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 24d4be8a-fac4-3e62-8e34-0a3f85845170 | -8.62181 | -54.69665 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 929ce7c0-dc56-3d2d-a456-31af6ec507b8 | -6.25313 | -55.44147 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 57941aae-92db-3c7c-88ea-e9832dc0028a | -6.70093 | -55.41025 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1601.0 |
| 49bbd9b5-76ef-370c-a778-bdd46326e057 | -6.60033 | -58.59222 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e3b82a88-8cda-3f4c-9dbe-aaaef27cd3c7 | -6.35804 | -55.85953 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bb4c723-6e61-3e2b-be59-af811c38a750 | -7.18822 | -60.68225 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 6c4ac013-e7cf-391a-9f42-21c1c29f8093 | -6.90501 | -59.48817 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d74d2618-28ac-37a9-889c-3da6bae9448b | -6.82169 | -58.87412 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 93fc2b89-10e5-331f-bcb0-b7a07e8cdbab | -5.87239 | -57.79139 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b84339c5-30d6-3d79-9056-1b8a928b7969 | -6.69336 | -55.42028 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 79f50d5c-0bd5-3681-a91a-c3f0222f3993 | -6.80149 | -59.40278 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6680dfd8-900d-3b55-b38f-6742ef40ad0f | -6.74601 | -55.67289 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 384ac730-50bb-38be-b437-36b69c2dd134 | -4.96619 | -55.85988 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ace0454d-c70d-326f-a0c8-00acd5cbec99 | -6.17858 | -57.73159 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8fe293d8-bfb5-31f4-8e65-ee3391674b3a | -6.79656 | -59.3972 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| ca99371b-c663-3267-bae7-cc22e8128a13 | -7.05223 | -52.717 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| c270edf3-1cf4-3eb4-a725-efdb1e441372 | -7.2898 | -49.85084 | 2026-09-01 00:26:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8d00e8d4-8461-36d4-bd61-2234c86cc5c0 | -4.97256 | -55.84113 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 57abe60b-4ef0-3f1c-b405-9cc9b53042e8 | -6.94571 | -55.63568 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| bf833767-1f6b-338f-8de9-5d455e38a088 | -8.50302 | -55.30284 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e4afec94-51d9-38db-a689-29c9a6a74a24 | -6.9545 | -55.63444 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 3fd8599a-4231-3ae6-838d-d7e0c4ddcdcc | -7.01768 | -59.64344 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bdfec428-b09f-32b1-85a9-4148c662a79e | -4.36471 | -47.77063 | 2026-09-01 00:26:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 70f56696-8862-3059-ad6f-6b9c442d343f | -10.06207 | -59.39649 | 2026-09-01 00:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 16fd2e1a-6103-3dcf-9d4d-7ff79c3f2ba6 | -7.29064 | -60.58095 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| b2d265e3-6cdc-388a-9144-b807ff1363ea | -9.4715 | -57.02658 | 2026-09-01 00:26:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 39fa1660-aba1-3c10-b37f-e37410269339 | -6.80299 | -59.57536 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2e698718-17c6-387b-bfbe-79f9e6809182 | -5.85147 | -57.56369 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 966ee1fb-71ae-3672-a94a-41871378c08b | -7.41024 | -49.75098 | 2026-09-01 00:26:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 06af1cbd-c25d-3325-ac15-644855346223 | -6.12533 | -57.68817 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ad78bc5f-6beb-387d-a13b-7df681c4f4a3 | -7.3102 | -60.57215 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| a80a8327-77a5-3545-9399-46c6747477dc | -8.7973 | -62.49066 | 2026-09-01 00:26:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 23.3 |


[Clique aqui para ver as próximas entradas](README9.md)
