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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c0e0b90-243e-3990-8060-bf62ccea3fe7 | -19.881901 | -45.0336 | 2025-09-07 00:45:00 | METOP-C | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 283318b2-d869-3289-b063-b9174dd0784b | -6.8196 | -52.8046 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1ad760-c0b8-3057-9e97-455afc65fe8e | -8.6703 | -47.457699 | 2025-09-07 00:45:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e427e140-86cd-3402-98a9-ba19b9de7d0b | -7.2307 | -43.864101 | 2025-09-07 00:45:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa64bf83-b57c-3b31-85f6-f2760ae5da70 | -8.1778 | -44.7971 | 2025-09-07 00:45:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7817f68f-9257-32a8-9791-b94356ca54a0 | -13.1091 | -44.847 | 2025-09-07 00:45:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f10ab82-82df-30d5-a55b-ed5f58b43de6 | -12.9422 | -54.800701 | 2025-09-07 00:45:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5225fc7f-7ee5-3499-98d4-7d8708a96b98 | -6.8244 | -46.405102 | 2025-09-07 00:45:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae19ef74-4653-31fb-b724-3a6554d5a9a1 | -6.2176 | -43.299599 | 2025-09-07 00:45:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e59e967-6f8e-3735-b694-392423b47d54 | -7.7463 | -48.821999 | 2025-09-07 00:45:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 34233a1d-ab64-3fd8-88e7-bc860d9e8dfb | -7.7538 | -50.766399 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87e40310-81b6-3261-8ab5-71ec0f355b6f | -6.1808 | -53.257999 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee23df0-de18-33a5-bc7b-6116caefaaa0 | -7.7236 | -48.812801 | 2025-09-07 00:45:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| cdb315cb-5f37-3983-8de0-969c4ee94691 | -13.8173 | -46.279499 | 2025-09-07 00:45:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b3dd46d1-931b-3d17-8ef3-37e90b142d19 | -6.1926 | -53.2649 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5e64fe-354d-3fe2-85f5-a31097cf377e | -21.698299 | -47.208302 | 2025-09-07 00:45:00 | METOP-C | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05c3ee5b-56b4-3ab0-89cb-71430ecd8ca9 | -6.7159 | -50.4557 | 2025-09-07 00:45:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9418983-389f-30b2-bb24-8f00c04cd570 | -16.2838 | -45.691299 | 2025-09-07 00:45:00 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2a49a116-4c21-3975-a4b6-23b27941b27d | -6.1886 | -53.246899 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a912c1-1c48-33c3-81d7-af5aeca48782 | -6.2576 | -43.507301 | 2025-09-07 00:45:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d3e5781-4db8-331b-b4e0-60366dcdeac9 | -7.7479 | -48.828899 | 2025-09-07 00:45:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 89cef977-2168-3b92-bb67-d87f9385a6be | -6.2547 | -43.495399 | 2025-09-07 00:45:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d85d4c65-7cd7-3b1b-a9b5-8a04945f9279 | -6.8273 | -52.839401 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd74868f-2172-37c8-abfc-69aedb7a39c8 | -8.6965 | -47.883598 | 2025-09-07 00:45:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56d9b9b2-6a9b-32cb-9593-d8535f0b8662 | -18.682301 | -44.448002 | 2025-09-07 00:45:00 | METOP-C | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| baade8ac-458a-3137-a7c6-23a67b24e544 | -14.7994 | -48.110802 | 2025-09-07 00:45:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1ccb5c15-5a42-3d0e-bf9c-417510ecc2cd | -14.5568 | -43.724201 | 2025-09-07 00:45:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3819140c-d920-308f-9fe9-04f731623ae1 | -5.6654 | -45.429298 | 2025-09-07 00:45:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 423b0b9d-6369-3c22-b553-d9c9d1d8aeb6 | -11.6159 | -47.162899 | 2025-09-07 00:45:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ac27a49-bc06-373e-ab8b-a6432e78ba45 | -5.7522 | -45.534599 | 2025-09-07 00:45:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7066db7-f7ac-3578-b13b-a8ef78a5ed8f | -11.8335 | -47.571701 | 2025-09-07 00:45:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c8da55e-2d09-37da-8d29-d51afa6beb13 | -3.4 | -50.287701 | 2025-09-07 00:45:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecedda30-c2ac-3cd2-b781-75ee6ed1c058 | -7.6702 | -50.302502 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49c2d56d-4842-3a86-9935-392f7b712203 | -13.7541 | -52.778801 | 2025-09-07 00:45:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9b7d205-8c9c-3e26-b7a5-bc8e7ba24f10 | -10.7775 | -47.735401 | 2025-09-07 00:45:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae3907b9-2884-34ef-b272-2e30ad23ad34 | -14.5894 | -48.091999 | 2025-09-07 00:45:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 94478e56-1a44-3da7-bd6f-2ffa533508a9 | -11.8221 | -47.567001 | 2025-09-07 00:45:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66101ac8-c5c6-3954-8c3d-d626332d78ac | -14.7979 | -48.103699 | 2025-09-07 00:45:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d6b20d23-f843-3483-8818-4ed89db71638 | -8.6694 | -54.670898 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97074795-6a61-3d59-ba28-2775ec77b87d | -5.9848 | -44.172798 | 2025-09-07 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f76bb258-afa7-34f1-acbb-48bf5505c204 | -11.5816 | -47.733101 | 2025-09-07 00:45:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11487e27-cb71-3ab6-aadc-9a44569f9c63 | -16.772499 | -51.369099 | 2025-09-07 00:45:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e894b3dc-6012-3155-b972-f5891e19702f | -14.8416 | -46.694302 | 2025-09-07 00:45:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b61243cc-d30d-32ab-81b0-aa3eccb12cc0 | -9.9757 | -51.6567 | 2025-09-07 00:45:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0036d79-8dd3-3fc5-a16e-e70fe48cbf1c | -11.159 | -49.933102 | 2025-09-07 00:45:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e738762-f20c-3a5d-b6db-488be6ce9226 | -6.7687 | -52.806599 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76bafb32-59f4-3b04-b51a-03da7a31c624 | -15.5298 | -42.662201 | 2025-09-07 00:45:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 121f25cb-2db2-38e0-884e-a0d3d397a91c | -11.4699 | -55.555099 | 2025-09-07 00:45:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3eb5453e-298f-3deb-abde-37a2deba40e8 | -6.5463 | -42.955101 | 2025-09-07 00:45:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26cff882-5ff8-30f4-bdad-de259736354d | -11.8607 | -50.743301 | 2025-09-07 00:45:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ee69cfbf-fc30-36f5-af6d-8f1f58bb3617 | -22.405001 | -47.447102 | 2025-09-07 00:45:00 | METOP-C | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 688761d2-115c-3658-9e3a-4fe4704f4d3a | -5.9741 | -49.956799 | 2025-09-07 00:45:00 | METOP-C | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0b2f7c1-4681-30d0-835a-23f2474ec140 | -12.6037 | -44.6357 | 2025-09-07 00:45:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3bd8d998-3cd7-3da5-b727-9c6fec6af303 | -6.2952 | -51.4212 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5cc2f36-31dd-3f1e-ada9-01711d273438 | -4.1738 | -42.040001 | 2025-09-07 00:45:00 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3722a212-1346-36fe-a32f-9cd2c8d2d7af | -6.8293 | -52.848099 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3dc4c08-c96d-394e-b384-f9bf50ef8273 | -6.8216 | -52.813301 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 519dfde2-c640-32be-901c-963cd6db884d | -10.7273 | -48.601601 | 2025-09-07 00:45:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c9051a2-337a-39ff-b328-bca8aa0da89d | -9.4467 | -57.320801 | 2025-09-07 00:45:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20d70633-2caa-3927-ba88-c509cbfb3671 | -11.396 | -43.617599 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59cf5c7b-4295-39ff-9518-317c6a3a9706 | -10.5735 | -48.469002 | 2025-09-07 00:45:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d180b6cb-aa7c-3901-aaa8-ed262274ed96 | -8.6608 | -50.036999 | 2025-09-07 00:45:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f26f58c7-cead-3d33-82ed-3976251bf49a | -11.8142 | -46.7701 | 2025-09-07 00:45:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98ec40b2-b77c-346d-9c97-0c3867abb053 | -7.7457 | -50.73 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38bc7e15-5ae2-38b9-91c3-43e2e25968fd | -6.2117 | -42.469898 | 2025-09-07 00:45:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 00d3dec3-82d3-3b2e-9a56-a2aeb11f3383 | -8.6669 | -54.659 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7bee967-5814-340e-ba16-bced241ac70a | -3.3153 | -54.907299 | 2025-09-07 00:45:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2857f735-3c5e-3880-b9f0-d800d7780e0e | -8.5304 | -51.343102 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d8c0dce-e038-32fd-8faa-6a39a2442622 | -6.8079 | -52.7981 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e0afa59-a545-38a0-b8e5-b6bdb03c6ca6 | -18.684099 | -44.455799 | 2025-09-07 00:45:00 | METOP-C | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b5c3adf9-8f29-384f-83c0-6fa3e6c47405 | -13.8531 | -46.2556 | 2025-09-07 00:45:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eeedc58c-328d-38f8-b096-6ed2b724290b | -6.2274 | -43.297199 | 2025-09-07 00:45:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 562c60d4-de46-31fe-acde-c78c60e45da7 | -5.6894 | -49.2075 | 2025-09-07 00:45:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1185c16e-39b9-333c-b52b-08095c33b7b9 | -17.6625 | -43.550701 | 2025-09-07 00:45:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2098dfe5-d385-3287-83c0-fc11b0f50766 | -5.7204 | -43.930099 | 2025-09-07 00:45:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 778985fd-c0d3-3e6c-9d70-764b677fa257 | -8.9236 | -48.648899 | 2025-09-07 00:45:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3b126207-79fb-3d91-8057-6aa4d71a9820 | -22.760099 | -51.311901 | 2025-09-07 00:45:00 | METOP-C | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 67d19249-4868-33bf-b573-d79d208574b5 | -2.0665 | -47.1455 | 2025-09-07 00:45:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8268eda-5e38-3d9e-9f3f-767459ebe45b | -6.14 | -44.2612 | 2025-09-07 00:45:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81b01628-2378-35a4-8b36-32df6718f067 | -7.6734 | -50.3167 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf6377d-8706-3713-afbd-57e43da9cac4 | -8.9074 | -45.823502 | 2025-09-07 00:45:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b408374b-5fc1-3c33-8a1f-ea196ec29415 | -7.6246 | -46.559299 | 2025-09-07 00:45:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 915cf7e7-0089-3af2-b4c9-8bca0c116b02 | -13.8157 | -46.272301 | 2025-09-07 00:45:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 88e6f2f4-963f-37fb-912f-1e9eb41d2875 | -7.7448 | -48.815201 | 2025-09-07 00:45:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4a2af7e7-d3cb-3f41-b66f-7948eaba5f03 | -5.683 | -48.149601 | 2025-09-07 00:45:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 31cf1ad8-e4ea-3ba3-bc85-9c4d28ecaf87 | -11.8358 | -50.5345 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c5d91ee-20b9-391d-bf3e-cb2c84b1eb1c | -16.3251 | -52.958199 | 2025-09-07 00:45:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da3592f5-edf2-3620-aaa4-0ecd7690cb84 | -3.2302 | -50.8078 | 2025-09-07 00:45:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acb71aab-c00b-3ed1-8ed7-75b5f2cf9fc2 | -11.7664 | -50.6399 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f908a70-da0f-3a0b-b5ce-c4088435e95c | -9.7037 | -49.499599 | 2025-09-07 00:45:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d23c1ec3-7b8e-35ad-9455-eea5249787ce | -9.9801 | -51.629799 | 2025-09-07 00:45:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1b6ce18-2f60-312d-bb96-f0e7ba356520 | -7.724 | -50.312901 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d98b8f2c-042c-32c3-839e-d62049f13a23 | -11.379 | -43.547901 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 335866ff-b3ca-3101-bac3-0ab6696fda5f | -17.683599 | -44.5117 | 2025-09-07 00:45:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 03c1e8c3-7251-3cee-a0d0-60e1b435adfa | -11.7774 | -50.596401 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9d2323d-14bc-3489-ad8d-3cb8b5b1e804 | -13.7095 | -46.887699 | 2025-09-07 00:45:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 42b7d13e-5534-3d91-893d-dfac45e2af17 | -5.855 | -46.057098 | 2025-09-07 00:45:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c75604ee-359c-3054-84ca-2d2634789b4f | -14.4336 | -48.457401 | 2025-09-07 00:45:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 05de00ca-55ae-39d7-84ab-dbb51b6e9e3b | -6.2236 | -43.3241 | 2025-09-07 00:45:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e392aad9-fe6d-3ce7-9884-925b31c88ea0 | -5.9796 | -44.151001 | 2025-09-07 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README11.md)
