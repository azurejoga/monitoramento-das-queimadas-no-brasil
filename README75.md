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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaf7ed0f-058e-3941-8f5a-100bbdf7f297 | -10.75342 | -54.02425 | 2026-08-26 06:57:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 9c093bc1-e3fd-3695-9a5e-681cc2559477 | -7.38496 | -55.14922 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bb4a78ac-782f-384f-954d-9b1a56bb7ff8 | -9.6697 | -55.07826 | 2026-08-26 06:57:00 | AQUA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 01472626-426f-31bf-bebd-2551ebb21553 | -9.017 | -50.77133 | 2026-08-26 06:57:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9528f6d3-d1ff-35af-9450-d52b9fa4e83f | -8.14898 | -47.50174 | 2026-08-26 06:57:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 584f3d5b-48fb-387e-87fe-639c4981814b | -12.03546 | -46.01413 | 2026-08-26 06:57:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| c02aa47f-9d8e-315f-b0e4-9e6f3b899deb | -7.52617 | -61.38158 | 2026-08-26 06:57:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 5a7d08b4-1c9a-332f-8819-d9542fc3542c | -13.87125 | -54.08822 | 2026-08-26 06:59:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| e1242867-0676-3687-8d73-f585f2d13281 | -13.19549 | -51.31587 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 07152cdc-dccc-319d-8d5c-40e961c34e78 | -13.21665 | -51.3564 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0bb1c024-8d4f-339c-b264-dfe6b639c9b5 | -13.33561 | -48.21205 | 2026-08-26 06:59:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9fd640e1-5a61-3f59-bf09-bfda19fadcec | -13.218 | -51.3473 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dfe2605b-4b83-35d9-9de0-823fc3c2011c | -13.36688 | -48.21724 | 2026-08-26 06:59:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0b747e8d-f80e-33cf-9198-dfb89a2c025c | -13.16489 | -51.33924 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 77a99cbb-e9ff-3b8a-b5f7-0eb601cebe32 | -12.65484 | -48.40977 | 2026-08-26 06:59:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 23acd095-bcf6-3adb-bce0-d63dd07fd844 | -11.7635 | -54.53101 | 2026-08-26 06:59:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a38f833d-85bb-30b2-bd78-ce90932a4f31 | -14.79236 | -48.78697 | 2026-08-26 06:59:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 872ced0c-1551-31dd-b9ef-fddc4fc813e5 | -13.25975 | -51.38746 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b51194e2-7a28-3086-8956-688f14f66ff9 | -12.66504 | -48.41119 | 2026-08-26 06:59:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0867bb0e-adf2-3a2c-9e78-ee97d870650b | -13.29722 | -51.43969 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 149fa7c0-dae1-34ad-bc21-68b9bb50a6fc | -12.76263 | -46.44364 | 2026-08-26 06:59:00 | AQUA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0b524359-6fca-3c6c-939c-17ac9966da64 | -13.24095 | -51.51471 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 606f0fbc-637a-3997-be31-2f9d3a0abe85 | -13.1928 | -51.33413 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 29ebdb69-0648-3b21-bcb4-1aa9489bd3ce | -13.22686 | -51.34862 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 2c44cc50-0941-3987-9119-79265fd15338 | -13.18529 | -51.32366 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 22934f0a-6463-361b-acd0-a81598a93d72 | -13.24876 | -51.33916 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 257ed1c5-6b07-37f6-8755-82e87b1ddd4d | -13.26244 | -51.36922 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 04e6d30f-a002-3e25-ab55-afadab389def | -13.29857 | -51.43059 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3c033455-18ab-3f2f-998c-4f13270b84e9 | -13.28568 | -51.45653 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| dedb9f05-b693-301f-bdc1-6415a8a21b8d | -13.36876 | -48.20337 | 2026-08-26 06:59:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2cbedae2-9eca-3b12-b056-0d263d377e4d | -12.64301 | -48.4205 | 2026-08-26 06:59:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6a978a60-f7ba-38d9-ba02-e8a9ffb6a8ab | -12.76047 | -46.46041 | 2026-08-26 06:59:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 53c60850-58fc-3188-b8b6-8d0737ca45b9 | -12.65322 | -48.42185 | 2026-08-26 06:59:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| a3f4bc74-049d-3890-bc5a-4d73126ae094 | -12.67694 | -48.4001 | 2026-08-26 06:59:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 66abcc93-2d85-3d40-88b3-5da340f9ec20 | -13.28838 | -51.43835 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d8617c9d-73a1-3675-88ff-05465708f5b1 | -13.17509 | -51.33146 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 92b8889b-3c5b-315a-93d5-36058b35c138 | -14.13107 | -52.35606 | 2026-08-26 06:59:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 35c62a6d-3cdf-3695-86b7-e22862fbf7f3 | -13.25627 | -51.34963 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 35384fc9-ca63-35ee-ba94-4af3113c0b1e | -13.17375 | -51.34058 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 12ec2bfc-157f-3772-b5c9-697bd4079253 | -13.24742 | -51.34829 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 82961c7a-47a3-339a-b177-54a56b246687 | -14.79917 | -48.79436 | 2026-08-26 06:59:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8fb2c47e-b3c9-35bb-a2d4-2c4321be7e1e | -13.23571 | -51.34995 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 1ba322e2-5020-341e-9958-9586444801e8 | -13.30741 | -51.43192 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3ddeda67-3322-3d3c-82da-861892d478ed | -13.30606 | -51.44102 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| a55e2e3a-6041-3c6c-b5fc-5c1270554026 | -13.19415 | -51.325 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| d0a840a8-43eb-3cda-8889-2f934b12bc65 | -13.25761 | -51.3405 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1f8b1cd0-387d-3783-9d5e-8913fa5310c7 | -13.28703 | -51.44744 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 4b55eae5-91f6-337b-b789-1fbfb83b45d7 | -13.2255 | -51.35773 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 32da110e-10da-3cda-acfb-131a77b12af0 | -12.6854 | -48.41447 | 2026-08-26 06:59:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 617c3302-af50-337d-a0f8-718ad04fef47 | -11.74443 | -54.52791 | 2026-08-26 06:59:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ebbca5d4-a972-3c71-8b38-fbe0c66b39ec | -13.29587 | -51.44878 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| aeba4101-deee-3f7f-9605-aef523d08dae | -13.17643 | -51.32233 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 59428fad-2a86-367d-b676-cdf617247be7 | -14.79073 | -48.7989 | 2026-08-26 06:59:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| a68ad568-bf08-30e3-a9f3-e0f44d3d35d6 | -13.2153 | -51.36551 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 14c818c4-52dc-34b6-b6df-182ba8139221 | -13.30471 | -51.45012 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 147fa761-d08c-3065-bcfe-b0e52f3f5a24 | -11.76521 | -54.5204 | 2026-08-26 06:59:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7bca2f42-9ecd-3329-80a5-2ee18e65180f | -13.25359 | -51.36788 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| ee8aaec8-e391-3338-9cd8-82f7f9cf1522 | -13.26378 | -51.3601 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 603db2ae-3407-392f-b5e7-161aa5787e4d | -13.16624 | -51.33012 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 6fdbd183-b20f-33a3-aa4c-98183cbb732b | -13.25493 | -51.35876 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 4d0d0c4d-a554-3eae-a3da-30f99455c436 | -12.67522 | -48.41282 | 2026-08-26 06:59:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 807c3946-7cd3-36bd-b89c-7fc1f671b2c5 | -13.18664 | -51.31453 | 2026-08-26 06:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 378a8540-c4ca-30f0-a685-01c9cf25764f | -13.3038 | -51.4304 | 2026-08-26 07:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 948a5937-71a7-305d-9716-91547733e797 | -13.3034 | -51.4517 | 2026-08-26 07:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 3086f806-09d0-3e9f-adf2-e0d91cc2d2b4 | -9.6024 | -55.1078 | 2026-08-26 07:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ce32493e-9599-3ac3-a057-758e36bc98e0 | -12.0358 | -46.0146 | 2026-08-26 07:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 4eb8b4cc-63a1-3153-948c-7ca6d360e416 | -10.7596 | -54.0384 | 2026-08-26 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 10392e51-0801-3edb-90f4-c4d78cf87413 | -10.7784 | -54.0368 | 2026-08-26 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| ead23555-9057-39a3-b2c9-6f9c624842fb | -7.5104 | -61.3832 | 2026-08-26 07:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 5e7f9d7e-4171-333f-9980-6faee995e38f | -12.0354 | -46.0374 | 2026-08-26 07:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4c3c16cd-49d7-3d83-b78e-7929160d6c04 | -6.641 | -58.4987 | 2026-08-26 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 28fbb42d-bcda-3f99-9f73-f426e4dc8f1d | -13.2842 | -51.4541 | 2026-08-26 07:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e5cf37e1-ed05-39e6-b0e7-9ac7bcf63640 | -7.5289 | -61.3825 | 2026-08-26 07:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f4436f49-7753-3ce6-9385-e0246019727a | -12.0166 | -46.0173 | 2026-08-26 07:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b4f6dc8b-a281-34e7-a129-26d4d0b0c580 | -7.5104 | -61.3832 | 2026-08-26 07:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 46b5c6f0-ea3e-38bf-a99e-a7f760690866 | -13.1715 | -51.319 | 2026-08-26 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| d36d1173-9a52-3ea5-a48a-48a54f8eda17 | -13.1903 | -51.338 | 2026-08-26 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 858e7878-5e91-36d4-83b1-be49fb09d4dd | -13.3038 | -51.4304 | 2026-08-26 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 146.6 |
| ea02d3da-6c2f-37ff-a103-99f3e9a5b6ed | -13.2842 | -51.4541 | 2026-08-26 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| faefec38-b372-3c4c-b072-013032111763 | -13.1711 | -51.3404 | 2026-08-26 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a75933f7-a30b-3c84-818a-91b13be4aa21 | -7.5289 | -61.3825 | 2026-08-26 07:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6c3a0187-9131-37bd-9f2b-2574653b996d | -13.2668 | -51.3497 | 2026-08-26 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d04aa690-bcee-34b7-8352-e3330696a7aa | -6.641 | -58.4987 | 2026-08-26 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 30378097-e884-3606-ac3d-4796e05ce12a | -13.2664 | -51.3711 | 2026-08-26 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 46d0d878-e699-329b-9b43-ddc2bf98c6f8 | -12.0358 | -46.0146 | 2026-08-26 07:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| cc1ce9de-eaa5-3a16-a906-1f4327e16cd2 | -13.3034 | -51.4517 | 2026-08-26 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 50b99182-3042-3a4e-8af0-d4e6a803ff71 | -13.2476 | -51.3521 | 2026-08-26 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 016ad632-f71c-34a6-b71b-76ac87c5e220 | -10.7596 | -54.0384 | 2026-08-26 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 9a216d4b-a1b3-34f2-b166-2795d60d8ec8 | -9.6024 | -55.1078 | 2026-08-26 07:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 525ac1f4-5697-307b-b758-1338f389687a | -10.7784 | -54.0368 | 2026-08-26 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 70420b4c-9fec-3be2-b751-d34e856f194b | -13.1906 | -51.3166 | 2026-08-26 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 88d3a791-858f-3143-b9b4-4356489d097a | -13.2284 | -51.3545 | 2026-08-26 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 8a6b4ccf-0e2e-3863-abf3-7da17762bc53 | -12.0358 | -46.0146 | 2026-08-26 07:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 7921175c-03bd-3dfa-9f27-0fbf152c8535 | -13.2479 | -51.3308 | 2026-08-26 07:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 2e73a4d1-e586-3525-8c2d-d8d447046af8 | -10.7598 | -54.0179 | 2026-08-26 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 04bd689b-9c03-30b5-a07c-76bdc7961d7a | -7.5289 | -61.3825 | 2026-08-26 07:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 355c1461-7958-3587-ad6f-e506a6509aa4 | -10.7596 | -54.0384 | 2026-08-26 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| dfbc227f-f90b-3170-aa01-6168b46e1666 | -9.6024 | -55.1078 | 2026-08-26 07:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| bb65a23e-3565-39f4-9414-beef3a65fdb1 | -13.2284 | -51.3545 | 2026-08-26 07:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| b9fe4633-b8e9-3cc2-ac6d-584733107e9d | -13.2668 | -51.3497 | 2026-08-26 07:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |


[Clique aqui para ver as próximas entradas](README76.md)
