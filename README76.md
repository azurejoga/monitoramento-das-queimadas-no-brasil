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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4d64178-0a69-3a51-8ac3-13c59991f85a | -13.2677 | -47.85926 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2d69d8a2-693f-30a8-ba22-293514d0a581 | -10.91098 | -47.80531 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 339c8144-86df-3993-9001-ac24f7a7919e | -13.57164 | -49.6148 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c4b9bb1d-5024-30df-825b-ef1b7f01eb77 | -13.23123 | -48.56168 | 2025-10-29 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0dbea197-0f2c-3fb5-b5e4-85c97ac9c06b | -9.50752 | -46.51512 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d3b3826-f6c9-3713-8666-e269c30c3d3b | -13.61797 | -47.60513 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc429c89-3c12-3e6f-9cba-fa442fa42cd6 | -13.64046 | -46.50541 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3502893-ef1e-36fa-862d-9d4e5156d25e | -12.86328 | -48.62624 | 2025-10-29 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af830854-2bae-37ed-aa82-4874679aab5f | -10.90286 | -48.37795 | 2025-10-29 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 587618b7-3779-3e96-a638-1fce050e24cf | -10.85554 | -47.89642 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c6840605-b168-3136-a1b6-1a8203fa0eb7 | -10.87978 | -47.99597 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0c129bd-065c-3641-90de-9196207f2b07 | -13.28866 | -47.36881 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 050dd224-8f1b-35a1-8fb4-6a8309ef0bb5 | -10.5494 | -50.00039 | 2025-10-29 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca80b39f-1642-36df-aa0f-b076d4176157 | -12.87008 | -48.63181 | 2025-10-29 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5aaaa660-297a-3136-be53-7a9e9a65c47a | -14.12904 | -44.06747 | 2025-10-29 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eab38b52-7263-3243-93bb-59d242393d30 | -13.90924 | -48.46561 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f331a3e-0fd3-3e84-9e2b-deac6607cb38 | -12.53255 | -47.53768 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9166e283-f81c-3820-a387-1d8d9ec3e810 | -13.37263 | -46.63564 | 2025-10-29 04:46:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dad7a19-ed88-3eea-82f5-6ba1b6d08d1a | -14.60802 | -48.43016 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7f4066e-98aa-3c4b-a523-e55693a00a80 | -13.0358 | -46.7356 | 2025-10-29 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c283eaca-cd50-3ef5-95c4-30790b561654 | -9.27274 | -46.38636 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01975ea8-e559-3f09-a809-443f5cad9489 | -13.17415 | -48.44969 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60eff644-5790-374b-b330-ac80322d3c20 | -10.3697 | -44.27098 | 2025-10-29 04:46:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af9bb67e-8f4f-3ad2-8afb-7e6047ced05c | -12.29344 | -47.00663 | 2025-10-29 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ab435de-cedd-37af-a3b2-4c4b1ce4ea3a | -12.09319 | -47.2532 | 2025-10-29 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0fc2b43-fae2-3257-8776-e48c889db65d | -11.27244 | -45.52678 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f823f783-b7e1-3f83-834b-c5c12873c334 | -14.65207 | -48.39606 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 416647bb-da2a-3f11-8588-0bda3f1f5aaf | -12.82596 | -47.26738 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 903b8f0b-4925-30f7-ad62-7f5bc3bea5f7 | -14.1982 | -48.35604 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f7dd29c-2bdc-34ee-868d-e57ae9a01223 | -13.57456 | -49.59465 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3dbeda5b-9db9-36b0-ac6b-7b10f9e7d221 | -10.23086 | -52.14805 | 2025-10-29 04:46:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b92dfea-b0cc-32a7-be5c-c8678fd47513 | -13.54826 | -47.17317 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55024e48-7e36-3237-95d7-ffeba0ddb104 | -13.56236 | -47.15313 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe96bb9e-92a7-3582-a160-7226b849870d | -13.32143 | -47.43569 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dbe6903-a924-34ce-b8fd-03c957aa36bd | -10.65571 | -47.99682 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9122e32a-38f3-3779-bd0b-83379b9b541c | -13.5561 | -49.57089 | 2025-10-29 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5d0207b-6aff-3c0e-b747-0b92ab4b4492 | -13.20723 | -47.05728 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1dad7c8-3206-337d-8b2d-e71661c6522d | -14.26319 | -48.11724 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f210abce-046b-358b-96ff-f08b66f7043d | -13.63728 | -46.49663 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 23b491dd-56a6-3016-9043-aca16e884022 | -14.32041 | -46.52533 | 2025-10-29 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c558358-7445-3615-bb17-7e4d7c623f75 | -10.51304 | -47.72709 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c53dd524-6e24-3b81-ab1f-566bac38faaa | -13.31278 | -47.70691 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 024762df-9ad9-3dfc-9c43-224dc7ccc4d5 | -13.6925 | -47.68359 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c20d47ec-0277-3e41-9831-e364d46c3105 | -13.2216 | -47.07469 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 898c28f5-3a31-35d9-9ee3-c65489c90b5f | -12.18472 | -46.71705 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a4dec425-0ef4-326f-9419-bc6bf8ff195e | -15.11159 | -43.26144 | 2025-10-29 04:46:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c8a60bf3-b699-332d-980d-e30ba6c154d6 | -9.23105 | -46.35777 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb4f8a63-94e0-3b0a-aa30-111eb56a252c | -10.65017 | -47.90109 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d165148d-aa7f-340d-9410-05b2bffac6e8 | -13.64683 | -48.4362 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21e3ee43-de78-328c-84e9-89ea8582c7de | -13.57157 | -49.59016 | 2025-10-29 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 746a451e-4b83-3e3e-9e19-e9ad077a510e | -11.06179 | -47.53385 | 2025-10-29 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b7509ad2-d06d-3631-8506-598538980e8c | -13.61528 | -47.59488 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de91969d-2551-3c18-8dc9-608072a5c5fb | -13.42278 | -47.39282 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 590e6bd4-bc2e-35c0-b4c8-ce7a8b961285 | -10.94862 | -47.62419 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eee7842e-a750-38b9-993d-5a86786a849a | -15.09564 | -43.83786 | 2025-10-29 04:46:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c42c6c7d-24be-3bba-9104-f9414ee1818b | -10.51819 | -47.71834 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f1ca2dd4-c666-3e01-956c-60187fe2d14d | -13.94531 | -48.48108 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6716182c-b117-3170-9091-64187f93cffe | -10.88591 | -50.08983 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2262dcd9-3e0f-33dc-aa33-6f90794e8cce | -10.76731 | -47.89247 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9b7b533-488b-39e8-9c10-753720e81655 | -10.63892 | -47.89895 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc6700dc-2dc4-3383-8c5c-3f35f417460b | -10.85383 | -48.64169 | 2025-10-29 04:46:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fde533de-f898-379a-9bd9-95f6f60c9072 | -12.06645 | -45.71668 | 2025-10-29 04:46:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67b4e6c3-23c6-3242-9ef4-4767460cd06d | -12.15896 | -47.69439 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d019e07-b465-3aad-8954-b2ccb0eb0e86 | -14.2568 | -48.106 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4ded7945-f4bd-3dac-85c6-9e8a73000ab8 | -13.27348 | -47.72921 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60c236fa-6826-3f26-88db-587b96964abd | -12.44292 | -43.75443 | 2025-10-29 04:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 136b9dde-ec68-3c0f-88ac-c11678b3510d | -14.78982 | -46.18109 | 2025-10-29 04:46:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ddabae5-213b-3bc0-a8ec-a202a381755e | -10.4257 | -44.98965 | 2025-10-29 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a2e3561f-e0d8-3e5d-b3e4-79b103d36bbd | -14.59847 | -48.41397 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 325bf786-228b-31b0-aeef-122921c377c6 | -10.63656 | -52.18206 | 2025-10-29 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e6b30ec-bfde-35fb-9ef7-b0976dcc7241 | -9.81953 | -47.71478 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f97b1c3-e455-31af-89af-7aeeaf7a1cad | -10.36626 | -47.562 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb984974-fd09-3d61-97e7-dd1bab59f0cd | -10.51236 | -47.73174 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce465bc8-16f2-32c5-b7f2-59135faf1cc8 | -13.64856 | -46.46201 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 817dcd8d-8e9b-32e5-ac5b-51eff85c0aec | -10.636 | -52.18556 | 2025-10-29 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02752d41-bed6-3453-b876-c615099b487c | -13.81561 | -41.6913 | 2025-10-29 04:46:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 11174196-4b76-3d2d-963d-4632219fc9e0 | -13.66899 | -47.19344 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2f7a972-3aa9-3315-978a-0e4c17b6359c | -11.99916 | -49.849 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5b09d8f-1cae-3471-87c9-ccaa760aa6d3 | -13.30929 | -47.46498 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 468376b4-00f3-3400-b6f2-de6db162c077 | -13.35402 | -47.67168 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c484b8b9-4f56-33ac-a0a4-8eef159a682e | -14.48588 | -49.32837 | 2025-10-29 04:46:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d1bd16a-ebad-3062-b248-9a76e7a002ec | -12.55912 | -44.9647 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4d0d828-6e08-301b-8451-78f00f6b233e | -13.6569 | -48.44727 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6140ef24-feb7-3371-9d09-749f5cbc2ee8 | -13.27741 | -47.72987 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3ea63f7-0a6e-3ee0-b53d-fd49b6496edc | -11.26065 | -47.81923 | 2025-10-29 04:46:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42a846c6-d853-3c36-bd62-1dc7ec242189 | -13.34544 | -47.67527 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edd94bac-97f7-3a3f-b75c-dc2abee4a352 | -10.6291 | -47.88577 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7d66eab-cb80-3038-9cb6-ecb7adc99385 | -9.87967 | -44.88334 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83103b53-fda7-32f0-acc7-6cd055e0e2e7 | -13.55251 | -47.35128 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68c99eac-7d44-33c4-a0f2-faf460f85e0e | -13.69455 | -47.68523 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3703145c-8db4-3a18-b953-6fa6e22a6e0b | -12.91609 | -45.04107 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcef7afd-29c8-377a-8ba8-ae2ec3c4221a | -13.46697 | -47.46074 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 290387a4-03e9-3fd9-80f8-51e4165c27e7 | -13.05142 | -48.46858 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb7bea09-ef85-3ea2-9ccb-bb552a374fbd | -9.54424 | -46.92384 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d3b57c94-04b1-3352-b68e-900fca64a5f3 | -13.63745 | -46.46324 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03105b9a-16df-384c-85c4-eaced50188c2 | -13.04455 | -48.46298 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97cb3f46-1958-3faa-9cba-c77498a90ae0 | -10.91983 | -47.6055 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 374259be-d5fb-3fd9-bf92-bfc17a42a8d1 | -10.86044 | -50.14317 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4692c9c0-0952-3c77-b1ec-59d2aa07698f | -13.86776 | -48.48433 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90ed6083-5a2c-3a9e-abc6-61f34944dc65 | -14.52549 | -47.98683 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README77.md)
