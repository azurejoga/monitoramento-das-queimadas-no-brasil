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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a61af8f-b3c9-3584-980f-7d0186833c88 | -11.81141 | -54.50229 | 2025-06-20 04:02:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dfbf2af-543f-33e4-a281-d5eeba240f64 | -11.31735 | -45.19855 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 180f1663-540e-3ab6-835c-b53a39201840 | -10.65837 | -49.36836 | 2025-06-20 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cb218803-236f-3f20-8477-83170fdf5b12 | -11.13861 | -46.66204 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb04448c-b76c-39ab-be67-9ea47db1e6e4 | -11.11998 | -46.67019 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff5e3e3b-513a-36b4-9690-302e0221f395 | -11.12065 | -46.66641 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b141116-d7af-301d-8d05-77f99a40462b | -11.31194 | -45.20711 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf44448c-362b-3827-a56c-50778b5b92e8 | -10.92728 | -49.28072 | 2025-06-20 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2059efe5-6ccb-3083-a6f6-cca158cfa6a9 | -15.42683 | -47.83455 | 2025-06-20 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 199b6c47-379f-39a8-b2e4-4e5a91d2d3b0 | -13.65518 | -53.94358 | 2025-06-20 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 243299c5-8b32-3e07-865f-8c26d33c10a9 | -13.25994 | -46.81902 | 2025-06-20 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16ae731d-9b1d-3992-9751-32d416f366b3 | -10.46488 | -47.05164 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| ecd99605-44a6-339a-97dd-bedef9061521 | -10.92738 | -49.27889 | 2025-06-20 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc44abe1-4598-36cb-a662-cd1069316628 | -14.62836 | -48.12087 | 2025-06-20 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8288ef25-ba7f-3a25-8812-96a139600451 | -14.43417 | -48.92207 | 2025-06-20 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b24cfd39-c5cc-32e4-b44a-a897f63d7a99 | -10.86083 | -53.76357 | 2025-06-20 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25ccba31-e6a9-33b8-8c75-a87def9d514c | -10.46997 | -47.04817 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 22917e22-60a4-31c8-8c87-ca26e5bc1451 | -15.4006 | -47.80879 | 2025-06-20 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0140297f-1bea-373e-90b2-22321e567363 | -13.09116 | -52.29582 | 2025-06-20 04:02:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec4a8a42-c737-3298-8cdf-42d3cc6688c6 | -11.82057 | -54.50005 | 2025-06-20 04:02:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21804f76-4c8f-31a2-b66e-3be830a4be11 | -17.77885 | -42.80738 | 2025-06-20 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 58ca32f2-73a3-359e-9898-e5106e6694b4 | -11.46592 | -47.29538 | 2025-06-20 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9e37a1c-c0fc-33f6-919f-12c9ce45d57c | -11.46667 | -47.29117 | 2025-06-20 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2a70081-8362-3076-9cb7-5a7665abbd8e | -13.65633 | -53.93806 | 2025-06-20 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06f03b62-8fe8-31ef-a043-498917d04253 | -10.52429 | -46.64616 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b7819d1-71dd-3954-a178-fa4e4c4e2889 | -13.25512 | -46.82254 | 2025-06-20 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e753010-43b2-3361-85da-317782d0ffda | -11.14278 | -46.66277 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 534f9380-644f-3005-bf77-dbb3bd47d130 | -14.48067 | -50.289 | 2025-06-20 04:02:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c41f745-882f-3603-853e-7842461236f5 | -14.62916 | -48.11659 | 2025-06-20 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16415964-61f5-3b78-81cd-987105c174c6 | -10.72723 | -49.55468 | 2025-06-20 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f24b86da-4793-3d6f-95db-9b529440df54 | -13.28668 | -46.43933 | 2025-06-20 04:02:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 775ebc16-dc45-3952-bdd0-9e5215272606 | -10.53329 | -46.64634 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a394909e-78b9-39a3-947b-d3a127568e69 | -10.48213 | -47.05497 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4ccef198-d21b-37e9-8701-9839df8f28ce | -10.83167 | -54.01066 | 2025-06-20 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d5743cf-5f33-3fca-b134-aede04f5e230 | -13.38787 | -48.45156 | 2025-06-20 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bce92298-c349-35f2-9374-3495d3729dcc | -10.0769 | -52.74584 | 2025-06-20 04:02:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e49fdc22-65f3-34ee-8e96-fcbcf54b989c | -15.40408 | -47.81338 | 2025-06-20 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 621db3a1-922f-32d1-897b-36b7e5cde339 | -11.31276 | -45.20245 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 40e69311-4f56-3f39-97a7-b69a0ee61c6a | -11.96199 | -53.5056 | 2025-06-20 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 873cee24-1d5e-3dff-9245-58e524b5cbcb | -10.49964 | -47.00677 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a892d49b-a431-389b-9183-7a59790d01f0 | -10.94057 | -49.43088 | 2025-06-20 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97a461e2-4ea6-3abb-9cca-a3ba7c48d0c6 | -11.57116 | -47.87118 | 2025-06-20 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af6b2f72-8da1-33bc-924b-09ac2e4da5ac | -12.7645 | -44.40999 | 2025-06-20 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 149b2f59-44b9-32a3-89ff-a887e6b72aac | -10.52909 | -46.64558 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e78048f9-c3e0-3842-ad9a-31b0c7f238e6 | -10.15645 | -48.98424 | 2025-06-20 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05c8a69b-83ed-3d40-92cc-d338cadff06a | -11.93387 | -48.42385 | 2025-06-20 04:02:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec3fc0ca-2f11-3e69-8806-a820a0160bef | -12.26525 | -44.60362 | 2025-06-20 04:02:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 436e01b0-601e-39e3-8093-6895c26eee4c | -12.21655 | -45.53083 | 2025-06-20 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7fb8a1af-e3eb-3e2b-aaeb-454fa475c3ef | -13.24214 | -48.41763 | 2025-06-20 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cadd637a-f76c-3285-8f0b-31724334d5b8 | -12.64825 | -54.11898 | 2025-06-20 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e992d3a8-27b7-37f6-b799-317b10f559e0 | -10.46767 | -47.06097 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 68ba95a4-3c7b-30a2-b69a-9ae261ae6899 | -11.31287 | -45.20593 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b362458-9d4d-36a2-911b-fe815d87e5c5 | -11.13849 | -46.63821 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcd1016f-40a2-3530-b76c-a725d684521f | -10.07793 | -52.74063 | 2025-06-20 04:02:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ce76e02c-8072-3937-b242-bf07c0270736 | -11.64164 | -49.18603 | 2025-06-20 04:02:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4dd3542-eadb-35e7-913c-bdd165b750c9 | -13.65753 | -53.94136 | 2025-06-20 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d494dbaf-4aeb-30bf-8d9e-657f01f6b51b | -14.62404 | -48.12009 | 2025-06-20 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c156a4a5-f172-3b73-9855-5a94d14daf25 | -11.58009 | -47.87302 | 2025-06-20 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e50fc595-6aa0-3946-a44e-6028488421f7 | -12.34707 | -49.31201 | 2025-06-20 04:02:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 677fea29-cb9f-3072-8298-0375c88f91af | -10.59413 | -49.46129 | 2025-06-20 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f060c17-32ba-39cd-9207-b4a2e6629467 | -10.59056 | -46.93226 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8945228-24e5-364e-9c18-5bc7cd187ced | -16.68253 | -43.88344 | 2025-06-20 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ec286cf-2928-32ee-9251-551e5b7ef749 | -12.34221 | -49.31108 | 2025-06-20 04:02:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d584868f-244f-3670-88b6-aa5c3881e074 | -12.21737 | -45.52605 | 2025-06-20 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4a218ca-6b00-3e59-a001-0dee37f66358 | -11.12898 | -46.66791 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4393cfd-ef50-3d81-a772-5071a32fbc53 | -10.52337 | -47.58326 | 2025-06-20 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 710a68e2-8516-38de-919f-926a11c15813 | -11.98531 | -51.61141 | 2025-06-20 04:02:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcd6ad00-9d14-35a0-96d2-d7d634c214ac | -11.97962 | -51.61032 | 2025-06-20 04:02:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfc95876-47d8-3535-b80e-5d8610c3ea77 | -15.4781 | -46.59132 | 2025-06-20 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22ab311e-3a04-3646-9917-fb67fda51f9d | -11.79662 | -48.08994 | 2025-06-20 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 744b9259-8d82-3042-b65c-7912e11c78ca | -11.15366 | -46.62498 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d5943efb-346e-3301-b1c6-d3c4dae3fb46 | -11.14965 | -46.64799 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c907aa41-c828-3db1-85f2-fe0e276457d5 | -10.08216 | -52.75235 | 2025-06-20 04:02:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b55a1875-373f-33b7-954d-2bf16e0ac5ce | -12.2012 | -49.61731 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c73b4f40-7996-3e65-bb5c-43b6b17ed2c3 | -12.39451 | -46.36573 | 2025-06-20 04:02:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63336d63-32d5-3889-bf21-81cbb94f5edc | -17.57749 | -47.49988 | 2025-06-20 04:02:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eda7bad7-990d-3950-bac8-99e331408f34 | -10.47503 | -47.04479 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| fd1d8268-46d1-3338-9445-c744b65ba24a | -10.48664 | -47.02977 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 38847a62-18f8-31c3-a8ef-207cf3d2ef1a | -12.34812 | -49.3065 | 2025-06-20 04:02:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fd73ce1d-9ec2-3662-a875-662119e036b6 | -13.26059 | -46.81537 | 2025-06-20 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 906a303c-a85c-39a2-a23b-ebef8443bd2f | -13.57648 | -44.26839 | 2025-06-20 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07420083-ac27-35a3-aa35-98c12adf4d03 | -14.43053 | -48.91622 | 2025-06-20 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4fcc4da6-53fa-3d69-b07f-b050159240eb | -13.77751 | -54.1969 | 2025-06-20 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 721c7363-88c6-3cc9-8dc1-b6b44434822e | -10.5189 | -47.58243 | 2025-06-20 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 404208f9-c74f-3ee1-8a7b-3f35a40c0e58 | -10.4302 | -47.11321 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a6a924d-5be5-3b6f-b5e0-4eb827050380 | -10.65782 | -49.37133 | 2025-06-20 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 97839435-8b16-333d-a72e-c521fdd78ecc | -14.48009 | -50.29202 | 2025-06-20 04:02:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77894cc9-7a91-3e43-9360-e02c6b1a9cdf | -14.03084 | -44.11438 | 2025-06-20 04:02:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ace66146-8360-3d06-ba01-5227a8184ad3 | -10.48718 | -47.05165 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 707318b7-a21f-36a2-bc7a-c894e0f868ee | -11.11444 | -46.67719 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b7680fd-fc44-3961-ab8f-0342b31755e3 | -19.96887 | -44.21572 | 2025-06-20 04:04:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e79f5f7f-be8d-3ae2-9ffd-a27118cb6024 | -20.16032 | -45.72306 | 2025-06-20 04:04:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c7b4efe-d47d-317c-96f3-b3969b964814 | -19.63762 | -45.19498 | 2025-06-20 04:04:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2f72c20e-494d-37aa-8f84-8df7e4d59e7f | -22.19626 | -41.6449 | 2025-06-20 04:04:00 | NOAA-20 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 2104a739-b8b9-357e-8580-8e2bf30b5b5d | -18.9907 | -52.08888 | 2025-06-20 04:04:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3c1e947-c1b3-3acc-b981-71e63aa01923 | -19.63831 | -45.19096 | 2025-06-20 04:04:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8dd2e17f-e1d3-30b4-8438-75c3f6b0c43c | -22.31259 | -53.58885 | 2025-06-20 04:04:00 | NOAA-20 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 83e10c31-90b5-3d41-8650-2796b9d47bea | -23.59161 | -47.43776 | 2025-06-20 04:04:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 636b53a6-e9f8-3167-bed4-01d9dbc9d497 | -19.54529 | -49.66812 | 2025-06-20 04:04:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9913b9d9-1dcf-3a7f-aad5-54577a9c4bfc | -22.6993 | -43.34842 | 2025-06-20 04:04:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README15.md)
