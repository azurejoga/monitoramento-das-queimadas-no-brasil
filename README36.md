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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ba71ae5-3936-34fe-9422-ee28c30d993a | -13.03192 | -45.20766 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f138a07-5d1e-3776-a062-0736cea028b4 | -19.6737 | -48.99657 | 2025-08-22 04:21:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d1caa1e-db63-3da7-8a37-ed66be6d977e | -14.59317 | -54.7837 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b36b3fdd-90c9-3616-bfba-8db3857b16ec | -15.65769 | -52.68766 | 2025-08-22 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbeadf99-6817-3d4c-9d46-a16a0fcab7f8 | -13.00017 | -45.21369 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c54c50c-6171-3948-a3c6-96bdda7f13fd | -20.26541 | -46.68989 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2f7886e-f4e9-3fd8-988e-799a769ccfe7 | -13.03075 | -45.17051 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7577e92a-10a6-34e7-9220-18031a4f3d21 | -19.93626 | -44.57308 | 2025-08-22 04:21:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 9adc1d55-1263-3926-aa89-b251191fb527 | -13.46187 | -47.05794 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a3a3c96-6e3d-3c6c-bc0d-019a545085fa | -19.56316 | -44.02929 | 2025-08-22 04:21:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65fc52e4-e7aa-3641-a799-13032605bda5 | -11.90115 | -55.89476 | 2025-08-22 04:21:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9f16b56-65a5-3511-9d7f-0de49e6c06a8 | -14.58778 | -54.84835 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72ea88d7-c84d-3091-ada0-0392f817938d | -13.83363 | -44.46392 | 2025-08-22 04:21:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42eb1495-1e1e-3922-827f-0d6bb232ab9d | -15.5027 | -48.05309 | 2025-08-22 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c98830e7-4b71-3b39-86bc-28615db04b3f | -17.80838 | -44.30861 | 2025-08-22 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95035597-3f7b-3a2b-9b4e-b2c3ff249987 | -13.16919 | -46.91019 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc3c7fb7-8670-3433-a1ee-6462e4ecc1df | -14.32728 | -53.10141 | 2025-08-22 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d786546-207b-3b18-9b1c-c56a968f28fb | -16.48192 | -45.08972 | 2025-08-22 04:21:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e190ef6-d43b-379f-97e0-8fd63bd6e32a | -20.08262 | -46.12611 | 2025-08-22 04:21:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 463ae68b-b496-3c4d-b3f4-df5ed1fa6573 | -17.23261 | -46.78988 | 2025-08-22 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7c7ca8e-f2c5-3441-a87b-de43bd5dff16 | -12.99907 | -45.2209 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc082a1b-0593-3670-ba88-1fd64756819f | -13.15306 | -46.88546 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d492f09-1c84-32f7-afaf-969d623a58c7 | -13.18461 | -54.96042 | 2025-08-22 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8c7104d-e030-37c5-b9c5-176d65b3d477 | -17.91683 | -44.48671 | 2025-08-22 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9560033-50c4-3ddd-bc4e-db4047e82dd0 | -12.98964 | -45.23783 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 389606e7-eb26-3003-9608-8dae76b687f6 | -12.93481 | -46.18291 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 58ce5681-2289-3abf-88c0-e470701771fa | -13.03357 | -45.19684 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca2a7e6e-7e25-385a-8b25-c38c8f4e2d0e | -14.45366 | -48.47474 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b28c7fe1-5ca9-3acb-923e-6f12ea06c99f | -14.82994 | -47.93113 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51c2639c-bf71-3839-80e4-12112db652da | -18.51532 | -42.83019 | 2025-08-22 04:21:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ecce6ca2-d5bd-34b3-89f2-0335c17600c1 | -13.3663 | -46.26771 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49a248e6-af73-3d7d-ac0d-2f34f0561f58 | -14.61992 | -54.86584 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7da5c85c-377c-3169-8f21-6176b072698c | -13.37854 | -46.27714 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ecea5da2-8db2-3e05-8d86-0ceed17bcfe0 | -14.78684 | -59.65278 | 2025-08-22 04:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84b27e8f-7418-3e77-9895-d7f3c460da7a | -14.76721 | -45.39481 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03e9e639-180a-3df6-b29b-da76a25d190e | -14.97561 | -54.53645 | 2025-08-22 04:21:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a8a2913-ca55-3e27-aec1-5f739d1bbb02 | -12.99687 | -45.23531 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 811f69ad-f186-3042-81ea-4024b83126a9 | -13.39403 | -46.22174 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e03071c-0589-3497-b1f2-e379d7814637 | -20.3047 | -46.63446 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38378512-e569-3fc0-bb8e-a0372d7a9659 | -14.86674 | -47.97156 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae68b153-eaa7-30dc-ab48-97595a117385 | -20.24813 | -46.65601 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28a004f4-c482-3f26-9e85-27de604cbebb | -12.95136 | -46.27264 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28bb3335-c0a9-33aa-a32e-4f8b1c2d9139 | -15.0267 | -54.86684 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3a1825a-632c-3bb9-b305-57af90f798d6 | -20.30581 | -46.62703 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a490424-aa1d-310f-937e-dc163fe9091c | -13.90526 | -43.8866 | 2025-08-22 04:21:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99cb02cf-d972-3044-91ca-74b3316c4f1e | -13.03078 | -45.1927 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03823691-e7c6-37ec-8d13-737aa77081ca | -13.63919 | -46.88226 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f99f6897-0672-3172-872c-5ebe1f4a14b2 | -14.76219 | -45.42778 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5992e67a-0b6c-365d-9b76-6f4210761df7 | -13.36685 | -46.26418 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a3e0ffa-5849-3bd2-b23c-b6b0578a5222 | -15.19911 | -48.70012 | 2025-08-22 04:21:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b4d9e97-7c19-349c-b2ec-a19e3743b3b6 | -12.99962 | -45.21729 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6eaaf34b-ad12-3f75-817b-cae01311d201 | -18.75084 | -43.84807 | 2025-08-22 04:21:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09c4144d-0b61-3804-b826-67e71d047d2a | -12.98842 | -45.23055 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1843471f-73bc-373a-802f-dbaf82339ecb | -15.55742 | -50.32358 | 2025-08-22 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55be44b3-221b-3a30-a296-4fe41b6545b8 | -13.0196 | -45.17614 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83940da3-042b-35dc-8df5-24550138533c | -14.89383 | -48.05918 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d22ae04-b505-31da-b4e3-9914c96510b2 | -14.46445 | -48.47315 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 781ba32a-1ab4-345b-a123-c2786293f20b | -13.14575 | -46.91012 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7d48655-7853-33e5-9043-0e47fcd2da81 | -18.89009 | -48.25045 | 2025-08-22 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 88c221a2-bdf6-3971-b7e1-7c3b6ea02753 | -14.91595 | -49.45568 | 2025-08-22 04:21:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7d05393-76fd-349f-80cc-026102b39251 | -13.02015 | -45.17253 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4742ea3-d548-3324-9abf-32c0965559de | -14.97367 | -47.14157 | 2025-08-22 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc1347dc-84da-368a-b899-09b4d1bda70f | -13.50145 | -47.06411 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8926436-035c-30ad-9236-74cfb33c471b | -19.30028 | -48.92668 | 2025-08-22 04:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 175a4271-4d86-3765-9338-1752fd04772f | -18.88335 | -45.01823 | 2025-08-22 04:21:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 85219aac-9384-3e68-a10e-4d22b726a992 | -15.56755 | -50.33007 | 2025-08-22 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e3388af-139a-34f9-83df-a6e2f801f241 | -19.71684 | -48.97738 | 2025-08-22 04:21:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45ed6513-31fd-3b91-9e6f-f58b1915ff17 | -14.85455 | -47.96185 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0212c8ea-2676-354c-9c2f-c3555b3e42f9 | -18.94191 | -48.35001 | 2025-08-22 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01409ae3-6103-3661-a9b7-7119123079da | -20.27276 | -46.57063 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af317d66-a7e9-3e36-8c3d-40492dd0a0f7 | -15.00607 | -54.8692 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25225d04-b338-3b9a-8fba-938ab32f7073 | -14.75814 | -45.22701 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 614106b0-ece8-35e4-8cc3-653a96b26ab7 | -13.6536 | -45.71083 | 2025-08-22 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 523a8b40-1d73-3f3b-96e0-a829488eba56 | -12.51131 | -57.66164 | 2025-08-22 04:21:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20e0274b-9891-398f-a18d-08f5a8ff2f8a | -13.0213 | -45.18749 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cf16f0c-b75b-38ba-aa0d-963ea582f2c2 | -12.98305 | -56.88726 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ed8acbe-08bd-3d66-b8fe-2e6ec98eedd2 | -14.63041 | -54.83809 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d866ebf5-3c08-394e-980a-0fb90b92c85f | -13.43588 | -57.17236 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f1e3eca-e767-3e89-aa8e-fbaccd29de9d | -18.11153 | -43.97663 | 2025-08-22 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 823e71fb-5772-32a2-ae28-e7a435677117 | -14.46279 | -48.35677 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f46a11fb-6273-3001-b3a6-0e416a909314 | -18.66142 | -46.98565 | 2025-08-22 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cffebbb6-468c-3265-966f-9ae2cb34a542 | -13.14415 | -46.89873 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 027df8fa-a900-3c7a-b268-8a9e8b78e97e | -14.88378 | -47.95168 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 467f6410-0082-3644-a155-d1e33475e7bb | -13.48828 | -47.0399 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f17fb51c-7284-3da9-a6b4-be890098df8d | -14.5166 | -47.85218 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3cec08d-f19e-3573-86e3-9161ed5ec4af | -12.99632 | -45.2389 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a73d4258-d943-3bd4-a692-bd84244a18c2 | -12.92104 | -46.16259 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1ffa067-0bbd-3ec7-abff-bd5e5a9d0ae8 | -14.3515 | -51.96237 | 2025-08-22 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c5869ff-6a4e-30a8-b15d-614f8c696d0f | -13.6425 | -46.88281 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b6d81fd-248a-3240-bbaf-394e0a9b5670 | -13.29941 | -46.39079 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ae9174a-26d9-3fd2-885d-195c1454b862 | -14.60581 | -54.83416 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a5dd0e3-bcd5-3123-bfd7-b54ac6c8e646 | -20.23076 | -46.61089 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b0de99a9-93aa-31d4-bb64-0a224b100519 | -12.95356 | -46.28024 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2b2e88e-56a5-3e0c-96ae-d0cba22cb204 | -18.87925 | -45.02184 | 2025-08-22 04:21:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 35.0 |
| a5009e8d-13ce-3c87-af3d-80fe06b2dc0e | -12.95194 | -46.24741 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 603e4b0b-6cf6-337e-be3e-15134efca2bc | -17.61031 | -46.69555 | 2025-08-22 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42858a87-62dc-34b7-a679-087107413645 | -14.76834 | -45.41 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b1b903ed-2cad-3210-8883-95047c1ffc4e | -12.49635 | -53.81049 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d299c3c1-ab81-340f-9282-845151896a4a | -20.30808 | -46.61182 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4df8a875-d83b-364e-bf64-3829cf0d2172 | -15.155 | -47.96052 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README37.md)
