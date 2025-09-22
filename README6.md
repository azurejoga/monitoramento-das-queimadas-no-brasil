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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 683498bf-d411-3364-9a56-a7639a758584 | -6.9024 | -44.7656 | 2025-09-22 01:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 9fb08d7c-f29a-38e0-a350-4c24c7b454c4 | -20.2735 | -55.5141 | 2025-09-22 01:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 98d2681c-cdc9-3cfa-ae59-8877c81eab6d | -23.0031 | -48.3742 | 2025-09-22 01:10:00 | GOES-19 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 8354c274-1141-3fe5-be9e-e959828f46f5 | -22.9835 | -48.3321 | 2025-09-22 01:10:00 | GOES-19 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.1 |
| 30178491-6c61-35ab-bb33-c1d540694767 | -18.3998 | -42.8395 | 2025-09-22 01:10:00 | GOES-19 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.9 |
| d738bebf-65f1-31cd-b78d-688d886de463 | -15.9594 | -59.3687 | 2025-09-22 01:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 540371a2-e1b7-325c-ba26-4de61f260700 | -10.3572 | -46.0585 | 2025-09-22 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 716.3 |
| 5f24bc70-27e3-3d85-b6e7-679a25425e5e | -20.274 | -55.4927 | 2025-09-22 01:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 165.8 |
| aa6b8035-dd5a-31ea-8fa9-1c8bc9e435c5 | -11.6247 | -52.8624 | 2025-09-22 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 6b77cc45-b5d5-344d-abd3-eb2110f51121 | -22.8529 | -50.6155 | 2025-09-22 01:20:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| e427ec13-d12c-314f-8691-08393f0d4c88 | -11.6436 | -52.8605 | 2025-09-22 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 11029a29-f11c-3d44-b21c-2c903eaf9c92 | -11.8814 | -64.9323 | 2025-09-22 01:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| cc560b1f-4c68-313f-a7b9-cb10f0531e5c | -6.3937 | -45.0131 | 2025-09-22 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d88b5244-e887-355d-b7da-a27dd9550076 | -22.8117 | -50.6021 | 2025-09-22 01:20:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| 23e73d29-5297-388c-b9ed-f2ebb83edeb9 | -11.6249 | -52.8416 | 2025-09-22 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| be12be4b-68fa-3f12-a84b-95c29473d66f | -22.9828 | -48.3559 | 2025-09-22 01:20:00 | GOES-19 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| 8dd3fdef-e700-3d4c-b026-bc2c2c4cf909 | -20.2735 | -55.5141 | 2025-09-22 01:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 122.2 |
| fc412f00-c4cd-3f4e-9f29-a6694a0521af | -22.832 | -50.6203 | 2025-09-22 01:20:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.4 |
| 8e26a3c6-a054-317c-a256-c96beebc144f | -15.9591 | -59.3887 | 2025-09-22 01:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 85f6befc-8307-3ec6-a72b-79c954d25150 | -4.3197 | -48.0908 | 2025-09-22 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 3e63092a-5c4f-3435-87db-01907f8000bb | -15.9594 | -59.3687 | 2025-09-22 01:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 94f1d9d2-ce65-3bc6-858b-893388c7848d | -22.9075 | -47.4275 | 2025-09-22 01:20:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.3 |
| 51550e1a-b73e-336c-a7b7-01166b1b5bc1 | -20.2533 | -55.5172 | 2025-09-22 01:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 2b851ea2-089d-39c4-afbb-ab323d1adb0b | -11.8626 | -64.9332 | 2025-09-22 01:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 691da8af-d79c-39e9-9d6e-ee091f4bf8c0 | -22.8326 | -50.5973 | 2025-09-22 01:20:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.8 |
| b4832f4f-9119-38a3-9ad5-860b225428ec | -20.2537 | -55.4959 | 2025-09-22 01:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 48b4bb74-e11a-3250-9733-43ed5c444d4e | -22.9285 | -47.4219 | 2025-09-22 01:20:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.1 |
| 9d30bf74-5268-32fe-9757-e98fabae4bfa | -22.9255 | -48.1819 | 2025-09-22 01:20:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 98.0 |
| a17ff85a-f06b-3acd-acf9-7276d36694dc | -4.3012 | -48.0917 | 2025-09-22 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 016028c5-28d6-3ad9-9b70-d55ffc91bdfc | -22.9044 | -48.1873 | 2025-09-22 01:20:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 2fa40f9d-e7f5-30b9-b5ad-fb1b96904517 | -6.9024 | -44.7656 | 2025-09-22 01:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| deba8a1f-26e5-3552-84c2-503b00dd0d60 | -11.6439 | -52.8397 | 2025-09-22 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 39b426c2-cfdd-37fb-8a8e-43df1d3f6c46 | -22.9278 | -47.446 | 2025-09-22 01:20:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| baf581e9-2b31-39f1-93dc-86f23fad6a79 | -20.274 | -55.4927 | 2025-09-22 01:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 641fd7ee-9944-37f6-9004-e18995531094 | -11.8626 | -64.9332 | 2025-09-22 01:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 93a89b18-82f1-32a5-89de-3c2d980a04cc | -20.274 | -55.4927 | 2025-09-22 01:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 46567b68-3761-36a1-8f67-32376e2c923b | -21.2095 | -48.833 | 2025-09-22 01:30:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.0 |
| 9aa71775-d895-322c-924a-7b76e02fc18a | -22.9075 | -47.4275 | 2025-09-22 01:30:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.6 |
| 9f2cb597-4e4d-32c6-bcf6-c2638e5bf832 | -11.8814 | -64.9323 | 2025-09-22 01:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e7f943f5-704b-3fb3-a46a-38ab64ee82a9 | -11.6436 | -52.8605 | 2025-09-22 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| f0e0cd12-bada-38bb-98d1-af4480d5059d | -22.9285 | -47.4219 | 2025-09-22 01:30:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 142.6 |
| 24963c9b-f6e7-3c1a-a33f-844c36a61c34 | -22.9278 | -47.446 | 2025-09-22 01:30:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.0 |
| 05ed6c86-57eb-3842-bc8e-ce19b91dfb7f | -22.832 | -50.6203 | 2025-09-22 01:30:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.3 |
| 17059de9-f734-3238-babb-2cdddaf09412 | -11.6439 | -52.8397 | 2025-09-22 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| ea2456b8-1dd4-3449-b43a-b90371faa1af | -20.2533 | -55.5172 | 2025-09-22 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 863c1897-e10d-306c-85b2-69ea00f2a042 | -22.8529 | -50.6155 | 2025-09-22 01:30:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.3 |
| 62b711a8-e1f4-336c-8d1e-94df23c0e1a2 | -4.3197 | -48.0908 | 2025-09-22 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d94af0bc-c404-3bac-9d25-4b2151aca693 | -20.2537 | -55.4959 | 2025-09-22 01:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 3b8d3ca3-ebc5-340f-aee0-fc673230b493 | -22.8326 | -50.5973 | 2025-09-22 01:30:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| 82110589-65ef-34c6-a410-5803e12c6855 | -20.2735 | -55.5141 | 2025-09-22 01:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d15d1d57-39e2-34f0-9631-194066334d04 | -11.6247 | -52.8624 | 2025-09-22 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| c67fd48c-de49-3dbc-88f6-53ef3e434b1e | -22.9075 | -47.4275 | 2025-09-22 01:40:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.0 |
| 92d26de3-02d9-3dc6-829a-d04bde3c0daa | -11.6439 | -52.8397 | 2025-09-22 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| f8694fb5-fc9c-3f33-9dde-6f11977d7137 | -11.8626 | -64.9332 | 2025-09-22 01:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 327836ee-045a-3931-8df9-fe92b8fd9989 | -6.884 | -35.1765 | 2025-09-22 01:40:00 | GOES-19 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 87.4 |
| 07d78b1d-fac1-3cf1-a039-2e97aafb3bb8 | -22.9285 | -47.4219 | 2025-09-22 01:40:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.5 |
| 5fb3680b-40df-32d1-8fb9-75e1a119441c | -21.3367 | -48.688 | 2025-09-22 01:40:00 | GOES-19 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| 0bdefb90-fe22-3d82-b884-74373c00cbec | -6.9024 | -44.7656 | 2025-09-22 01:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4fac27d6-87ce-362f-9efa-571c56c6eba4 | -22.832 | -50.6203 | 2025-09-22 01:40:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.9 |
| 3c56179d-06de-37f7-a543-283369040338 | -11.8814 | -64.9323 | 2025-09-22 01:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 79c93087-ef87-3ce4-862a-5cd1321b1a6f | -11.6249 | -52.8416 | 2025-09-22 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 0e6fc3af-8e98-340a-a30d-618a291abaa2 | -22.8529 | -50.6155 | 2025-09-22 01:40:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.1 |
| 873ebec3-519b-320e-822e-3e872bbcfe86 | -11.6436 | -52.8605 | 2025-09-22 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 8706e0ae-cc91-32be-9081-6f5825d17369 | -7.3556 | -44.5415 | 2025-09-22 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 8edd2951-7bc3-3048-a61c-a44627a6074b | -20.2537 | -55.4959 | 2025-09-22 01:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 36b3e52c-6230-36e2-93ae-48354c427e7b | -7.3742 | -44.5628 | 2025-09-22 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| d755f160-c6f8-3c58-9990-a5b67c0c3dc8 | -20.274 | -55.4927 | 2025-09-22 01:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 76.1 |
| e2017e54-7f85-30a6-b687-1bf4386a4fa9 | -6.8836 | -35.2039 | 2025-09-22 01:40:00 | GOES-19 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 63.5 |
| 98a023f8-56fb-37c3-a392-48899a3673fb | -19.6447 | -57.73811 | 2025-09-22 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.8 |
| 05c6d380-6651-3c39-9f9d-a1bb3806641a | -19.635 | -57.73372 | 2025-09-22 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.5 |
| 8e25fd63-1968-3d5d-9b24-befe5445eb6f | -19.63079 | -57.74111 | 2025-09-22 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.0 |
| 4f2fc800-a124-3190-9d4d-6adba5961757 | -15.96601 | -59.39347 | 2025-09-22 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| f419f09f-7ed3-3322-b78b-e2986d719221 | -15.84351 | -59.51447 | 2025-09-22 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 053bb0cd-3ff3-3f15-bf41-eb0d7edd1abf | -15.9533 | -59.37767 | 2025-09-22 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 20c9b1ef-be13-3909-9f4d-2c396d60f68f | -15.96188 | -59.37019 | 2025-09-22 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 258d0969-34e0-38cf-9f90-f5cce319aa72 | -15.82853 | -59.58424 | 2025-09-22 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b9e0280a-73ac-353f-a00d-84a2d37108f9 | -15.96655 | -59.375 | 2025-09-22 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 808922ea-9d60-3dd0-8ae9-50ef0fa0324d | -15.99457 | -59.47791 | 2025-09-22 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8dbed3bd-d131-33fa-9895-39041383530f | -15.95273 | -59.3958 | 2025-09-22 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 2df7a75a-a391-323d-b9be-0cd443995272 | -16.00413 | -59.45483 | 2025-09-22 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| e51e53c5-ab8c-3187-807a-416b40e4bf0e | -15.95722 | -59.40067 | 2025-09-22 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 9b7cfac5-e691-3ad2-8d69-2dfb2af5a4c9 | -15.83045 | -59.51762 | 2025-09-22 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4e6733e3-1b3d-3837-84dc-6ed1db66f141 | -11.84799 | -64.93745 | 2025-09-22 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 558395e8-a6ac-3808-8e0f-5b1485f76168 | -11.87235 | -64.93856 | 2025-09-22 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 5b3be52a-42eb-3cd2-a234-e57981c61351 | -11.88185 | -64.93708 | 2025-09-22 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e89dcab5-d8a9-341e-a24c-e7494b1f1049 | -10.6713 | -69.103 | 2025-09-22 01:49:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef99c78f-bb97-36ab-a5b6-2d03f4c0ba16 | -10.43395 | -61.33498 | 2025-09-22 01:49:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 9cc0e7ba-bc9d-3f1c-a74e-af917e18c350 | -11.84953 | -64.94797 | 2025-09-22 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 58bb4c77-1612-3095-a930-46cc24bff8e0 | -10.92474 | -68.59003 | 2025-09-22 01:49:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 16.3 |
| a275a0ff-8eaa-3f17-b8e2-69de7fa4fac7 | -11.88342 | -64.94759 | 2025-09-22 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f70f3be4-e9ac-3bf2-8b2a-dc7ef612f0c3 | -10.91583 | -68.59129 | 2025-09-22 01:49:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b658186b-4397-30a4-97fd-8d9d7d979968 | -11.88028 | -64.92656 | 2025-09-22 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7a0798e1-50ac-396a-8fea-aff4f41acb21 | -11.78938 | -64.93578 | 2025-09-22 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ae027aab-6129-35c3-887d-9f00ebf6e3ea | -10.63539 | -69.04122 | 2025-09-22 01:49:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 550d60b9-e2c1-33bd-a7c2-6742317438c9 | -10.86522 | -68.28416 | 2025-09-22 01:49:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac804874-475b-38e1-a476-0cd7e794278d | -11.85749 | -64.93595 | 2025-09-22 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e9298ced-6c33-35a6-89a7-ecc4301b4d87 | -10.43708 | -61.35453 | 2025-09-22 01:49:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 857e8dd2-31b1-323f-9316-4cfb375948d8 | -10.85575 | -68.55921 | 2025-09-22 01:49:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 1001b572-d444-338a-91e6-cf51e3e64109 | -11.87078 | -64.92804 | 2025-09-22 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d76c74b6-7db1-3602-987e-0b267784f13b | -11.78782 | -64.9253 | 2025-09-22 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |


[Clique aqui para ver as próximas entradas](README7.md)
