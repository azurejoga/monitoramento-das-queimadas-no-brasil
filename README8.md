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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d4f464c-79b0-35d3-a5c9-1fc359940fe1 | -11.72963 | -44.20947 | 2025-09-13 00:50:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 740dd7a4-f006-304f-834d-28a84b68609d | -14.19438 | -46.25208 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 3ade9642-2bce-3945-88fc-bc41ba17d2e4 | -17.24281 | -50.23384 | 2025-09-13 00:50:00 | TERRA_M-M | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8214134e-2988-308d-857b-0b295d55519f | -11.23165 | -55.00348 | 2025-09-13 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5d4bbbb9-76c7-367b-ac69-1b959262a88f | -14.2037 | -46.26093 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 07e6d850-ad2c-3b6a-b3ff-d32b896d5fdf | -10.45704 | -50.0136 | 2025-09-13 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| a0f705b7-2f62-3bc5-9e20-c71adc5d94b8 | -14.21521 | -46.25755 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 222.0 |
| 1810c63d-6a14-30b5-a4e1-507b3e4ef234 | -20.01302 | -47.64655 | 2025-09-13 00:50:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 575d6466-bc8d-386f-ba18-c5801bc23b90 | -11.81143 | -50.55342 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5402be77-5818-3836-892a-9b5479b06e0f | -10.64815 | -46.28217 | 2025-09-13 00:50:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 4b6e54ca-dc76-3b37-8c03-9cc5d03218ad | -13.00537 | -46.75678 | 2025-09-13 00:50:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 116afc96-779d-387d-b44a-995e37c36b9f | -16.64263 | -49.78311 | 2025-09-13 00:50:00 | TERRA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 54456601-5b6a-309d-be02-c6f430515a4c | -15.21651 | -56.69926 | 2025-09-13 00:50:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 91564d12-05b0-3963-8cc9-6e0c1065982d | -17.5386 | -44.55612 | 2025-09-13 00:50:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d435939a-1b70-30e1-9490-5c376a76f7d5 | -15.11373 | -52.48849 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ef3b56e9-3691-355f-8980-063852b091d6 | -10.15609 | -47.90504 | 2025-09-13 00:50:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 17f3ec5b-05ce-3d87-8222-a35dd014affd | -13.4718 | -51.78848 | 2025-09-13 00:50:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1963661e-3079-3763-8f29-1b65d75017b0 | -11.85356 | -49.76943 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 894eff85-8735-3cba-89d2-048e425225c9 | -16.43178 | -49.04555 | 2025-09-13 00:50:00 | TERRA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ddac7abc-8acf-3876-9a64-a02c3897c984 | -17.42859 | -49.22623 | 2025-09-13 00:50:00 | TERRA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 232bc956-c121-333f-9928-b79a88150dc6 | -15.13196 | -52.47961 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 62fe868a-7dc9-3943-a0cb-a708cc5268c1 | -10.69961 | -49.17559 | 2025-09-13 00:50:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| da85f5d5-2947-3340-b16d-db5bcef62b64 | -14.18534 | -46.27094 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 47df2a93-0728-39e8-8b89-8ff6462fbda7 | -14.46318 | -53.40358 | 2025-09-13 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b38aeb66-79ac-3ef9-9777-3699f69ba388 | -17.41173 | -49.23956 | 2025-09-13 00:50:00 | TERRA_M-M | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f769269b-b764-3171-94ca-82812c961538 | -15.78765 | -52.22757 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2f004bd7-2c94-3006-9aa6-28178f573ebf | -11.43876 | -43.57079 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 445ed82f-2f98-32c7-a6bb-324534fa329f | -11.86674 | -46.75772 | 2025-09-13 00:50:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| cc10b03f-3ef6-3173-bf48-98bf2cb74090 | -20.60255 | -50.40499 | 2025-09-13 00:50:00 | TERRA_M-M | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.1 |
| d1280284-c7d0-3a85-9e7c-c9175ac05a07 | -16.5247 | -51.75237 | 2025-09-13 00:50:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8dbee270-dcf1-3cba-a9e5-827576161300 | -11.6144 | -52.21843 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b5020fde-3501-3e9b-b3df-6004784a840b | -15.86495 | -51.85301 | 2025-09-13 00:50:00 | TERRA_M-M | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8219950a-022b-383e-aa7f-798405020264 | -10.7469 | -50.53278 | 2025-09-13 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0d8f8265-e291-3c1a-b455-2b63a491285f | -15.06547 | -52.46735 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 807348e3-747a-3232-bb9f-39b3a7a9a7a6 | -14.18798 | -46.28737 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 75075157-8949-3ef3-a382-40319ce19886 | -20.09145 | -46.90541 | 2025-09-13 00:50:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3b54a75d-b0fd-3af9-9322-aef3f2fd0e8a | -15.14071 | -48.31221 | 2025-09-13 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 76f24b0d-a881-3dc9-9b5f-09ace172dae6 | -11.16866 | -51.41347 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 96edac98-c629-3a84-bc01-c20325c3bcdf | -14.46737 | -47.32688 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3ca45d18-6f90-3b69-a1ea-be46d4fbd95c | -10.86696 | -48.18267 | 2025-09-13 00:50:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ee3003a4-3bf6-31c4-bc92-6f4384a13520 | -17.28325 | -47.25082 | 2025-09-13 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 42.8 |
| bd5a3395-f862-319a-8e64-40ef239912f2 | -15.81303 | -52.2142 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e066f586-8272-3994-8654-cbacb2379099 | -16.41307 | -49.04863 | 2025-09-13 00:50:00 | TERRA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 54d30ae2-d7a7-3b46-a121-a845ed2122b5 | -15.07808 | -52.49361 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 381b3743-9825-3ac3-9bf6-778f24b48d2e | -15.14087 | -52.47836 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 4548a985-3c80-3573-ac86-f109390d25ac | -16.54114 | -51.7405 | 2025-09-13 00:50:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 25ca7f8a-4e4e-3b61-914e-c2daffe233a9 | -17.84026 | -50.41747 | 2025-09-13 00:50:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1a4a7c0b-ad77-380a-9b87-c80dc1c4b06d | -11.14209 | -51.4831 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 356c98dd-2439-3b1e-8432-63c28038d8d2 | -11.16103 | -51.424 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 32bf6d44-54e2-3d6e-a2a5-fe52bf549f29 | -17.83894 | -50.40815 | 2025-09-13 00:50:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2977c3af-f042-39e1-a77f-44998764692e | -13.28256 | -43.786 | 2025-09-13 00:50:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| d91d6804-6c6e-39dc-9309-54078ef6c704 | -12.07013 | -50.94484 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2b20b0b5-9a71-37a7-ac36-076ec27182fa | -18.05027 | -45.44663 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| ba590222-1075-3d30-a14b-be37c24c9356 | -10.90326 | -45.587 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 8ab31aad-d254-31a7-a5c1-1429cac3f30e | -16.50537 | -55.11671 | 2025-09-13 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 54ced04f-5001-32fa-b74c-bdec83eb8d33 | -13.59013 | -44.89703 | 2025-09-13 00:50:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 35cdac32-4519-3bae-ba66-2614ad3dc0cd | -11.07043 | -51.50008 | 2025-09-13 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 48386b8e-779b-3e55-ab32-0c2df40a6959 | -20.65294 | -48.69893 | 2025-09-13 00:50:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3573fded-5b1e-3eb4-9e7d-c1f30aa4d6c2 | -20.61008 | -50.39419 | 2025-09-13 00:50:00 | TERRA_M-M | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 198.9 |
| fcb041c6-23f6-39ad-afe2-f4471bb3d273 | -10.64505 | -46.26299 | 2025-09-13 00:50:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| d45be8d2-f636-3617-bd14-f1bb968e612a | -12.91171 | -54.75234 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 5a62cd07-40c5-3017-85d3-c29f0629cdfa | -18.71014 | -51.78925 | 2025-09-13 00:50:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 35dac400-1c40-36ec-8660-5f684a8effe2 | -17.41469 | -49.25962 | 2025-09-13 00:50:00 | TERRA_M-M | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 44bc6485-73d7-3b43-a8bd-3ad8c1ba3db2 | -19.63968 | -45.08125 | 2025-09-13 00:50:00 | TERRA_M-M | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1be18f0f-0c40-3c05-85fd-6d338fb49214 | -18.7012 | -51.79056 | 2025-09-13 00:50:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8923e1ba-d5bd-349e-8936-129fe144ba81 | -16.49801 | -55.14301 | 2025-09-13 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 0e497458-d8f5-38ae-89a5-785c92fd0297 | -17.34316 | -46.67481 | 2025-09-13 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5243d2f7-7a8d-37c9-abba-1929227a0a62 | -17.13783 | -48.50848 | 2025-09-13 00:50:00 | TERRA_M-M | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fae7d1f0-71ea-37d4-bb9d-0f674d45f8d7 | -18.89252 | -47.04875 | 2025-09-13 00:50:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| aaa5fb97-7973-3d19-89a4-beb90ec059b3 | -16.62731 | -49.805 | 2025-09-13 00:50:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9a4a8db4-08fe-381a-9cb9-f870d106eb2e | -15.6977 | -50.58111 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 116f4c61-eef6-3465-80ba-759ce44f5edc | -17.2339 | -50.23526 | 2025-09-13 00:50:00 | TERRA_M-M | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 45d8f0f1-a23c-3ff3-b1dc-75b26895386e | -13.13536 | -47.13269 | 2025-09-13 00:50:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b0752153-696b-37f4-9ef1-6680ef170989 | -16.98123 | -45.82137 | 2025-09-13 00:50:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c474852c-4687-3aac-a363-6d3e0d1ede62 | -15.77199 | -53.49789 | 2025-09-13 00:50:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c1ab301e-9a23-3073-94c9-3e3458b1f03e | -16.49654 | -55.13067 | 2025-09-13 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 164.0 |
| bd24e032-69d7-3ff4-bffd-86d95bd5de35 | -15.21468 | -56.68341 | 2025-09-13 00:50:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| fb9ce2b3-b35c-3c55-9fa9-48756480b876 | -15.7711 | -52.23931 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cc32695a-ed6e-3f5e-9409-144066772e83 | -11.74204 | -46.62823 | 2025-09-13 00:50:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 93166032-278d-34b0-8243-587733369078 | -16.64883 | -49.76205 | 2025-09-13 00:50:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 825a31a5-418c-36bf-b273-f093af98f88f | -20.03044 | -47.63108 | 2025-09-13 00:50:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7f0aa89f-fda5-3586-98b9-6aeec994f329 | -16.08841 | -49.96799 | 2025-09-13 00:50:00 | TERRA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 111.9 |
| af5d5787-136e-3b6b-b7ef-71e30dbfac3b | -13.25771 | -51.71881 | 2025-09-13 00:50:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad689878-1afe-339d-946d-91521d34bf5f | -15.77999 | -52.23802 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 498bc885-2082-3c37-8080-8075f16f492c | -10.77613 | -50.53846 | 2025-09-13 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 8dfe449e-d530-3914-9dc8-1908d258947b | -10.74401 | -50.5129 | 2025-09-13 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 61dfd5ec-ee5b-3504-b2ca-4b444ee24038 | -14.20593 | -46.24872 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 8d3c7f05-9f68-3689-b8b5-2e41ba8ac1b5 | -10.69548 | -48.66325 | 2025-09-13 00:50:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a7fdfad9-eed9-3b4a-b964-ee5e01e35846 | -16.08699 | -49.95832 | 2025-09-13 00:50:00 | TERRA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 1b82b205-8d6f-3ed9-afa5-915a7a236794 | -12.27873 | -53.92249 | 2025-09-13 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 60333878-b359-3667-89ad-fc9ab7ada96f | -20.07723 | -46.9459 | 2025-09-13 00:50:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6b794f5e-bb3c-367e-b1f0-3d48f17b840d | -16.16752 | -48.8709 | 2025-09-13 00:50:00 | TERRA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e88f3085-651f-3757-af37-77d6fad8ffe9 | -18.70887 | -51.77976 | 2025-09-13 00:50:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 08e2dc14-5e13-3723-b143-4e50bdb1e888 | -16.87375 | -49.34469 | 2025-09-13 00:50:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| ed6e7c6e-8279-39d3-9633-93e8507db510 | -11.85511 | -49.77998 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f814c5e2-5867-3711-a776-bcc06a13f9d0 | -20.34176 | -46.67208 | 2025-09-13 00:50:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c07cc157-58a6-351d-9a76-7d467b92712c | -19.26072 | -51.43131 | 2025-09-13 00:50:00 | TERRA_M-M | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e1e41d01-ed46-3323-89dd-989842baa458 | -15.87121 | -49.93232 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 484d12ec-5d24-3e09-a205-8ff3031f4f7a | -11.83031 | -50.56459 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4413ad6f-7f31-3fd5-a476-1b55480b03bb | -18.59774 | -47.19049 | 2025-09-13 00:50:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |


[Clique aqui para ver as próximas entradas](README9.md)
