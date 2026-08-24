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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbf4e6cd-da73-3ab8-aa2c-d90db3cd5aaf | -12.09802 | -50.60587 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| d4d8328c-c26c-34d9-9cbf-eeca491f414f | -13.6883 | -51.83664 | 2026-08-24 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e42f0e7-f19a-3b0d-9379-596bdd5e972f | -8.67881 | -62.84618 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95c7522b-8e05-3719-9e40-ca8bfe7690fc | -9.2227 | -60.77548 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b38569b8-0fe6-3f8c-aab8-8531fc0c7757 | -15.28942 | -52.8159 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6f7cbe0-668d-3698-831c-97189e936690 | -13.27452 | -51.44305 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5bd4bc0f-cb16-336c-a4ec-f9af285d39f3 | -9.24516 | -60.83697 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78ed8fb5-7cf2-3bd6-8825-9801586dd474 | -16.41384 | -51.83462 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6073a44c-b35c-37c7-93e4-9028625ad5ea | -16.4188 | -51.8407 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a1e07f2d-986b-3d0a-90e9-1b3310d9b6d6 | -8.93766 | -62.14103 | 2026-08-24 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 131d5d69-2350-3333-a238-d540664af758 | -12.12593 | -50.53524 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96c3f4af-4c53-3ead-a425-34e756d99fe6 | -13.16796 | -51.3912 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4f015921-ccca-3771-b313-9664f8d1a0b4 | -9.21381 | -60.90542 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8824212a-4b72-3f90-acbb-a085ae014a07 | -15.27631 | -52.87512 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d835c6df-b29d-34e1-9b99-ba453c6d0a56 | -15.58979 | -56.00797 | 2026-08-24 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 716d8b14-ba6d-378c-b13e-2ca3234f5035 | -12.10822 | -50.61179 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 6e457d44-73b6-3860-89e5-a1a511cd66cc | -15.20364 | -52.80377 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9c97348-4132-354d-a836-71080f812702 | -9.40075 | -60.5944 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d461e0b-bf6c-3179-b797-0e078f9a2317 | -9.17699 | -58.07001 | 2026-08-24 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba64b8ff-bdc4-3490-9d3a-6880d2c1e615 | -11.91776 | -55.90514 | 2026-08-24 05:31:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50c098de-01f6-3cb6-8990-bb2115914648 | -12.10284 | -50.59884 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9cc9f65d-cb9c-3d48-b57a-006ed7af1237 | -12.1401 | -50.53083 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a5ea7c8-cba8-3863-9560-1897a342c248 | -12.11339 | -50.5894 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6acb2be4-dab3-3454-810f-562c3873e5f8 | -12.11403 | -50.58332 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e234376b-262d-3144-9179-e0a2940fc973 | -15.26972 | -52.879 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 291a9862-5aa5-33bf-aa8d-5429c1f55469 | -15.26826 | -52.84151 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab87c432-d5d7-3c3f-b708-b3a6e8e4400e | -9.20391 | -60.83073 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aa86f49-dd86-3832-b3ca-ea214084bbc9 | -8.66281 | -62.84011 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5d20e17-6416-3460-9572-36cd2033d6eb | -15.26689 | -52.85506 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48311a7b-e926-379e-a778-501d96bab726 | -14.59989 | -53.18624 | 2026-08-24 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b1a913f5-5ec4-3552-854d-b970acc44612 | -15.27345 | -52.85124 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 203daa95-efb6-3055-8aa2-25caec3121d9 | -11.63417 | -50.53514 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d02c9c1a-7bad-3742-a971-97b1f6918b86 | -12.09745 | -50.58587 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 156aec7b-9323-366e-8eb9-bde2b4a13d37 | -9.20645 | -60.93112 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac98fe89-384c-3789-bdda-12d7d69e4ee4 | -14.41139 | -51.78099 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f04ee34c-9686-3b53-9bb7-cb991b9de836 | -9.86 | -60.13288 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b0f4361-7048-3179-9b45-4048f756ec95 | -9.40423 | -60.59492 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1d2a2df-03d4-316c-a228-f1974ca2d026 | -11.90912 | -55.89942 | 2026-08-24 05:31:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 585b567f-451a-3487-a42f-aa2fa1dcbad8 | -12.11531 | -50.57116 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd4295c1-e1da-3702-9817-d330bad04252 | -8.66666 | -62.83715 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d92d6d5-aafa-3fc9-b2cb-f7c1a06deea9 | -12.12399 | -50.55365 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4dc53d7-c45c-351a-bba0-2151eeefa6de | -9.40133 | -60.59055 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f011697-dd6b-333b-9cae-c96a066d2f90 | -15.35505 | -52.78057 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7383b15e-8460-3f5e-823c-714b1531bfb2 | -12.08938 | -50.59715 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 3e916628-a469-3895-bf94-5c2153245a12 | -15.67081 | -56.10135 | 2026-08-24 05:31:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acf9b1d3-f4d4-3083-8fe0-cb56ddbd235a | -14.32313 | -51.86413 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 90fcb731-a286-38bb-99ff-84e6e0659e91 | -15.27711 | -52.87577 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d271da23-b1dd-303a-b106-580b28d98d0c | -16.66054 | -54.70562 | 2026-08-24 05:31:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9cf6864-0145-38e1-b3fe-a896b86846be | -16.66016 | -54.70919 | 2026-08-24 05:31:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8146851a-701e-3dbc-9d55-4fc8dd4de49c | -14.29222 | -51.78891 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12b1c45b-fbff-3eec-84e1-23c0f17202e3 | -16.0634 | -50.44152 | 2026-08-24 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b2a89338-c179-33d1-8dda-5fa778556d09 | -12.1116 | -50.5815 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| eeb5f5af-8c2f-3df6-99e9-9c2863a555a7 | -16.38779 | -51.82948 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0b6e7b71-5b6c-3d8b-81f0-c076f8f40ac5 | -10.81047 | -50.94489 | 2026-08-24 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 391032d2-38c1-38ad-914d-df6f8c4683fb | -12.11595 | -50.56503 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce84ae91-7b70-377b-a337-14cbcd0239ce | -16.05509 | -50.45443 | 2026-08-24 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 472fc0be-7733-3877-bf10-b2684198c89a | -15.4478 | -52.84592 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae15ea2a-3c0c-3129-a5a2-94494d19aca2 | -15.27025 | -52.87414 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| daa3d87b-07a7-388a-90d7-2ce43a66a392 | -12.11788 | -50.54664 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6001c28-9936-349e-85b3-9966651f850f | -8.67051 | -62.8342 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d660e185-fa7f-3112-b114-4a5363557cd1 | -16.65997 | -54.70771 | 2026-08-24 05:31:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6f9c35c9-14fb-3e46-9130-fdd35e5eb1ec | -11.19947 | -55.0753 | 2026-08-24 05:31:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 452df62a-e225-3f1c-a9ac-f7d25d5ad7d8 | -12.13204 | -50.54225 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd2e00e8-088d-31ea-9116-2db32033fdba | -14.33578 | -51.75517 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc4e26ec-fb88-3b1d-a7fe-5d6ee5791f4d | -9.39438 | -60.58952 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d028f7b-056f-38f4-b844-f2b8f5ddf452 | -11.67189 | -54.54591 | 2026-08-24 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1f2fa1d9-d41d-3554-b45e-623badfc1c5b | -8.66612 | -62.84063 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 487a8761-26ea-34c1-94ce-481436361034 | -9.38801 | -60.58459 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70304f04-4594-32d4-a26e-7842cda71e0b | -9.87071 | -60.10938 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28eae8f3-ef79-3cca-9f22-5cce895fd659 | -15.35473 | -52.78714 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3269bc12-f6c0-3ee6-8407-501c1fe16c90 | -8.67496 | -62.84914 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59748454-0937-3c6d-b5d8-a493e67d4456 | -12.06444 | -50.5755 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 16c463f1-5c15-3462-8012-9cd043e9de2f | -14.35456 | -51.76298 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8d51d58-7163-3ac7-a888-e61519bdefeb | -15.265 | -52.87369 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a92ef621-c1ea-3916-a060-6c6505b6f8dd | -16.4132 | -51.84118 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6fc8792-1832-3bb3-bdfa-951c227da40c | -13.27495 | -51.43953 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c962591-5e93-3b07-8569-601c9d999074 | -12.12645 | -50.57101 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c489d777-60db-3f6b-ba70-b397c23956c0 | -14.40623 | -51.77942 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| db9a2ad1-6b52-3c2f-ab26-ea82f5806f6b | -12.11834 | -50.58235 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd76b512-bae1-30e7-947e-1a467a5ef021 | -15.79172 | -56.06601 | 2026-08-24 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d7514624-ae71-37d9-8d68-f17f7a27b604 | -14.33433 | -51.76097 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54468df4-3ac7-3579-b962-41da76a8ad60 | -15.67578 | -56.10199 | 2026-08-24 05:31:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7225266-2a78-3248-bce6-f69a8e685688 | -13.89653 | -54.03847 | 2026-08-24 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a8fcae6-7b23-3390-b335-a0d91a8952b6 | -9.59225 | -60.503 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31474f1f-262b-3fa2-8779-6f639874bbd5 | -12.12244 | -50.54572 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60dbe9d9-88cb-358e-9769-39a4c0a52ce2 | -9.27656 | -60.90664 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c30fa4a-fb9c-3f1b-bd22-3a38fc52f86a | -13.17385 | -51.39758 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9e2ce965-6b40-3ffe-b6ad-cc502d2cb7e3 | -15.35516 | -52.78283 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4857c13c-7b8d-3983-88a7-adc8fd0e22e8 | -9.10074 | -60.91133 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2308817f-a4e6-336a-a0eb-aa5261bc3077 | -9.50186 | -60.50157 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d38bd6b2-90b3-3a4b-bd1f-7be49a5bdd35 | -15.4106 | -55.7769 | 2026-08-24 05:40:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 48609fd4-9796-3027-8644-88c7452c163b | -7.7034 | -63.3249 | 2026-08-24 05:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2bf97803-6094-3f5e-bc5d-88b97dadef4e | -16.0919 | -52.3335 | 2026-08-24 05:40:00 | GOES-19 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 42dc1cf1-f9a2-304c-b9ba-6a183aa5a555 | -7.6665 | -63.3261 | 2026-08-24 05:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 0a217e09-1de7-39ea-9829-323ad8bed6ce | -7.6849 | -63.3443 | 2026-08-24 05:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 6eab6038-0017-3ea0-a77e-0bc7c75b14bc | -7.685 | -63.3255 | 2026-08-24 05:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 187.2 |
| 0ea5a24f-a9ff-3054-9033-8043f48d189f | -7.7034 | -63.3249 | 2026-08-24 05:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 21fc0cdf-59a9-32bc-b6b0-bba7cea51d5a | -7.6665 | -63.3261 | 2026-08-24 05:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 742eb6b1-19d6-37f1-afdf-5263dfe6605e | -7.685 | -63.3255 | 2026-08-24 05:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 5f978733-5284-3fe1-998c-b88790d25302 | -14.3171 | -51.7688 | 2026-08-24 05:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |


[Clique aqui para ver as próximas entradas](README46.md)
