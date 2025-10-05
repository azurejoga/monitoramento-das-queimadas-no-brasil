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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1655089b-3c77-3b32-bac0-0f7356491edf | -14.9352 | -46.8507 | 2025-10-05 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d641875d-890c-3991-89a3-9d34b8715b88 | -11.7519 | -44.7461 | 2025-10-05 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| d1fa38f8-f233-38ce-b01c-6e13ea5fc11d | -19.503 | -50.377 | 2025-10-05 00:50:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| bb66cd2d-f88e-3f59-927d-69250beeb4b5 | -4.6317 | -43.205 | 2025-10-05 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 8a812682-5446-3e03-97f9-e6713fc1705c | -6.4134 | -43.0489 | 2025-10-05 00:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| ab9feb69-71a6-3265-bd46-593dd4e4f978 | -5.4721 | -43.4045 | 2025-10-05 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 6b476279-c355-3d60-9f38-8a0a382fb351 | -12.4665 | -45.5386 | 2025-10-05 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 3796d480-6a4e-3794-939e-6153541424de | -5.6363 | -43.9027 | 2025-10-05 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| d5a27934-cb90-392d-b4da-dd7d072429de | -4.6318 | -43.1816 | 2025-10-05 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 157.2 |
| b6e1b08a-470a-35d8-9c5d-adf53cab20c2 | -19.5233 | -50.373 | 2025-10-05 00:50:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 252ad9f6-4829-3445-97c0-0b27440db692 | -11.8777 | -56.8769 | 2025-10-05 00:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| cf97102e-75d3-352c-9673-cebf2f324568 | -15.928 | -48.822 | 2025-10-05 00:50:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 05156341-b0e5-3d54-8dda-a0bf1ab95362 | -3.6196 | -51.0461 | 2025-10-05 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 3da45db7-1420-304c-b207-4d744e4eacc8 | -4.6505 | -43.1805 | 2025-10-05 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 260.3 |
| c85a8d39-1697-3926-a171-66d00dea492f | -14.3353 | -47.6755 | 2025-10-05 00:50:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| f90c1d26-5b7c-39bc-8ff0-3e0e7b62fc2a | -12.4669 | -45.5155 | 2025-10-05 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 176c5cc5-94b6-3e0e-8b99-d43eed282115 | -23.0036 | -52.7084 | 2025-10-05 00:50:00 | GOES-19 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 56.4 |
| df481136-c860-3c85-a188-9fe23281a5ed | -12.9844 | -51.0433 | 2025-10-05 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ce07ee91-d0f3-3ff3-ad93-d3cdb2b9eb30 | -14.3348 | -47.6981 | 2025-10-05 00:50:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 9c869d91-36d2-3535-8e55-b3d22c3931c1 | -14.9157 | -46.8541 | 2025-10-05 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 27d5c97d-906e-354f-a06a-e3fa6ee44cf5 | -10.8379 | -57.1781 | 2025-10-05 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 59b272f1-9ea5-386e-b429-6443c2a34c10 | -13.1161 | -43.847 | 2025-10-05 00:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| f6e5fe0c-6c53-391d-8800-c0d7a1a048bc | -5.6361 | -43.9258 | 2025-10-05 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 6a4fa0cf-abb0-39a6-9ffe-bc49c4ac5abe | -4.4445 | -43.2397 | 2025-10-05 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| db8d765d-f2ec-3ee9-97ff-67f2f0267464 | -11.8588 | -56.8785 | 2025-10-05 00:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| bb37dbc4-90cd-3ba5-9c67-af8c054568a9 | -5.4907 | -43.4264 | 2025-10-05 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 163c53de-10e3-3637-bfcc-581813402b0a | -14.6711 | -48.3381 | 2025-10-05 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 4c207b90-13d7-3dbd-9f6e-2be5c458a4d9 | -14.3158 | -47.6787 | 2025-10-05 00:50:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 171b0e97-f7be-3951-994d-fb0c6f215f66 | -23.003 | -52.7309 | 2025-10-05 00:50:00 | GOES-19 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 221.5 |
| a103a009-acb6-385e-b9fa-5257b77eabcc | -11.823 | -45.0596 | 2025-10-05 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 47d3dd42-b727-3a2f-bac1-6ed1829308a3 | -11.8775 | -56.8969 | 2025-10-05 01:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 25700ab9-90db-3dc0-b130-05ac77298784 | -11.7712 | -44.7432 | 2025-10-05 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 0ecb14a8-04f6-326d-b558-9ea1ee51e02e | -4.3197 | -48.0908 | 2025-10-05 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b5141c55-9a58-39ce-ac8f-13e0a2a93547 | -3.6196 | -51.0461 | 2025-10-05 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 26dfae97-5c97-3e7c-9e1a-eec990ed7d3c | -14.3158 | -47.6787 | 2025-10-05 01:00:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c8f5a08b-2cec-30b1-a01e-41c6e7b10d05 | -7.7301 | -46.3185 | 2025-10-05 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 7cde5863-8616-3e70-a696-d27493efe8c5 | -14.9352 | -46.8507 | 2025-10-05 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 43ae3fec-c624-3fc1-bc0c-ecf8b7b2a1ba | -14.3348 | -47.6981 | 2025-10-05 01:00:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 8f713503-67a7-3693-89ad-2821f4de4315 | -19.5233 | -50.373 | 2025-10-05 01:00:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 52.2 |
| edde5d59-628a-35e3-9396-382e3fea8a1e | -11.823 | -45.0596 | 2025-10-05 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 1fa7fade-2b0c-33a3-8c00-7fe92a4c820e | -4.6505 | -43.1805 | 2025-10-05 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 178.8 |
| cf0a3e2c-1d3d-3573-af45-a349e003da39 | -4.6504 | -43.2038 | 2025-10-05 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a7bcc80b-4ca0-3948-bbe4-40469aadc6c9 | -11.8777 | -56.8769 | 2025-10-05 01:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 45128155-8ef2-3476-a225-5404655bd167 | -13.1161 | -43.847 | 2025-10-05 01:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d8a053bd-c8ae-3a28-bf9e-c305d29464c1 | -14.9157 | -46.8541 | 2025-10-05 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 9f288381-2483-3a2b-aecb-adea6d5a295e | -5.6363 | -43.9027 | 2025-10-05 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| d97b341b-170e-376a-a771-6429dcc2c6e5 | -10.6382 | -46.317 | 2025-10-05 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 2d352b91-c163-31e8-8d9f-ba9d4f73ff95 | -5.6361 | -43.9258 | 2025-10-05 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 21cd40c3-91aa-355c-ac86-9ccb0f6b7d57 | -6.3946 | -43.0505 | 2025-10-05 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 0facb859-4a75-3275-bc53-706c41bcca5a | -15.9084 | -48.8254 | 2025-10-05 01:00:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 2e7cebe8-3c14-33d1-9e5d-59313b99d19f | -5.655 | -43.9013 | 2025-10-05 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 94133d3d-7807-3d9c-a9bb-83a8e0f16539 | -11.8418 | -45.0799 | 2025-10-05 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d3c97f17-1fd7-3a28-bdd9-1efe2484482d | -6.4131 | -43.0724 | 2025-10-05 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| edb9f2f6-d095-3c48-bf4a-35724d66fc3a | -6.4134 | -43.0489 | 2025-10-05 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 705591a3-a90c-3236-8ada-0d3a093c22ac | -4.6318 | -43.1816 | 2025-10-05 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 217.3 |
| ee57cf22-1546-3013-917b-eb6c0170875d | -19.503 | -50.377 | 2025-10-05 01:00:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 26dcda59-b696-3932-b1bc-69e39cdd7de4 | -6.3943 | -43.074 | 2025-10-05 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 3459787c-11a4-33e0-bd07-de7152c7272f | -5.4909 | -43.4032 | 2025-10-05 01:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| a5d44e7c-388c-3f97-86c6-59c87c0fa7a6 | -11.8225 | -45.0827 | 2025-10-05 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 57762bf2-1d69-36aa-adba-6129c857e1d1 | -3.6013 | -51.0259 | 2025-10-05 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| aaa1c657-98fc-3a9f-b28e-2d2c264e6363 | -15.928 | -48.822 | 2025-10-05 01:00:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 414d5542-0114-31cb-81c2-3e55ae337e56 | -4.6317 | -43.205 | 2025-10-05 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 15c6af8a-b803-3fd1-b445-748bc492ef81 | -14.3353 | -47.6755 | 2025-10-05 01:00:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 185.8 |
| cb3b3747-6f5c-3767-85f5-14168bd6fade | -4.4445 | -43.2397 | 2025-10-05 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 071b58e0-a163-3238-a26a-5c6cc7292aae | -12.4669 | -45.5155 | 2025-10-05 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b24135f8-a6be-3959-a8be-ee3a0d5b4842 | -10.8379 | -57.1781 | 2025-10-05 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a76ba918-7e29-30fc-908c-0ffecfa17868 | -10.6572 | -46.3146 | 2025-10-05 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5e7e32e8-b7d2-3f32-ace3-a0d260e80486 | -4.7268 | -42.9886 | 2025-10-05 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 6b31e35e-ef89-3703-9477-e1d4d85d1a85 | -5.6548 | -43.9244 | 2025-10-05 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 9689d965-929c-3549-9cc4-ea7054a306ec | -3.6012 | -51.0467 | 2025-10-05 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 26a3163d-9306-36f6-9734-d6e9e01efc2c | -4.4445 | -43.2397 | 2025-10-05 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| a5b76596-c85e-3852-b9b8-0865fb5487de | -2.6883 | -48.3899 | 2025-10-05 01:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 8e38a7e3-5495-318d-97e5-0dfccdd86f3c | -4.6317 | -43.205 | 2025-10-05 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9d073f1d-a4f6-3c46-a35a-76157fc2ebd6 | -5.6361 | -43.9258 | 2025-10-05 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 65916476-e780-3562-bc73-5d5f6274b19e | -13.3517 | -47.5818 | 2025-10-05 01:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 0a2ff462-8422-3a73-8c43-65fa47023262 | -15.928 | -48.822 | 2025-10-05 01:10:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| ce832b76-9f83-3548-b9f7-1b30b5255318 | -3.6196 | -51.0461 | 2025-10-05 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 431a018c-5957-3139-99b7-05a6e8136f1c | -13.14 | -50.8954 | 2025-10-05 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 0bc0962a-dd0d-3782-8d31-5eba5f326b28 | -13.1585 | -50.9359 | 2025-10-05 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 159.0 |
| e5496521-151e-3a00-a228-f59084b8b8bc | -3.6012 | -51.0467 | 2025-10-05 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 8b067909-1160-3399-a3ca-e669896dbd68 | -15.3014 | -47.9654 | 2025-10-05 01:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 09e834da-01dc-3471-9d92-738bb57758ec | -4.6504 | -43.2038 | 2025-10-05 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 27ad1f16-8474-392a-ba72-1c7fee3591de | -15.3019 | -47.9428 | 2025-10-05 01:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f47df59e-cc18-3777-9fe4-77d772ce2cf7 | -4.6318 | -43.1816 | 2025-10-05 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 84f13173-3180-308f-bcc5-24db7f16fc1c | -4.6505 | -43.1805 | 2025-10-05 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 229.4 |
| 1d3d09a4-445b-3713-85e0-795a55ea5c49 | -6.4131 | -43.0724 | 2025-10-05 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 474dd0a3-fcb0-348d-ada3-3f7bd0786225 | -8.5384 | -46.3304 | 2025-10-05 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 85224d77-2ff9-3747-8f0c-19b3395f8b2b | -8.5387 | -46.3079 | 2025-10-05 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 17827cf6-1db2-3c2d-83c2-16f5b477a845 | -14.9157 | -46.8541 | 2025-10-05 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 121b115f-fc42-3f2e-8d12-bd5877b0ea76 | -5.655 | -43.9013 | 2025-10-05 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 385a5371-7f67-33e6-9941-a4b91dd96da9 | -13.1161 | -43.847 | 2025-10-05 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5b72228d-00d1-3406-a320-4a3bfc9262f1 | -11.8225 | -45.0827 | 2025-10-05 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ba90b50e-4b7c-3451-9919-433241249b44 | -13.7291 | -51.2479 | 2025-10-05 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 2e4b21a5-c2f2-354d-9bcf-d4a7f569be7c | -13.1592 | -50.8929 | 2025-10-05 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 457af03f-8e04-3e15-af7c-9018f97611ec | -4.7268 | -42.9886 | 2025-10-05 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| d160123d-c3bf-3fe8-b491-591e41c02548 | -5.6548 | -43.9244 | 2025-10-05 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c229d82c-9897-3275-9fd0-e9eb5e3c9bde | -15.9084 | -48.8254 | 2025-10-05 01:10:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ad6d01a7-2b3a-30b1-bc0b-98521f359184 | -3.6197 | -51.0253 | 2025-10-05 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 9faeecaa-87bb-31e4-9eef-2c04ac43abbd | -13.1589 | -50.9144 | 2025-10-05 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 228.6 |
| aca1fb13-38b6-3b33-a265-9718480be285 | -11.8777 | -56.8769 | 2025-10-05 01:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |


[Clique aqui para ver as próximas entradas](README15.md)
