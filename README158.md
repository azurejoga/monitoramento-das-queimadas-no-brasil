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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4b9bf45-2511-3789-91d6-ed7a57e059fb | -11.0183 | -44.0382 | 2026-10-10 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 520e049f-5d9d-3db4-874f-850af14df627 | -12.0063 | -43.4402 | 2026-10-10 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 8be8b90f-2ab4-3bee-8e75-48f2ec05129e | -10.9388 | -45.3687 | 2026-10-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| e1fabeac-83ad-333f-bd26-2a920d76498d | -11.7776 | -45.4576 | 2026-10-10 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 160.7 |
| a942db21-ae84-3b51-a8ef-525cebe11e6b | -11.0187 | -44.0148 | 2026-10-10 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 3fdffed0-2449-370c-a27a-ee89ccd18c2b | -9.9398 | -44.7869 | 2026-10-10 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 250.9 |
| ccb74279-a1f2-33be-b713-78cc86bdd3b0 | -11.2064 | -45.3321 | 2026-10-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 8d30f9f6-f652-3f7b-8b2c-dbcd745dabc3 | -11.47 | -43.3824 | 2026-10-10 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 927c390d-e4b1-35d3-b0ab-603c6098c075 | -11.5874 | -45.3931 | 2026-10-10 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 9111bf73-0c69-357f-8d8a-6c4253b63de6 | -12.4649 | -51.2769 | 2026-10-10 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| b483532a-9858-37f9-8543-4469cf76cb59 | -17.4581 | -45.0511 | 2026-10-10 14:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 1d341d3e-9843-32b3-8b37-2988ab4298ee | -14.9757 | -41.6952 | 2026-10-10 14:00:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 183.5 |
| 86946b1f-395a-340e-a5cf-aba7c76b8f0f | 2.1146 | -55.877 | 2026-10-10 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 3c1e1a2f-060d-3b70-bb4b-1ba66b9a605a | -10.4914 | -47.231 | 2026-10-10 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| af9a023b-77a0-38fc-bb6c-bbf82114b285 | -11.8499 | -43.5835 | 2026-10-10 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 263.4 |
| 7ecff35f-8683-31d6-a258-e6c9ae315278 | -12.4837 | -51.2959 | 2026-10-10 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| e208853f-6525-3ae5-a6ad-8c4487ed2d47 | -12.2119 | -44.769 | 2026-10-10 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 263.4 |
| 1d31fbd5-4eca-3b4d-8636-b45d04cdfadc | -12.1729 | -44.7983 | 2026-10-10 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 724601cd-7e30-3ce3-97bb-f648c19722f3 | -12.4646 | -51.2982 | 2026-10-10 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f7b896d8-44ed-342d-87c1-dad8a148cd81 | -11.0374 | -44.0355 | 2026-10-10 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| e8ba130c-63a0-31ff-9540-78c23da0dc0b | -11.7742 | -43.5245 | 2026-10-10 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 49a28b0d-966c-38d1-9368-28c88d9a3601 | -8.9311 | -45.1355 | 2026-10-10 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 0b735f7e-cc03-3dbd-8f83-3377413f7f9e | 2.727 | -60.2586 | 2026-10-10 14:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 126.7 |
| b64d2f0b-2a94-39b5-a629-2d662de3fd82 | -14.9763 | -41.6703 | 2026-10-10 14:00:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 132.3 |
| b7344bf3-0ecd-3391-8001-5a669cb28bce | -12.1861 | -48.4124 | 2026-10-10 14:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a5e5e271-054b-398a-ba21-5916bbdc6d62 | -11.7772 | -45.4806 | 2026-10-10 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| c580fa1e-57c3-3d11-8e0c-0d10e6b733b4 | -8.3011 | -45.7245 | 2026-10-10 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 221f6d77-f7ff-323a-92c4-20644dc67ee0 | -10.473 | -47.1887 | 2026-10-10 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8a29c3ca-30bf-34b1-aa88-77183f08d649 | -9.1924 | -49.7678 | 2026-10-10 14:00:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 4a5e1418-73dc-39f7-9cd7-d24073266718 | -11.1876 | -45.3117 | 2026-10-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 8673b340-8fbb-3568-9e57-8ff2f0f983c1 | -11.0937 | -44.0975 | 2026-10-10 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 811.9 |
| e824b8e0-613d-3a56-bedf-0621a3c08e3c | -13.1444 | -54.3612 | 2026-10-10 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 6cd25f23-5f04-3fc8-96c5-e301bb223a1e | -10.454 | -47.191 | 2026-10-10 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e4b18301-9d67-32df-9078-25623658018b | -11.8692 | -43.5805 | 2026-10-10 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.4 |
| def299a0-4c72-3cb4-9bcc-be0be2617d6b | -13.183 | -54.3365 | 2026-10-10 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| afafea65-bc95-3a25-b807-60649f754b31 | -9.9208 | -44.7893 | 2026-10-10 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| e61788f1-eb54-3c1a-a907-82b0d603f2e1 | -17.4575 | -45.075 | 2026-10-10 14:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 9716da21-2ef1-3624-a69e-7942c66dbf4a | -7.7779 | -42.3246 | 2026-10-10 14:00:00 | GOES-19 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 940a752d-d1cc-35fd-927c-1e6d6ba239ce | -13.1636 | -54.3591 | 2026-10-10 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 688f6587-d239-3989-993e-f735f3ba9b99 | -8.3014 | -45.7019 | 2026-10-10 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 29a652c8-89fb-377d-9b04-b61fc741cb82 | -10.2317 | -46.8382 | 2026-10-10 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 70a486f9-90d5-3a5a-a790-101dc430f092 | -12.1917 | -44.8186 | 2026-10-10 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 6ad66418-31fc-3957-99df-1340d2824e7d | -11.1873 | -45.3347 | 2026-10-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 03e410c2-a344-3257-ad2c-a9361be6190b | -11.5683 | -45.3959 | 2026-10-10 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 200.5 |
| a86c338e-49be-330b-b268-ff18bd765bf7 | -11.8787 | -47.3668 | 2026-10-10 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| aa6a5446-1943-3992-aa93-eb7c03981b92 | -11.0941 | -44.0741 | 2026-10-10 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| e19d2aab-3f6e-3f65-8272-f118590fc9ed | -11.0745 | -44.1003 | 2026-10-10 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 226.4 |
| 8ddfd224-0bb7-3d8a-a4a8-912a5ba151c2 | -11.2853 | -45.1832 | 2026-10-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| e8954686-149a-3dbc-96cd-434068fa0f27 | -12.211 | -44.8156 | 2026-10-10 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 1b109b93-922c-3323-bd22-0b618e6bfb4a | -12.1733 | -44.775 | 2026-10-10 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| a95e9bec-2368-3e3f-b99d-c0bfbde80014 | -16.0077 | -40.6571 | 2026-10-10 14:00:00 | GOES-19 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| acab5d92-ebee-3ac6-91e2-706350edb6dc | -11.5121 | -47.6155 | 2026-10-10 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| a000d5ee-7c72-3fc9-a4f0-1c37429e7d84 | -15.6892 | -43.8327 | 2026-10-10 14:00:00 | GOES-19 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 133.3 |
| da968a5e-7a3c-3bff-bc77-09f439f64a98 | -13.1827 | -54.3571 | 2026-10-10 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| e0e39439-e72b-3afb-9537-4f1a6c6720ef | -9.9381 | -44.9022 | 2026-10-10 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f23effe2-4666-3bee-8a48-f247fdac8fa1 | -10.4144 | -47.3069 | 2026-10-10 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 398f455d-6858-3e56-9549-06c5671ef1ba | -9.9384 | -44.8791 | 2026-10-10 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 208.5 |
| cf6337b2-823b-3d57-ae8b-de7320e136e5 | -9.9211 | -44.7662 | 2026-10-10 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d6453828-65fc-3199-bd31-868463e5c0f9 | -13.1633 | -54.3798 | 2026-10-10 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| b8416b3a-7c0e-37f1-994b-46521c88ffd1 | -9.1924 | -49.7678 | 2026-10-10 14:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 689d37b8-7aad-305b-b783-5501b011f26c | -3.7817 | -41.6718 | 2026-10-10 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| df1e9860-7a71-390b-a9f6-fb4103d50549 | -8.9119 | -45.1605 | 2026-10-10 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 0e813f71-2e6e-39c4-ab38-99117d69a938 | -1.1715 | -49.1268 | 2026-10-10 14:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e359d4c4-e10b-3d36-8d4f-7aa2ab6cd4ec | -11.8499 | -43.5835 | 2026-10-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| f7f6749f-e73f-3468-83f5-48ac63be6426 | -8.2061 | -45.8017 | 2026-10-10 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 69820667-b059-33b5-9773-b6315507e02e | -11.8692 | -43.5805 | 2026-10-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 76415e0f-3d49-34f4-a2f0-1738739791d1 | -11.0937 | -44.0975 | 2026-10-10 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 564.9 |
| 11028cda-bd76-316d-a1e4-b6d0999eced5 | -7.4703 | -42.7842 | 2026-10-10 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| b6d1ca52-c035-3999-be3e-865a3cac4984 | -12.0457 | -43.3864 | 2026-10-10 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 166.5 |
| fd09ada7-625b-3745-852b-4688049e5a8b | -11.7742 | -43.5245 | 2026-10-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 6e0a58fd-d888-3dfd-b2f3-4c61ae96ae31 | -10.454 | -47.191 | 2026-10-10 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| aad1d6eb-e9bc-3c47-b715-5c08481eb101 | -7.4977 | -54.9854 | 2026-10-10 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 8ef37160-567f-32e3-b250-5e9209ef8f12 | -14.9757 | -41.6952 | 2026-10-10 14:10:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 240.6 |
| 423aa5db-c3bd-3bb5-98bd-0880345e3a3a | -9.1525 | -49.9639 | 2026-10-10 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| fdf79348-bb33-34ba-96d7-d386e916c86b | -13.1641 | -54.3178 | 2026-10-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 336cbbda-4e34-3bef-9bc8-ddaf049c9abc | -11.0374 | -44.0355 | 2026-10-10 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 8ba904f7-04a4-35ec-a627-72f7a898d6f9 | -11.0183 | -44.0382 | 2026-10-10 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 185.8 |
| cabfd90e-8838-35f9-9359-c09ae24abe69 | -7.4886 | -42.8295 | 2026-10-10 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 9395952d-786e-302c-abb0-07673c3538e5 | -11.1197 | -45.9602 | 2026-10-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| a6b4c70b-7544-3954-a3b6-0ab6d1f360de | -12.6873 | -43.0884 | 2026-10-10 14:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 0a31ece9-fe2b-3b28-9242-e7e836fa8567 | -13.1636 | -54.3591 | 2026-10-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 8bf8ede7-2a83-3757-9bfa-cb46a4ec9298 | -13.1444 | -54.3612 | 2026-10-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| f72bd2d1-81b3-3f23-b807-c1edd2d7744f | -13.1639 | -54.3385 | 2026-10-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| a16427f4-53a3-3db2-ab3b-e085c6d37a73 | -11.0745 | -44.1003 | 2026-10-10 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 5de073e3-347f-3ea1-8b92-c88650e16a49 | -9.9398 | -44.7869 | 2026-10-10 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 6ca2ab38-2922-3d01-9904-f1bdabd73291 | -1.4486 | -48.9953 | 2026-10-10 14:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 41bcdd78-441d-3b17-b149-23e323c374ba | -15.6892 | -43.8327 | 2026-10-10 14:10:00 | GOES-19 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 72c8ca22-dee2-3a27-a010-77e3d5011837 | -9.9395 | -44.81 | 2026-10-10 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 135.1 |
| eb09ba55-686b-3f45-bc43-dfc57d033b87 | -11.0933 | -44.1209 | 2026-10-10 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 353.9 |
| bc7fa473-fda7-3948-99f2-fc8fc0399b3a | -15.1088 | -46.9343 | 2026-10-10 14:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 7f2249f9-867c-321f-b445-f3ffbfd566fa | -7.4883 | -42.8532 | 2026-10-10 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 356e37a2-b5b4-3df4-8214-18156513709f | -11.7768 | -45.5035 | 2026-10-10 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| f7d9d9bb-27a7-3fbc-8d9d-8cfe249c840d | -13.183 | -54.3365 | 2026-10-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 6351d4fc-0d3d-3381-8efe-049832945533 | -17.4575 | -45.075 | 2026-10-10 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 8842f424-6e80-33dc-a63a-dc811a7b6c01 | -11.7362 | -43.5068 | 2026-10-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 0517a8a1-940b-3f27-b86f-23f583b528dd | -8.9275 | -45.4094 | 2026-10-10 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5d1c22e2-7d0a-3776-bd7e-aa43bc908e69 | -9.9384 | -44.8791 | 2026-10-10 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 200.2 |
| bdde9021-8037-305e-8220-abf41ccadbee | -10.4334 | -47.3046 | 2026-10-10 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| ad286107-60d1-3016-9a12-21b49df1eb08 | -11.8787 | -47.3668 | 2026-10-10 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 657d5e80-56b8-3711-99ee-d0d9d7d86290 | -10.4144 | -47.3069 | 2026-10-10 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |


[Clique aqui para ver as próximas entradas](README159.md)
