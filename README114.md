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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa71e211-4a82-32a2-a0e0-434ceecb64a7 | -19.61971 | -42.25074 | 2024-10-04 04:34:00 | NPP-375D | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ecd03fde-ac6e-39e4-9394-c9be4e6739b2 | -19.61406 | -42.25568 | 2024-10-04 04:34:00 | NPP-375D | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 10933c3c-cfe0-301b-be20-610e6032a015 | -19.61343 | -42.26151 | 2024-10-04 04:34:00 | NPP-375D | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bdc3f6ef-a309-3288-8b71-0190d6c0bb31 | -19.56268 | -42.72414 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bbd7732a-c95e-35e9-a805-b9a963b88720 | -19.57097 | -42.73861 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1789742c-f0fd-330c-838a-2541bc969b77 | -19.57041 | -42.74365 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 67001e2b-f8d9-3264-ac83-9f931324d34c | -19.56755 | -42.72488 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 12885fbc-1724-34e6-9823-ae8497fecab3 | -19.5059 | -42.89097 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 34e102a0-e07b-3acd-859e-d22d1e08436b | -19.50533 | -42.8958 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 12c2acc0-9c20-31b5-ab92-8ef38e8d58c7 | -19.5047 | -42.89297 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 603d8867-7d78-3e0c-8c8b-fb37cd8d9524 | -19.50416 | -42.89788 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9eda4785-c3ef-391a-801c-9a8f38de4afb | -19.50221 | -42.88054 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 725ff172-461d-3016-bebf-68a362c22c04 | -19.50158 | -42.88597 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6914ac02-3a97-3d40-af7f-9da076240a3a | -19.50102 | -42.89079 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d1da6a8b-0e0a-3075-b9e7-be8da969e016 | -19.50092 | -42.88282 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a07c6983-9da1-3e70-906c-a245b29d7b71 | -19.50049 | -42.8954 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ddc281e9-6b87-3d50-bffd-0babd059ceea | -19.50035 | -42.88799 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d77dc529-c7ef-3e2a-8964-b3aece199e31 | -19.49985 | -42.89259 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c70ea356-5931-3b8f-9ae4-09ac01b26823 | -19.49932 | -42.89736 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 67cec1d6-fe40-3a5d-b9b5-eb405a6b45fc | -19.49729 | -42.88072 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 8fd073c2-f2f5-3d63-8252-c0c6c0dbc09a | -19.49671 | -42.88576 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| a11d0b97-0bf2-3078-b7bd-902a585567db | -19.49667 | -42.87691 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f92afa10-4843-3bfd-bd22-ab4e3e78d276 | -19.49617 | -42.8904 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| 6b98d443-6bcd-3b5a-be7d-d09dbd4ddb7a | -19.49603 | -42.88282 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 2ee94758-40ac-352f-910c-1e368354f39a | -19.49565 | -42.89491 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 0d2a021e-5c97-3deb-a78a-cb740f873f58 | -19.4955 | -42.88765 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 5273b0db-a4e0-3e0e-9761-ee40886c5de9 | -19.49506 | -42.89996 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| ee8e3f72-5a73-319c-b02c-1858bff1775e | -19.495 | -42.89219 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| d54088ed-8d09-30d8-9dff-3b60fedf48c1 | -19.49449 | -42.89686 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| 8afa73e9-f4c8-39c5-a4c3-49a18e4dcd7e | -19.49393 | -42.90202 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 44efcfbc-ff42-3b78-80ec-0aa8a26656e7 | -19.49243 | -42.88044 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| b09d097b-64f3-379d-a2eb-f44b327548d7 | -19.49184 | -42.88549 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| 76adecff-9891-3085-8622-bb13f6acf021 | -19.49182 | -42.87648 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 8f7c35e9-adad-3ba5-a88e-e18484c95110 | -19.49131 | -42.89015 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| 42995bbd-7c8e-34eb-b8b3-c378371a18a7 | -19.49117 | -42.88244 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 4fa7f02d-3f92-32da-be3b-67e4c247fbac | -19.49079 | -42.8946 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 3cf4474c-b35e-3052-b609-abb051534926 | -19.49063 | -42.8874 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 5bae3be0-58bc-309b-ad66-9f36a4e33628 | -19.49022 | -42.89953 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| e4b24226-0cdd-3670-829c-6f901ceaece3 | -19.49014 | -42.89193 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| 37c24de2-6dab-3cb8-ab26-1ef20059cdca | -19.48964 | -42.89647 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| b03d3b9f-79bc-342b-abfa-43f93da7fd4e | -19.48835 | -42.87334 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c27f5a7b-6f00-30e2-916c-a9ccd37480b5 | -19.4876 | -42.87986 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2f40b823-b927-3a61-8abc-3effa2d0c949 | -19.48699 | -42.88512 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d7ec4eb2-7d5e-3ad3-9c47-360dd86290a7 | -19.48643 | -42.88991 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7cd2af7c-094e-3a73-974b-95a8115c067e | -19.48592 | -42.89439 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a38cfc52-e9e0-30dd-879d-4f33117a3c6a | -19.48351 | -42.87281 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0edee937-e9b7-3366-9da5-a8389dd2aaaa | -19.45108 | -43.06946 | 2024-10-04 04:34:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 13f4918f-c310-3a50-80e7-02690d985c97 | -19.44512 | -43.07924 | 2024-10-04 04:34:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 422cf63d-e6a7-31d9-94de-06dedc9a34db | -19.44457 | -43.084 | 2024-10-04 04:34:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a1e10649-035f-37d2-bf2d-82a2ed19f296 | -19.44156 | -43.06823 | 2024-10-04 04:34:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| efc76255-4849-3d7c-b9e5-e76af74f049c | -19.44099 | -43.07318 | 2024-10-04 04:34:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 18d79439-5e62-33a9-a60d-8373bbeba4dc | -19.44041 | -43.0782 | 2024-10-04 04:34:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d7065a06-7a7a-3acf-a23c-5531b4f117f6 | -19.43738 | -43.06246 | 2024-10-04 04:34:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a79e3ae3-2863-3f3b-bda6-828b79fc50a5 | -19.43682 | -43.06738 | 2024-10-04 04:34:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6069bc80-1053-3c03-9c77-7d7e74c31603 | -19.57244 | -42.7255 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 45b46b22-cbf7-37ed-b561-bb56d50c4127 | -19.57168 | -42.73223 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 644cbcab-0815-3d62-a30c-03a62ef8e03b | -13.29832 | -42.31069 | 2024-10-04 04:34:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 62d06c7b-c773-319d-8ca4-a23ad005597f | -14.3311 | -42.34431 | 2024-10-04 04:34:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 28856809-ba4f-34ca-82f6-abe0cd921f3c | -16.47532 | -43.8135 | 2024-10-04 04:34:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62b27873-d2a3-3372-96d3-67177df21d08 | -16.4747 | -43.81835 | 2024-10-04 04:34:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85e093d5-32ff-34e2-9d3e-ca32699fc418 | -16.47041 | -43.81731 | 2024-10-04 04:34:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cb2b3dd-7a1c-30e5-a87a-689477a1f04e | -16.34743 | -43.69568 | 2024-10-04 04:34:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1ca387e-c36e-39bc-906d-7be38658a385 | -15.95646 | -43.36732 | 2024-10-04 04:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbf13470-7941-3590-bb0a-efe77aecbe50 | -15.9559 | -43.37183 | 2024-10-04 04:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c20fefc7-8867-3f52-967f-7c4d492b7cc8 | -15.76975 | -43.5792 | 2024-10-04 04:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22493fec-9372-3fd6-97ac-4e82f0a11eb4 | -15.59223 | -43.64756 | 2024-10-04 04:34:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04c6baaa-8f31-3d46-84d7-e15651e50704 | -15.59169 | -43.65191 | 2024-10-04 04:34:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17c78c6c-6ded-3f1d-a7de-0f53741cd039 | -15.30291 | -42.53543 | 2024-10-04 04:34:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc5af1a6-3178-3a24-a236-9ac6ace8577c | -18.04523 | -43.32781 | 2024-10-04 04:34:00 | NPP-375D | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd4ae1f5-3e21-301a-9641-3e9b08bc692b | -17.91966 | -43.44113 | 2024-10-04 04:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bda60b2e-66b9-3994-9fca-30d813410080 | -17.91509 | -43.4406 | 2024-10-04 04:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b76cfdcb-bbb1-3441-a4b0-c3bd1241d9b2 | -17.91445 | -43.44585 | 2024-10-04 04:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b9ff4049-a94e-32bd-b7fa-400fc3c26bd7 | -17.91051 | -43.4402 | 2024-10-04 04:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a6d558f-dca3-3e1f-8ceb-0f09eb1bbf7c | -17.90989 | -43.44534 | 2024-10-04 04:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10b7c10d-8bb3-3a53-b15e-b741c786c7af | -17.24639 | -43.21759 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 119b0f79-49d4-3ef4-81de-6c622a03ea7b | -17.2418 | -43.2171 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8fef631-db8e-38c9-bb86-04b390a9e392 | -17.23803 | -43.21532 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d591b082-e789-3df2-bc72-ab983136dac6 | -17.2372 | -43.21665 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17c6c1db-9543-3c7d-9b0f-585ccf9a03e2 | -17.74444 | -43.81442 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 41.4 |
| cad0c674-7205-3d0c-a48b-7479dd6fa42f | -17.74393 | -43.81855 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 943e0022-1385-3a20-a831-66e45fb4cf8f | -17.7434 | -43.82279 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| e805d2b7-7b05-3796-b3bf-006ff71c392c | -17.74055 | -43.80943 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 497d382f-4ad2-397b-9a29-4f0b441baef2 | -17.74002 | -43.81369 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 805cfb0f-9484-3e97-96ad-87f6046d49a8 | -17.73951 | -43.81786 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5ecee05d-14be-3ed5-a23b-9cff22e7105c | -17.73899 | -43.82207 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a7e26c57-94d5-3a44-911c-0ba72e1e30f8 | -17.73776 | -43.79543 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1be0ce32-b94b-3a62-adf9-69a29b6fd133 | -17.73721 | -43.79992 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8fc01f7-24b9-3129-9d1a-cd8382d8a0ff | -17.73666 | -43.8044 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e4eb343-01bf-3f8b-a3d8-bc3ac49f1d52 | -17.73612 | -43.80877 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26ea651b-ac44-3f86-865e-d059abdb15ae | -17.7356 | -43.8131 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 40682c65-d4c3-37ac-aee7-a4ec9599677c | -17.73508 | -43.8173 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cf35777a-ec4f-3dbf-8023-dfb7a9de0c14 | -17.73456 | -43.82152 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 66d1965a-211e-3181-94f4-257a76ce6400 | -17.73335 | -43.79466 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fb1afeb-b1d0-33d7-9284-3627e4a34e20 | -17.73279 | -43.79924 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95f2cc56-265f-39e0-b8c9-f35a3c9a1289 | -17.69581 | -43.77887 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e905df2-6a02-3198-a308-ef54e680e50d | -17.695 | -43.77627 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 306ae91d-c7e7-3257-b0c4-bd220bb019f7 | -17.69446 | -43.78073 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1973982f-036d-3b09-b2ab-cbe16d61d20b | -17.69136 | -43.77842 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f58275fb-bed3-38e1-87ca-71d3b41f8f5c | -17.09588 | -43.80338 | 2024-10-04 04:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fe29553-3734-3184-becb-2b286bcbbc5c | -16.68051 | -43.88194 | 2024-10-04 04:34:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README115.md)
