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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b66dab50-bb6d-3862-9bd2-57a9475fc8a7 | -11.03077 | -56.2838 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db86f8d8-c969-34ee-b530-609838ed6b91 | -12.49136 | -58.47159 | 2025-06-29 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5abf5b6-45ab-3299-a0a4-e302c0a68b2c | -10.34498 | -57.50236 | 2025-06-29 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a1abbc17-a600-3f46-aec1-665cb67f23e1 | -14.21778 | -45.51076 | 2025-06-29 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a13a537f-e5bd-3250-992e-c9c427424cb0 | -11.54765 | -52.78794 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 40b5b2e7-56cc-3941-a6ba-e5c32f462ca1 | -12.04607 | -48.07924 | 2025-06-29 04:34:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 627b94c4-dcc5-30cc-9a72-7c505d15eb3c | -18.50212 | -47.59959 | 2025-06-29 04:34:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43fdc2ff-1515-35e1-a9b9-596c5455a2a9 | -12.10487 | -54.57007 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 624a06ec-b1ab-3559-be15-700ceb38973a | -11.27474 | -52.74123 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4acfd63-5580-340e-ab27-7e6b79770471 | -12.41912 | -54.87418 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e252fa34-9eb1-34e1-8365-56161a69662f | -12.93166 | -51.5645 | 2025-06-29 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 039daadf-f3a5-37db-82fc-dbcbf120465d | -17.76122 | -52.44554 | 2025-06-29 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8621749-5408-383c-9ca1-3bde7ec6fd90 | -12.10421 | -54.57373 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42702f12-3da3-3113-9c4b-fb2fbda9b324 | -14.69192 | -53.38906 | 2025-06-29 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f975f792-1797-3142-be82-de97b786de9f | -13.30513 | -47.51358 | 2025-06-29 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fdcc36e-fc52-3876-8418-cd9dcaeb0abb | -12.11104 | -54.58258 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbb36757-4ac4-3eca-905f-f1a94cb69507 | -11.02423 | -56.26725 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d4f6f8ad-367e-30d8-8483-70fb35a77bfc | -11.26138 | -52.75264 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 81697a52-4abf-311f-8fa5-76a8ae1e489e | -10.03682 | -59.35544 | 2025-06-29 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 197264dc-d8a8-3a75-9069-d6710ccd44ff | -14.83907 | -48.33925 | 2025-06-29 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 181b64dd-ef1f-3142-80ce-a61b57852514 | -11.53732 | -52.7816 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 50e01c7f-713f-3960-b7a6-b6b25d3cc6e4 | -11.02143 | -56.25652 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 001b0f0a-c6d9-3e65-8b43-6a24abdb5865 | -11.54395 | -52.78731 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f8a02183-78c4-3794-b868-5f054cfb2262 | -11.11326 | -55.44171 | 2025-06-29 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 677196bf-b648-3d75-a3d6-5d2674c4b43d | -11.27399 | -52.74568 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e447245-d7e8-3836-886d-fbe7e267f96e | -11.56012 | -52.80395 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9a63fa4-36ea-3e71-9936-2dce8184c0eb | -11.55503 | -52.78925 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec3d26c6-f390-3009-83c1-55340468301b | -11.03487 | -56.2725 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 045c7d10-0f65-3ab0-8f86-c509184e5a9e | -12.10894 | -54.57083 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f993d7d-bfb3-3e80-a79e-559f67bd1cf7 | -11.54625 | -52.77396 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 9fab9b5f-17b0-3e92-acc5-3e20a5ce1723 | -15.78288 | -48.67979 | 2025-06-29 04:34:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a72e4ef-0d7a-30aa-90d3-b0ad0d972195 | -11.02758 | -56.28653 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca3563ce-047a-3e77-aa01-767f61d7b281 | -11.03022 | -56.27161 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| de395f13-48ad-3ed0-a94b-441c0849bf99 | -11.55071 | -52.77016 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| bd19082d-e7ed-31a8-b0f2-979a18a44ecd | -14.69111 | -53.39112 | 2025-06-29 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23c2c2f1-271b-329c-82c5-d5031f5e1ecc | -19.68017 | -45.37714 | 2025-06-29 04:34:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 539c7d99-1314-38a8-a13e-11fb0ea2cf3f | -11.2718 | -52.73613 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a99d0b12-bcba-3d33-86c0-9ae0522b590c | -11.55426 | -52.79371 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a510118-847d-3bfc-a3f7-752f8bc5fe7b | -12.475 | -58.47188 | 2025-06-29 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2af9c285-0e0d-3a51-822d-ded7b42e872b | -11.02734 | -56.26086 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6650b9dc-7684-397a-a5f7-47370201d3db | -15.93113 | -52.27922 | 2025-06-29 04:34:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dfd0bc5-bc6b-3b3a-a413-35a209bfc583 | -11.02093 | -56.26991 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a33c6a95-8421-3986-84a9-79ac68f3323a | -11.04395 | -55.37304 | 2025-06-29 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67cb9f9b-7d6e-31c9-96b2-961d05d9ddf7 | -11.03197 | -56.26176 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e022e51-761a-3326-8bed-5e6141b2a14d | -19.93362 | -44.20257 | 2025-06-29 04:34:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d49a3d56-fddf-35ea-b51a-5cf82e7395dc | -13.95551 | -54.48612 | 2025-06-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60fb3c80-831a-3b54-90df-6df15a42277c | -11.00852 | -56.2321 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7fcf813-42c1-34f5-8179-c6eecbf3ef2c | -13.27502 | -48.42725 | 2025-06-29 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08cac127-c3b5-3c69-9ad9-d32bed75f7c3 | -11.02607 | -56.25738 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e58bbc5-e619-3b69-816c-ef0343f5c4df | -12.99203 | -59.05378 | 2025-06-29 04:34:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c71c8ed0-c09f-3830-bdb4-6a2ddf85858a | -11.01715 | -56.26423 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cca34eaa-c150-3a8d-83e4-71b5728bada8 | -11.02846 | -56.28154 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e7fb878-99e0-30e9-9596-9d194b1264b6 | -11.11765 | -55.44247 | 2025-06-29 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ab3a1ae-9b80-3363-803b-b65ee45699a6 | -15.64942 | -49.73132 | 2025-06-29 04:34:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09f98881-649c-3aad-8c70-a118ea7d0be4 | -11.55211 | -52.78414 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 4ade4a57-fc8c-3859-91fe-c0690f4422b8 | -11.54903 | -52.80202 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8e9d10a1-ab05-370a-805b-5b97f03acc1f | -11.27105 | -52.74055 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8c1c5e0-2f5b-3bb1-a100-6a3dccea81d6 | -11.25995 | -52.73862 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f8eb919-c8fc-3cd5-9610-3e54f6aaa2ab | -11.03284 | -56.25686 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76b10f14-0f2f-360f-a9ac-699d5c4ccf7c | -16.3917 | -49.23154 | 2025-06-29 04:34:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d412d60-62e0-352d-b46b-8b85771320a9 | -11.54256 | -52.77332 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 8176d94e-7856-3c2b-9328-b773dffbb1b0 | -11.57301 | -52.10994 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3e81715-36e2-3427-a1d4-7e4a37d89296 | -11.43607 | -54.47602 | 2025-06-29 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54065c4c-50f5-30b1-870e-8baf243be25b | -11.02293 | -56.28564 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69de0256-ed3e-3eeb-b163-4beca1cc5409 | -12.02039 | -47.77446 | 2025-06-29 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30015973-48e8-3953-a827-00eb7d465178 | -16.58032 | -49.32857 | 2025-06-29 04:34:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69325a7d-ccda-3a63-a98c-81090df6cc83 | -14.83852 | -48.34291 | 2025-06-29 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7be1407-b7c5-3264-ae4e-0a51ce94d3b2 | -11.03311 | -56.2824 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 795d3d54-bc91-3715-be83-babd673c0870 | -9.92026 | -59.91413 | 2025-06-29 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45badc22-1647-3368-b930-5764175f47ed | -10.04183 | -59.36055 | 2025-06-29 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ec0b730-b5c0-3f16-b1a6-4c2044e7b34f | -10.03601 | -59.3596 | 2025-06-29 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0455d73-4257-3cbd-a4b8-5e37f354f0c9 | -12.60146 | -57.87363 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 053753d0-6dfa-3e7a-acfb-754759498850 | -11.5498 | -52.79753 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e2349215-cf82-36e8-8253-5e05ba5a8268 | -12.98853 | -59.05378 | 2025-06-29 04:34:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0776d7ad-e4b8-3f7b-9aa8-4232a1bbf160 | -15.33826 | -49.13271 | 2025-06-29 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e32f9909-f19a-34f6-a6a6-c7f1c7e4f91c | -11.55057 | -52.79306 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 856f8e02-6e91-39a4-a922-e780c726f18f | -11.54333 | -52.76888 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| ea2cce29-6019-30eb-9174-f6cabae32e82 | -11.54025 | -52.78671 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ce2af37c-bfac-3c23-90f3-6990426df435 | -11.01828 | -56.28477 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99074b7b-4926-341f-9b6c-cbdd324919b3 | -12.47039 | -58.46761 | 2025-06-29 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f297a28-3718-3ff0-90bb-5dfe37578a05 | -17.76057 | -52.44942 | 2025-06-29 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2e84a98-34d5-3407-935f-4ff72bc3ba2b | -16.39114 | -49.23519 | 2025-06-29 04:34:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19b6b972-abb1-3b60-a5b2-030a8ee262b1 | -15.72695 | -49.56063 | 2025-06-29 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2c0582a-a6db-3792-a2ca-a6e648bd9d8d | -12.61207 | -57.87267 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 726e9114-71fe-3375-8015-5df111b8d629 | -16.16393 | -45.68575 | 2025-06-29 04:34:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9f5bc3e9-f766-3d94-b3b6-92d245d92cf0 | -12.10355 | -54.57739 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 881a6ccf-5a1f-3892-8e98-d3eda99bf6e2 | -11.03956 | -55.37231 | 2025-06-29 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 158295f9-a136-3651-b85b-0909422cfd42 | -12.99325 | -59.05822 | 2025-06-29 04:34:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb5f6d82-23bb-3bbd-9531-2913260a256e | -11.57231 | -52.11409 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 177f5e3c-1512-3b6a-8a84-19d12aa59955 | -13.01643 | -53.41924 | 2025-06-29 04:34:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61207d10-e337-3441-bf2f-cfef53ff43d4 | -15.56948 | -47.85672 | 2025-06-29 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9384b07-b582-3ba8-a730-74b1bff5cc7a | -11.55796 | -52.79438 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5afcdfe3-029d-3ec5-bb13-492f7c3debd3 | -12.02376 | -47.77499 | 2025-06-29 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f0dc754-baff-334b-afd4-93d57591cc2b | -10.35064 | -57.50027 | 2025-06-29 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2cc14227-e894-3a92-8bba-6f90b4164823 | -11.54826 | -52.8065 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1825545-fdb7-323c-8852-e7e1c55af7ad | -13.95444 | -54.48677 | 2025-06-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb51d4da-62cc-384c-b846-f3f2c8b53578 | -11.55656 | -52.78033 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dde0d003-bcd9-3f14-9855-c649c1aab56b | -12.99136 | -59.05725 | 2025-06-29 04:34:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92d19748-440e-3191-8737-7b8dbbeafb2d | -14.02795 | -54.48452 | 2025-06-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d51996a-71ae-30a3-847a-86cff4dbd5d0 | -11.5344 | -52.7765 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |


[Clique aqui para ver as próximas entradas](README21.md)
