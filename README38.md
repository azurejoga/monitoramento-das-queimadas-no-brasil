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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0354e944-42fb-3cbc-8d80-55f0d23d9c53 | -11.09599 | -46.15582 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8164cb5c-98e8-3658-aadf-09e685cd0cab | -12.87226 | -48.50085 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b6d9ee1-ad56-3845-bd1b-113a8580e813 | -14.35243 | -52.88954 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0cf34e-83c5-33ae-b969-417a44fefc12 | -12.20678 | -43.17539 | 2026-08-25 04:27:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6de7d09-64df-3282-93af-40b19abe8d2c | -14.28009 | -53.19881 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e065aa8-e5fd-38d5-a306-ff1dae3ff1b9 | -10.77537 | -50.92838 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2c452786-8986-390c-ad67-955386a9be30 | -14.25677 | -52.12754 | 2026-08-25 04:27:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e8c42af-06f8-3817-88d4-bd4a23c68130 | -12.13065 | -45.12084 | 2026-08-25 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce0d7dc1-7a2e-3283-bfe9-e231d0a27a5a | -16.05857 | -50.46215 | 2026-08-25 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a54fce1c-4a6c-3916-8cee-91fe054ef498 | -10.80207 | -50.92533 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0e3b47a9-54d5-3712-8df4-f6837eb1f3ee | -13.65602 | -51.86032 | 2026-08-25 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 568a6fb1-af89-3be1-b39b-87df40ad534e | -15.23656 | -52.79795 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65b3616c-c4c8-391c-8ce6-b75cc9ba96ee | -13.86042 | -54.00601 | 2026-08-25 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 913c367a-1083-3771-b0c8-154c55997221 | -10.5311 | -50.7748 | 2026-08-25 04:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed19a526-09fd-3d2d-aa90-fae6a3c4d039 | -11.56104 | -46.9672 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db311bc9-c15d-3116-ad6f-632cd369731a | -11.77628 | -47.27153 | 2026-08-25 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59193c67-86e1-3e06-9a05-d45a4aadeb09 | -12.88585 | -48.48301 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3359e549-a5f4-3b5e-be9c-74384be3b08f | -11.97259 | -45.89578 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65ba478e-fe5f-3095-863d-aa44c786a45a | -12.86259 | -48.49513 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48e284d8-87d9-30fc-a09f-d6cfa41e1fba | -11.8834 | -43.82289 | 2026-08-25 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0705cbd2-4482-3049-844f-07294b60ed7b | -16.83748 | -42.01728 | 2026-08-25 04:27:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 11432b92-c356-3605-949a-81d361ceabb0 | -12.14323 | -48.26265 | 2026-08-25 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99cf6a06-b94e-38da-85ab-c06e0c40e3be | -12.7441 | -46.4724 | 2026-08-25 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0717766e-b626-34f0-8d11-2a58e501bcb1 | -11.38885 | -45.15782 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5d8bce2-605c-318c-9547-bc4f1ce83328 | -9.16174 | -59.40186 | 2026-08-25 04:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27107b1a-6312-3571-a6c8-2154274947de | -11.88629 | -43.82732 | 2026-08-25 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1ccc4053-e5e7-37b3-b256-cbaa935c99e1 | -14.45312 | -44.29547 | 2026-08-25 04:27:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5ebe4189-2cf9-38da-9882-acf57c5a7b0a | -11.43133 | -44.54772 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2555736a-be19-31b3-93c0-3f9c2bdb8a8a | -11.44147 | -44.5493 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35f6ddc5-07d4-375d-ae84-44ab45604f24 | -11.40051 | -45.1706 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecda8fe4-cb0b-3975-a62e-6ea30861126e | -14.35595 | -52.8944 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ec21b76-cb4b-31a1-9a09-f2121ff7be80 | -14.38913 | -51.76495 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b62b048a-479e-392e-bf34-4640020946e1 | -15.55597 | -53.11834 | 2026-08-25 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3922ba22-bab8-3adc-8e5e-f837f2530b53 | -12.71976 | -48.38557 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c80ce12-d541-364e-b51a-d20b0fd963db | -13.35064 | -48.20029 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42b794ea-49d2-3544-8e17-83c326c9cc11 | -16.39679 | -49.93043 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 778be22a-9219-329e-8e60-ae6d0ec8e81a | -12.77908 | -44.26382 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5b3914d0-c27f-378e-9e3b-ad86882591c5 | -10.79601 | -50.92848 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 09503132-0035-332f-b9db-66f4e08d5695 | -16.84103 | -42.02163 | 2026-08-25 04:27:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| 10f20cbc-add4-38f0-9048-ea371deebb23 | -13.36026 | -48.20549 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2b3d138e-e320-3e60-885b-35ae70256fc9 | -13.89748 | -54.06549 | 2026-08-25 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55ec4c10-480a-3741-a955-c9bc700d60aa | -16.41553 | -49.92806 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff7ef5d9-98fd-327f-9b86-ebeda5adcfe3 | -16.4241 | -51.84446 | 2026-08-25 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a172566a-b192-3849-a9b8-e20503552be7 | -11.15741 | -53.99913 | 2026-08-25 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 509e9f00-b2e5-31ce-b6a4-cf6a2bd7f503 | -14.36024 | -52.89518 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 422642e9-f735-306c-8a4f-d586ce0bbcdf | -11.3894 | -45.15427 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3573a458-904a-3740-a5f3-9e2488fc545f | -12.64309 | -47.7892 | 2026-08-25 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09150a0d-c0a3-39b6-8217-f78504e3be1b | -15.25122 | -52.79143 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 065683c9-dfc3-30f7-ba41-996497e0635c | -13.10488 | -43.34591 | 2026-08-25 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f859c81c-eb88-3001-b545-125835fc0439 | -13.86134 | -54.00118 | 2026-08-25 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 923521a7-9ed1-31c8-a813-a8065877e0ca | -11.98031 | -45.91146 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9d78388-bece-3927-9e37-e9ec32160b47 | -13.62986 | -49.02448 | 2026-08-25 04:27:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3db5f6c6-a9f2-3bf5-a557-1dfb25903d54 | -12.20493 | -43.18798 | 2026-08-25 04:27:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ef102fe6-5275-3b5c-8a34-82ae89487fff | -12.74354 | -46.47593 | 2026-08-25 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 907df7e0-10fb-3272-b740-098983c1f0ff | -11.97479 | -45.90335 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 476ef908-cc9c-307c-b4df-bc315b760029 | -12.75245 | -46.44123 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae9925d1-8063-345f-b9e6-95391b144ad9 | -11.97755 | -45.90741 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d5190c9-a83f-35cf-a3c7-523904bb45aa | -12.74298 | -46.47946 | 2026-08-25 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a2a753a-ac6b-3618-b1a1-389889b1e2e1 | -12.86603 | -48.49573 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cfa4efa-1654-3315-aa59-c52c31686fe1 | -11.99133 | -45.92767 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01ae9eca-f48d-3a3b-8fbb-d6dd32775226 | -12.77579 | -48.36397 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 819fd9ea-6b12-3f34-9c79-f7e554b57e62 | -13.65199 | -51.85938 | 2026-08-25 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 909c935e-02e4-36d4-91ab-ddb41eb1287e | -12.13207 | -43.38714 | 2026-08-25 04:27:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75dab1dd-86ab-37f4-91b9-8db61e688173 | -12.21097 | -43.1718 | 2026-08-25 04:27:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 403e825c-e2d2-3f43-8bb8-02e8901ace4e | -12.75301 | -46.43771 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9915a813-19ef-3f90-b6d2-43dbefbe651d | -12.19835 | -43.18289 | 2026-08-25 04:27:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fd4e4537-6361-3cb5-b040-322394c12e4f | -16.39184 | -49.91681 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| af62ed1c-1a8a-3d18-992e-035670377119 | -12.60794 | -44.6345 | 2026-08-25 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56f5d354-5ae7-303d-82af-bb59a246dc6e | -12.75576 | -46.44178 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0509f4c1-1a47-3952-b420-38712e7897af | -12.84205 | -48.49713 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 273eea3e-8d56-3c1a-b583-6ebd9a146d9d | -12.78138 | -44.272 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4ef1b714-f146-37c4-ad65-3c97a714c4f2 | -16.43853 | -43.46376 | 2026-08-25 04:27:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d2d46ad-f2c9-3032-bb4b-d4277b12a42a | -16.39748 | -49.92632 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 13c1c904-9665-32b1-bbf9-233dd2422343 | -15.30332 | -52.81475 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c30cbe45-3a67-3cdd-afa0-207b69432a91 | -14.38162 | -51.9681 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2de3bbc5-f31e-30ad-9a34-b0f3575581d2 | -14.35693 | -52.89993 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1396f57b-0fe8-371f-8eac-8b56c48a5900 | -11.16229 | -54.00009 | 2026-08-25 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| badd9ed2-cd8d-3470-ad17-41df3a6d3356 | -12.73422 | -46.47089 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b460bb2-cc27-3a13-895d-e58c1973a50d | -12.77277 | -44.25892 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50c25990-53da-3c75-b40f-6dda24065e77 | -10.78217 | -50.93692 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 53e9fc0e-954d-3cb0-83c2-d977f3f7576a | -12.76831 | -48.36655 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3b6755f-ee8b-3b93-a7e9-9e14d87495d3 | -14.87119 | -52.6559 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2285b9c-2b1c-30a4-93ce-0b16d5870812 | -12.78081 | -44.27581 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 706b4019-7516-3960-9472-662c041312d8 | -13.35344 | -48.20446 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5834613d-fd03-38e8-9180-d87fedd5e0b7 | -10.79079 | -50.93483 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| a8265aa6-00a8-3538-883c-3f226909c2db | -12.70226 | -48.40592 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44d52e8a-d1e3-37ee-9010-d0b249f08e3b | -12.88259 | -48.50258 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43027bd0-06f0-30a5-bc7e-86ddc539e4c8 | -15.23732 | -52.79374 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d9dea43-bbe3-357c-8258-88f49194a30f | -14.35321 | -52.93252 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5574ff1a-df22-3331-909e-2ae4c45bd460 | -14.35672 | -52.9257 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9355c90b-b81b-300d-a51c-843d80e69be9 | -14.36294 | -52.90442 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ce5d27f-7b8e-3612-b207-ac5351f37107 | -12.86537 | -48.49967 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 018ae8c6-452a-3890-8f3d-f7ec4a0ea12f | -16.42112 | -51.83879 | 2026-08-25 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b09e1ec6-a037-357a-8d1d-d4169445b522 | -14.55052 | -49.11095 | 2026-08-25 04:27:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e17e9e32-f554-3231-bd26-1f12a1ded593 | -9.67571 | -55.09582 | 2026-08-25 04:27:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7952aa7-34c4-3ed0-abda-4736b59a7097 | -11.5638 | -46.97132 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f2853f3-2584-32bf-b4ac-46759e28ac0a | -12.76768 | -48.37028 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e98682c5-92f0-3773-9ffe-ceb5ba2de45c | -12.71225 | -48.38828 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32265646-13ed-3a75-a48e-295d31c1978a | -16.40099 | -49.92698 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9d73192-8973-3a5c-8599-1ecc310ebe55 | -14.39888 | -53.09548 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README39.md)
