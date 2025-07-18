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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85b16d61-6b1e-3ce5-b2c8-616796907f6f | -11.73912 | -48.18945 | 2025-07-18 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 8a1c76f8-40c7-302f-96e6-513fdfff92c8 | -8.0632 | -50.08927 | 2025-07-18 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15d2d5a2-6c54-365f-becf-be3c2d2e7f23 | -11.74243 | -48.18999 | 2025-07-18 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 22094ef0-f714-3210-b587-3bf67e9a97a0 | -15.78424 | -48.67933 | 2025-07-18 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb4dc204-0305-306f-9538-283b365e4c11 | -20.21786 | -44.47787 | 2025-07-18 04:29:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 54126932-18ca-3a9a-8693-fbb4d3d8033b | -16.4207 | -53.16056 | 2025-07-18 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c695ed51-e52b-3318-a6b9-906e90bbef52 | -16.70783 | -49.35738 | 2025-07-18 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e63019cf-7dc3-3beb-9a8e-b05c15e053e3 | -16.65153 | -49.13364 | 2025-07-18 04:29:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bff798e7-e644-3b97-a7f3-53d80821033b | -18.22433 | -54.55277 | 2025-07-18 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ee0e03e-d2bd-3fbb-99f8-011e0e6ffe6e | -19.88879 | -46.05171 | 2025-07-18 04:29:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a72b1f4-157e-33c3-93d0-4a6b9bc97fcb | -19.88895 | -46.04978 | 2025-07-18 04:29:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f48a34c9-be3f-3121-91e1-01f4541e9010 | -20.99199 | -49.77363 | 2025-07-18 04:29:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e45c83e9-3520-36e1-a21d-95f66a00d998 | -20.52109 | -47.35541 | 2025-07-18 04:29:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4724d0c7-b443-3920-807d-8be1b2fc4dee | -18.53055 | -46.16011 | 2025-07-18 04:29:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7a81233-0375-3b31-994d-dc566eb3844d | -16.79635 | -49.09906 | 2025-07-18 04:29:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc13205f-6b5a-3929-bcb3-9a9ba13b5c46 | -18.34923 | -52.53156 | 2025-07-18 04:29:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 353ec4ab-a191-359f-aea0-81880fa31b7a | -20.40387 | -42.90658 | 2025-07-18 04:29:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fca321f9-e153-32b0-a1ed-b6a5929a5b91 | -18.42352 | -53.02866 | 2025-07-18 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e55af4f8-bd9d-3642-addf-aa97f9bf8a53 | -21.23117 | -47.74587 | 2025-07-18 04:29:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e54ec045-af6d-34ff-88cd-b375189a21aa | -15.34004 | -49.42186 | 2025-07-18 04:29:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b25a41a9-be78-38bb-8710-ed13190aed9e | -21.64964 | -41.18252 | 2025-07-18 04:29:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a39667ed-cb68-3162-b79a-8d3be85a366b | -17.68179 | -46.81864 | 2025-07-18 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96366812-5258-3f3b-8a23-b17781281b18 | -20.0589 | -45.86683 | 2025-07-18 04:29:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3c62459-a978-3be5-84c3-899b6b8e4734 | -18.40886 | -44.18865 | 2025-07-18 04:29:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30fae4c9-efe2-343f-a9f4-1dd82a598644 | -18.58582 | -52.38613 | 2025-07-18 04:29:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1fafbd4f-f39f-34a5-b367-be5f27074aa9 | -21.56201 | -43.66726 | 2025-07-18 04:29:00 | NOAA-21 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 69c1c268-3294-35a2-a6f6-dd34ee9fed20 | -18.42271 | -53.03328 | 2025-07-18 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4766207-a3d6-3f0f-8dcc-af4e08ceac28 | -15.8265 | -45.77494 | 2025-07-18 04:29:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8710ddb4-12c5-3fc4-a4e0-cb2c9af3a1c9 | -18.22907 | -54.54976 | 2025-07-18 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 860be76c-af94-33c3-bba7-14f90bfaa13d | -21.07763 | -43.14883 | 2025-07-18 04:29:00 | NOAA-21 | SILVEIRÂNIA | MINAS GERAIS | Brasil | 3167301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9e2b4517-9636-3bb8-bd9d-b94da5ac1c9b | -20.99645 | -49.76685 | 2025-07-18 04:29:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e9364e76-bcac-3d2d-b505-1093e2a8c452 | -18.87884 | -47.99041 | 2025-07-18 04:29:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c5424d19-80b5-3ec8-8347-0a33f1bc0c17 | -20.9139 | -49.0665 | 2025-07-18 04:29:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aeb3773a-cf93-30a4-85dd-71f56d2068ce | -16.71172 | -49.35434 | 2025-07-18 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7edbaad7-bdb2-30a5-aa83-fd74797c130b | -16.41982 | -53.16553 | 2025-07-18 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5538175c-4831-3d3b-b97e-ba2b0efb2a9b | -19.78906 | -47.89416 | 2025-07-18 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42f79185-8f13-34f6-9fc5-b20f0e9bfbd6 | -21.64934 | -41.18564 | 2025-07-18 04:29:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0154bafc-bfbf-345e-898b-b67a674b11d8 | -20.41049 | -43.63008 | 2025-07-18 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5f038221-72a9-3c6e-b76c-3751def6824b | -16.71114 | -49.35794 | 2025-07-18 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 945d271e-30d9-3a6d-82eb-ab7ddf2a7ec0 | -18.41109 | -44.18988 | 2025-07-18 04:29:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa604476-a1bf-37c0-93c3-16f90e5618ac | -19.45431 | -45.30659 | 2025-07-18 04:29:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48afbfcd-f326-3f4d-8b01-9249d71d9943 | -20.8724 | -44.24006 | 2025-07-18 04:29:00 | NOAA-21 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4e1511a2-9531-38b3-935c-cda043ad47be | -20.99587 | -49.77053 | 2025-07-18 04:29:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e605052b-5fa5-3fc0-a906-2c19fdf985cb | -20.99314 | -49.76626 | 2025-07-18 04:29:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6c8f5c9d-6a94-3333-8711-82fa49b100cf | -20.19716 | -50.498 | 2025-07-18 04:29:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 09e438da-b059-3cb5-ab7f-4d7c33babc4a | -18.22503 | -54.54902 | 2025-07-18 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e282295-f58d-3976-a770-171c0ce710cb | -19.34377 | -40.8668 | 2025-07-18 04:29:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7eb6ca5a-713f-36b0-bb69-d62d5aa52f08 | -18.65994 | -55.73239 | 2025-07-18 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d2a97f53-a896-3aa8-91af-f3af83b68847 | -21.67335 | -41.68851 | 2025-07-18 04:29:00 | NOAA-21 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fee83b86-3b6e-3cc6-8222-683041409b0b | -18.4071 | -44.18937 | 2025-07-18 04:29:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74fe9cbd-8e32-3c46-9936-051bbcc087c7 | -17.78179 | -44.36675 | 2025-07-18 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 849efb2e-0f49-3ae6-8e49-5fbb604723fd | -18.66078 | -55.72807 | 2025-07-18 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1483e44c-0acd-3f45-b148-c062c0a2810a | -20.98982 | -49.76568 | 2025-07-18 04:29:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4f524425-b8b0-3854-9926-affbfd38b338 | -20.04033 | -41.66244 | 2025-07-18 04:29:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 8eaf3c39-a28a-34fc-b4bc-f100557445d5 | -19.00866 | -49.77907 | 2025-07-18 04:29:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9a8d8e3a-3ec6-3d85-8c29-84bfe8cc0eca | -15.33946 | -49.42549 | 2025-07-18 04:29:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c82e7def-b772-3e62-8cbe-a1ea7b422c6f | -18.8794 | -47.98665 | 2025-07-18 04:29:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 119b64fa-964a-361a-b9d3-14a9c616282c | -15.7263 | -47.04254 | 2025-07-18 04:29:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05064875-d849-3ba1-9468-9b65bb6718f3 | -18.6129 | -44.26592 | 2025-07-18 04:29:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| afeec4f9-ac30-30cd-bcf2-2a41ac991243 | -16.65992 | -49.3382 | 2025-07-18 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5aa8b988-c8a5-39c1-9ddb-312e1315af6a | -18.58938 | -52.38683 | 2025-07-18 04:29:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb99dd5a-5c57-35b4-97b8-9a2e5292cd2c | -18.58507 | -52.39038 | 2025-07-18 04:29:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f94a99c-c4e3-36a8-9718-c9646d72e941 | -16.7084 | -49.35378 | 2025-07-18 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b52ae26e-3d42-3d15-aa8d-1baadf317dff | -18.53414 | -46.16058 | 2025-07-18 04:29:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e576e89-37fa-3e69-8451-eb8d87b219b8 | -18.6573 | -55.72287 | 2025-07-18 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4332297e-cd81-38b8-be1e-35cd3d66a1c9 | -16.10116 | -46.97676 | 2025-07-18 04:29:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ee67f87-e82b-3041-ae08-f06baab0bf79 | -20.04517 | -41.6627 | 2025-07-18 04:29:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 34b96dea-632a-34dd-9585-c679a47936df | -20.41086 | -43.6282 | 2025-07-18 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e0496f9b-4936-3974-ba0b-752d2c2811d6 | -20.99256 | -49.76995 | 2025-07-18 04:29:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d4cce1cd-1f58-3a6e-8474-3f6546fdf674 | -15.72292 | -47.04201 | 2025-07-18 04:29:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b3db457-f250-3273-8fad-f966b25aff84 | -18.61687 | -44.26655 | 2025-07-18 04:29:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24013798-d63e-3079-b1dc-74fc2f2a1275 | -20.03975 | -41.66776 | 2025-07-18 04:29:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| a8fb1bc4-d4c0-3fc0-8ce8-f6fd0c6c0d27 | -15.37387 | -52.75794 | 2025-07-18 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8b9ce35-1107-34b6-9f8c-505127ee8b00 | -18.65813 | -55.71857 | 2025-07-18 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1f9e196f-2de0-3a42-9f32-02ad6a071cac | -16.29188 | -48.01357 | 2025-07-18 04:29:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 759d68c2-d9ff-3419-a078-04f8665115f5 | -18.61441 | -44.26519 | 2025-07-18 04:29:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b037c024-56b3-31c6-8f67-0c38b296569f | -18.72793 | -47.42059 | 2025-07-18 04:29:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abb0dc01-366b-3128-8922-a3887035ca01 | -21.21478 | -46.19637 | 2025-07-18 04:29:00 | NOAA-21 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 137ebf43-3f39-3e13-b5df-4c61da8a733f | -17.26672 | -49.00553 | 2025-07-18 04:29:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eaa40747-b781-3978-8007-83f2baeb9505 | -19.34352 | -40.86817 | 2025-07-18 04:29:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 90d424d1-10e4-344f-a55b-0fda26ac448c | -3.3958 | -47.4785 | 2025-07-18 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 446fd1fb-1ef5-34eb-9bd2-8139248f9f78 | -3.3957 | -47.5003 | 2025-07-18 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 8c2e9b7b-fbb4-3d5a-97b5-14847b4aacaf | -11.7508 | -48.1825 | 2025-07-18 04:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 9a222db9-67ea-3e57-8ced-d655ab79c6e2 | -5.6379 | -43.7175 | 2025-07-18 04:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| da4c1ee2-1ebd-3485-ad68-7016d6bb1fee | -5.6567 | -43.7161 | 2025-07-18 04:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 1930c3a8-9de5-3a09-92d6-06f71ac047a3 | -22.41787 | -48.15067 | 2025-07-18 04:32:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1a07c4d0-b3f8-3efa-a51c-bdbfd27120ea | -23.96406 | -48.11458 | 2025-07-18 04:32:00 | NOAA-21 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 09def9c0-9a83-36a6-8cb4-0bb13b4d378a | -22.88 | -44.76812 | 2025-07-18 04:32:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fc49fc97-8544-3fab-9d5f-50c2ce7adee7 | -23.47985 | -47.17386 | 2025-07-18 04:32:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c88e81a2-530d-3d9e-ac10-e9c160c6409f | -21.11032 | -55.80685 | 2025-07-18 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 669c9058-56ae-39b0-9557-a6a8131c7929 | -25.42308 | -49.09557 | 2025-07-18 04:32:00 | NOAA-21 | PIRAQUARA | PARANÁ | Brasil | 4119509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a28c2b7b-e13d-3010-8b4c-fe9029f0568e | -21.03764 | -55.98265 | 2025-07-18 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfd7a1fd-879a-3209-9042-f26c1ee175be | -20.20464 | -56.61488 | 2025-07-18 04:32:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9a7196f8-e94e-3cc1-abe9-a5606e70a9f8 | -21.03685 | -55.98675 | 2025-07-18 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3163eb7-8e8e-3ea9-8792-9faee2f231f9 | -21.04183 | -55.98355 | 2025-07-18 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fe46352-2361-32f5-ba48-5de291b0d85d | -22.4173 | -48.15465 | 2025-07-18 04:32:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a98ae58c-ca25-3cf2-81ef-1ae995b4cbaa | -22.51445 | -42.08329 | 2025-07-18 04:32:00 | NOAA-21 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c46dc3d4-ddb4-3369-a76d-b836e69aaa35 | -22.56156 | -42.14057 | 2025-07-18 04:32:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e909f052-3732-33d7-b47e-8f11ea30c3a4 | -21.34409 | -55.63632 | 2025-07-18 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88851510-1d67-3c67-9a7b-8566dffa33d1 | -22.41444 | -48.15009 | 2025-07-18 04:32:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README19.md)
