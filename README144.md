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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23070677-b66c-3cd6-8baa-b9a93e8478cb | -18.70814 | -57.32037 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| a1f74d0a-a892-33d9-887e-5a6506cf26ea | -18.70753 | -57.32562 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.9 |
| 44363b86-5ae9-33ce-94b7-097aa3753fc4 | -18.704 | -57.31452 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| a3d4f067-065f-319a-b457-5fceb1a07fff | -18.7034 | -57.31977 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b3a60823-fb61-3e00-99a6-e0df7be94f01 | -18.70279 | -57.325 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.1 |
| 60f1327b-ae03-3f8b-915c-6857dbaaa04d | -18.70219 | -57.33025 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.1 |
| f074cf6d-c9e2-3e48-8d7c-c49b39364206 | -18.69866 | -57.31916 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b62e4b8b-9330-3f73-9d0e-ed508a5fb324 | -18.69806 | -57.32439 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.1 |
| 4bc33034-8267-3186-ba4f-6b27d9ecdf2a | -18.69745 | -57.32962 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.1 |
| dc43fff8-825b-3b6a-9d84-e974dd2b1e17 | -18.69332 | -57.32378 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 3e6e4f81-c873-375a-8ee5-6514ab811a98 | -18.69272 | -57.32901 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 6bcabaf4-6a2e-3ccf-a2fa-bea68eeca933 | -18.68799 | -57.3284 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e62f1896-9900-32ed-9759-947d2f192baf | -20.7758 | -57.89309 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ce5ea37c-38a4-3fb7-8b73-f41cfe9f6f27 | -18.59797 | -53.04166 | 2024-10-01 05:31:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a3e9904-727f-3dd7-914e-2f6da69a7c03 | -18.59176 | -53.04084 | 2024-10-01 05:31:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19dce6dd-5124-3c7a-8ddf-a95956edc938 | -21.69745 | -54.79326 | 2024-10-01 05:31:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b44ef8c6-c312-3583-ae5d-8ff54fa348c2 | -21.69707 | -54.79757 | 2024-10-01 05:31:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35c2ade2-f742-3aad-83a6-50e61b4716fd | -21.69127 | -54.79705 | 2024-10-01 05:31:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c6ab8cc-c4a3-3088-960c-007f0cc51e5c | -21.69089 | -54.80132 | 2024-10-01 05:31:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9627023-c0c3-3351-a586-ab68198138f1 | -21.65084 | -54.8512 | 2024-10-01 05:31:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3f03f67-739b-37d3-87e8-8f4c6a27b9e8 | -21.65045 | -54.85533 | 2024-10-01 05:31:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7ef15c8-e20b-36e3-ae28-2643053d07aa | -21.64507 | -54.85059 | 2024-10-01 05:31:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dbd1be6-692b-3895-bddc-b3af8bfe8689 | -21.64469 | -54.85475 | 2024-10-01 05:31:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95dbf5c9-56b1-37e0-8e84-f7acd8a5db06 | -21.4195 | -57.24338 | 2024-10-01 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e2d0896b-0123-3d8a-b6b8-10be879f03a3 | -21.41815 | -57.24298 | 2024-10-01 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 286bf3eb-e49a-36ec-b6d9-ce86d0ffcb92 | -21.41318 | -57.24274 | 2024-10-01 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8196eaad-cd95-34e8-b9ef-64d73191a5ee | -20.75898 | -54.82558 | 2024-10-01 05:31:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75e4167b-1479-349f-9bda-cbaff0463d34 | -20.75325 | -54.82514 | 2024-10-01 05:31:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3e13c2e-26eb-3205-8268-3db3f6fa8a6f | -19.97885 | -55.48671 | 2024-10-01 05:31:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c285d71-15ef-35b3-b5e1-22a6104ad78b | -19.97345 | -55.48576 | 2024-10-01 05:31:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 300d0e0f-6217-3d42-9422-6dcc0f6ae111 | -19.97308 | -55.48939 | 2024-10-01 05:31:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f199599-921f-3a6d-a233-d7188895636b | -19.97276 | -55.49252 | 2024-10-01 05:31:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48fc1a23-77d0-3346-b771-1bfa53e489a3 | -19.97245 | -55.4956 | 2024-10-01 05:31:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fbb54ea-08f7-3fa6-ba51-a77e136b9c74 | -19.96772 | -55.48804 | 2024-10-01 05:31:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce3bd806-850c-3843-a426-62a078d5114a | -19.9674 | -55.49119 | 2024-10-01 05:31:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98e41a86-ba4e-3d69-85d4-ea056e77b820 | -19.96709 | -55.49426 | 2024-10-01 05:31:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79ce4a49-a6db-3e17-8a88-695757a6c1f6 | -19.96677 | -55.49743 | 2024-10-01 05:31:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1707e0e5-ccb2-394a-b35e-9760fea9dd64 | -18.87578 | -54.50426 | 2024-10-01 05:31:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 680dec4d-20b5-3ff2-ad3e-fa08577754d3 | -16.66642 | -50.59206 | 2024-10-01 05:31:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9db96fac-293d-3a74-919a-652fc01193fd | -16.66578 | -50.59901 | 2024-10-01 05:31:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f61940fb-2067-37f8-972f-0c385d99e7dd | -16.65877 | -50.59795 | 2024-10-01 05:31:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b29747ff-b7ee-3ba0-9c0e-2ba097a89246 | -16.62816 | -52.58232 | 2024-10-01 05:31:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11f27586-a0e5-3794-ad1d-d49a3466ee32 | -16.62433 | -52.58094 | 2024-10-01 05:31:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01508d78-8370-3bd7-a317-287b83eafadc | -16.62381 | -52.58595 | 2024-10-01 05:31:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77586a89-e67b-3917-a526-402ddbb46edf | -16.62193 | -52.58113 | 2024-10-01 05:31:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c2f06cb-082a-341d-8373-9f45554c89bf | -16.10103 | -50.34018 | 2024-10-01 05:31:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1a2cdedb-4a43-399a-9c42-f18eaf8c6963 | -16.09755 | -50.4142 | 2024-10-01 05:31:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95d9ad0e-2529-3e50-bdf4-d14154fcbc51 | -16.09705 | -50.33921 | 2024-10-01 05:31:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 850ef15b-2a36-3551-ab0b-a50c90cbc54e | -16.09456 | -50.40827 | 2024-10-01 05:31:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b67c364-4fe1-3f3d-bab4-ef91d0fdc050 | -16.09444 | -50.33406 | 2024-10-01 05:31:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38930ee3-35d9-38c9-8c21-be714a90951d | -16.09375 | -50.4168 | 2024-10-01 05:31:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a7b271e-cbda-30c2-820c-9a351acc85e9 | -16.09372 | -50.34171 | 2024-10-01 05:31:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f39db53d-665a-3f38-a141-abcd2293d8af | -16.09232 | -50.39266 | 2024-10-01 05:31:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 07443b90-e983-3da1-8a0b-4594bbdac683 | -16.09166 | -50.40004 | 2024-10-01 05:31:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82b8dd61-ecdc-3e26-b7ef-e56b47f07a4a | -16.09105 | -50.40701 | 2024-10-01 05:31:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3dff8328-5d10-38bb-827e-46a567012695 | -16.09047 | -50.33244 | 2024-10-01 05:31:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1c220c7-792c-3673-8178-10f49a558f72 | -16.09043 | -50.41399 | 2024-10-01 05:31:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e6002dc-64ad-3a49-b28f-f73eb4f16d6f | -16.08871 | -50.39457 | 2024-10-01 05:31:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8b88898-813d-35c0-a637-9d23af379bef | -16.08101 | -50.40042 | 2024-10-01 05:31:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c360bf09-b8aa-3f03-8e36-debca2f628d4 | -16.07588 | -50.37884 | 2024-10-01 05:31:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3a58b17f-e191-30f1-bfd5-789ecf88e06d | -16.06953 | -50.37027 | 2024-10-01 05:31:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 11fdc19c-c5f2-3225-a65b-8611da0a2a90 | -17.21027 | -57.37558 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1c5d72ed-69c2-302a-a637-d4a8ec3c05b0 | -17.20564 | -57.37496 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4dc3a1ff-022c-3927-b3ce-b5a27a9c7ec5 | -17.20505 | -57.37988 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6d314305-be85-31fc-913d-b39f7358a4b7 | -17.20043 | -57.37926 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 33746324-c75e-3e0a-a8ab-217311ff29ea | -17.19984 | -57.38417 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 62a67343-b438-321b-92ed-c1e9cec79194 | -17.18721 | -56.1957 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 482f017e-7bbd-3650-8ad0-a46127d15ff7 | -17.18651 | -56.20159 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 85e3f83d-a299-3396-808e-5e6a8534d982 | -17.1864 | -56.19605 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 71e7cb68-843a-3de5-9458-32885b192bd3 | -17.18581 | -56.20749 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| d42915a8-0ab7-3c98-a9e5-396de7626c68 | -17.18574 | -56.20195 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 35963d37-bfb0-3345-bce0-90e6851f1dc3 | -17.18511 | -56.21337 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.1 |
| ef18f20b-7b7d-32c5-9342-94ba20d74b1e | -17.18508 | -56.20787 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| e096e3b8-e4ba-3b29-819f-9774004dd028 | -17.18443 | -56.21376 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 28929285-8249-342f-a041-0e16bf1e9ab1 | -17.18221 | -56.19507 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3c5ee48c-9aec-3e4d-b4a2-f2a2fd780761 | -17.18207 | -56.15305 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c9ad77c4-100e-3655-a3b2-e5b5f166ed6e | -17.18151 | -56.20096 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| dfd8aa83-a7d4-37f6-8ba6-34be92937bfd | -17.18139 | -56.19541 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 9ad32022-6e1f-380d-9502-24a4a20e4477 | -17.18138 | -56.15898 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e1e1afef-a252-3cee-bafa-f070f7b2248f | -17.18081 | -56.20686 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1a5f0665-b6a3-3b5f-b056-fe7558bcada1 | -17.18074 | -56.20131 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 20c4c7de-1d75-30d2-a57e-44e69d32cbff | -17.18068 | -56.1649 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| d55987a4-fc38-3506-8f24-e84096371a45 | -17.18011 | -56.21275 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 86fd9e62-bac2-39bb-8ac6-615945412502 | -17.18008 | -56.20723 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| c1903b8b-cc5f-364d-935c-45806f8881b5 | -17.17998 | -56.17082 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| bc99e15f-886b-3344-8d0e-8d78fc86a62a | -17.17943 | -56.21313 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| ddf1c190-01ca-3110-8286-61d965d72176 | -17.08916 | -56.72771 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| fb4e5c28-9a24-3054-9986-94796f575853 | -17.17942 | -56.21862 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 50c80881-f3d1-334b-81eb-34f9cc919084 | -17.17929 | -56.17674 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 37bce4b6-9224-3e2c-a140-e9d51bae91c0 | -17.17878 | -56.219 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| c37e5ac3-ad85-3677-b369-21639e71d308 | -17.17706 | -56.15243 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 82c6bf87-4a15-33e6-8d19-73185b01c7a6 | -17.17636 | -56.15834 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f56c8e0b-9019-3d26-b19a-bfc78eb4e9b6 | -17.17581 | -56.20623 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| bf33a857-0eb3-3447-9d4e-a5dda75d9375 | -17.17567 | -56.16426 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 071cc410-b0de-3cef-b7fe-c778d211816d | -17.17512 | -56.21212 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| fbc20bab-b7b5-323d-b7f8-3c4c84100227 | -17.17497 | -56.17019 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 28a6f448-58d0-3eb9-a0ad-f5f2d28edf14 | -17.17443 | -56.21798 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| f77c78e0-e577-3587-a352-c7401f151c8a | -17.17428 | -56.1761 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b49aa10d-fbed-37e5-89e2-1f17e28c9baa | -17.17374 | -56.22382 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 16d7b7ec-f6b2-32a7-b492-3e9c1985284a | -17.17359 | -56.182 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |


[Clique aqui para ver as próximas entradas](README145.md)
