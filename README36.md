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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cc35533-2bf0-30e4-9441-fd11a504252f | -9.95905 | -47.38052 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c14f29b9-7c54-329f-b3c5-14e410373e43 | -9.95893 | -47.37613 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3216721-7557-3951-82bd-95e96383c470 | -9.95828 | -47.37978 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4aa5f84-a7be-3e56-99f1-c06d84252b2b | -9.95781 | -47.38783 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 187d86df-5b04-38f4-99ba-5424ccf3d90e | -10.3957 | -47.35664 | 2024-10-16 04:08:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7c12fbd-431f-347c-a9ee-7a69dcdaa446 | -10.39513 | -47.35988 | 2024-10-16 04:08:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f8f6424-2c85-3de8-a946-40bbef67cf5a | -10.39506 | -47.36025 | 2024-10-16 04:08:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 526217f5-98d1-3db9-9474-fea1828005cc | -10.26307 | -47.30354 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 760c277b-3c4c-3f91-a6de-c77d0515449b | -10.26246 | -47.30706 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99d7ace6-6008-368d-aa8d-0d5cf86bc85e | -10.25844 | -47.30635 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91359820-1497-3626-b6d6-524938a91d4f | -10.25502 | -47.3021 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6179c82-899e-3d3c-91d4-31e73471c9a8 | -10.25441 | -47.30564 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22a3ebe6-bb71-3a14-8f07-75b821066700 | -10.25282 | -47.29079 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 009e6b37-aa90-3ee4-a012-a47833beea81 | -10.25222 | -47.2943 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47d2e70a-e635-37db-a3a4-59574fcbfd09 | -10.252 | -47.19986 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9429bc92-4905-3dff-bae7-f1cc5596c92f | -10.25161 | -47.29784 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad57b6eb-dcca-3f71-917d-447591b619aa | -10.25099 | -47.30139 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f6ac96e8-c167-30e3-b9d8-dea9bc76caf2 | -10.2494 | -47.28656 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6afb8fb-c724-3131-aa2c-93d8594568ee | -10.2488 | -47.29008 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b22ec6bb-7f93-3013-a983-ba241689a191 | -10.24819 | -47.29359 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d0069e50-4fa4-326d-a61c-c6f872cb86ac | -10.24801 | -47.19909 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e322f9c4-19ac-3b83-aa3f-e57774e6905a | -10.24758 | -47.29713 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6c722a0-4958-32f0-9606-b779579e77d8 | -10.2474 | -47.20261 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d436087e-a96a-3dfe-847f-bcd4cc2d5460 | -10.24696 | -47.3007 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1452b489-fcea-3fc4-a189-2c9be7128126 | -10.2466 | -47.27883 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3ae9de1b-ce53-3e6e-8c4d-18b49930f868 | -10.24599 | -47.28234 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 279fbab5-f6f6-38c2-bb30-18c35e128095 | -10.24538 | -47.28587 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a92d953e-8d3a-3b5a-aaff-a2df7c134979 | -10.2444 | -47.26757 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 48b958e7-7ddb-3881-a2f6-85be0330a92b | -10.24379 | -47.27108 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c351bbec-3701-3d1b-8112-dba073127ace | -10.24318 | -47.2746 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9a25450b-b3ad-364e-a94a-f034e719d9fd | -10.24257 | -47.27813 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7357cce-4a36-3a26-9b08-7bf5dc061bf3 | -10.22959 | -47.21011 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2630d0c9-9ef1-312d-8f19-334a8a6ce2f7 | -10.22559 | -47.2094 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7b055861-b890-38d1-a6d1-ec341538a151 | -10.22497 | -47.21292 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 14cb6312-0393-3be9-90f8-518256c70713 | -12.15743 | -47.52258 | 2024-10-16 04:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d5df44a-3843-368e-9aaf-2e4aa9de6190 | -12.04799 | -46.7234 | 2024-10-16 04:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8a008f7-ab37-3489-a5d0-865bb80e370b | -12.04502 | -46.71805 | 2024-10-16 04:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5f4408b-f1ed-3564-b59f-b27916293974 | -12.0442 | -46.72276 | 2024-10-16 04:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 626a9712-5c17-3800-9d5f-dcd07b530654 | -12.04287 | -46.708 | 2024-10-16 04:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd930e63-6187-303c-b455-758192b3f02c | -12.03908 | -46.70737 | 2024-10-16 04:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79055431-86ce-325d-822e-788ba09ea0dd | -11.88743 | -47.70872 | 2024-10-16 04:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ebbd01b-418b-3db8-8d15-b025648e6c9d | -11.31757 | -47.58495 | 2024-10-16 04:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b930fabb-b198-32e0-a974-533ca1023c86 | -12.96745 | -47.06975 | 2024-10-16 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d82246a6-7236-3e79-8010-122572a3a1e4 | -12.5312 | -46.81978 | 2024-10-16 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5113117-e0a6-3cf6-a4fb-468016a4641f | -12.52744 | -47.83562 | 2024-10-16 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ab8f85c-0c71-3ff1-bcbe-61bf2cfac7ff | -12.52742 | -46.8191 | 2024-10-16 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 082ee990-5cd6-38e7-81b7-183a45e89c85 | -12.51273 | -47.41963 | 2024-10-16 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 500286c5-5367-38c5-a432-5dc604c431c4 | -12.51184 | -47.42472 | 2024-10-16 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c892733-c7ec-39ac-9854-c0f589dfbbf3 | -12.50881 | -47.41892 | 2024-10-16 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59a0fb38-dace-399d-95c1-bd61bec1cba4 | -12.50792 | -47.42401 | 2024-10-16 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4560b306-fb2e-3ace-bb99-c2057b4ae0be | -12.48781 | -47.28605 | 2024-10-16 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6ecb55c8-46e6-350c-baf8-be1b7227c585 | -12.48694 | -47.29099 | 2024-10-16 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f4fb7249-3dab-35e1-90c5-b70368c0504f | -12.48393 | -47.28535 | 2024-10-16 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 37f906e4-9777-3e59-b3e0-9e70fb141cda | -12.48305 | -47.2903 | 2024-10-16 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| da734e3e-2f92-38d0-89aa-eddb47c14c9f | -12.47917 | -47.2896 | 2024-10-16 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f64f8a0-2ba0-3e41-958a-2ef5c43e73c1 | -9.3228 | -47.37011 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77e939a4-64ac-3155-958a-b1d5c3976aca | -9.01185 | -47.464 | 2024-10-16 04:08:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0839b39-55d8-34f1-8bf6-0abda854e8a4 | -9.28601 | -47.60386 | 2024-10-16 04:08:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ec3b111-7283-3f75-98bd-ac8b2aee2c97 | -9.28533 | -47.60773 | 2024-10-16 04:08:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f340a08d-d019-3d72-a541-8146187cfdf4 | -9.27894 | -47.89262 | 2024-10-16 04:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ec0474f-97ef-3d3d-bae9-1d9767834dd3 | -9.21087 | -47.95495 | 2024-10-16 04:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27c52413-738b-3b57-b1c1-7e5db7fea700 | -9.20922 | -47.95214 | 2024-10-16 04:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87e600b3-40dc-3137-bd6f-6bb0f2101b30 | -9.20853 | -47.95621 | 2024-10-16 04:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee1ad3a2-9f4d-34c0-9418-690a3e02f42e | -9.20771 | -47.9352 | 2024-10-16 04:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c97412a-a0c1-3bca-aef4-012727a600ed | -9.20702 | -47.93922 | 2024-10-16 04:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bc77d0a-6821-363c-8876-e99c4f7f56cb | -9.20564 | -47.94733 | 2024-10-16 04:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56b4dd2d-ab25-3344-9429-79ff41f45dc2 | -9.20494 | -47.95143 | 2024-10-16 04:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13d13d89-384c-3f41-8469-13882bf46c5d | -9.20136 | -47.9466 | 2024-10-16 04:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75834d65-0d6d-35bc-86c9-c23f34d9946e | -9.20067 | -47.95063 | 2024-10-16 04:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eda4efce-876f-3305-82d0-eb33a4817242 | -9.12215 | -47.70008 | 2024-10-16 04:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c26cd4c-f9f8-3251-a93e-3f4ed40f1d98 | -9.11794 | -47.69932 | 2024-10-16 04:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71e9bc53-0a91-3895-b7ee-828a96386bce | -9.09047 | -47.78324 | 2024-10-16 04:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35068174-a25b-3333-a3e1-346dad2e1225 | -8.90714 | -47.91374 | 2024-10-16 04:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5c58614-9788-367f-a166-2e53613833b1 | -8.86231 | -47.55238 | 2024-10-16 04:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b41e596-f1cb-3719-9f06-90a1e387ba92 | -8.80336 | -47.86277 | 2024-10-16 04:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d080a04b-36a6-32c6-ad91-c64194ad386e | -8.80266 | -47.86671 | 2024-10-16 04:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a740d6e0-3cab-3603-95ed-1aa369ef039a | -8.80116 | -47.86288 | 2024-10-16 04:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c08ca62-987a-3bef-b55a-a58e2df20525 | -9.99509 | -48.63782 | 2024-10-16 04:08:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c885f72c-5c53-37d6-a6d6-0d70e37b2467 | -9.99431 | -48.64222 | 2024-10-16 04:08:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ee95050-dfce-3440-bfc2-28722a0fba0d | -9.6288 | -48.54702 | 2024-10-16 04:08:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad6c191e-c49c-335c-a9fe-a89b4b25b038 | -9.62806 | -48.55129 | 2024-10-16 04:08:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9a47269-bb38-3861-b664-5d22f8cfeb53 | -9.61106 | -47.55489 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10cb65a8-a22b-3ece-a58a-a570ebb93c7f | -9.60912 | -47.55515 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 718b3eb8-509a-3d20-a908-301bc6a99ef4 | -9.49 | -47.82248 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83324a18-0e5e-39e1-9706-3c14866649c0 | -9.48648 | -47.81776 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96a9dce8-75be-3ffa-8663-0f11fc534913 | -10.83796 | -47.78439 | 2024-10-16 04:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bfd5499-2da7-331d-9113-1d1d503613f4 | -10.83385 | -47.78366 | 2024-10-16 04:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f09d4560-7b13-32bf-9d40-315e055c7112 | -10.83323 | -47.7872 | 2024-10-16 04:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 631027c6-4711-37e5-8db6-2a24d888733b | -10.52075 | -48.64886 | 2024-10-16 04:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3f55c96-77aa-36db-b46f-8065f1df0ef7 | -10.50301 | -47.77153 | 2024-10-16 04:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8d24368-6b08-30e8-9fe1-5aee265668ef | -10.50019 | -48.91652 | 2024-10-16 04:08:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bf4214a-9f6c-3887-bcd8-c25c7307b286 | -10.03089 | -47.65415 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0b7a523-33c7-393e-835c-8499c4ab73cb | -10.02622 | -47.6805 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e03f303-bff5-3726-a3f8-cf59b0dacc90 | -10.02557 | -47.68418 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e527e0b2-69a8-3016-a0f3-4e41bbeaed46 | -10.02273 | -47.67613 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0bbdb8f9-72fb-39f6-ba28-de6853f38723 | -10.02208 | -47.67981 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e48cfb79-5487-3f4e-b60b-4edea5898396 | -10.02039 | -47.68007 | 2024-10-16 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95024a71-2d90-3461-b26b-9e378e704dd3 | -12.18046 | -47.98589 | 2024-10-16 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e6f2372-6c1c-3ca5-be6d-4911c75e2329 | -12.07075 | -48.38467 | 2024-10-16 04:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d37d69c-0d85-3d30-b403-650613a913de | -11.52538 | -49.07568 | 2024-10-16 04:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README37.md)
