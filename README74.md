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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6efe942b-cbe8-32b2-aa31-f035549b5ac5 | -10.98298 | -46.50376 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| b7012626-1d4d-320a-8a42-212fc83756a9 | -10.98264 | -46.44404 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b1e6eef7-22f7-3c36-a7f7-e66c8c706971 | -10.98152 | -46.51339 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 39d843ba-835b-3dc6-bc30-8bb507ffa1b8 | -10.98114 | -46.45396 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fb2061f3-6463-308a-a6d6-7187e2eef30d | -10.98007 | -46.52299 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9d2c9563-106f-320d-9932-3a1ca797b84e | -10.9709 | -46.40644 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2c3c5eb5-ac68-3a8d-bfb2-d11404fb8203 | -10.96947 | -46.41611 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| d2f67b47-7ada-3d45-bf20-630830a6a048 | -10.96176 | -46.40508 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 7beb0e0b-9da1-35ca-80b6-830896a911c8 | -10.95547 | -46.38459 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 188031bb-71af-397a-8a64-c241c04713eb | -10.95405 | -46.39414 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 7d6eb522-f0c3-3284-b348-fd54f7c841e6 | -13.53399 | -47.57296 | 2024-09-30 12:34:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d6a9ab09-d130-3a3e-ab85-048f1b087a32 | -13.53242 | -47.58326 | 2024-09-30 12:34:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a04cd8d5-2364-3623-95fe-52232bd0144c | -13.52461 | -47.57156 | 2024-09-30 12:34:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7074ea79-61c9-3701-9367-5f244c08e755 | -12.81414 | -47.45415 | 2024-09-30 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0a583dfb-f2f2-3dd1-9d95-f05ad452bb23 | -12.80474 | -47.45265 | 2024-09-30 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d093a214-8ea3-3f7d-8b6e-a780ab8a727a | -12.53057 | -47.97068 | 2024-09-30 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7e1f4e81-7285-3319-94b5-c401a842b9fe | -12.52086 | -47.96914 | 2024-09-30 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e87ac6d6-eacd-31a0-a28c-bc530598cb8e | -12.48672 | -46.44189 | 2024-09-30 12:34:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e3fb9944-a1a0-3d12-b707-ab18b6476fd2 | -12.47767 | -46.44054 | 2024-09-30 12:34:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 32b11d2f-b0f8-325e-87d3-5e99c5473a6f | -12.47625 | -46.45004 | 2024-09-30 12:34:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8365e075-b3dc-357b-8151-f7e4ab50be43 | -14.26167 | -47.09366 | 2024-09-30 12:34:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5b1c264b-65fc-3e8d-a761-867d565cb177 | -14.25254 | -47.09225 | 2024-09-30 12:34:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d1dfdb51-584a-3d43-80a9-64da722b0cea | -15.65419 | -47.21408 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 516aee7d-d6f1-3106-aa5a-64ca44c47e26 | -15.37137 | -47.43774 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a9cc2c88-6416-3aa3-800a-7eb893d8750e | -15.32236 | -47.5237 | 2024-09-30 12:34:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0aa852ee-5da7-378d-9958-fd2f060b42fe | -15.23974 | -47.57125 | 2024-09-30 12:34:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ac145056-4ed0-3502-a1df-26db239733ea | -16.82631 | -47.6999 | 2024-09-30 12:34:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 64f8e445-e678-3145-8064-df47b780b21e | -16.82482 | -47.7097 | 2024-09-30 12:34:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 32817e63-7406-358f-93b9-3ca9e195af73 | -18.87755 | -49.16065 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 280.7 |
| 70a335d6-5b43-3f1a-bc01-ff08701605ea | -18.87582 | -49.17148 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 824.9 |
| f90815c4-b7da-3f3b-9e4f-717517ed8195 | -18.8741 | -49.18225 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 548d9c87-b852-3932-8260-29be922e9e79 | -18.86977 | -49.14803 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 42f7b977-251c-3a8e-b4df-12f812a3a439 | -18.86802 | -49.15895 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 552.2 |
| 31ef6a50-5dfb-32f0-8b79-aee862fcfc4a | -18.86628 | -49.16978 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8a5c68fc-c043-39bb-96b9-1e2c533dd327 | -18.86025 | -49.14627 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 4df6feab-b6a0-3989-b547-74edd0258807 | -18.85849 | -49.15718 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 9ee10206-08f4-3960-9d12-c3d4eb895c33 | -18.85729 | -49.13925 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f329960b-5e68-3c2b-bb7f-33e73b851434 | -18.85559 | -49.1501 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 126.4 |
| e4a80131-27dc-3950-a992-c8a0b2cbab1d | -18.88881 | -49.15149 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| f4aaa5e6-933a-3888-b4c5-8546efca27f7 | -18.88709 | -49.16231 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 156.8 |
| 6af20be6-e0a9-3410-89a5-3f2f36708040 | -18.88538 | -49.17305 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 157.6 |
| f47e6a4d-4538-3c8d-8a9e-e0256902259d | -18.88364 | -49.18396 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| fc487de8-1187-313a-a468-28646611e5c9 | -18.87929 | -49.14977 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.2 |
| 17a6f9fc-5505-3b93-a266-8d3ca276a565 | -18.90085 | -48.19455 | 2024-09-30 12:34:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c9498ffe-ed06-3c88-94f7-63ab4b2406b0 | -10.75886 | -48.74986 | 2024-09-30 12:34:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ef0239ad-20b7-3b32-8ae2-008df0412c05 | -10.75674 | -48.76334 | 2024-09-30 12:34:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 519fd1c2-8348-3c4c-84ae-1ac0bfd95bab | -15.35843 | -51.43077 | 2024-09-30 12:34:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cf0daf5a-414e-3d47-93bd-53f547d703d3 | -10.74624 | -48.76167 | 2024-09-30 12:34:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 36a19dd2-9da7-37a0-b56d-617f81ca555b | -10.83608 | -48.12265 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 5b95c583-6b6d-3598-beea-5983aeeb5bf2 | -10.82423 | -48.13263 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| efc5c242-4e16-35c4-85be-281f32673e45 | -10.73357 | -47.99187 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f5ce3c58-9605-3701-a0cd-edeaa3628c33 | -10.71421 | -47.98275 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 43c6d943-332f-3a40-bcc2-3915303e5d0d | -10.5726 | -48.03745 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f8168b39-3d0c-3db2-9c00-92ab8aebf335 | -10.57069 | -48.04969 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e81d5981-6851-3679-90d2-ecc573cf10fe | -10.56251 | -48.03636 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ac94d6af-b7ce-3bab-ab29-09420824c990 | -10.56058 | -48.04865 | 2024-09-30 12:34:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| fa1dc0fc-8345-3735-b6af-e1d8f87f0070 | -10.45394 | -48.20676 | 2024-09-30 12:34:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| df3fc79f-7b8e-382c-b982-2bbe47ddec03 | -10.45203 | -48.21896 | 2024-09-30 12:34:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| fff06354-5aa3-3de2-83f4-235ddfda396d | -10.45012 | -48.23117 | 2024-09-30 12:34:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b416217d-bf32-3a39-b0cf-5ea25c8308fe | -10.44189 | -48.21724 | 2024-09-30 12:34:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 68499238-4eb3-384a-8b9b-28e11ef0644a | -10.43166 | -48.2161 | 2024-09-30 12:34:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a5e49322-9c04-3705-9b97-780f707cfd82 | -10.41738 | -48.18296 | 2024-09-30 12:34:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 84f6db88-1fc1-3cff-8323-4d74514c71c4 | -13.50006 | -48.59148 | 2024-09-30 12:34:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0ea8c128-1278-372d-8adb-3cf2f6829b96 | -13.49862 | -48.59706 | 2024-09-30 12:34:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| b588c1ca-b421-384f-9006-c5eba7ccf7a0 | -13.49815 | -48.60336 | 2024-09-30 12:34:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b1ab25be-cc87-3a90-9f47-4453db1166ca | -13.48502 | -48.61906 | 2024-09-30 12:34:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9ed14b26-0078-3075-bce5-446a657b5fd2 | -13.4533 | -48.62585 | 2024-09-30 12:34:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bab1ed82-f597-33a7-bb2d-97de5a7c63d9 | -13.20821 | -48.55433 | 2024-09-30 12:34:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 90cd5199-3cd7-3c62-9e69-7ce127a240da | -13.19376 | -48.51617 | 2024-09-30 12:34:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 80eb4edc-7e6a-338f-8265-dc193aa1a317 | -13.19202 | -48.52725 | 2024-09-30 12:34:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 0ef00f0c-7846-3b79-a6b2-4dede1d36635 | -13.20627 | -48.56683 | 2024-09-30 12:34:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 7b067fea-c179-39ef-a2b2-93d20aa3e5e6 | -13.19823 | -48.55286 | 2024-09-30 12:34:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c5e1a6a2-556e-3c4b-a951-3332c3bfdfa1 | -13.1963 | -48.56527 | 2024-09-30 12:34:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 151.8 |
| fd778fcd-7444-3e18-b9fc-2b50cd412896 | -13.19444 | -48.57714 | 2024-09-30 12:34:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 305.2 |
| 1b511e22-e6e4-3b6b-8de8-a9a47959db29 | -13.18825 | -48.55135 | 2024-09-30 12:34:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 994ff5a9-3211-3599-ac98-92726b56e524 | -13.18632 | -48.56367 | 2024-09-30 12:34:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| e8c7a99f-a384-3078-92e3-a9837404ef7f | -13.04417 | -48.61906 | 2024-09-30 12:34:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ea9d2bc3-b9fa-371d-9f86-ce515b38c823 | -12.95671 | -48.52486 | 2024-09-30 12:34:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ee1e1c96-1ba9-3822-a14e-f60cc943547c | -12.95554 | -48.531 | 2024-09-30 12:34:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e04f22df-e729-3552-bfc5-5f87ad2c8087 | -12.52887 | -47.98161 | 2024-09-30 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 9d5f998c-735a-3511-b4f3-99c56e7d4658 | -12.51916 | -47.98005 | 2024-09-30 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| fa5dec6b-eb74-392f-97bf-9c653fc7ed92 | -14.76473 | -48.76698 | 2024-09-30 12:34:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a1ce778c-5a83-3f24-b41e-98d3baabe086 | -14.76433 | -48.76147 | 2024-09-30 12:34:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 3de0bfdb-8f42-37cf-913c-59f7103d3f8b | -14.76293 | -48.77815 | 2024-09-30 12:34:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 7a566b91-b5ad-3244-8830-b5e87a8ba98d | -14.76268 | -48.77206 | 2024-09-30 12:34:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d0657f9c-c6a1-31e1-b493-7776b4fe2037 | -14.7579 | -48.73785 | 2024-09-30 12:34:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e0635ff7-9b72-3d94-afd7-d014a2b57d4c | -14.75617 | -48.74896 | 2024-09-30 12:34:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 1d2065b1-4e65-320e-9c53-1c9e50735dc2 | -14.75446 | -48.75992 | 2024-09-30 12:34:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 286.7 |
| 9ea76105-1783-3e12-b854-98846daaba9c | -14.75277 | -48.77068 | 2024-09-30 12:34:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 00570e8e-4818-396d-b7f5-503df242d736 | -14.74802 | -48.73643 | 2024-09-30 12:34:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 8ce59488-95cf-3b78-bb2a-1da3ebb75f25 | -14.74627 | -48.74762 | 2024-09-30 12:34:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 39.5 |
| ef41280f-f46c-3a6e-a2c1-21d2fa5262a9 | -16.46369 | -48.9759 | 2024-09-30 12:34:00 | TERRA_M-T | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d6fff37b-4274-3873-afd7-da482187e6c2 | -16.46192 | -48.98714 | 2024-09-30 12:34:00 | TERRA_M-T | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 132.1 |
| b463ed40-a024-3be8-82d5-8ca6ae5fbbfd | -12.22036 | -50.4866 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 2ce3dba0-d6c5-3e68-9002-0943b9286b34 | -12.10091 | -50.01889 | 2024-09-30 12:34:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| c1f7b6f0-598c-3b3f-a349-a0d1a3f5b200 | -12.09843 | -50.03402 | 2024-09-30 12:34:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 320.0 |
| f6908713-26ba-3565-bccf-483539499b77 | -12.09595 | -50.04917 | 2024-09-30 12:34:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| ed62546b-4605-357e-8ce4-56a0ea01cbd6 | -12.08963 | -50.01702 | 2024-09-30 12:34:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 6dee6efc-5660-30b3-96aa-55900c7e3dd2 | -12.08713 | -50.03215 | 2024-09-30 12:34:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| fadb2713-4d59-3c79-8ff8-d4662be3b88b | -12.07997 | -50.00848 | 2024-09-30 12:34:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |


[Clique aqui para ver as próximas entradas](README75.md)
