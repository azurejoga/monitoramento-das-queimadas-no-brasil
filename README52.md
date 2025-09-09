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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c292de2a-c3fa-3b29-b27c-f74f0d87b4ab | -15.06643 | -50.12634 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 147651a1-5a7b-333d-bfdf-1aa426e91aaa | -15.27537 | -52.35744 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc8b33e5-9e86-3831-bf85-973ec9932104 | -14.52582 | -53.9653 | 2025-09-09 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f4f9c13-ae9d-3f56-9501-941e1f130e80 | -15.76899 | -53.58571 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5c0c414-3742-30b3-94b9-c77820b1c21c | -16.06948 | -50.47671 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b79390c-34dc-3bb7-8bf8-1069ce1fafee | -14.53877 | -48.74454 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6143b2e-5f3c-33a2-9733-afd163677d21 | -12.89601 | -62.08604 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 461b0d1e-e94a-3608-bfbb-732363047163 | -15.25182 | -52.34945 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 013ebd01-cf64-3d3d-a122-7c93b6f06854 | -17.08083 | -49.23041 | 2025-09-09 04:36:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 808bf989-cdf4-3faa-ab60-ce417f9f4709 | -14.77198 | -47.20491 | 2025-09-09 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 259aec39-39b8-31cd-b808-2ac6c0edd553 | -16.65242 | -50.18558 | 2025-09-09 04:36:00 | NOAA-21 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23369fdc-f0c4-332b-9710-37027d7d6f9d | -19.83314 | -50.94171 | 2025-09-09 04:36:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4f712120-4da7-314c-bc8c-b3460f1bfe33 | -17.30404 | -46.71395 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7ac19041-1a2b-38e6-b777-7fc520c3fa9e | -17.27742 | -46.74261 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0ecee4c5-2880-324c-9872-cb0c86896133 | -16.89896 | -45.8331 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54230ed6-408f-3dfc-87d2-35f984c71b7e | -16.32243 | -52.92541 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21558b55-ebdc-3445-bc68-978f6483ae6f | -15.11329 | -48.04966 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 834942d5-d8a0-319c-9229-3c33e4a4067d | -16.43244 | -49.29176 | 2025-09-09 04:36:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2818815-7fd9-3646-865d-e4d0f73a0394 | -15.26247 | -53.79865 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41bc3bce-195f-3e86-8073-e6b52f8079c2 | -15.11901 | -48.05835 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0ab776e-3021-38ef-9fff-c1606380d40a | -17.91875 | -51.74562 | 2025-09-09 04:36:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d509b910-6587-3889-a8a6-65a301431398 | -17.72755 | -44.47743 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02c315e1-ea66-38ce-a9fa-7e500fba08e0 | -16.96146 | -45.84841 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9053f718-5887-3073-ab17-dc22d2153fec | -15.52838 | -48.39271 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9bff0c42-1895-396e-bc21-ef9b302aec8c | -17.26878 | -46.7506 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9fb486bb-dc77-308c-8b36-8d3d215fd731 | -18.1536 | -51.83158 | 2025-09-09 04:36:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 667a652f-5256-39bb-b5fb-cbed09e4d5ef | -15.27254 | -53.79931 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b0e5597-d04f-3aa6-bde5-6ed099c933a4 | -18.79217 | -49.65566 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8e32ea4-405d-336e-b42d-8688ca928c48 | -18.1461 | -43.39322 | 2025-09-09 04:36:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cfa57f6-5ceb-3d91-97a5-5f7bcdbf223e | -19.90932 | -43.85448 | 2025-09-09 04:36:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 1fd9983d-f29c-381a-bf45-43b703e1d524 | -18.81954 | -49.67917 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 2705ff74-343d-39cf-a438-80eb28ddb2cf | -16.70088 | -48.63494 | 2025-09-09 04:36:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| de872298-a906-37d1-9b08-1e6e8b59aeb8 | -19.90987 | -43.84974 | 2025-09-09 04:36:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 41fb204e-fb63-3df5-aa4e-e3e03c21fef7 | -18.81786 | -49.66746 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0989d91f-dacd-38c2-9a27-c1eb257c36c3 | -19.54732 | -44.04766 | 2025-09-09 04:36:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 169e1159-c180-3d63-91c8-cfd8f8180e36 | -16.43523 | -49.29593 | 2025-09-09 04:36:00 | NOAA-21 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 674fa8d4-ab0b-3b97-b989-0ff07222e742 | -18.82846 | -49.68829 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| d56739b0-355a-3c5a-b991-aa6a25751499 | -18.46714 | -49.55743 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 315cb1e7-145d-39c3-8c12-29aace14a0b0 | -15.70457 | -49.89636 | 2025-09-09 04:36:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9803753-b89a-3d8d-b925-f3cac39a3629 | -17.67827 | -52.26306 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcfbb4d7-bd58-39e1-8ef6-2dbc6d7634f5 | -19.72556 | -43.91134 | 2025-09-09 04:36:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 447b2a5b-8dee-3c03-9f8f-9f62edfc06d2 | -19.55182 | -44.0484 | 2025-09-09 04:36:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae32ec11-c4ee-3504-8263-c76e76ca7212 | -16.34556 | -52.93772 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f449908c-0dc9-3121-abf8-39d231571b9a | -17.67702 | -52.27064 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3771468b-d738-3a0d-8bd8-708211ac808e | -18.0193 | -47.12729 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f635385f-76f6-3d92-a465-0d1504601f46 | -15.53229 | -48.36635 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1296f7f7-1d05-3b91-9cd0-743b0a85a6f3 | -16.30145 | -45.69276 | 2025-09-09 04:36:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1bff11f-b185-3547-9477-1163d7c848c0 | -15.0986 | -48.07841 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15ea7f7f-0df5-3ca9-a69c-bcaa16f11874 | -18.83794 | -49.6937 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aeaba866-f08a-3382-834f-2d3376f0e992 | -15.70842 | -49.89333 | 2025-09-09 04:36:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 780c7917-8f2b-3f2c-a061-a26cc13289a2 | -13.95154 | -54.02008 | 2025-09-09 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f7320dd-e8d1-3fc1-ae26-3c9294ed174f | -16.4344 | -49.01096 | 2025-09-09 04:36:00 | NOAA-21 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4a433f0-23b3-3152-993a-21e864ecea08 | -15.25801 | -53.8025 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b6f511b-f880-381d-94d1-80731b7ff612 | -14.91903 | -55.8932 | 2025-09-09 04:36:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0789472-c18e-323a-9e1c-97e85640a8a8 | -17.37526 | -49.23523 | 2025-09-09 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c104ff0-1cf8-3b5a-83f7-fd43338e2fbe | -16.8902 | -45.7804 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f0393d9-b79d-3faf-90e8-4acae909c6ce | -15.2706 | -52.3648 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43a2294c-9a5f-397e-9276-22db7478a639 | -15.26965 | -53.79409 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b841f567-8ee1-3751-be63-7c114a89bd40 | -18.82957 | -49.68087 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 273a33d0-41be-3eb7-b184-b9e8f17a6d1f | -17.97975 | -47.11603 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd2461e3-5cc4-321c-90dc-ee04e195e60e | -15.70126 | -49.89582 | 2025-09-09 04:36:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3d16ff6-a58e-38c8-98b4-68c99b0f00e7 | -15.75627 | -53.53004 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 596dd80a-e632-3cc0-80b0-775837765c49 | -17.29049 | -46.70227 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a998145-a288-30e3-b313-0c8a1b420727 | -19.41472 | -46.52011 | 2025-09-09 04:36:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 62cf48e9-472d-311d-8364-17d918d4a1b7 | -15.2562 | -53.80562 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba2c2b47-ab49-316e-8ed3-12ce36cb4a0b | -15.26092 | -53.80774 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c133819a-185a-383e-83df-67c7f97882e5 | -15.53343 | -48.38207 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ae29c73f-f864-3923-bfb1-ee3d5ffc2817 | -14.53932 | -48.74089 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f40aea7-e6f6-39ab-a1e8-a1356363d34e | -14.37386 | -60.2986 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e59dde09-cd41-3b37-ac15-3b424946c362 | -16.9846 | -45.88247 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c65264b3-2208-3a18-9f22-b20c2040d7cf | -18.76548 | -47.09955 | 2025-09-09 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e79b7384-fe2e-3fc1-a1bb-0f64bfc95566 | -14.5538 | -48.75816 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29d8213d-a6e5-3807-8daf-acc5b427d5b7 | -15.25278 | -53.81085 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06ff5125-09f6-350a-bee6-359513cb8d6c | -16.34487 | -52.94181 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5578f7b-7a66-3c9e-ad11-2d5346afa93f | -17.40209 | -49.3079 | 2025-09-09 04:36:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5909a9c8-c7d3-3aa0-8066-a0ca30729e22 | -15.54529 | -48.37235 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 75aba486-e7a1-3d96-b317-8d405a4d8e75 | -18.01623 | -47.12247 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84e7d636-e888-3990-8019-32131b274ad5 | -14.70414 | -60.26022 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f04c164-2daa-3b20-9997-b11863691d95 | -18.78714 | -49.6434 | 2025-09-09 04:36:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a998a2a-9b35-3346-aea1-5458b1af47da | -15.77871 | -56.41577 | 2025-09-09 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f24c3d4d-29a5-36ba-bb79-26e673d014c1 | -19.47846 | -46.12991 | 2025-09-09 04:36:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a863a42b-df74-3554-8187-fc4d224e1d7f | -12.87984 | -62.09813 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e42da4c-38c0-331b-b27e-9c86296acaae | -16.08432 | -50.4902 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22e5426e-3192-3aef-a841-c2beb0e320c5 | -14.79505 | -48.18774 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07be17e3-720b-3443-8674-dc0d3d77e99a | -15.78083 | -53.53891 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 875aca32-6739-348a-af7b-bfb56d55e8c3 | -16.2882 | -45.6818 | 2025-09-09 04:36:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ed631c0-b58b-3a35-9823-22f1ebeaf963 | -16.32944 | -52.92656 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e262a62f-00ee-3513-9e27-f814d0f674f0 | -18.04697 | -47.08981 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6178ac36-ca3a-3fa1-8703-7b71c77b895d | -20.17582 | -44.79643 | 2025-09-09 04:36:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d8f4d12d-71f2-3d8c-a283-94dea7ff447e | -15.78447 | -53.53946 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d2e9f0d-99ab-3ab0-b10b-ec54dec3c2de | -15.2454 | -53.80947 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff815bd1-030c-3330-a903-215052e73558 | -19.73566 | -43.90999 | 2025-09-09 04:36:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63784d69-f4b7-3825-85aa-d412300ca59c | -15.26068 | -53.80178 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 389f2899-6930-38d0-a556-b5fd562b74c7 | -15.26357 | -53.80701 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 331b5add-8616-3b9e-859b-0498cfa4d4c3 | -15.78287 | -53.57031 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7225d282-f724-339e-bdc0-31bfc684fcaf | -15.24345 | -53.77648 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f381552-9a8a-3c8f-bfd8-0124ed3698ed | -16.28754 | -45.68682 | 2025-09-09 04:36:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e67ec551-5446-3851-a268-fcd07e2028c3 | -15.25988 | -53.80631 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ab81dec-1f07-3273-a622-5e5d8f2668c5 | -16.43299 | -49.28811 | 2025-09-09 04:36:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f636c44e-f94f-3087-a755-33530cf2fa44 | -15.10709 | -48.06815 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README53.md)
