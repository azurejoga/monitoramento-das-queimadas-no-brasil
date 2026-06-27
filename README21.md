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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb29eb78-2349-3c29-a34b-b125121142f4 | -12.1685 | -59.76084 | 2026-06-27 06:14:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0dea518-e23a-3b7d-b6b4-f69f054d8881 | -12.16879 | -59.7608 | 2026-06-27 06:14:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 486d7a4c-06f0-3deb-9356-6c2378d30fa3 | -12.16946 | -59.75457 | 2026-06-27 06:14:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be23a820-29fd-30da-b5e2-a0c80db08786 | -12.1692 | -59.75463 | 2026-06-27 06:14:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d89b35b5-ce54-3b5a-a9d9-110d62d521bb | -12.4651 | -58.5009 | 2026-06-27 06:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 5824f020-82d2-3000-881d-3c7e42797183 | -12.4654 | -58.481 | 2026-06-27 06:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 5d979754-0c55-33d0-9b7b-307d0b60f44d | -12.6236 | -57.8926 | 2026-06-27 06:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| c5f17964-e2b8-37ed-be93-2bb4c9de0691 | -12.6236 | -57.8926 | 2026-06-27 06:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| eaff3ea5-708d-3d40-ac11-dec040e77d03 | -12.4654 | -58.481 | 2026-06-27 06:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| c87b8110-9918-36e4-b5fc-9457cf67c805 | -12.4651 | -58.5009 | 2026-06-27 06:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 1ba680dc-8aaf-34fd-93d7-610fa1b8a8a0 | -6.49898 | -42.2322 | 2026-06-27 06:33:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 21c58e6a-ef20-313e-9670-46b9d0fe9dbf | -4.28338 | -48.35964 | 2026-06-27 06:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 7b6e9e4d-9e1e-3872-9798-fdba7c74bd0f | -3.86483 | -42.97316 | 2026-06-27 06:33:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b049268b-8fb5-3a49-925e-17a272d159c8 | -5.77767 | -45.06151 | 2026-06-27 06:33:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| b82a6626-b0f4-3de3-8659-944c59445f1d | -5.77623 | -45.0714 | 2026-06-27 06:33:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dba1a50e-63ca-3947-9205-e38c157de964 | -3.86662 | -42.96063 | 2026-06-27 06:33:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5a7033ae-24ee-3498-aea3-64843319a266 | -4.28195 | -48.36897 | 2026-06-27 06:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b358b069-c2c3-3639-9e12-36c43e9a4f43 | -5.78696 | -45.0629 | 2026-06-27 06:33:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 34a0a39c-4a9d-3847-94e8-21806fe3d9aa | -6.50114 | -42.21683 | 2026-06-27 06:33:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| d7ade463-303d-37a9-ba79-231c4ef22f3d | -5.76838 | -45.06015 | 2026-06-27 06:33:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 46d44150-bdaf-3d4c-899c-4951e60116ee | -7.73726 | -44.17916 | 2026-06-27 06:35:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| a6036aa2-cb4b-328d-9e08-ef7a134bc287 | -6.98162 | -42.88287 | 2026-06-27 06:35:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 8ddb69d1-2bcb-3d26-8df9-1f7e9a50564a | -8.78193 | -46.92537 | 2026-06-27 06:35:00 | AQUA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7c6084af-6688-32bd-a501-0f551a010f9d | -7.73626 | -44.18542 | 2026-06-27 06:35:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f242b122-65e8-3571-a0ca-6cd6d1723dc4 | -7.73799 | -44.17355 | 2026-06-27 06:35:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b0b21afe-dd13-3cf5-bb25-6851f890a1b3 | -6.9686 | -42.8956 | 2026-06-27 06:35:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 72269fd5-83fb-39af-98e1-942d53206ac9 | -6.97062 | -42.88133 | 2026-06-27 06:35:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 9f13c78c-9805-3151-8fd7-91c24bb852dc | -8.2271 | -47.10797 | 2026-06-27 06:35:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 295215cb-8e71-39a7-9384-83120a20e9f2 | -7.74657 | -44.61275 | 2026-06-27 06:35:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 78bb377b-3a86-3c62-afb2-7bc0fefb6b18 | -6.97957 | -42.89718 | 2026-06-27 06:35:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| d6f43c53-bbd2-3967-8f66-f775bb7d6186 | -12.61193 | -57.88478 | 2026-06-27 06:37:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 864ce0be-582f-3b62-9c8d-d838543dfc44 | -12.43941 | -49.58007 | 2026-06-27 06:37:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 86e5ef1f-5715-34dd-8ed6-449b71e21907 | -10.47869 | -47.07928 | 2026-06-27 06:37:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cc60c892-805d-34cf-8aa3-b8932b1b0219 | -10.55429 | -46.24209 | 2026-06-27 06:37:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 815f48a1-2753-3e16-adc5-9336626cbbbf | -10.56495 | -46.23357 | 2026-06-27 06:37:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6fb7a739-96dc-3d60-9b00-82a5e4a11893 | -12.82533 | -44.35152 | 2026-06-27 06:37:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f82cf9d8-5d0a-3fd1-a243-3e620d4ff9e6 | -12.46519 | -58.47483 | 2026-06-27 06:37:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 806c346b-9af9-3df1-848e-ab3c40ec8365 | -11.90653 | -57.4011 | 2026-06-27 06:37:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 33.0 |
| a3c31a52-09a3-349e-a996-892c105b4b34 | -12.61887 | -57.87813 | 2026-06-27 06:37:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6e5a0ce8-c4fc-3e90-8858-7bf3e08aebbd | -12.45679 | -58.47786 | 2026-06-27 06:37:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 20dc6bce-7aa7-3971-a574-510ed8f9f7a2 | -12.6033 | -57.8753 | 2026-06-27 06:37:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 49c10821-eaf6-3e90-b19a-626d1defe01d | -10.47954 | -47.13547 | 2026-06-27 06:37:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 690b1c0e-658b-3cdc-bd6b-2048bde0769b | -13.25011 | -54.40248 | 2026-06-27 06:37:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ce5d6576-0f1c-3069-aec4-6acd534fa4c8 | -10.77958 | -46.47209 | 2026-06-27 06:37:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 57da9319-4970-33c1-9ba2-dad4e40a3ca9 | -11.90838 | -57.39627 | 2026-06-27 06:37:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 1d2e84b8-3d1f-360a-86ff-29de8a99a73c | -13.66363 | -53.94201 | 2026-06-27 06:37:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7597d702-2b5a-3d57-8dc9-35661fa60af7 | -12.6236 | -57.8926 | 2026-06-27 06:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9342480f-a591-359e-903b-cb2790553e3e | -12.4654 | -58.481 | 2026-06-27 06:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 4378eb3a-97bc-3349-984c-c151f8f4d8f9 | -12.4651 | -58.5009 | 2026-06-27 06:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 251b6757-a858-3ac9-b4f0-2f9ec410816f | -21.75347 | -56.26981 | 2026-06-27 06:40:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 15.1 |
| fe5dd77b-b21b-36ec-aab5-1ff3ab2576dc | -12.6236 | -57.8926 | 2026-06-27 06:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 0bf8be0d-77f6-31d9-bd57-d24570858b3e | -12.4651 | -58.5009 | 2026-06-27 06:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 050d5c22-717b-3cb2-983e-9561ffd8ea74 | -12.4654 | -58.481 | 2026-06-27 06:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| bab556f9-51c1-3e7e-8da7-6cdfb990d08d | -12.6236 | -57.8926 | 2026-06-27 07:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| d04e4f83-8faa-323e-b360-1d12fc85c5a6 | -12.4654 | -58.481 | 2026-06-27 07:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| c84e9778-db21-327f-9e4c-2444778e7e29 | -12.4651 | -58.5009 | 2026-06-27 07:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e16b7e24-3a68-3f23-82c0-3da9842bcbbb | -12.4651 | -58.5009 | 2026-06-27 07:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 71120439-a07d-34e0-acd4-d09235144ee1 | -12.6236 | -57.8926 | 2026-06-27 07:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 15fa93c1-a96f-34aa-8570-8c2d254fa207 | -12.4654 | -58.481 | 2026-06-27 07:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 81bc4c9f-ea67-37be-9a12-971256513699 | -12.6236 | -57.8926 | 2026-06-27 07:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 983b791a-0bd7-3b1b-a0ee-36bae95a0bcd | -12.4654 | -58.481 | 2026-06-27 07:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 217692d4-c0ef-36ed-8985-390b4bd8c4d5 | -12.4651 | -58.5009 | 2026-06-27 07:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 9ae5648a-54ca-352b-bed7-5999a25a7a52 | -12.4651 | -58.5009 | 2026-06-27 07:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 4ddb9063-f833-3877-95bf-313e2012a9ea | -12.4654 | -58.481 | 2026-06-27 07:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| e173a3dc-8754-3712-a05f-43e58b96e1f3 | -12.6236 | -57.8926 | 2026-06-27 07:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 3ca2feb7-3fc2-34e1-a726-00fad6293271 | -12.6236 | -57.8926 | 2026-06-27 07:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| b795722f-6c32-31ad-9198-76282b7b7a6a | -12.4654 | -58.481 | 2026-06-27 07:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 6fe742c3-8025-32f2-aefb-07d1175e4405 | -12.4651 | -58.5009 | 2026-06-27 07:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| abaf82c4-fec1-3219-8a09-ec797205452c | -12.6236 | -57.8926 | 2026-06-27 07:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 053f0303-1bc4-3149-922f-a6eaa880d04a | -12.4654 | -58.481 | 2026-06-27 07:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 5be8a142-ad61-365f-b6f7-657af563072a | -12.4651 | -58.5009 | 2026-06-27 07:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 89e974af-7aab-307b-af9f-6fb7e49aa05f | -12.4654 | -58.481 | 2026-06-27 08:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| f3b5f449-aac7-3fa2-b8f6-57640134fc60 | -12.4651 | -58.5009 | 2026-06-27 08:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 85fc13e9-5bc4-323f-86f0-64b4baf3767e | -12.6236 | -57.8926 | 2026-06-27 08:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 890d9cc5-ec76-348e-b055-976c113976c3 | -12.4654 | -58.481 | 2026-06-27 08:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 883ad919-9657-3fc7-8d3b-dfd32e4c958c | -12.4651 | -58.5009 | 2026-06-27 08:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 3beb0a5c-afde-323e-882e-d1888d635ae3 | -12.6236 | -57.8926 | 2026-06-27 08:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 4123b96a-acf6-399a-b464-b81c6f2977ac | -12.6236 | -57.8926 | 2026-06-27 08:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| b49bf8af-d738-3e6e-a82a-b9db0891602e | -12.4651 | -58.5009 | 2026-06-27 08:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| d78037a4-b9de-3311-8624-fa7fdf2575bc | -12.4654 | -58.481 | 2026-06-27 08:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 91dbd74a-e6a0-36aa-8660-249dbfdeea9f | -12.6236 | -57.8926 | 2026-06-27 08:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| e0fd5713-3248-35a0-96c8-4dfeb13709f8 | -12.4654 | -58.481 | 2026-06-27 08:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 90dab733-1451-326e-af70-057b93023694 | -12.4651 | -58.5009 | 2026-06-27 08:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 504ed03d-b389-3167-90fc-4ee66a83020b | -12.4651 | -58.5009 | 2026-06-27 08:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 227f7d4b-6f86-399b-b7e1-03f36e1b7741 | -12.4654 | -58.481 | 2026-06-27 08:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 4c12bd14-b495-3a79-b049-a01fd7553660 | -12.6236 | -57.8926 | 2026-06-27 08:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 164e8857-1148-3a65-b662-904be7bfdfcd | -12.6236 | -57.8926 | 2026-06-27 08:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 41.7 |
| e3c8ab30-332a-39aa-9178-d83a09c3ee0c | -12.4651 | -58.5009 | 2026-06-27 08:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 734ecd30-2c8d-31ef-8590-8f8190a11371 | -12.4654 | -58.481 | 2026-06-27 08:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 8efb28f8-30bd-34b1-890c-3e17e00d6b99 | -12.4651 | -58.5009 | 2026-06-27 09:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| eaae76b3-4848-3703-be51-3906cefa18ad | -12.6236 | -57.8926 | 2026-06-27 09:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 317035cc-dad6-396f-a67d-c1fcda80f348 | -12.6236 | -57.8926 | 2026-06-27 09:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| cb4dcf60-bc44-3cde-9c7c-e434a9470a74 | -12.4651 | -58.5009 | 2026-06-27 09:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 98c75a3a-df31-3e47-9c07-694eb11a909f | -12.4654 | -58.481 | 2026-06-27 09:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| d4cdcf0c-55c2-32f8-87d6-7f3fd941379d | -12.6236 | -57.8926 | 2026-06-27 09:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 001cca03-4853-33d3-bd84-dcfcc3467256 | -12.4651 | -58.5009 | 2026-06-27 11:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 5665afb3-84fa-3347-8b20-cdbd7af3d34c | -12.4462 | -58.5023 | 2026-06-27 11:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| b5b49222-b7f6-399c-bf53-98c7a086f1f4 | -12.4651 | -58.5009 | 2026-06-27 11:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 246.9 |
| 57a5e999-7741-33f6-b71e-f92f0dc70a1b | -12.4654 | -58.481 | 2026-06-27 11:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| ead74204-76ff-3071-adaa-b39456e29d86 | -12.4651 | -58.5009 | 2026-06-27 11:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 313.9 |


[Clique aqui para ver as próximas entradas](README22.md)
