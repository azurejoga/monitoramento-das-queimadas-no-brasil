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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb881ff0-750f-3c81-a132-2d67931ea31e | -13.23061 | -48.56604 | 2025-10-29 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 313fadca-b9be-30a8-91a6-0b4384bd6f8a | -13.63935 | -46.51353 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0484f4bf-e807-3b12-9a43-fc4d2c26b8f8 | -13.81876 | -41.69384 | 2025-10-29 04:46:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 848902d6-4355-334c-9225-a7786c012445 | -13.04421 | -43.8238 | 2025-10-29 04:46:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf730cf8-c5e1-3725-ba12-76c868865cb3 | -13.37318 | -46.63155 | 2025-10-29 04:46:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 330c11e3-f85d-386b-ab50-910890c28a3c | -10.66505 | -44.80558 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fab528b-0103-3ca7-936d-3fd67d998af3 | -16.11506 | -45.7524 | 2025-10-29 04:46:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a2f0c34-1948-3556-bced-a2464eaed91e | -10.42507 | -44.99438 | 2025-10-29 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| c4ff7a1d-6e2e-3762-a084-81caa2b5d3fc | -15.45888 | -47.6885 | 2025-10-29 04:46:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b237766f-45f9-31b5-881b-a00d0b2dadf5 | -12.55617 | -44.96608 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 511a8f43-582f-3878-9da6-0398eea0f4eb | -13.2057 | -47.06842 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 187add3d-6ef1-3cee-8988-084370630303 | -10.56649 | -49.84265 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 80dc96ba-e9da-3460-a37a-1784fbc7f3a6 | -14.32198 | -46.51327 | 2025-10-29 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09f1387c-7870-3829-82d1-4a9c0d23615e | -13.04932 | -43.82445 | 2025-10-29 04:46:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abf34592-794a-324b-8f66-1ba483b9d6e9 | -13.63876 | -47.02294 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d304658a-97d1-3848-a59a-d394805b43f9 | -13.38236 | -47.41051 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f40e55bb-20f7-3d0e-aa7c-2e85e2732547 | -13.52625 | -47.33104 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0104c677-e3bd-39aa-ae22-ac376f216c9b | -10.84375 | -49.13639 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b153d00-f260-3360-8a72-aa66beafab7e | -13.29922 | -47.9192 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8cbd6a0c-8603-3c13-ae9c-92f1edcd8a9b | -13.02141 | -48.76854 | 2025-10-29 04:46:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5e5ea181-7131-38c5-b26a-e5ee8414ded6 | -10.97734 | -50.24826 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed2b9fb2-0f75-3c57-b627-d7ec447e7c6d | -13.85175 | -48.51553 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e15d884-99b0-35c8-9dc0-a79bcc890d06 | -13.58114 | -49.59959 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d81309bb-d7cb-3fb4-afaf-0211cbb75927 | -13.56979 | -47.16017 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a15d2d72-bd2b-3473-8cf5-d52a7345abb9 | -10.8521 | -47.89264 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d32df10-8046-3c0c-bc9e-60108de46d5c | -13.9473 | -48.46681 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eead5a07-c7f2-31b9-ae16-effa802a7c76 | -13.54933 | -47.13522 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ceb4e8b9-484d-3643-8ea0-73583352803a | -11.26357 | -45.52551 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 653d1490-7705-3748-9a98-de441314905b | -13.62287 | -46.47376 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5dd13265-34df-3887-ac1a-c68da1dd5518 | -11.58294 | -47.9407 | 2025-10-29 04:46:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82fc22b5-9dd7-3bff-9383-cc74b49da14c | -10.98846 | -47.72787 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 814761dc-c5cf-3192-9b8c-55d145d5827f | -12.70952 | -46.31047 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 026d89e6-5a20-30c1-b9f0-481eec305756 | -13.24285 | -44.11309 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7667919-cdde-3635-ac76-0b12991a7a6c | -13.5452 | -47.13475 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26c70ce5-b174-36b7-a7d0-cd1f9d6b9002 | -11.97439 | -44.03384 | 2025-10-29 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f34db790-8c0f-367b-9e94-936b4467d36a | -10.76804 | -44.74222 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36d72aad-6f81-3a38-b33b-afcbd258645d | -10.45233 | -44.4882 | 2025-10-29 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a84e913-516d-3971-880f-88b033df6a5d | -13.54038 | -47.34923 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65fc7386-fcba-3756-aea5-c776dc471a65 | -9.73434 | -44.06433 | 2025-10-29 04:46:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6b6fef1e-9ba9-3ef1-91fe-d6083a6c3495 | -13.63021 | -46.51642 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a150ced2-e0de-33d4-a010-9e6f451fbe46 | -10.33415 | -47.78923 | 2025-10-29 04:46:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54fc5e1f-9187-36ba-88b7-3d1326c9fe75 | -15.10089 | -43.83851 | 2025-10-29 04:46:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f90a8a54-91cb-3662-8864-143e69953185 | -10.5224 | -47.74283 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe291a58-055f-3b4b-af2c-788b1b6a7c14 | -13.22619 | -47.07183 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f6104b2-10ca-352b-805e-c13766d991bd | -8.10721 | -55.08866 | 2025-10-29 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 046457f5-6fd0-3432-9c32-3c2d83d5a682 | -10.38128 | -47.11383 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 162068db-9e0a-3107-88cc-45f83da48a38 | -12.29295 | -47.01025 | 2025-10-29 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 729d03ad-db91-392c-a901-3cf2b68fff63 | -13.63313 | -46.46274 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0da0b54-8a4b-3b7d-a564-3f378973e0b4 | -14.60416 | -48.42971 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8a2419d-4c65-3ee3-a9f6-326db76e188a | -14.6636 | -48.39796 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0c28754-b09e-3bc4-8379-90461324f39d | -14.61714 | -48.42098 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f22f7a2-5406-37d8-a92f-02ebe9748184 | -12.58195 | -43.36883 | 2025-10-29 04:46:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f07d117-69d1-3836-8fba-061498a43f70 | -9.80227 | -47.75473 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 012761b5-4b73-3f0f-a785-6c315abb66af | -13.35483 | -47.66594 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4fc3993-2c2f-35c1-abdb-c9bf31f54b7c | -12.1894 | -46.71379 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| eb98c0e1-4e6b-39b0-bae7-43e47d823f27 | -14.23649 | -48.10882 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f19547b-af98-3dba-ba7a-f0c214b6d475 | -14.31418 | -48.00742 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3e4ecc84-bb9f-39dc-8f99-c2d060c25c1a | -11.26977 | -47.53472 | 2025-10-29 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26abbd7e-560f-30ed-9c88-565e811e3394 | -13.65757 | -48.44252 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e12b22e-8909-3164-a3c3-00462c850125 | -11.33722 | -54.38729 | 2025-10-29 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| caed573c-40df-33f3-b9dc-560d20fcdbb4 | -12.52738 | -47.55153 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dfae55b-8de4-3c35-95fe-a131e64a7c56 | -12.08433 | -47.99699 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23a53fc6-434e-3378-b4ce-dfae69615927 | -13.70399 | -47.67532 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a577c3af-8612-32df-81a5-08608ec95868 | -12.74956 | -45.16933 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a3e1051-53ca-39ed-a399-ad0076329f54 | -14.52012 | -47.99637 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e806c034-83dc-3a50-b5e5-98dce3d2c646 | -14.23123 | -48.11805 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad743284-0a82-3fa1-aa0a-c85c05515ef3 | -10.85314 | -50.0964 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 482f8159-6028-3096-80c3-ac6e84941535 | -11.99715 | -46.77726 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b2f85828-4290-3a94-ac74-65dcaf5845bb | -14.27436 | -47.31808 | 2025-10-29 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3d84a3b-9bfa-33cf-8395-609d87051294 | -13.5567 | -49.56675 | 2025-10-29 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25a2bb49-8d9e-3bba-8fb7-af0c876a45e5 | -9.01843 | -63.5769 | 2025-10-29 04:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 324298c6-27c0-309f-95b0-add3fc84294b | -12.52961 | -47.53595 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc3dfec6-734f-3c5d-b144-22f7e33ead24 | -10.65441 | -48.00583 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 31d17885-6857-3e33-a533-d922f6dc4d87 | -12.97795 | -48.39024 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee3c3543-80ab-3c0b-8e29-9a5aabd2f2e0 | -10.42961 | -44.995 | 2025-10-29 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ebd5af6-d70d-3ac4-b3cc-b0d83be9190d | -14.67999 | -46.34205 | 2025-10-29 04:46:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7810797-0ec4-342c-8fcd-0a787b6220c8 | -13.37841 | -47.40942 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae8457f3-fbe5-3a0c-93f9-8b0ce8fd2d64 | -13.27739 | -48.56706 | 2025-10-29 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49a7bedd-ac44-33df-8ba2-f4a50a7532c9 | -10.51929 | -47.7375 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2a84343-fe2b-3aeb-866d-e64d7c45deaa | -9.09251 | -47.82189 | 2025-10-29 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 689bf01c-04d3-3799-9947-d22012eb51aa | -12.64259 | -46.7191 | 2025-10-29 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e71377a4-e953-3db5-ae8c-103f3af61376 | -14.82952 | -47.40408 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1c5a5d7-aeda-3375-9025-80fa17c74ed2 | -15.15654 | -47.23199 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0f6903e-8b3a-3e58-8255-47cd067deaa0 | -12.01363 | -46.77963 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1ae5ec24-e130-3deb-8999-5bef0b336635 | -13.63823 | -46.52171 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 402256a4-5076-3438-8b8f-fcbe2ab0874a | -13.9308 | -48.44562 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e80edc4d-1bb1-39d1-8fce-e9d4e349f857 | -13.54313 | -49.58494 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c17071b-6004-356a-aa7c-91688a4bc580 | -11.37129 | -47.01517 | 2025-10-29 04:46:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ad94900-e64c-3896-ac98-3a797e2c4ec6 | -13.87226 | -48.47993 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 790457e3-6f1c-31e4-ba93-3ce2748c370f | -15.09602 | -43.83456 | 2025-10-29 04:46:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4276d0cb-27ec-368b-a429-59c3f55bbe5b | -9.22751 | -46.35355 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 389bd394-d790-3f84-97a4-d2d3c3ccaf09 | -11.34286 | -54.39627 | 2025-10-29 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 26c84fe2-b9d6-312c-959c-a589ae3333a8 | -10.6469 | -48.00486 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 93678bbd-2905-3346-b3bf-c0c72a7570f8 | -11.8512 | -47.9242 | 2025-10-29 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 325be53b-07d2-3f0c-a051-2f1a5a89cf52 | -13.22212 | -47.07091 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5236e4d2-7943-3225-8171-8244a9fdf33f | -12.10601 | -44.59827 | 2025-10-29 04:46:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0218b48-4d53-35c7-b35c-824a45aa3f30 | -10.65392 | -47.90182 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e3c91ef2-5121-343e-ad06-3ac9e05dcf33 | -14.42072 | -47.84818 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 259120ee-25b5-3b69-863e-c5a38def34a9 | -9.80602 | -47.75533 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5712e57-6ca4-3244-8047-d3baee7d7106 | -12.29393 | -47.00301 | 2025-10-29 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README68.md)
