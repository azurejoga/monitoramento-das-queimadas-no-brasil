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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 175960b3-d5ba-3887-bbd6-12b4396243df | -11.88779 | -49.90607 | 2025-09-30 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20b986f4-2b64-3c22-9e29-0c3da88acba4 | -12.29198 | -55.14495 | 2025-09-30 05:08:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c489e705-d4a8-3336-9e3c-92cc3ef37659 | -11.19536 | -47.22523 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 151bb849-bb4c-3df2-b6ad-4a43aa8d8436 | -11.30438 | -53.95672 | 2025-09-30 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 824bd655-5ff9-351c-89f0-637ef53f887d | -10.10068 | -54.18689 | 2025-09-30 05:08:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c619b96b-1947-3a77-8430-79f1dfa8275c | -11.88868 | -48.05587 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a4aa83cc-0caf-365d-acc3-79745a64306a | -8.82901 | -46.1874 | 2025-09-30 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bc841e6-1ff0-3020-9c28-7821790d6a25 | -13.36875 | -47.31082 | 2025-09-30 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b9d83de-ebff-37a8-9979-2d84b9456097 | -11.19863 | -47.24421 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ce3abef-024f-31c8-9750-3b3d0c747edc | -10.76925 | -45.37227 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8fb60f3b-631f-3519-bb25-c8c0b4137197 | -10.40224 | -48.16638 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53211cc4-380c-388e-a69d-5805ff98ae11 | -8.22941 | -45.5027 | 2025-09-30 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4029a8f4-ad2a-34b1-8e58-173e26709911 | -12.22337 | -43.75584 | 2025-09-30 05:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9066e441-cb37-3499-8673-96508e7bd5e4 | -8.94268 | -51.69258 | 2025-09-30 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 215c1741-d499-3ac5-93ee-56e4ea1e5035 | -10.10056 | -54.18635 | 2025-09-30 05:08:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d75b830d-dd7f-3dc6-ba44-7c927f4e5738 | -13.3716 | -47.31806 | 2025-09-30 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| daa1a0c2-28e2-30fd-90a1-ed0344f536ac | -8.02067 | -55.41556 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5855876-9ca6-3dc8-a9a1-23fd4acf550d | -11.6473 | -47.49657 | 2025-09-30 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1f099f2-43d0-381f-a9bf-e9ae21a40ae2 | -11.72888 | -44.44404 | 2025-09-30 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 597cec01-320b-32cd-b808-d2ed8082338f | -12.78065 | -46.85792 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9eda89be-3743-3e21-9b9b-d08abd846dbb | -11.16409 | -54.12597 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 29e33384-1ce1-3e2d-b471-2aaca08d465f | -7.91283 | -44.63253 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1b8caf0b-e9d9-30fa-acb5-49e5a3536fee | -10.95461 | -46.50143 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71b53ac4-ca4d-32a4-bcbb-7804fbc21fef | -11.19626 | -47.21796 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 83949eb0-f1e8-3465-9c2d-7a5e1aeea93f | -9.03931 | -46.70058 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ca72af2-420c-382c-83ff-26d2ef4824d8 | -12.87454 | -46.90437 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a75031cc-f473-3bec-ab53-b4bfad5eaa23 | -10.19556 | -44.90358 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 5ad7ea50-8b75-35f4-8344-24eaa70e676a | -9.40331 | -54.70597 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7114b73-1507-39fe-b685-9402cab5f937 | -8.25847 | -45.51217 | 2025-09-30 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f7b7e03-861d-321f-8258-1050842934be | -9.31957 | -50.62894 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91d41331-0085-3bfd-b1ad-4a0d5e72ec6f | -12.00567 | -49.75649 | 2025-09-30 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f27cc705-fd51-3721-ae5c-ed5a3e02a275 | -8.87788 | -46.65747 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d52ea8b8-d7c3-35ce-9a31-f22ba2f647d3 | -9.55376 | -54.63675 | 2025-09-30 05:08:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5537bb19-d4fa-3745-81cc-9f913d6e509a | -9.38968 | -54.74954 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b09f28b7-35a6-3980-b25a-44c23455cc53 | -7.76013 | -45.76331 | 2025-09-30 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f500a6b9-bdf3-3c4f-8e11-942a1e19663d | -13.57726 | -48.05621 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15ed69bd-e18d-377f-b1bb-c9b1f94c1f70 | -6.84142 | -44.83894 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1d3779d-aaa7-34ca-adc6-3def1ab43883 | -9.6094 | -50.89456 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cf65bc3-b948-3d47-8a64-2fed4175b3eb | -10.19297 | -44.89371 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7bc7c03a-dfad-388a-bf71-cd749ce9ac4a | -7.83036 | -47.00194 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ab80a26e-97be-3d18-9b1c-da8e5ab5dc33 | -8.14538 | -46.36447 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 991f6cb3-6fb0-38ca-8f31-7ebfb3f5bce1 | -11.16114 | -54.12134 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| f36b2821-9d7b-3f23-aae0-3681b03066a8 | -9.46163 | -45.48899 | 2025-09-30 05:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5710b779-e03a-3d7f-8476-f433c95d32ba | -10.38733 | -51.16183 | 2025-09-30 05:08:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccf9ab13-e85d-3c4a-acbc-47f7159bd418 | -11.75374 | -44.75086 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4b8729c2-378c-31ac-8cab-1f0152404875 | -11.45652 | -51.50558 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a15b0d67-2bfc-318d-83df-31ad630759c3 | -10.62755 | -48.55015 | 2025-09-30 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a67d0f37-0dc9-3c39-869c-cc4a2654ed83 | -10.22563 | -57.99863 | 2025-09-30 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d03f6807-3280-340a-9c0d-fc97c63a2b15 | -11.25068 | -47.23307 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16b12f98-035d-3cfa-b74b-09320cf5d654 | -10.66076 | -53.71049 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7687a34-3774-3956-9978-11676808672d | -10.83162 | -47.96362 | 2025-09-30 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 271ce733-4fe0-3f9f-aa33-4e9a55721420 | -9.4079 | -54.72189 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02188ab4-a619-31ee-a264-766efc462e80 | -13.40987 | -47.5465 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 133fcd6d-2f11-302f-990f-3fbb48317e68 | -8.14744 | -46.39181 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88dbac07-d15e-3c7d-8c5e-2ff076589be4 | -9.32279 | -45.70042 | 2025-09-30 05:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89b55a2b-6498-3ffd-882e-ca42c19b8426 | -9.12962 | -47.63116 | 2025-09-30 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e7183f1-0ed1-3423-9baf-b6f8730c84fe | -8.16011 | -46.38268 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64595875-5c2e-3d99-99da-97ad5abe79d6 | -11.15401 | -54.1203 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 77295d80-ec9b-3251-ad07-9539c865015c | -9.5161 | -47.69325 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad438e74-c5be-3a2d-af13-2579ec78e95d | -8.86622 | -46.65986 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9a2639f-51fa-38a3-aa0b-18a5f4560ca9 | -7.60951 | -47.33432 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 859aca1f-1482-3a60-8d0a-a5dd2b7e31c6 | -12.75542 | -46.87233 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e831cec-08bf-3f75-b768-b7307e5a1d2e | -6.37018 | -45.62309 | 2025-09-30 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 489569a7-98b8-37a8-a9ef-878da35ea5d8 | -10.07705 | -50.21725 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9ccf1c77-20ff-399e-8bb2-7aef2b144d0a | -9.42902 | -54.72139 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd577fe7-2f7b-30da-a518-8f06f90aef2d | -10.40162 | -48.17125 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 559bcb5f-b060-3a6e-b83e-ca81d601315a | -9.40102 | -54.69799 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2cd8a09-2846-3ab6-976c-ad9126e86654 | -10.19933 | -44.89438 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 859e0696-e9df-3a2c-9251-bea1f4785614 | -10.10593 | -47.7799 | 2025-09-30 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f7dfcb8-2543-347d-a1ae-8c787cb2ca2c | -11.19825 | -47.74472 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80b2671d-0eca-34ea-ae2a-7cf93b491bf1 | -12.45567 | -54.30533 | 2025-09-30 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14c99e64-c4fc-3ddd-a2fb-5525cd4cf648 | -11.64064 | -46.84547 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31229b75-5dbd-3517-a7d8-ab31d095680a | -9.41643 | -54.68894 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c41e347e-3f06-38b7-9158-d4f6524a3108 | -6.37077 | -45.6189 | 2025-09-30 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20822940-a0d9-327e-b40e-c0656ab0e21d | -11.18805 | -47.23885 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4a2df89e-4ee7-3624-bb7a-15f5fa8d696b | -7.75971 | -45.76543 | 2025-09-30 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a64a00c3-dbe7-387f-9b45-972f5878cd09 | -8.53129 | -44.66808 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27c12012-5e77-30ed-87bc-88b38bb92f71 | -7.21009 | -45.47304 | 2025-09-30 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61892062-28e2-38e2-821b-b37a08b2423a | -13.39613 | -48.07124 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71ae792d-32ad-37d5-a9a4-e60f13710469 | -11.97443 | -46.57857 | 2025-09-30 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc742aee-59d5-35c9-b081-e3b3ce59f526 | -9.40501 | -54.69478 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09bccf67-63f5-31f4-b052-54ffec2ffe90 | -13.3884 | -48.06306 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65d07a63-c902-33b6-9b75-b6fdfb1a05d2 | -8.87175 | -46.66092 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ea48d77-62ab-3a63-a349-aa9db80a782c | -9.29578 | -54.50242 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a036c008-a6dc-3edb-a8cc-e714f2be56f2 | -11.75396 | -46.84294 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9a9a280-be2b-3a79-8839-065bbe6e8704 | -6.93581 | -45.40145 | 2025-09-30 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a445450-48b7-3e6b-a523-25b04018b383 | -10.19995 | -44.88926 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c4c63317-dbf4-3f91-a3f9-752873996a11 | -11.15647 | -49.81593 | 2025-09-30 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b4fb4d2-8a72-3375-ae29-7eae19aa96f9 | -10.95106 | -46.48666 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 19cf736d-f2aa-32d3-9e51-5566dde8c9f8 | -8.1419 | -46.39053 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5bb3ee5-f312-307c-9d1d-6063bfb5c68b | -7.91633 | -44.60528 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93bad2c7-01af-323d-bd75-b92d99b2d952 | -12.79342 | -46.89781 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d56169a-5717-3bd7-a275-40cb626677be | -9.32385 | -50.62955 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5c93ad8-689a-3afd-a14f-93d59f2c2999 | -11.19401 | -47.23615 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d58655c-7ba3-381b-9d20-513aa3f05d2a | -11.41192 | -55.06453 | 2025-09-30 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4cbe769-7f7e-375f-8811-54530e90b559 | -10.89394 | -53.7423 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd3d62f0-1c46-35e2-b167-5216d2f6e137 | -11.97283 | -46.58004 | 2025-09-30 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 132e7222-50a7-37a3-b1d5-a9250e51a385 | -11.7534 | -46.84073 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42cad0e7-965b-373a-ae9f-2e04a205c7cb | -10.1936 | -44.88848 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e551c9b7-0467-33f0-8365-dddc60d2dc3c | -10.71114 | -53.80182 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README89.md)
