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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a332435-aaf3-362b-8ec8-b6f420f61f0a | -6.67469 | -59.48899 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4a856a4f-7e51-3158-8480-89dccf115fd2 | -6.64982 | -59.77948 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8cb51df1-c7b2-3399-84db-3982606e06e0 | -6.60662 | -60.00182 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 62728c7e-d5ee-3fdf-ae99-d84b4ab3d84d | -6.54703 | -60.03527 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b2a45b5b-e3fb-3853-a52e-88ca5d11e9d7 | -6.54572 | -60.02579 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fca3bedf-7cdb-30b3-b68f-af4dcf5306e4 | -6.53843 | -59.77322 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fda4c26d-c625-3e00-ad5c-66cbea6cc335 | -6.53716 | -59.76395 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bfb4f357-0df2-3647-a7c0-b7b546d60c60 | -6.52227 | -60.058 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e41712b8-1f9e-31b0-b607-26dcc944c834 | -9.28134 | -60.25655 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 143b6518-3288-3757-ba87-9a18d1b0d62f | -9.23276 | -60.36463 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c25c7496-ba93-33fe-af92-691f59c0eb30 | -9.21719 | -59.77468 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c87f32c6-3d0a-3ff6-a289-258352973741 | -9.20795 | -59.77598 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 722cb04a-3593-31ae-8e4a-de151ae0fc9a | -9.17423 | -60.36206 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6096884b-6d3b-3cf0-b74c-c4f5a2833518 | -9.15557 | -60.40228 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e824537c-30b3-3933-9f51-43580f2f753a | -9.15417 | -60.39185 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 783f30d9-93c9-3b08-a635-4a1ec3927880 | -8.79862 | -60.15631 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9ccbdc75-37b6-3751-ba0b-ccbad80c336d | -8.79725 | -60.146 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c3ccfc10-d834-3579-b676-59b979cdf4d6 | -9.28166 | -60.80593 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 10ccb045-4368-3bec-b6f5-14edeeb08944 | -9.26352 | -60.81955 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 36c14048-3291-341f-ae9d-b96fd6fe83ce | -9.20877 | -60.79907 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| be41bc56-56a6-3a42-a3c4-d0516f504308 | -9.2073 | -60.78806 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ca5b29b9-40ae-340c-8d3d-35280d320000 | -9.1956 | -60.7006 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 73d83d2c-efc4-35a6-be95-ced4b7fe14da | -9.18589 | -60.70191 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 451a59ac-2d78-3136-b58c-ff0fae16f9c6 | -9.18341 | -60.75787 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1e13bcf7-1d72-3614-a86e-24bf004e4045 | -9.07774 | -60.58057 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b2960554-3817-38a9-bfcd-62b404574ad2 | -9.07631 | -60.56993 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e1135ea5-7589-3e28-b0f9-42302d74dda8 | -9.3972 | -60.90857 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bc4ea1f9-0d51-3e19-b266-b10a4c180d19 | -9.38881 | -60.92114 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 35393e06-da44-365e-aa50-f2d9799f6032 | -9.38733 | -60.90987 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 5a6008e5-7613-3a11-809f-d78fba7ea522 | -9.94771 | -59.8056 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e08cddd9-73d1-3bdf-9ce6-54ae7487d7f0 | -9.93044 | -59.93742 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 99e3d076-7910-322c-8aa9-bb829cd5661f | -9.92614 | -59.8353 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| be97047d-ea45-3b2e-9b52-afaf50340721 | -9.91697 | -59.90839 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c9d5cda4-f4ba-393f-b0eb-12ac78ffcbec | -9.86881 | -59.83306 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c75af586-2b30-3a35-9671-1968873f218d | -9.863 | -60.11904 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f5b770a5-4872-3151-bf08-0f82f1f2cf0e | -9.85673 | -60.28939 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| cda0498d-4182-38dc-beae-89a591a56e0b | -9.85534 | -60.27889 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 93434429-5f6c-380a-b365-bd7694b4107a | -9.84717 | -60.2907 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 418f3cc1-d6c3-3932-82ed-a1e05cbc3bf7 | -9.84579 | -60.28021 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 2f8ca6c0-220c-3ee7-a735-97d205651aa7 | -9.8444 | -60.26969 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 95eb437f-c468-3527-af85-6699f23314b6 | -9.75383 | -60.42864 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3e771422-7036-3983-aa24-5f72a25c92f8 | -10.45714 | -60.11061 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 64aeedc6-0c87-36d4-bb1b-ca04a5e555f0 | -10.16948 | -59.87542 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a689171e-a6c5-3303-af17-0e74e87463c0 | -10.16812 | -59.86529 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 35fc5090-4906-36c9-839c-f91f59697246 | -10.75445 | -60.74995 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 66bcbc35-edcb-3589-9cf1-be1bc2b485ba | -10.74449 | -60.75122 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c81f95b7-5a12-35b6-b275-fc0f287c3c37 | -10.47439 | -61.25834 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 92248004-e6be-33c2-8fff-92174246e63b | -10.4728 | -61.24625 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e618b591-b2ed-390b-b516-842db25df8f6 | -10.43098 | -61.00718 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 974c2404-19c9-3926-88fb-f76794aed543 | -10.42091 | -61.00861 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7c42245a-7a6e-395b-8e53-b86e1a89bfaf | -10.41937 | -60.99685 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8a131f5e-ce33-34c7-b24a-ef64ab6af093 | -10.40551 | -61.29149 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 48e717e6-c927-302b-92ef-68b109be8226 | -10.40394 | -61.27905 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| ec69b1cc-d853-3e1d-ad6a-a0c847fd4149 | -10.40243 | -61.26709 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| e74f314b-122e-3396-b953-d455e2dac0d0 | -10.39666 | -61.2857 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| cb507e4b-5a12-3dae-9bde-3090af3ed0bb | -10.39636 | -61.21907 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 31ee104b-51d1-395a-9829-8d0977d70468 | -10.39503 | -61.27338 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 2f9d6e44-491f-3ee3-b832-823a31fbab16 | -10.39364 | -61.28014 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| fc493a4c-6ad4-35b8-a713-bff6a7cc936b | -10.39349 | -61.26173 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 21badce4-37e0-31b5-a030-295a76a62ef9 | -10.39213 | -61.26813 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 5dc6469e-ba00-33dd-b2f2-fe3c756e533b | -10.38553 | -61.20164 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 1ff882b3-5ccb-3165-ab2a-e6be9ef1e0bb | -10.3846 | -61.20831 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 0199bac5-9f0b-37a2-a769-4c01d59000b8 | -10.38308 | -61.19619 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 49ca6bc8-f97e-3562-aa0d-fe39cb87c81f | -10.38008 | -61.23909 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| b2e807d8-c6f3-3f21-bf8c-01e6464e9f28 | -10.37851 | -61.22718 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 1fbc29c2-818d-3a26-8314-73ed83850d29 | -10.37531 | -61.20292 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2bb2db49-f4b8-35ca-a03e-f933b0fa90db | -10.37214 | -61.17886 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c104ed81-d03b-3b87-b712-16d21e54c31b | -10.37054 | -61.16676 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a7647887-df20-34d7-bf09-26a872ce19fe | -10.36986 | -61.2406 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 086e50d9-3a84-32ea-a28b-35b309484e04 | -10.36829 | -61.22861 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 6307152c-635a-3164-9a05-3ce57ca6118f | -10.19208 | -60.89683 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4440abc3-eb34-30dd-bc99-cfad83c48206 | -10.1821 | -60.89812 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 65a7f747-b8aa-372f-b210-5fa8fcb5dbd2 | -10.0575 | -61.11737 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| bb38147f-2934-3ce5-9722-93687d4a576d | -11.40568 | -60.41663 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 11e977dc-281e-36e3-b5fe-91a9b891ce49 | -11.40422 | -60.40524 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1da1f2ad-ffe0-3f2c-b020-6fe6a6adcabc | -11.40279 | -60.39407 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f5d7e32e-b10b-3e3a-81a0-a37b063e7cc1 | -11.30642 | -60.43576 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1bd930a2-2998-3943-b17e-c51e0962767d | -11.29662 | -60.43727 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 419325c6-2c84-30a0-bbe1-416aadf55057 | -11.29356 | -60.33523 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e84f6cf4-42cf-38cd-849f-36515bb57c60 | -11.26549 | -60.36769 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7b7e4650-18e5-3bd8-928e-1e6bf41da21b | -11.26166 | -60.41422 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f60e7021-81d7-3d8f-bafc-5d3b28209b02 | -11.06164 | -60.44249 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1b4e1bbc-a3c7-3c5d-b6ff-d0ab59f12bb7 | -11.33917 | -60.53474 | 2024-10-12 01:37:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c518a069-27a0-3757-bcfc-4c5516b25165 | -11.31939 | -60.53743 | 2024-10-12 01:37:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 07b8d452-c72f-3b80-ab7b-1ca0fdbcf63c | -11.28175 | -60.49107 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 504e31fc-9a10-3eb7-bd2b-711a0b527df1 | -11.28023 | -60.47952 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 54bd8095-92cd-3662-baa8-937312947e3f | -11.27583 | -60.44608 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 2c55096b-14ac-3d3b-9275-d9d32d334ac6 | -11.27339 | -60.50377 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| cbc6d309-7f12-3ec0-9726-ce075a8e602e | -11.2635 | -60.50492 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8e90255c-4ce8-39ff-87e5-2daefe72eebc | -11.24965 | -60.55313 | 2024-10-12 01:37:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 55edb59b-dd3e-3f8e-b40e-b5636f496768 | -11.23912 | -61.35672 | 2024-10-12 01:37:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 75d151f5-5f73-312f-92b8-4bb9dec949d4 | -11.23514 | -60.4406 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 22613ef8-1a2a-3c09-b55f-e0a7ca08e8c2 | -11.23109 | -60.48687 | 2024-10-12 01:37:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1490d892-403b-37f2-82d2-10e3a0275b81 | -11.21947 | -61.3395 | 2024-10-12 01:37:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7d5e0cf4-6e1e-3b1b-920f-06f2d49305cc | -11.17752 | -60.62702 | 2024-10-12 01:37:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 7238c4bb-4101-37c6-ac9a-3f63d0309821 | -10.9133 | -60.95395 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e387b1f8-844f-328d-ae1b-fc76d7a9786d | -10.90582 | -60.89495 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5541b714-9237-303b-8c66-d36b51d117f6 | -10.81995 | -61.41683 | 2024-10-12 01:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6f42e68e-bc93-3671-a314-423540e708ed | -4.73515 | -60.80037 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2cf1d114-4458-3ca4-b137-c2aa40b8d7e1 | -4.73383 | -60.79061 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |


[Clique aqui para ver as próximas entradas](README26.md)
