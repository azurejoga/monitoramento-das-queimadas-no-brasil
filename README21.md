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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44b34c67-18a6-350a-8c49-51aa26e75c46 | -4.2558 | -46.3855 | 2026-10-04 03:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d6553fcb-00ca-32d8-b891-1e8bf53c06b2 | -4.2887 | -50.2675 | 2026-10-04 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 558.9 |
| 319de53e-1f05-3255-a5c4-692cd2776fc8 | -4.2702 | -50.2683 | 2026-10-04 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 339803e7-24fc-3e19-9e53-4bc3d532e88c | -3.1299 | -53.7431 | 2026-10-04 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| aa2c8268-54b9-3b7f-b34e-f551155ccb75 | -4.2745 | -46.3624 | 2026-10-04 03:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 44879a0f-24ff-3d37-a11f-7a97e2643ff3 | -3.1116 | -53.7234 | 2026-10-04 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 196.4 |
| 52c806d7-060e-3f38-9f37-22a8b19e38de | -3.4761 | -50.1094 | 2026-10-04 03:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 3d118054-8e3d-3611-9c0e-4a300ef20ce2 | -4.3072 | -50.2668 | 2026-10-04 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 9a7ddeeb-10fe-30c0-b192-2639a17e7e08 | -2.5842 | -51.8623 | 2026-10-04 03:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9ce3e83f-c9c5-305b-a051-5260d94be142 | -4.2888 | -50.2465 | 2026-10-04 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6af42113-1fa8-335f-bd40-1a684769bea2 | -2.7979 | -54.1134 | 2026-10-04 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 485aa5d5-dae0-3dad-a36c-57a334ca73eb | -2.8163 | -54.1129 | 2026-10-04 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 58ce6b42-9c9c-3bb0-8268-707a1ffb0677 | -4.2886 | -50.2886 | 2026-10-04 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 221.4 |
| 41735826-fc47-37cb-8183-fcde77b4077d | -7.54066 | -39.90997 | 2026-10-04 03:36:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a4069636-e1e1-315c-b0df-7ece66be2a10 | -5.73857 | -45.14743 | 2026-10-04 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 20de2a1d-2dab-3c3e-8a23-fafae194f757 | -5.12272 | -42.40891 | 2026-10-04 03:36:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 25f627d3-e6d0-3f58-882d-2bf6298f2df7 | -5.54966 | -44.21398 | 2026-10-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8070ed59-7bde-3704-b73c-dbc0805f2201 | -5.74125 | -43.27551 | 2026-10-04 03:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5869a4e9-d0a5-3666-ac12-b6190d97003b | -8.34431 | -38.96848 | 2026-10-04 03:36:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dff3faa1-c551-3cdf-8dfd-7742eeae502e | -5.73767 | -45.14539 | 2026-10-04 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4731a3d-a12f-33b8-a32b-39711749e38b | -5.54466 | -45.27256 | 2026-10-04 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd676e46-a8e0-3190-bb7c-c87cb914e1ad | -5.73661 | -45.15134 | 2026-10-04 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3900d16f-a421-3af4-ad3b-d0e2365f223e | -6.57118 | -44.15486 | 2026-10-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b330c43-ec8d-3df2-9545-0ce10a7c9e4f | -5.54861 | -44.21964 | 2026-10-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 384ed58f-cf54-3f2d-b40e-cbd4e138054c | -6.89806 | -43.68521 | 2026-10-04 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0149a9a9-6c49-3731-9cee-f20ef87ad664 | -5.07573 | -38.05926 | 2026-10-04 03:36:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e43fb1f4-ff73-3ae4-b09c-5262c5765697 | -4.73351 | -43.27198 | 2026-10-04 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bc0eee1-427b-3958-82cd-f3ffd2eac02f | -5.74425 | -45.15479 | 2026-10-04 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c451e53-4947-3861-828a-840b4331de61 | -5.12343 | -42.40479 | 2026-10-04 03:36:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b91f03a8-d1dc-39e1-b8de-e6065acabdc1 | -4.86227 | -38.98867 | 2026-10-04 03:36:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 083c51c2-3049-3812-88e2-67d7c1e002d0 | -7.97027 | -39.83662 | 2026-10-04 03:36:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b4b88501-514d-374a-a802-49b7e8d5f12a | -5.74126 | -43.27744 | 2026-10-04 03:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5cc8f3e5-44ac-37a1-a61b-ef8299cc97e3 | -5.55268 | -45.26754 | 2026-10-04 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 26af9565-78af-39f1-b873-f825a74190ca | -5.86586 | -43.60379 | 2026-10-04 03:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0530be76-0684-38e6-b6b5-1e7035f9e974 | -4.48229 | -45.54722 | 2026-10-04 03:36:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 66b9f78b-c51a-3952-879d-12c402a5ce5d | -5.12239 | -42.4083 | 2026-10-04 03:36:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 768b14a4-ef57-32f4-aab5-c0542367f2e1 | -7.1085 | -37.60393 | 2026-10-04 03:36:00 | NOAA-20 | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 81009bab-1463-3f76-b7ad-1e38b55205e3 | -6.70817 | -45.97329 | 2026-10-04 03:36:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20d3e5db-067b-377d-9ceb-a45d49bc1e85 | -5.73631 | -45.15961 | 2026-10-04 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47f1e1ee-03a2-3d26-8ce1-b425e7db3905 | -5.73748 | -45.15334 | 2026-10-04 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 955b786e-bc5a-31dd-bed3-a67d02229203 | -5.54878 | -44.21861 | 2026-10-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d180230-ce6c-3c52-8b71-7a45f6af5eee | -5.96051 | -41.31333 | 2026-10-04 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 48a3467c-e6e7-3abd-8ec1-27cb73fae42b | -6.30399 | -43.34202 | 2026-10-04 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 048594f2-28d8-3d3d-a897-eca7a2dff8e4 | -4.11866 | -38.354 | 2026-10-04 03:36:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a00b3019-1767-319f-b0e9-0a3473707803 | -7.45317 | -39.23091 | 2026-10-04 03:36:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b5d85a0a-8523-35bd-911c-b7178ce3e36e | -5.86486 | -43.60019 | 2026-10-04 03:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4881832-df8b-3e97-afa0-52dcdf75c627 | -5.86673 | -43.59888 | 2026-10-04 03:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2646502b-70e2-30c6-b6fb-86ac0aba643d | -6.57214 | -44.14971 | 2026-10-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9a4fbbb0-0ae2-3f48-8505-b9276d1977a8 | -5.96314 | -41.31108 | 2026-10-04 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 413d5268-8b1d-303a-b101-c4c0156035af | -6.31609 | -43.34428 | 2026-10-04 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe80a3d6-ccc8-3eb9-baf1-42d6d3ac33aa | -6.89719 | -43.68996 | 2026-10-04 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d615ab29-03fa-3e70-9a7f-7801081c79d3 | -4.9279 | -45.69716 | 2026-10-04 03:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42585d0a-9c63-35bd-9ec8-65dfc525ddbb | -5.12314 | -42.40419 | 2026-10-04 03:36:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6cfabcd5-708b-334b-a866-d560cf0f84ce | -5.96648 | -41.31081 | 2026-10-04 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2315c49a-c89b-3e7d-bf03-6b80e1568713 | -6.57024 | -44.15993 | 2026-10-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc494c45-422b-3274-89e9-f10d30c1f2af | -4.73435 | -43.26722 | 2026-10-04 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| feb1daba-b2b1-3d22-b4c7-f3d59912197b | -4.11943 | -38.34946 | 2026-10-04 03:36:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 257058ab-c928-38f1-91c8-5536a5cf0e64 | -6.30315 | -43.34665 | 2026-10-04 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62ac76bc-b14c-3f4f-a410-d422eeeeac7c | -5.96255 | -41.31455 | 2026-10-04 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cfa7ba4d-53fb-3560-ac7d-f3884391a7c9 | -5.74309 | -45.16103 | 2026-10-04 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b364b2cc-6640-3649-a93e-0b9f9f148a9d | -11.70483 | -43.63609 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1dcac5b0-da9e-3294-a131-beed0e900ce2 | -11.81702 | -43.54305 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5888bf84-23c7-3a15-a021-aca0bd02727e | -10.70302 | -44.20358 | 2026-10-04 03:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f85b41d0-1bb7-3b2d-ae5c-1e9b679b4b02 | -11.81205 | -43.53889 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7eaf97c7-f713-374e-ac91-12546a4dd794 | -9.88174 | -36.40063 | 2026-10-04 03:38:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec7cd921-1c00-323c-8d0a-ffaa3e16e1ea | -11.81546 | -43.55088 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a4330b9-ace4-3cc8-9eb8-52aa41f31cd4 | -11.81743 | -43.55075 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2b363e8-7204-3b05-8b34-758f28e23857 | -10.69712 | -44.20221 | 2026-10-04 03:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6b80cc67-0a8b-3ba6-86c4-d83ed911d01d | -12.68214 | -39.09563 | 2026-10-04 03:38:00 | NOAA-20 | CRUZ DAS ALMAS | BAHIA | Brasil | 2909802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 47a0c6a4-92e3-3524-8ccb-22356e6cc25c | -11.70776 | -43.63557 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6d9453f-ac86-3eec-9fdc-362dee6032c6 | -11.81823 | -43.54658 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cab4e9d2-ba94-3ac0-9ad5-ed10083dd4fb | -13.37646 | -41.34518 | 2026-10-04 03:38:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fd68c829-21e0-3f45-baa9-aa8eccd68329 | -11.81247 | -43.54642 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 391a4bd9-10de-3c3d-90d5-54197589d9b4 | -11.81627 | -43.54678 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ba3d9a1-0bfb-30e1-b318-ee4d047c622a | -11.70696 | -43.63958 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74cff902-4721-3072-9f8f-f370fe7ae33a | -11.81391 | -43.53889 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dc826e8-9b93-3833-b662-0d0656497128 | -11.8196 | -43.53944 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83120d42-31e9-38ee-ae18-172ea27a3d0e | -12.72512 | -41.80935 | 2026-10-04 03:38:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7cbc031a-2e72-37c7-b4fa-f770c2d957dd | -11.8113 | -43.54263 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a352191-4c1a-3a77-ba4f-92377d8a65fd | -11.8128 | -43.53514 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec00139c-d3b3-3337-98b2-ddb915c0c07c | -11.81772 | -43.53951 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 938c4bdb-8b9b-337f-bb08-ab233d96c450 | -11.8132 | -43.54262 | 2026-10-04 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26697f5d-1162-36e0-afde-ebb70d960694 | -3.1299 | -53.7431 | 2026-10-04 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4bff724d-f286-35fb-b5fb-b1f334c2b7e5 | -3.13 | -53.7229 | 2026-10-04 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| edd633a6-e26d-3194-bbac-3585150f19db | -3.0548 | -54.2277 | 2026-10-04 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 30d3787e-5a1e-30e5-9713-b26d74b9786f | -4.2745 | -46.3624 | 2026-10-04 03:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 9945f0cf-9b1e-333f-aace-2b36193d23d2 | -3.072 | -49.5525 | 2026-10-04 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 3ffdddde-05cb-3b99-b899-5678467ea11c | -3.0364 | -54.2282 | 2026-10-04 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 28755789-e2bb-3a71-a860-689154709ed8 | -3.1116 | -53.7436 | 2026-10-04 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 164.7 |
| 7504a904-daf5-3164-8ecc-5d6e7659ce1f | -4.2887 | -50.2675 | 2026-10-04 03:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 631.0 |
| b69a447a-acff-3927-8a2b-8ce3da3cbb76 | -2.5842 | -51.8623 | 2026-10-04 03:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| bb153fe0-95a7-39d7-97f8-3d3adbd87016 | -4.2744 | -46.3846 | 2026-10-04 03:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 63037dbf-0aa9-39c2-b192-8f53dc77d87b | -4.2559 | -46.3633 | 2026-10-04 03:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 61b06307-0354-3265-9b74-a72617afd8c8 | -3.8756 | -55.8184 | 2026-10-04 03:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f6f41a87-d368-3588-adf3-d0f5fb113d80 | -3.4761 | -50.1094 | 2026-10-04 03:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 700400e2-e3f0-355a-8baf-3ed9dc3c872e | -4.2702 | -50.2683 | 2026-10-04 03:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 182.0 |
| 930bf9bc-f80c-30c9-bb7f-52ef91301428 | -2.8163 | -54.133 | 2026-10-04 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 129b57f2-9190-3540-a5c3-aa8a0980bba0 | -4.3072 | -50.2668 | 2026-10-04 03:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 78d9d9fc-1d9c-3e57-a023-df273aa29c99 | -4.2558 | -46.3855 | 2026-10-04 03:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 95.4 |
| a028247c-fc97-3480-8cd2-148bf378d284 | -4.2888 | -50.2465 | 2026-10-04 03:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |


[Clique aqui para ver as próximas entradas](README22.md)
