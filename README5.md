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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 646b1679-60dd-33e3-a4a9-8f0961892066 | -7.68584 | -40.15802 | 2025-06-24 03:36:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 13d4d8f0-3bf8-364f-9dd1-7d8f706235e8 | -8.05976 | -43.10963 | 2025-06-24 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 021cd8f1-4c7d-3bc0-a26a-f15245b16a9e | -5.78287 | -43.61011 | 2025-06-24 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a3983e4-ba10-3076-a1aa-fa0c666434f0 | -5.9805 | -43.76314 | 2025-06-24 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cfb6435-2546-338a-84e8-92f43b6109f3 | -4.55814 | -38.45985 | 2025-06-24 03:36:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 84b90d00-bf6d-3581-82f5-ce739274db79 | -4.7939 | -37.79591 | 2025-06-24 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8066b3e4-e7d1-312a-adc5-89ee3e6d83ea | -7.20691 | -43.10087 | 2025-06-24 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 4bf74f4e-6d7c-3f27-945d-4884222f906a | -5.49136 | -42.14811 | 2025-06-24 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ecdfc7e5-e7a2-33b7-9587-ab676b218ce9 | -7.06099 | -43.91556 | 2025-06-24 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3b9b6e3-b539-3a31-a9d1-09e47c8607b5 | -7.00891 | -44.60656 | 2025-06-24 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 678f0abd-dabd-3ddd-b2ac-73b24cf79513 | -7.00743 | -44.60559 | 2025-06-24 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5792b641-1bf5-3728-819c-c70bae4ec1c2 | -6.95172 | -42.80179 | 2025-06-24 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83c746cc-09db-383a-8d5c-32e108eaa735 | -6.34159 | -43.74753 | 2025-06-24 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a77b6ac7-ab2b-302a-9115-10f5ca5dfa4b | -8.06617 | -43.1041 | 2025-06-24 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5cf79761-3d9d-329d-8461-eef36eb70d57 | -7.09803 | -44.373 | 2025-06-24 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bb500a8-d5e1-301c-a2eb-5c9b6ef71acf | -6.00662 | -43.74757 | 2025-06-24 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4972e5e1-d327-3f4b-b49a-ced8af0fe207 | -7.20099 | -43.10335 | 2025-06-24 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| e221b477-6753-3b88-99f1-9186572577e5 | -6.95116 | -42.80499 | 2025-06-24 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3a19b69-e2d5-3d40-8893-f4df932b27d6 | -7.45003 | -45.56855 | 2025-06-24 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f20c348-5904-31b2-a5ef-c32623a6aa3e | -4.98124 | -37.40123 | 2025-06-24 03:36:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c390fb63-097f-3949-8033-f4d21dcaf309 | -8.24812 | -44.9572 | 2025-06-24 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3699b7e2-1f00-3a4e-9068-43d40475eff1 | -5.49188 | -42.14503 | 2025-06-24 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f6656073-2981-34c9-9119-43ffbb67e1e6 | -5.91786 | -43.47749 | 2025-06-24 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9c174b3d-a657-3dc7-97f0-ddb20cd37ce2 | -7.05964 | -43.92303 | 2025-06-24 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc827cc3-77b6-36a0-966e-9fafc3d2760d | -8.06559 | -43.10733 | 2025-06-24 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f7d2f4b1-9238-3719-8781-ccced1e8836e | -5.48401 | -42.14299 | 2025-06-24 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 156e50b9-90ee-3596-9def-75971ea3e1b1 | -7.47832 | -45.58907 | 2025-06-24 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc495e41-3dbd-3e1b-bcc9-d345227b4611 | -5.7835 | -43.60645 | 2025-06-24 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 575ddaf8-b935-3201-aea8-1244fc3e48db | -7.20631 | -43.10425 | 2025-06-24 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| a66b1ba9-0740-346f-b703-0c5cdf13773b | -5.78074 | -43.60889 | 2025-06-24 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cab6c0ef-995c-3ac3-99c2-9106bac3327d | -8.06384 | -43.11703 | 2025-06-24 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 0d17163b-5178-3833-8647-943f8452b638 | -5.91718 | -43.48127 | 2025-06-24 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 503f8f58-d945-327a-9e73-89ec469d0473 | -5.97982 | -43.76695 | 2025-06-24 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44effaf5-8b1f-30b5-af34-189ef6de5fea | -6.00594 | -43.75141 | 2025-06-24 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07c9cb5a-c5e6-3650-b650-750cc732f299 | -4.79467 | -37.79104 | 2025-06-24 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5c7de1c4-41ed-33c0-ab38-94a2b8bc5221 | -4.98175 | -37.40002 | 2025-06-24 03:36:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9b7e0e7-db9c-3b29-8f35-1858574370e7 | -8.24733 | -44.96139 | 2025-06-24 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7841c07c-105f-3093-a5b2-4f3d1e9d0f55 | -8.06035 | -43.10639 | 2025-06-24 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 8092f569-88a7-3f5f-b0e1-ffb878e5b801 | -7.86638 | -47.8754 | 2025-06-24 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 61fd24c7-7a95-3047-a37f-ea474ab97dbd | -12.79939 | -48.73419 | 2025-06-24 03:38:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9ffab68b-9fdc-3a10-af00-1d86cda5b251 | -11.37225 | -43.74768 | 2025-06-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ce0cda4-d5ee-3aa7-89c9-c1f8a1eae9d0 | -14.43522 | -48.92119 | 2025-06-24 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2ba78b3c-0571-3b81-ba5f-b360da1afa67 | -10.51188 | -47.57994 | 2025-06-24 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fcae7e11-b676-33b5-811a-fb185d9dcb5f | -8.86944 | -47.26876 | 2025-06-24 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 210129cd-c3cd-300c-89b5-78691bfb8752 | -9.41437 | -48.4198 | 2025-06-24 03:38:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 44770cce-372e-376a-b191-7b94fe9bb55c | -14.44003 | -48.91811 | 2025-06-24 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4233b3a5-0808-36bd-adc4-b3278010be24 | -12.28972 | -48.80422 | 2025-06-24 03:38:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 52c28907-9fee-3a2c-aab1-e0e8c6ca4e2f | -10.65163 | -44.49324 | 2025-06-24 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9489bc05-4fb4-3919-b07e-50f724234f83 | -11.37013 | -43.75001 | 2025-06-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72468fdf-2bfb-3ba3-a09a-7db1a2550b5d | -8.86829 | -47.27479 | 2025-06-24 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27e9a372-e847-3af2-837c-564d23e41ff2 | -16.32502 | -43.6191 | 2025-06-24 03:38:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79af5133-0de5-3545-bee9-17a0d53638d1 | -16.4868 | -39.47558 | 2025-06-24 03:38:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5b0ba24b-4e03-3128-abe1-3f6353595b6b | -11.93748 | -48.43076 | 2025-06-24 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de97755e-c3f6-3018-8306-4bc0fe1816f6 | -16.5863 | -43.64603 | 2025-06-24 03:38:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a87806f9-bde2-3aed-b41f-5ac6963257f1 | -11.09977 | -46.64981 | 2025-06-24 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90e4b5c0-c4f1-341f-acb3-de40362adcf8 | -14.38224 | -46.13562 | 2025-06-24 03:38:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a8351a9-fa00-3fdd-ad29-d45744cfa6b9 | -9.64686 | -48.56499 | 2025-06-24 03:38:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc4a6351-d16e-352c-b105-78482f4f10cf | -14.38557 | -46.13944 | 2025-06-24 03:38:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 669d6bc0-fe23-3fb0-a3d0-061e08463a4b | -14.4334 | -48.91634 | 2025-06-24 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9fcf6ffd-9d72-3a31-8bac-f9a17472a95b | -12.28929 | -48.80417 | 2025-06-24 03:38:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 49904e7e-fd79-3bf9-b8b3-e176c91e8631 | -14.43662 | -48.91489 | 2025-06-24 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2fbfe55a-f154-3065-8417-210d7af04574 | -10.65231 | -44.48962 | 2025-06-24 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eaf49b51-8cc1-3071-91d0-5bd0bd4167d0 | -10.28307 | -47.61553 | 2025-06-24 03:38:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c855026-4298-3b26-b0e7-ea987a9d66bf | -13.07138 | -48.83993 | 2025-06-24 03:38:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a428d5c3-a6e7-3ec1-9c33-1924dbc55666 | -13.55223 | -42.48402 | 2025-06-24 03:38:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fdca23ab-1543-3a86-b67d-44b119bb4710 | -14.66549 | -46.9453 | 2025-06-24 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1631e7e-f4ab-3ac4-8bd8-07450e3b604c | -14.19718 | -42.78213 | 2025-06-24 03:38:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b1c7bfdf-42b3-36ee-94a2-c065e62887b8 | -9.48075 | -40.51683 | 2025-06-24 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e778eb09-f99c-3fd4-996c-a5faa5895e49 | -16.3297 | -43.61998 | 2025-06-24 03:38:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5df43d11-c449-3549-a733-5dcb3bcb78ad | -10.28424 | -47.60959 | 2025-06-24 03:38:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cf022653-926c-3f9b-8d71-cee268610e93 | -13.25427 | -41.33281 | 2025-06-24 03:38:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| df8401a7-66ce-39ef-b771-29832cdb0c2a | -13.5459 | -42.49283 | 2025-06-24 03:38:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3b1860cb-ae70-3b59-8e5f-9d8746111564 | -12.80622 | -48.73555 | 2025-06-24 03:38:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca3a90f8-7b00-32de-b830-90a6a59a0eac | -13.55302 | -42.48151 | 2025-06-24 03:38:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5664b52-e8a6-33c2-bc40-8b88883b50ef | -14.38643 | -46.13516 | 2025-06-24 03:38:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb55c591-b5b1-38e4-aa6c-967c9cfc6fde | -14.43473 | -48.91013 | 2025-06-24 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 706f5237-63f6-33f4-b1de-c6bfd3007ce9 | -12.40785 | -43.80256 | 2025-06-24 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d49952af-5338-366b-ae42-27b23014954d | -10.2872 | -47.61142 | 2025-06-24 03:38:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f04bd04-ecc3-354f-85de-58f6f7e38036 | -10.462 | -46.98212 | 2025-06-24 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8210e2d9-ca08-3515-8fca-34639765aff7 | -16.58163 | -43.64511 | 2025-06-24 03:38:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 342f5c93-2ecd-340a-a23a-20f94c48389c | -14.00349 | -42.55371 | 2025-06-24 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f2ba056a-04da-3c02-a299-25b6624577dc | -10.28049 | -47.61027 | 2025-06-24 03:38:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d209a20-f61c-380a-a6a8-d201a55a2522 | -13.55218 | -44.09494 | 2025-06-24 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e03ba80b-8792-3d1f-bdc7-4dd0d65212b8 | -8.70325 | -47.17861 | 2025-06-24 03:38:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1f6dfb8-1434-3462-8f15-c2764e8b0f55 | -13.50717 | -42.67781 | 2025-06-24 03:38:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 53bc4e8f-84ce-3d70-bc48-f338f1e3e980 | -13.25996 | -41.32568 | 2025-06-24 03:38:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ddaa9e2c-5fab-3259-9c7b-fabfc4d31023 | -8.87161 | -47.27311 | 2025-06-24 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da7e3c6a-6a18-32b2-94f2-600b6c41ddbd | -11.5696 | -47.43233 | 2025-06-24 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8a5fdc25-f25d-34c6-aa08-4d6718847096 | -15.11144 | -41.08534 | 2025-06-24 03:38:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 33c83276-969d-3734-a665-9398f2a9b028 | -13.07283 | -48.83323 | 2025-06-24 03:38:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8c9e07eb-94a5-3b35-80d8-08eb6a8fd316 | -14.21375 | -42.77004 | 2025-06-24 03:38:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1fda8b0e-6699-3104-8f47-418e0b1de8af | -10.45558 | -46.98086 | 2025-06-24 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 97f3fc58-fa92-32bc-8b2d-ab1517eeff5c | -13.7683 | -44.10106 | 2025-06-24 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d30ac190-c497-35bf-a576-d586bbd5d95d | -10.51523 | -47.58271 | 2025-06-24 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 654aa3df-2a64-3ef9-a415-ba2463cfdf2e | -10.51851 | -47.5813 | 2025-06-24 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01fc6f8d-4911-3daf-858d-2e57a6b1140c | -14.19352 | -42.77631 | 2025-06-24 03:38:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| cc3a5638-10af-37e2-8800-7f8c163dac21 | -11.37165 | -43.75082 | 2025-06-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a98036e4-2442-3b17-a4e8-aba73f2ac87c | -12.40222 | -43.80445 | 2025-06-24 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90fcec5b-67d9-366c-87b3-bc5c57669222 | -14.14495 | -40.2472 | 2025-06-24 03:38:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 906df16e-e31b-3722-94f5-e6eca2b1b266 | -11.37529 | -43.75105 | 2025-06-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
