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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce95a214-26d8-3c38-ba45-71534e0e02fb | -16.13748 | -58.49468 | 2026-06-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ce96774d-e12c-371c-8f5f-2b3e8200658a | -14.28858 | -58.6498 | 2026-06-06 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7820f8c-7a5e-32cd-94dd-7302c1efe1a9 | -17.99827 | -51.14859 | 2026-06-06 05:14:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87df8f6a-338a-38f9-a49e-8849047d5ded | -13.49755 | -56.57031 | 2026-06-06 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 48b883b2-1249-396d-bf2d-809fe0bda656 | -14.22844 | -45.79572 | 2026-06-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bf375333-5b0d-3beb-952a-144002ab1f90 | -14.46537 | -54.88318 | 2026-06-06 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9d99a6a-c994-39f8-833d-b42824ccd1ae | -17.99673 | -54.27858 | 2026-06-06 05:14:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 966112af-952f-3e3e-9287-4f5e12f02ba1 | -13.95653 | -53.84546 | 2026-06-06 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5656b4a2-dfc3-341b-89f6-255edb751a14 | -16.14137 | -58.49157 | 2026-06-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a829af12-3388-33ec-8659-16d9a06f11dc | -14.77132 | -52.67819 | 2026-06-06 05:14:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fbe18486-eaa2-33f5-b1e2-d870c9a31160 | -14.21601 | -57.42368 | 2026-06-06 05:14:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2df86b16-e57f-36bb-82cb-7259b6656bb5 | -16.59381 | -58.23631 | 2026-06-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 94809219-5134-3451-9d96-39d3c418a605 | -19.16546 | -53.97861 | 2026-06-06 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1abb13e-fd42-3fca-a182-7a948ebc3d62 | -20.4502 | -54.86552 | 2026-06-06 05:14:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4926bfc8-f62c-3a9f-b449-9b5dc02b30f4 | -14.22716 | -45.80883 | 2026-06-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bf1fedbc-e549-3fe8-935a-a7900dcd4df9 | -19.74616 | -53.5461 | 2026-06-06 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6dc8074d-b7cf-3229-ac04-82fe963ac1bb | -13.93424 | -53.89007 | 2026-06-06 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01c089c7-46f4-3b83-8b14-a94a5fa405df | -16.60053 | -58.2374 | 2026-06-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| dc4d372d-6ab6-32e3-be25-df0d6480ba74 | -17.99863 | -51.14542 | 2026-06-06 05:14:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33d1f876-64ce-3254-8d51-bde859a0763c | -14.26847 | -58.44992 | 2026-06-06 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16e347f4-e1d3-3f88-b158-b6765fec22c8 | -16.1037 | -56.75388 | 2026-06-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a86e64d7-63aa-3497-ae36-1fd0022cb1b1 | -14.46918 | -54.88374 | 2026-06-06 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25af1f86-7f36-3a3d-a8f5-e6282ad75de2 | -14.46472 | -54.88795 | 2026-06-06 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b61902f-a473-37ca-b43e-8bfa33b4c608 | -12.77373 | -59.00674 | 2026-06-06 05:14:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ab24990c-a3ff-350c-8835-e233ae102e08 | -18.00088 | -54.27911 | 2026-06-06 05:14:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e1387af-a053-39b4-aed2-e3c8db63a551 | -13.50101 | -56.57084 | 2026-06-06 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b3e9bab3-33f3-3bce-a30c-492f5d818307 | -14.21546 | -57.4274 | 2026-06-06 05:14:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d837f6e8-bc83-373b-a00e-62e028840775 | -14.21152 | -57.4306 | 2026-06-06 05:14:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a57c7b81-6280-329d-bd9c-10e4f62c2349 | -14.24222 | -47.9749 | 2026-06-06 05:14:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f19c96fa-99bb-396b-9c43-99bab87b827f | -16.13803 | -58.49104 | 2026-06-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5be69643-43be-36dc-8cee-0f6f83b73901 | -14.25355 | -58.43655 | 2026-06-06 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 994b2fb3-7a36-387b-83f6-af16643ee1ec | -14.0829 | -58.88147 | 2026-06-06 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2de9142e-6f29-32d3-9978-4db765818ea2 | -22.17293 | -50.38448 | 2026-06-06 05:16:00 | NOAA-21 | QUINTANA | SÃO PAULO | Brasil | 3542008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 59eb8532-dd36-3272-a7cc-ab1dbed3e737 | -23.73513 | -54.60789 | 2026-06-06 05:16:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4a7a6844-c49e-3926-bb14-a33b3a946268 | -21.98483 | -57.60738 | 2026-06-06 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83a88758-6d83-3beb-ab95-fddfb60438bf | -23.25434 | -55.08157 | 2026-06-06 05:16:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c36bb3b6-cbad-3d0a-a830-2a4da159e3b8 | -23.73075 | -54.60729 | 2026-06-06 05:16:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d1a2c937-c889-3bb9-9c65-bdd4c529f416 | -23.73146 | -54.60443 | 2026-06-06 05:16:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c1567b04-13e6-3a55-8af0-07c2fb46a723 | -23.25856 | -55.08216 | 2026-06-06 05:16:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2bf565ce-5d5a-3332-96b6-68fb36437692 | -23.73096 | -54.60903 | 2026-06-06 05:16:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6b5a69e6-8127-3fc5-9403-e92dcb4e376e | -21.52151 | -48.62386 | 2026-06-06 05:16:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0f1885d-9f53-34ee-86b7-c4f8b0d4622b | -10.87129 | -53.73578 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e644b2a8-2345-3a2c-9204-07b75933c035 | -11.00783 | -54.3118 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5feca404-6487-3180-8d30-d1eca8c5310e | -10.86453 | -53.73789 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 544e16eb-4cd8-3dc9-8435-9ff1c8fb4030 | -11.63843 | -55.17836 | 2026-06-06 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bba725d0-6509-3e14-be61-2622b42181a7 | -11.27196 | -53.96773 | 2026-06-06 05:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eccc0ef-4a1e-3f7f-b875-cb321f9f057a | -9.08564 | -50.61097 | 2026-06-06 05:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4464c025-beb5-3d93-bad4-98c4deed836a | -10.77068 | -54.0979 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a87f8e7-f46a-3ec0-bbdb-d81643816c81 | -10.85842 | -53.73711 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 583338ff-46e2-3a44-9224-73cab7826a24 | -11.00967 | -54.31234 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 726d3a0a-3287-3b20-bb4e-c88599921d82 | -9.07213 | -50.6019 | 2026-06-06 05:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56217737-3b9b-31b8-8d4a-640f72e92869 | -11.05351 | -56.92479 | 2026-06-06 05:46:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d3f7663-1e3a-3438-b029-2fd1db67f0f7 | -10.57369 | -57.32348 | 2026-06-06 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6ca48e7-234f-3378-992e-2489fb1892f8 | -10.77608 | -54.10328 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db7f4328-a5de-33b1-a185-51e8505cab22 | -10.85111 | -53.74587 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9e004cd-2aff-3d63-93ca-72329365ff63 | -9.3723 | -50.54039 | 2026-06-06 05:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4acb93e8-0477-303d-819c-0ec8e3f3c707 | -11.2708 | -53.96608 | 2026-06-06 05:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00beddf6-b3ed-393f-b22f-3be88707f90d | -11.05426 | -56.91908 | 2026-06-06 05:46:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32de659d-9dc3-34fc-b67e-27465ee97bb9 | -11.26592 | -53.96683 | 2026-06-06 05:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b76d9238-bd42-34af-8565-8adb6a006b2d | -11.63576 | -55.17944 | 2026-06-06 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0954343a-ee96-3182-9335-29ddd87410b5 | -9.16999 | -58.06532 | 2026-06-06 05:46:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b21432fe-7139-3790-b4ee-2374c22940fd | -11.00732 | -54.31602 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb12c156-051e-33b5-92d9-a3e525f5ffcf | -10.77665 | -54.09871 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e12011f-a290-3457-a0aa-f5bbf4d03a56 | -10.86517 | -53.735 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f5a763c-f793-3a1d-9c38-ea5b5e839080 | -9.09445 | -50.61052 | 2026-06-06 05:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c872f46d-435b-34fe-b0b1-d54890e94dc7 | -11.05276 | -56.93049 | 2026-06-06 05:46:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ba514ae-806e-3bbe-b69b-9c7b37576bce | -9.08723 | -50.60963 | 2026-06-06 05:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 13d6299f-0954-3ea3-86fa-b2af54c1933a | -9.16938 | -58.06976 | 2026-06-06 05:46:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b32b80e-a7e8-3fc1-850a-ad960512c060 | -10.85171 | -53.74109 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62eb9765-4a48-3fb9-9dc9-aff48d301270 | -10.57439 | -57.31829 | 2026-06-06 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bffd56d4-be64-3cac-b7ca-9e2cb88aad17 | -9.07934 | -50.60284 | 2026-06-06 05:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75215eae-800b-3c25-a192-b95abaa4ad90 | -10.84442 | -53.74976 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf012d54-15f0-3232-9c63-e37b3e587f14 | -10.8523 | -53.73634 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72d120d4-e241-3c6d-9f9d-2103a5807bf4 | -11.00323 | -54.31581 | 2026-06-06 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f09abb2-d9f4-375f-8018-ee3a4b7a2e84 | -11.63625 | -55.17554 | 2026-06-06 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cd22994f-2a06-3b9a-ab12-d9adaeeb403d | -13.4988 | -56.56798 | 2026-06-06 05:48:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7985c309-cf73-3dc7-a16c-376daed70f6b | -14.45909 | -54.89291 | 2026-06-06 05:48:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 999adae5-9283-3c65-9c30-1732a52938ae | -16.59447 | -58.23276 | 2026-06-06 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bf386abb-caec-3b71-be5e-c09689218860 | -14.76859 | -52.6796 | 2026-06-06 05:48:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68e069d1-2ddd-3e3d-a2ab-67472c0cb6b7 | -14.21565 | -57.42641 | 2026-06-06 05:48:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97eba9e0-a9da-380c-b3a9-f137053ce4f9 | -14.25257 | -58.43645 | 2026-06-06 05:48:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b0004c9f-3ed4-382f-adca-38271c5dfbfc | -16.59562 | -58.23346 | 2026-06-06 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| c753e961-10af-3d9e-be47-4a46bbbc3020 | -12.77202 | -59.00756 | 2026-06-06 05:48:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cfdd6642-394a-32b8-94f0-750c99d0778d | -16.5987 | -58.23895 | 2026-06-06 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 70dcce00-88b2-3b63-9002-99b612604cb3 | -18.00038 | -54.28428 | 2026-06-06 05:48:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cf279f1-b733-3005-970d-a7af6f44f2f6 | -18.00091 | -54.27869 | 2026-06-06 05:48:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca8ea694-9f15-3c35-8b5b-9a299b1feb4c | -16.13496 | -58.49194 | 2026-06-06 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f488b554-cf59-38ea-b391-00da1f1b0adf | -14.45957 | -54.8886 | 2026-06-06 05:48:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5e260cd-6f1c-3b95-8580-621db147831f | -16.59938 | -58.23341 | 2026-06-06 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 50b7f285-a639-3d76-8e15-723142735bb3 | -13.498 | -56.57077 | 2026-06-06 05:48:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 40bde4a4-74d6-314b-af46-645bc939d27d | -16.13559 | -58.49522 | 2026-06-06 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 33db8eaa-5b1d-346c-93d6-deda0feb0cf0 | -14.46552 | -54.88925 | 2026-06-06 05:48:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17bb5bba-43d9-3dee-b3a0-283d61cfa1c8 | -13.49353 | -56.56729 | 2026-06-06 05:48:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3edbeeb-2d79-35c9-9d9d-f1a043f28d3f | -13.4984 | -56.5674 | 2026-06-06 05:48:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f92edddb-a9af-3adf-932f-4f394ce4a599 | -14.24662 | -58.44584 | 2026-06-06 05:48:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5a27329-8ed8-355e-adcd-71e48a80387d | -14.20988 | -57.43174 | 2026-06-06 05:48:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ac1b5c6-3a3a-36e8-9486-3be7cba617b5 | -12.77259 | -59.00319 | 2026-06-06 05:48:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68c3467a-6215-3c64-800a-a01dfb7a6655 | -13.49274 | -56.57005 | 2026-06-06 05:48:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 925018d4-24b9-3a94-99c8-ce89aed93612 | -13.49837 | -56.57133 | 2026-06-06 05:48:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ee71d8d-538f-3212-8aef-fb27ac8672f7 | -16.13976 | -58.49259 | 2026-06-06 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README13.md)
