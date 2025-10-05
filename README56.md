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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2af9cd17-accd-312d-a8c8-a2dc66e5b7e2 | -12.45466 | -44.73815 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf1a3344-1f89-338d-8d1c-1628d7ddecd9 | -11.07957 | -47.91679 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 395f8ca0-9081-3c59-b97a-c777b0b3639a | -11.87188 | -44.95947 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b896746c-f04f-34c0-9059-9a2ad3b44e61 | -15.29603 | -47.33125 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9613eca9-6d42-36b3-ad51-0f65579382ac | -15.11246 | -45.76346 | 2025-10-05 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9be3314-74b7-38a2-91a9-2fc718547905 | -13.27735 | -47.59262 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2e3ab4be-d09b-3d50-8d2a-a27cf66fc872 | -11.6778 | -47.48663 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 35530aba-0302-3478-b7ee-dd76867c5c82 | -15.54096 | -46.81206 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ebdadda-38bc-356f-8b8a-1cad2d89cb33 | -13.25016 | -47.81938 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df1e2dbb-3f6c-3a7c-9d72-e9a6f3856f04 | -14.58094 | -52.46234 | 2025-10-05 03:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 228c3bda-6478-3cd0-815c-a7e855a3605b | -11.1083 | -47.87595 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8173bd0a-8283-3e06-baf5-8a1d953032d7 | -13.72942 | -51.27018 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a0f9ec2-5940-34d7-bbc9-0a4936691fe3 | -13.73122 | -47.95953 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a39d484a-c737-3212-ac5c-0d347c6d4636 | -16.38002 | -52.16232 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0a8de3b8-4529-3486-a87f-eca28ec9f934 | -13.15858 | -50.88927 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 894a4b4c-7e8b-351b-958f-b61c50f39652 | -13.03155 | -44.88448 | 2025-10-05 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7cef16b-8399-3379-9d19-3c4225a83cea | -11.8712 | -44.96331 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6be4d8e5-06e7-3909-926d-a67ec4f3f5d2 | -15.23153 | -49.29855 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19b5f813-9e5e-3007-815c-6ef4e7b575b0 | -13.30902 | -48.08623 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb3df0d0-5128-364e-ab72-c1fedb020289 | -13.73812 | -48.06678 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ea16c8a-9c5c-3779-bf0d-0957db9f8b5a | -15.54021 | -46.81605 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3bf9008-be90-38f3-a291-41c8cc6644d4 | -13.29796 | -48.12101 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41ed92a3-ba51-33a0-a80e-f9db8739772f | -14.33424 | -47.66728 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c8b2bd2-2ce5-35d0-bc28-dbdf7e9706ce | -15.34131 | -47.34027 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15611fb1-9503-32f2-af41-4ce8c86fec36 | -12.97674 | -51.03846 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| db2710ca-b412-3925-b0b3-d38757c9caf3 | -15.17108 | -43.62657 | 2025-10-05 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 872a871a-ca47-3077-b32a-3cb9dd674946 | -11.82886 | -45.08121 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2264feca-fbb0-3935-8ab6-379748584dad | -10.72743 | -47.8783 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 073ba26f-50b6-3c52-b451-40a5d83068ee | -12.98178 | -51.04433 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1d85dea8-6f44-3ce9-b050-b41c1ce824f3 | -15.14048 | -45.74937 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7f2161c2-b8ed-33f1-9027-77e393946544 | -15.59647 | -52.51907 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cfba5ca-93c0-382c-8671-20eb7cdbe7d0 | -13.28179 | -47.17857 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4cf4880b-b344-390c-a3e4-d4e207a3002e | -14.66838 | -48.36425 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8ec7a561-ff0c-331b-b265-cdec7e31b299 | -15.29984 | -46.30931 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7bb6aa8-6b7e-3829-9d6c-1f58540797c1 | -10.9999 | -46.52451 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8fc03ed3-718d-356b-b7d6-0368b73a55e3 | -13.14962 | -50.93373 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 501cff48-e042-3d35-b46c-164596cf8c13 | -13.48019 | -47.22793 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9846cb78-08a4-333a-b7e9-4fe6a03480aa | -13.81755 | -43.17935 | 2025-10-05 03:55:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 87f938ab-36e5-320b-8375-b2d3fbe7a982 | -10.83894 | -47.97502 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6a5bea8d-78f1-31a8-bcb8-ef16b311fc2b | -13.08612 | -47.95481 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 887dbdfe-8893-3051-bf84-6887481b97a7 | -13.78822 | -47.83587 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90802833-8594-3fa4-acb7-46f808fc8cdc | -14.75414 | -54.6575 | 2025-10-05 03:55:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c767cb23-a34a-315d-8e64-815b6c2e81f7 | -14.69129 | -48.27385 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d77227e2-ba4c-3b4f-9ac7-2736bb221062 | -11.78603 | -47.92361 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05be3829-3cfb-3e13-a272-2c8307679b0f | -13.0918 | -47.92456 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4d87905-caef-36ac-80de-534c545644db | -13.3249 | -47.17991 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bab86a7-47b7-3c77-858b-132aca87ab30 | -13.27763 | -47.58947 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cbf79c70-0a3e-3ce2-900c-0cce5c328021 | -15.9788 | -50.91533 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c841155-7489-3ad2-836e-27268305e2d0 | -11.81575 | -45.08258 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aade2c10-6dd3-3944-a595-87a2ccccb2b5 | -17.34166 | -46.83156 | 2025-10-05 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e72beb6-8e1a-3903-9dc4-8746e7f0ec51 | -13.44742 | -47.27289 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 73af0ffa-d156-33b3-9f6e-abe55bbedf0b | -11.09638 | -47.74551 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7624d13b-0726-30b6-bb91-115792e1db0b | -13.28637 | -47.62432 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0cbc24fa-9a58-39b3-9297-f02324471751 | -11.82868 | -45.05833 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e20c288-44cf-31f0-8361-27f4082f2755 | -14.41552 | -46.17529 | 2025-10-05 03:55:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f193b631-5e18-3cb2-88ae-c1eeb4d64426 | -11.80269 | -46.84141 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6173b78-17d7-3800-87f8-4f76b12e359f | -13.34832 | -47.58229 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 740f1851-2c62-3c26-82e9-2b5fd46e78cd | -13.10078 | -47.87688 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a59902da-fc09-3811-9241-0d7af7c06bbb | -10.79441 | -51.00349 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bb27aeef-938c-3b5d-8f26-6bd326367ebc | -16.34533 | -51.46801 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 452463cc-8a46-3716-bfb4-3c9f1f93934e | -15.54508 | -46.83819 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8561fd06-2b6c-3cdd-be11-635e3b9ad203 | -11.07118 | -47.87793 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5a9b7c9-674b-3d5c-84ae-e37afc31052f | -18.53888 | -43.94523 | 2025-10-05 03:55:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14bcbb4f-d144-376e-bb45-1bd35a000e92 | -12.39593 | -51.11357 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6908acb-0f18-3dc0-8cf7-a65049544c51 | -14.82841 | -47.22578 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18f00e0b-c37c-30d6-8325-7177babec6cd | -15.23044 | -49.2982 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91ea7fa3-0126-3db6-99db-8a835af03ff1 | -11.81985 | -45.05979 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c03456bf-b815-30ab-8cb9-9c2d64a05479 | -18.33236 | -45.89147 | 2025-10-05 03:55:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2a4445ef-3bab-353d-8e3e-d904e2274af3 | -16.94267 | -52.68127 | 2025-10-05 03:55:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7fa33ea-3958-3c9c-a4ca-6ee05f8f4c5b | -13.34176 | -47.19278 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1653cd65-4250-386e-927b-2901aa9ce1fe | -16.53569 | -47.77453 | 2025-10-05 03:55:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c0ee70d-33be-3d6e-bc5d-7adbb8101045 | -16.35287 | -51.46106 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 028b3739-7cf9-389b-87c6-55f4ec65d5d1 | -12.89082 | -47.30988 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0256597-9a8b-3d8e-9a06-de221abe240d | -13.18052 | -44.48355 | 2025-10-05 03:55:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca4bf0c8-6293-3498-8114-87574320ca6f | -15.85204 | -46.26802 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de7a006d-a6e9-3401-8d79-5853e72f6de7 | -13.10415 | -47.94005 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6cc7ca2-2939-393e-9153-8913b9b1338a | -12.86446 | -46.8633 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 070ed846-ccc1-38dc-9a46-9b5feadc4743 | -15.16049 | -44.07377 | 2025-10-05 03:55:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 408c538e-9dea-3341-91a3-405a269e413b | -13.17663 | -50.87706 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97fa9fe2-4dea-3a98-b9bc-fcf43ae437ee | -15.71614 | -46.25018 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7c4e405-48c8-3f86-aa50-d307c02fe082 | -13.45127 | -47.26659 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3df20c9e-72e6-36a4-b817-f13b086a7460 | -16.41228 | -43.74754 | 2025-10-05 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acb614d7-ec11-35e2-94c2-e1ac54a3b89c | -18.00295 | -45.00514 | 2025-10-05 03:55:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc9603ea-e021-3edd-b18f-19ee6ad24472 | -14.68266 | -48.29194 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 49d8f49d-75b2-393d-ac5f-0b90fbd69553 | -11.68575 | -47.48695 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 836a0eac-3044-3260-9041-35dd414bb758 | -14.66705 | -48.37102 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3c88f2f5-179d-3af2-8c9f-e62e628d5995 | -10.46024 | -47.80995 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d51948f1-97ae-3313-ae8b-af5b178875a5 | -12.39175 | -51.10277 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 407174b6-3a84-34ad-bc98-9b8a742e4c76 | -12.1081 | -45.14356 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a87de1de-24fe-30ae-8391-7b764ae2a34c | -13.30633 | -47.56905 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ba851b2-bb53-37e6-a1bc-40f263313709 | -12.81746 | -46.86056 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8887b7ee-9d7e-37cc-8093-4060b156071b | -17.24671 | -46.80423 | 2025-10-05 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e87df56d-7cd4-3d6a-bb63-89d339149555 | -10.50084 | -48.11219 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44ae1095-59f7-3ac0-b9af-8e52918ab794 | -14.61779 | -48.11942 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0574fc1b-941c-30e6-891d-897f11825636 | -13.23797 | -47.81949 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e97ec176-7c10-3330-a869-5dd3519b8172 | -15.59782 | -52.51279 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fccabd18-9401-396b-9b99-e8b2e3c68290 | -12.45503 | -44.64249 | 2025-10-05 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f36a20d6-3aec-3e35-bfcf-547063db86cf | -13.24743 | -47.23216 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0381c69e-ddef-3f26-b61b-97df8ebccc2b | -16.34025 | -51.46351 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a7f03bc3-49eb-3e01-ac12-e2eaaefbedc2 | -11.7157 | -45.34929 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README57.md)
