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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eee0e528-a962-3f63-b39f-398aabe9053d | -3.81048 | -41.61068 | 2024-10-09 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ea35cb0b-d070-36b7-b9b1-c77d2e14668d | -3.8096 | -41.61584 | 2024-10-09 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d9c6e879-ea36-3197-b3a5-998a0ba4a720 | -3.80506 | -41.60429 | 2024-10-09 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| cb320fc7-db55-31cc-a884-1e2a73e3239a | -3.80417 | -41.60945 | 2024-10-09 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 265d0a3b-f51e-389a-9902-b0a2c58bbab5 | -3.80242 | -41.6197 | 2024-10-09 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 19c703a1-8ae4-38b6-91ed-0db22b4dbde5 | -3.79875 | -41.60303 | 2024-10-09 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3e9e4e86-8ecc-3f09-a274-01334a0bcd8f | -3.79787 | -41.60819 | 2024-10-09 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 0efdfba9-cd71-353e-95d4-01eafcd7b1e7 | -3.79699 | -41.61332 | 2024-10-09 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d39f6ec2-ccab-36d8-9e1c-b4ab012c4f43 | -3.79611 | -41.61845 | 2024-10-09 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 8ceab808-056c-35d2-abf2-edf983a3413b | -3.62047 | -42.76782 | 2024-10-09 03:19:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b71399de-a421-3460-b9b0-02f60aa2e901 | -3.61943 | -42.76521 | 2024-10-09 03:19:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9127245d-dd79-3567-820a-d0513707839d | -3.61478 | -42.76041 | 2024-10-09 03:19:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e9722d8-7dca-30cd-bace-1f290253a363 | -3.61367 | -42.76662 | 2024-10-09 03:19:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 389d40b9-8a7c-32dd-847f-c67a77b2bb7f | -3.61263 | -42.76398 | 2024-10-09 03:19:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d15fdf1f-af73-328c-b1dc-27601ea52f57 | -12.73229 | -38.61116 | 2024-10-09 03:21:00 | NOAA-20 | MADRE DE DEUS | BAHIA | Brasil | 2919926 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 51c3419d-9036-3080-982a-4b783cd3afdb | -11.14058 | -45.38433 | 2024-10-09 03:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0673db2-a0ca-3ea3-97b9-5cd108ea9f12 | -11.13357 | -45.38286 | 2024-10-09 03:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0941e448-820d-3f07-ac4b-3799157bacfd | -11.12383 | -44.95367 | 2024-10-09 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71fcef4f-0d2d-3586-bbe0-e8f95ed0bc73 | -11.12375 | -44.95532 | 2024-10-09 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7585ae20-62a5-3530-9f52-08f3002c8a81 | -11.12258 | -44.95979 | 2024-10-09 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 535070fc-0198-3133-9300-1ca30688ae38 | -10.80392 | -45.15318 | 2024-10-09 03:21:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28c1dc8c-0b68-3e86-acf9-307ab9bfb23b | -10.79691 | -45.15196 | 2024-10-09 03:21:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0edc7a2-1c3b-395d-b19a-fd65eb8f33fd | -6.15838 | -44.00986 | 2024-10-09 03:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc9ab545-29bd-3aca-8983-4c21df394553 | -6.15712 | -44.01668 | 2024-10-09 03:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8122f13-4724-32e1-bd4e-44cba7126013 | -6.15568 | -44.01124 | 2024-10-09 03:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 727c26dd-91ac-349b-8bf1-cb40663be564 | -5.81442 | -44.12329 | 2024-10-09 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d2c9b3d7-cd63-320a-80e1-e2e0c3ce51f4 | -5.81312 | -44.13013 | 2024-10-09 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a5c93dcc-4a96-3379-abba-b8e575856775 | -5.81037 | -44.12704 | 2024-10-09 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 012e9e98-10a2-3168-9dbc-eef0b3040278 | -5.80905 | -44.13424 | 2024-10-09 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| be832a4c-d753-34c5-952d-2f95acb0b35d | -9.6328 | -40.6181 | 2024-10-09 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b0c5e1e9-6a46-3a4e-a7ae-1a4127f357e2 | -9.63214 | -40.62164 | 2024-10-09 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3318b745-ca79-3ecb-a8e5-6563f70ae6db | -9.57481 | -40.35004 | 2024-10-09 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c787175d-ed69-3dfb-82bb-e8805b92cabb | -9.57418 | -40.3534 | 2024-10-09 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c3a922dc-a726-36e0-9335-d8828256bef3 | -9.36559 | -38.04255 | 2024-10-09 03:21:00 | NOAA-20 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 83073fb7-f7e8-3170-8a12-adbf70912974 | -9.36475 | -38.04729 | 2024-10-09 03:21:00 | NOAA-20 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dfca05a7-111d-3e4a-8517-9c49e8963a1f | -9.16615 | -40.10942 | 2024-10-09 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f2baec17-bb5f-316c-b24f-5ab7eed2ab4d | -9.16556 | -40.11275 | 2024-10-09 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 15c24c42-0ce8-3ecd-a573-3ff47441af28 | -8.5792 | -36.98563 | 2024-10-09 03:21:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 177f8d7f-5879-3990-8773-38756112a06f | -8.22769 | -41.562 | 2024-10-09 03:21:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7edbcc8d-2167-3e05-9dc5-8554db996dc2 | -8.12863 | -44.41856 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdf5f044-ac9f-39fc-ad8a-7e0a8d353f88 | -8.1273 | -44.42549 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c02516e-1548-3f30-b697-50fade51c8d1 | -8.12683 | -44.41777 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d265984e-b06f-3cfd-8777-e17b21c5ac93 | -8.12592 | -44.43277 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f953ae08-db69-3f2d-bd25-ddb13339ae00 | -8.12546 | -44.42471 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc5e9edf-8501-3b46-9bb6-a4e76422e25e | -8.12403 | -44.43195 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21d4952f-aa5b-3ead-b242-da42a48465fd | -8.12029 | -44.4243 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29b6d37b-0d36-3ee8-85d8-b96818c0f94d | -8.11889 | -44.43164 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b91ad70-0181-38b8-8cec-c6fdd2a52798 | -8.11701 | -44.4308 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f911d5e-1e6b-3682-b432-842dd46b7954 | -8.10432 | -41.09045 | 2024-10-09 03:21:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7fef8f5c-6305-35f7-9b15-e5ee5b1750bb | -8.09935 | -41.08529 | 2024-10-09 03:21:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0e604126-7333-3ca2-9172-c0dfc4757fbe | -8.09862 | -41.08929 | 2024-10-09 03:21:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 87b232d6-2e00-3bc1-b478-46f28bbb21ab | -8.09292 | -41.08815 | 2024-10-09 03:21:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 81c350d9-f770-39d5-9b18-e5bbe176e3db | -8.00236 | -44.36895 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0cf9d5c8-e9b6-37bb-a3e9-3d96e631c0ec | -8.00105 | -44.37574 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 832558fc-76e8-3dbb-be36-a964076f896b | -7.99975 | -44.38251 | 2024-10-09 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4869ed2c-4565-301c-91e0-faa79e8aedf4 | -7.92981 | -42.45577 | 2024-10-09 03:21:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dd4d63b7-7844-3518-992f-d3af1c73cd6e | -7.92352 | -42.45486 | 2024-10-09 03:21:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2e9dc9c8-8dcb-332f-b68c-a3592dcc7466 | -7.92169 | -42.46463 | 2024-10-09 03:21:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ee4e94a2-f756-3c84-be01-65b37c45ccd0 | -7.76892 | -43.1029 | 2024-10-09 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 80e9bd8b-664e-39c9-8968-925902e1ad29 | -7.76798 | -43.10348 | 2024-10-09 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d762cb3e-3c5c-3a15-934d-58e679e784c0 | -7.7678 | -43.10901 | 2024-10-09 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6fff952e-a250-3d3e-8ad9-5fd592a3570d | -7.76682 | -43.10953 | 2024-10-09 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ffd860f1-7302-3c90-ab9a-c5ec232906ad | -7.76231 | -43.10226 | 2024-10-09 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aef17d86-9594-3268-87fa-6fa863cff839 | -7.73294 | -43.04292 | 2024-10-09 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 243612d9-eea0-3e3e-852e-1cc40bbb5f52 | -7.7319 | -43.04848 | 2024-10-09 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd612b5a-9e2d-35a7-9ae4-4486771a12b0 | -7.72975 | -43.06005 | 2024-10-09 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d1bc3e42-ed62-3165-9761-4fdb1fc51d3e | -7.72541 | -43.04726 | 2024-10-09 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2850d964-45e7-3b24-93fb-d6b467b392f4 | -7.72436 | -43.05288 | 2024-10-09 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f29b88d9-c461-32be-8271-50866af2abf6 | -7.72326 | -43.05878 | 2024-10-09 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| cbcf77dd-0a0d-3c13-aa28-4e7ea77e3939 | -7.69475 | -42.99623 | 2024-10-09 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2edd0365-3de9-3d1e-9fa5-2341c36dc033 | -7.68941 | -42.98904 | 2024-10-09 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1d423008-ce84-36c9-a811-60dd50e459f2 | -7.68831 | -42.99482 | 2024-10-09 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 90503395-501d-3e29-8d13-9a4eecf1dde4 | -7.68293 | -42.98782 | 2024-10-09 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| b394ad0e-cb26-33f1-b9e1-636ae7dffe55 | -7.68288 | -42.98787 | 2024-10-09 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| c0e95306-3640-3ce4-891f-3d0a9de34fb0 | -7.68181 | -42.99373 | 2024-10-09 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5a38c604-caf5-3b6a-a7ad-1890258cfb9c | -7.6818 | -42.99381 | 2024-10-09 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a6e4bde5-7291-31f1-8331-04756be15e3b | -7.66763 | -42.50156 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9de37d5a-55d0-3571-8bf4-e4572feb4de3 | -7.66476 | -42.51676 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0e8e1a21-f8e9-3691-b662-3f54e333e415 | -7.66235 | -42.49506 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9e4d4f65-f207-3c39-a757-a38bd7688c39 | -7.66127 | -42.52001 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 636f28c4-70f6-38c7-b495-9f54712b418f | -7.66032 | -42.52528 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| be842312-9708-3729-9de8-5df9696a4ffa | -7.6599 | -42.42064 | 2024-10-09 03:21:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a314717-9068-31c0-bdcc-28d9d8172aeb | -7.65935 | -42.53057 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dab0247c-6940-3f44-a043-cfcc762359db | -7.6585 | -42.51545 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9709deff-eaa5-3b57-9be0-b5b3ada96aa4 | -7.65752 | -42.52058 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 328304fa-f9d2-316b-af8f-7ee461c6c039 | -7.65653 | -42.52583 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e8300e7f-ae55-37f8-a71a-0b6503f9ba20 | -7.65455 | -42.41454 | 2024-10-09 03:21:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 100c41c6-75f4-3a5c-a853-41af6f05c102 | -7.65452 | -42.53649 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7a78e582-1581-3e97-8c3d-309d56fd523a | -7.62277 | -37.36523 | 2024-10-09 03:21:00 | NOAA-20 | TUPARETAMA | PERNAMBUCO | Brasil | 2615904 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f10d2b33-4675-3cad-8f5d-e427bf7508cb | -7.61331 | -42.42743 | 2024-10-09 03:21:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7a224e02-05c7-3b2b-bdcd-f0a8881b7405 | -7.61239 | -42.43236 | 2024-10-09 03:21:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b9a99a1e-d21a-3145-ac7c-69a0e260cec0 | -7.61145 | -42.43744 | 2024-10-09 03:21:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 91122889-729b-34e3-8463-915af3b7fa56 | -7.60169 | -35.02528 | 2024-10-09 03:21:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 41ab12f6-4c1c-3e66-b113-594bd6e511c2 | -7.3073 | -37.44294 | 2024-10-09 03:21:00 | NOAA-20 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 628998d1-295a-3b92-a92c-0fa59c3496eb | -7.30646 | -37.4478 | 2024-10-09 03:21:00 | NOAA-20 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e0ac1f27-9093-3b1e-968b-314bc72bdc63 | -7.28062 | -35.28564 | 2024-10-09 03:21:00 | NOAA-20 | PILAR | PARAÍBA | Brasil | 2511509 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a79b7653-4077-3dd3-99da-63e46ce5f187 | -7.23741 | -42.29976 | 2024-10-09 03:21:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bc5a7b2a-2113-371c-8b54-654fa911e313 | -7.2337 | -42.30013 | 2024-10-09 03:21:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 059bc349-9a56-393f-8127-aa7be309a62f | -7.23117 | -42.29852 | 2024-10-09 03:21:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 31a089cf-1ff7-3705-8d06-5604ac6e3cd4 | -7.22746 | -42.29887 | 2024-10-09 03:21:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |


[Clique aqui para ver as próximas entradas](README59.md)
