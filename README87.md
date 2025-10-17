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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8838bcd-ea62-3ca0-9636-6e595582bb86 | -7.05865 | -45.0527 | 2025-10-17 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1156c2b-0080-38a6-9e59-88159abcf883 | -5.7183 | -44.5118 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6476554c-1aaf-3ea8-b0e3-41fb25b94134 | -7.10724 | -44.74279 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09166840-a210-37c9-a6f2-d0c8433647dc | -3.23547 | -45.96156 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97aa4677-aee1-3982-814c-8c4efa6e028e | -3.24244 | -45.96561 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d43a547-0cf5-36e1-96fe-84018156dcda | -4.18489 | -48.92935 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e7d76b3-bd53-390e-abfd-1b8c556000e5 | -4.10784 | -48.0234 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ed1b129-fdfd-3119-8830-7391503035ee | -7.98174 | -44.16192 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a2b35b28-6cde-3077-8756-a7e15e4ef5e3 | -2.78986 | -49.5956 | 2025-10-17 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f23ea36e-acd5-3865-a039-9ce862cdb14e | -3.3718 | -52.80008 | 2025-10-17 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00508a46-9055-342d-ad49-799e0eb90f6a | -6.31591 | -45.52992 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 416b132d-0a29-3dd4-8c14-70b812b1e311 | -7.5714 | -43.82645 | 2025-10-17 04:49:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c16cc0a-925c-3949-825c-bad3c5c95c37 | -2.87742 | -50.73686 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44193c46-f8d2-3cdf-b013-2b00b184944d | -6.20758 | -41.76014 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 23602a43-9dad-3600-859d-c20495489f81 | -4.82291 | -47.08507 | 2025-10-17 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5af0ba51-8343-3d0c-bea9-ceeea250a3a1 | -3.23474 | -45.96646 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ad67ac7-343b-33b6-ad53-83de933c03e7 | -5.97874 | -45.50865 | 2025-10-17 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f284fb73-414a-31af-a382-ca9bb041d34c | -7.40021 | -44.74829 | 2025-10-17 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3064f88c-9db5-382e-b6c5-be2eb8ae48df | -5.59628 | -50.05727 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc1d8224-70a2-31ec-ab4f-9316b2314403 | -2.13094 | -48.00695 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 041faf9c-0481-3bc3-8851-04eadf7380e4 | -7.67881 | -44.621 | 2025-10-17 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9220c82a-11ac-3256-a80a-3668c5509fc5 | -7.61913 | -47.83353 | 2025-10-17 04:49:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 597cd7d0-746e-3172-a3b7-2af3ec445fb9 | -2.44485 | -52.25301 | 2025-10-17 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3451f307-0354-3404-8f7e-997fd05ffdc6 | -3.52826 | -50.30439 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b62db074-639a-322d-bcfb-c6229bd4ad80 | -5.88963 | -44.75269 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba9f9739-6446-3294-8e0e-0de61f8325ef | -8.29743 | -43.39869 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4cceaf46-190b-36e0-8364-18aa6742593d | -7.17617 | -42.36926 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 40887923-a14d-3459-a82d-aa361412951e | -7.76019 | -42.45803 | 2025-10-17 04:49:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f9df576-54a7-35e0-ae53-b1030a77699e | -4.53764 | -48.41001 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a81dea85-9761-3c84-8452-9842cf7979ce | -5.89959 | -44.74578 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ab1c5a6-219a-3a49-a55b-67b40d52b8b4 | -6.95724 | -47.71567 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b03cd472-32a0-3f1f-903c-1438af44f496 | -5.24263 | -50.94991 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cad69ca8-b140-3666-bda9-73675369b8e2 | -5.96977 | -44.03034 | 2025-10-17 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56d1fdd2-6074-3996-bcaf-0f2d1fccd48e | -3.10671 | -47.51376 | 2025-10-17 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a1b4ebc-979a-3866-99a0-2aa348d58a47 | -7.47671 | -46.90328 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4fd78d8-fd8d-374a-a0e1-797eadbf1dce | -4.42249 | -40.17243 | 2025-10-17 04:49:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 39f63008-5a42-317c-8b9b-3d322d43f8a6 | -4.89429 | -47.64166 | 2025-10-17 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bac8038e-d9e5-30c8-b94d-7f1c80bb7d51 | -3.28698 | -52.59061 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd625002-36ba-31ef-8e33-e7520555230b | -3.97287 | -42.49331 | 2025-10-17 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3eb2cc5e-5ba9-3d17-a277-1c0ba8e79967 | -3.27824 | -50.04229 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5143941c-4ce7-396b-86af-ebd6ccb16c27 | -6.39833 | -41.48322 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 15dd062f-4db4-3c2f-9e8c-77e9d19886be | -5.35716 | -44.817 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cd7a1c7-3408-3397-86da-ec8220977358 | -5.88364 | -43.88378 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dcfcbc2-662c-351d-979a-2eb6906607eb | -7.75455 | -42.49943 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9857aea3-0d0d-32c3-bea1-c465fc407cc2 | -3.12919 | -50.21323 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a78ee51d-c84d-3b53-a08a-3cc8b051adb7 | -4.4246 | -43.4038 | 2025-10-17 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 5946c120-11f9-37cd-951d-2b43f3398c52 | -10.2939 | -44.0221 | 2025-10-17 04:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| bed94ccf-5200-36e6-b422-2a5f1141adcd | -12.4073 | -51.3049 | 2025-10-17 04:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 20a9058d-6d5f-3fac-97d3-db161773f85f | -10.5132 | -43.4289 | 2025-10-17 04:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ec6e2a56-db64-3238-8bd6-c303bb0e55d6 | -9.1378 | -46.6261 | 2025-10-17 04:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 22743a30-d675-3678-b939-af34c58ae33f | -12.4264 | -51.3027 | 2025-10-17 04:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 01653411-7f11-3956-91f4-5731e1349b1f | -10.5136 | -43.4052 | 2025-10-17 04:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 030d2f6d-74a2-3d08-be3b-f1bfc0dc31fb | -10.2935 | -44.0455 | 2025-10-17 04:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 0ee33804-2eab-3c4e-9497-2ec439487a5b | -10.4941 | -43.4315 | 2025-10-17 04:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 62f03224-1c78-3005-9b09-03c35ec3d825 | 1.8218 | -55.7037 | 2025-10-17 04:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 1bb24738-86ee-3ea2-96f9-f97c54fff46c | -10.534 | -49.5471 | 2025-10-17 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 90c6209f-0bc7-3f17-814a-7f0bf47b02f5 | -10.4945 | -43.4079 | 2025-10-17 04:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 60504fcd-b00f-304a-a446-ec024cff9721 | -4.4059 | -43.4049 | 2025-10-17 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 9b02350b-d433-3097-9de6-ced22c8e46c5 | -3.5028 | -52.4938 | 2025-10-17 04:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| ca776f9f-88bf-3fdf-b02d-cdfddf0bcad4 | -10.2748 | -44.0247 | 2025-10-17 04:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a94e8282-2f9d-32c2-b751-788574ec72eb | -4.4061 | -43.3816 | 2025-10-17 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| fcca1c6e-1072-3e89-aa86-b906b8676a19 | -11.35633 | -45.26389 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8ba8952-947a-3a3a-855e-b729419eeba0 | -9.13123 | -46.62809 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6017186c-32e1-3f83-aa73-7194ba8bfce7 | -11.45783 | -44.23706 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70c847af-195d-3ff9-bf3a-3f183add7808 | -11.4612 | -44.05188 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0dbf7d3e-6781-35ae-bc66-b1c323a3926c | -8.62333 | -54.56296 | 2025-10-17 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 098a6cd0-3575-30f0-9c7b-ca34c316fe70 | -8.08575 | -45.43923 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0f7955ea-d113-3490-bde7-c8fb01cae47e | -12.5049 | -54.38573 | 2025-10-17 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae7d9437-c6de-3891-b73d-5b83ba9167a0 | -11.40515 | -44.20632 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 057bdf47-c095-373f-8d12-42059266f500 | -11.40664 | -44.19507 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b92af44f-ee76-31b8-bd47-4ac195d04a1d | -10.64103 | -45.21898 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27dacd53-1aef-36ef-a06c-d082401233aa | -8.25852 | -44.06258 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7664c9c6-e05c-3db0-8826-f369f14130dd | -14.34087 | -51.46439 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a4bcdfe4-f4ab-3f74-81a7-28eac2d07bd1 | -12.41579 | -51.30795 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 1c32cc44-0a70-3418-bec6-df58a477542e | -12.15359 | -49.68108 | 2025-10-17 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cacb258-2b7f-3aea-a766-d0834b25c1c1 | -13.38781 | -47.21375 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b48e039-f042-3af8-be3f-681115490593 | -8.62093 | -50.44983 | 2025-10-17 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 928e9909-dc2b-36fe-8823-65b8bcdcd4ae | -8.62265 | -54.56706 | 2025-10-17 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b5f193f-7a42-347b-9f56-4fcaa3966b84 | -10.28407 | -44.04831 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa5aac76-d51e-349a-bafe-8ef2a28ffc82 | -9.15649 | -41.05509 | 2025-10-17 04:51:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 202e4944-65b0-3d12-9047-bca18d1bf550 | -9.05518 | -46.98452 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f8ae809-09c1-3b45-994b-b1e37c70444b | -9.24281 | -44.35994 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d878fd0c-64ee-3bbb-b366-f7612be681b3 | -8.10925 | -55.09116 | 2025-10-17 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7fda324-c6f1-3549-a2f7-96b303a99ca1 | -10.49555 | -43.39908 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1adcec2d-ce3b-3011-b3c7-b225822f0367 | -12.44049 | -51.30445 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 357c9823-79f6-3ecc-a6e1-cd2a1524b323 | -10.46617 | -45.06741 | 2025-10-17 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad9df7d8-984c-3222-ba00-ff29cc311e53 | -13.337 | -47.2759 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b198e10e-6ac0-3b2a-a367-14fe6570586d | -9.14861 | -46.73544 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0db85d0d-7490-38c5-bf5b-228b37e15ae1 | -9.14082 | -46.64766 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a73ffb38-941e-335b-8375-2c9d35f69aaf | -11.18715 | -51.75407 | 2025-10-17 04:51:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1632c332-a60f-3841-b491-a9e05dd40209 | -10.92522 | -45.42133 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40b01896-7ab3-34a6-a84e-4b8800a6242b | -11.19382 | -51.75514 | 2025-10-17 04:51:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec07d1cb-c25b-37c8-a950-caa8525e2339 | -9.14948 | -41.06274 | 2025-10-17 04:51:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ae960b2-9309-33e5-a9cd-ceba34c13ed2 | -11.46205 | -44.24332 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e4bb617-2503-34e8-92ea-05fb11b85da8 | -14.92465 | -46.72667 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8653e6ee-bbac-3ee2-a970-45fc90fc497c | -10.52893 | -49.5504 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7481e948-7562-3898-9d23-816d5bd2b631 | -10.9197 | -47.87048 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0563d27f-a955-309a-b4a7-e422e877dd48 | -10.99678 | -44.50119 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95375b41-f728-342d-9507-7e6226ddc1cb | -8.63049 | -45.68916 | 2025-10-17 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6808ea64-283a-395e-a3a7-2832b222bf96 | -10.23306 | -49.86785 | 2025-10-17 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README88.md)
