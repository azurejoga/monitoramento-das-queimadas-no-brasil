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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 377bf77c-1838-3ce2-920a-90e82d2642bc | -5.8612 | -43.8858 | 2025-09-30 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 863f6850-837b-3a29-9d6a-0793e96905d5 | -9.1434 | -47.6457 | 2025-09-30 13:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 18f37b69-5edd-35c3-95d0-f603e77a0898 | -9.1246 | -47.6476 | 2025-09-30 13:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 4ea9d4b6-3551-35b9-970d-d1fb2e8ceff5 | -14.3847 | -47.1486 | 2025-09-30 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 196.8 |
| ce1a9318-70ff-32f5-8a4d-ecb0e9aa3275 | -8.672 | -47.7144 | 2025-09-30 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b0758209-e621-3aa2-bb98-1a35bece8e70 | -12.2156 | -47.7889 | 2025-09-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 07d9f44c-6c42-3dbc-b483-1a7b9c46af23 | -9.0425 | -46.7032 | 2025-09-30 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| cc47e4c8-cae8-35d8-a7e6-a8296e514576 | -14.4041 | -47.1454 | 2025-09-30 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 41ebb663-2f14-30cf-a86e-400f96b9ea21 | -5.4752 | -43.054 | 2025-09-30 13:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| d7f330c7-2b4f-32bc-8804-008bd1007772 | -9.7681 | -46.1519 | 2025-09-30 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 567e3cdc-85be-34a1-af15-39be3da74156 | -7.9191 | -44.6245 | 2025-09-30 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 0913f0b8-38b7-30aa-8e55-07811e090ea1 | -9.8221 | -49.1038 | 2025-09-30 13:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 33f31ab8-389b-3511-ab5a-a029888d7908 | -14.7171 | -45.2291 | 2025-09-30 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| b6c0721d-494e-3026-8353-aee95b4d8108 | -15.7719 | -43.6714 | 2025-09-30 13:30:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 7a833475-df76-3d6b-a8f8-a2da1cccfc18 | -12.2344 | -47.8086 | 2025-09-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 0db79b49-b240-3cc7-9f03-0c5d3f54877c | -8.1428 | -46.3693 | 2025-09-30 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 9bb3ae17-defc-3ae8-b2c4-48be2b866583 | -13.8354 | -47.5076 | 2025-09-30 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 81f5358f-6e94-37f8-8680-4a27415daae6 | -8.9287 | -49.8348 | 2025-09-30 13:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 3839c5ba-ded3-39fd-a73e-3f2eb13e5c66 | -10.7482 | -45.3713 | 2025-09-30 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 34605d4d-d989-3617-9a6d-3d1b6ffff210 | -7.115 | -47.785 | 2025-09-30 13:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 2441bb12-92a6-3ca6-8be6-db9547755a32 | -7.0181 | -44.4807 | 2025-09-30 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6340c9b7-c736-32ad-882e-fcdb8094cbd4 | -18.218 | -53.2962 | 2025-09-30 13:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 182.1 |
| b3d165ec-eb2a-3a53-9f25-71fb18d33bc7 | -12.7022 | -45.2715 | 2025-09-30 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 3a0eddcc-f138-381a-9486-f497632c0a4b | -14.5323 | -48.4938 | 2025-09-30 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| d65a1e6c-6db6-3472-b723-c68e88939f29 | -10.1045 | -47.7851 | 2025-09-30 13:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 18a0dcc2-4d2a-3244-8eae-431be685fb06 | -15.9273 | -46.2101 | 2025-09-30 13:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 3bd0e00e-4d22-3e46-be4c-8e98a924a652 | -7.8348 | -47.0207 | 2025-09-30 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| d74c8f27-5eb8-36e6-8dd3-6ff86b5aceb0 | -18.4862 | -44.0191 | 2025-09-30 13:30:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 182.2 |
| f040e37e-7f13-3cce-a6de-7146a717f884 | -8.7331 | -47.334 | 2025-09-30 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| aed504d0-d6eb-336a-a3e9-d2686978d892 | -11.071 | -47.8262 | 2025-09-30 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| ef5573d3-58e6-3dbe-bc3c-2bebe8fe0559 | -14.5517 | -48.4907 | 2025-09-30 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 78bdcb3c-79f0-3f38-8fab-41f1fc87e82d | -5.7411 | -42.6812 | 2025-09-30 13:30:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 186.5 |
| 924d41e8-cfa5-3282-8b14-728423cefed2 | -9.4005 | -54.7186 | 2025-09-30 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f1903ee7-a85d-307b-be4e-49f57e56665d | -10.0342 | -50.1997 | 2025-09-30 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 7c99d442-8865-387b-9bf7-d719938a02d9 | -14.7166 | -45.2525 | 2025-09-30 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 350.4 |
| 39521afa-8a29-3ac5-92a9-178e774fbe20 | -7.1193 | -45.5417 | 2025-09-30 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dbcb6dd0-0214-3f33-8745-d01ef5131e47 | -10.0528 | -50.2192 | 2025-09-30 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 597c34c9-d0dd-3009-bcd3-2f8d9a161d9e | -13.8264 | -47.9794 | 2025-09-30 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 91726acc-56f8-32c0-9bbf-007ee6ce8ff7 | -10.6419 | -48.6021 | 2025-09-30 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 8dd4af80-833e-39b0-8b37-3c4e78f6e9ff | -10.0339 | -50.2211 | 2025-09-30 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 1a5b84ad-8f4d-3bb1-bba8-97e1841ea754 | -7.8375 | -46.7766 | 2025-09-30 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 596909aa-7632-31ca-810c-b9ff9e72e31c | -14.5141 | -48.4299 | 2025-09-30 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 437dfa14-e8a9-3c8d-878d-affd396d393c | -10.6423 | -48.5802 | 2025-09-30 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| b5c1b99b-15be-3a0c-8653-43cdfef2bf40 | -7.8188 | -46.7783 | 2025-09-30 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 04e6f13a-6704-319e-88bc-363b8110c94c | -11.7537 | -46.8461 | 2025-09-30 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 09c5acb7-2973-3f03-95f7-54cc60d20a81 | -10.0717 | -50.2173 | 2025-09-30 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| de993d8e-3fc1-3cca-b4bc-6de19cb15cf5 | -7.938 | -44.6226 | 2025-09-30 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 62290b35-c86e-31cb-87ff-9d29b71672e7 | -8.1616 | -46.3675 | 2025-09-30 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| a7ee455d-1fee-3c07-b31e-808bf4757f3d | -13.7368 | -48.6372 | 2025-09-30 13:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 50c2ec27-4b0e-3ac6-80c5-ce55232732dd | -6.504 | -45.2312 | 2025-09-30 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| c2591c86-b0b2-3734-a3b0-3e8a18f4d8b5 | -12.2153 | -47.8112 | 2025-09-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 4b9cb222-5251-3bf5-b183-93d3dba803af | -7.8378 | -46.7544 | 2025-09-30 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 7fb9c51d-33f6-3cea-81bf-93e67e2f6ba4 | -9.1248 | -47.6256 | 2025-09-30 13:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 6bab86c3-8294-39fc-b0b3-b01259ea1ee9 | -15.2746 | -49.263 | 2025-09-30 13:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 84146abf-b3b9-3c55-b8f7-ff90115a7ff5 | -5.475 | -43.0774 | 2025-09-30 13:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 45c4f73f-5921-383b-90ec-f96c0b7dd0c0 | -7.9194 | -44.6016 | 2025-09-30 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 93f751cc-bead-33e8-b1ff-6cd0c0555daa | -7.835 | -46.9986 | 2025-09-30 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 175.3 |
| e8591b26-552a-3d42-8aca-8db082986678 | -18.2176 | -53.3177 | 2025-09-30 13:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 453.9 |
| e8fd8688-7f82-3f2e-8233-3f9527414ef1 | -12.2348 | -47.7863 | 2025-09-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 77bf748c-4ad0-39cd-9bc0-8f8f45b66116 | -9.4007 | -54.6984 | 2025-09-30 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 14803b14-23f1-3f5d-bf55-29bb3e71a1d2 | -13.7319 | -54.7307 | 2025-09-30 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| c6e1c6b6-8594-338b-9d6b-a1cdccaad6b4 | -6.098 | -42.6521 | 2025-09-30 13:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 3b1e0e3d-19f1-3ee9-b99a-cd7c310f6063 | -12.7018 | -45.2947 | 2025-09-30 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 796ae8e5-5288-36ad-9fde-d2370e7345e6 | -11.1546 | -54.126 | 2025-09-30 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 8af9bad7-86eb-301e-9ce8-7beb5e8ec643 | -12.8774 | -45.1742 | 2025-09-30 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| c50516e0-bd5c-30e2-b22a-8b46303da58b | -11.1735 | -54.1242 | 2025-09-30 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 23d2417b-cab3-3d4f-b6e5-777682bc59ae | -12.952 | -48.4185 | 2025-09-30 13:30:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3159ede9-3946-3507-83c5-cb0113d18603 | -6.0978 | -42.6758 | 2025-09-30 13:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| e6b829b0-dbe0-3b91-9774-321fb9db12a9 | -15.9268 | -46.2334 | 2025-09-30 13:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 112.7 |
| d58f09a9-eefe-312c-819c-67e430966c7f | -7.2996 | -42.8722 | 2025-09-30 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.8 |
| 627b0877-743f-3ca4-8282-daa159e9757a | -14.6603 | -46.9663 | 2025-09-30 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 144.4 |
| d66183bb-5c19-349a-997a-05b84d1b17d7 | -8.541 | -44.6515 | 2025-09-30 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 4babd2d1-60ad-3b84-90b3-7b0d1bdff968 | -10.1851 | -44.8939 | 2025-09-30 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 377.2 |
| 133bab9f-d732-3508-b740-01e03b447c30 | -9.1105 | -45.8426 | 2025-09-30 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 2c765ab9-9b79-3548-8abd-9b02f71d9b94 | -10.1855 | -44.8709 | 2025-09-30 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 5489160b-a61e-3306-af03-c6fec86c8d0c | -12.3867 | -50.1731 | 2025-09-30 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 20414b69-ca8a-3e65-bddb-bdbe52e5f68a | -5.4752 | -43.054 | 2025-09-30 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 496fa957-e3d1-3049-a436-be0c9d3f9310 | -12.8774 | -45.1742 | 2025-09-30 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 3602fa92-adb1-3ef0-9732-76d2462e3c1e | -10.6423 | -48.5802 | 2025-09-30 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| b2536488-21cc-30a4-a1be-58e7a5337c0e | -12.8429 | -47.0063 | 2025-09-30 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3c71fbe1-9390-3308-befb-9b894795c549 | -7.835 | -46.9986 | 2025-09-30 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 248.8 |
| 4fdaab10-156c-3cab-8164-a68f62325f84 | -14.4041 | -47.1454 | 2025-09-30 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 0e263428-9478-3d71-bd4d-6c4ce1260820 | -10.0714 | -50.2387 | 2025-09-30 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 2173e139-ec9d-328d-b87d-1715551c24af | -15.9268 | -46.2334 | 2025-09-30 13:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 318.4 |
| 2a793cfb-fe5f-346d-a0f2-1b55b732852d | -7.0481 | -45.1856 | 2025-09-30 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 6346c840-f49a-388c-a781-1b1475bba971 | -5.4565 | -43.0554 | 2025-09-30 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 1843d0e3-81df-3d1b-a7f4-25766da0b45b | -11.7537 | -46.8461 | 2025-09-30 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 99f191aa-bc44-3af0-9b34-f956db5e9391 | -12.863 | -46.9582 | 2025-09-30 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 36a0245c-f299-333a-9b40-f0cda0bb6ffe | -5.6815 | -43.0384 | 2025-09-30 13:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 177cfa01-5d5b-337b-9175-ea03a4b1c1e3 | -10.1045 | -47.7851 | 2025-09-30 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 97d0fc9c-2e0c-33de-8bad-e6883e2b2a8e | -13.7502 | -47.924 | 2025-09-30 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7a63ee0f-42a1-314e-80b4-26e163979b69 | -11.1546 | -54.126 | 2025-09-30 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.0 |
| 05f6f745-9dc5-3f64-8b5f-559363d23c86 | -18.2176 | -53.3177 | 2025-09-30 13:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 286.7 |
| cd26f1f1-201a-3343-bff8-0ddd0f9ed79f | -5.8615 | -45.9551 | 2025-09-30 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 26a1c7c1-4480-3bf6-ba2e-98551476ba5b | -13.7319 | -54.7307 | 2025-09-30 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| fe461925-9a76-3651-9281-84a2fb9e6495 | -8.8357 | -46.6578 | 2025-09-30 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 9043f3b7-75c6-38b2-ace7-70f32ab8a3cc | -10.1855 | -44.8709 | 2025-09-30 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 96321151-24bc-31af-b708-9ab7e2591828 | -17.9016 | -57.577 | 2025-09-30 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 8e217de3-b316-3b34-8075-55c9c1dd21c9 | -8.1428 | -46.3693 | 2025-09-30 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1b8a546c-b882-304c-9167-a92e77888bf4 | -11.1735 | -54.1242 | 2025-09-30 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |


[Clique aqui para ver as próximas entradas](README116.md)
