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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c4431c0-f883-38ba-b940-a40cf6f3b875 | -9.5962 | -46.2618 | 2024-10-05 13:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 6a20b7c5-13cd-3f38-8ee2-79f2ae17f59b | -9.5959 | -46.2843 | 2024-10-05 13:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 2a081e02-f946-350f-a624-118f9b2e0ce6 | -9.8858 | -47.1901 | 2024-10-05 13:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| c770f9f3-f477-37a7-8689-5a1f431a662b | -10.2908 | -45.4305 | 2024-10-05 13:26:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| b75cfb68-54f1-3350-a1c5-89518cd74d87 | -10.2476 | -52.7449 | 2024-10-05 13:26:04 | GOES-16 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 47b06cb4-c16b-37af-832e-16ed332d6ba7 | -10.2479 | -52.7242 | 2024-10-05 13:26:04 | GOES-16 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| bdf1b343-e3f6-3aee-b767-a56ffd006ff7 | -10.8288 | -42.8377 | 2024-10-05 13:26:07 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| a905760d-eb10-3086-8a05-8055b4cd3aac | -10.7546 | -46.1667 | 2024-10-05 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 88df7de7-92f0-3a2c-921e-379c2b6456c0 | -10.7542 | -46.1894 | 2024-10-05 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| ad96685d-14ec-3209-935d-588f60420a22 | -10.7834 | -45.5495 | 2024-10-05 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 184e5c24-aeff-3f8f-bb0c-e978571b6179 | -10.9102 | -49.7215 | 2024-10-05 13:26:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| deada343-f5f7-37df-902a-48155e1e0ac5 | -11.1983 | -46.9871 | 2024-10-05 13:26:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 282.6 |
| 66865cfc-98f2-35c9-88e9-02646e53dda3 | -11.1155 | -54.2319 | 2024-10-05 13:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| eacc190c-5ab3-329b-b1ae-6fbb2226ac9f | -11.3662 | -47.2113 | 2024-10-05 13:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 3557d676-fcc5-306c-84e1-59bf4689d17e | -11.3177 | -45.5228 | 2024-10-05 13:26:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 1821b16a-39e3-3e83-98b6-c6658d6792cb | -11.3849 | -47.2312 | 2024-10-05 13:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 6ce9d8cc-1e03-3dab-ad88-2ca97626e8a1 | -11.3368 | -45.5202 | 2024-10-05 13:26:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 145901c8-90e5-324c-bd04-99ae7210da7f | -11.6995 | -47.8131 | 2024-10-05 13:26:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 26689ebd-49cf-397f-be35-99c5e74967d8 | -12.4689 | -47.5312 | 2024-10-05 13:26:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| efd93f33-4502-318d-91e0-b5fff30a0fc0 | -12.6532 | -54.0415 | 2024-10-05 13:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 066f689d-6ee3-3b92-b651-767a0e0b6706 | -12.7815 | -50.5758 | 2024-10-05 13:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 61d4a1d9-c19e-362e-9a52-f22f3313a7a7 | -12.6723 | -54.0395 | 2024-10-05 13:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 24ffa439-c2e7-34d0-8313-ab3233f16fac | -12.7623 | -50.5782 | 2024-10-05 13:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| eba31044-e8d3-36e6-850e-54886e7268ed | -12.8198 | -50.571 | 2024-10-05 13:26:19 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5e0e50dd-00c5-3502-b7a2-947e4b301ea6 | -13.1351 | -51.1955 | 2024-10-05 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 5602359d-2bf6-3164-aa41-40c369159e0f | -13.0598 | -51.1195 | 2024-10-05 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 230872b5-c05e-3627-8ea6-704a3bc04cd9 | -13.0594 | -51.1409 | 2024-10-05 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| a1d315f8-7ef0-3945-bcde-a34970ed2855 | -13.1543 | -51.1931 | 2024-10-05 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 2b784acb-65c7-3256-8b2c-85720fd4a04b | -13.154 | -51.2145 | 2024-10-05 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d1ba27c9-aaff-3111-8262-54f8679e4cb0 | -13.1547 | -51.1717 | 2024-10-05 13:26:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| a1fce4b6-64fb-3989-873d-4135ba1ed9cb | -12.9776 | -51.4706 | 2024-10-05 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 6208cb59-6899-3ebf-bdcb-9864881c689b | -13.1249 | -46.3291 | 2024-10-05 13:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| f3793bfe-200e-3c2f-9962-16ab3874f3b7 | -13.1056 | -46.3321 | 2024-10-05 13:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 147.6 |
| c6629b03-d9ba-3694-88e9-762f52f9044c | -13.1728 | -51.2335 | 2024-10-05 13:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 7f39a0a8-88ad-3205-834a-53ddce2b5113 | -13.192 | -51.2311 | 2024-10-05 13:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 7034a7a1-6229-39fb-a721-36ffec0354ba | -13.6136 | -51.2629 | 2024-10-05 13:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 28424614-65a3-37b3-a4bf-12efe0344149 | -14.0008 | -45.0781 | 2024-10-05 13:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 662cd422-5789-3fc3-8a17-ff780844d144 | -14.0207 | -45.0513 | 2024-10-05 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 55ac7bfb-6b28-3e47-b275-91d2e41f233b | -14.0202 | -45.0747 | 2024-10-05 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| f4eb1e87-dbe1-3800-b904-583fb32a2010 | -14.0504 | -45.4877 | 2024-10-05 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 7e8fc549-91d7-3785-b0de-57399d07f09a | -14.0572 | -45.1614 | 2024-10-05 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 0a713c9b-4585-3c24-a8ce-d96976095ae4 | -14.0577 | -45.138 | 2024-10-05 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 229.0 |
| 4f5fbce1-12bc-3e84-90f9-f24aa449d93f | -14.5646 | -48.8217 | 2024-10-05 13:26:28 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 821d60f0-8706-3c05-aec8-8c17d7b2495f | -14.5456 | -48.8025 | 2024-10-05 13:26:28 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 6a775b9d-6a4d-3fe8-8b10-6c7728726c54 | -14.8167 | -48.8265 | 2024-10-05 13:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0699fc16-ff30-38ac-8715-cb7b2ada3c80 | -14.8172 | -48.8043 | 2024-10-05 13:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 7c9895ff-2088-3d56-8d8a-e99385eb0fb2 | -16.692 | -55.9324 | 2024-10-05 13:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 5986cfe6-1d51-34ca-baac-5340f193ba28 | -17.1091 | -56.7479 | 2024-10-05 13:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 61f5a482-a079-3119-8602-1a064460ab7f | -16.9711 | -56.8058 | 2024-10-05 13:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 71618c5c-ec34-3cad-815c-c62ff59ac7ff | -17.0319 | -56.6749 | 2024-10-05 13:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 0e1e7431-96da-3979-8590-20d812828fa2 | -17.06 | -56.8 | 2024-10-05 14:03:47 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5bff3410-c89b-3bab-b06b-44225471c680 | -16.96 | -56.74 | 2024-10-05 14:03:50 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 64d5ec5e-2f61-3c71-943c-0996326c8de0 | -17.0 | -56.84 | 2024-10-05 14:03:50 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| df2f1e45-b9db-3bad-b213-eb6754299a8a | -17.0 | -56.76 | 2024-10-05 14:03:50 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1a4c911c-d032-304a-bfb5-76793881425e | -17.03 | -56.86 | 2024-10-05 14:03:50 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4dfe0b58-c06f-36b4-a27b-ae95cafdb7b4 | -17.03 | -56.78 | 2024-10-05 14:03:50 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52afcca1-4f22-3d7b-9dda-0b2213b32f8e | -12.75 | -50.56 | 2024-10-05 14:04:11 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 368dbe06-3b70-39eb-99ad-1d339a70e756 | -12.78 | -50.57 | 2024-10-05 14:04:11 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc7a1ddb-8a41-3fc4-aaf1-b6809082e815 | -12.78 | -50.51 | 2024-10-05 14:04:11 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9683931d-7921-3a88-9b22-b55b1213384a | -10.78 | -46.18 | 2024-10-05 14:04:24 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| befb829c-9237-35ea-9607-3aea9eb38cd8 | -1.4479 | -49.3568 | 2024-10-05 14:45:14 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0df14131-b1d9-3d19-a26f-3eca0e5168c4 | -1.3964 | -47.336 | 2024-10-05 14:45:14 | GOES-16 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 8e457f5d-b7f6-3fe4-90e8-8f1ce5d89652 | -2.5727 | -49.7149 | 2024-10-05 14:45:21 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ad5f1402-b885-342e-87eb-8921e5fd13eb | -2.9082 | -48.9193 | 2024-10-05 14:45:23 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| ce067290-24c4-30d2-927e-7595a716c235 | -3.1221 | -42.6287 | 2024-10-05 14:45:24 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 29279d7a-71a9-3ae6-8ce4-01dffd1de64a | -3.2906 | -42.5271 | 2024-10-05 14:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e1c661ee-37e4-3038-a826-ae9f228cfae0 | -3.9522 | -44.2832 | 2024-10-05 14:45:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| a47c50d6-ed3a-3dbe-a0d4-4d1e4181391a | -3.9961 | -43.2418 | 2024-10-05 14:45:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| c6323701-0859-3e6a-a310-36008efde309 | -3.9959 | -43.2651 | 2024-10-05 14:45:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 70a71d6e-15cb-33b3-9226-dae11ff4d270 | -4.0146 | -43.2641 | 2024-10-05 14:45:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 3367fa85-1819-3c28-a855-020229a94307 | -4.0148 | -43.2408 | 2024-10-05 14:45:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 160.5 |
| c980e2e7-1ba7-3fd0-a6d8-7ea2946c4b04 | -5.5787 | -46.2867 | 2024-10-05 14:45:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| c51f1ef8-c483-31e9-9acc-ea9d0d5b7bf4 | -5.56 | -46.2879 | 2024-10-05 14:45:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a5232fdf-9756-3b44-a4bf-75908c9add10 | -5.9862 | -46.6366 | 2024-10-05 14:45:40 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 18bbc31c-ff9c-3b3c-8bfd-b8749589ad73 | -5.9977 | -47.4728 | 2024-10-05 14:45:40 | GOES-16 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f1b610bd-79af-3061-9e2e-880946f76154 | -5.884 | -47.6989 | 2024-10-05 14:45:40 | GOES-16 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 859ec982-f2a2-304d-ae8b-9acc00515794 | -6.3311 | -45.6963 | 2024-10-05 14:45:42 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c277d2c2-aaef-3321-a833-8a6eff5c9d00 | -6.3498 | -45.6948 | 2024-10-05 14:45:42 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 073d6026-9241-3bf2-95bf-a17638f5d535 | -6.8216 | -59.1686 | 2024-10-05 14:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f8bb5ff3-004a-33a6-bf5f-644684ef17e2 | -6.8411 | -58.9939 | 2024-10-05 14:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 5b7551a9-e35f-388d-9d89-b9ceaa16a558 | -6.8412 | -58.9746 | 2024-10-05 14:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| e7e74892-89f8-33c6-929b-0bc5f57cd18d | -6.7281 | -59.4038 | 2024-10-05 14:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| d0b465ce-02a1-33cb-959a-4609fb82b05f | -6.8596 | -58.9931 | 2024-10-05 14:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 4ab6c821-8a23-38ca-abc0-81f7043f668c | -7.4409 | -64.2897 | 2024-10-05 14:45:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 2366e3f0-8e3e-3406-92e5-bbd568446335 | -8.1948 | -43.6936 | 2024-10-05 14:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 8e7918b5-4185-3692-9d95-af7ef909df67 | -8.1753 | -43.7424 | 2024-10-05 14:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 218.1 |
| 929e116f-2e1b-3847-8f1e-c9e7d72361a7 | -8.1759 | -43.6957 | 2024-10-05 14:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 035f92ec-2a49-35df-a897-410c291f15d7 | -8.817 | -45.1937 | 2024-10-05 14:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 64e6e0fe-e6b8-336c-bcb3-cdb31baacc8c | -8.8366 | -45.146 | 2024-10-05 14:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 08d20a3b-5865-3873-b298-f712e72f1353 | -8.8362 | -45.1688 | 2024-10-05 14:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 90dafa32-2ccb-3805-801d-10df88e8f741 | -9.1899 | -45.562 | 2024-10-05 14:45:58 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5b7873b7-e502-351e-8bcb-a5aff7e1ea8d | -9.3271 | -51.0931 | 2024-10-05 14:45:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| a4116378-a94a-3e87-9578-9b076724ee1c | -9.3269 | -51.1142 | 2024-10-05 14:45:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| d2af2168-834d-3665-a982-f8eb8e178c41 | -9.5917 | -47.9729 | 2024-10-05 14:46:00 | GOES-16 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| c01a63c7-079f-30f6-ac20-a0c7007683cd | -10.2476 | -52.7449 | 2024-10-05 14:46:04 | GOES-16 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 131.4 |
| c4212312-83e9-343e-8b78-9cbc983f79f8 | -10.2574 | -47.6796 | 2024-10-05 14:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 2ea9ee9c-786e-3e0d-8ee6-53f80f3875bc | -10.4235 | -50.7355 | 2024-10-05 14:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 27eaecbb-c5a2-38a3-bb95-048698b39482 | -10.5799 | -54.9301 | 2024-10-05 14:46:06 | GOES-16 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 172.4 |
| f43a8a11-54ce-327a-a7e9-f6c6205dc7c8 | -10.6985 | -46.106 | 2024-10-05 14:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 3b5832ba-6370-34da-b2d3-fc2b9648d9d7 | -10.6791 | -46.1311 | 2024-10-05 14:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |


[Clique aqui para ver as próximas entradas](README166.md)
