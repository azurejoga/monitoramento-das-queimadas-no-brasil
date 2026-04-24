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
| 1a1a2665-08f8-3163-881f-fb04171b38a2 | -18.26679 | -52.89144 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a161ff7-18c3-38ff-ade4-f16373268e1f | -20.19191 | -46.92941 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb900b12-cc66-38a1-96e7-61b8d848d27b | -22.26031 | -48.47639 | 2026-04-24 04:32:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93c9e827-c94f-3e97-bb9e-abdac1fc2fb0 | -18.26883 | -52.90131 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c06d882-ddc0-3cdd-b2bd-ec020b7b5a2d | -21.85353 | -46.98297 | 2026-04-24 04:32:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ecde858-faa1-32e2-b624-380048548e35 | -20.15922 | -46.85767 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ba6e6ff-ec46-339c-b52a-8da648023d5c | -17.48161 | -51.09268 | 2026-04-24 04:32:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9271f267-a8c4-33c9-9b55-b8768ee052ee | -22.54996 | -42.2104 | 2026-04-24 04:32:00 | NOAA-20 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ed17eeb4-ed76-32cc-b86a-0ff0cdd882ce | -18.28403 | -52.92333 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32013da1-0599-37f5-8296-4928ca4e466e | -20.20383 | -46.79686 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bca04eb-8559-31d0-a135-3fe3582835dd | -19.45159 | -56.61557 | 2026-04-24 04:32:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 88501051-1ec7-3680-8c2a-a6d2908ec1be | -20.18785 | -46.88308 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6981e512-e958-37d9-ab0d-599302b673af | -18.27541 | -52.90732 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbeff367-9df5-3029-bfff-3092e0a6ed33 | -19.44487 | -56.57846 | 2026-04-24 04:32:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| abee0275-b650-3698-aa84-4eeefcba6f5a | -21.69997 | -48.43571 | 2026-04-24 04:32:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f95e4b0-97c4-3b15-be4b-3203b1ce207e | -18.2685 | -52.89416 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f648337a-c628-3fe7-91c8-cedb4b17fa1b | -20.1651 | -46.86675 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e70b048-bc1f-3c4e-84d7-45a8a3250631 | -20.24361 | -46.77234 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cea67678-eb21-3845-9feb-b72cf55a38ae | -20.16216 | -46.86219 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b97e8e25-5b40-38da-b069-a902e1269730 | -18.16933 | -51.11319 | 2026-04-24 04:32:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89b14640-c1f0-32e3-865c-d0a612d00861 | -19.09738 | -56.06459 | 2026-04-24 04:32:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d160300d-3932-379f-8a00-cdf6b30d1438 | -19.44155 | -56.6184 | 2026-04-24 04:32:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f1be9648-5d46-3e87-a603-64f5daea5478 | -17.56244 | -46.60583 | 2026-04-24 04:32:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f70c2ea3-f524-3eb7-a156-faf8aaa45104 | -16.43084 | -54.91551 | 2026-04-24 04:32:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5767975a-ca20-3d3c-95ff-ed6789bddfb1 | -20.2054 | -46.88565 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d599869e-ca10-316b-9610-ad38edc4df06 | -20.23517 | -46.75434 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01244290-4e77-33a2-9e7a-f04989683848 | -18.27171 | -52.90661 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 732a8d7e-1fa2-3ddd-9739-43a4aad8fbd7 | -21.58579 | -41.93448 | 2026-04-24 04:32:00 | NOAA-20 | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b4dfb60b-87e5-3aa4-b361-6649c698b587 | -16.42057 | -54.92256 | 2026-04-24 04:32:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83207e80-5a1e-37f2-8ff0-edbb5da6718b | -20.23809 | -46.75906 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0249b73-380a-36ea-97c7-fd3760654d41 | -20.19895 | -46.88065 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 308a45fc-0a68-3221-a1bc-ba30455609fd | -13.71301 | -57.48191 | 2026-04-24 04:32:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 877404fe-b9b4-3706-8a42-ea39391b5145 | -17.47882 | -51.08812 | 2026-04-24 04:32:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1816f004-57b3-3417-ac96-3870fb4ceb27 | -18.27092 | -52.88034 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20541358-51e6-37f2-9de3-f026e98c13a3 | -18.27458 | -52.91193 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3eed6bb-ad56-3125-ab8c-2653cf8b7c02 | -20.23871 | -46.7548 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28081f3a-0281-3978-a0d3-04c94e19b815 | -19.44012 | -56.57594 | 2026-04-24 04:32:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 646e9cdc-39f9-3308-ac47-b3e00d7f8099 | -19.43253 | -56.61494 | 2026-04-24 04:32:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e2486e51-82ea-3834-8ece-b956fa75f4ef | -16.70658 | -44.95431 | 2026-04-24 04:32:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1952ac02-ff22-3f55-992a-721299175e12 | -18.27349 | -52.90939 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b27c4ff0-dd52-3f6e-b8f6-108dad975f74 | -20.19519 | -46.75668 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af8d3841-a1a3-31d3-b9b6-fbc58d409775 | -17.47816 | -51.09207 | 2026-04-24 04:32:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac3def6f-ed33-3245-a41c-207383b6527c | -20.21197 | -46.81528 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfc55eb4-0901-3bf0-84f3-e62a5f644e73 | -20.19526 | -46.73093 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03a873e9-9c5a-3edf-96a4-47982c939fa2 | -20.18726 | -46.88717 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9505acf6-d747-3cd1-b1a6-83e920ab17ea | -20.20187 | -46.88524 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9f7908ec-5fbc-3d5b-90a9-d04d97d1e0c1 | -20.24193 | -46.75852 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 825f575d-e651-36b6-a8dc-15b164cd03b4 | -20.22978 | -46.76669 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5c2713e-1ae7-349d-9c88-9858cfdcbd5e | -19.09463 | -56.06094 | 2026-04-24 04:32:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 11558336-0a43-3c84-b41c-79031155c5b4 | -19.09903 | -56.06192 | 2026-04-24 04:32:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9a240c0f-e8ec-3c70-a4c2-36919d261494 | -15.96913 | -51.36691 | 2026-04-24 04:32:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d21046e-14e5-3833-8b93-faab1938636f | -22.93776 | -47.16585 | 2026-04-24 04:34:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 33c6e98d-533c-3936-b8fe-2911a2dc0bfa | -25.74969 | -49.56095 | 2026-04-24 04:34:00 | NOAA-20 | CONTENDA | PARANÁ | Brasil | 4106209 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b1e7df95-7b95-382c-b618-bc558799f695 | -22.09651 | -50.23627 | 2026-04-24 04:34:00 | NOAA-20 | POMPÉIA | SÃO PAULO | Brasil | 3540002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 128b81c3-7e5e-39ef-9e69-ea9a7475e46c | -23.04747 | -52.46666 | 2026-04-24 04:34:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f9db969f-a096-3c1e-92c1-9e136de05a26 | -27.4991 | -51.39816 | 2026-04-24 04:34:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b43eec18-9684-39d0-a0f4-3dc8aa32e4bd | -25.18747 | -50.15909 | 2026-04-24 04:34:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2ce603d5-8b38-3aaa-aae5-a18c380746a3 | -23.03955 | -48.43418 | 2026-04-24 04:34:00 | NOAA-20 | PARDINHO | SÃO PAULO | Brasil | 3536109 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9104fb06-4969-30a7-b87b-a2ad91b7ce0f | -23.40582 | -49.34951 | 2026-04-24 04:34:00 | NOAA-20 | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e14bd641-96fd-3412-a368-dd6e150d3c1a | -22.36662 | -48.35007 | 2026-04-24 04:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e6df35be-227a-3b80-bc57-5cad695c8b70 | -27.49517 | -51.40138 | 2026-04-24 04:34:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 47d9f9a0-1997-34c0-a327-6c85c37e3e5a | -22.93187 | -48.80508 | 2026-04-24 04:34:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b24a158-612f-3c6a-aeee-969be825db81 | -23.06757 | -52.43287 | 2026-04-24 04:34:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3b3ff808-6176-3bc6-a230-e781623b0e24 | -25.65101 | -50.12345 | 2026-04-24 04:34:00 | NOAA-20 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c6f8ee1b-c24c-3d0c-be5b-4fa525af30f5 | -25.89788 | -52.17514 | 2026-04-24 04:34:00 | NOAA-20 | MANGUEIRINHA | PARANÁ | Brasil | 4114401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8e4cebd9-1aec-38d3-9a19-baae794a048f | -25.65434 | -50.12405 | 2026-04-24 04:34:00 | NOAA-20 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e38e2acc-1abf-30df-9e07-cbe56be4021f | -27.94877 | -51.06155 | 2026-04-24 04:34:00 | NOAA-20 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a42355d9-4a0e-3a91-bfb2-a52d5bc16ab1 | -22.97043 | -52.69408 | 2026-04-24 04:34:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 848e6930-5779-3b71-bcbc-a6b0303d88a0 | -27.89963 | -50.22567 | 2026-04-24 04:34:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 18c0359e-7780-3f43-8a9a-4a6e14ebeb39 | -22.96972 | -52.69818 | 2026-04-24 04:34:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2b2b902d-4cfa-3bbc-8c7d-0c2f47127cae | -27.94938 | -51.05763 | 2026-04-24 04:34:00 | NOAA-20 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 973cbd3b-ff63-3505-82a8-c13984eb5f08 | -27.90023 | -50.22166 | 2026-04-24 04:34:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1e7f52e5-b020-3b25-94b0-01d0927cb39c | -23.37937 | -51.12671 | 2026-04-24 04:34:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1f7e1949-4112-3abb-8ff2-99a3a790b83c | -27.49578 | -51.3975 | 2026-04-24 04:34:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6e0dd164-6a27-3b37-8149-c4bcd764c50a | -23.55896 | -47.5169 | 2026-04-24 04:34:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0b130a87-1e06-3cb9-914b-64764b86afea | -26.49869 | -52.17892 | 2026-04-24 04:34:00 | NOAA-20 | ABELARDO LUZ | SANTA CATARINA | Brasil | 4200101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 698c8e74-0c68-3eab-8ffe-5ec96864c7ca | -26.47721 | -52.02578 | 2026-04-24 04:34:00 | NOAA-20 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b04a4dbc-b8c4-3b3d-bc09-872a79add135 | -23.31954 | -52.21538 | 2026-04-24 04:34:00 | NOAA-20 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c2ed676b-413a-3ed5-9f34-b671efe6172c | -23.53923 | -47.63132 | 2026-04-24 04:34:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4be7c0cf-a4d0-33f2-9021-3fce060cd5e0 | -18.2659 | -52.9016 | 2026-04-24 05:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| f626f747-f0e3-3c1a-a6bf-019d3433fcb4 | -18.2858 | -52.8983 | 2026-04-24 05:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 86fbfe6b-4629-3d01-ac7a-422643539abd | -9.23294 | -46.64769 | 2026-04-24 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68d96411-2ec2-36a1-b801-47c55aa86885 | -9.23219 | -46.65381 | 2026-04-24 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 52ee1484-c5a5-3dd1-b09c-a0ce5db22d68 | -9.23559 | -46.64998 | 2026-04-24 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bee8df7a-12a6-3904-b150-854f9ea634c4 | -18.2858 | -52.8983 | 2026-04-24 05:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9b20d1b2-d0a8-38f7-84d3-464b8e75a7bd | -18.2854 | -52.92 | 2026-04-24 05:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 8b2272fa-ad17-3942-8adf-fd81a850c505 | -18.27745 | -52.89538 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75188cba-89e5-3cc6-aec3-0fb51a401be1 | -11.57721 | -54.88884 | 2026-04-24 05:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53e0b020-2220-3169-a2ea-9731b2bb37a9 | -11.91185 | -58.06916 | 2026-04-24 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d7a70f0-ad2a-316f-b3f4-c0617c1758ad | -17.47893 | -51.0904 | 2026-04-24 05:21:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7812b1a0-6c89-3c54-ae64-bf93c6516bae | -18.2677 | -52.89071 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 23cf51b7-1e4c-3ba4-a422-4225d9ab4e6e | -11.85492 | -55.01562 | 2026-04-24 05:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b481a94-c6be-31f2-b0a6-7cba3a2bdeb0 | -13.98975 | -56.6492 | 2026-04-24 05:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 410dfafd-024c-3073-a1a8-786ff61cd6b4 | -11.94489 | -58.08176 | 2026-04-24 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27f1c157-6ff8-34f5-ae88-e8716c825a63 | -11.84639 | -55.01805 | 2026-04-24 05:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 687c3f62-72a5-307f-bf26-9436f85956be | -12.98606 | -54.68495 | 2026-04-24 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04c0306e-5b6a-3298-8d4a-f715b0b7914c | -12.09257 | -51.22537 | 2026-04-24 05:21:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f90c8ea3-7dbe-38eb-bd80-152edb8917a5 | -18.27575 | -52.91085 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 57c5c6e0-853e-3a3c-9577-3ac615c30e50 | -12.98658 | -54.68105 | 2026-04-24 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f20e243c-1f97-3802-a369-a9b9e85e5a6a | -18.27377 | -52.88216 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README6.md)
