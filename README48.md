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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bcd3afe-db9c-3897-a34e-7bead9612da5 | -17.81632 | -57.65614 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7b316c94-2e63-3df5-afa7-25d62a5ea38f | -18.05831 | -57.54296 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1940c1b4-3a8e-3a19-bac9-52e9b802c529 | -17.26455 | -46.9082 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0ddd8dc-1baa-31f0-bbcb-c7e095da7c21 | -17.88456 | -42.86825 | 2025-10-09 04:21:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 34.8 |
| f184b884-27e6-3788-af06-9cfe07caf4cf | -16.61679 | -46.77367 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2521f56e-8043-35dc-bcce-701870432d06 | -18.0318 | -57.56491 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 699e70ff-f3eb-3d7c-b33b-1f98744c6409 | -18.05657 | -57.55103 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| db4c90d0-09b4-3faa-ad52-4b63d1fe5fed | -17.95609 | -44.41805 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee702cc4-acf1-3762-a8a7-40422922c832 | -18.41821 | -45.24447 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1dc743dc-1d49-3503-8907-df77c5a054ba | -17.95136 | -44.99759 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ce495f28-2e90-3ce4-a53d-098839ad135b | -17.49332 | -45.30549 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 167422c1-b07f-3e4e-88d3-9caf9f4d2b4d | -19.94436 | -44.88909 | 2025-10-09 04:21:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 825eefd0-b7ab-3bbb-8f8f-1e5bce846b61 | -17.88551 | -57.66053 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e9ed6330-c2d4-3f71-91a2-cd603b660843 | -19.47432 | -55.47221 | 2025-10-09 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 03c3a3db-2b35-3e06-a137-825a8377de58 | -17.639 | -47.20422 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e9e10c52-b7e1-3b5b-817c-87260b497d3b | -15.49476 | -47.95998 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f305425-d5be-3f41-9225-8165304c9190 | -15.48804 | -47.95879 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 328a486c-d2bd-37a6-a0c5-6bea618d7a58 | -18.03038 | -45.00529 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74e666bc-94a0-3f61-abb4-25d4389c01af | -19.50326 | -43.83668 | 2025-10-09 04:21:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| adae2c7e-f10b-3ecd-87bb-c4b712ef7626 | -14.45765 | -52.89646 | 2025-10-09 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5184a0ce-122d-36df-8879-43a0b0476a13 | -15.36221 | -47.29491 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c1294ff-0d16-3818-9766-d231b41bee1f | -14.93374 | -46.78577 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17cb5450-f6ac-36a5-aad0-d2f94412cfb5 | -15.52468 | -41.85153 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1f67f81b-dc58-324a-873a-384c894d8e95 | -17.38388 | -46.88416 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd5d1cf-371e-3e74-abbd-8429396e94e0 | -15.55577 | -45.29824 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cde32b2b-4aff-370e-9d31-079b928a55d2 | -15.4814 | -46.86622 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19dc3580-ab61-3b6d-be3a-bc89f6c9fffb | -18.01901 | -57.57067 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8ba06a54-94e9-3509-84f3-50ac6b95b454 | -15.7994 | -41.46172 | 2025-10-09 04:21:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 521c90d7-e809-3337-b366-a6051d806c3b | -19.71558 | -44.00057 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e19b5355-035f-3485-a28a-22347196ee3e | -17.31794 | -49.36129 | 2025-10-09 04:21:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9be218e6-af3d-31aa-8d95-4dd879f84082 | -17.82306 | -57.62498 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 00473d72-eb20-3de7-bfa3-8d1445da878b | -17.89108 | -57.66176 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b3bb0283-36b6-3bd4-af0b-5fe2da8f73ba | -18.00613 | -44.97752 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd336f63-b328-3134-a5be-c50df49373a5 | -17.48186 | -46.95171 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0707124f-d07f-33c2-973b-9645896d5a7d | -17.99524 | -57.49187 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1b90b56c-3b0d-3433-b426-deb996df2058 | -15.05712 | -48.07911 | 2025-10-09 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c5838a9-aea1-3d67-a751-f6ebd02b7e1e | -16.59941 | -58.15676 | 2025-10-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4d0ef998-631d-302e-b0cf-979abb35906e | -15.16115 | -45.74713 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6229b4a-10c1-3ebc-8642-74a14bc8cb47 | -15.01053 | -47.53225 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 55c89d49-3919-3183-883d-2bcbb5928704 | -16.42498 | -47.82522 | 2025-10-09 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa17ac07-666a-3f9c-b471-498431263a5e | -18.0497 | -44.44374 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da1ce7a9-4538-3feb-972b-3d5aeb06964e | -20.29718 | -49.69589 | 2025-10-09 04:21:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a3e5f7a5-8f96-3ef1-b028-991b35c2f2b7 | -20.30068 | -49.69598 | 2025-10-09 04:21:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 035f34c7-d86c-343f-abc8-b7392266d5bc | -17.3767 | -46.88663 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 503f9d3a-d4e2-3fe5-bf2e-0d1cfb3363b0 | -15.27794 | -44.14409 | 2025-10-09 04:21:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4c3ae19f-e6e5-3ee6-b51b-46856c5c22e5 | -17.88991 | -57.65738 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| da16da51-0ab9-3fe0-86ea-f4a84ba4f7d6 | -14.52498 | -48.70239 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5480e638-7e4f-3c3d-88da-446565cafd31 | -15.39263 | -47.3145 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 484ec756-7029-3b32-a356-406a0d295e71 | -18.41248 | -45.23555 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fac4695e-05c7-39c6-b015-5c1efb676d55 | -17.57823 | -46.06576 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44d44e36-eb39-3f49-9a50-728fc575273a | -17.63569 | -47.20365 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| de4de582-b707-3c4d-9f06-27305f3ecb16 | -15.15945 | -49.56321 | 2025-10-09 04:21:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a71de13-c2ea-381c-a46f-70ee54cf9240 | -17.84162 | -57.64723 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 13ed7646-ef36-32df-9b68-fbfe739aad65 | -17.89539 | -44.25973 | 2025-10-09 04:21:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edb89198-4b72-3483-ad55-42fb8bff9e67 | -18.08517 | -44.44809 | 2025-10-09 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea7a8452-e7ca-37c1-b28c-c161524e94b4 | -15.36942 | -47.10069 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ba64e46-875b-3338-8930-4370d3b2d9dd | -19.49958 | -43.83605 | 2025-10-09 04:21:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c907a7d1-d6ed-3ed0-b5ce-775e364a16b3 | -15.29785 | -46.15576 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c191046-cfdf-33b5-8857-b2839aee4219 | -15.47353 | -47.95295 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a328bab-0efe-393d-8b67-07357a5024c1 | -15.48414 | -46.87035 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ee3283d-3462-39eb-ae17-19ad7b31bb66 | -19.18197 | -46.50886 | 2025-10-09 04:21:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 129ef4a2-a119-3b4d-9222-6b10562cc433 | -17.52866 | -46.0537 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d8956d8-4e95-3b93-ad25-d855c5638f68 | -16.43151 | -47.95411 | 2025-10-09 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea77d0fd-ce03-33ca-a5bd-9d036206c124 | -18.18503 | -47.42339 | 2025-10-09 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd036864-e8bf-3a2e-bd61-072d4716ba65 | -17.37227 | -46.89326 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95eb8e8b-75a8-3808-8787-c28202ab83d4 | -18.03323 | -44.98571 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8614431c-7a8e-3603-9880-864c808a53f8 | -17.52998 | -46.75243 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c6bcc23-7fd1-3f83-aa9c-427945c3ad7a | -15.38441 | -47.30195 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c78119d6-b613-309c-933b-54489b712778 | -17.91143 | -57.51013 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 12f29343-e7bb-3647-af29-5858834ca195 | -18.24949 | -46.99207 | 2025-10-09 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ee23e0b-a25e-375b-99f2-299d6e0df52a | -15.72821 | -46.24809 | 2025-10-09 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45a08d61-c3e1-36aa-a88f-5b18a2b5b13d | -15.38774 | -47.30251 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edc33077-9fa1-336a-bb21-76c44bb765f3 | -14.97866 | -46.28571 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd9921d3-65ae-3462-ab5f-7ae3f87830b8 | -17.23081 | -46.92833 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08a2724c-2693-31c5-b94a-5d4108fa67e2 | -15.38691 | -48.05957 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34e47ef6-2b3b-34e6-b0fc-a129275a1d72 | -16.27653 | -47.12083 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b31b5ca-b2bc-3d38-a970-9fac2fe2eadb | -19.18253 | -46.50514 | 2025-10-09 04:21:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0801c6d-7a25-329c-83c5-48199de3cede | -14.84468 | -48.45023 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9079c107-4ea6-3c3d-b7ff-61fb97df7463 | -15.06387 | -48.08028 | 2025-10-09 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a1a2040-6894-3896-974a-829654f9184e | -15.80324 | -43.78405 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2266c0ef-92eb-3063-b430-f62d10df3748 | -18.18446 | -47.42701 | 2025-10-09 04:21:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03a87fbc-d26f-3330-b1cb-72e3d6a099d6 | -17.97441 | -44.96092 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37e936c6-cae2-3941-9ddb-e44815a2ddd6 | -17.93798 | -57.54324 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2d3b7751-6fee-3d12-b159-893c80e79c8a | -15.46897 | -47.95978 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 713efab0-6a46-3e48-95cc-ac4a53ef4ad8 | -17.96112 | -45.0033 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28b42f47-603e-3384-b4f7-d1863f083e69 | -20.30059 | -49.69654 | 2025-10-09 04:21:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 88c05402-7b04-3c6f-91b3-102f58de3481 | -16.37832 | -46.38759 | 2025-10-09 04:21:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9533062-9dff-3fa1-97ee-608187ecea82 | -18.78609 | -44.61647 | 2025-10-09 04:21:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f44814c-948f-3f27-a958-59e7934ad68a | -18.07362 | -44.47869 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c90d095f-3517-3cea-a6f6-91a6be1a1fb6 | -19.17966 | -46.50896 | 2025-10-09 04:21:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8546011-63ae-3d54-bdb2-d009d09b8234 | -18.02026 | -57.50993 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c3ba1413-079c-3ae9-b6b5-ee94622f9f81 | -17.49729 | -45.30221 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43b1dd79-70e1-3a4b-b31a-63783bde0adf | -16.29273 | -45.24223 | 2025-10-09 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e1a30d8-f86b-3b4a-9855-54f46a5f92d8 | -17.89182 | -44.25924 | 2025-10-09 04:21:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b67867f-6aa3-33ee-8824-0176111fc3c0 | -17.95481 | -44.99817 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 91b25387-8cb8-3d7b-9fda-3207cbfcdb1d | -15.16392 | -45.75127 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54793e51-d964-3fdc-8d3c-2789553ae5ae | -15.5625 | -45.29933 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33cbde7c-c125-303b-b4bb-020009272f45 | -15.48858 | -46.86379 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba0cc37f-d1f1-35a8-bcd2-741ef19b03cd | -14.46042 | -52.90601 | 2025-10-09 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6027546-93b9-30ec-8c9a-a65c291144ad | -15.32109 | -43.85085 | 2025-10-09 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README49.md)
