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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b4b3c4c-ce3d-3dde-ab74-1096ab23466e | -14.5199 | -48.38306 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ca25ae8-a870-3e13-8700-7c429627ee52 | -15.27359 | -47.89815 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f65f603-0fd5-3b06-9634-3f130427085e | -14.51594 | -48.43772 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab34a7d6-9382-32fc-b455-d742da0663ce | -14.78613 | -48.31006 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5db4002d-aa6d-3a61-bf0b-cc3dd1cb858e | -13.78362 | -47.96527 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2da18bf-c59f-3318-aded-db7482a786da | -15.2808 | -47.88459 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11c08b66-8d23-36ee-9c70-e22d37d69661 | -16.67635 | -44.55659 | 2025-09-30 05:10:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c45de90-23d3-384a-888b-556f0d04c670 | -16.22207 | -52.28421 | 2025-09-30 05:10:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3953d421-8bf4-3c99-85db-ea62e5968a75 | -14.51981 | -48.42841 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28bfed33-89a4-39f7-b239-c82cd91e9112 | -14.52615 | -48.49018 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c08d786-65d6-3c36-a8dc-99f9dc925aa5 | -15.6225 | -46.2542 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01d6324d-e592-3acc-82f6-41b10f24f6c4 | -15.128 | -48.38964 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41cdb15b-4457-3c36-bc88-aba822cf3113 | -14.44668 | -46.3564 | 2025-09-30 05:10:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25419203-3a93-38f7-8067-c25fcf518575 | -21.04101 | -45.68785 | 2025-09-30 05:10:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b58b177b-5287-3951-9e47-67eed5863ae6 | -14.52019 | -48.44794 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b69b96a-2a2f-3040-8aa0-0bd8b55211b2 | -13.78621 | -47.94355 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 926c7863-1413-3aba-9b4a-5af16ff30f10 | -14.71092 | -48.14373 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0612fd5c-2228-3d8c-b825-f9adaeaffa7c | -15.84083 | -59.60212 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54992ec5-ca72-30e9-94ab-c2bd0e28d4a0 | -14.51946 | -48.45435 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5a3af08-08dc-3897-951e-91a27dfd734e | -20.62522 | -46.17561 | 2025-09-30 05:10:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0aa186e3-1856-3871-95e2-2ee51c7be331 | -15.24954 | -48.74874 | 2025-09-30 05:10:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3c2df12-6f75-3fe6-ad96-9ecbbadadfb0 | -14.78652 | -48.30673 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46f91727-0858-3cef-be28-743c337e8506 | -14.00511 | -49.63073 | 2025-09-30 05:10:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf1d80d9-041b-3be0-9ff6-e8b8889dbc46 | -15.24919 | -48.75183 | 2025-09-30 05:10:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9f15ada-dc04-3e8c-8fd0-3d17b4258f15 | -14.56649 | -48.23517 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fdddc75-604e-392d-92fd-5f1a33e06ab4 | -17.91201 | -57.58657 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 37a87287-69dc-33c8-a069-f1051228a3c4 | -17.88406 | -57.6238 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 32984ede-51fa-343b-969c-f3f69aa1518c | -14.65753 | -46.96741 | 2025-09-30 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82df5fd2-6a03-33ac-8bc8-affad5ccc613 | -14.50962 | -48.42296 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbc36357-e793-34c5-837f-a04a78f41201 | -14.54651 | -48.26576 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2c7c0b86-d4ae-319e-96fc-9860eb34dab4 | -15.24719 | -56.79764 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56d9acb0-02f8-3ee5-8e4e-eaab25855745 | -14.51359 | -48.43496 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2873c30f-e2e2-31b2-8a40-bf4e8f80e08d | -15.17046 | -52.81971 | 2025-09-30 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6beb5fcb-e545-35b9-8917-84a8f921cd92 | -13.73184 | -54.72403 | 2025-09-30 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9d030975-5a30-3980-ae3c-be783bed3dbc | -15.62872 | -46.25492 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52cc77ec-0563-3a5b-a225-c50f6af90956 | -17.90417 | -57.59291 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3866ac9d-fd72-3c97-a1ea-314dd1ced225 | -14.59369 | -48.28449 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61b904fd-9a16-359c-8cd2-d869e9e4861c | -14.51904 | -48.39011 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d216f8c-2915-31f5-bb1a-354145aa724d | -15.27399 | -47.89458 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c6187ae-9ec8-3a42-a82e-9b805c013938 | -19.71475 | -45.88437 | 2025-09-30 05:10:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09eedb91-15fc-392f-a450-ec2ea70d4ae0 | -13.88002 | -57.65861 | 2025-09-30 05:10:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e09ca142-5acc-35bc-be45-e2acfa25bdf9 | -14.51698 | -48.45165 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 832f3e25-e0f0-3f1a-b3a8-5e2f387115dc | -13.79508 | -47.86898 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de695eb8-f1fb-343a-98ca-6e5571387ce7 | -15.89711 | -57.49009 | 2025-09-30 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceaca4cd-199e-34c7-9731-76c05790ddbb | -16.38542 | -47.03341 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eddf8477-2ad9-3b5a-a0c7-0ff3b7a15b9d | -14.51449 | -48.42756 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b90dd333-888e-397a-af2f-8298ac3ff49c | -14.51447 | -48.45058 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 97803b88-46ef-3fb6-aa2a-3a1291f9f1ad | -14.52566 | -48.38045 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3370350-49c1-3404-bab3-8d0a2188cfbd | -15.24664 | -56.80127 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 969fbdc6-d5b3-3e80-b747-1b9bb2f093d7 | -13.636 | -48.0406 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77230901-2858-3b70-9a15-d82b38fa414d | -14.53654 | -48.25695 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e06882ae-5b2e-3663-8d87-be155f26547a | -14.52095 | -48.44136 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0af54fa1-fc2b-374e-84b5-eba314f9c134 | -16.40889 | -52.17319 | 2025-09-30 05:10:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea3e4a37-27bc-39e5-a530-642b1bbde275 | -13.75674 | -54.72792 | 2025-09-30 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7fb91c0-d920-3c0e-943f-905953c2d048 | -16.4234 | -47.03505 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5f9db76-0d20-3b91-a937-6d52ca57555f | -14.69899 | -48.24612 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7854cebe-2b06-3747-ad0b-dcace6c96dbd | -20.6144 | -46.06656 | 2025-09-30 05:10:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83c868eb-b08b-3d29-99ff-1bd85cabc0fe | -13.78911 | -48.01184 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e399221b-f636-3869-8608-9d0f8fba2105 | -15.0746 | -45.0619 | 2025-09-30 05:10:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5dc05366-5d84-316d-b11d-472fd772358f | -14.51777 | -48.44515 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cfecf31b-18e0-370a-86bb-8d3311389669 | -13.73124 | -54.72816 | 2025-09-30 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cbfc023a-baf5-383c-9d88-ed8bc69f4e2f | -15.914 | -59.49821 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2000635d-69f4-34dd-a8ab-6b1829d70809 | -15.26839 | -47.89395 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48ac3464-fd92-3ead-908d-b3f18e2fc992 | -14.55393 | -48.48375 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f55a881-5617-3482-bf1a-707ad5d3b240 | -15.38993 | -47.0703 | 2025-09-30 05:10:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79755768-38d5-3605-8bfd-0a7073969c52 | -15.26701 | -47.85598 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71ffc8e9-c2db-37c4-9150-2cae558af774 | -15.02964 | -46.9841 | 2025-09-30 05:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d407eb11-87f2-36f9-970b-411a423b039f | -20.06006 | -46.79707 | 2025-09-30 05:10:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57de32e2-c8bc-3e64-92e4-726c855dee79 | -14.53757 | -48.23707 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 469bf117-111f-31c3-803e-d58cfba78cb3 | -13.78316 | -47.9691 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8064d6a5-dd8d-3e46-8b03-027527a97edd | -14.5389 | -48.23613 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 156b3ce9-1774-3e08-a64a-c801bcd774b0 | -17.40145 | -47.15184 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2816abc-9196-3d63-9c91-49c591395cd2 | -13.631 | -48.03635 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a3de38f-abc7-3232-9730-cfe6a37b4dd4 | -14.52651 | -48.48709 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c88cf5c7-311d-3301-ada0-3b8c0efa24fd | -13.80527 | -47.96957 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 575d164e-facd-3637-978c-40d25d0ff1a7 | -14.54687 | -48.26265 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f29201e0-e6ac-38d8-9a74-38da3939d46f | -15.84655 | -49.49239 | 2025-09-30 05:10:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25e8f840-cd74-3442-a6e1-a8b3a3ebebc5 | -13.82735 | -47.49875 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed8ca640-3db7-3bc7-9a1f-b332841279b9 | -13.82767 | -47.49598 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1d8ecf5-51c2-35cd-8769-2e0bffc12025 | -13.78531 | -47.9511 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0fef345-cce2-3d88-8d66-1795da6e5533 | -15.17135 | -46.41599 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2e86113-35a1-3fc1-a94d-37a8e0a3a143 | -15.20897 | -50.11336 | 2025-09-30 05:10:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 818a84c3-972d-3c03-90b8-bb3a02fa45c2 | -19.22564 | -45.81673 | 2025-09-30 05:10:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0847b6ea-e729-346f-bd04-aaebed887ccf | -14.80588 | -59.71015 | 2025-09-30 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46f999a7-1f67-3ecb-9beb-449e0633ccfc | -14.70436 | -48.24724 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ade04a3f-16d7-364d-aee3-e1c6b76fe993 | -14.51005 | -48.41941 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5810534f-8222-3cfa-ba63-816ef2a1b330 | -15.86685 | -59.33655 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b052c01-5304-3a7d-a9b4-4ab79a6820a9 | -14.81536 | -59.69558 | 2025-09-30 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6ce19ef-bfe2-3674-854b-bbd7792189b2 | -14.70512 | -48.14599 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54e796ce-0603-3b1e-984c-50083b8473b6 | -13.80861 | -47.89564 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 622320d5-c14b-3075-ac7d-c5c45761e511 | -17.20493 | -56.35802 | 2025-09-30 05:10:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f5ce2afc-5947-34bb-bb6f-28ccd2afa8f1 | -14.53145 | -48.49102 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| befb211c-6628-36df-ab97-e4555f6eb113 | -15.27736 | -47.86493 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 501264d2-a73b-3084-8d8f-26780c891533 | -13.75004 | -47.92053 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1d8b364-a76d-3f4f-b9b3-7ca38084d0ae | -14.51675 | -48.43068 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a17c0ee-5df9-3aab-8d5a-6d9c1e3655c7 | -14.528 | -48.37985 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57e22e27-4532-3536-928b-3820b68af38c | -14.5882 | -48.19033 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28878190-0923-3497-9ca3-de84205d3b35 | -14.53148 | -48.37738 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1710d332-96ba-3bc1-afbe-e0724942b6d6 | -14.73687 | -45.66215 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fe50d07-db75-3a15-8e68-d7d9d927c5da | -15.26691 | -49.26771 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README101.md)
