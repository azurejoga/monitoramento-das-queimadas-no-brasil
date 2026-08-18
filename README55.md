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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0b7608e-5f30-3d4c-979a-3a42b65ff929 | -8.57933 | -54.69674 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| bec65fd7-6736-3336-b8b9-2747ebb9ceba | -12.39974 | -54.95569 | 2026-08-18 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f31ecae4-ba8d-3a7f-a66b-9c2188ccadaa | -7.60703 | -60.95411 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e07c5f80-51de-3e84-8cbc-55f17498ba29 | -13.42344 | -57.06892 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbd21a87-cf71-32d3-af5e-35d3e710afe5 | -7.63751 | -55.62837 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2a30a87-2cf6-3c21-9ea7-f07d40429eab | -7.90742 | -61.73724 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a839898-0795-3ffd-89de-aebafbd3d056 | -13.40854 | -57.05148 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12e6d6cf-c369-3c3c-a8b1-36022026719c | -8.56163 | -54.68979 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f291797-59b0-3a1e-9e12-7cbbf2916670 | -12.94703 | -56.6456 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 932e79c8-cf79-3bab-8109-0df720bab70f | -12.4025 | -54.95599 | 2026-08-18 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b8ef73a-976e-37af-a9fc-e814ad0cd11f | -7.55608 | -55.56773 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69b669f4-1686-3190-8bb2-c7a610a99a49 | -8.22866 | -55.03573 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 80bd5094-b814-37a5-9258-6fe4b6047faa | -14.10832 | -58.4318 | 2026-08-18 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2be0832-5d26-3717-9587-08d887cdc9c6 | -8.55327 | -55.31718 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e87c8ff-2bfa-3b84-afcf-eafb3922a4ca | -9.52623 | -67.1655 | 2026-08-18 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6862291-06d6-3bf1-bf5a-bf00f264f2d1 | -7.88374 | -61.79463 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87861c68-b143-3ec5-976e-b89328448c2f | -8.73546 | -62.90281 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62179a7e-8352-33de-8201-f5241afb5f24 | -7.61024 | -60.95975 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33eedda8-406f-397f-bd4d-4c71de897ce8 | -9.1777 | -59.67378 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2949c04e-a7ee-362f-8fc3-1936d19996cd | -8.9003 | -60.54846 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b9c6afe-b706-3b76-8eab-517d99e73484 | -8.62799 | -54.70376 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18a31afb-0f9c-3652-a493-9d18dbc76663 | -13.43291 | -57.07571 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07f49abe-ac98-3fb7-b8e2-bcca36fd89c0 | -9.47418 | -60.50197 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52f6f88f-81ca-339e-88a6-3dea7996d8b8 | -8.55498 | -55.30429 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4de0a764-709a-3b75-a3be-30030a1ad7ab | -8.56046 | -54.69911 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e8991bb2-af65-3cf9-82cb-f695fad87f88 | -14.03103 | -53.68821 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 631ed679-94f2-33f4-b8c8-fe76699b87d2 | -9.30555 | -62.04554 | 2026-08-18 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4b9b69a-1517-37d7-8f73-4dbb7cf65971 | -13.40899 | -57.04764 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a4a7f60-79ac-319a-8a69-1d53689bac48 | -8.20493 | -55.0326 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a23f6bb-643c-3c41-abed-c7986b7d57ae | -14.03791 | -53.68924 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 07e207ff-08fb-3343-aa6c-2018c90a2fbe | -9.9691 | -67.86797 | 2026-08-18 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b791470b-5845-39d3-8df9-476754e1a541 | -14.03834 | -53.68451 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2f5dc569-665f-3195-a4ed-6bccdfc0995f | -9.01475 | -60.5034 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b7132e7-cc7c-3f44-abe2-456b118c1494 | -7.90497 | -61.72744 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af7303e6-7604-38c7-85d9-09e03e68cf6b | -8.58663 | -54.6881 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb909b4d-2c9a-32e5-b95d-b339b4f96077 | -8.95816 | -60.57522 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a609fd6-c2ac-36c2-b084-1573996d2fef | -8.08511 | -61.36455 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a4beabe-0625-305e-87c5-aec745e661e1 | -8.96497 | -60.52659 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee929baf-1cf0-3cce-b0c5-271c6333c2f0 | -8.96507 | -60.49572 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45e03197-80e4-34ed-8f30-d97300012153 | -8.09569 | -61.34605 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a4f8c3e-e11c-31d5-bd3d-f1b567a5bf5d | -8.89798 | -60.59382 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddadadf8-3358-3446-9415-03702a758aae | -9.47836 | -60.50258 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13afbbfe-83b4-39a9-b2ae-e2e14b94bed3 | -8.08125 | -61.36394 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d2063a5-29f3-3be9-9514-ef7046b179c1 | -11.33062 | -55.27002 | 2026-08-18 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50f4ac7b-192c-3184-a93f-d4a343fefff0 | -7.88873 | -63.76523 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adc2a42f-2f38-33a9-a54d-c9889e9a8e04 | -8.57632 | -54.72039 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 597b79d7-2f8c-3058-8518-74777a0fc1a7 | -14.03165 | -53.68188 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a2d02984-1dde-39bb-aaca-6348ca819ca8 | -7.6164 | -60.94507 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 741f72fc-a1b6-3b3d-a5f4-d56b375daa1b | -9.16393 | -59.67614 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fc3dbc0-0896-30e8-ba43-09fa345e2291 | -9.84017 | -65.06393 | 2026-08-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b41c8fe8-f5ab-38ad-803e-a6e7695d4864 | -8.58792 | -54.72634 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 51e33e20-97d8-36f4-b184-69ba91f77558 | -7.9112 | -61.73779 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5bcdbe1-34c0-3c0b-a327-5bf1774acd17 | -10.27728 | -67.80894 | 2026-08-18 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b22ff50-e870-33de-a385-736fcefe8a6a | -9.16482 | -59.70265 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52492c1a-ae15-38e9-81bc-aa12b0be815f | -8.58361 | -54.71174 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a5cc25d5-3532-39b8-ad33-8732d04ec615 | -9.42993 | -60.44209 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 35058960-4daa-3184-ada3-25ab36cc3753 | -8.95711 | -60.58268 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 144dafdf-305e-387c-9f8a-751ee77b8d82 | -8.73607 | -62.89868 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6297742-48ba-3cc0-8600-51bfc96bf423 | -8.95357 | -60.5478 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4a81717f-3ed8-30ac-ab46-f3b5f30b1220 | -8.90425 | -60.57949 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c1ca5eb-331e-3259-abb6-955aab44e4f2 | -9.42736 | -60.4299 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7d874de-d071-3347-9b82-078f5bd992ba | -13.41696 | -54.38362 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ec5f3c0b-bec9-3de1-8986-98c8f1e4ecd1 | -7.63801 | -55.62449 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75985449-2263-33ea-8351-8eea4b13ebae | -9.17331 | -59.6731 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13186981-23e0-39d0-9e9e-dc01b3889b25 | -7.7839 | -61.11752 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 364e13fd-92b9-327e-8ff7-55e865b0e64c | -9.42641 | -60.40608 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 604fb45a-0288-35d6-86e4-e40bb6f8987d | -9.50909 | -68.49864 | 2026-08-18 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e7b4ae6-a159-30fe-9804-379a20336d43 | -8.58051 | -54.68753 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 2ddeca4d-b366-3a34-829e-ddd1ee0e48d5 | -8.90442 | -60.54905 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 222590c3-b5de-3211-9be0-396f9403d423 | -7.56898 | -55.55742 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 262ba404-50e3-36c5-b6e0-9d1457ff82c7 | -7.88685 | -61.79981 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0b2f991-b401-3e09-913e-a1de7e57a9c3 | -13.9361 | -53.9361 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b2e6925-a59b-3a1b-bd23-85386c2459cd | -9.16541 | -59.69829 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| abcfc725-967c-3469-8502-2b1c81e28f5d | -8.21306 | -55.01635 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56f66bb0-7557-3c55-97cf-60eb4f0dd458 | -7.88587 | -63.76097 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46f07e30-b912-34b1-ab3a-9cb798a4842c | -8.72411 | -62.9053 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44c948f0-10fc-3ca5-9de1-10f8ab2ea500 | -7.91875 | -61.73894 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44377399-d385-3d05-b4f8-99e5bfcb3999 | -8.58126 | -54.7301 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 52d3f3d5-d957-3c27-8149-8aa209a8e15d | -8.94587 | -60.51219 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef0299cf-eeb5-3341-a4b8-ac8a3159ef13 | -7.95188 | -61.82828 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3db6df8d-379b-3428-ade6-2d88c495d966 | -7.90675 | -61.74184 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c5934c9-217d-3f8d-a5dd-8a652abdb023 | -9.53033 | -63.66211 | 2026-08-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fae1d4ca-1268-305a-bf1a-34fb2a6204eb | -8.5885 | -54.72189 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 90134462-8045-32be-ba6d-9295143f92c4 | -8.95979 | -60.53348 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acaeef20-d930-3c08-9910-cfb5b41426bb | -11.37524 | -55.42121 | 2026-08-18 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 23a8082f-aff0-33ab-a78d-0a499ebc359b | -8.75635 | -62.91018 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93df445a-1d55-384b-86e4-0a63be16f652 | -8.55967 | -55.31382 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc0e00e0-f8ef-38bf-9e88-a8207402ae6a | -10.4148 | -61.2081 | 2026-08-18 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ce20478-e81d-38bd-b975-f3b06657c9fb | -9.16386 | -66.11833 | 2026-08-18 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b65743ea-8a98-3bff-9174-3c99f42a951f | -8.62839 | -54.70674 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c50b128-0f8c-3c1f-99e3-4a6928dd3ce3 | -9.4279 | -60.42604 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a415fd06-1008-3eb8-8331-6b40a6bf2871 | -8.7283 | -62.90172 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9794970f-06ce-3305-8756-c241728c7295 | -9.01116 | -60.49893 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a179b9dc-a668-3599-8a1c-660c81aa6f70 | -8.21678 | -55.03425 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 439a529e-5e92-33b8-aef0-059ffa44ca17 | -7.60242 | -61.23275 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9efc95e6-c7af-332b-a2e3-368b98e4c64b | -7.38173 | -59.99388 | 2026-08-18 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc3e58a7-f720-305a-b93d-73f5ad2a4a8f | -7.91253 | -61.72859 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd62805e-064c-32bb-af4c-4ad63a96d7ad | -13.41545 | -57.04081 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb86fd7c-037c-39e6-b457-28652df12a2b | -9.18267 | -59.67018 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34f2e002-c794-3df5-b6bc-ec29fed46046 | -9.01061 | -60.50274 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README56.md)
