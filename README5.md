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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb0e4b55-cd40-33ca-a5b7-6bf48815ebb6 | -9.4325 | -50.1299 | 2026-09-14 01:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 4312ea78-a0a5-3f38-98ea-3120ff995c14 | -6.38 | -35.36 | 2026-09-14 01:15:00 | MSG-03 | VÁRZEA | RIO GRANDE DO NORTE | Brasil | 2414704 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 771e1a67-2dfe-37a0-96e7-0368c843e2a9 | -2.91 | -50.45 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 455cd980-bbaa-3f31-aa29-eb975dadebae | -2.94 | -50.46 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d80ac5ff-d7f7-3370-9339-e8b6eb67051d | -2.91 | -50.4 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e47459f3-2f2b-3c16-b20e-60aaad0a6336 | -2.88 | -50.56 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b30a508e-b0aa-3b66-92f0-50348b544718 | -2.88 | -50.51 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb2bd3c9-f538-3d7b-9445-424996eee825 | -10.66 | -54.12 | 2026-09-14 01:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8afc6493-1895-3b44-bb88-9a08cf6f5de9 | -10.69 | -54.13 | 2026-09-14 01:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c409e219-25de-359b-8fae-b7a2ba7b31b8 | -2.91 | -50.35 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65c4958c-adb5-3f26-a7fc-d699fbb1a7c9 | -2.88 | -50.45 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 989841b5-f9bb-3a45-a81c-08672a9b5a63 | -2.91 | -50.51 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9ae4628-7da4-363d-ae36-c445bc0dff76 | -2.94 | -50.4 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93d464b5-de0d-3d67-bfd5-6aa490475412 | -2.91 | -50.56 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33614f5c-c0fa-3cd9-aa2d-f13116e0c895 | -10.66 | -54.19 | 2026-09-14 01:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1733bbb-0884-306e-9e21-d947975b5fe7 | -2.94 | -50.35 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1220c587-02cf-3432-8068-b8bf7a1d844f | -2.88 | -50.4 | 2026-09-14 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 582c7b86-8729-3000-8cfd-b8f772cba387 | -10.69 | -54.2 | 2026-09-14 01:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62618660-9c2f-3505-a1cb-ad9c9c5247cd | -4.8562 | -48.3667 | 2026-09-14 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ce60b452-5e4f-3261-a015-0e7e4a37aeb6 | -6.5837 | -58.8498 | 2026-09-14 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 1901d5dd-7728-3195-8106-24770770ca2e | -5.1439 | -55.9543 | 2026-09-14 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| e2892c8b-3299-37ee-9430-95dacd8e328a | -6.1111 | -57.6645 | 2026-09-14 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 191efacd-68d3-38d5-82e5-3ba33003df61 | -4.8563 | -48.3451 | 2026-09-14 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 3ebeaed9-2efd-32ff-8134-da86fc7c1959 | -5.1256 | -55.9352 | 2026-09-14 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| fb6a23bd-af84-35a2-934e-3d360b48d8a8 | -5.1255 | -55.955 | 2026-09-14 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 2e662df0-e4e5-3094-82ee-676ef70b3641 | -5.8507 | -52.0878 | 2026-09-14 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 7ef0b784-90e1-391f-bed6-cbf0a86b9514 | -6.2831 | -59.9394 | 2026-09-14 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 03f7e115-71f9-38ec-8498-6e487517aa00 | -3.1816 | -61.1235 | 2026-09-14 01:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 8eb90a03-bb94-3ccf-832f-3f2227402e8c | -6.3197 | -59.9764 | 2026-09-14 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e3b7be07-a941-313c-9145-86631e4e1cec | -9.4513 | -50.1282 | 2026-09-14 01:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 8915b560-e75a-3c58-b518-d7e9464927f2 | -9.4325 | -50.1299 | 2026-09-14 01:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 8fb42d81-57b0-36b6-bfe4-f0af4dc51a74 | -6.1109 | -57.684 | 2026-09-14 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 87461de2-4745-343d-a072-c0e3c7393df1 | -3.728 | -61.7555 | 2026-09-14 01:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 50d90085-7c02-3efd-87fe-b931ea62dd27 | -6.6927 | -59.1352 | 2026-09-14 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 599ee898-5fba-3328-8daa-9b9d157c4422 | -4.1333 | -60.6882 | 2026-09-14 01:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 5bec2ba6-4162-33de-a904-f8373d2309a9 | -4.8563 | -48.3451 | 2026-09-14 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| e6e09fc6-2059-327c-b007-a3286e14c23a | -9.4325 | -50.1299 | 2026-09-14 01:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 144.3 |
| bdba6928-ddc6-3cc0-9396-f61756b56547 | -5.1256 | -55.9352 | 2026-09-14 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d70f95ed-2acb-336c-8dfd-baefa5d1c344 | -5.1255 | -55.955 | 2026-09-14 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 71dc36ce-3306-3ec4-a5d8-f2965fc7003d | -5.1439 | -55.9543 | 2026-09-14 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 199212aa-b4e5-30f9-88c5-ca7c90e24752 | -9.4513 | -50.1282 | 2026-09-14 01:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| fe395d0f-5df6-3aa9-88f7-a7576a13e034 | -6.5837 | -58.8498 | 2026-09-14 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| cef11a9e-2326-3327-860a-abb4c8b40a94 | -6.1111 | -57.6645 | 2026-09-14 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| b99ee0f5-ce2f-3657-8d05-fc43a5e7c233 | -10.0295 | -36.1344 | 2026-09-14 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.2 |
| b4b05237-45d6-32bd-ae66-3da7c0d57140 | -4.1334 | -60.6692 | 2026-09-14 01:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 65abb4df-555a-33b5-b279-7620624165a4 | -6.1109 | -57.684 | 2026-09-14 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 179a9302-c6a8-3317-8830-3b96473e8003 | -3.728 | -61.7555 | 2026-09-14 01:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| a465df2a-a43d-3989-84fd-a7de9cb484d0 | -4.8562 | -48.3667 | 2026-09-14 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 73ac0a79-2d54-339b-b5ea-95e53022512a | -4.115 | -60.6886 | 2026-09-14 01:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 8e70d839-ee4d-3554-9443-3284f361971f | -6.3015 | -59.9387 | 2026-09-14 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| aeaa9392-f9b7-3aea-a8c1-ba26c606e982 | -6.2831 | -59.9394 | 2026-09-14 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 475d653f-6823-3d9f-9040-3fdcb81770e2 | -4.1334 | -60.6692 | 2026-09-14 01:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| fbb0cc58-aded-3f18-8317-c4afb1c763c0 | -9.4325 | -50.1299 | 2026-09-14 01:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 1a38d1c2-75ad-392d-9f30-033d36f44ce5 | -6.1111 | -57.6645 | 2026-09-14 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 9ef624f4-1e8f-3d91-89b6-864c9120935c | -5.1439 | -55.9543 | 2026-09-14 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 65223982-e9f2-3503-be8b-e868be0d6e1a | -6.1109 | -57.684 | 2026-09-14 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| abb05a59-4bca-3d42-9323-c85f81c0d6ad | -4.8563 | -48.3451 | 2026-09-14 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 53712c41-2972-36c8-8cc8-eaec91dd768c | -6.5837 | -58.8498 | 2026-09-14 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 27154cba-d32d-38a5-a9f0-a2d86ab8660b | -9.4513 | -50.1282 | 2026-09-14 01:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 6b4475e6-65bf-3214-8d18-18fa113111c1 | -4.8562 | -48.3667 | 2026-09-14 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| da4cead4-2b46-3be7-abfb-e9b6c96a12a1 | -3.728 | -61.7555 | 2026-09-14 01:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| a52fe132-fb56-353e-9b25-2d48499c80ec | -4.1333 | -60.6882 | 2026-09-14 01:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| e60fdb99-a063-3a6c-badd-467c00cf35d9 | -5.1255 | -55.955 | 2026-09-14 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 00039f5e-90d0-3259-8fad-b96b43ea79d2 | -4.115 | -60.6886 | 2026-09-14 01:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2dab62b8-8a8e-36fb-8fea-043facf709e3 | -10.1086 | -48.857 | 2026-09-14 01:50:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 0593953b-8971-3a46-b95d-537e1292e335 | -5.1255 | -55.955 | 2026-09-14 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 5df40e51-939f-3269-a885-966bc307f546 | -6.1109 | -57.684 | 2026-09-14 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 472bb49c-deaa-35dc-982a-226ddcdff73b | -9.4513 | -50.1282 | 2026-09-14 01:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 46e513ad-27c9-3dfb-b77a-045b628a1ad0 | -11.1699 | -46.3838 | 2026-09-14 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 94c005b8-3a48-3b95-9814-79002c441d99 | -6.1111 | -57.6645 | 2026-09-14 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| bd4e9286-9c1b-3550-8135-df0766c9f9db | -5.1439 | -55.9543 | 2026-09-14 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e068fe5e-59f9-385a-9ca7-be86e78a1fee | -4.8563 | -48.3451 | 2026-09-14 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 1fbf857c-4253-3c83-ad56-fcd690a2f1a7 | -4.8562 | -48.3667 | 2026-09-14 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 185.7 |
| 67a3ee3f-4a13-370a-b9c5-32e58088f4f9 | -9.4325 | -50.1299 | 2026-09-14 01:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| f1d8c5e7-29ba-3ea2-8bfe-5a5db41bbb64 | -5.1256 | -55.9352 | 2026-09-14 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f67bd6da-70f8-3656-8b73-dcaa4ee0da75 | -6.5837 | -58.8498 | 2026-09-14 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 60bd6c6f-67e6-31e2-bc5e-4c64ffdf305f | -10.1086 | -48.857 | 2026-09-14 02:00:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| cd41105b-5cfa-35d5-a6e3-9c0aa6fb3c0c | -9.4325 | -50.1299 | 2026-09-14 02:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| f50bd5a4-9a98-3501-ad10-829ac23a08a4 | -6.5837 | -58.8498 | 2026-09-14 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 2413f527-8acb-3ec8-875c-813d9f3ce62b | -4.8562 | -48.3667 | 2026-09-14 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 294.9 |
| fcbdbcc0-e44b-3a80-9735-dad002772f33 | -4.8563 | -48.3451 | 2026-09-14 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| f7babdb1-0c9e-3b51-97ba-dccc0dbf6670 | -6.1111 | -57.6645 | 2026-09-14 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 7ea238a3-7895-35de-bb57-95d119bdca43 | -5.1439 | -55.9543 | 2026-09-14 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1de0a387-bea8-3e73-94a6-51d48d31a215 | -9.4513 | -50.1282 | 2026-09-14 02:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 55912a6f-578e-3ecc-b1bb-81a995187a94 | -14.1861 | -47.3844 | 2026-09-14 02:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| fdf6a2ce-377a-3074-a35a-3cde7d1af4e7 | -6.1109 | -57.684 | 2026-09-14 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7b782ddc-c9c7-3818-a100-cbaaeea7245c | -5.1255 | -55.955 | 2026-09-14 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| b7ef6d49-87b7-3418-81af-64221e3a2f7b | -6.5837 | -58.8498 | 2026-09-14 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 4c0eaf5a-e364-391c-bb3d-1644bb396dca | -4.8563 | -48.3451 | 2026-09-14 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 8c06fdda-05b2-3ca2-ac3d-3af57584eb6a | -4.8376 | -48.3677 | 2026-09-14 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| fd90f72e-44a0-3f41-818b-f0ddc337c7be | -9.4513 | -50.1282 | 2026-09-14 02:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 432a7518-32c8-347a-9540-0aaa2c7589c9 | -6.1109 | -57.684 | 2026-09-14 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 2cfc77aa-f70e-383d-9fc8-05833a4b1e42 | -5.1255 | -55.955 | 2026-09-14 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 77b37b6b-a03a-36c1-8fce-1e7047372346 | -6.1111 | -57.6645 | 2026-09-14 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| ce46c47a-fba7-34e8-89ac-96d76f7f6f4c | -9.4325 | -50.1299 | 2026-09-14 02:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 6864d6cc-e91c-3621-b098-d770b9532224 | -4.8562 | -48.3667 | 2026-09-14 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 241.8 |
| ab61f620-0c79-3b2b-8f64-c693eb27a3fc | -2.94 | -50.62 | 2026-09-14 02:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2c1d3d7-8bbc-3a34-b37c-0fb882829f93 | -2.91 | -50.62 | 2026-09-14 02:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40c65b7a-2cfc-38b8-84b1-47d17c810e29 | -2.94 | -50.57 | 2026-09-14 02:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e6468e0-5290-3497-945d-346af9de12d2 | -2.88 | -50.73 | 2026-09-14 02:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
