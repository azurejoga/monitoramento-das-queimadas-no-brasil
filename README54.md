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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0301bc96-4581-33e3-bc56-36b97729d916 | -3.6143 | -48.91912 | 2025-10-16 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1188a364-6c4d-3df6-81d7-395744eba7a1 | -3.43433 | -39.64842 | 2025-10-16 04:38:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 732af72e-be6e-3122-8eee-757d0e9d5d81 | -7.16852 | -42.52292 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e206f154-0612-36ad-9438-490781df1f44 | -6.05364 | -41.93593 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5e8ddf34-375e-3729-8ea1-819791a1f1ad | -6.21671 | -41.55085 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bc70b1b8-acfb-3308-b831-d598915cd1b0 | -4.03387 | -50.88253 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8055cd56-6c4c-30d8-8a87-9d75bb2e2b02 | -7.2023 | -45.48648 | 2025-10-16 04:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5eb9fb41-f542-30db-8490-d746451b059a | -7.0452 | -43.97339 | 2025-10-16 04:38:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab7ce505-d8cf-36ea-ab20-a0b50a65b439 | -5.46627 | -44.64298 | 2025-10-16 04:38:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3608e800-bf2a-3c97-a518-5805b018325e | -5.83595 | -42.33722 | 2025-10-16 04:38:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c814b1da-6ea6-3161-aaad-f9a56d134138 | -4.67124 | -44.11252 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ede1d1c-92c4-30d7-acd9-399b5056b088 | -6.59459 | -43.92159 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d33c8d7e-3519-36f8-940e-a4043c130833 | -6.56865 | -42.9685 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a5c72f0b-7dd6-3b18-ae43-b2caaf849c60 | -2.05407 | -48.79956 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce463aa4-32fc-333e-9635-f35029412e6d | -7.47185 | -41.51601 | 2025-10-16 04:38:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c6dac751-929d-3746-b362-8dc7c379120f | -5.46794 | -42.92914 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| a153628e-fd8b-35d6-8fc4-b3ef0e970cac | -8.25326 | -44.08152 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d6d9c57-8bb6-3317-a629-ce0c8bf6ffbb | -4.56294 | -44.00293 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 337abc7b-a5d0-3bf6-976b-41cc2dee46e2 | -4.25802 | -48.54972 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4058deb5-df60-3f9a-a9aa-a6a6083b4952 | -2.74173 | -48.56038 | 2025-10-16 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6e7cb0b-29e5-3c87-ba9f-0fb278d6ffe9 | -4.66188 | -44.0934 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 82fe7031-ac17-3fa1-9195-895aa6f950b9 | -7.08084 | -41.94268 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cfad15dc-88a3-39d3-ab47-03a2183480fa | -5.85225 | -44.66801 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efca1377-4e64-3a14-8ea4-339e289aea44 | -5.47046 | -42.94239 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1c6ae08e-7d70-36bc-bfcf-4228775ee6a6 | -2.88677 | -50.7399 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88d6b747-182c-3c0c-8fab-3deb193b04a5 | -5.7476 | -44.98476 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9cb4425-391b-3aa7-b6a0-3264e7fcf181 | -8.24109 | -43.41759 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 98e5d693-455f-3f12-8bbc-459272228b84 | -7.93712 | -44.12133 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 955bf9e2-e69d-36b3-9d61-b472ded74ab6 | -4.38478 | -43.37964 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52253792-d237-3b9f-80c5-06aff594a283 | -5.76918 | -47.90747 | 2025-10-16 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51c10bb1-41c2-3c60-81ed-1e08e6f04c66 | -4.25472 | -48.54921 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68cd7c47-553c-34e3-8a9d-5e2907c32331 | -4.78434 | -43.54871 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bacbe335-aa34-38ad-83e7-0220432bc8af | -6.33333 | -44.31655 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 739c6e8b-7c79-3971-bd9a-ad03679c9390 | -3.92756 | -47.697 | 2025-10-16 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bc195eb-e8dd-3443-b36a-7c44d8545a6e | -4.92902 | -41.54984 | 2025-10-16 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b73ef4cc-1444-30ad-89aa-365cf0e24f72 | -5.29683 | -41.17779 | 2025-10-16 04:38:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8e09ad85-f80d-32d0-8280-5ab4f4b4a043 | -4.67281 | -44.10217 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| dd7caf3b-ce69-3491-bd81-b40ee6386bc5 | -6.80505 | -44.54022 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 802af41e-ade2-36d1-918e-01aedde7c611 | -5.23686 | -43.67479 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b3b3e57-ce00-3c81-bdb6-526c33e5e937 | -6.32434 | -46.32091 | 2025-10-16 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa7fe1a0-fca2-3394-b4e5-b3648be30bdf | -6.01277 | -43.1194 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5444b47c-f05e-397e-ae95-d9bdb541a4bf | -4.66724 | -44.11197 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4109c043-b6ae-36e8-bee2-8715c30132fc | -4.01136 | -44.16836 | 2025-10-16 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8b2104c-d0b4-338f-a734-05f4055bb454 | -7.16753 | -42.50089 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 45b487bd-1888-3791-aeba-3d7ca4760a1f | -3.05662 | -52.65746 | 2025-10-16 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 869e5d59-97eb-3e3a-bb39-b448f2c1c081 | -5.97012 | -42.91065 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 47409103-65fc-375c-a81a-8e90a05c7a4c | -4.81179 | -43.21372 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41988b31-99a6-3cec-a6fd-b3e0a6ccd084 | -6.50822 | -44.461 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e92f5845-9c7f-3263-aaef-d5003e5837f7 | -5.58354 | -44.75018 | 2025-10-16 04:38:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e03d3b84-0cb4-3028-bef6-5ca5db864b61 | -5.85258 | -43.87458 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33ccc7b4-5449-33ad-9b8e-48e43625b17d | -4.78041 | -46.61698 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f331aa3-6d68-3f7b-9c7d-602a292280fd | -8.2519 | -44.06437 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0484302-7efe-3585-ae7a-789b7accb15f | -7.93132 | -44.13233 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ceeb6b76-bcad-3580-a104-d0f148b95954 | -8.25571 | -43.3432 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 09e877d0-5956-304f-94b7-b93a143067c7 | -2.87931 | -50.74258 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b34e7b80-cbed-31f5-bbd5-9c85ed65fb91 | -6.06453 | -44.30838 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27b2fa4a-eb50-3775-a07e-281433362e4e | -5.96493 | -44.79928 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd3d73f0-14e8-3362-9fc7-8c00c85ccfce | -4.92977 | -41.54475 | 2025-10-16 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b92c435-9aea-3df2-bb5d-f2e95910e320 | -6.31372 | -44.72174 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2df4e6f-3c2c-3fc5-be07-c30c0489480c | -5.43238 | -40.98424 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 959c3cba-7a16-353f-8063-9e6377a9e679 | -7.0084 | -43.74947 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5e86925f-73c3-312a-a3aa-01cb79346a04 | -5.4567 | -41.02745 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6e7a5c7f-f7fc-3582-90e7-701b9d8207dc | -6.04892 | -41.93519 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 90f88851-be43-36e3-b097-7e1d9f2ec988 | -5.16118 | -44.99131 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a566316-4f73-318b-a35f-1ecfd1cb8857 | -4.69063 | -50.77373 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a17415a-a77c-3ac5-bef0-bf86988d6eb9 | -1.48732 | -55.44346 | 2025-10-16 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab1c1b78-b274-3014-aeb1-4a752121f303 | -5.9569 | -42.24531 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4468be32-4de8-3de9-82cd-ff3f8e4ca57b | -1.98935 | -56.92252 | 2025-10-16 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5961d75e-14ba-3d8c-8701-ed54431bd3cb | -5.46671 | -42.93752 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 586faf4e-bfa4-3e5b-906f-8c1a338fe8d7 | -6.40008 | -42.55526 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dd3201e7-698a-36c5-a38e-dc6fdd110397 | -6.33283 | -44.32 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06ba808d-9c99-3fe6-9957-70b4c0a27f36 | -2.88107 | -50.73136 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 880ad774-5808-3aed-ab60-ed45292b7467 | -7.89972 | -44.98884 | 2025-10-16 04:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e23225d7-611e-351d-8637-67082db26213 | -3.68312 | -47.63043 | 2025-10-16 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1510815d-6f6c-34d4-b200-b054711fd80b | -5.47108 | -42.9382 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 72cce1f3-88c7-31ea-bafb-bdad7f5130e7 | -3.85298 | -41.56361 | 2025-10-16 04:38:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d5d0ab27-5860-3f2f-8bd3-20ae40774f3f | -4.36227 | -43.38777 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e24f076b-36c9-3621-b4dd-c62826ed376a | -6.17842 | -46.73976 | 2025-10-16 04:38:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7825c37-bc54-3ac6-b030-19752659b953 | -6.00145 | -44.2231 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 843581df-bbe9-3e71-baec-f4c3ef3c58c3 | -8.20098 | -43.31971 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 0da4b183-ccb3-3dfb-8a35-599381bc0005 | -4.39314 | -43.38085 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f35fa4fe-aa23-39d4-9e4d-3fa3969455c0 | -6.23936 | -44.98149 | 2025-10-16 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8511890a-56e0-3e93-a441-99b8e8c94543 | -4.15328 | -43.12938 | 2025-10-16 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5c901b0-36c3-318b-a43f-6eec3c7b9806 | -6.59097 | -43.91729 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 140bf120-77e2-3b48-b5eb-f9d6efc6bc6d | -4.36172 | -43.39156 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4839feac-460c-347f-9c34-d24eea39e3b1 | -6.62435 | -44.43436 | 2025-10-16 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c95c086-d2f6-3d33-b74d-754fce50a5c7 | -6.71391 | -44.39318 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf51bf88-13d5-319a-82fc-5e63542ee06b | -3.07731 | -49.50132 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c69d13a9-8a2b-36c9-92a2-77eb28425ec4 | -4.91775 | -45.97777 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae6c1222-3f1e-3de5-89d1-767695d961fd | -2.25578 | -56.05562 | 2025-10-16 04:38:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24df01f3-09b3-3003-a67f-32b693baf597 | -4.28633 | -48.62804 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54aa2342-91d1-39be-bff0-a5251cab619c | -8.25383 | -44.11283 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3231c0b3-f46b-351c-b22f-16fdb4515695 | -7.95332 | -44.12758 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1618dbe4-34f9-3b33-8bce-dc83aefae0e7 | -2.44725 | -49.37368 | 2025-10-16 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2977fadb-06c2-3f31-a9e9-c3c78ae8e525 | -7.05206 | -46.68564 | 2025-10-16 04:38:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1778ad62-54f1-334f-8d5a-5727cb83226a | -3.65696 | -51.74789 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f5bfa17-06ec-35e0-945c-974019e21c73 | -5.87773 | -42.80247 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 72ec6edb-0d4e-38c8-893d-54f2e6d45af2 | -6.22448 | -47.03605 | 2025-10-16 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e2ab5db-b226-3e9d-ad65-6f046b10e04b | -6.94975 | -42.68445 | 2025-10-16 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c5beaa8-511d-3adf-adf0-970144b40be4 | -2.88048 | -50.73509 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README55.md)
