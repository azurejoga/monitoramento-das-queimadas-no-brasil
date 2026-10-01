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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5d52b73-070a-364a-9eaf-5556535013d6 | -3.37482 | -50.94241 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c538e5ad-3394-392f-adb3-e97cd2efb226 | -2.99294 | -51.02943 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 778a738e-702d-3cf8-b85b-b145a14a950f | -2.90988 | -51.326 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f92623ce-b88e-32b1-a382-357fe9018f93 | -2.98564 | -51.03349 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bbec86a3-3811-3d79-b661-93c501acfe22 | -1.20819 | -49.28828 | 2026-10-01 04:12:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71387566-45aa-3538-9069-4fa78f5d1e03 | -3.96016 | -49.44882 | 2026-10-01 04:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a651c9e-47f2-35fd-b74c-b98279af04b2 | -3.68948 | -47.12355 | 2026-10-01 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62169cc2-31c2-3ef8-8c55-f43248f5865a | -3.09906 | -50.26679 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76197fe8-61e7-373c-bb62-9bdcc52b4501 | -2.365 | -50.34589 | 2026-10-01 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d030860-c1a4-31f7-a522-cccf4eab763d | -2.30027 | -48.58917 | 2026-10-01 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7d1090e-f4e9-3228-8627-488c1f21a599 | -2.9152 | -51.32405 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba75819e-4859-3f6b-b2c8-3906db991e82 | -3.12269 | -50.27549 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a02bf80b-6f65-3fc0-a874-d0099f102918 | -4.13225 | -46.86946 | 2026-10-01 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad7b1917-7607-3716-baa5-cd1992b729bf | -4.12657 | -46.87391 | 2026-10-01 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8b1b8b9c-9493-32d6-9eae-b8f8af04d38d | -4.1589 | -48.89951 | 2026-10-01 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fb2aa56-ef8d-3bda-abee-832216d72a97 | -2.97742 | -51.04282 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c80b38d9-06a1-31ef-ac3f-5446cdc8543f | -7.53694 | -47.12392 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6b744a8-eb60-330b-a329-4c55b473be93 | -12.17808 | -47.38622 | 2026-10-01 04:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23bc0e7c-c9b6-38c8-abaf-79b996422576 | -8.62302 | -45.37567 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8d47ee1-ff67-3ea9-a8c2-f0c6ba897aec | -4.25449 | -50.77011 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 776af72e-6239-3f34-952b-163f4c863e97 | -8.21319 | -45.48849 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df511d95-2db8-3361-b902-1dd87a378771 | -11.44571 | -43.42487 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c228d9c-9ea2-31b0-b5e3-081902b5b485 | -4.29201 | -50.73693 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51ddcc91-9117-3969-845a-75ca2c75b309 | -11.18512 | -45.10831 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b41c95e7-fc72-37e8-b16e-8ec5a10fa78a | -4.30524 | -50.76037 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc264857-65cc-3186-abed-e2edb8b774eb | -8.33331 | -44.16319 | 2026-10-01 04:14:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bdb64b6d-9c9b-3ae1-8576-e18faca25f35 | -4.25369 | -50.77475 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 87d1a75b-b73a-31a8-a942-05fe0154ab27 | -11.20283 | -45.20126 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 960c96b2-1264-3689-a426-479d01d41f93 | -4.25518 | -50.79077 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 25c741ee-5f09-3371-b005-05c1fc362561 | -4.25458 | -50.84353 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ae0adab-bd8f-3be4-afc9-7d6ee50a5613 | -6.13182 | -53.27631 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94b2657d-43b5-390d-996d-8c726fff43ee | -6.72243 | -45.99218 | 2026-10-01 04:14:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afa623ae-919b-3f37-ab38-324acf970d84 | -4.26937 | -50.75767 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d3f3dbfb-060e-36a7-a5f5-57f003b951e2 | -4.28135 | -50.79927 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 48145a16-565a-3456-b83e-d9bbe3da8217 | -4.28078 | -50.79043 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 936632f9-fb13-339f-8dc6-ea725ee7bb51 | -10.84791 | -48.68485 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4f659a6-b71f-389b-b11b-6458d0f8f599 | -8.00996 | -47.44844 | 2026-10-01 04:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1235a8ef-f7e5-302f-ab87-cc0ed20fe603 | -11.43238 | -43.41855 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a25e143d-a51a-34a6-8f7c-4c48829a809c | -5.74177 | -45.15715 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4e97fc5e-c062-33f8-a693-b19677894743 | -5.74115 | -45.16091 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 67f167c2-ed7b-3c58-91ca-c64192ce2812 | -4.25702 | -50.75546 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e1a4a270-6b09-3e9d-af62-508c4bbfca35 | -11.1751 | -45.12103 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3c7544d3-752e-3b94-966e-ce0556c71d1d | -7.56428 | -47.21278 | 2026-10-01 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f399dda-cb7a-3d18-a011-67cd57810cec | -4.62771 | -50.60662 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47a081a9-f1a8-38e6-996b-4c91bfb08e87 | -8.98872 | -44.17643 | 2026-10-01 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af31e5df-1cea-3831-bc30-4f894e420665 | -11.42189 | -43.41675 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d3ae32f-8653-3340-b676-c7b09b22377e | -11.42124 | -43.42067 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f0bb2a6-c281-3518-83c1-e59a227ca28b | -7.07179 | -42.30074 | 2026-10-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 8e4fd550-3003-3214-973a-08a3fc779d3c | -11.41167 | -51.01865 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bc67121-b30d-3a56-a66b-1a0b42a9cd2d | -4.26568 | -50.8162 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6014e372-a7bf-3a57-8b20-303682dcb64e | -11.4232 | -43.40892 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 026ded8f-32e4-3833-a02a-03b283c743e0 | -4.26068 | -50.83133 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95cd312d-f4bd-361b-9a6f-94cb128e2cba | -11.41353 | -50.98011 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 598b7539-818a-3107-a596-6a2ecbf6ad5f | -4.26241 | -50.76117 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| ab584918-2ecc-376d-9308-7d6ac48886ab | -6.69958 | -45.62616 | 2026-10-01 04:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98ae7f8e-58a8-3b08-b657-b6551e4a4a44 | -10.91597 | -43.84954 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20571682-9442-39b3-b948-bd891d78a22d | -8.24286 | -45.43111 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02b80899-1b80-3180-9e37-2df340f1158f | -7.11387 | -43.15924 | 2026-10-01 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 5db3952a-04c6-3b60-af5a-e801768faeda | -4.27719 | -50.74923 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 58cd0a87-4fde-30e9-aae0-a3e53c5f574c | -4.29002 | -50.78586 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ce4ebb9c-b1d1-31a5-bd32-e830ec3f345f | -10.46239 | -46.76893 | 2026-10-01 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f79966fa-25dd-3ae4-8d3c-84bc8fcd1aef | -10.55139 | -50.04636 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f484ba6-4d07-3b4d-89c6-2a6a6a5de22f | -10.84396 | -48.7064 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9d80bf8-3b50-3ff3-9516-f95c9ca816d1 | -11.42255 | -43.41283 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02a86ad6-3cd5-3d71-b351-234f6f5a8d39 | -11.43937 | -43.41975 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 37a3fe8e-69a2-3645-b7b6-fe73a2f5898b | -5.17756 | -46.19698 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 299e4540-7994-3d42-8416-c1e49f5aae57 | -11.42888 | -43.41795 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04f7d33e-bdce-309d-af1c-b012da4fdda1 | -5.75069 | -45.15489 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0cd8946a-0c1d-3995-bb25-34a7f74eb8b4 | -4.28841 | -50.7953 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a83ea81b-3d10-3be9-be5f-a54af13ca84d | -4.27679 | -50.78866 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 2458fe0d-f359-365d-890d-2c7017c07385 | -7.03821 | -50.73322 | 2026-10-01 04:14:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a6cea8b-6e18-3eef-b74a-fc583e6acb9a | -10.72751 | -45.32496 | 2026-10-01 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5858147f-dba9-3eaa-91ac-a204043f6ce0 | -4.2632 | -50.83065 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ac9a446-ed2a-3aec-ab05-b831a7744331 | -4.24545 | -50.74881 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 344da69e-4ea0-39e2-bd3e-2bb4f7ee401f | -11.12595 | -44.59441 | 2026-10-01 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e35a468-3df6-3914-bf49-dc01aebb4f01 | -11.20589 | -45.13871 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df2b7180-4ecd-3174-9b53-10576c410b9c | -5.22242 | -46.02662 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aba38f86-d2e9-3381-896a-2017483a29ec | -4.45749 | -47.9181 | 2026-10-01 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2e189627-20d8-3e7a-be33-3d9813923a55 | -11.34491 | -43.3597 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45b16e35-67c4-3037-b524-079e45f744cb | -7.19681 | -46.54805 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72cafb3e-e820-327e-b415-70d95465123f | -11.32488 | -50.97003 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba1c70d3-569c-3824-a31b-648058915bf0 | -4.27804 | -50.74429 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f2d36bf4-d450-3e09-956e-1c132961798d | -5.44077 | -43.73706 | 2026-10-01 04:14:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 158a3b88-8128-3a85-9f5f-8a0db53006a6 | -5.17862 | -46.20103 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1a73aaf1-9285-37cf-8698-6d418a63454a | -12.3528 | -46.37843 | 2026-10-01 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdce63be-4800-3f9a-b113-d3d9285ffc0b | -11.17973 | -45.11691 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e0d7714-1eaf-330e-996c-4804ca63794a | -5.75359 | -45.16315 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 01512790-c5b0-343e-a253-da031c085062 | -8.49561 | -44.75774 | 2026-10-01 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d44e0fd1-6fd5-3bd7-b4b9-18268bdd50e1 | -4.28438 | -50.80603 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a4d3c9e1-f463-3188-a22e-9d2493bdf9db | -11.45514 | -43.45477 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 56ff7d69-e442-334d-943f-1f4a30f3e419 | -11.4143 | -51.01558 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19f27734-6811-38b8-be79-cd9079c05568 | -8.2463 | -45.43542 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a628312f-4528-3b05-82af-bc990433a28c | -11.26402 | -43.51985 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e97d3da-9c49-3554-a3f2-d2e2fe88593e | -4.29105 | -50.73287 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 815b6493-4ecd-391c-b69c-c4221da52727 | -12.41353 | -40.92156 | 2026-10-01 04:14:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4e721529-1969-37bc-a438-b421ee61a907 | -8.77382 | -47.84095 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9c85db0-3bb3-32e9-aa18-6ff5719bc334 | -4.28754 | -50.80037 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f6c5f438-a62f-37f5-8649-e8bd30b76646 | -9.16319 | -45.59709 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67c59d56-4aff-3d89-b2bf-508feb687898 | -7.8545 | -45.82381 | 2026-10-01 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 01301462-b9ad-3917-b8b9-c78fd529b3a3 | -9.20377 | -45.82241 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README30.md)
