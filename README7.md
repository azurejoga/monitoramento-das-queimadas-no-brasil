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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b69e09fd-07b0-3b1e-a716-914e534dd913 | -15.73041 | -55.69348 | 2025-12-30 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68d4ebb4-5c01-33e6-b0fb-124c501c0dd6 | -13.50847 | -46.70682 | 2025-12-30 04:36:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| debe336f-7379-39a3-aa7d-bdb8d06c7486 | -14.38911 | -47.3706 | 2025-12-30 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9826b19e-d475-3869-8fda-25b7e8e2b3f5 | -15.50339 | -51.85581 | 2025-12-30 04:36:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c34b8f3-2c5a-3e07-a9fc-65a7681134cd | -18.11516 | -51.15488 | 2025-12-30 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e029e787-4f0d-391a-a7b2-512a7329f23d | -15.49722 | -51.85085 | 2025-12-30 04:36:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f231f296-d7be-37eb-aa00-8a6b6ce57b18 | -15.1289 | -52.94906 | 2025-12-30 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b1ea3faf-7424-3ea8-ae5e-f292581c0aa7 | -15.5 | -51.85522 | 2025-12-30 04:36:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 441407b8-164b-3619-b503-f21458eec1ad | -14.38854 | -47.37457 | 2025-12-30 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46836ead-bfca-3008-84ec-4fd00e7f15ce | -15.54334 | -42.94327 | 2025-12-30 04:36:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d3316d7-587a-3621-8016-210bc77b1ed4 | -14.38563 | -47.37004 | 2025-12-30 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aaf2b5d8-0f01-31c5-83e3-e052f8d0b78a | -15.6343 | -48.54927 | 2025-12-30 04:36:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e7dc2d6-9f28-34f9-9199-4606849d3ee8 | -15.12967 | -45.28342 | 2025-12-30 04:36:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9a237558-f8d0-3f60-bcd7-77e2ab9d9fe0 | -15.49382 | -51.85025 | 2025-12-30 04:36:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24fceaad-0f3f-3151-8a1e-bc2f7c96c531 | -16.00803 | -41.67981 | 2025-12-30 04:36:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8fae464f-6aa4-318e-aef3-c22087d6a994 | -18.65104 | -42.6725 | 2025-12-30 04:36:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f69614df-6535-3bc5-9ea2-ea5549ccfc0a | -17.76343 | -47.05786 | 2025-12-30 04:36:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 837ca4a7-b3c6-3843-b004-f7388aaa32dc | -18.60069 | -41.70969 | 2025-12-30 04:36:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d03cce94-fa4a-3fec-930c-3ac2a78eb575 | -15.11824 | -52.94714 | 2025-12-30 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9668f00c-9549-30a4-a119-2c60d3af1cf6 | -17.0691 | -48.10008 | 2025-12-30 04:36:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cd42ac6-3441-3811-a576-8592b45deadf | -15.50617 | -59.39594 | 2025-12-30 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5eab5bd6-a9b9-3031-b797-b42d6512fe1a | -15.50401 | -51.85203 | 2025-12-30 04:36:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edeea037-7861-359e-9d53-21fa9d785ddd | -15.4932 | -51.85403 | 2025-12-30 04:36:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb7b5fe1-93b2-397c-a887-9dfce60ee363 | -15.13819 | -45.27948 | 2025-12-30 04:36:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c0f8ef5-9ef8-3c44-a38f-e167a2509f62 | -15.37072 | -53.04076 | 2025-12-30 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62bd9de7-d2d0-32f8-9465-bd5443c2424c | -16.05247 | -58.97524 | 2025-12-30 04:36:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 197c357f-35fb-3673-a12b-a353f868d36a | -15.1218 | -52.94776 | 2025-12-30 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4576a066-7ef7-3c4d-862b-44f20e418aa7 | -15.50062 | -51.85144 | 2025-12-30 04:36:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d8ebdbd-2c68-32ff-80a4-f280b5371efe | -14.38621 | -47.36602 | 2025-12-30 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 04ed1be1-e9a7-3c15-8040-62c8aa5b5a4f | -15.12959 | -52.94493 | 2025-12-30 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 53b77ce6-20a6-3be8-9515-0824c7a98bb3 | -15.13427 | -45.2789 | 2025-12-30 04:36:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9df60e6-cf2b-37f9-b4d0-09042d6d06df | -15.1375 | -45.28461 | 2025-12-30 04:36:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0090a7f4-899d-3b73-88a7-280b097e61bf | -15.50684 | -59.39263 | 2025-12-30 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8195c060-27f2-36bd-87fb-9792a6e88496 | -16.57693 | -51.55289 | 2025-12-30 04:36:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 372b7287-be86-3b66-88b4-da612745b94c | -15.13359 | -45.28402 | 2025-12-30 04:36:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd021d77-e156-3153-9dfa-279f12619788 | -16.3843 | -46.28323 | 2025-12-30 04:36:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21a30414-3dab-3060-9f26-3594eedb6de5 | -14.50098 | -52.55553 | 2025-12-30 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dd9a7e6-1449-3c3f-a602-f23270f12d53 | -16.5718 | -51.03886 | 2025-12-30 04:36:00 | NOAA-21 | AMORINÓPOLIS | GOIÁS | Brasil | 5200902 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebcc4d2a-fdba-3e8f-ac92-3494e2bac824 | -15.12899 | -45.28854 | 2025-12-30 04:36:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f12a545-cc58-39ae-8fc9-d80346edeed8 | -17.76521 | -47.07187 | 2025-12-30 04:36:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ac6b237-c81b-39b2-8f91-fd6e0e5ace91 | -14.38429 | -47.36707 | 2025-12-30 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c34bbdd-af8f-3222-af5b-baa8169acb52 | -13.50491 | -46.70628 | 2025-12-30 04:36:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd228b7a-770b-3524-b29b-1dcb187efbe8 | -15.25966 | -41.8126 | 2025-12-30 04:36:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3fc6972b-9572-3a1f-bb7c-5c1e2b5e6176 | -19.77692 | -41.91174 | 2025-12-30 04:36:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 60e5ea6c-e417-38cd-ae74-4fb4a89539cc | -15.59328 | -49.09671 | 2025-12-30 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31934cfe-3d20-37ec-a0ca-502525e72b74 | -16.85151 | -50.67162 | 2025-12-30 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8ef7baa4-feec-3823-b9f6-35f2be7615a1 | -16.57633 | -51.55656 | 2025-12-30 04:36:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51d51e3a-b3b2-3e70-9b25-ecc8acdc56bd | -17.16397 | -47.72175 | 2025-12-30 04:36:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff62a16f-c632-3e9d-85e0-72df3f252106 | -15.67841 | -46.70243 | 2025-12-30 04:36:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a205ec07-fd57-3558-b3c8-a175a0eabeea | -13.5055 | -46.70217 | 2025-12-30 04:36:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6f24827-a1e7-326b-8b3e-a6ff5de62e1f | -15.4966 | -51.85463 | 2025-12-30 04:36:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d70455c1-6d66-3700-a150-bb0b49062a9f | -24.54252 | -50.73206 | 2025-12-30 04:38:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| b80b1157-0ccf-364b-b299-64ddc1bd92cd | -18.82157 | -51.61117 | 2025-12-30 04:38:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 18b56001-e18f-3192-86b2-b584e6b03e08 | -21.25656 | -48.65519 | 2025-12-30 04:38:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9a73afc0-033f-3e62-9d54-8efe7f4541a7 | -23.26785 | -51.0287 | 2025-12-30 04:38:00 | NOAA-21 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f4311d8f-7ae7-388b-86d0-ac4045564a63 | -21.15879 | -43.08672 | 2025-12-30 04:38:00 | NOAA-21 | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ede86c72-a950-382f-af67-16863f9d3fc0 | -21.25714 | -48.65096 | 2025-12-30 04:38:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4eafa57c-71eb-3735-be1c-9cae346372bc | -23.6942 | -49.52412 | 2025-12-30 04:38:00 | NOAA-21 | ITAPORANGA | SÃO PAULO | Brasil | 3522802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4d145013-781d-3f3c-ae78-39d8c6d41eb1 | -18.63923 | -53.29382 | 2025-12-30 04:38:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12929def-2734-38a8-8b4b-de748ee7dae9 | -19.09834 | -56.07162 | 2025-12-30 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4f817735-5799-3d9f-bc86-acdadfa541ed | -19.09437 | -56.07081 | 2025-12-30 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ebda8de5-c66e-3de0-81bf-2f444a74a367 | -23.26727 | -51.03251 | 2025-12-30 04:38:00 | NOAA-21 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f80e394b-cfb8-39e9-b876-a494768dedcd | -20.91766 | -49.23279 | 2025-12-30 04:38:00 | NOAA-21 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5ac898e3-2f2e-3964-a87d-565010f6ace7 | -18.4202 | -54.56235 | 2025-12-30 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f64a720-12fe-371d-b9b2-085ffb4563b6 | -18.82489 | -51.61176 | 2025-12-30 04:38:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b7794c04-f0a6-31f1-b5dc-63396355b97a | -18.82215 | -51.6075 | 2025-12-30 04:38:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 17f53867-7bc6-366c-bcec-7e71f20f327d | -24.54647 | -50.72872 | 2025-12-30 04:38:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| a7b42fae-3f63-3c1d-a5bf-8a7fec61e913 | -21.08557 | -48.58758 | 2025-12-30 04:38:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0394e77b-ded1-377e-8ff6-d01fb9988ada | -18.82548 | -51.60809 | 2025-12-30 04:38:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f3b53bb5-42c9-3255-8c40-3fea31f9a026 | -10.0463 | -36.2664 | 2025-12-30 04:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 118.8 |
| d0c13b68-a7a6-39f0-a447-174177bc173f | -10.0463 | -36.2664 | 2025-12-30 04:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 294.1 |
| e186d9bb-776a-3db0-99eb-464f8db08d17 | -10.0458 | -36.2935 | 2025-12-30 04:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 104.8 |
| cf21ca2a-455c-3dc7-a45f-eed41a8d6458 | -10.0468 | -36.2394 | 2025-12-30 04:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| 88b28946-af0d-3e88-af1f-44e1c08871aa | -10.027 | -36.2699 | 2025-12-30 05:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| 1bea36f9-8bc3-30c1-900e-a21a6c4dbccc | -10.0463 | -36.2664 | 2025-12-30 05:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 117.0 |
| ef313f20-0df1-3a20-80ee-cebabb272dde | -6.93391 | -44.5784 | 2025-12-30 05:01:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c118dde0-5b0d-38ce-87d8-b20b0b91d327 | -4.17609 | -48.63587 | 2025-12-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 747bfa23-b7e0-3c3b-8c74-65e6ac93de32 | -2.22461 | -48.11949 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95216a94-7dce-363f-ba7a-b44b0f79605f | -3.5572 | -43.59732 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43a989ad-0db8-3be5-acf8-101a31361570 | -2.09725 | -48.37525 | 2025-12-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5793a1f-9559-328f-9a4b-7897628b38ec | -4.60925 | -46.59257 | 2025-12-30 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0d0d31a-3ea2-3485-9e1e-c941e0fa0a64 | -4.60849 | -46.59758 | 2025-12-30 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51637fc8-7819-3a02-b654-6beff2eaf100 | -6.60633 | -47.62111 | 2025-12-30 05:01:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 568ae660-a490-338f-a946-cae0cf94f6bc | -4.34527 | -44.12008 | 2025-12-30 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6d2abe6-7398-3313-b125-764aaf3b7d99 | -3.54902 | -43.60205 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1980d135-5eff-3b43-9607-abbc6d8eb06f | -1.4808 | -54.20135 | 2025-12-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3d15545-7be6-30a1-a88d-1e81a4a13328 | -3.18386 | -48.02706 | 2025-12-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d3b6d0b2-178b-3fc4-b41a-0861b952e040 | -4.60372 | -46.59703 | 2025-12-30 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af35a913-e830-3c26-96c6-5b17b7601f90 | -6.93149 | -44.57775 | 2025-12-30 05:01:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b52aa29-c642-318c-a4ea-bd3499960905 | -5.3139 | -45.17889 | 2025-12-30 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a5d875e-a737-31ba-8e58-04aff6506d9f | -3.55036 | -43.60427 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a23db138-dbf3-3ba4-8279-03553ebaf1de | -3.55534 | -43.59896 | 2025-12-30 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afc6e89d-ebf0-3a4f-8b90-a5e4e1df3286 | -3.02864 | -49.44271 | 2025-12-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbf0715a-36ec-3b63-8414-5864ce34b915 | -2.22734 | -48.11916 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6761adb0-027e-3b63-b7cf-02fa0af06afd | -4.60447 | -46.59211 | 2025-12-30 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87478488-cf73-3c44-a74b-3dbd07b612df | -1.49173 | -45.88959 | 2025-12-30 05:01:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de78a492-7b96-33ea-99bc-2e2e888b3415 | -2.17703 | -48.01799 | 2025-12-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9ce254f-8e89-34ee-a06b-148cb2722610 | -3.02099 | -49.44154 | 2025-12-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ff8211c-8839-3662-842b-a345a1a4d431 | -3.17127 | -48.02508 | 2025-12-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bce81ea-5ef6-36e3-95da-c63fee865534 | -3.02553 | -49.43745 | 2025-12-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
