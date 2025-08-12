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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c20637a5-1e8f-3fc7-b6ad-840547f6054c | -9.3806 | -61.5315 | 2025-08-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 47f0c7c0-bc34-35cd-98d6-6c79eda5bebc | -7.1482 | -60.1366 | 2025-08-12 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 853abdfd-96bf-3fee-a781-646b26b4b644 | -9.723 | -49.4806 | 2025-08-12 00:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 07b9021d-c3e5-3f35-a271-df56d15b55e8 | -6.5856 | -44.564 | 2025-08-12 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| ade3ff3a-1dc8-36c0-bad2-43fa4e8ab619 | -7.0799 | -59.1964 | 2025-08-12 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3e00e72e-5cf3-32a7-8d57-77713d6fe0b4 | -8.9399 | -60.7481 | 2025-08-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| d6f7255f-3ddd-3305-a9ea-d166c0ab0431 | -15.4219 | -53.8863 | 2025-08-12 00:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| af937871-68dc-3d1e-b582-07c580d7daab | -19.2907 | -48.4291 | 2025-08-12 00:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 9452640d-42bc-394c-a4d2-42f013d2a4f8 | -19.7148 | -46.2151 | 2025-08-12 00:30:00 | GOES-19 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 9dcefb4b-50e2-3ae2-96f2-37718bf5c537 | -8.5602 | -54.7175 | 2025-08-12 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 987708d7-c593-3812-9c39-9b973ed9a624 | -7.1299 | -60.1182 | 2025-08-12 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 236.1 |
| 1e440205-a526-3120-9393-4e745be88249 | -16.2961 | -52.9016 | 2025-08-12 00:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 55e0d0e1-81fc-32d2-8e07-0e00f3f9fbfe | -8.9215 | -60.7297 | 2025-08-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 48cebb76-6533-3058-9eb0-236dd2d52523 | -8.9401 | -60.7288 | 2025-08-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 33202c5b-dd22-3d31-92c9-58437167112a | -8.5211 | -43.3063 | 2025-08-12 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1b5d7a30-55c9-3dc5-a6a7-c0ba11c9eb8a | -22.9828 | -49.0361 | 2025-08-12 00:40:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 5496a71d-1670-388a-ba1f-eb648e72f10b | -19.3109 | -48.4248 | 2025-08-12 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 95ae6513-c890-306e-ba82-3717d04c6cc1 | -8.9215 | -60.7297 | 2025-08-12 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c809d73c-f56a-33e5-bc71-89790a202be2 | -19.7148 | -46.2151 | 2025-08-12 00:40:00 | GOES-19 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 1a862618-9c22-3ae9-85fe-226ffd40cdb5 | -7.0799 | -59.1964 | 2025-08-12 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 61bccdc9-ecaa-3689-a8e8-2e2bf5d6f352 | -9.3806 | -61.5315 | 2025-08-12 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| fa67b331-5e6f-3fe4-9793-de6ca0c30b86 | -22.6145 | -54.9905 | 2025-08-12 00:40:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 41.9 |
| e241725e-b0f0-35e7-b7db-1bfe1bd02b2b | -12.7759 | -45.4445 | 2025-08-12 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 58dc909c-b051-3f90-84e9-5e366c9345d2 | -6.5856 | -44.564 | 2025-08-12 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a4d44b6f-41b7-336a-ba20-c16a8fc97768 | -16.2961 | -52.9016 | 2025-08-12 00:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f492dcf1-6625-3a41-b82e-53f5919a235d | -8.5211 | -43.3063 | 2025-08-12 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 0b91c422-461f-3b60-a6e7-064436c76a5f | -9.723 | -49.4806 | 2025-08-12 00:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| b1784eb2-e0ac-3eda-a60b-47d64449f9d5 | -22.6353 | -54.9867 | 2025-08-12 00:40:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 59.9 |
| c89a8913-2e1f-38ec-888b-ab6abf1d49df | -9.5152 | -40.331 | 2025-08-12 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 524cdede-a8af-397e-9ae5-ff36dfc1f5ae | -6.9686 | -59.2783 | 2025-08-12 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 3bd30013-b84a-3ea1-901e-7acd412b2f0f | -22.6348 | -55.0086 | 2025-08-12 00:40:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 43.7 |
| 12c2db53-d6fb-3d60-b6da-5d8f6031a24e | -7.1482 | -60.1366 | 2025-08-12 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 147e6ab0-5957-362b-bb96-e6de72a7355f | -15.4223 | -53.8653 | 2025-08-12 00:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 3476cfe5-8c68-34e3-a120-9ae990fd9558 | -7.1299 | -60.1182 | 2025-08-12 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 199.3 |
| 8190a854-d303-307a-afc6-e2fe48d23be0 | -8.5788 | -54.7162 | 2025-08-12 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 98b4eddb-056b-36ca-b646-88c7fe9ac1c4 | -7.1298 | -60.1374 | 2025-08-12 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 1da814c5-31b4-3cc0-b6b2-91d970e1346b | -11.9493 | -43.4019 | 2025-08-12 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 2d713206-46aa-3c59-b9a4-996dd1b69b46 | -15.4029 | -53.8678 | 2025-08-12 00:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 143970b9-5929-3c60-928b-78288c5a87ac | -9.5147 | -40.3558 | 2025-08-12 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 20696433-4665-3ead-a47a-ce923c8145ec | -21.7801 | -48.3036 | 2025-08-12 00:40:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 17ae02d5-c2a8-38b3-9d0e-98416bbebde4 | -15.4025 | -53.8888 | 2025-08-12 00:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 6dd2bc89-7408-3845-abf2-43403bbae7e3 | -7.1483 | -60.1174 | 2025-08-12 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 0f47b368-b77a-3b41-99cd-a3cec3ed484a | -8.9401 | -60.7288 | 2025-08-12 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 9cde680b-e941-3d6c-ba11-bf9d897e102f | -19.2907 | -48.4291 | 2025-08-12 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c185f91b-fec6-3574-bb5f-5272e4597087 | -16.2957 | -52.923 | 2025-08-12 00:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0ec0d83a-6e9b-3214-a5f4-4d5f5c5bb922 | -22.6348 | -55.0086 | 2025-08-12 00:50:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 54.7 |
| f46de018-2dc1-3a95-9b93-c56c0dd4431b | -6.5856 | -44.564 | 2025-08-12 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 7a16626e-99f1-3925-96df-0d24dd14f4de | -8.5788 | -54.7162 | 2025-08-12 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 81087f19-89c7-3e7b-b9d5-02dcd4c7c0d7 | -7.1482 | -60.1366 | 2025-08-12 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 73d38e3f-3cb9-3f9d-986f-4422d7221cf2 | -7.1299 | -60.1182 | 2025-08-12 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 228.2 |
| 5340a320-72ff-348f-9a08-f36e5ff47b5f | -9.1894 | -59.6558 | 2025-08-12 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| cab232b4-14af-3c61-94cb-3344939fdae1 | -19.3109 | -48.4248 | 2025-08-12 00:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 632906cb-89ce-3004-8dee-6d29124505a2 | -22.614 | -55.0123 | 2025-08-12 00:50:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| 1c8cdf91-4b3b-3d0d-9288-ec5be1d1c204 | -19.2907 | -48.4291 | 2025-08-12 00:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 928a81c7-dd40-3279-8f32-aef758b2b25d | -8.9215 | -60.7297 | 2025-08-12 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ca38ab40-9037-3bc5-a475-848c821fdda2 | -6.9686 | -59.2783 | 2025-08-12 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 5f794539-f0e4-3721-abff-260a9434e37a | -14.6894 | -53.7272 | 2025-08-12 00:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c94e1cad-d3d4-30a6-adc9-3dcd5a7184fa | -22.6353 | -54.9867 | 2025-08-12 00:50:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| 48894598-4492-3d4a-8673-7a68550a7ec3 | -8.5602 | -54.7175 | 2025-08-12 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 027bc1d1-4c4a-3336-bbaf-2ed4cd4a6916 | -7.1483 | -60.1174 | 2025-08-12 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 41d77fa0-fb30-35cd-82fd-6ffff3983db5 | -8.5211 | -43.3063 | 2025-08-12 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| e8f70a13-ee7c-382c-9deb-98b60af5b81b | -22.6145 | -54.9905 | 2025-08-12 00:50:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 61.3 |
| 69cd3c43-d6ee-3142-9f1a-5aec4da4b4fa | -12.7759 | -45.4445 | 2025-08-12 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f2c9cabd-767e-3c19-a27d-9bb409ef3e18 | -7.1298 | -60.1374 | 2025-08-12 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 20cb34ef-2295-3f4c-ab6f-8692e533e508 | -16.2961 | -52.9016 | 2025-08-12 00:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 48a732cf-9e87-3bfc-87a3-54ef00b80426 | -22.9828 | -49.0361 | 2025-08-12 00:50:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 28b44397-ad32-3dbc-8414-d294bff519e5 | -16.2957 | -52.923 | 2025-08-12 00:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| dc39f002-5382-3b5f-b281-936570ec5f04 | -7.0799 | -59.1964 | 2025-08-12 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ebfc7179-d28a-3f81-898c-c44daa166bc1 | -9.3806 | -61.5315 | 2025-08-12 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 44879b67-0451-35fb-a6cb-66f39e94c469 | -6.7272 | -43.5822 | 2025-08-12 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| c40706c3-1a6a-3a19-825f-34b8523f0c97 | -14.6898 | -53.7063 | 2025-08-12 00:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| eda53216-fa36-35e9-ab4c-164b60d905ea | -8.9401 | -60.7288 | 2025-08-12 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 854d1be6-a431-329b-b1fb-0e909789b30f | -9.7041 | -49.4825 | 2025-08-12 00:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| b1ee6941-db41-343c-8154-71578f464e0b | -9.723 | -49.4806 | 2025-08-12 00:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 34cf27e0-f316-3c1a-b74d-05e7d7d1e4de | -22.614 | -55.0123 | 2025-08-12 01:00:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 96.0 |
| a82dde28-81e9-3db5-8141-2d6e4909b66d | -22.9828 | -49.0361 | 2025-08-12 01:00:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 1e29dc16-1f0b-31d4-a989-22c49b53db26 | -14.6894 | -53.7272 | 2025-08-12 01:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 8c231ff2-86ff-30c1-92ac-8402930e0810 | -12.7759 | -45.4445 | 2025-08-12 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 3cb72f00-a23b-3ec7-9fc9-8cc6e00d4a7b | -16.2961 | -52.9016 | 2025-08-12 01:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| adf3ec87-7bf0-3913-9a4b-803a6cf64756 | -14.6898 | -53.7063 | 2025-08-12 01:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 2375a012-fdac-35d6-883d-585e50154f3c | -7.1482 | -60.1366 | 2025-08-12 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 224aa9d3-7b90-3447-a155-febf81792fc1 | -7.1483 | -60.1174 | 2025-08-12 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| ce5d7107-9eb5-3704-891c-04eb635658a6 | -23.1498 | -47.0511 | 2025-08-12 01:00:00 | GOES-19 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.0 |
| 8922e289-8b48-3519-b4ab-fe8c0e824922 | -8.5788 | -54.7162 | 2025-08-12 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| aebcc64f-9567-310a-9f9f-16d8fa87ca04 | -8.5211 | -43.3063 | 2025-08-12 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| cc8ea81b-81ba-357a-b830-5be492e53fcc | -8.9215 | -60.7297 | 2025-08-12 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| c624bb5a-f466-3fe3-8cb1-a9813ace8838 | -19.3109 | -48.4248 | 2025-08-12 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| c7930c11-fd29-303d-a104-c754972128ad | -7.1299 | -60.1182 | 2025-08-12 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.9 |
| f3c90ce1-d7f8-3a5d-b662-a412e0ca77a1 | -6.7272 | -43.5822 | 2025-08-12 01:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| cdca9c94-fb42-3261-a8fc-3d6596706661 | -9.3806 | -61.5315 | 2025-08-12 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| dff7ac7c-0c91-302e-a572-c7e1b5e85e06 | -22.6145 | -54.9905 | 2025-08-12 01:00:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| eb2fbe86-c0ca-3df3-8a3e-5d583adaa10b | -19.2907 | -48.4291 | 2025-08-12 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 1d45ef70-64d2-3ae5-9795-95d814d63e89 | -7.1298 | -60.1374 | 2025-08-12 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 0b0df153-c6b2-3cec-b32b-b0f9cb91343e | -6.5856 | -44.564 | 2025-08-12 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 2393b87e-6383-34ee-87d5-b34ec1866581 | -22.6353 | -54.9867 | 2025-08-12 01:00:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 87.4 |
| 809f6e32-4caf-318f-bc39-56d63ae9bf2c | -6.3008 | -51.3996 | 2025-08-12 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 32840db8-f5ec-381c-aa17-71fad2b6f2da | -7.0799 | -59.1964 | 2025-08-12 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 5ac8b031-1cf3-33b2-be0d-d1b7da1affd9 | -12.5742 | -47.0006 | 2025-08-12 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| c6e6509c-df3a-3b0f-9701-d1a6d2a18a4e | -9.723 | -49.4806 | 2025-08-12 01:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| e84e9283-c8f5-3011-93b3-639ef8bf69ed | -22.6348 | -55.0086 | 2025-08-12 01:00:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 124.7 |


[Clique aqui para ver as próximas entradas](README3.md)
