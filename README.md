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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d02da17b-15cf-3364-a8df-b4dabed3b8d7 | -9.3875 | -60.5528 | 2025-08-15 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 711b0f8e-48d1-3530-b461-a916954d4aa3 | -9.4995 | -60.5085 | 2025-08-15 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8b09f79a-79c0-3ebe-b418-e35d93917f71 | -3.4439 | -49.051 | 2025-08-15 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 48239eec-572d-3a9c-8bad-5ccc76a5225c | -7.5289 | -61.3825 | 2025-08-15 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 7f4d4c58-b1b0-3b80-a40f-1f192e59cb73 | -9.518 | -60.5268 | 2025-08-15 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d6dc7ceb-ea57-3048-8d71-e046f412d8ce | -9.4992 | -60.547 | 2025-08-15 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 0ec00157-e5d8-37f0-9219-cc0dce9588fe | -2.4876 | -47.5737 | 2025-08-15 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 1a7c3ff7-8d53-3e4f-a268-0792fef5e35f | -7.5919 | -63.4978 | 2025-08-15 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6d2033ad-e618-356f-afed-b001aacbac39 | -7.5291 | -61.3444 | 2025-08-15 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 900ba6da-d6aa-3ad9-9aa7-43b5b5209bc5 | -7.6103 | -63.516 | 2025-08-15 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| fb41077d-499e-3882-ab5d-fb2bc8429081 | -9.0357 | -40.5219 | 2025-08-15 00:00:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 159.9 |
| 06be901d-e897-37ae-891a-b574715d3e7b | -6.49 | -62.9306 | 2025-08-15 00:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c57bd42e-5495-3278-b7c4-92a1bb56c4ed | -5.455 | -60.12 | 2025-08-15 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 1b794dc6-7df8-3706-a212-ab06d0a662f9 | -7.0982 | -59.215 | 2025-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| dc92783d-5192-365c-9b45-3fd9747e85c1 | -5.762 | -46.6741 | 2025-08-15 00:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| b02a0d39-d2ec-3cc3-ac7e-5a45fa4ab1b1 | -6.9302 | -59.5497 | 2025-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8f355a07-acf2-3dbf-ad9c-02f72e4a4d3f | -7.9516 | -61.7654 | 2025-08-15 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 43d03ed1-57ab-3ff1-bfc7-9f43889c0fe9 | -7.5385 | -63.1046 | 2025-08-15 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 880ddf0b-2a1f-3103-9e1d-7c4c35378d20 | -6.9303 | -59.5305 | 2025-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 54b2febe-6971-329e-9c6e-72e00c4ebd3c | -11.3466 | -55.4326 | 2025-08-15 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 010f7802-32e1-345b-90b2-2ddb854465eb | -7.33 | -60.6273 | 2025-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| fac00e39-0f5a-3d20-8c0a-475044577baa | -7.4258 | -60.0292 | 2025-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b2a8b6fb-84b5-30cd-b259-091d45beee55 | -7.5386 | -63.0857 | 2025-08-15 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 87f6e4e8-26bc-3b6f-8f57-290216ac6506 | -7.3116 | -60.628 | 2025-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 43791786-fbc3-357a-b790-564e8ebcdd52 | -8.1029 | -61.1878 | 2025-08-15 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| dc258150-b2ca-3e6d-a13a-5622feba1867 | -7.0797 | -59.2157 | 2025-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 4faab245-004b-31fd-b44a-75c6e7cb5528 | -7.5292 | -61.3254 | 2025-08-15 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 06b598eb-ba87-3cdb-a4da-27b466f03154 | -3.4254 | -49.0517 | 2025-08-15 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| bad554e9-95a8-393f-8e6a-be12c02e52e9 | -8.1246 | -55.569 | 2025-08-15 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| bafcdcf3-0f83-36fb-a49a-50324501c14f | -11.3657 | -55.4107 | 2025-08-15 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 0780727b-94d6-3799-a984-8ee2a93b3606 | -18.5124 | -50.742 | 2025-08-15 00:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| cdc11559-ef40-34df-975f-ddfff1f058b2 | -9.5179 | -60.5461 | 2025-08-15 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 2dea96cd-193c-3333-a7c4-340865057c7b | -11.3468 | -55.4124 | 2025-08-15 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 94793e5c-963d-3eb8-9b94-6bc1ef84f521 | -9.4994 | -60.5278 | 2025-08-15 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 900ad213-cb16-370e-a900-bbe3d94eb757 | -18.3009 | -49.5567 | 2025-08-15 00:00:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 59.0 |
| d5f6c8a6-aa1e-3b28-a04f-e46b08170fbb | -14.2444 | -44.5897 | 2025-08-15 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 5e96ef3c-ce33-3480-a67e-c5e11e4826e0 | -7.9517 | -61.7464 | 2025-08-15 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e947def3-10a4-3ead-873c-878b508cafe8 | -5.455 | -60.1391 | 2025-08-15 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 3f0f9db1-2d9d-3a1d-b78d-73ccab3fdc10 | -11.9104 | -43.4319 | 2025-08-15 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 4a1268eb-c7fe-363f-92fb-fb7015af3cd1 | -7.0796 | -59.2351 | 2025-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 9e29b730-c9c1-3880-b675-a0a48872866f | -8.1432 | -55.5679 | 2025-08-15 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 97b50b0a-808d-380b-a84c-e6a6c6b1db81 | -13.1265 | -57.1494 | 2025-08-15 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| bc1ea56f-909f-36cd-a0a0-c73041357ef0 | -11.3655 | -55.431 | 2025-08-15 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 166.8 |
| df5fb3e9-ccf4-3ebf-971d-ed7c92a1371e | -11.9292 | -43.4526 | 2025-08-15 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d6fa382f-1e55-35a0-b26e-f60791dbde28 | -5.4366 | -60.1397 | 2025-08-15 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 49058f7d-0ebc-3166-a450-53f304672568 | -7.2931 | -60.6287 | 2025-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bd0bc898-ed85-3121-8c1e-5624617bb790 | -7.52 | -63.1052 | 2025-08-15 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| c1a45426-c8ac-3237-acac-3e353aad3f2a | -11.9296 | -43.4288 | 2025-08-15 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 29b32d01-51f0-33d2-b08c-6ccf7adeee40 | -7.6104 | -63.4972 | 2025-08-15 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0ff4ba31-9366-36ad-9ad7-a5b2a1af02a2 | -7.6104 | -63.4972 | 2025-08-15 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9c573aa7-7e40-3a56-9d80-297bf05dcefa | -11.3468 | -55.4124 | 2025-08-15 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 167.7 |
| a2b09d87-a89d-3779-9e07-0b5ad94f6720 | -11.3655 | -55.431 | 2025-08-15 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 0b73cec6-0ab6-34ad-954e-2c24e76e440f | -9.0361 | -40.4971 | 2025-08-15 00:10:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 1e66dc22-fe37-35dd-a3af-72e17072ef25 | -7.5918 | -63.5166 | 2025-08-15 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 74ab6e93-962a-3b0f-b169-eaada2b06b0a | -7.5385 | -63.1046 | 2025-08-15 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 16657812-bff4-37a3-8b1a-22c68925bc0e | -7.33 | -60.6273 | 2025-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a30528f5-8b0b-3fb5-8df9-d86d40169dfc | -5.4366 | -60.1397 | 2025-08-15 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b72a2b0c-3489-3f97-99e2-2490eb4e83a4 | -11.3466 | -55.4326 | 2025-08-15 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 164.3 |
| db9de7ae-d998-3b8c-bea5-b9909a6b9ada | -11.9292 | -43.4526 | 2025-08-15 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 97f29e2b-2777-3554-b1bb-bcad0943d572 | -9.3876 | -60.5335 | 2025-08-15 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f4a98d59-6c8a-3518-a3f4-a819daac89d4 | -9.4994 | -60.5278 | 2025-08-15 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 168.1 |
| b4e12c46-3cf0-3780-9067-1893ff05fd77 | -5.762 | -46.6741 | 2025-08-15 00:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 18ee74f8-8494-3078-8938-172720cb271f | -7.5292 | -61.3254 | 2025-08-15 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 84cb1544-4cbf-395f-9b37-18454bd0a15e | -9.518 | -60.5268 | 2025-08-15 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 93eab06b-1238-3b9c-88c2-13b2b49c0126 | -7.52 | -63.1052 | 2025-08-15 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 104.4 |
| a9e3ce54-bf91-33f2-9842-80e7fa0518e5 | -9.0357 | -40.5219 | 2025-08-15 00:10:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 139.0 |
| dee40826-225f-3090-88cd-f04fb7ea2193 | -9.4992 | -60.547 | 2025-08-15 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 7c0af632-1093-3bc4-8a5f-95c7c441999c | -11.3657 | -55.4107 | 2025-08-15 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 7f754c55-b4c1-37b6-a156-0c704c4872b9 | -7.3116 | -60.628 | 2025-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 1e2ca1cc-e04f-3534-accf-348d2a091cea | -9.5179 | -60.5461 | 2025-08-15 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ae380ae2-5c5b-3f07-867b-6dd30fe4935c | -5.455 | -60.1391 | 2025-08-15 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 140.7 |
| d55cee57-7306-3d3e-aa00-952c1633481c | -7.0613 | -59.2165 | 2025-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 5c4424a4-5687-38aa-aa74-03f9978f94b7 | -13.3203 | -45.2177 | 2025-08-15 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 972d156d-0699-3187-816a-5fd3928f2ffb | -8.1029 | -61.1878 | 2025-08-15 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 462c9c9d-1159-33f4-a8dd-b873a03c78fd | -2.4876 | -47.5737 | 2025-08-15 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e55cbc00-4ebf-3820-94c6-35e3b31a1eb3 | -7.5291 | -61.3444 | 2025-08-15 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| be92baa6-3b5a-32fc-a223-696a94a7d5ca | -7.5919 | -63.4978 | 2025-08-15 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 6fe8614f-1593-3941-be28-fe7c03944b02 | -7.0797 | -59.2157 | 2025-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| e2e27f09-3703-3815-9fb2-28cb56240695 | -13.1262 | -57.1695 | 2025-08-15 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 9862ffcf-5c4d-384a-bfb8-5869453304e8 | -7.5386 | -63.0857 | 2025-08-15 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 94a8c657-1c86-3afb-82f7-a5660b0e669f | -7.6103 | -63.516 | 2025-08-15 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e74c9cbb-d2f9-37da-9072-fa9818dfac0d | -9.3875 | -60.5528 | 2025-08-15 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 75e7c237-66d5-376c-816d-bf884564a498 | -9.4995 | -60.5085 | 2025-08-15 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 933ed8c8-15d2-307a-9155-4a3450a055d6 | -7.9517 | -61.7464 | 2025-08-15 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c4855638-8b42-3784-a6bf-ba737678d904 | -3.4254 | -49.0517 | 2025-08-15 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| fc0a03a7-f681-3ddd-b85f-e3cafb111341 | -7.9516 | -61.7654 | 2025-08-15 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 2726cdc6-4812-336d-9fbd-9f600b6c3a13 | -9.5351 | -63.5771 | 2025-08-15 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 07b37664-d35a-3f01-8ed4-688bbfa19ef5 | -5.455 | -60.12 | 2025-08-15 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 41e2b2b2-089e-3f79-bb44-c23757b62e31 | -7.0796 | -59.2351 | 2025-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| decae8c5-ea1d-3ef8-8021-5bd5251971ad | -11.9104 | -43.4319 | 2025-08-15 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| c2e7a541-cdef-3c7b-9e76-2e1f721e8948 | -6.49 | -62.9306 | 2025-08-15 00:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| cb43d004-e707-3b88-83b0-52647ccad1f8 | -7.5201 | -63.0863 | 2025-08-15 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| a85799d3-58cb-38d9-b383-bd8c723c94b2 | -6.9302 | -59.5497 | 2025-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| cec57f9a-77fa-3e02-bd13-0426bf18c439 | -7.0982 | -59.215 | 2025-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f02ffcb0-6127-31c8-bf5f-8262f1771a81 | -14.2444 | -44.5897 | 2025-08-15 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a043c202-3d56-3c08-926f-ad246d3ac277 | -11.9296 | -43.4288 | 2025-08-15 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 3f434c59-c2eb-36db-85ac-fa59a5adf7fb | -6.9303 | -59.5305 | 2025-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 1838a355-1925-31ff-aeab-75b36d6f9e5f | -8.1246 | -55.569 | 2025-08-15 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 67406731-1113-3d32-8897-873e6fad8656 | -7.6104 | -63.4972 | 2025-08-15 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d3b9884a-5ce1-3837-a787-3c10f8f01713 | -7.5386 | -63.0857 | 2025-08-15 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |


[Clique aqui para ver as próximas entradas](README2.md)
