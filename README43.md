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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 342cc501-25a9-3caf-a7bd-73b63859219f | -11.50205 | -54.63652 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8b6534a-1a15-31a2-9e83-90cd7ffa6526 | -14.43686 | -51.8548 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b8d3c83-ec53-3eb9-a7dd-1a4a8b537a66 | -7.59319 | -61.23233 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 7dac2c1c-4c9b-3095-9a91-f97b94b00506 | -11.58319 | -54.6894 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b49c80c4-e32a-3705-875b-f57c5ea49dfb | -13.83055 | -53.77773 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f7d6182-dddb-3bac-9bd7-54225f1a0edd | -13.81401 | -53.78525 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0c7eee1-f528-313e-bef8-ac6c842be88a | -9.9828 | -53.94445 | 2026-08-15 05:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 397fdc40-b583-3d86-ae03-8a00c790ec98 | -13.81209 | -53.80077 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76d0d1cd-4810-3c7a-96f9-fd072730316a | -13.83094 | -53.7746 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 578ba667-875a-34e5-9a65-58a7afbe1cfa | -10.72465 | -50.5533 | 2026-08-15 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b2662358-ea72-35dd-9ada-19b5b1ee71cc | -14.43467 | -51.92735 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 911557c8-7571-32ec-a4df-55364cbdb944 | -13.81067 | -53.81231 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fbe343a-17df-3d25-9fed-4b3e196c3845 | -8.61235 | -54.67952 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dce9652-641c-394c-a104-2f346a4551ce | -8.61472 | -54.67744 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b55aa285-30b4-392f-86b8-2992a8b1d304 | -13.80803 | -53.79156 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a348e911-0115-34de-9fc7-7e25f09ee879 | -14.10575 | -53.70453 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a72ec4f-7afb-3dca-8787-f29a54ce3987 | -8.25595 | -57.34706 | 2026-08-15 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 416118cb-74d8-38ab-b7dc-dffb4fb1b622 | -14.43561 | -51.91896 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a16abe69-75df-3928-99a6-af505c13e4f3 | -11.22914 | -54.82624 | 2026-08-15 05:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f4a4b89-a941-3af7-9ec0-1db4ce6ea7a4 | -13.2699 | -54.19618 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e128624-92f0-3383-b09e-a1e83286918d | -11.51075 | -54.64258 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a24ddf1e-7506-3bea-ba5c-38c17e054266 | -16.89477 | -54.14431 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c1305df-9c99-303b-a6e2-323b3f7b7785 | -16.90225 | -54.17043 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8be4e3b-4be1-3212-8580-ef0b11a43ff8 | -16.88364 | -54.14912 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e063c549-16a3-340d-b58f-58822e680450 | -16.89525 | -54.14734 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96dfd6db-4bea-39dd-843f-2574c6e3fc56 | -15.51184 | -52.98729 | 2026-08-15 05:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bee02fc8-e2b3-32cb-8762-cc9b7f7cb58f | -15.54455 | -52.99396 | 2026-08-15 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b394781f-66f9-3112-9e24-648eeabfd38f | -18.90756 | -54.83121 | 2026-08-15 05:38:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b31208b8-3429-3a92-9d5c-14f6572a91ef | -16.89543 | -54.13872 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4066609d-bf51-3baf-802d-c3795d0a1977 | -16.87432 | -54.13836 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d01267d-537d-3f59-b5a4-d355c9237660 | -15.2137 | -52.72172 | 2026-08-15 05:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69cf87fa-7cbb-3657-a594-2677d33517bd | -16.89492 | -54.15041 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b6b1bc9-146a-3a4a-a6c3-039b7d325702 | -15.52589 | -53.01098 | 2026-08-15 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd22e3d4-1db3-3031-a272-c60346239ead | -16.90324 | -54.17059 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0f94390-fb2c-3419-a1ab-228fca66d28f | -18.90245 | -54.83052 | 2026-08-15 05:38:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df95c808-6a9b-3b94-9bce-5d7ac4598f93 | -16.8977 | -54.17302 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef14569c-53db-3ea3-83b5-f6b0e5622456 | -16.87398 | -54.14134 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ccdc089-8e9a-310f-a32d-7085783ffef1 | -16.88397 | -54.14632 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7d00407-063e-3cce-9980-5c21aaa3fb24 | -16.89406 | -54.15034 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8b283aa-3c04-3d7c-8192-9bd43fda8a42 | -16.8962 | -54.13877 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fbde9f7-71fb-3591-a773-969ff2c92396 | -16.90359 | -54.16746 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4104c390-8b0e-38c2-80cc-389b48327399 | -15.23393 | -56.47794 | 2026-08-15 05:38:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7260396-99ca-3954-bfe2-1c60e055d06d | -15.29306 | -53.1888 | 2026-08-15 05:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96eb9b25-7681-396e-99a4-d2ee4cda46b3 | -15.51739 | -52.98769 | 2026-08-15 05:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e99a3bd-26e2-3073-a0df-26a84f3b3dd9 | -16.87845 | -54.14833 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3c41015-c85e-3ebf-8e7c-3e73cccf8f33 | -14.75579 | -56.34726 | 2026-08-15 05:38:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4cd27cc-891d-33f9-8811-f62e90cfae99 | -16.10786 | -49.85975 | 2026-08-15 05:38:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| edbd4f85-0bf3-36e3-994f-f09d5e104ce0 | -14.75521 | -56.35168 | 2026-08-15 05:38:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| aaf35aea-acde-3830-9cbf-da404a49fbbf | -16.89559 | -54.14431 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91643339-1695-3403-b036-f4472f1e19e7 | -15.52632 | -53.0073 | 2026-08-15 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0645fc06-179d-31de-80f5-6d5942fdcfc6 | -16.11157 | -49.86389 | 2026-08-15 05:38:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bfbeda4e-97db-3df2-bb46-4a7b0f7550e7 | -15.52251 | -52.99186 | 2026-08-15 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 54295a8f-3923-3339-b6e7-8c688a4b95f4 | -15.21931 | -52.72231 | 2026-08-15 05:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ceff9a70-ae43-38c8-bc0b-83ce37a522ce | -16.10727 | -49.86601 | 2026-08-15 05:38:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6022baa5-ae27-3608-99dd-50df34057b5a | -16.89589 | -54.14157 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc7d352f-b239-3098-9316-fde2a57df3e7 | -16.11399 | -49.86697 | 2026-08-15 05:38:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32c21a49-1d70-3cff-aefc-a53b5c8a6d29 | -16.88884 | -54.1498 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e79e85d8-464d-3587-8930-02ac6b951c22 | -15.55006 | -52.99472 | 2026-08-15 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0e9f9c1-1cf0-3ee3-b83c-5d414b1d701d | -15.54454 | -52.99508 | 2026-08-15 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c85328f2-55ed-31c6-b6d1-ed1eebfd6d71 | -16.18599 | -55.9557 | 2026-08-15 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 867a06f6-27e7-34af-9ba7-c06bb31a9a95 | -16.10114 | -49.85881 | 2026-08-15 05:38:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22440bb7-0ca6-33b8-8f15-c52ba4b3f527 | -16.10547 | -49.85686 | 2026-08-15 05:38:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be130203-3287-3731-964c-126a0169f147 | -15.51226 | -52.98358 | 2026-08-15 05:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38ca176d-e1ca-3e02-8005-a1b8ee3a0689 | -16.89442 | -54.14728 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ef208b0-3c10-3c1a-8b48-e34be684e1c0 | -15.51782 | -52.98397 | 2026-08-15 05:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a89c5a79-a801-3ad8-86c8-297af0dbc6a3 | -15.52803 | -52.99257 | 2026-08-15 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 334d77c3-6c08-3c0e-a150-1cd5f6a7abb5 | -15.41076 | -56.73604 | 2026-08-15 05:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1a0275f-adda-31b0-91e8-96d9d45da207 | -16.87879 | -54.14542 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3168077e-a3f9-33a2-8d07-2185f6772d00 | -16.10485 | -49.86293 | 2026-08-15 05:38:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 306455f4-fa60-3061-a4b9-6c1244cbd8ea | -15.59882 | -56.16399 | 2026-08-15 05:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97a29e86-fba7-35b3-ae3b-fdd29cb2858f | -15.55005 | -52.99579 | 2026-08-15 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9284632b-ba13-399d-b9c2-00fe82d0806c | -16.8951 | -54.14149 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed14df41-2684-3b34-be77-d725a752a875 | -16.88917 | -54.14697 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02b51fdf-9c87-36cd-86de-4bde75c710ca | -16.18542 | -55.96033 | 2026-08-15 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e71e0d23-3ad7-3cc7-89e5-668ea030ef44 | -16.87914 | -54.14244 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e8d20b0-f2d6-323f-ab93-d0d18d245adb | -16.90262 | -54.16732 | 2026-08-15 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50f35df9-4b68-3566-8602-977b7113b03d | -11.418 | -46.3733 | 2026-08-15 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 9aab4868-a3f9-3387-be63-edb1b48d8c76 | -11.4371 | -46.3707 | 2026-08-15 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 9454fc70-a50d-3408-9ccc-17dad6cba00a | -11.4176 | -46.3959 | 2026-08-15 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 26a1042f-363f-3114-a31b-19070199cdf1 | -14.4499 | -51.9004 | 2026-08-15 05:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| b1b802e9-c35c-33e3-b7b3-867b3c6372a3 | -11.4375 | -46.348 | 2026-08-15 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 82cc4c7e-6fbc-35db-b0c5-39f4a30ab19d | -14.4306 | -51.9029 | 2026-08-15 05:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 181.9 |
| b55427a8-7398-3a2c-a2ce-f6792ecb2d01 | -11.4184 | -46.3506 | 2026-08-15 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 18262301-2ed4-3b58-b377-9e19687ce651 | -11.4367 | -46.3934 | 2026-08-15 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 5abec572-82cd-3425-b3fb-4244be464e5b | -14.2867 | -42.6956 | 2026-08-15 05:40:00 | GOES-19 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 113.2 |
| e649cdba-6bb9-3d9e-b3b1-0956bcd739d3 | -14.2862 | -42.72 | 2026-08-15 05:40:00 | GOES-19 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 127.0 |
| 58368853-09b4-345d-9da4-69b909b8591b | -14.4302 | -51.9243 | 2026-08-15 05:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| addf2276-1121-37af-849f-13504680fb62 | -14.4495 | -51.9217 | 2026-08-15 05:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 0a34ff8b-5889-3462-95cb-43df4faee4dc | -14.4306 | -51.9029 | 2026-08-15 05:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 254.9 |
| 4ddafb29-7b49-30af-a6f9-ac6ef7a2f865 | -11.4367 | -46.3934 | 2026-08-15 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 2e13a167-d530-3a10-9d74-b33e0c0b2fe9 | -6.9334 | -43.6333 | 2026-08-15 05:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a004c11e-6668-3cbb-923e-cba11cea76d6 | -14.4112 | -51.9055 | 2026-08-15 05:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 342f755b-d3c8-3db3-a1d5-ea5ab2513da9 | -6.6194 | -59.0609 | 2026-08-15 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b8248d62-d7fe-3b24-855a-b36431603102 | -11.4371 | -46.3707 | 2026-08-15 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 233.9 |
| 8a8c8940-7275-35fe-94be-b31173aa8675 | -11.4176 | -46.3959 | 2026-08-15 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| af888aae-2ccd-3daf-8ad5-0802d5f60a76 | -14.4495 | -51.9217 | 2026-08-15 05:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 91ba8785-6541-3f6b-8f1d-7a1a8b3ca721 | -11.418 | -46.3733 | 2026-08-15 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| dbe6e892-867a-3600-8d2b-e6dedcad48ea | -14.4302 | -51.9243 | 2026-08-15 05:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 68a952c6-9522-385d-8b48-cea14e5f80cd | -14.4499 | -51.9004 | 2026-08-15 05:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| d0eb6aab-43ab-30da-ab01-fd363881f00f | -6.78758 | -55.83116 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README44.md)
