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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76df48c4-7a8d-3919-b964-8cd71cf92504 | -8.90346 | -50.0488 | 2025-06-03 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b387e2f-090e-3028-a0e1-8343df3ae7a1 | -9.60702 | -49.01832 | 2025-06-03 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f8ecb95-e2ae-3916-84fb-498af56e7332 | -8.1972 | -49.80139 | 2025-06-03 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce5f5f3f-1bfb-37c1-8588-8593862e97b2 | -12.29622 | -43.54649 | 2025-06-03 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4df265b7-9a08-3d49-92e2-0abdf43441e0 | -15.69847 | -43.42141 | 2025-06-03 04:19:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bccbbc12-b449-3236-907a-fc4861c36043 | -14.86737 | -45.12133 | 2025-06-03 04:19:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a23b946a-a41c-38ee-9441-fb7d1ea3bfae | -5.49765 | -35.58306 | 2025-06-03 04:19:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 23dca927-9af2-3339-a354-7e9ff0ac199d | -10.3604 | -48.73007 | 2025-06-03 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 425b10e7-5327-3bc2-82cb-1cf251d0acfe | -8.97114 | -47.96833 | 2025-06-03 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c79a7f3-1582-3d7f-a9f9-58c326dd34e1 | -11.92023 | -54.81806 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44c3566c-87f1-3db0-85a3-f4061738899f | -9.11057 | -49.63454 | 2025-06-03 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 029b8c4a-f0d0-3b77-9d95-aad7380eb8ba | -10.24683 | -47.60994 | 2025-06-03 04:19:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0447b7c-ba35-36a2-aa00-97b617d3470e | -9.38791 | -48.42687 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a403437-7971-3767-a499-7646138733f9 | -9.37564 | -48.41204 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78b4e00e-b635-3892-b9d5-f56eeed25ca8 | -10.68941 | -57.65242 | 2025-06-03 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c75a03c8-306c-39f8-aaf6-5ab54455c6e3 | -9.62386 | -49.09885 | 2025-06-03 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a4a6c64-0b33-3851-82fe-f50d0a737b8a | -8.91104 | -48.90278 | 2025-06-03 04:19:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a157768-e76a-3eaf-b012-7491944c2edf | -12.0959 | -54.66842 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd222081-7eed-34bb-bde0-c3d74cd6df7a | -14.0184 | -55.14032 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d93a5abf-2f29-374b-aab9-731141b1a64e | -11.57497 | -47.44365 | 2025-06-03 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b78b519c-8e6d-36a0-b584-87002bea0131 | -11.92026 | -54.42423 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a51f0df-4d0f-3019-88e1-972a5db69e42 | -2.44649 | -47.49536 | 2025-06-03 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7adbb2ae-a664-3de6-9097-2090571c2545 | -8.47117 | -46.50467 | 2025-06-03 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 676a6fe3-cb9e-387c-be56-96fcb8e5e6cf | -11.67533 | -43.78779 | 2025-06-03 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d53eb868-9a4a-3fd2-a3d9-6e73fdc85238 | -11.92137 | -54.41836 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52bc5fec-d20a-3461-ac7e-63950bdc9623 | -9.60258 | -49.0221 | 2025-06-03 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16d287ea-1e1b-39de-a8a2-683f88c23c93 | -9.07202 | -47.15351 | 2025-06-03 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee814e6c-117f-3121-85ff-f234fe9ced6a | -9.6663 | -48.71198 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0080881d-fdcd-3a48-a7aa-346cc95b10d9 | -12.37537 | -45.91953 | 2025-06-03 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 411baa27-167f-3158-b921-b7bc2d007047 | -8.46781 | -46.50412 | 2025-06-03 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4ff7b48-4fac-34f7-865e-962cb7f41a16 | -13.41832 | -43.75314 | 2025-06-03 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c2d482b-dbaa-336e-82bd-de691c10dc17 | -14.03092 | -55.13031 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cf7f9bf-42f8-321d-ad9f-0964be66b938 | -10.46522 | -47.94349 | 2025-06-03 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6e876985-8746-38d2-b799-b271a148af0b | -5.50289 | -35.58391 | 2025-06-03 04:19:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bbd0e826-883c-3763-bc6d-e6e8319b20f0 | -9.19768 | -49.69223 | 2025-06-03 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb636d9b-dbd9-3cfd-a2d7-4623e85b96d3 | -12.63892 | -48.1695 | 2025-06-03 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f60a3f8a-449f-38bd-a3d5-cc23fab40078 | -11.57775 | -47.44791 | 2025-06-03 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8f797826-1729-36ae-8a9b-db33893923fd | -12.36168 | -54.16942 | 2025-06-03 04:19:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fbde6f2-4572-3a65-9e81-4f2a12814a37 | -14.87965 | -47.83161 | 2025-06-03 04:19:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fc0155d-2069-37c1-97ef-a42cd86f60af | -10.82133 | -56.94553 | 2025-06-03 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 646bbb9a-0117-3a38-916e-a0ea1a0f403c | -12.66868 | -58.22189 | 2025-06-03 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f283d160-1512-33d7-87b6-a4ba8720f0f4 | -18.8679 | -53.6218 | 2025-06-03 04:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8b33a5eb-7a7b-3c28-8eb1-24ee4000471c | -18.8875 | -53.6402 | 2025-06-03 04:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 7a0d1dc8-8103-36e9-877a-b19031a9dc76 | -18.8675 | -53.6434 | 2025-06-03 04:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 115fabb4-c375-3c45-b541-2087121d27d0 | -18.87004 | -53.64663 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ee94293a-3bac-30fc-910a-501ff2951bcc | -18.87655 | -53.63427 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6c877c3f-219d-3a0d-8788-2ca6aef72d3d | -20.95286 | -56.60636 | 2025-06-03 04:21:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 576bded3-8ae6-3614-821f-a6773f58332c | -21.19637 | -44.93753 | 2025-06-03 04:21:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b769eca4-e08a-399f-a900-2b1efb64c424 | -18.87503 | -53.64332 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 884311cd-a715-3bea-8e0d-32cca5348e40 | -18.18201 | -49.14107 | 2025-06-03 04:21:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1f8b8f34-f69b-3bb8-a0ae-3c0e00d8eed3 | -19.45455 | -45.30665 | 2025-06-03 04:21:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| facdecf9-3745-3582-9190-3e3964ba53b0 | -20.71342 | -56.63348 | 2025-06-03 04:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79c19570-178f-3707-b337-121787df0681 | -20.45328 | -44.18325 | 2025-06-03 04:21:00 | NOAA-20 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1ac96a29-7d80-3034-8940-b9f15253f123 | -17.7942 | -45.03081 | 2025-06-03 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb981633-2069-3089-9e7e-658419df1233 | -18.83928 | -53.60126 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2368a6d4-c359-3a6b-930a-5e6da9b9511b | -20.22937 | -45.71857 | 2025-06-03 04:21:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e8e92a6-e320-3d6e-9eae-d37fe6a869a4 | -18.86398 | -53.63234 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 99544a81-80b2-37be-975d-19d82c20a27e | -21.24472 | -56.15899 | 2025-06-03 04:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1e3f91a-7231-3763-8599-5f6b17f9cb71 | -22.67476 | -42.85379 | 2025-06-03 04:21:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b96bc65a-9a57-3593-a6fa-77192a98b4ec | -18.84007 | -53.5971 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 606fca11-636e-3c07-a2ec-70488e554509 | -18.87161 | -53.63824 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 34.0 |
| b4af9e88-1b4e-39c9-93c4-a30f3c3730b1 | -21.34702 | -48.67104 | 2025-06-03 04:21:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4049f121-e0f4-3041-bf32-100457209421 | -20.57858 | -44.575 | 2025-06-03 04:21:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4bc685fa-df41-3537-99b5-173ac5875f9c | -21.13123 | -47.80058 | 2025-06-03 04:21:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d803e796-0848-3f1c-8a09-a9602d50b80d | -18.87413 | -53.64671 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8590d767-430e-3ed9-9857-26027269203c | -18.86241 | -53.64067 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 33086307-1ec7-3834-ad4f-e44fa0c10b36 | -20.68874 | -56.67709 | 2025-06-03 04:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 706a87ea-e2fc-33e0-a4c8-c5f67e4b7ed5 | -18.87083 | -53.64243 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 2787d5c1-d06e-373c-a251-0ef07e6df57e | -20.58595 | -49.50459 | 2025-06-03 04:21:00 | NOAA-20 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb40658e-cef6-3ed3-8cd0-eb3f49e01f4e | -18.87581 | -53.63915 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 215ade38-cb1e-3f7c-897c-66a14189ab60 | -18.87915 | -53.64342 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 9c39b9dd-1c40-3209-b9db-76bd94303c3d | -18.83808 | -47.681 | 2025-06-03 04:21:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a88f7002-374f-30f8-9e71-93353f47a588 | -18.8674 | -53.63735 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4cf81837-36de-3703-bb8d-23d4c0d360a2 | -22.61767 | -47.39737 | 2025-06-03 04:21:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e7c6de2b-90af-3885-bf0b-3e5df241dc85 | -20.72445 | -56.62991 | 2025-06-03 04:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ce6ff3a2-8efc-3aa6-8180-07aaa4af7949 | -22.39598 | -43.1112 | 2025-06-03 04:21:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 94d57ef1-273a-3bfb-b4b5-7d65b7d14ac5 | -20.95773 | -56.60749 | 2025-06-03 04:21:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24044be0-fb30-3768-a1d9-3c253111f360 | -18.87239 | -53.63411 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a47e0e59-caf4-377a-b801-9a0f2e1b3c48 | -20.22592 | -45.71801 | 2025-06-03 04:21:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8e376d1-2f9b-347b-b37c-3b6f20ff1d55 | -18.8632 | -53.63649 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2306cbf1-91a8-316a-8395-5f18e7d33041 | -23.33956 | -46.77103 | 2025-06-03 04:21:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 50fdf32b-d939-3cb4-829f-88554753fece | -17.11128 | -49.1389 | 2025-06-03 04:21:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54e9aa2a-ddbd-3cce-92d3-24b49e2d62f8 | -22.61825 | -47.39355 | 2025-06-03 04:21:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7747659b-97a6-3a04-bba6-0b07b4e329aa | -20.71954 | -56.62883 | 2025-06-03 04:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8457fcd2-9d4e-3060-9c8e-4dbcde380caa | -18.87425 | -53.64751 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bcb01f1d-dbab-301d-b8fd-c0c422923036 | -23.4176 | -47.0503 | 2025-06-03 04:21:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 243ef409-ad32-3375-9a32-6076fcdbb44e | -18.86583 | -53.64574 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 20808981-7e81-35e9-87fc-a319c1be6def | -20.71837 | -56.63442 | 2025-06-03 04:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cfd83f4d-899d-3e4d-ad08-2c196f0b6e8f | -20.71462 | -56.62778 | 2025-06-03 04:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fb0aab24-c8c5-3fe7-aa76-3208a46c40e4 | -18.86662 | -53.64154 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 131b9351-d63c-363c-ab55-1b9c65e41db4 | -18.87495 | -53.64253 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 26.2 |
| a404ec06-f1c9-3edf-9fd1-7e57e1b09dbf | -18.83477 | -47.68042 | 2025-06-03 04:21:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a965a8f9-691f-3753-9b4d-e954e9561102 | -18.87576 | -53.63837 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 1aef5a89-8fb5-332c-933c-066c13c248bf | -20.68821 | -56.67534 | 2025-06-03 04:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e3bc2bc0-009d-3325-951e-dfc9dbdaef9c | -18.87658 | -53.63503 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 69580395-8f25-376e-bfb1-cdf06e70e7aa | -18.86819 | -53.63321 | 2025-06-03 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 843ced49-169e-3e9b-9745-45de734bdd83 | -17.44418 | -48.91259 | 2025-06-03 04:21:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c62bc906-92f4-3f56-9868-d9fb27a8c1db | -20.68994 | -56.67144 | 2025-06-03 04:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f54b071-6396-32c5-bebe-8147c3d84d60 | -20.0043 | -47.88583 | 2025-06-03 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1daa9a18-05f1-3c8e-86af-3d59421d48ab | -22.39516 | -43.11184 | 2025-06-03 04:21:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
