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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8844f93-d4d1-3645-ac9c-567cb301db93 | -11.00237 | -47.9052 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 222c0461-f3f9-34e4-a3f8-e0d73b708e5e | -13.45398 | -47.93201 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b0048cd-bdd7-331e-8ef1-0477dd63175c | -11.94394 | -44.23901 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b33834d-2bb5-389e-b7af-03b5ab11fa00 | -11.64259 | -47.85719 | 2025-10-18 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98f3eae3-b20d-3cb9-b2b4-fc4aa94e961e | -11.48817 | -44.27752 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38f6f6c4-6b82-3e14-8dd3-a05befe53f88 | -12.71066 | -45.8493 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd1b304c-65e7-3110-9bb3-01234dd3a831 | -13.777 | -48.24072 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a7ea5df-7a08-332a-9fc2-b2b94ef20e13 | -15.79966 | -43.56592 | 2025-10-18 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fa1bffa-3677-3326-a764-0e372ca59139 | -11.59678 | -44.06733 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f6cc290-33d1-378b-8108-8f6200a7f93e | -10.96415 | -47.86626 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e99bd867-a618-3cc2-abe4-df20e8a75f03 | -13.70765 | -40.98573 | 2025-10-18 04:32:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9c68eada-037f-3082-a4dd-41e0982182e6 | -13.27312 | -46.43984 | 2025-10-18 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52923377-2edf-3736-9083-171128a6e6e2 | -15.54671 | -47.27843 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 595ce4ab-a4ff-3675-9dad-b74c98dc1030 | -14.85963 | -52.44167 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7965dd86-0a60-3150-8884-ac5e42567a1f | -11.51943 | -44.06681 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f763dca4-cc2c-3604-9905-6879a58037ae | -15.80104 | -43.56743 | 2025-10-18 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7bffca80-29b0-33f3-89ff-243fbc8fbb79 | -16.46799 | -43.04374 | 2025-10-18 04:32:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58c51985-08bd-30df-9072-da31cd1a8261 | -13.04526 | -48.18872 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a31394d3-44e7-3d27-b71e-394b71420331 | -12.3944 | -47.20768 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef1c0794-1bc4-3bda-b62c-c7a0240fce6d | -15.92664 | -45.69593 | 2025-10-18 04:32:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 114fcfd5-591d-3dc4-b20f-edd40b068a98 | -12.36445 | -44.08096 | 2025-10-18 04:32:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 085238c1-ad89-3c28-aef7-145e75d3fc14 | -15.78799 | -43.65024 | 2025-10-18 04:32:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60a77633-9fff-3574-b96a-c113d32956bb | -13.35511 | -47.26716 | 2025-10-18 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77d3fac6-d657-3a59-bab7-fea6e7cd95c9 | -13.75974 | -43.81114 | 2025-10-18 04:32:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72cfa740-65b4-398a-b812-855171b91e19 | -11.4961 | -44.17386 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09aaf905-0f51-3878-b27d-b773fcc03297 | -12.70315 | -48.63011 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79f2661c-7a81-3992-b4b7-df6e5cf3b6d9 | -10.92929 | -47.55745 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3514b870-b7d7-35ab-b8d5-fbf08341ca69 | -13.47798 | -48.12538 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da78e92d-5802-3078-bdb7-65d26b8b152c | -13.75846 | -48.12095 | 2025-10-18 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0bbaee35-e999-390e-9629-d2a4c410fc41 | -11.40164 | -44.08199 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19b7efd3-386a-33c5-b298-f7eb7f6488ff | -12.17809 | -45.0754 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e99e9da3-2b97-329d-a32a-ffcc4a8c7af4 | -12.48337 | -45.46227 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db76c130-22e4-3c21-bbf4-f85b5d817f05 | -12.15281 | -45.07569 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 74c1660d-ce90-350e-9d91-dfd49bc2f79b | -13.44195 | -48.11576 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b597aa2-97b8-3994-91b7-f2230c95cd18 | -13.51097 | -48.00333 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9492f00-b1e2-3b79-82fd-5c23f6adf864 | -11.49784 | -44.1873 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f7be7cb-8c51-3400-9a5f-c0237f0cf905 | -14.43239 | -52.89923 | 2025-10-18 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3167b12b-129e-3362-999b-f77bf72f50dc | -14.90763 | -52.39202 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e8f91f5-3fce-35a7-92d7-7dc48ef55eda | -13.04374 | -46.9526 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d1ab885-a3e5-3ad3-ba37-a25ab3d7c0c7 | -12.74723 | -48.63383 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa13f6ff-3fad-3683-a0ac-371832f292de | -16.24103 | -43.50895 | 2025-10-18 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f947f86-7d53-339a-929f-17843162b0fa | -11.48324 | -44.18509 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62b65a6a-a907-32e9-9315-832b8128c634 | -17.72721 | -44.36019 | 2025-10-18 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f81ee4c-f04b-36b6-9396-982b204dbc07 | -13.18319 | -46.43367 | 2025-10-18 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d649e2f1-ddc0-38c2-8be0-4d04a58b2b5d | -12.36438 | -47.18097 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eb8bd4f-435c-38b4-ba09-708faa307789 | -13.77643 | -48.24428 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dd340886-b968-3929-97e8-2da5c0ca36b8 | -11.36032 | -44.28584 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3f8d6d5-6654-3e79-afa3-9f9f97784ebe | -14.93249 | -46.7177 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75a2bfdb-69e7-3f33-b4e7-3f191d62216f | -12.4683 | -45.46785 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 0cc48510-d388-3cda-856a-56e45d0eb1d1 | -13.76539 | -48.22786 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 856d41c0-b09e-3a06-8311-66084739df0a | -17.4927 | -43.46603 | 2025-10-18 04:32:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3eb7d288-73f0-30a6-9cc5-74ed77c9f86d | -12.91628 | -48.5876 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 09e6aa6f-222c-3e65-aeab-d6bc0b005d0c | -16.53359 | -43.67352 | 2025-10-18 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82430355-dbfa-33f9-8433-aab0e2070c77 | -10.62556 | -48.0178 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50383b14-151f-3280-a8e2-95d8727fc832 | -13.00503 | -43.8533 | 2025-10-18 04:32:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05b7cf4a-4e86-3ba3-bcc8-c1fbf11c79eb | -15.05223 | -46.60967 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90ffca4c-d986-331b-97af-c9ed8797f5ea | -13.53205 | -47.99953 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e022d7c-f3e6-365d-a20d-aa0c517695b8 | -11.48943 | -44.16846 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdaef60b-51e8-3d4a-9a9b-cb71d3d84bc7 | -15.06919 | -41.97591 | 2025-10-18 04:32:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2da386c3-c9fc-3592-9539-8724c5a6f9b2 | -11.61563 | -44.09241 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b9bde417-af8a-3ad4-aec3-4cd1a3bf1db1 | -17.84692 | -42.62246 | 2025-10-18 04:32:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4d51fa6e-c2c5-359e-bf1d-343037a63892 | -14.91337 | -46.72993 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 425d39bd-699d-3920-8d6b-fc2a4eaa35d7 | -11.60589 | -44.08204 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c769808b-5640-3726-839f-9ab18def4d9e | -13.41333 | -47.91134 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f386b6d-09a1-3708-b667-f6fd7bc3d4ed | -15.58218 | -44.51266 | 2025-10-18 04:32:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc88eacb-fc7d-3ea6-9edb-757641e15899 | -11.24706 | -45.31554 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b367566d-d086-3e45-800d-75685231e3e9 | -14.50498 | -45.611 | 2025-10-18 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88aac572-37e3-363b-9a33-d50882050646 | -13.24521 | -48.55847 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7d26f2f-1954-3b2b-8abf-6fdb32600466 | -13.51762 | -48.00443 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9df86850-a2ed-3960-83a4-86845f42e3f1 | -12.97458 | -47.11077 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f3c818c-ef62-3c23-8abb-6d228e00c37f | -12.36227 | -47.18105 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd9012ed-cea9-3d19-b9c0-00878f23e1c9 | -11.4858 | -44.26846 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c438a249-7039-3e11-ac77-c7217d8cb2d5 | -12.78796 | -48.62531 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d6c20c6-731c-3919-8c7d-de1340911697 | -15.0591 | -48.75004 | 2025-10-18 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9257f2b4-7800-3bfa-b548-94b16014871a | -14.09465 | -43.63658 | 2025-10-18 04:32:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 91a62e28-eb5a-3098-a859-5a6f2839a313 | -11.83055 | -45.13818 | 2025-10-18 04:32:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc04ce16-d6cd-3fdc-b108-0bccbd12b92d | -12.80061 | -48.6533 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75b02336-cf1e-3cae-84d1-8b4338f4fd89 | -12.96954 | -47.93972 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d509c79c-f1bb-38e8-b0aa-c2667c293eb2 | -13.5121 | -47.99623 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c0adadf-4d60-3c04-a035-af15ad7accc6 | -13.76369 | -48.23852 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94db1851-c628-3b4f-bb21-c5b48e293a42 | -13.03871 | -46.94075 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b4e3d31-86ca-3830-94f1-1417e6ceb466 | -17.72778 | -44.3589 | 2025-10-18 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c22c2eb-9ec5-3351-bc95-ac325ea7720f | -11.60413 | -44.06842 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1e047821-0665-39ae-b7e7-70c807052cd4 | -12.46017 | -45.47457 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfe51f48-71af-3a4d-823a-197478ab7518 | -12.97402 | -47.11439 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6de4fdc0-e7bd-32d3-983d-7c55d5f66f95 | -11.34779 | -44.24493 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0521ef63-ac22-3b12-b186-4675e12b8075 | -14.90825 | -46.76353 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9a73257-fa0f-3f2c-9edf-acf51e074c31 | -12.43116 | -47.79413 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2f564cb-2f19-3638-8f17-ed237f4df2da | -11.51272 | -44.06136 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04da91e6-f34f-3bd6-8787-8b156f1e6eb1 | -13.77254 | -48.24728 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b195c4a9-eda4-3f32-a835-ea449794811c | -12.49431 | -45.50771 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 379469d0-85c3-3585-876a-2691159383b1 | -13.02994 | -47.27286 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 084365ea-cca7-32ba-8bab-94378434bf57 | -13.76645 | -48.24262 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f721d708-4e3d-3de5-a61b-b730fd609e35 | -11.60286 | -44.07713 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df7240a7-0407-3f9f-b0a7-20fcafefa64d | -15.08736 | -44.00386 | 2025-10-18 04:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86cbfb81-ad48-3560-8d3e-672657b804c6 | -10.62891 | -48.01832 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e76bb6a-38e5-33b0-90e0-6941c05b1dd3 | -14.01636 | -44.67989 | 2025-10-18 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bb2b1a7-f5b5-3af1-93cd-92d04b1dfa27 | -11.38586 | -44.26371 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bb19649-26bf-3051-96a3-021e356b659b | -11.60525 | -44.0864 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 487d5296-221e-37af-b63f-560446cd2dcf | -13.75172 | -49.80091 | 2025-10-18 04:32:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README60.md)
