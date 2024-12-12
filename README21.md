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
| 235d6c46-24d1-30dc-9a91-f0ce3794d611 | -2.52406 | -51.79039 | 2024-12-12 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 443dcbe8-941f-3c4c-902a-cb49038709bd | -5.9692 | -44.13184 | 2024-12-12 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5247f4f-df1d-3540-88f9-4ab9144988fc | -3.92237 | -38.65305 | 2024-12-12 04:38:00 | NPP-375D | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b9f463a1-9980-3711-8359-70efffc70daf | -6.05909 | -44.05212 | 2024-12-12 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 82c7009d-a672-33a6-a61f-009361371530 | -3.18662 | -52.44851 | 2024-12-12 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1762d39-d0ea-3b0e-ad49-1e554eb8a40d | -4.37754 | -48.7513 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb05a809-beb4-3b2b-bf27-cfc03caaff39 | -5.59811 | -41.3835 | 2024-12-12 04:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| bc015a2c-dbeb-3ced-b375-3d59ed973fac | -4.35161 | -48.46629 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ef8cc9b8-7633-32e3-a4f7-7450dc1efb8f | -3.82874 | -41.57275 | 2024-12-12 04:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 642f967f-1173-3042-b55f-d4142588779f | -7.42915 | -44.73273 | 2024-12-12 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce677fbd-fb49-3ee8-8ed8-bdbcb57980ba | -3.41525 | -44.45903 | 2024-12-12 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 290941b5-7ea5-32d3-a165-bff2b14ca73a | -3.96728 | -48.00273 | 2024-12-12 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3597e2e5-6aef-3b3c-a4bb-89069c8ad453 | -6.92629 | -43.51699 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 6302bb45-3798-3576-8877-924658f7680b | -4.07784 | -46.72291 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e2db4c0-a7c6-3af2-bad9-bf87624936d7 | -6.12075 | -42.53173 | 2024-12-12 04:38:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f669f566-40cf-3ae9-a776-a0cfd9b5041e | -5.35552 | -44.19731 | 2024-12-12 04:38:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43afc73f-d63b-3bc3-be26-663b11f83767 | -6.12925 | -42.53782 | 2024-12-12 04:38:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 85b2ceb9-7fd5-326d-b059-81986357f15e | -4.03846 | -46.7478 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea35e0a7-1360-3e9b-899d-cf26c54baf4b | -4.51308 | -43.61847 | 2024-12-12 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8e2422b-ea03-3b57-a13a-8fb9f990f072 | -2.27589 | -53.48486 | 2024-12-12 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a87cbd1b-6d86-3f10-9ed5-5bad756d00dd | -4.00011 | -46.89376 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9727c7b1-6f04-3482-8972-3618a42cf16e | -2.70896 | -47.55616 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d472d67-de79-34a7-94ee-e05a6903de6b | -2.58442 | -51.92342 | 2024-12-12 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94854eeb-bc4a-3b8c-8d33-7347cc92a909 | -4.09143 | -46.61135 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9a47672-8456-3a25-a208-c034e45c8013 | -2.07821 | -52.28285 | 2024-12-12 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb80f366-c15d-3c7a-9e57-1cd42035d1b6 | -3.24121 | -46.87962 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0a45b67c-57db-3ff3-864f-61ac8f09c730 | -5.59277 | -39.44703 | 2024-12-12 04:38:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| af01e9cf-4d99-37b7-a962-0e2f2cb0db99 | -4.41762 | -47.99979 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b1506f6-5ba9-398b-9d7a-df8a2ba02b49 | -4.03264 | -46.80917 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6481cb75-b78c-3ad5-900d-363d9a4a616e | -2.62485 | -51.95177 | 2024-12-12 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e07a9ae1-a693-3c38-977a-d1634ee1d9fe | -4.19032 | -42.42978 | 2024-12-12 04:38:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9fb5b4e-109b-33d3-bbe4-f963ec9e2fb5 | -1.63715 | -55.10638 | 2024-12-12 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f483959e-6446-3961-8720-555d999568d8 | -5.92406 | -48.05256 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae6e56de-17f2-30c0-9d40-b000305d201d | -2.96347 | -53.72727 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1e6494e-7e0e-3734-8c17-8ed723c727cd | -3.85484 | -40.44737 | 2024-12-12 04:38:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a6041b2f-0c64-31af-b586-7ead7d242610 | -7.30288 | -44.52082 | 2024-12-12 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7561448a-6819-342c-b8c9-132860581504 | -4.87347 | -48.52304 | 2024-12-12 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15ad6411-14fd-337a-b0f2-9e63aa6768a9 | -6.92928 | -43.49609 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0f90e01d-1bd6-335c-8d6f-e6873064ec71 | -4.51616 | -43.62005 | 2024-12-12 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0e8a8e8-89df-3633-9aab-d408f98a90ab | -2.30873 | -46.99355 | 2024-12-12 04:38:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a3975ce-c785-38b2-bd4f-d8745e809ff2 | -6.9338 | -43.52647 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 7b95d044-8ef3-3022-bce7-cd48a5d148a3 | -3.56363 | -43.49331 | 2024-12-12 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae8e063a-da23-3b27-aca7-84d6d7ab91cf | -4.60395 | -48.4989 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecd95c1b-cfdd-32e0-aa5c-8ad305aed9a6 | -4.37699 | -48.75477 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2badc35c-5977-30dc-9210-cd3b13dcd8ff | -3.24405 | -46.88388 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0eac5864-8b8b-35bf-ba13-403264dcb35c | -4.54642 | -43.56564 | 2024-12-12 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30304c99-3c8f-3ef2-9b3d-9b493f852d75 | -2.95942 | -53.72662 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29c101d5-4ee7-36a7-a2c0-09dbb6df6c5f | -4.03319 | -46.89798 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ebe7cb4-b628-3136-9c26-4d7c12ed3744 | -4.13012 | -46.70725 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d02ddc2-b7b9-3284-8083-213e434d7334 | -5.38897 | -40.66193 | 2024-12-12 04:38:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 57ab7218-2eb0-3dcc-8f70-f04d3474a608 | -4.04773 | -46.66364 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| add55d16-c2de-3b54-9ab5-1ecf7ddabebc | -4.80207 | -50.82465 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0f21fab-c8ec-31ce-81bd-7efd38c31514 | -4.79924 | -50.82043 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 795f421c-7f17-3429-a916-d156e9497c25 | -4.25543 | -47.58482 | 2024-12-12 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 296e720b-ad33-3006-8cc9-02818984775e | -2.95913 | -41.82357 | 2024-12-12 04:38:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b9b649e-4520-3529-969f-f2c211e0dc5a | -4.08956 | -46.6699 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be89cb5b-4fb9-3cba-8bca-024d82ff5126 | -5.22593 | -43.87854 | 2024-12-12 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6fe92c5-0a52-3493-a64a-f7a0c91ed3c8 | -3.98286 | -46.89112 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b22f0876-8382-361b-b3ef-7c26f26219b6 | -4.00287 | -46.55547 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 592a1cce-915d-3545-819d-ad39e3e055d2 | -5.92013 | -48.05564 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 024f9699-ca55-3aad-b7dd-72cd8d6c0ec8 | -6.93635 | -43.53956 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2e64a4f-7a9b-3c67-a958-33f97af7d880 | -5.92462 | -48.04893 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89aaced7-b133-3ab5-b34e-5fb35143a7aa | -7.80062 | -46.20354 | 2024-12-12 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 583cb836-2c9f-398e-a4d6-18d41c36d7c3 | -4.83128 | -44.21298 | 2024-12-12 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1e166bf-7d8a-3343-93c2-5d466e4ea072 | -6.04298 | -42.15884 | 2024-12-12 04:38:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b042f598-ea07-3629-aea3-e9a9f6e8d87e | -3.71157 | -53.7529 | 2024-12-12 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1165f2ba-2cb7-37d4-9d5d-a821db0fca48 | -3.97941 | -46.89058 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84ee61a7-d588-3d48-8dec-02706ed2fc5e | -1.86862 | -47.08482 | 2024-12-12 04:38:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a13c6ce2-5517-3b98-84d7-e4d02fe03d62 | -4.20671 | -50.66068 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 660003f9-6f6d-30b6-b58e-67ea0dad1a0f | -3.70757 | -53.75222 | 2024-12-12 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f606fd8-3e2d-3420-807c-7859807ee576 | -4.01597 | -47.03284 | 2024-12-12 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c72e88b3-9c66-3774-ac83-1e50ed30cd75 | -6.93124 | -43.51346 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 02d96507-07b4-37a6-a14e-db70adc53100 | -4.02512 | -46.88143 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f6c9819-8908-3208-8944-1f3ac991a8bd | -6.92946 | -43.52587 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| a35cff3f-1516-35d0-b88a-e2f5693bea80 | -4.18714 | -42.42019 | 2024-12-12 04:38:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cc703d72-987d-32d4-872d-8abcefa621fc | -3.99035 | -46.88842 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca1ef7c8-796c-3fd8-b814-b00b9ba771f6 | -4.27802 | -46.89605 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38db2910-b5e1-3409-87c9-16450960ff06 | -5.91958 | -48.05921 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c820efa0-6664-3df1-befa-9fe0819df969 | -5.92688 | -48.05667 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 040946f0-01dc-3d95-8b2b-902d559d2510 | -2.95037 | -51.78461 | 2024-12-12 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bace5dd2-f7a5-3db8-aa51-302f091632a2 | -5.59734 | -41.38893 | 2024-12-12 04:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f47190c2-7010-3cc2-a874-52bb25a9bf42 | -4.16795 | -48.19166 | 2024-12-12 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4e4aa98-6543-3e31-9e66-be2415361736 | -7.29931 | -44.51661 | 2024-12-12 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd30f8f8-ccb2-37ba-9128-1703cca4928d | -4.54876 | -48.00589 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 29cd70ee-8d0f-3e8a-acbf-3393eadf54bf | -5.38853 | -40.66502 | 2024-12-12 04:38:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b34747a4-c616-30c7-9316-6ae55181ff2a | -3.27013 | -49.76573 | 2024-12-12 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84da5ea1-5929-3b65-9fb2-1680ca182deb | -6.93696 | -43.53539 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3dea126e-9734-320f-a7f9-2e7123068892 | -2.27242 | -53.48075 | 2024-12-12 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee6a90f9-2349-39ea-b573-4a3bc7f13e1e | -1.59592 | -46.4843 | 2024-12-12 04:38:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0de76e0a-d96a-3c6a-a21a-0256ec222879 | -4.074 | -54.30329 | 2024-12-12 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a161000-bd13-37b7-8794-1b3eb51d4a4b | -4.90512 | -42.07595 | 2024-12-12 04:38:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c55734c-87f5-32ad-b41e-6a5e186afde1 | -4.237 | -43.84308 | 2024-12-12 04:38:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46a82d94-837f-3ef9-9000-998aa5ccc668 | -3.92177 | -38.65709 | 2024-12-12 04:38:00 | NPP-375D | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51f56162-b4ff-3401-9f5c-0082c33d637c | -3.8544 | -40.45036 | 2024-12-12 04:38:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b02f4b12-d8a5-3e4c-8506-c34ff6d02743 | -2.08211 | -52.28119 | 2024-12-12 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bfacf2b-f46c-398e-be3c-368452335bc8 | -4.4107 | -48.73521 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2450c6f0-51cf-3281-a92a-2ac0068acc00 | -4.03088 | -46.88999 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4a63d8b-ad54-3e37-9125-71fa71ff44d7 | -4.55211 | -48.00642 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f665343-8b80-392b-af8b-85b19ccc20ab | -4.09593 | -46.67485 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e01c177c-0f84-33a9-abf8-5a8fadff0017 | -1.97491 | -48.69281 | 2024-12-12 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README22.md)
