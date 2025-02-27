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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b78dfa5c-fcd4-3d54-8934-dbe23c557f4e | 1.31536 | -60.06481 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5021e351-2716-3224-9d98-01f37785cd3a | 1.31251 | -60.06907 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d97c749f-f253-3c2a-baa8-a78418fcb919 | 2.91485 | -60.43226 | 2025-02-27 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c41f783-e909-3cc9-9966-bc6be32aeb50 | 1.68188 | -60.36901 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20143b2a-d667-3803-8b7b-84424fd7f8cd | 1.33146 | -60.714 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5879fb14-025c-39ea-9561-dec34db2338b | 2.67387 | -61.4111 | 2025-02-27 05:33:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e01dde5-e335-3480-adb3-ab9a8c4b65ea | 1.28385 | -60.10328 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b15cd97d-e003-3418-acd7-8fd0f346dc35 | 2.91205 | -60.43633 | 2025-02-27 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eab5eaa6-744d-3608-be61-82a68f4e18bb | 2.67332 | -61.40764 | 2025-02-27 05:33:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| be130e73-f3d4-3dca-8f01-4fda4740c07e | 3.36518 | -60.60452 | 2025-02-27 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 040103c0-ccb8-3a7d-84f5-28b2cab91568 | 2.91149 | -60.43278 | 2025-02-27 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e3e90ad4-c8a5-3a8c-89e3-ae3da4d5d018 | 2.1152 | -61.81964 | 2025-02-27 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 617c4408-2178-35d4-8b06-42b0386527c3 | 2.4494 | -61.31868 | 2025-02-27 05:33:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43815e27-4eb1-3826-8469-867b197daeaa | -12.32248 | -64.06873 | 2025-02-27 05:37:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69885147-1678-3f74-b362-fdaa1fbb58b8 | 2.11582 | -61.82359 | 2025-02-27 05:57:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e76015cf-f4f5-3aaa-8982-5c5a36d1e08b | 2.11512 | -61.81924 | 2025-02-27 05:57:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64cf43d6-ecfd-3e1f-aaca-09ef4bb7fb07 | 3.38721 | -61.21309 | 2025-02-27 05:57:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0dea80c-e97e-37ab-a1a3-e12c5dea442a | 1.71401 | -60.72284 | 2025-02-27 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0a54fff-a609-3aaf-b908-d74ec5d958c1 | 1.71484 | -60.72798 | 2025-02-27 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eac912a3-2917-3549-ba51-b9af1c318105 | 3.38272 | -61.21381 | 2025-02-27 05:57:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8928d532-32ae-358b-95cd-637464ac45f1 | 2.44889 | -61.31839 | 2025-02-27 05:57:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf64d3f1-452c-35f9-a1ae-c0c5619db956 | 2.11072 | -61.81989 | 2025-02-27 05:57:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a99bf4e-5b11-3791-a613-b19c125db472 | 2.11003 | -61.8156 | 2025-02-27 05:57:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34e84318-076e-3d45-a462-0bed8cfdcab9 | 2.90917 | -60.43415 | 2025-02-27 05:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2868943e-5377-3244-8986-a132d45f6d76 | 2.91004 | -60.4393 | 2025-02-27 05:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8a205e84-9e5c-394e-9f6c-f6da6e61141b | 2.04385 | -60.57809 | 2025-02-27 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ab06f00-ca57-3d8c-80b4-3da38b6de553 | 2.10631 | -61.82053 | 2025-02-27 05:57:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76ec5f97-39d8-3a84-a671-4344cc87fdcf | 2.91395 | -60.43338 | 2025-02-27 05:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 72913263-ec88-31c2-89c3-61a360768a2e | 1.29425 | -60.43583 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a62aa7d1-cc9b-3f8b-ab99-13143fc874fd | 1.28935 | -60.43661 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72c38797-5d13-37b3-a3c1-fbcf242a423e | 1.31613 | -60.06853 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5461b877-0802-3582-860c-4efa129fb830 | 1.31189 | -60.07037 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b541f3c5-7612-33b4-a93b-c970008dd610 | 1.28133 | -60.1048 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d312aea7-8f4a-3280-b2cb-c4f03ee484ad | 1.29025 | -60.44207 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8fa9178-25c1-32a2-a04f-b84989d74cee | 1.29336 | -60.43035 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 859c16f0-84ce-3ece-9a78-637ec3093298 | 1.20811 | -60.12864 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d275ee9-d15a-3331-9ccf-f82bc5e0313e | 1.31646 | -60.06667 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bf85f04-69b1-31c9-923b-631b594c0621 | 0.83098 | -59.95042 | 2025-02-27 05:59:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 564fec71-251e-3377-852b-aba58d5097b9 | 0.83052 | -59.94749 | 2025-02-27 05:59:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1646f787-0049-3a7b-b6ee-9a2a243d3278 | 1.28087 | -60.10192 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 225e3a91-e8cd-3549-b99e-3ac75c406e82 | 1.31692 | -60.06957 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16e6fbb3-5d77-3132-8065-8aaddadbf75f | 1.31144 | -60.06748 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cee4ad0-3a3f-35ce-92b1-08c2149b0e3c | 1.20856 | -60.13153 | 2025-02-27 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 808a4f9c-47ea-3cb7-8c9e-8d7839a2f2e5 | -21.04882 | -47.77934 | 2025-02-27 06:05:00 | AQUA_M-M | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 2e052feb-bc64-3fbd-ba95-c309b5ad27e4 | -21.0506 | -47.77438 | 2025-02-27 06:05:00 | AQUA_M-M | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 544dc211-3088-37ed-82b2-d7e0ad3bc0b1 | -7.05117 | -44.34623 | 2025-02-27 12:18:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fa6e8e64-efc4-3dd3-8840-b002d44af5db | -7.43628 | -35.6677 | 2025-02-27 12:18:00 | TERRA_M-T | ITATUBA | PARAÍBA | Brasil | 2507200 | 25 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 2c3362f9-7fd4-36f1-9ca5-ad9908b5e1b3 | -8.12065 | -43.13962 | 2025-02-27 12:18:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fff43762-4ec2-38fa-8354-eb0fc986faff | -7.81265 | -44.18912 | 2025-02-27 12:18:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 179bd3e8-f949-3a06-888a-503a4360802e | -7.81397 | -44.1801 | 2025-02-27 12:18:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 81826ebc-5938-3a37-8b13-d8c8e1b1d7d2 | -10.52846 | -44.66933 | 2025-02-27 12:18:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 45b10395-e7ef-31b8-9106-fe97c99aaf62 | -8.05472 | -42.31242 | 2025-02-27 12:18:00 | TERRA_M-T | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 301e64b0-4226-32c5-86bd-402307d0798d | -13.91205 | -45.31638 | 2025-02-27 12:21:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c80d7436-c8b3-38a4-859b-19cd0f271376 | -15.14283 | -43.80189 | 2025-02-27 12:21:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| eb2eb774-ace8-359e-84ed-d0705ba675f3 | -13.9001 | -45.32682 | 2025-02-27 12:21:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 9c5af5ca-2f08-3d90-9fcf-520ef108685f | -13.89876 | -45.33599 | 2025-02-27 12:21:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 559de46d-3976-3381-b8ae-401dc4edd67f | -13.9134 | -45.30723 | 2025-02-27 12:21:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f234ee8d-fc31-364a-9220-bd38e9b72869 | -20.55814 | -41.29641 | 2025-02-27 12:23:00 | TERRA_M-T | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 524c7e5a-6fc5-3a36-9af3-bafff980c86c | -20.86092 | -46.22614 | 2025-02-27 12:23:00 | TERRA_M-T | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b2ed5f65-7f8c-3ce4-9462-b7342f78e48f | -21.72399 | -45.60444 | 2025-02-27 12:23:00 | TERRA_M-T | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 87d6d8ef-de08-38c7-98ee-5d00716f0012 | -19.44707 | -44.82991 | 2025-02-27 12:23:00 | TERRA_M-T | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e46d5add-26af-393b-9e70-0a225e9097ed | -21.05508 | -47.77593 | 2025-02-27 12:23:00 | TERRA_M-T | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2380a898-b22b-3516-9df8-3af0037ccf39 | -22.53361 | -44.36596 | 2025-02-27 12:23:00 | TERRA_M-T | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 332ce360-3619-3796-b9f6-24c47d3612bf | -17.18853 | -46.61106 | 2025-02-27 12:23:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5c4a24ba-b55c-3bd6-b340-0c11766c5a65 | -22.62193 | -46.99424 | 2025-02-27 12:23:00 | TERRA_M-T | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 566ee7db-948f-3e3c-b861-786300cad895 | -15.70932 | -46.44243 | 2025-02-27 12:23:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b7bb55c2-6508-3f51-964b-c39194412fbd | -20.20176 | -40.31183 | 2025-02-27 12:23:00 | TERRA_M-T | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| a2417f66-a2b5-3dd2-8b17-0ee519518924 | -23.00953 | -44.53027 | 2025-02-27 12:23:00 | TERRA_M-T | ANGRA DOS REIS | RIO DE JANEIRO | Brasil | 3300100 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| ffee1804-cf97-3e73-be07-f1d80d6b9b10 | -20.55991 | -41.28117 | 2025-02-27 12:23:00 | TERRA_M-T | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| ed44ccc1-e071-3bed-998a-655fbb4bc877 | -16.60212 | -43.8998 | 2025-02-27 12:23:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 48a1e383-ab37-3e0a-b830-28794c272dd2 | -18.48174 | -44.35318 | 2025-02-27 12:23:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7565cc98-067c-3ecf-ba9a-7911dc2f0e5d | -20.57784 | -46.96168 | 2025-02-27 12:23:00 | TERRA_M-T | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 606cf342-9639-36a3-be0c-0b8cbe127f15 | -21.05354 | -47.78594 | 2025-02-27 12:23:00 | TERRA_M-T | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 56f33c8b-d3e5-32c0-8db5-c9ab779115c3 | -23.88713 | -47.60276 | 2025-02-27 12:25:00 | TERRA_M-T | TAPIRAÍ | SÃO PAULO | Brasil | 3553500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 90310e95-b2e9-3cc8-a932-058b3f9f78a3 | 2.7989 | -60.8078 | 2025-02-27 13:40:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.4 |


