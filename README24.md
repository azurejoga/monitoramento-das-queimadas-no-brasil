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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ed38695-82df-39ef-ba22-ffd215d7aeba | -7.34638 | -42.08034 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2403e8cd-27c6-38f3-a6cf-ccf61cc369fd | -6.09829 | -57.68114 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e68680ca-86a6-3228-8819-7df7d370b8a9 | -6.83863 | -43.52048 | 2026-09-27 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bef639f4-be06-3a9e-ac1b-e8f8d6d6a67a | -3.94985 | -56.09317 | 2026-09-27 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a10f1b35-2bc9-3702-9ee8-ab0b308739ad | -3.19208 | -51.03508 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 83c6d97f-dcba-31bc-9a22-3f1032a937e3 | -5.17924 | -46.11598 | 2026-09-27 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05033ba9-54af-3161-b486-7f7a11513cbb | -6.83914 | -43.57246 | 2026-09-27 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bef5b271-2422-3c55-b96b-b1f8b66df2c6 | -6.0499 | -53.60607 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c32238f7-be70-3c13-bed4-e5e8f1406f6c | -4.05146 | -45.33822 | 2026-09-27 04:51:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 0f1fb91c-d997-3bd9-8b05-f945b1984ce2 | -4.53922 | -54.98156 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f9a3be37-fc60-3a91-993e-5c71acc39cbf | -4.58624 | -54.92046 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ca5af80-7e46-3fed-8540-69ce9323b93b | -3.51422 | -50.31452 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e7f8e9b7-d59e-3f4a-b7bc-47c8a9624e86 | -3.57008 | -50.29607 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9fcf159-d53e-308b-abcd-de4ad6966d74 | -8.34597 | -44.16132 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7ef14f2-8ff3-31b5-bd17-5aeba8961d29 | -1.82003 | -55.33362 | 2026-09-27 04:51:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 242d65bb-d7b4-3272-a241-6e6b5bb8e8c7 | -8.63099 | -54.67204 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa402f82-c857-3e4c-bbf9-575aa2a287ab | -3.0703 | -58.41607 | 2026-09-27 04:51:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bc1aa31-913a-375c-b32f-90772c475007 | -4.45888 | -55.03352 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d703e81-58b6-3f14-9133-324b35adb1e0 | -3.01165 | -54.20681 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2f4f7d4-3023-3e15-8149-7973d5f92128 | -6.6824 | -51.59727 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4a0cba7-f8eb-352a-8f1a-9a6b89ca80fb | -6.06042 | -53.60416 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49f61fcb-a6e4-3fb1-992f-1126c2b413cf | -4.4441 | -55.03186 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aba5e5bf-ffda-37aa-8672-a36ac3e7a731 | -6.63356 | -59.93877 | 2026-09-27 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3220386-6cf2-3b59-b836-bde8ffce8c52 | -8.04015 | -54.89741 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3191aba3-b3bb-3fda-a1e6-4f45a8d0d595 | -5.86383 | -57.56025 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dadeff78-b5e0-3f7b-97af-f2de17dcbd28 | -3.19595 | -51.0321 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dee6f20-bfee-3a19-8bfa-045bd557d9b7 | -3.00761 | -54.21007 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e594d32e-9111-3535-a0f3-1c6eae6781f5 | -8.35121 | -44.15589 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6e27f7be-1f9f-3eed-9356-073c4c67c3ca | -8.34463 | -44.17118 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce94ca01-2d20-3eea-a7eb-9868bfdf4f88 | -3.43016 | -50.33525 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73cb6970-aa93-3401-b047-ac06831c765c | -7.68092 | -54.75375 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2dbdcbf-dc97-33d1-92f5-82470258a8e1 | -3.23172 | -54.32587 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78ec8e7b-ad8e-31c9-9f5d-8ab86f165e2b | -8.08938 | -54.7407 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9e5d3d6-561f-308b-bcd8-cc6cc2e7f16d | -9.10404 | -54.68917 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94153433-3bec-3606-ac27-f106b6bed9fe | -2.79773 | -57.69437 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0caa85b0-832c-323f-bb84-9ec564260dbd | -4.56329 | -54.89768 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 96799ac1-4b73-3983-b479-112d12603781 | -5.74237 | -45.06545 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 989559a0-3e86-353b-a108-aeaa303eda2b | -2.78806 | -57.70081 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 98d27b6f-2f3e-35d3-8506-a0ffb384bc6b | -6.0901 | -57.63065 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d96a9450-19d6-3fba-9957-64f85a555d67 | -6.87473 | -55.58196 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 170b3a56-5f1f-327e-bbdd-898c60e23dfa | -6.07264 | -57.81411 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09aec49c-a7e6-3059-814c-6cf4353d73c1 | -8.34733 | -44.15136 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1101a83b-57d5-3010-aadb-139d53979a85 | -3.4228 | -50.42749 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bceddea0-a8cf-3d1e-8d3a-16753ceb459c | -1.61931 | -55.10873 | 2026-09-27 04:51:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7beae135-cf2d-3807-9d50-d046a4b1a6cb | -3.41941 | -50.42695 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 792a93bd-4205-3576-bd34-c6a1308bcf1f | -3.42372 | -43.16539 | 2026-09-27 04:51:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3b63e80-725f-342b-9e7d-6b2c3dcbcf15 | -3.80324 | -51.01768 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40ba0aef-13ed-34d4-9f81-129831559575 | -5.88797 | -47.26402 | 2026-09-27 04:51:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8afdbac7-434e-3359-86be-9cdc7e09b36d | -3.00881 | -54.20252 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cfb3e6e-9759-3be2-9656-86446377e222 | -3.71629 | -54.65767 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01d8e203-6d7d-335d-80f7-dc663d356b5d | -6.07721 | -57.81839 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a532b087-70d9-3493-88e6-a095809db5b3 | -3.76639 | -51.80326 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e010acb1-454f-36d9-9171-ac4a888a4082 | -5.89039 | -46.58251 | 2026-09-27 04:51:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 418b371d-5d11-353a-93cd-4c6a1c72be23 | -4.35953 | -50.31556 | 2026-09-27 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adef80ef-83be-327f-b778-b27ed46d3739 | -2.90576 | -54.09867 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2b673fc-5e00-3c67-8be7-ecedef3a96ee | -2.5114 | -56.23345 | 2026-09-27 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 589bcc96-b0c6-34ce-bbfd-1c3cd0e0f2d4 | -8.35172 | -44.15877 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| f5b30215-664c-3d29-be0c-e165ade8a8e5 | -5.5712 | -47.41386 | 2026-09-27 04:51:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aaf4a028-84dd-3673-92ea-eaa93a06db63 | -6.22605 | -51.6907 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 459622f8-237b-3ac2-95c4-796e1367f76d | -3.41659 | -50.42277 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a278e145-f97b-379a-92ad-58be4bcef1de | -3.71342 | -54.65324 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53b5ba7d-98b0-3b1f-90a5-8b3a6dbea65d | -3.96579 | -48.11613 | 2026-09-27 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f22f633c-0415-344f-b4bc-8f1ebffaefa6 | -7.33322 | -42.08741 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6e0d88ee-effd-3cfb-9b12-da0f5b4e25a5 | -4.81473 | -45.92858 | 2026-09-27 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01388c0c-aa7d-383f-aa2a-9a0f4a807330 | -7.34313 | -42.08012 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1defb8a2-ad6f-33e2-bd47-bfe72bf81c80 | -7.69048 | -54.75902 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7688216-9a72-3a34-84d7-17209435392b | -8.35294 | -44.14249 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c291951-2507-3f36-ac79-cb66e16fb7b9 | -5.75964 | -45.28896 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9f3244ab-5f86-3cb2-b609-d763f968200a | -6.06515 | -57.80929 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4eef7416-c877-3636-ba9a-04a05a16e624 | -2.86724 | -54.11952 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a4c2fe3-a854-3647-b503-8e3c67b0c6eb | -7.12588 | -43.66572 | 2026-09-27 04:51:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48f96d0a-fad5-3aaf-ac16-2c042a3525c2 | -2.66018 | -56.54114 | 2026-09-27 04:51:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6126f3cb-e6c3-3f8b-878e-264e2e2a75e1 | -7.98041 | -44.81047 | 2026-09-27 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a43b9136-362d-37d4-81b1-e961960e1f58 | -4.4624 | -55.03406 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a65be12c-ce31-3bce-932b-9105db534395 | -3.86856 | -52.28405 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b4d9195-12f6-364c-82ef-b30c713a9961 | -5.60519 | -47.43721 | 2026-09-27 04:51:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c3f7eb9-212e-399f-8f26-904d1dbbc0a8 | -2.9284 | -56.57583 | 2026-09-27 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97d8a75b-6d6d-31ed-906c-3b0fb6c404cf | -3.06534 | -50.33614 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8baec4d-f8da-3381-9150-d7ba1304d863 | -4.26064 | -51.05135 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c29799df-aaba-3750-ba05-c87e29c5e2b7 | -8.3495 | -44.16919 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 304.2 |
| 27ffd917-eedc-3f29-afef-5522e742a7d1 | -2.91419 | -59.13962 | 2026-09-27 04:51:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6123d94c-968e-3316-afa2-64bb881d6418 | -3.42393 | -50.42021 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 077ef919-a890-3fc2-ba7c-9a17782fd1e8 | -6.87329 | -55.58662 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e1ea26d-c24d-3e59-be4f-4d96215bf8cf | -8.35338 | -44.1861 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2a387bbc-1a23-364d-a92f-9f1df9491e5f | -6.47201 | -53.51929 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e8c53b3-8aa5-39d8-bc7d-abe2c32d1699 | -2.99807 | -50.47068 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb81c4a7-5738-35d3-8c78-ead3c5a25249 | -2.8614 | -54.13398 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 622a7fed-f848-352f-8dc7-143af85c1fca | -4.13157 | -54.25256 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ae0485d-fa98-3692-97f7-7040566efab1 | -5.88173 | -51.93882 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d82c499d-ea86-323f-b297-332e6c7c7b84 | -9.08325 | -49.86901 | 2026-09-27 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ca710e6-bb12-3965-a621-7d05d46be381 | -3.03947 | -54.6949 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80ac04d6-7b4c-3ef2-bb26-f50bb265fd2f | -7.33979 | -42.08395 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1126e2fb-f320-3aca-8c35-4825600e210b | -6.09352 | -57.63476 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d965fcb-d369-3869-bc3a-659b310615d4 | -5.98672 | -51.87621 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea9f6e1d-6bbf-334d-8058-5dac9ce3d102 | -7.36244 | -42.11954 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 58a8445b-88be-30be-ad38-0771247ee82e | -3.51366 | -50.3182 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3b7174ec-a2c6-3c3c-9996-fa033ad7c16d | -2.25909 | -52.02412 | 2026-09-27 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72794265-9539-3012-87fd-b488f754a0c1 | -8.35081 | -44.16541 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 428.2 |
| b32f1c5b-7f59-3f75-9d36-796ea606e74a | -3.71752 | -54.64992 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0edb9cf-99da-3f89-95f4-2a02b85c0cab | -8.03396 | -54.89267 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README25.md)
