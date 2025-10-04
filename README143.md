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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5961fe8d-9605-3b8a-afff-5376b9dcc0d6 | -9.32963 | -45.75355 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 96cd69c8-6ad1-3b48-895c-ce1946efb06f | -14.2214 | -46.05992 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 139.2 |
| c408bc8f-336f-34c9-b166-f4ff7111e29c | -13.98207 | -45.08704 | 2025-10-04 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2984954d-7990-3234-9cd9-03e032191a22 | -10.33497 | -50.34056 | 2025-10-04 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2ee2843c-64da-371d-81e2-f4cc45d4aeed | -11.1035 | -47.7527 | 2025-10-04 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 30350cdb-9d46-3fff-881e-297ff8b4444c | -13.74419 | -51.30448 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |
| cd1c47a6-343f-3dec-9362-9e740b7f7406 | -10.7695 | -46.59491 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f6ab5c91-beca-3b76-a164-7b63784a086a | -15.61988 | -49.10891 | 2025-10-04 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0b16236f-bb07-3629-9d2f-2c2a8a2e238e | -11.91077 | -46.25795 | 2025-10-04 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d78f3b52-127c-30ea-9e93-02374b39a805 | -11.51423 | -45.01321 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ad166111-73f1-3e13-a3bf-b45064c37477 | -9.82021 | -46.13429 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0bfa0a62-c908-3120-b2d6-51e8f4d79225 | -9.26388 | -45.768 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 572f516a-a6ca-3449-a43a-f8b4bf842bbb | -14.656 | -48.24031 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| ee4207ec-0ffb-3402-9787-5966e775a2ad | -12.71218 | -48.56163 | 2025-10-04 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 00ec603f-fb5a-3afd-bddf-3fb50c76b002 | -13.92759 | -48.17775 | 2025-10-04 12:19:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b81e995a-41ad-31c6-982d-a85cc26ab895 | -10.92401 | -48.92959 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 82ecd8bd-b023-3ae6-9d24-435fe0a36ba5 | -11.85871 | -44.9503 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 80cfdbfe-76cf-35e5-822a-a0d0412cecf3 | -13.45785 | -47.26294 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8c11762a-dfbd-3436-aceb-d2f2bfad2d0b | -14.22296 | -46.07721 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 2851a8d5-1c6d-3db7-af97-77fa74061778 | -14.41181 | -52.88311 | 2025-10-04 12:19:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 9240f150-198e-30e3-84ba-87871d2ede9a | -15.21497 | -48.65479 | 2025-10-04 12:19:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d3bfb932-8d40-3f57-89d0-2d8cafb7ba35 | -11.56387 | -47.6937 | 2025-10-04 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| cbe895cf-1cd5-3378-b720-5411730bff2d | -11.93012 | -49.91934 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4397506f-e7dd-3b0e-8865-ccf66e1c1f08 | -15.12677 | -45.70728 | 2025-10-04 12:19:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| cc98c70d-4f23-3201-8b75-1f28682d69f3 | -12.53716 | -45.98845 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 482972f6-cb15-3654-930a-4130f9a4cbba | -13.15146 | -47.94165 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| e5531b72-81b1-3003-ab38-da870fd6b4a3 | -14.91909 | -46.87763 | 2025-10-04 12:19:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 30e2f7b3-893c-36b1-a933-909afd0082d8 | -11.51779 | -46.77752 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ffce9c8a-d4f5-3e46-9434-76f6823f026d | -11.16604 | -45.78258 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0175a805-00bd-3c76-8f1e-70d9a1e48847 | -10.64358 | -49.14237 | 2025-10-04 12:19:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e9a487e2-f7db-3dcb-8b82-e8a7b882deae | -9.28681 | -45.67103 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 60cfdfd3-f709-30e5-a452-6c9de6bc2282 | -13.32642 | -48.07151 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| aeaba982-31aa-3513-b401-d6bff5277715 | -13.13876 | -47.96744 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6d95ab89-c9aa-3a9d-872a-ae44f9dae75d | -8.91744 | -46.59924 | 2025-10-04 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5ff541c7-3527-389f-a0a7-61cc826868c5 | -9.88674 | -47.8163 | 2025-10-04 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eacdd955-4a52-3dfa-a65b-8c61104b68c3 | -14.41393 | -52.86975 | 2025-10-04 12:19:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b7464438-6871-3df3-919d-20e7622a93e3 | -12.78567 | -47.71848 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9095d665-77c9-3f4f-a679-caf2a0d4847d | -8.94936 | -46.63147 | 2025-10-04 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ad2e15b-cc29-31b8-89e5-134f8a481dd5 | -9.98735 | -48.27121 | 2025-10-04 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c7b4a12e-d651-3678-84f7-8891d5d3d757 | -14.86188 | -48.35461 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8e9adfbb-f163-3adc-b718-e2191df169dd | -13.10256 | -47.89145 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 69205e34-18ab-393c-87e3-854aa4d153a0 | -13.09368 | -47.8902 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 77eca4af-302b-3048-8c77-f2b69b55f81c | -15.95352 | -43.3242 | 2025-10-04 12:19:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 57fc56c2-e15d-335d-a456-b7eb10820f1e | -18.30871 | -47.44263 | 2025-10-04 12:19:00 | TERRA_M-T | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 3374d17f-85d5-3d09-8fd3-d586b50584b3 | -12.23532 | -47.83983 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d955e037-bb52-375d-be70-6cf4b6318327 | -14.75332 | -48.13925 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 97c4d07e-a2d2-3683-b30f-33e9d7b3d4e2 | -9.14409 | -47.78741 | 2025-10-04 12:19:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 79089a03-af35-33b2-b9b5-6463e31a148a | -14.58292 | -52.50169 | 2025-10-04 12:19:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 29.8 |
| b11720fd-d411-33fe-8820-b1e91b423a41 | -11.86717 | -44.96305 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 50b0ba3e-364e-352f-b2f4-3f167dec7c6b | -11.57658 | -47.66793 | 2025-10-04 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 96072a43-ac26-3eb1-8efb-551d1302bb93 | -12.5424 | -46.02084 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6aca6e9e-ad1c-313f-8e31-d1f32dfcd50b | -13.3894 | -47.55841 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e219b806-2db2-3ff9-9391-991dbae8e318 | -13.11031 | -47.83663 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| f786c3d3-4f50-388b-9901-8719298af958 | -14.32063 | -52.90934 | 2025-10-04 12:19:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0c227098-a6ba-3c54-9017-3144075f9ebe | -13.11127 | -47.95757 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5d29db1b-2117-3c7a-bbcc-1721e74d9b2b | -11.82268 | -48.07045 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| f012f91a-e371-3024-84de-52e40225b02a | -14.31456 | -52.91539 | 2025-10-04 12:19:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| c1a6b88f-dc79-3e40-9a99-5a1ead0bdaff | -9.11306 | -46.71303 | 2025-10-04 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| be36ff60-6bfb-3787-95eb-9ee2a9ae70da | -11.7984 | -45.02369 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 568b74a3-3754-3a04-8816-5e312ebf399b | -18.00366 | -49.83855 | 2025-10-04 12:19:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 36d8dcf4-13e8-3ee9-83cb-edcb1e57a2f9 | -12.93257 | -50.98751 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 066fe14e-6d94-33e1-85fb-afde6a9a1682 | -14.04907 | -49.13055 | 2025-10-04 12:19:00 | TERRA_M-T | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3d3d8d50-70fb-3832-8fdb-ad483e6e0c29 | -16.96632 | -48.39017 | 2025-10-04 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 74b91123-71ef-3b1e-bf36-a91d24410c77 | -12.88359 | -47.28773 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6c319549-b168-33b4-a335-813d28a65d7a | -10.19422 | -45.4872 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ddff1392-cc00-3c60-9026-8683fd3eb6f9 | -9.68397 | -45.71622 | 2025-10-04 12:19:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 4e14f13d-0d72-32fa-ad8c-8c0a13387b97 | -12.82302 | -46.86273 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 7ad55f8a-241b-3c31-8fcf-5a6edd59ef11 | -12.38155 | -42.53605 | 2025-10-04 12:19:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 31.3 |
| c4b08245-c6b9-3df1-9c4f-7f98b24a1311 | -13.23919 | -47.83358 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4c5c41d3-37a8-308d-85e9-a4934c5436c4 | -13.29174 | -47.85691 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| e902bc18-03dd-34a8-b667-94cd0cca3113 | -11.11363 | -47.745 | 2025-10-04 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c2ec9a2d-5376-385b-97da-40e416ebca43 | -10.5699 | -48.70363 | 2025-10-04 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| b9da89be-b213-307a-a4da-664a503b130e | -13.57935 | -48.17336 | 2025-10-04 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| dbe7b0a4-daae-3264-8db8-44e8e26b48b9 | -14.21041 | -46.06899 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 7a0f0fbc-1cc7-3667-90b9-06a9d64c234e | -15.20273 | -46.38765 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1d0a6d34-10b4-33e0-a1ea-c422c4d2a7bc | -15.52867 | -46.85103 | 2025-10-04 12:19:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 36de3adc-51ea-39c9-9bb7-9a1d2dec3bdf | -17.70251 | -47.08879 | 2025-10-04 12:19:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3ba02ba1-85e5-322f-ba59-721b97f3e89d | -9.33246 | -45.66409 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 4ea47249-70bc-3761-a2f4-cc8d726327fc | -11.24453 | -47.80369 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b873593f-4032-33de-88e7-5cd1b1a6e25f | -17.98865 | -49.81727 | 2025-10-04 12:19:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 307.0 |
| 1362ff1d-9d59-3090-8312-76049fcf412c | -13.17959 | -50.99118 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f5502e6f-bc78-319b-a2a8-e577269c6abd | -9.99621 | -48.27246 | 2025-10-04 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 373732f0-adc9-3d8d-b6ec-b5ba328cba23 | -13.17036 | -50.92509 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 99624a68-886b-3cb3-9758-b687cc70b06e | -12.70464 | -48.55137 | 2025-10-04 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c59076ca-a3b1-362a-9684-37d9b3b38cf2 | -9.69463 | -45.70757 | 2025-10-04 12:19:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 917b9768-1792-36a7-bbc8-47de3a15bf17 | -14.31669 | -52.90199 | 2025-10-04 12:19:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| a2ce3b8d-e409-332d-bc2a-a783e492c61b | -13.25566 | -47.26032 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 18e4bbec-0e2b-3199-ba6f-cb0b2f6f6a73 | -11.88534 | -44.98318 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 4bb20d76-7135-3599-93ca-f2026c63c575 | -13.30063 | -47.85819 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 5f96cd7f-2579-3b4c-8404-c909de51a24e | -13.26277 | -43.66991 | 2025-10-04 12:19:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| e32023e1-c914-33c6-bd94-82ea399b9e1b | -9.46124 | -45.53492 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 591b151d-e927-3016-a993-885101cfcdb5 | -12.09296 | -45.18621 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 4249a159-9540-34b1-b7d0-30d80716e50d | -11.82177 | -50.08669 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| eb14a40f-4a87-3195-a7b6-a6260496a166 | -13.11533 | -47.86519 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a674fcea-bcb2-3211-9730-40354cae9911 | -12.95005 | -51.00114 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 6cc93268-dad3-3e0e-b03b-5c5afb3bc6fc | -11.07545 | -47.88565 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 77110f88-130d-3dee-b80d-2ff2e87b7585 | -15.23918 | -49.31557 | 2025-10-04 12:19:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 496bea44-58fb-337a-9f17-61f67bef58bc | -12.86271 | -47.03932 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2ee2908a-22bc-3456-afa7-ba84e02e6f1b | -11.57437 | -47.42772 | 2025-10-04 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1dbff033-4654-3122-9b22-a52b08a93e00 | -9.97018 | -45.64146 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README144.md)
