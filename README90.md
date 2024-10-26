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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2f09e86-3eb1-33c5-a769-00e9074e13f2 | -15.69652 | -51.41117 | 2024-10-26 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bccb91fd-fdd8-342f-9b6c-2531eee80221 | -18.25398 | -56.00531 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| ecfc101f-072b-3367-a55b-72bc1178d339 | -18.25331 | -56.00925 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 609eb6f5-09e2-38a7-9d30-ce4e849ffe42 | -11.40029 | -51.23322 | 2024-10-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a03d1362-6efa-3436-91be-37f7bafff546 | -11.39974 | -51.23678 | 2024-10-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f15f2a3e-f74f-38e8-9212-99df43d5105f | -14.8876 | -53.08821 | 2024-10-26 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4b2b6bc-ed23-3eb7-a656-8db9537ea86b | -16.74693 | -52.4576 | 2024-10-26 04:46:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbbaa58d-c454-35f8-b333-0af1dc67a590 | -17.05437 | -53.45625 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1bb19ae0-9ee5-301e-90dd-f6e3fe75ee62 | -17.05381 | -53.45985 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 314ca99d-e1b9-3467-afe9-d5252d8f5a91 | -17.05324 | -53.46344 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cd9de72-087a-30e3-90e8-8b5e24479b68 | -17.05163 | -53.45209 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab5edb09-49f5-3f7a-9f92-a63dc4db7cdc | -17.05106 | -53.45569 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1de8f50b-14f4-32c8-a1b3-5eac7ee46029 | -17.0505 | -53.45928 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fc4e828-eb9f-389f-90ba-ecb0b21ff397 | -17.04993 | -53.46288 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dfc5185-c2a3-3a83-8c0d-eae2d956c048 | -17.04888 | -53.44793 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6c86d4d4-a858-3333-9eff-2603093baf0a | -17.04832 | -53.45153 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c7e65af-3463-3d5a-ae28-39e27e1160b4 | -17.04775 | -53.45513 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6df2637-f1c5-3358-bb7b-375820b8f98b | -17.04719 | -53.45872 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50cb7473-3311-32ea-ac81-f99e0246b7d3 | -17.0467 | -53.44018 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78546123-5d01-3a47-b7cd-7c7a6c448302 | -17.04663 | -53.46232 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3953a5c-008b-3b5a-b098-8f0e3a88433e | -17.04614 | -53.44378 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be58bc1d-3fc6-32f5-8612-ccc550c4b1ff | -17.04606 | -53.46591 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd241d44-76b5-3ac1-9df4-4748b30d5672 | -17.04557 | -53.44737 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e034b9ee-de99-3522-a6b9-177b9a0d4331 | -17.0455 | -53.46951 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83572574-3dd0-3f0b-9f21-2cc04291bce9 | -17.04493 | -53.4731 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b634b49-bb7e-36d3-b7c3-d08d8e282f39 | -17.04445 | -53.45457 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47fde87c-ef67-31a4-9e12-48be9b795b6b | -17.04388 | -53.45816 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d78f4e91-e10e-3c33-8b06-ed95cf072ce0 | -17.04339 | -53.43961 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5de8b636-68f9-3fff-858b-06ab3c5451f8 | -17.04332 | -53.46176 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a88ebf50-0c5b-3c10-baef-57cb4f12b497 | -17.04057 | -53.4576 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 18261fc0-6273-39d0-93c7-23d30a1083f1 | -17.04001 | -53.4612 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9d763b1c-a97a-35d1-b984-3c33b2f53ab7 | -17.0367 | -53.46064 | 2024-10-26 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1265ebf1-3676-3b9a-8a4a-995e1a8e0b98 | -18.24987 | -56.00862 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 2d36c922-ed3c-3520-80c9-aaba2cfb52c5 | -17.37894 | -54.02449 | 2024-10-26 04:46:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81cebb45-4fa6-3552-a7e3-e3f1e1e62579 | -14.55243 | -55.9946 | 2024-10-26 04:46:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| accbf37f-efbf-374d-8d39-23f5dfebc150 | -16.55727 | -56.24488 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 94261643-add0-305d-a6d5-dc49e47f3d0c | -16.5587 | -56.23661 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b710a4b6-34ae-3417-86f1-e76685a564d3 | -16.55799 | -56.24074 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cf4be0e7-5bde-38ba-8629-db953071765f | -16.55446 | -56.24008 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 22c3807d-dc0b-34bf-8d84-2c2a5a60ebc3 | -17.15221 | -56.12056 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c0737fdf-f6fa-3a62-babe-9714582ec139 | -17.03786 | -55.98433 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ee855291-c5ec-39db-812e-d2e00199e8aa | -17.03718 | -55.98833 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 292db01d-1d9c-30db-8925-4ca780bab383 | -17.03439 | -55.98368 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9331d61b-ed9b-35b7-8082-d6a64f5d8793 | -17.0337 | -55.98769 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 510cc468-7585-32cb-aa45-7ddf05d0dc8f | -17.03091 | -55.98304 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ddcc3f97-8e74-3d02-a7f4-6155c97bda64 | -17.02743 | -55.9824 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 63d5e791-907c-3f7e-a63c-d32a4de5c610 | -17.02674 | -55.98641 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e10301c7-67c6-37df-a5cc-e4f87fd5edda | -17.02327 | -55.98577 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3f839460-b614-3005-99de-ad61dbeacd69 | -17.02258 | -55.98978 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a0d3647e-bc04-3cd1-b788-a6888b555731 | -17.02234 | -55.98294 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1d0d8296-40c5-33ce-a8d7-7abadb1e9c79 | -17.02189 | -55.99379 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b16d378e-6ac7-3721-957f-91e0df9991c6 | -17.02167 | -55.98695 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ff9e1280-965a-3409-a915-4d9b10abe44d | -17.021 | -55.99096 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1861f94c-db3d-3fd0-b9c1-eb38c80d2aa9 | -17.01966 | -55.99898 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 09dedfaa-d3b3-33b6-a02f-eb0479219a4a | -17.01635 | -56.00518 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 68009cbe-54c4-3c73-81df-7cb042d9535d | -17.01136 | -56.00573 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 45ed6c81-b5ad-3c41-a5ab-af3461878592 | -17.00919 | -56.51262 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7dcb7586-c101-3c23-802c-a1243297c510 | -17.00838 | -56.56037 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 84fe8a2f-9d35-3e27-a652-bf5fa1664a32 | -16.5608 | -56.24554 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1824b3ad-cabe-390b-a2d6-235cec788ab2 | -16.56009 | -56.24967 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 19b34518-c5a3-3877-b855-bf058d02eade | -17.56777 | -56.74416 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d74f3bea-abde-3fcf-bb4e-83496733d82f | -17.22901 | -56.67332 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4e3735f3-3993-37ca-a377-c623bf719c6b | -17.22751 | -56.67156 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 325c7e05-5798-3ab9-a54c-034fc69a8057 | -17.22676 | -56.67581 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a5fea902-0e51-36ad-b8cd-d8806a6c2e0c | -17.22543 | -56.67265 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3cb9967d-440b-373a-93ec-940e1af8d1fb | -17.22471 | -56.67691 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 08e1caed-9a52-33a7-ac08-b69e3af388fb | -17.01832 | -56.00702 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d539db41-b602-3875-95c3-51808d96b92e | -17.01704 | -56.00117 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 34f72d51-2f65-38a2-9ca0-cd8c08e16191 | -17.01618 | -55.99834 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| db650f28-9f93-304a-816a-3ba750d54c27 | -17.01551 | -56.00235 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 925c13db-f7a5-32a7-98ff-fbb14e917e29 | -17.01484 | -56.00637 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1e72b4b3-4d12-323b-8393-631314238b61 | -17.01347 | -56.50907 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e419a431-9056-3ea9-bfcb-ee9dcf550fc9 | -17.0127 | -55.99769 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 6b8623a9-f0c8-372b-b386-4084ef02e747 | -17.01203 | -56.00171 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 20eb9df5-cb79-35e4-960c-972bcef5b110 | -17.00788 | -56.00509 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9f12ebdc-59ea-3171-9e29-5d889fde8027 | -16.56362 | -56.25032 | 2024-10-26 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| aec5ccd1-10f7-3249-9f96-30e21e1dab45 | -18.32316 | -56.19785 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8646acbc-4c0b-324c-8e26-562de3a1166e | -18.3101 | -56.25333 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 94060d33-3099-3d98-9d68-b51ae0a233ad | -18.30512 | -56.17797 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 77e4ad50-fe07-328f-84e3-d4ea34375736 | -18.30444 | -56.18197 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 12695b97-fbb7-384c-a71f-696a54ca5857 | -18.29898 | -56.23467 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| eac28d51-658c-3881-a686-78da51a0d8ae | -18.2962 | -56.23001 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5b140856-fcbb-3c8d-a180-820ce86658f4 | -18.29328 | -56.02483 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 99de3b1c-5990-3156-94d1-9361b40c45c2 | -18.28984 | -56.02419 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cb7a3bea-fbba-3d96-b0e5-8c4c35c810a0 | -18.27041 | -55.99209 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f12ad710-12f8-3cb7-8216-b2dafd0d31c6 | -18.26907 | -55.99998 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 81a61485-ec03-3575-aa0c-c033fc31e974 | -18.26697 | -55.99145 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 85a7ea27-4822-37b7-8816-a2232f8779d4 | -18.26564 | -55.99934 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2d160ae3-d374-309b-9240-7f04d07d2965 | -18.26364 | -56.01117 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0ad7c8db-c9ae-3009-ad58-bd5fc63ef5ef | -18.26353 | -55.99081 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 23bb6bfa-2b8e-319b-a3ff-647df3d09069 | -18.26286 | -55.99475 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c927d641-d64d-37ab-aef5-b367fb468d81 | -18.2622 | -55.9987 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6d8059c2-f5e8-3d6c-bbf8-4aa86de0d730 | -18.26153 | -56.00264 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 61330e33-c6d2-35a4-b9a0-69df0e5f5798 | -18.26086 | -56.00659 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a4e2f31c-249c-35ee-9d95-797dd0b45d6c | -18.26019 | -56.01053 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9a0d5205-29d2-33cb-8cc5-c61c68fa02b5 | -18.25953 | -56.01448 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 604d0349-af7b-3561-b4e5-c3ae99dee8c6 | -18.25876 | -55.99806 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7e3c01fc-faa5-3d9a-9614-9aec5930e00d | -18.25809 | -56.002 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0d9917c4-719f-3eb7-9f5c-0e4bbf2ba0ca | -18.25742 | -56.00595 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b2320d1c-92b0-3675-b4e7-c113352fcec2 | -17.0499 | -53.452 | 2024-10-26 04:46:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |


[Clique aqui para ver as próximas entradas](README91.md)
