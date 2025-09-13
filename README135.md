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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a23ea22-0793-327c-8c9a-47c8dee653d6 | -13.2341 | -43.7554 | 2025-09-13 14:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 450.7 |
| 670c148b-8b21-34cf-a4ba-34f39505ef26 | -10.107 | -50.4057 | 2025-09-13 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 58e02f40-94e9-316b-b12c-abc7673376bd | -12.9595 | -47.9963 | 2025-09-13 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| d8768b0f-4f66-3804-bde7-18cf5dcf9a0c | -8.9749 | -46.1054 | 2025-09-13 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| bb4ad5b3-9bd5-3899-945f-fda7cd297e29 | -9.8646 | -50.1951 | 2025-09-13 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| cd5d9b59-0c08-38f7-849b-e968612ea399 | -10.0509 | -50.3686 | 2025-09-13 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 9485b98f-57e8-3dff-a2c3-1947834dbd37 | -16.0061 | -47.9329 | 2025-09-13 14:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 2b9335ba-4f32-3651-8844-9e2aebbd7f4e | -12.9294 | -54.7333 | 2025-09-13 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 367.9 |
| cf8c24c2-cd82-3818-a6a2-33c92117f692 | -9.2505 | -51.2261 | 2025-09-13 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| c0120b06-bd4e-3e9d-9405-9e1b3f46564d | -9.4819 | -55.9601 | 2025-09-13 14:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 5dfa2106-439f-3baa-bd88-a6094a94e718 | -11.7388 | -46.6005 | 2025-09-13 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 169.4 |
| e09d1497-eefe-369c-8094-b5708e1c1e4b | -14.4584 | -47.34 | 2025-09-13 14:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 9336d783-6b98-32fa-84bc-baec93852266 | -11.056 | -51.4962 | 2025-09-13 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| d2141fe0-7ff0-351a-978f-d196359f1412 | -10.9286 | -47.2 | 2025-09-13 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 358.1 |
| 9b8b0289-d66f-3789-a79c-8c04ce063883 | -14.394 | -52.9245 | 2025-09-13 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| af1875ba-d961-3570-98ca-d93668f27e4d | -12.1044 | -47.5816 | 2025-09-13 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| b4c59a5e-4357-36d6-b988-fd0e4d5ed770 | -13.9366 | -48.2745 | 2025-09-13 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d1df76b1-e905-35b8-a55c-a071f817be99 | -12.134 | -44.8275 | 2025-09-13 14:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 9cc12804-96eb-3542-96a3-99a8ef69399e | -9.2844 | -59.3986 | 2025-09-13 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| c83daf7c-9194-3da7-ba59-d82b4902ef95 | -11.7391 | -46.5779 | 2025-09-13 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 276.8 |
| 6efea725-98d5-3277-ab9e-67970b7fea6b | -16.0257 | -47.9294 | 2025-09-13 14:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 99352dab-27bb-3d7f-b722-61201b86c39f | -18.0466 | -45.418 | 2025-09-13 14:40:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 127.7 |
| bf55a3ff-6042-30af-ae85-d2a9488b5392 | -10.66 | -48.6655 | 2025-09-13 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| cc4a8d96-5316-3d55-8a8b-8edba76712b8 | -13.9168 | -48.2998 | 2025-09-13 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 41a56b29-a69d-3960-8485-c7a7b7e5be4b | -5.1934 | -40.9531 | 2025-09-13 14:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| cb79f527-aeb5-3ada-8c87-d2511bdeb73b | -16.0056 | -47.9555 | 2025-09-13 14:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b7fbb0d9-991c-39d6-982a-804962e2d5e7 | -8.9595 | -44.4436 | 2025-09-13 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 53111c4e-cba7-3451-9979-0b27d4058bfe | -10.6979 | -48.6612 | 2025-09-13 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 425f79a4-688c-360b-8d74-bc037579748e | -11.1152 | -51.3211 | 2025-09-13 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 9c6d87d8-3dc0-3610-b629-51f5045bfeae | -14.4394 | -47.3206 | 2025-09-13 14:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 744366f2-f2f4-30de-95b0-7e060c3793d1 | -11.3117 | -50.8122 | 2025-09-13 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 017b2ddc-4841-35d2-a6be-5c0a77ae03ac | -12.9101 | -54.7558 | 2025-09-13 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 49a36a6f-0dd9-37f0-aa6d-dc82f2528972 | -18.0071 | -46.9266 | 2025-09-13 14:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 116.4 |
| faf4d08d-f638-30b7-a39a-2c8fc78da2e4 | -12.9103 | -54.7352 | 2025-09-13 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| a7dc8247-0d2c-35eb-946f-c79dba1d6233 | -14.4939 | -53.8973 | 2025-09-13 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 5f802451-f781-3d2b-a844-c8fb4ac32660 | -15.1169 | -52.4705 | 2025-09-13 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 1adeed83-f776-3587-9746-8cee9c9b7f63 | -12.8649 | -62.1268 | 2025-09-13 14:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9d3006f1-82e9-387f-b14e-264898102f6d | -11.1423 | -50.7242 | 2025-09-13 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| be3b6c89-f063-397a-9d0d-21d465f1638b | -12.8452 | -47.9459 | 2025-09-13 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 9bdcc11f-07de-3e76-b96b-23ad5dd65d23 | -10.032 | -50.3705 | 2025-09-13 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 5f3ad003-ac95-3211-a1b6-d00d9dd8abf5 | -10.9096 | -47.2023 | 2025-09-13 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 8af4fdd2-83a9-3bb4-8547-2b664f81dfb8 | -15.8648 | -47.2322 | 2025-09-13 14:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| a974fdf5-2289-3cd1-b38a-f466052711c2 | -10.5482 | -49.8899 | 2025-09-13 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 895dc7a6-1528-3ec2-94f6-0ee6bb4e967a | -16.08 | -49.9709 | 2025-09-13 14:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 420c876c-d0a5-3ed7-962c-43ec2a035e8c | -13.8979 | -48.2804 | 2025-09-13 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| bbdc509d-d72b-307f-b5b0-1dc3ad9e059e | -13.9379 | -48.2076 | 2025-09-13 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 5d968859-b433-3e0d-9fa1-2ed2c113f65b | -10.4331 | -50.0093 | 2025-09-13 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 46502267-e079-3def-b2a7-fdc60f6f7f20 | -12.9787 | -47.9935 | 2025-09-13 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 68406cbd-a8ad-366c-9dfc-1306f28dbb9d | -8.19 | -45.5774 | 2025-09-13 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 8b26a9c9-e1d5-3de5-8220-67985ed11f62 | -16.6532 | -49.7649 | 2025-09-13 14:40:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 9cb1b847-add3-3c02-9120-884bbd3d179d | -9.2656 | -59.4191 | 2025-09-13 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 7ae0b82c-d3c5-3ce3-9dd3-ba3b6eea7671 | -11.1237 | -50.7049 | 2025-09-13 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 5a3b8e6e-01db-3b81-a0c9-9209f8ef15c3 | -13.9185 | -48.2105 | 2025-09-13 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 416e8cc9-c06f-3eac-965f-e4266f569993 | -12.8837 | -62.1449 | 2025-09-13 14:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| fd63b15d-0c78-3bda-bbc9-012d40c993c0 | -11.2695 | -51.1142 | 2025-09-13 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| d514dd06-8f4d-384c-90ea-2d09d95e2dd8 | -14.7635 | -44.8929 | 2025-09-13 14:40:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 3f00e5bb-99b3-3907-aa60-6d644a4fb915 | -14.3095 | -46.089 | 2025-09-13 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 452.7 |
| 67d476e5-5cd7-3262-9ccc-41aa5409894a | -10.5484 | -47.2242 | 2025-09-13 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| d4614cda-f0c3-3abc-8aeb-3090e269b584 | -16.4903 | -55.1484 | 2025-09-13 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 140.9 |
| 45c26624-a46e-366e-a8ec-ac26051c451a | -12.8259 | -47.9486 | 2025-09-13 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 794ce2d9-9a77-322c-925b-1f404265f34e | -10.7952 | -46.003 | 2025-09-13 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 1d02a759-ac9c-3a6f-b155-66e14102cb39 | -12.8647 | -62.1461 | 2025-09-13 14:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 145.3 |
| a3419066-bbdc-32bb-ab20-f731509d1fff | -12.9402 | -47.9991 | 2025-09-13 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a9b52852-4d8d-37d9-b028-5b91b490b149 | -22.1964 | -49.6194 | 2025-09-13 14:40:00 | GOES-19 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.0 |
| 08207292-5d85-3265-a769-62cf053740f5 | -11.8698 | -46.7627 | 2025-09-13 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 0c6e0e54-bd40-3663-a609-7ae34cc41cfd | -15.1557 | -52.4652 | 2025-09-13 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| d16c6cb4-20a1-3867-833f-96872c8b78ca | -12.9292 | -54.7538 | 2025-09-13 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 270.2 |
| 28917932-07ee-3732-9177-85c82bf57fa9 | -12.7827 | -47.1502 | 2025-09-13 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 292.0 |
| ad04156b-4306-3a71-b4f8-c7c79c51faa8 | -10.5295 | -49.8704 | 2025-09-13 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| a37c29b2-6992-382a-b577-262f11ba3004 | -13.9375 | -48.2299 | 2025-09-13 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f746e2ce-c44d-3865-a776-777ad76f2df0 | -10.9092 | -47.2247 | 2025-09-13 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 669e161f-708b-3e4e-b7b6-4cd1847378f4 | -16.5682 | -55.1592 | 2025-09-13 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 204.2 |
| 23f0894c-f0d6-3578-b5e6-47264281e93c | -10.0506 | -50.39 | 2025-09-13 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1382976c-8df6-307c-9fb0-c652a0a0d3b5 | -8.956 | -46.1074 | 2025-09-13 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 593a6e75-3575-39fa-9e67-6f68c7a25aeb | -11.2882 | -51.1334 | 2025-09-13 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 104d60a6-06f9-382b-bc18-21f694f1083f | -13.9172 | -48.2775 | 2025-09-13 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 953add83-8d08-3527-bb06-624a690a8450 | -14.29 | -46.0924 | 2025-09-13 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 249.9 |
| 005bfaf0-770e-3451-809f-dd1d14a856f3 | -11.7204 | -46.5579 | 2025-09-13 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 209.6 |
| efea8ac6-152d-3974-a09e-511d168ce350 | -9.7222 | -51.0573 | 2025-09-13 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| cbbf9fd9-4f3b-3be1-bf38-cd1c88eeddc9 | -12.8646 | -62.1654 | 2025-09-13 14:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| fb55e891-5735-35ea-97c7-12cbc0c85bf8 | -16.5679 | -55.1801 | 2025-09-13 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 195.3 |
| 07b16f99-f745-39b6-ae8f-c3f3150bd2f6 | -11.77 | -50.6329 | 2025-09-13 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 4f386399-cc7f-3e4a-af12-7d65372300f0 | -9.4817 | -55.9801 | 2025-09-13 14:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 89a90001-2146-3da1-bfd0-80d9c8fd5e4d | -11.638 | -50.5625 | 2025-09-13 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| dfe37f74-e6ad-3f15-a0ba-eff9ce1a21c5 | -15.6663 | -54.3572 | 2025-09-13 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| c5d8c90f-6848-3535-a517-77e9d1dc7cd0 | -6.5968 | -45.3143 | 2025-09-13 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 5d3b09ab-4681-322f-9ec8-58822eb0e609 | -14.4588 | -47.3174 | 2025-09-13 14:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a8639007-be61-3386-a0e6-26165ff3b98d | -12.9482 | -54.7519 | 2025-09-13 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 0123fe29-f86b-3994-bd1d-ba1bd659061d | -12.8456 | -47.9236 | 2025-09-13 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 164.4 |
| bf0ade29-f600-35cc-b8fa-c5567401d9bb | -14.491 | -40.6778 | 2025-09-13 14:40:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 7a19b972-b02f-38af-8e62-e5a0f5fcdfbc | -14.6398 | -52.0881 | 2025-09-13 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 64670d7b-5048-3520-a033-d4e7dfdc35d4 | -11.331 | -50.7888 | 2025-09-13 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 008bf4d1-d836-31d3-91c0-7050e769e44a | -11.2692 | -51.1354 | 2025-09-13 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 5eaeff52-83db-3ee2-bdd2-d112c5f9ec0d | -5.1746 | -40.9545 | 2025-09-13 14:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 161.1 |
| a7e0d725-50d6-36d8-b5c5-76adf9f3f152 | -11.7208 | -46.5353 | 2025-09-13 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 178.2 |
| ff962354-b6fc-3197-a052-2c784566168c | -12.0488 | -51.07 | 2025-09-13 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 51012eaf-e6b1-36b1-9c47-61b7c81cde4e | -11.1234 | -50.7262 | 2025-09-13 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 61891249-6049-336c-87cf-52241a63ca76 | -16.4906 | -55.1276 | 2025-09-13 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 170.5 |
| db968284-e4de-35a0-a491-309921dec3c9 | -10.9477 | -47.1976 | 2025-09-13 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 417.2 |
| 1fe003be-aef3-32ff-b2f2-f28b3cd7885d | -11.7763 | -51.5038 | 2025-09-13 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |


[Clique aqui para ver as próximas entradas](README136.md)
