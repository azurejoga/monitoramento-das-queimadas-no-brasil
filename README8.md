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
| d94b4125-83a9-315c-b1de-48e3699f492e | -2.2165 | -45.40963 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41d591dc-f1c5-328c-9210-ee0817781aeb | -2.2865 | -45.60066 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 8c280f8c-f341-3ca6-837e-688d514ce274 | -2.20925 | -45.40847 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6207f69-0157-34a6-8230-5aa02c19ee0c | -1.43312 | -45.66438 | 2025-12-11 04:16:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 616e344b-e2d0-374b-987f-6832e622d2a4 | -2.46541 | -45.32338 | 2025-12-11 04:16:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7e008f52-1401-346a-99a5-324f38b89a9d | -2.02953 | -47.14155 | 2025-12-11 04:16:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d5f8015-20e6-37b4-b856-5a7711ba24fe | -1.69045 | -46.55312 | 2025-12-11 04:16:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93a325e5-1b5a-3503-a8ee-3708fc57e0e6 | -1.10951 | -53.68874 | 2025-12-11 04:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a65ed557-7e91-3668-a812-ba743a1e8704 | -1.93602 | -45.43792 | 2025-12-11 04:16:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a5d5163-8a4e-3396-9e21-f57c06845669 | -2.21647 | -45.66552 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 810e0e0d-05eb-334a-a569-57775915afee | -1.15288 | -48.37876 | 2025-12-11 04:16:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15f740ac-9334-3119-91ca-a7f8295094f8 | -2.08389 | -45.32688 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf3cb33d-2a46-3884-b7ea-afa009520135 | -2.24142 | -46.5135 | 2025-12-11 04:16:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a56ec101-dbb0-3fe1-be52-c6fcc9606725 | -2.29085 | -45.59699 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4bb6d94a-239e-3d3d-b60f-be5e4e9307f6 | -0.98664 | -48.06797 | 2025-12-11 04:16:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0de34cda-230b-3299-84da-36bb0ef8b09b | -2.99572 | -41.78296 | 2025-12-11 04:16:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| babbc73c-ca43-3cf4-9ef3-9863286a34f0 | -2.19634 | -45.44236 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a8e9823-e6b8-32a7-9936-89a94d5821a7 | -1.82659 | -46.52673 | 2025-12-11 04:16:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36900796-33c8-317b-8011-bdd2d9a2719a | -0.92397 | -46.88996 | 2025-12-11 04:16:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 851354a5-9388-3793-a1f6-7d5cda8c672d | -1.68943 | -45.79624 | 2025-12-11 04:16:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 837eb757-4eee-33e9-84a1-74862c2a3745 | -2.21578 | -45.66981 | 2025-12-11 04:16:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4754762-779d-395f-a176-1b327e79a7c5 | 0.22507 | -50.07803 | 2025-12-11 04:16:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb04caa4-3d76-34a2-b9cd-8938a2613f18 | -1.93669 | -45.4337 | 2025-12-11 04:16:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0425cf8e-a654-3179-8f14-1888db5bb45c | -0.92744 | -46.8941 | 2025-12-11 04:16:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfdc9bed-1958-3a0f-a216-532e0e5f5adf | -0.64212 | -52.39293 | 2025-12-11 04:16:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37b2c32e-b0a0-3cb5-ac99-89204cf87c38 | -0.98229 | -48.06726 | 2025-12-11 04:16:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc603187-5534-3bf6-a66b-fb09fe1129cb | -1.19566 | -47.53754 | 2025-12-11 04:16:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2983995d-6c99-390c-b965-88053b29c38c | -2.36255 | -45.66536 | 2025-12-11 04:16:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 155a0583-869d-3b8e-8a0f-4fd4e15f7422 | -2.19588 | -45.44484 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dbb94e1-92ad-3b7d-b724-144864ad6ab5 | -1.91409 | -46.27741 | 2025-12-11 04:16:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 129196ec-9bf9-3205-8c1d-720b7fed6caa | -0.64563 | -52.39545 | 2025-12-11 04:16:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 487787f3-3f6f-37b2-ae88-2d90a237010d | -2.21287 | -45.40905 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fbd2681-e4be-3eed-a963-cd2a69799cc3 | -2.29354 | -45.6499 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52c7003e-1f91-38cf-ae9b-cea11e86091a | -2.1348 | -45.33857 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4df8b920-5e0f-38de-8d5b-6ce099051829 | -1.4257 | -45.6632 | 2025-12-11 04:16:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d683ea1-4a02-32ae-bac3-220169317e66 | -1.20044 | -47.53442 | 2025-12-11 04:16:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6635531-d6c7-3a9c-afa5-c274c5bcf51b | -1.42941 | -45.66379 | 2025-12-11 04:16:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 552e3097-efd0-3949-b5e0-925b8747558f | -1.19626 | -47.53375 | 2025-12-11 04:16:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f08429e6-4873-3654-972e-94f007aa44e8 | -0.92856 | -46.88712 | 2025-12-11 04:16:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52afff54-6882-377e-8186-991f77b0e31f | -2.29016 | -45.60123 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 5dbe832c-5d08-3d02-bf43-47710f3879d1 | -1.52914 | -47.13015 | 2025-12-11 04:16:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df143bfa-34b2-3341-a51f-464b557d481c | -2.17912 | -45.75687 | 2025-12-11 04:16:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c394840-aaef-3d31-bad0-77d509144e31 | -2.03037 | -47.1417 | 2025-12-11 04:16:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0457ba59-da8f-3f36-9d61-cfa81942105b | -2.2122 | -45.41322 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7bb907e-8512-3efc-8b48-3ed3cb682c9d | -2.24008 | -46.51612 | 2025-12-11 04:16:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90a50408-e16d-3f88-8e47-7a6fbd8a5fcb | -1.75234 | -45.60262 | 2025-12-11 04:16:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbaf8322-a1ae-3b8e-bfb1-013dda41e7da | 0.23016 | -50.07714 | 2025-12-11 04:16:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff9045a4-7369-3e51-98ef-7741c5bb6a7b | -2.46901 | -45.32395 | 2025-12-11 04:16:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 98513bd7-71ab-3fab-9549-887f2abfb120 | -1.09428 | -46.62856 | 2025-12-11 04:16:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22424248-06a8-39b8-a9bd-261c144e263c | -2.24064 | -46.51824 | 2025-12-11 04:16:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c8c7692-c44e-3126-83ef-8382afbfd908 | -2.21582 | -45.4138 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c8c07f9-7ad5-399a-93d7-c3676eb8a356 | -4.49927 | -43.42699 | 2025-12-11 04:18:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f97e82f5-a782-322a-938a-b491da14c81c | -4.07009 | -47.95195 | 2025-12-11 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 978456bd-11ca-36e6-959c-91e3b1ef8030 | -3.48318 | -51.53766 | 2025-12-11 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d923f3a1-e13e-302a-b77c-b8fa759912b4 | -6.94245 | -38.61964 | 2025-12-11 04:18:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 34f54364-ed76-3859-ad7e-5f77f19525f7 | -3.17492 | -48.0294 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 651a63ef-666e-3c2b-831a-e64c9a3bdfbb | -5.56289 | -43.80676 | 2025-12-11 04:18:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35138e55-a0b8-3192-8e5d-05340b5a53f4 | -1.30635 | -53.491 | 2025-12-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2429fa3c-1065-3cca-84b1-a1416aeeb348 | -1.80578 | -54.0588 | 2025-12-11 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 908646ca-6df6-3079-a44d-d822af4d1504 | -5.00679 | -41.28868 | 2025-12-11 04:18:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0bd0b45e-3e94-33b3-b23e-4b3c85b7c29a | -2.29563 | -49.31131 | 2025-12-11 04:18:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aac5647-99b4-387c-a95a-05216856d691 | -6.93996 | -38.60889 | 2025-12-11 04:18:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f34f6405-2564-3145-9bbf-ad171ae61f92 | -6.55095 | -46.9593 | 2025-12-11 04:18:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb400484-98fb-3822-b5a6-dead5e63fba7 | -4.95465 | -45.08154 | 2025-12-11 04:18:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7a22bbe-c840-3903-9d3a-0357db6acf66 | -2.21556 | -51.89941 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5233eecd-4f59-3280-9b82-9135c52dd013 | -1.59107 | -53.75882 | 2025-12-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c35d1ced-7e05-3c3f-9afc-bc5cca342586 | -4.49649 | -43.42297 | 2025-12-11 04:18:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35aa7436-ebeb-31de-ba4e-7a63b9be75cd | -6.0326 | -43.70586 | 2025-12-11 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 96ee50bc-51fb-3365-93f4-52e4a661f79a | -6.03205 | -43.70935 | 2025-12-11 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4435aa46-5595-31f0-98d1-1ad8bcd2203a | -3.48905 | -51.53526 | 2025-12-11 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55b344a6-1278-3cab-ad51-917e905e48af | -3.39864 | -42.10518 | 2025-12-11 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| acfa656f-79fe-3f56-90b0-e2cca32c6925 | -6.79392 | -39.42637 | 2025-12-11 04:18:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 28c7a2ad-6279-3c7b-ba22-b82728a5cb05 | -5.68884 | -44.48294 | 2025-12-11 04:18:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19d74d1a-0ffc-3929-bf29-8983fd7ebff8 | -4.06475 | -47.65804 | 2025-12-11 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38af8b43-ee03-3768-b3ab-0e40d85b6ac6 | -2.88313 | -52.71777 | 2025-12-11 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8e5954c-8305-350a-8625-e5018a1953a0 | -4.93537 | -43.96046 | 2025-12-11 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ccacb978-9ece-3a74-9936-d828fe6f59e8 | -3.84202 | -47.82821 | 2025-12-11 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db6ba09f-3ead-3117-a193-f743afdeaf7b | -3.39435 | -45.42329 | 2025-12-11 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bdcd011-83ee-32f3-8c2a-4d72e751d3b0 | -3.82503 | -48.87368 | 2025-12-11 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b426b9c-cd5c-3437-89cf-f4a2a9c22208 | -3.21482 | -42.69161 | 2025-12-11 04:18:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0ca0d41-8717-383a-b168-5bb944af56e4 | -5.00339 | -41.28816 | 2025-12-11 04:18:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 32e6a021-0e42-3c64-a0e4-e2159a8d7a7f | -2.657 | -51.64468 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1314209-23a3-3129-be7e-afb175f6df25 | -3.39395 | -41.17214 | 2025-12-11 04:18:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bbdf0404-592f-3be7-b2d4-61a1db6d6a21 | -4.30775 | -44.1214 | 2025-12-11 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d32926a0-8247-3220-9e1a-297b3a193b22 | -4.68267 | -43.25639 | 2025-12-11 04:18:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd78b07a-b974-3c77-a32c-2b3c8631c2bf | -3.35301 | -46.21303 | 2025-12-11 04:18:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5791b39c-4fcd-3aa5-b899-c93a7239c955 | -3.23131 | -47.46878 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 841056dc-686a-39a3-9648-47f7bb5394d2 | -4.49593 | -43.42646 | 2025-12-11 04:18:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef0a5486-b780-3c62-a240-cc9511b47334 | -4.06876 | -47.65887 | 2025-12-11 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63dc2505-524b-3288-9511-f241f017b2ad | -2.62874 | -45.55997 | 2025-12-11 04:18:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4773fd68-01ba-3fbe-a84d-fff190f4e7be | -2.08792 | -52.11538 | 2025-12-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6364bd8-6a4e-3aa6-b5c2-b69f76eb3950 | -3.087 | -44.89368 | 2025-12-11 04:18:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b8ea162f-293b-3c09-a007-4ee3f7fd0a7d | -4.19829 | -44.47698 | 2025-12-11 04:18:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 215b6c7c-e229-313e-bfed-b18f5eeafb41 | -3.49584 | -44.88848 | 2025-12-11 04:18:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c57112ce-3476-3947-aaa1-399cd9f9b942 | -6.23031 | -44.16212 | 2025-12-11 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2ce8df0-7399-309a-a5aa-0ca57afa94a1 | -2.94335 | -53.02871 | 2025-12-11 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a7a46e9-4277-31b1-b174-6e49083fe7d4 | -2.08689 | -52.05288 | 2025-12-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86359c95-d47d-3151-b6e9-2522ad9b3cb2 | -2.3177 | -46.48171 | 2025-12-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 458c04eb-1d4c-39d7-9f19-e74abb15f646 | -6.93665 | -38.42689 | 2025-12-11 04:18:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 63088ab7-8749-3815-8325-f1f3faff682e | -7.77776 | -37.89179 | 2025-12-11 04:18:00 | NPP-375D | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
