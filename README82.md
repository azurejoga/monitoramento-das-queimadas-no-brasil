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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b091d56-2945-3e6d-ae71-41089eaf88cd | -9.01846 | -48.15236 | 2026-09-21 05:06:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0401f28-8230-3fba-9626-dfe4f034785f | -9.55044 | -66.01176 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 538e4e77-b682-3bf2-966c-4421730405ba | -8.9642 | -49.14995 | 2026-09-21 05:06:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f00904e-42ab-32dd-a7dd-f457bfad297e | -10.90687 | -53.96935 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dd6eaed-e7a4-3f71-8eff-f135614ce32f | -8.89978 | -62.3429 | 2026-09-21 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e19dc44-e1b7-3aaf-8a64-cdc728130e4f | -9.67938 | -54.32285 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2875e5de-e368-3ad0-8371-abd07fe68c0c | -9.03108 | -51.52286 | 2026-09-21 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 831a797f-4763-3987-97a5-dd9ca3cbf28f | -9.55451 | -66.01949 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9214236-86b6-3770-ae47-40bbf0dd92bb | -10.93212 | -61.4127 | 2026-09-21 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 725ad08a-ba35-33d5-9298-9bf9b22ba5a2 | -10.37641 | -48.90701 | 2026-09-21 05:06:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 084142b9-913b-3fe3-a160-852dcd5af5b5 | -10.92657 | -53.95961 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0a7426a-62cb-3f22-8bab-2c366b869444 | -7.55937 | -61.33073 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0ac6038-1a27-3ae8-9064-731d64e61677 | -6.43769 | -59.97577 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a72ad02-e4f0-308c-aeca-0f60473c25c8 | -9.41074 | -65.92337 | 2026-09-21 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f16f058d-982b-36f0-9edb-aaa085aafa91 | -8.19522 | -54.70713 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc874154-fa1d-32fb-9ffc-265e7ff0be3f | -10.42699 | -50.25574 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2c6a66ca-e35e-3314-b661-7199dc3acb4d | -10.09099 | -50.2514 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 328df26a-7cf8-3134-88d5-73771fda7a31 | -8.60794 | -54.62185 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57493e2a-ff56-3bbe-9c44-b76497da1d89 | -10.83905 | -50.8947 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ee871d1-81c7-3ec8-b162-d34a0fbaa441 | -9.44167 | -45.41354 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8f2e7888-ae15-3c8b-9ef5-decb806d7104 | -7.2537 | -55.59482 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbdb091c-1ea9-3690-bf74-07352b35dded | -6.46177 | -59.97284 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 20a46ff5-502a-32cd-87c4-f0db32ea621a | -7.52355 | -55.27878 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5f33a24-d5d2-32f3-a3e3-9ed664771d9b | -12.03013 | -51.49334 | 2026-09-21 05:06:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6268dcf2-ee13-37bc-8f82-73bdd19ca176 | -11.1284 | -54.01293 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e477010e-3b77-3ffe-8242-247076d0e04b | -8.24177 | -62.84182 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bf3e5b9-77b8-3aaa-a9e3-2c60be42916b | -8.78307 | -48.74532 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9600a82e-efcb-3c76-a2d7-ae5a64188e76 | -11.04569 | -54.16047 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cba369d5-4f78-36c3-b3b6-09aece7355a2 | -6.64625 | -59.95917 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7b16f10-ed75-3912-8d09-2df494b716bf | -7.55773 | -55.36686 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e67de5c5-40d4-307f-951d-666687e485e2 | -11.80321 | -49.80621 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ce486a91-cfe4-384b-9984-a119c73ec578 | -12.76907 | -52.85011 | 2026-09-21 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b498b0cc-a10c-387f-990d-0a74e7af5a25 | -6.4527 | -59.98079 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86e5687c-4735-3d52-b29f-a4502002a2db | -7.24931 | -55.60126 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb4d9235-a718-30c7-84ef-1de997d933b3 | -10.86557 | -53.96042 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb4b1319-6bad-3695-9390-ee84741abc1e | -6.75307 | -59.11552 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37e051be-f3ef-314a-b757-6c3a465afe61 | -7.28164 | -61.1169 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5a36b42-bc96-3c7a-a2ed-b8d18fe85a1a | -10.70761 | -50.77635 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b6b929a-2909-3108-b7dd-bf86b1f176ce | -10.38132 | -48.90763 | 2026-09-21 05:06:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d9e504f-de46-31a0-a6dc-2d28fa4c60c3 | -6.46401 | -59.98264 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 200203c3-e91e-399b-9607-6e45c94c946f | -12.80395 | -54.05577 | 2026-09-21 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7392bcc-f9a0-36d6-bba4-0303d2b1d8f7 | -9.82774 | -48.44409 | 2026-09-21 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7e270126-02e6-3462-9353-627350243509 | -11.79786 | -49.81061 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 71672110-acbb-3390-9358-c5ddc43bd0ee | -10.88541 | -54.09223 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c38c614a-4769-3370-b292-c6c2d1b5b087 | -11.95117 | -46.49626 | 2026-09-21 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5ccd3c3-9f1e-3a89-92f3-4644ceada277 | -12.53976 | -50.07239 | 2026-09-21 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82e759ba-1f26-3dd3-90d7-008a661f52e3 | -10.6963 | -50.76187 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1300fccc-c7ed-3679-8dd5-bc9471732ab0 | -10.85173 | -50.15644 | 2026-09-21 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 156d641d-7a90-3c04-b9f5-b9a3db530b5e | -10.67919 | -48.72784 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bd1c6b24-3f03-3e4a-ad3e-381757156b73 | -11.48101 | -47.76999 | 2026-09-21 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfccb8bf-3560-3283-84a1-9b63b1aab32c | -11.34089 | -51.36086 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d8edcd1-40d7-3b75-b96c-96a137e7bcc0 | -10.88363 | -53.97847 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98872856-0318-3db8-8d09-c73d66d26e6a | -10.48852 | -50.99503 | 2026-09-21 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54cec377-9a87-3c24-8a98-afabaeed9643 | -9.66027 | -54.33184 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77d18051-0f48-3a1b-8241-9b7381610bdd | -11.13378 | -54.00108 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b61f6ea-e470-3b37-97e5-ff16c7ea42a8 | -13.27051 | -51.76457 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aade9b1-5597-381d-b698-855c0024e6c5 | -8.189 | -54.70241 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ad1b4cb-335d-3155-a9d8-e14413b9878a | -7.56667 | -57.67834 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fa5802b-486b-3340-a117-1e7b49fdb73c | -10.92299 | -53.95906 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55b3db0e-e188-3c61-aeea-0b3dc10af74a | -7.24485 | -55.58632 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c036f680-3f6c-3637-a189-2a17de97983b | -10.42101 | -50.24409 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 32db8e47-eaf7-39b9-aa8f-834a2851f3de | -10.10768 | -46.94927 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e64ab57a-5798-3602-8131-a3d9709caee2 | -8.77981 | -68.84691 | 2026-09-21 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 167144d6-61b9-3b1b-8214-aff206e862ce | -10.85424 | -50.16029 | 2026-09-21 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5aaa6607-4d89-34e0-8c81-3387c0392468 | -10.90925 | -53.97817 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7697963-ea0a-3728-8ccc-a901c20a76f3 | -10.48592 | -50.29161 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| bdc6643c-061b-348d-b895-712622499469 | -8.86497 | -68.51328 | 2026-09-21 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2364e404-e09a-370c-9d3e-412bdfc7b118 | -10.10921 | -48.44024 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56ab3fd0-4a84-396c-8135-5f31ef2099af | -9.28672 | -60.635 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d74039a-e02f-3424-bfbf-e337c3fec44a | -12.27616 | -50.15855 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1a90b7f-0d5d-35da-8826-e7e14efcbfac | -10.41593 | -50.23579 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 6dcf4531-cb2e-3153-aa7a-de61d3a39553 | -10.69309 | -50.75283 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73cd925f-7926-3b8c-8c0b-904a9e9453a5 | -6.92386 | -62.91237 | 2026-09-21 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5a22b5f-01c3-3b3d-86ea-8118d2c1475f | -10.12368 | -48.4422 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbf88a4a-6e91-3475-a971-96265728a023 | -7.48367 | -64.70448 | 2026-09-21 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a89dc183-00c9-316f-999e-c4765049c731 | -10.76219 | -50.79698 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| c745bb1d-e809-37d3-a8ad-a8bed90f8129 | -14.6573 | -54.44813 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09c36575-ff13-37b3-8884-b2e82a007b8b | -15.97042 | -50.11299 | 2026-09-21 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 051afb2b-7a8a-325f-b00b-fe8299579b90 | -14.05707 | -52.11499 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c9c2a26-734d-32bd-8741-a2221796ae98 | -16.03737 | -52.5188 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd21605d-50f2-3d81-a15d-8fb8314b8258 | -16.3131 | -53.86836 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7927f79-5a85-3f1b-ac15-35187f5d0c45 | -15.63109 | -52.70198 | 2026-09-21 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0f21dae-32ea-3b86-bfb3-f0020a8bab05 | -15.44675 | -48.46082 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1920c4f4-c596-35c4-8bd4-2f78eab6a4dd | -15.47152 | -48.40339 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28535826-0f73-3e32-88fe-53d657b66b00 | -16.0384 | -52.51097 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e840d486-9408-3dc1-a2b9-aedd1714c6e9 | -16.02956 | -52.51381 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 025d26ac-d7af-3bb6-8612-b1b4517a9e00 | -14.9257 | -49.89736 | 2026-09-21 05:08:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ecd4b389-aa30-3d18-9d22-bd2a7c5cf588 | -14.17585 | -51.79573 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05d12934-b3ba-36d3-987e-e9195c283045 | -15.75991 | -56.45075 | 2026-09-21 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9944506b-51b6-3b56-9be0-ff05dbbc051a | -15.45631 | -48.47306 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4800af64-a360-3c34-a1a2-a74563d476d7 | -18.03933 | -50.93262 | 2026-09-21 05:08:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e646e135-1a75-326c-aa4e-812e72742cfd | -15.46101 | -48.47982 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 420bcaf8-167f-3967-952b-68595a3aab72 | -20.77328 | -55.63505 | 2026-09-21 05:08:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a6e8ca3-6c7e-3e76-86a0-8fb4ed342cbb | -16.31376 | -53.86343 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1009f10-cfa1-3cd2-8d8e-c0ed523b24e3 | -14.1023 | -52.12509 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73291701-4be8-3bef-bcab-a433ff14cafa | -16.03424 | -52.51043 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 2ad46d0c-3a10-384b-947b-845a109b681f | -16.68303 | -47.88473 | 2026-09-21 05:08:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a27d72d-00a5-3b17-b422-bca33bf91c6d | -15.45557 | -48.47945 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bad32680-1cc7-38b9-9945-d8549637c183 | -14.66212 | -54.46652 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8529c8c3-447c-3618-b490-1ede7cfdeaa2 | -14.62094 | -52.11668 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README83.md)
