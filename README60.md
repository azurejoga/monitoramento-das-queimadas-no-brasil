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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03cda3ee-cee8-39bc-b432-9ab06bacc651 | -14.04623 | -47.98802 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a71a895c-0fc9-3713-a5f6-74370af0605d | -12.76405 | -46.87859 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04710de8-881f-3ff5-82fe-7d3fa51ed37c | -13.20746 | -47.32174 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a50fbd50-b1d1-3b31-92d4-f0572e86c13f | -17.51019 | -43.48453 | 2025-10-01 04:21:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c4a85d1-7584-3546-a6ae-1a0b1524b87a | -11.46481 | -45.00245 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60338e41-dd63-3ba0-94db-eb6940b7ca55 | -14.92151 | -47.82021 | 2025-10-01 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48aff394-4091-3219-b58b-c2ab6142f000 | -14.56706 | -48.22047 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 135eb5fa-f8c9-3f6e-b672-f86aaeb90673 | -17.49599 | -43.47765 | 2025-10-01 04:21:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2c71a1ef-50d5-3951-bce0-994255c59140 | -12.11088 | -44.18316 | 2025-10-01 04:21:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 466ec449-3bff-3c8c-b0ca-8d5ba62f75a4 | -14.7162 | -48.27204 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e06569a-a84d-3169-a7ac-6bd5ed5f0955 | -13.03559 | -48.67474 | 2025-10-01 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c1e013a-8871-37b6-af73-52dc9f719833 | -15.26117 | -47.88929 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cbf7923-213d-358a-85da-0b56d2633b00 | -15.17721 | -46.39862 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 320cf467-a15b-3899-b3ad-f4a3e3a0b7ab | -11.3858 | -45.07391 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 343f3614-4d9c-3ebd-8de4-5d47738ca52d | -12.24415 | -47.82361 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e70b5582-7c05-3ec0-8400-0f00790d70dd | -11.13919 | -43.38166 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 21967124-5bce-31a9-9c80-f7db8f1b3cce | -14.98455 | -46.9568 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43ee62d4-45ee-377d-9a55-62ed5275e5d9 | -14.68927 | -48.11883 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 738c4245-3c4e-3f13-bc67-d159e7bd2703 | -13.73758 | -48.81583 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 50fc63a9-a191-3f28-ae0a-006bdef02de7 | -15.84366 | -46.24364 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a1f744-1baa-3520-898a-c0012663ccd1 | -14.54504 | -48.22795 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47083ab4-b6d1-3dec-9ff0-2090f2a12f58 | -15.30533 | -56.79333 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cfefb4ed-2053-3373-8532-55e6d4895d8e | -12.95459 | -46.42522 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e9a612fa-f250-3b40-bf2e-646a24211917 | -12.77382 | -50.55991 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ead34d6a-8052-3396-ad91-142baaf71d67 | -13.37338 | -47.30517 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b1f0270c-7043-3c97-9c73-3cbf5a2d3a02 | -12.80285 | -46.89214 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44ce8377-056c-3424-a551-30ca99f21664 | -14.59264 | -48.29748 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32f8f0ec-3b5a-305c-84fb-00c76c556af1 | -12.62137 | -44.86377 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b916aa75-d260-378b-b11e-3fdb2beae6c0 | -13.37101 | -48.09549 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4424bb2f-094e-3fe5-b771-0630a0975ed7 | -15.21096 | -48.00822 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c2b1545-c566-3b07-9d6a-f72c0c1c0a10 | -14.60651 | -48.3189 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ed8c959-a401-33ff-b57f-8c520b19b9cb | -15.26313 | -56.77716 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f71422d7-2808-31c0-803a-3be7dfc3f73e | -13.33086 | -48.14293 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02ce318a-1520-3638-b6c3-e0d5ccad4c17 | -11.1379 | -43.37845 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a1389785-c975-34f1-bb6b-711ef80e3dae | -12.45624 | -50.21175 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7404e7a4-b56a-3e43-b04c-c870d750cff2 | -10.93419 | -46.505 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7c460af2-9fb8-3410-82f2-a310b03e76e6 | -10.81483 | -45.35711 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28a1a7c3-4f47-3551-b70f-d264d9bcc4ea | -15.27004 | -51.47935 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1abc935b-154b-3f82-9b5b-ba5ff5c7e792 | -14.75309 | -45.773 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56c02e39-fc74-330f-b6ca-be33f8b8c6dc | -15.34375 | -47.84378 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34603806-b6c4-3e5c-bdf5-1596325f1e34 | -12.45889 | -50.2411 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb8e84aa-19c4-34b8-a13f-4a9c79936e41 | -15.52979 | -44.34875 | 2025-10-01 04:21:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bcb2484f-62b0-3a18-a9f9-6b9d89ad3871 | -10.90809 | -46.56226 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69fc40de-f7c5-30d0-9ca4-b7ffcdc0e18f | -10.45105 | -48.08157 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c779a0f-3261-3aff-a0d3-5bdd86f5b8e1 | -11.8017 | -46.61495 | 2025-10-01 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d9151537-298e-30f0-b234-7ef5b22d1056 | -17.62275 | -46.70073 | 2025-10-01 04:21:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a712d024-d614-3725-9e9c-ed956672a9f7 | -12.94385 | -48.40482 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecb9127d-26f7-3b79-9f41-97d35727b369 | -15.23776 | -46.22586 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0f0624b-9a83-3559-ab84-a0dfd57f48ad | -14.8934 | -48.11924 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ffaeddc-b1cb-3f1e-b5ab-74b08653c385 | -12.91736 | -47.17762 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fed67ec-3d1f-3428-a799-d4d6a6e3b161 | -11.69001 | -44.3007 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be753b7f-5d6d-3be5-b04c-8183da337b94 | -13.33468 | -47.84137 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87cc3331-cd2b-3dea-a0a4-5d51c882ab1b | -12.2161 | -47.80374 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa2ad376-2256-381b-a79f-dcea73c3ccdd | -14.02822 | -53.88564 | 2025-10-01 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecd7dac0-49be-3ed5-8757-cf01d75a3d67 | -13.7749 | -48.00676 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f906741d-cb40-33f7-a150-1f762acb5f63 | -13.09938 | -47.03989 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7229be2-d480-36e6-8cb1-c053941ac64a | -13.57553 | -48.19906 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de312f0a-84e1-3cf7-87b1-6a8153a3eaab | -15.91158 | -46.22155 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99a6965b-04c4-313a-a2f0-28c9b10f64b0 | -11.82138 | -44.96018 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2a757a2-41dd-38ce-a95b-8cf36819f3de | -11.63031 | -47.49171 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 836c412b-d7ae-36db-bd27-6855d4fcaf5f | -10.95437 | -44.31606 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5861e7a8-f007-3567-b670-4ccbf0d82f3a | -13.8006 | -47.48639 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d84e4250-5de2-3787-8a01-3c895389b369 | -9.58555 | -54.59207 | 2025-10-01 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e388ad9-904c-3de0-b3e8-ac57cef442b4 | -15.27989 | -56.77864 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a805210-b53e-3f17-881c-7c03fbb2184e | -12.44714 | -44.66949 | 2025-10-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b3907b9-f260-3b24-bca8-61c3c8972864 | -11.64659 | -47.49797 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f64c494-b0e9-3324-8474-3253a497c5ef | -13.12834 | -47.43048 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 28515bfe-d1ca-3b36-a52c-9d23e7a0ced2 | -14.91152 | -47.20383 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6222512d-fe55-3bef-9e0d-683021c55182 | -15.33702 | -56.63702 | 2025-10-01 04:21:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edbb2f82-7aa1-31ec-9da0-358599f38cdd | -15.28054 | -46.41177 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d44e0792-fc7f-3022-9070-d9800fa9e8eb | -13.35993 | -47.28466 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04e0f27f-420e-3f9d-95bb-4e7099390c50 | -16.07739 | -51.02523 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cda7359d-9bcf-3ef0-9f48-14b5b8fe2aa1 | -11.68295 | -45.33042 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb268080-c57f-3f2c-ae40-c709f7b8d08f | -13.34849 | -48.16874 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9afd7a02-2130-3a29-9645-900dac739b46 | -17.88171 | -41.31765 | 2025-10-01 04:21:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b320a897-76d6-3ff3-8fd4-547856749328 | -17.06221 | -43.48387 | 2025-10-01 04:21:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e7d7a13-e859-3780-985c-673875af0e9d | -14.14331 | -49.19398 | 2025-10-01 04:21:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69814f61-0649-3761-9d9e-1529f9eadd92 | -15.2987 | -46.40386 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7252b6d3-afa4-3c55-9400-3e8482827d93 | -11.62488 | -52.24295 | 2025-10-01 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a018159f-4b62-3328-9a6a-88bb1ce980e7 | -13.24304 | -47.31284 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8c6cff0-1242-3ed1-87de-6e9bfc2d2214 | -15.28289 | -47.94552 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fb50cf0-661f-33af-84fd-656656a134b9 | -15.34508 | -56.96219 | 2025-10-01 04:21:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be130d5f-ea3c-38f6-aaaa-30904b73af44 | -10.7692 | -45.36778 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 649a327c-8b1f-357c-954a-6e2b7219396e | -12.7706 | -46.90158 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be2d69bd-fe0d-3c27-8775-d86c465a65ce | -12.78473 | -46.85664 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85f75d30-ffad-37b0-a8a4-19bfcd040c24 | -14.78577 | -45.80415 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 723729fd-293a-39a6-b69c-1b0b702dde19 | -13.97889 | -44.91262 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fb2fe46-3c04-3818-b965-f29a9a3c060d | -11.91643 | -48.00057 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06f94eab-e08f-34ad-821c-4ef18595a0d9 | -11.94555 | -47.88579 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ee29412-516d-3041-87d5-d2c70312c03c | -13.37319 | -47.32745 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86549105-e490-3cf1-a57c-0eeb9db56b1e | -11.64997 | -47.4985 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f8c88bbc-3e6a-3301-a0da-62f4887fccde | -15.44197 | -43.64645 | 2025-10-01 04:21:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6fe58793-b15e-3288-9418-01a45941ec64 | -10.81758 | -45.36113 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1480d254-2c85-3e23-9969-070f325db9a8 | -13.13619 | -47.42438 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8a607e2-2509-3269-8a1b-b107f89bc0c4 | -14.60799 | -48.18177 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eb7c9b8-1143-3cef-aecb-1b0d5803f681 | -10.0706 | -50.27552 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 584deda4-bd03-3fa2-bbeb-a4a11c0928c9 | -10.83192 | -45.37771 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eab664c0-063a-3f05-bc45-7cff4be13eb6 | -9.82417 | -48.26868 | 2025-10-01 04:21:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cfcce80-ef2a-3957-8abc-5527e4c221f8 | -12.88999 | -45.26374 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7c36c15-bdb4-3480-9fd5-00176e464f5d | -15.0098 | -46.96838 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README61.md)
