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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cf64b7e-03e7-3965-bb32-910480966997 | -19.63836 | -57.73738 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 23fa22f2-f8a9-315f-804c-94b2d5481918 | -19.8795 | -42.44898 | 2025-09-22 04:19:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ad34efc3-845c-3b71-84db-b4cb75561ab4 | -18.40586 | -42.86007 | 2025-09-22 04:19:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ff3dbc32-de0d-393c-870b-8900d0580f40 | -22.41532 | -46.80015 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7b407e2-f5e9-3648-a47d-8f39086cd3ee | -18.09781 | -44.26348 | 2025-09-22 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81df3e56-9db2-39f8-8dc3-a5955f81c0e5 | -20.78529 | -56.92617 | 2025-09-22 04:19:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba0e8b62-b32b-39bc-875c-1989709afb41 | -21.01486 | -45.80276 | 2025-09-22 04:19:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9702b4c8-0ffc-38ba-b129-7bffca27c955 | -20.1312 | -42.4868 | 2025-09-22 04:19:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 82fac4db-c03e-3c66-9aab-9ab31e262ddc | -19.84285 | -42.20542 | 2025-09-22 04:19:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 0c4ea629-c75a-36de-b227-964515e0e04a | -20.54371 | -56.15458 | 2025-09-22 04:19:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54f9b7c4-8f91-335d-aa69-71be5db8db19 | -22.4065 | -46.79084 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 797ca277-e806-33c8-97bc-f52445d2ccd0 | -18.04657 | -43.84007 | 2025-09-22 04:19:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ba1a1dcd-cc70-3f40-b2ee-30e3b9ade277 | -20.18911 | -44.62484 | 2025-09-22 04:19:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d77fcc2-f1f4-3881-9d6a-2bbf5943df6b | -20.12685 | -42.49077 | 2025-09-22 04:19:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 79d95683-73b9-37d7-b5f5-d9300c6a57f2 | -17.67936 | -44.08214 | 2025-09-22 04:19:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcca480a-4d42-31bb-8ded-903f99afc9b3 | -20.55501 | -56.1537 | 2025-09-22 04:19:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3570faa-3ffe-34c1-9401-6bfd24603d31 | -18.40227 | -42.8595 | 2025-09-22 04:19:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1713a449-c37f-3d1d-b457-396ed93c1ec1 | -16.59718 | -45.0996 | 2025-09-22 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c05f556a-37f9-39d3-b24a-2387c7ebe5d4 | -19.47138 | -44.76587 | 2025-09-22 04:19:00 | NPP-375D | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef80e372-9883-3bee-a23c-654ca6381acc | -11.52326 | -43.63065 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d336d0d6-6efe-361c-9097-4205bc30a7b4 | -11.5266 | -43.63119 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a338379f-f5fa-37bf-8fb2-9c2e9993c127 | -10.32353 | -46.10576 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1405b91-2aa4-34fc-a526-6ea5545d4e66 | -19.86476 | -46.10573 | 2025-09-22 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ae84d95-4e86-3637-8a6d-c5f29b835a24 | -17.33954 | -46.82828 | 2025-09-22 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 979034a0-7e82-330d-b330-2ef590a4fac2 | -17.06442 | -44.89748 | 2025-09-22 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 721bb06d-c14b-3cbf-9357-50f7e671d7f6 | -22.40709 | -46.7871 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25ab2551-3a35-304e-be68-9d07ca027a46 | -17.08095 | -42.85636 | 2025-09-22 04:19:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7fbc913-fb2b-3dbc-87e0-81a060e1d7e8 | -17.04992 | -44.90251 | 2025-09-22 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c14dfe57-59f8-332c-bb87-757b89e9e6f1 | -18.36085 | -43.71087 | 2025-09-22 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f199a33d-cdab-3810-a25c-cd8c1f457e2f | -17.27426 | -43.45323 | 2025-09-22 04:19:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5dee786d-0744-3d63-8700-0b7de115b765 | -21.96773 | -43.29234 | 2025-09-22 04:19:00 | NPP-375D | SIMÃO PEREIRA | MINAS GERAIS | Brasil | 3167509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 294f3b19-7656-3fe4-84c7-d9017d40eb34 | -19.84323 | -57.28399 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1151b51e-891d-3028-acf6-bf3d1b9ef330 | -15.04208 | -55.29133 | 2025-09-22 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c18045b-31a2-3465-810e-eda26d9ad932 | -20.272 | -55.49867 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb8584f0-f871-30f4-94c1-3c4a5bd99b8a | -20.54518 | -56.14779 | 2025-09-22 04:19:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66bfb389-8508-384e-b35a-dad0c63499a3 | -10.36922 | -46.05359 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e46144a6-597b-3331-b609-ae2653cf0bd7 | -16.00892 | -59.47145 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| a7d5fe1c-1bf7-3492-82bb-99e05ffa6b9b | -17.67139 | -44.08871 | 2025-09-22 04:19:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3344ac57-1f3d-30e8-9813-7f0eda81a7d0 | -7.70542 | -55.44874 | 2025-09-22 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7093ce41-6e66-3926-b5c9-5df0ba04d9ff | -16.60395 | -43.68045 | 2025-09-22 04:19:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75e6a307-ec6e-3ff6-b630-9450a303ebbe | -15.95319 | -59.37497 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98e8c101-083f-3269-a352-79984cd81272 | -18.54943 | -43.84777 | 2025-09-22 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4deb378-0ed6-392d-9dd5-43a15d3f4613 | -20.25981 | -55.50566 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6c6dfb4-bfe7-349b-a90e-4015a973933e | -18.40647 | -42.86254 | 2025-09-22 04:19:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a305893e-44ff-315c-983a-58f4667cc745 | -17.39916 | -44.27784 | 2025-09-22 04:19:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac48f889-13a6-3c08-bb45-e3f43c3392e8 | -19.63144 | -57.74041 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d143a198-725e-3bd2-9cda-f0712f235827 | -18.37296 | -43.70091 | 2025-09-22 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eee6d34-51ed-3fc4-9f4d-eb88e9f8fc3b | -20.36726 | -41.10107 | 2025-09-22 04:19:00 | NPP-375D | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| af2ed435-8390-346a-9279-93504bc1e99a | -10.38426 | -46.09141 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7336a3d4-b098-3e6c-8e86-b133e7bd5bec | -20.38047 | -58.06155 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b7fdf5c3-dc52-3f98-b99b-6c66ef4598bc | -17.69077 | -41.5297 | 2025-09-22 04:19:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76a79676-5b8d-3ef3-87f7-895d1f57a402 | -22.41316 | -46.79206 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 80dcba93-7459-3eaf-97ea-c3e8ae8eae28 | -19.64425 | -57.73888 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 13b60dde-c00f-3c8d-a66b-4c7d1edbfa70 | -10.3442 | -46.06594 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 934d9d1a-e3c3-34a3-aff3-eb7b707f8121 | -14.77587 | -48.60915 | 2025-09-22 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b45bfa1-d02d-3b74-b8fa-426923c9ea13 | -20.25681 | -44.4231 | 2025-09-22 04:19:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 53379f82-d646-3e3d-a20d-64fe19c7b179 | -20.2554 | -55.50119 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cbad1202-68c0-3441-beb9-0ab7e4f1b38b | -7.71632 | -55.45503 | 2025-09-22 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 231fa38e-e939-341d-9b30-46b60fcc42fe | -20.36678 | -41.10476 | 2025-09-22 04:19:00 | NPP-375D | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e632df52-e5fa-3979-9b3c-9ea9beddd557 | -10.37798 | -46.08643 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4395d3ea-9db6-3d0c-9850-1eb3a5049194 | -20.60908 | -46.07397 | 2025-09-22 04:19:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22462963-cf36-3311-9b34-a357a15cbdc0 | -10.40563 | -46.13428 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 159434ff-49cd-3786-ab3a-09c2be98665f | -10.34536 | -46.06914 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acbbbcb8-9cef-352a-b6d4-ee3eb8cbd71e | -18.9185 | -43.73357 | 2025-09-22 04:19:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 73da0f2a-3c6f-310d-947b-0260c268b580 | -10.39463 | -46.09308 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76f835d1-8a45-3304-86e1-563c77ef8dcc | -19.85182 | -57.29955 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 66620bcc-aaa1-3679-b43b-fa2253158643 | -15.98811 | -59.47953 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da3a20ff-a542-33f3-b641-41019f0a45a0 | -18.88103 | -43.2497 | 2025-09-22 04:19:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 96bf9a5f-98af-3bb4-9bec-11a7c21e17e1 | -16.00433 | -59.47258 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 514f12bf-c453-3c22-b033-25a070a8c5c4 | -10.40201 | -47.85512 | 2025-09-22 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 993d66cc-7a86-3363-99ac-6d0802ae3f1a | -19.4352 | -44.82212 | 2025-09-22 04:19:00 | NPP-375D | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55cee5b6-132a-3ef6-9f6a-d52341a13eb4 | -21.01821 | -45.80335 | 2025-09-22 04:19:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eff201f-b65c-319c-b32e-a0823fcee296 | -15.02909 | -55.28048 | 2025-09-22 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57467e02-af18-3159-8b63-eea4622803d2 | -10.38489 | -46.08759 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81e5a429-f624-3a2a-a008-546028b5c9e3 | -15.03856 | -55.2911 | 2025-09-22 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4adba715-cf2b-3d82-a0e6-1366ab6431fe | -15.92601 | -48.35036 | 2025-09-22 04:19:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c717036-20a9-37c1-b597-0b25317e3a10 | -16.00193 | -59.46994 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 8a3fac86-9e2a-3aa9-8d1a-3f1c47c80997 | -18.3801 | -46.46319 | 2025-09-22 04:19:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bc4ace3b-f6d6-36b5-b5ab-bafdba190781 | -9.16227 | -44.62051 | 2025-09-22 04:19:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92a19ae7-c9b8-3be7-a8af-07822e42a1f3 | -19.30712 | -42.67863 | 2025-09-22 04:19:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 758d4474-0c28-375a-8d8e-bc898983c05c | -20.36632 | -41.1046 | 2025-09-22 04:19:00 | NPP-375D | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0d5c8f30-e574-3512-8206-76dafdd0add9 | -18.05144 | -43.84372 | 2025-09-22 04:19:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb15f49d-f632-35e1-8423-25886fbeef24 | -17.27196 | -43.44466 | 2025-09-22 04:19:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5149c4af-a0b9-36ed-b1b2-33341bfc0faa | -19.92118 | -42.3661 | 2025-09-22 04:19:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 212ba756-f13f-364e-9741-b210f430ee83 | -15.95181 | -59.38098 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 293f7e64-3572-31fc-9e29-5f7c01536a81 | -19.63658 | -45.37376 | 2025-09-22 04:19:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2505aac8-ce1c-349e-be78-f609fe782e48 | -19.60469 | -42.97148 | 2025-09-22 04:19:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6cf0b8ab-8836-3150-80af-714d85709033 | -19.86651 | -46.09468 | 2025-09-22 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74c8fefe-80d6-3592-ba21-10121340c71e | -19.65014 | -57.74038 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e7ffb671-c391-3b28-85f6-4c00b68da18e | -10.35479 | -46.05512 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 812c64d8-9a04-37f6-9ade-276be100f94f | -21.60721 | -44.72652 | 2025-09-22 04:19:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d3690006-4c71-3a06-bd96-b71b22ee85b7 | -20.38745 | -58.05851 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 55ec7db8-5a40-3867-b278-7b2631d4566d | -22.22609 | -47.24741 | 2025-09-22 04:19:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06b2218d-5bbe-3f8e-8c9a-dda9d5688584 | -18.53844 | -43.85028 | 2025-09-22 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1a24844-fd6c-325d-bb99-cd10d88ddb92 | -17.13895 | -45.90996 | 2025-09-22 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 136f2821-7046-369e-8edc-de6d368ad93b | -20.19309 | -44.6216 | 2025-09-22 04:19:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ac9470e-5cab-3c0d-ac50-f3db733e235c | -10.36859 | -46.05742 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8391bf5-36b4-336c-8154-9b7dabf44089 | -20.26183 | -55.49614 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 925e3bb6-77ab-36b6-a7b5-ff4bbe90eb66 | -18.74952 | -43.88257 | 2025-09-22 04:19:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81adbf17-58f6-35ff-a59d-e8615599f1cb | -20.78797 | -46.2038 | 2025-09-22 04:19:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README21.md)
