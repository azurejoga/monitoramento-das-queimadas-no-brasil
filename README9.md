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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ced5724-81b9-3dd0-87f0-c0bac6c7f135 | -5.64571 | -47.85783 | 2025-11-26 03:57:00 | NPP-375D | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 654841d1-4467-3928-9b3b-7eb512782638 | -2.73527 | -49.46658 | 2025-11-26 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84b03c40-b627-365b-ae13-11afc3d37793 | -3.13921 | -49.4058 | 2025-11-26 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b43834c-e4b2-38d1-8bc6-1adecfcc8aae | -3.49214 | -44.51476 | 2025-11-26 03:57:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 55d766ee-ca14-38cf-8a77-bbeac42bd8b3 | -4.72457 | -46.46109 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0cef784b-8e67-3f08-a5ff-c4e25acef26b | -4.00971 | -46.50121 | 2025-11-26 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bd4239d7-90e0-3905-9386-6d7cd5d8aac0 | -3.47669 | -43.43164 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 057b5f47-0d2d-330c-a2a9-38f3cdbfb95e | -5.71519 | -39.4977 | 2025-11-26 03:57:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3de5c47-ac6b-3460-ae66-8068f7653f53 | -5.04141 | -40.22788 | 2025-11-26 03:57:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f0054e52-3487-3638-b0b7-9821be5b5617 | -4.16191 | -43.72916 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 99d438b4-de4f-37cd-b3c0-3a0cb4d4610c | -4.2621 | -45.12493 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fbb1e74-38c9-3412-a62b-73407532a1e7 | -2.55169 | -45.39469 | 2025-11-26 03:57:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| de2e77e2-9a9b-3461-b439-bf7a55002823 | -2.55258 | -45.38917 | 2025-11-26 03:57:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b3c22dfe-ad0c-3130-87d9-084782ce9a7c | -3.91825 | -49.22004 | 2025-11-26 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 757cc2cc-708e-33f9-b173-e99b728cfe30 | -3.45138 | -50.55795 | 2025-11-26 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b5231b2-fad3-342f-ab84-54ceea06a738 | -3.6756 | -44.16933 | 2025-11-26 03:57:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46cbda99-252e-3dd1-ba3a-5c3fefb16ac6 | -3.13285 | -49.40479 | 2025-11-26 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b458532-a64e-3fc3-bd98-74edfac6f824 | -6.68995 | -39.79939 | 2025-11-26 03:57:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 735e8a14-ce77-3e0b-9840-c5218b9fec02 | -4.5963 | -44.41413 | 2025-11-26 03:57:00 | NPP-375D | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b4c1ff29-2ed2-3f21-8c1f-dc75037b6f6d | -3.60309 | -38.77864 | 2025-11-26 03:57:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c498c8b6-a6d1-3095-8588-5f8ecfbfc44e | -5.111 | -44.2682 | 2025-11-26 03:57:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81497fde-19eb-3dcf-bd0c-554296feec01 | -2.49365 | -47.82618 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 60691cab-c50c-38cf-98d0-0777b380ee55 | -3.95836 | -49.03446 | 2025-11-26 03:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 924ae4a8-4974-3605-89b5-d87480078112 | -6.55981 | -39.02066 | 2025-11-26 03:57:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb588210-e650-3936-bf51-940efe3c4e1a | -3.39678 | -49.5251 | 2025-11-26 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0454cd52-ea16-32b9-a425-4ac19c0370d0 | -4.71164 | -43.99752 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74f86b5b-aeee-3629-a113-98c78b6c2e1c | -6.81364 | -38.57257 | 2025-11-26 03:57:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f307dc07-f93e-346f-8624-c45d15c5c438 | -4.28977 | -47.30782 | 2025-11-26 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2e4adba-c9b1-313a-8faa-4a1d01fdc5f5 | -6.88039 | -47.24192 | 2025-11-26 03:57:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d953fc7-4848-3669-8d40-9907d118337f | -3.39009 | -47.19252 | 2025-11-26 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f0d4f7d-8643-3264-b5a1-4b35fcd23715 | -6.30447 | -43.78481 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0191256b-6279-390e-88ec-c5f8e6f66830 | -3.42993 | -50.18367 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a4e5b1a-f096-3ed3-b298-4b903897b2e6 | -4.16818 | -43.71778 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| a78caf70-b865-33e0-9d5d-f3d37b3d9cd1 | -4.15504 | -45.1515 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5afd0967-c6cf-3815-914f-0cfb8e7b6702 | -4.74719 | -46.55809 | 2025-11-26 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc457ff3-bdd3-306b-9ad5-a6348f8b9557 | -5.25306 | -44.14529 | 2025-11-26 03:57:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5cb9335-ce5d-3a59-b05c-9ba5549967af | -5.42516 | -43.05317 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 963b7cc7-324c-3ddb-8258-85cb86e21bb0 | -3.8487 | -41.70868 | 2025-11-26 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8ab8cc4a-01e7-3d90-a521-510aa8cb973d | -4.17181 | -43.72242 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3989f7e2-2611-3367-818c-f42f918dd0f9 | -6.06128 | -43.25274 | 2025-11-26 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97a80c8c-715f-3530-8953-79d4c6a79cd8 | -3.45354 | -50.54547 | 2025-11-26 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40095f05-d9c4-3f67-b4cb-1d94bf4c173b | -5.28611 | -43.64366 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10a522b3-6b28-3086-8dd5-f5db9a283ff6 | -3.9835 | -49.28569 | 2025-11-26 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1afa7ba6-5dcc-307a-a283-28f79cfb8a82 | -4.45409 | -44.3005 | 2025-11-26 03:57:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 86acc024-cda9-3f45-adbe-fcd7b060265c | -2.48716 | -47.8293 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 183b40bd-88c5-3988-b80e-f2911ff2974e | -6.4821 | -40.80483 | 2025-11-26 03:57:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fd224960-ba9e-361d-9e1f-fb33502185d1 | -8.07998 | -41.08192 | 2025-11-26 03:57:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c12b822-f988-33bc-ab96-aef5b8d5201b | -4.16534 | -41.61472 | 2025-11-26 03:57:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d3926948-2851-3fcb-96f9-dd1c491e327d | -6.30251 | -43.79639 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 98805f41-0996-3b70-80a2-95440bc7c9a2 | -6.54481 | -44.45943 | 2025-11-26 03:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4769f915-0cd3-3926-9487-e4dae5af61e2 | -3.28247 | -46.02754 | 2025-11-26 03:57:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf4f260e-2e1a-34e9-8924-b297d4c73a47 | -5.55167 | -38.14538 | 2025-11-26 03:57:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f983b44e-0cd7-3ca8-844f-0d0df8642e9e | -2.41991 | -48.59821 | 2025-11-26 03:57:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dc395f82-ceaa-3da7-9576-157f631d1d4e | -3.18077 | -48.62479 | 2025-11-26 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cf34798-3ba1-3415-a3a1-58bc4dde05ad | -4.0149 | -46.50207 | 2025-11-26 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 945427d1-54d6-3680-a460-c0d3e00e00a6 | -4.16124 | -43.73317 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 90f4cdce-0b1e-38d5-95d5-2ee3b5d5a28a | -3.58187 | -42.36925 | 2025-11-26 03:57:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 18942eb2-b8f5-36e7-a636-5d7287c48a36 | -3.46153 | -50.54697 | 2025-11-26 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa8e5d90-e8f9-3ed4-92ed-8654b85bbc72 | -4.93929 | -41.1503 | 2025-11-26 03:57:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0979634d-345a-32e1-943e-72501f75f0c6 | -4.14892 | -43.64913 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d88e5fe4-6f93-38aa-ae45-e5ec04c65327 | -3.49291 | -44.51013 | 2025-11-26 03:57:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0376d2d8-ba43-3d3a-bd86-8c13de064470 | -4.45703 | -44.3036 | 2025-11-26 03:57:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4349c0e9-9e1c-3189-923f-2828a7579c45 | -6.35496 | -41.40171 | 2025-11-26 03:57:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e2373b76-3d1a-32a7-aa6e-f35d21585501 | -4.44637 | -48.75906 | 2025-11-26 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c603a14a-8fe0-34fd-9a40-177af54eb78a | -6.51097 | -38.81958 | 2025-11-26 03:57:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 51d44231-908a-3580-bfdc-8469637c6baa | -5.03297 | -43.26221 | 2025-11-26 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f6955bb-efc8-3aa8-9244-5429359b8f62 | -4.78581 | -48.28692 | 2025-11-26 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c59f425f-7664-3cf7-99c8-9726a7e56163 | -4.72202 | -46.45991 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fcb2313-852e-394f-827b-d2c25786ac09 | -5.42116 | -43.05244 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d130c9d5-56d6-3e77-b7a5-2b8c805ebdcc | -6.40414 | -39.79828 | 2025-11-26 03:57:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c07d3373-7f43-3918-a4a2-2de85f0f8c81 | -6.59504 | -44.31828 | 2025-11-26 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53f1bb34-4b07-37f3-bf85-37c734b146a7 | -4.71233 | -43.99345 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c315f61c-34ab-3d08-8b81-82e004eedbc2 | -4.1331 | -43.27546 | 2025-11-26 03:57:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 265caec6-cb05-3f64-8f75-5584dffde4f7 | -3.92672 | -49.22057 | 2025-11-26 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c5eb0535-4519-3e19-91c2-8f5752e60350 | -5.32893 | -43.56519 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe81da38-9056-3a96-9a9d-45eb12dfe105 | -4.25573 | -45.13411 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85f7d12e-f143-3f8b-8f71-5a3f0d020135 | -4.15896 | -43.72043 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f8484f3-4c17-3131-a8a5-4cc904176623 | -3.39067 | -47.18901 | 2025-11-26 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c383249-5adb-31bb-a97a-e10d382a0eed | -5.23387 | -45.43043 | 2025-11-26 03:57:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3907b2a0-bf89-3880-b36a-dc30bb5cb940 | -5.57323 | -46.28313 | 2025-11-26 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63c619a0-dea9-3fa2-8b6e-71d78facd2dd | -3.64603 | -39.47709 | 2025-11-26 03:57:00 | NPP-375D | URUBURETAMA | CEARÁ | Brasil | 2313807 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5f0515be-f32a-3967-a0a3-a50f4ebafe87 | -6.48992 | -38.82343 | 2025-11-26 03:57:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 69ffb3f2-58c1-37ff-b9ba-74e17dd49e15 | -7.01121 | -45.17029 | 2025-11-26 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89477994-0652-3727-8d0c-a8677f2cd865 | -4.10371 | -49.06345 | 2025-11-26 03:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ede5310-56a3-3b25-b1a2-c83136d13caf | -6.7412 | -39.0493 | 2025-11-26 03:57:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 11dcbb45-55dd-312a-ba27-33e57e0706b4 | -3.66989 | -43.57079 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5461813-a329-36e3-adfe-53d2acdca093 | -4.2892 | -47.31111 | 2025-11-26 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abf60c9a-23f8-3e6a-8a77-9831e6e3c96b | -3.32919 | -49.7224 | 2025-11-26 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 947d0bf2-81e6-3e1e-9462-2c3fd1aa0a7a | -6.31275 | -43.78633 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd9ebd26-a004-3fd7-a295-76cf79cf239e | -3.13116 | -49.40276 | 2025-11-26 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| abba2689-8ca3-3614-b7a1-574b9e8b2670 | -2.42068 | -48.59359 | 2025-11-26 03:57:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6a124b4-b75a-3ad7-9236-639ae657465f | -3.33025 | -50.268 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 429468a8-cccf-3c89-a2fb-7b12be5ae4e4 | -4.65522 | -43.98001 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0d26be07-66dc-307b-93ff-1311ac34b2bf | -4.8114 | -43.82374 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b887b600-2c44-35fa-b09f-b35a17841ade | -7.26732 | -39.6711 | 2025-11-26 03:57:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f4398f0f-33c7-3212-b5a9-1fee19e7caec | -3.35889 | -49.50595 | 2025-11-26 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1548d592-761b-32fc-92d6-5fae6db1deda | -4.72148 | -46.46299 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d81c28d9-0c5b-3d28-a880-eff7caff31af | -6.87521 | -47.24093 | 2025-11-26 03:57:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad231293-4692-3912-8269-b9f4c2af7a96 | -4.13738 | -42.92023 | 2025-11-26 03:57:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b1cc216-3de9-3328-91eb-2db4ff2458a3 | -4.87173 | -38.67375 | 2025-11-26 03:57:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README10.md)
