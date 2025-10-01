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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b8ffc21-61ba-34d1-b59e-aa043ffcfa1f | -12.254 | -47.7837 | 2025-10-01 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 0aa2183c-bbc1-3f37-93d7-4cffda715376 | -11.4596 | -45.0433 | 2025-10-01 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 268.5 |
| c3a1fb84-9f5c-3432-bd31-1b23c93369e6 | -14.4938 | -48.4776 | 2025-10-01 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a4726c26-957e-3d7c-a7e7-e4912e4cf769 | -15.9381 | -43.3223 | 2025-10-01 13:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 674.5 |
| 7e16a2e2-039c-364a-9c09-31f61f8d7d91 | -14.8026 | -45.7713 | 2025-10-01 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 824f6e2a-b5ca-39f7-9ebf-51e78e714ce5 | -9.9391 | -43.6012 | 2025-10-01 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 525b210e-61fd-3f76-a5d5-1c0e3ba1707f | -8.4833 | -47.7763 | 2025-10-01 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a089b0e0-2a5f-3d4c-a756-3af7e5fb89cf | -11.4409 | -45.0229 | 2025-10-01 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| ee61314e-381f-31f5-a562-5a4f711caa63 | -10.0906 | -50.2154 | 2025-10-01 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3a5de750-0862-3b7a-91c1-2271d1d6a2c1 | -12.2344 | -47.8086 | 2025-10-01 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e5d436dc-0fbb-349a-b9cd-4ce4cb343a55 | -8.6908 | -47.7126 | 2025-10-01 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 440a4f26-6d0d-3134-9501-be0181c02b26 | -14.8021 | -45.7946 | 2025-10-01 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| f0ffab7b-cc06-30d3-b139-c6a6da19d657 | -15.3928 | -49.1998 | 2025-10-01 13:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 8a63375f-6030-3049-acf4-1e533caaf375 | -12.7002 | -48.5637 | 2025-10-01 13:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| c3210e94-7c92-317d-8b53-54d5ca57748d | -10.0909 | -50.194 | 2025-10-01 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 5aac6dcc-9de1-3250-b3b3-a146cde17a7c | -13.7691 | -47.9435 | 2025-10-01 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 6a043d3b-5e13-371f-af9e-1a49d2b467fd | -11.6126 | -45.0443 | 2025-10-01 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 177.3 |
| bbe5f5ba-0feb-3f2d-a293-115c1c513afb | -9.9193 | -43.6508 | 2025-10-01 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 9f7ef370-b0ca-318e-be2b-915780e31e1d | -14.3524 | -45.8974 | 2025-10-01 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e17541ad-7fb0-3401-9595-f5b234af4202 | -9.4647 | -47.5903 | 2025-10-01 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 2a475c4a-fc2f-3d0b-9057-fc667fffffe7 | -8.5267 | -47.2879 | 2025-10-01 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 6df43222-474f-3f72-8ea9-1ad9890de76b | -13.2969 | -50.6821 | 2025-10-01 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ceab0e02-3c42-3337-8ca3-8439ae591b79 | -15.1786 | -46.4184 | 2025-10-01 13:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 89020e4a-b28c-3e09-87dc-dc653a27d1bb | -13.7868 | -48.03 | 2025-10-01 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 98befed8-4ca3-3f79-b7a7-39708e62c7f0 | -8.8609 | -47.6521 | 2025-10-01 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f05bd709-1cb9-3626-bc77-2d6d1b8310fc | -8.5587 | -44.7414 | 2025-10-01 13:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 55411fa2-4c69-31b0-8b07-f5cf7c1589a0 | -9.9186 | -43.6978 | 2025-10-01 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 198.3 |
| a1264de5-f9f0-38c2-b6f5-45261122fc41 | -15.9388 | -43.2979 | 2025-10-01 13:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 433.7 |
| d28ae6ec-4150-34b3-9992-5f25c6fa95fd | -6.943 | -41.113 | 2025-10-01 13:00:00 | GOES-19 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| a7d83d08-b7bb-3ebe-ac19-bb9ed064d1b8 | -13.0119 | -45.1988 | 2025-10-01 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 237.9 |
| 0e442d17-5f10-3d9e-8cfd-8ee4e9ade460 | -9.9189 | -43.6743 | 2025-10-01 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| e3a98f40-9d93-3bda-9a79-7a1536f0bde2 | -14.9733 | -46.8896 | 2025-10-01 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 40100db5-941f-3a29-adcd-f5fe629d3dc1 | -11.8478 | -48.0816 | 2025-10-01 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 2f7806bb-be7c-3b57-a17a-a18c0e873a8c | -9.4644 | -47.6124 | 2025-10-01 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 71a67b84-0c89-3122-99f4-07e89ca9a9d0 | -7.5561 | -46.7795 | 2025-10-01 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 2dd0e16b-b1a6-3b43-9f31-75ba70b6276d | -8.9182 | -47.5803 | 2025-10-01 13:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3d75f342-fc4c-301b-acc2-60443e3a8e77 | -11.925 | -48.0273 | 2025-10-01 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 5cc99ebf-1d79-3005-975b-063dd22cfd52 | -11.829 | -48.0619 | 2025-10-01 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e2e5ec47-5331-318b-b3e4-68a04f5feac2 | -11.4592 | -45.0664 | 2025-10-01 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1f125add-bf1b-3e79-a16e-41580f3d25ee | -14.8016 | -45.8178 | 2025-10-01 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| f6ca81a0-7e89-39f5-afbf-17a12edeeff4 | -7.8882 | -47.281 | 2025-10-01 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 13686103-98ab-3b2d-a093-cdefccd1d5bd | -11.46 | -45.0202 | 2025-10-01 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 209.5 |
| 4181a58e-cbb4-3151-b381-51636296332b | -14.1982 | -44.9263 | 2025-10-01 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 55b1a7ed-7213-3682-808a-627ea5db541c | -8.8797 | -47.6502 | 2025-10-01 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5ff17b1c-3b9d-3761-b9b4-58f53749e4e0 | -11.9254 | -48.0051 | 2025-10-01 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 6707188b-d37a-32b6-bfe5-9fbf0c841e78 | -9.9376 | -43.6953 | 2025-10-01 13:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 2d77a63e-7df9-3287-99ac-66de8bf75efc | -8.6722 | -47.6924 | 2025-10-01 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c24c89e2-57f6-39d7-9cfd-63a48695f4a8 | -14.3514 | -45.9437 | 2025-10-01 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 134.8 |
| ab2b9043-c0c7-3f5b-8665-3829f7d343bb | -14.2177 | -44.9228 | 2025-10-01 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| f2d23636-e354-372d-b66b-600ac7729d1e | -6.5546 | -43.9221 | 2025-10-01 13:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| a5cc4961-0755-3c42-928c-76b8e5e24776 | -8.5867 | -45.4914 | 2025-10-01 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 972ba30b-bf98-3445-aba2-c2eb924ab83f | -12.2536 | -47.806 | 2025-10-01 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 08400bee-89e4-3bf7-9113-b9f8906a2c67 | -14.9738 | -46.8668 | 2025-10-01 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 153.1 |
| b741deda-6b8d-3bd3-9d9c-d99656b90468 | -8.672 | -47.7144 | 2025-10-01 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 90a41de2-44be-32cb-8d3a-c05ab0072bc7 | -9.6893 | -46.3635 | 2025-10-01 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| aa25db46-69a9-3279-8970-e99e27e7d7ca | -6.3 | -45.0205 | 2025-10-01 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 16db9445-6aac-37f3-92eb-25f7e57bce4e | -9.1246 | -47.6476 | 2025-10-01 13:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 4b12030f-2257-3b76-aa46-dc2b19d008c7 | -10.0337 | -50.2424 | 2025-10-01 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3ca36e07-59ef-3a00-84ac-33b161171c34 | -14.8026 | -45.7713 | 2025-10-01 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 159.1 |
| d393abba-b438-3a3f-be0d-e65221696573 | -11.383 | -45.0543 | 2025-10-01 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| a3f02931-d2c9-3070-96c7-f95c9439bfc6 | -11.1757 | -47.2134 | 2025-10-01 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 9c86d3d7-3d1a-3391-a4a4-66e1e56045df | -14.9738 | -46.8668 | 2025-10-01 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1de3e694-f7e6-34e4-b4a0-869b9606a2b9 | -13.2969 | -50.6821 | 2025-10-01 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 31176e2a-1874-397b-8c8c-6d805027f195 | -8.5079 | -47.2897 | 2025-10-01 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 12c19da8-854b-3548-acc7-05174dd57f5c | -8.5587 | -44.7414 | 2025-10-01 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 3d5b98ee-919a-344b-9ba8-f0e99bac0c1e | -8.6911 | -47.6906 | 2025-10-01 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 849bc069-0e77-3aa5-a673-64aaa20dd289 | -13.0307 | -45.2189 | 2025-10-01 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 5ff44920-36a4-3101-bb30-b0053901e9e9 | -8.8609 | -47.6521 | 2025-10-01 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| f3f50319-3ff8-3303-a543-cd882cb7a2e5 | -12.2532 | -47.8282 | 2025-10-01 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 07d10dfa-c020-3158-a6e2-438e03950345 | -8.8923 | -46.6519 | 2025-10-01 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 7c969804-6914-386a-b583-d7b9a62c77ec | -6.5417 | -45.2055 | 2025-10-01 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| dac97c7c-bcb2-3cc9-afb6-c66f669b7cca | -12.2641 | -44.0363 | 2025-10-01 13:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| afc4ee21-30c1-33a7-b873-17445e9ca0a4 | -8.5404 | -44.6975 | 2025-10-01 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| aae23839-cf02-3d58-a605-6395b260a119 | -11.8482 | -48.0595 | 2025-10-01 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 4090b421-5e79-3bee-9d6a-b28a5cbf3329 | -9.9383 | -43.6483 | 2025-10-01 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 99b13937-f9b9-3da4-acf7-fe527136a7cb | -12.2344 | -47.8086 | 2025-10-01 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 2c39c568-0b5f-3b1d-ae4b-4fd1069c3e7d | -8.5584 | -44.7644 | 2025-10-01 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ec5e5a87-ea82-39d5-b507-8c95149cc5b0 | -15.9388 | -43.2979 | 2025-10-01 13:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 267.0 |
| ec0098bd-0caa-3f6d-9f2c-63d771a15cbf | -12.4618 | -50.25 | 2025-10-01 13:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 4226da53-32b1-32db-a9cc-31e37c6cd8fd | -11.9272 | -47.8941 | 2025-10-01 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 10db0015-9693-3fbe-9001-41cde42a906b | -11.8246 | -44.9669 | 2025-10-01 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 95a40415-69e5-3d78-bf1d-92f1436b0316 | -8.5599 | -44.6494 | 2025-10-01 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 925d021a-6f65-347a-9524-ebb40333e2ba | -14.3519 | -45.9206 | 2025-10-01 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 360aafe7-6bf1-3502-8507-b87d23914f75 | -9.1889 | -48.5166 | 2025-10-01 13:10:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e339fc6a-bd84-301b-b3ff-946ef9516782 | -13.3615 | -48.0936 | 2025-10-01 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| bd8d0add-d58d-3bca-95b2-129ab5960225 | -8.6722 | -47.6924 | 2025-10-01 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| bae75a9e-e488-386c-9de0-81bf060dffbb | -14.1732 | -46.1124 | 2025-10-01 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| f3741787-36e3-3baf-bb32-ab4cf4b744f3 | -14.8021 | -45.7946 | 2025-10-01 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| ad06f8aa-a155-35a4-960f-d80fac44b5e8 | -13.3278 | -47.8313 | 2025-10-01 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| d298a2c7-40a4-395a-8db7-f3df8bfa95c5 | -8.5018 | -47.7965 | 2025-10-01 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 06f75117-0846-3b78-8322-0945d8e067dd | -12.254 | -47.7837 | 2025-10-01 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 5c63eb97-3332-315f-932c-22e93ba2bfb5 | -8.9182 | -47.5803 | 2025-10-01 13:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8027140c-45e9-381e-aeeb-b655ff45e359 | -12.4622 | -50.2284 | 2025-10-01 13:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 249.9 |
| b1de1564-3e01-3abb-b6ff-22bf1216612a | -10.623 | -48.6042 | 2025-10-01 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 6736fcc5-ea75-328a-ab2c-a19f79e76f06 | -14.3514 | -45.9437 | 2025-10-01 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 142.2 |
| bc7b2b5c-6dae-3493-abe3-2e5ae2604878 | -13.2973 | -50.6605 | 2025-10-01 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| cae704c4-4da8-365a-934a-97cc46009e42 | -13.3808 | -48.0908 | 2025-10-01 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f39be50a-26d1-3c34-871a-0edd0fe00c5e | -11.1178 | -49.7845 | 2025-10-01 13:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| db60340a-6dcc-371b-82eb-04d68c882d02 | -13.6703 | -48.07 | 2025-10-01 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 9c83a7d5-26a4-37a2-b781-7139cd33ea41 | -15.3596 | -47.0724 | 2025-10-01 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |


[Clique aqui para ver as próximas entradas](README152.md)
