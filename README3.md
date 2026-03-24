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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a060522-6a15-3eea-923a-95fd70cf7c5e | -16.84263 | -50.67218 | 2026-03-24 04:12:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| dd2a869e-fa58-34ee-8de8-19f8f766c296 | -17.12484 | -51.20731 | 2026-03-24 04:12:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f4ef70d-e05c-346f-863c-51ead8a6b6ff | -15.67415 | -40.88451 | 2026-03-24 04:12:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3aed74fa-f6ec-3c0d-94d3-a68b28986e3d | -22.37151 | -49.1214 | 2026-03-24 04:14:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7262369-f3c4-32e9-a509-8dffb626b2e6 | -19.22857 | -44.75069 | 2026-03-24 04:14:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3d34fd6-c1b3-36f4-8738-4fb22ee13bb0 | -21.0412 | -48.79551 | 2026-03-24 04:14:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7aa80651-b342-3b6f-b7bf-2fdd50097e8e | -22.65474 | -47.64086 | 2026-03-24 04:14:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7f4bc13f-104d-351c-8006-f639b0160137 | -21.1608 | -48.67597 | 2026-03-24 04:14:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 96d22f88-e488-398e-a49b-cdc066f2ca89 | -21.70781 | -48.43488 | 2026-03-24 04:14:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 969f48d9-3c7d-36e8-a11e-c7f4e8b48535 | -21.15076 | -42.99419 | 2026-03-24 04:14:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a19271f6-8695-3ec5-bba0-2248bdb340de | -21.11456 | -47.46109 | 2026-03-24 04:14:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73d3be60-bb5e-36dc-831d-37fdd87b6ad1 | -20.15882 | -46.69518 | 2026-03-24 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d59bd460-d519-382c-92fa-c4d50d3dd3d4 | -20.87505 | -47.64849 | 2026-03-24 04:14:00 | NOAA-20 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b007922-fcd1-3f51-97db-449db53817ad | -20.16221 | -46.6958 | 2026-03-24 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9481916-0cf2-30c8-86ab-13cf62492e87 | -21.11733 | -47.46579 | 2026-03-24 04:14:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6165338-a789-346b-9a9e-77f6defa3ffa | -22.89559 | -43.58535 | 2026-03-24 04:14:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6b98529f-2ac3-3a93-9b93-89c5fd129503 | -21.16138 | -48.67359 | 2026-03-24 04:14:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1519d5f-dacf-382f-90d0-3acb1990e45a | -21.03883 | -48.79218 | 2026-03-24 04:14:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5e905c25-959d-358b-8895-3bce0aa5cbdc | -21.49757 | -47.17366 | 2026-03-24 04:14:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fba7cd2a-df93-30c2-b5a8-5d9d925a6afa | -21.62794 | -49.0302 | 2026-03-24 04:14:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f13368d-9e9a-3839-8ef6-11c85bf8ad0b | -22.25252 | -46.95065 | 2026-03-24 04:14:00 | NOAA-20 | ESTIVA GERBI | SÃO PAULO | Brasil | 3557303 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c70f985-da63-3697-9536-506b88a4dca2 | -22.65547 | -47.64223 | 2026-03-24 04:14:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4d84c0af-85c7-3f59-b439-677913483ab2 | -23.60735 | -48.25928 | 2026-03-24 04:14:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5b3a61e8-f3ab-3f99-8bdc-3f574cdec867 | -19.228 | -44.75433 | 2026-03-24 04:14:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3dd913a-4c32-313e-8195-af6e92c64530 | -23.02207 | -48.44606 | 2026-03-24 04:14:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70f616e0-7cf2-3025-9f26-e42bdaf363a9 | -20.88324 | -48.58797 | 2026-03-24 04:14:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c68febe8-bd1d-35fc-97b5-a1c0d4662e9d | -16.58005 | -57.80379 | 2026-03-24 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8ce747c4-e10e-38b4-bd7e-6d36b3707e7b | -21.04204 | -48.7909 | 2026-03-24 04:14:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 50b4e7fc-d92f-3724-81a2-ad25c4053cdd | -21.71653 | -47.25053 | 2026-03-24 04:14:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 54a75454-42fe-3462-8f5d-97e2025cc625 | -21.71137 | -48.43566 | 2026-03-24 04:14:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5124cae0-01b7-3c9a-a635-b6cc8222ac95 | -20.67672 | -48.79699 | 2026-03-24 04:14:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| da32b553-6779-32e4-8c8b-bb2c00ec5a79 | -19.15331 | -45.11694 | 2026-03-24 04:14:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e156df18-9000-3373-acf1-b91b898718b6 | -16.57848 | -57.81057 | 2026-03-24 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 94390a30-bf00-3b78-a4ce-f81ab566a25f | -19.48631 | -52.70829 | 2026-03-24 04:14:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a75c8ce4-ff18-31cd-9af8-5388fe9a09de | -22.43773 | -46.90981 | 2026-03-24 04:14:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31495eb1-de65-3df9-9665-19fb3479b62f | -25.14122 | -52.51548 | 2026-03-24 04:17:00 | NOAA-20 | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1d8123aa-befc-32fd-9fed-0d5b573a230b | -25.14213 | -52.51104 | 2026-03-24 04:17:00 | NOAA-20 | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 332f8263-4802-37fb-b2e8-16b6c9a439d8 | 3.34941 | -60.14196 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25cac030-4b8e-3b24-b12f-e07893ecb90f | 3.98508 | -60.03778 | 2026-03-24 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87db9b2e-0099-32aa-bfb2-27e03d4cff87 | 3.35354 | -60.13555 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73105060-8ef7-333f-8f52-c09c8363d764 | 2.78917 | -60.30402 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9288899-9249-3a2e-8d47-65cffbd5c310 | 3.36352 | -60.13414 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8dd9b0e-8ff2-3f6e-aeba-a50b2a6a3051 | 3.98466 | -60.03493 | 2026-03-24 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a5edea4-fed8-3042-9451-2bd4f17ef58f | 3.35397 | -60.1384 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d09676ab-7df4-339f-9674-abcca24e3321 | 3.44886 | -60.15547 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b44e73ae-c17c-3760-94c2-19938cd5786b | 4.80877 | -60.62945 | 2026-03-24 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32bb1a48-0daa-37f5-8294-40b7a5015543 | 3.3544 | -60.14126 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35491025-1530-3f79-9e9a-bf3d9afbc7fe | 3.44843 | -60.1526 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84fdca03-aee3-36b6-ab75-d4abfa2a3bfe | 3.60073 | -60.99602 | 2026-03-24 04:55:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ad09468-65c9-3c4a-98bb-a2a73adf6fce | 3.60024 | -60.99274 | 2026-03-24 04:55:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67bba8a0-690e-33e4-8391-6459c0d1a715 | 3.36395 | -60.137 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79ac2c49-2c58-314b-a81a-5062d775d0a4 | 3.34898 | -60.13911 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2843e3e2-788c-3481-b8d2-ff51a7cb8165 | 2.78874 | -60.30112 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eff55df7-6f0a-3d48-997f-fd80e29c26f4 | 3.36438 | -60.13986 | 2026-03-24 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bcdf901-95ee-3a5e-aab3-338424b4e0c7 | 1.08132 | -60.64835 | 2026-03-24 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f5685f1-7db3-3506-b6b2-9a3d4e0521cf | 2.0315 | -61.10395 | 2026-03-24 04:57:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c1901e7-72e4-3f45-bb9e-b6fa1918bf55 | 0.9892 | -59.37893 | 2026-03-24 04:57:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 242108d1-24d8-3baf-ab42-9f44fcaceebe | 1.08676 | -60.65046 | 2026-03-24 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bdd60f3-acc2-3d41-bb74-3babe1b541a2 | 0.14508 | -60.40837 | 2026-03-24 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 10a173bb-f17c-339c-905b-0194b6e3bb47 | 0.73859 | -59.6109 | 2026-03-24 04:57:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbd5ed32-2d55-3ec2-91f3-c56c963ad4e5 | 1.13472 | -60.08413 | 2026-03-24 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4879bc08-6196-31f4-88d7-f9ddce1e3c3f | 0.77145 | -60.5448 | 2026-03-24 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 406f4620-5d32-3e3a-a853-72d24ddd1fb8 | 1.84237 | -60.41945 | 2026-03-24 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b9e87d14-c3bb-3b32-b914-45a7858a7f3f | 0.51536 | -60.26734 | 2026-03-24 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2eb7e2e2-5452-313b-ac42-a7f0f940221c | 0.77415 | -59.87493 | 2026-03-24 04:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8d5eedd-cd91-3389-8c95-6b8960978e36 | 0.98008 | -59.38028 | 2026-03-24 04:57:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b03f5074-4571-38a8-9513-29eb6acdd0db | 2.03672 | -61.10771 | 2026-03-24 04:57:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2a92c0fb-b985-3a8c-affd-e7ef5af49e91 | 0.9808 | -59.38493 | 2026-03-24 04:57:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6b15571-79e6-3bd5-8702-db6936c59017 | 1.08177 | -60.6512 | 2026-03-24 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40c3b156-0789-3e26-b078-a7b4a54fd018 | 0.73324 | -59.60681 | 2026-03-24 04:57:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f5f9d5d-567a-312f-ba1b-edc37b8f22a5 | 0.94444 | -60.46498 | 2026-03-24 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25ee012a-9170-3173-b82d-3092eff6a71b | 1.8374 | -60.42016 | 2026-03-24 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4e688f8-5896-3c21-a588-0d832061e6d7 | 0.94622 | -60.46151 | 2026-03-24 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8c4ee79-a053-3373-bd45-34ab5429c9e0 | 2.031 | -61.10532 | 2026-03-24 04:57:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6be50563-04ed-3016-8011-2474adc1ecc3 | 2.03672 | -61.10316 | 2026-03-24 04:57:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 675c5a49-7b6f-3a02-8c6e-e1d71c57e39b | 0.93752 | -60.32656 | 2026-03-24 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cae953e2-487c-3ac8-9b71-1895be66ddf9 | 2.03767 | -61.10952 | 2026-03-24 04:57:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 28b0b9b4-ffb6-3eeb-9645-8f47e4762075 | 2.03622 | -61.10453 | 2026-03-24 04:57:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 552cb2cf-53c2-3fc6-afc5-4059908ad288 | 2.03719 | -61.10633 | 2026-03-24 04:57:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f47c29a8-fc97-38be-8732-c2c7227d0d18 | 0.98463 | -59.3796 | 2026-03-24 04:57:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5051bb14-c7fa-3c3a-961d-496848e76764 | -1.56031 | -54.00776 | 2026-03-24 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e5fe924-c405-31a5-8698-36ce2057a132 | 0.98536 | -59.38423 | 2026-03-24 04:57:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef3af429-b707-3f21-8979-ecbc4aca2100 | 0.77809 | -59.86918 | 2026-03-24 04:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0711eb8e-d430-38b5-8de7-cfbf58bd64aa | 0.62963 | -60.05577 | 2026-03-24 04:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f693424a-4a8c-38ab-a9fe-1c46c12cf1bb | -1.50294 | -53.67934 | 2026-03-24 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ced4b291-c788-3c35-9dd2-9487fb48b093 | 1.88543 | -60.6709 | 2026-03-24 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b1f25ce-0b21-3080-9229-15c080286d8c | 1.84322 | -60.42508 | 2026-03-24 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee16284a-95c6-39f2-84a3-0f8066dd3d9c | 0.77173 | -59.8726 | 2026-03-24 04:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e2269b4-495a-3ff8-be88-dd4c21d1c062 | -0.96914 | -53.17979 | 2026-03-24 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2de8f3f-ed94-39ef-80a0-bbcef5eac6b3 | 0.77339 | -59.86993 | 2026-03-24 04:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc231abf-1e47-32fd-8ca4-0ca708a59356 | 2.03197 | -61.10713 | 2026-03-24 04:57:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ea89cae-419a-37b7-89dd-faf1f779afd0 | 0.98992 | -59.38354 | 2026-03-24 04:57:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47da1f5c-1522-3d23-99c5-deb6595f06cb | 0.63438 | -60.05504 | 2026-03-24 04:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53d6c29a-0147-3715-8dc0-43785ff4d01a | -0.97244 | -53.1803 | 2026-03-24 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5779aaee-c893-37b4-a0c5-a04105d80db9 | -10.67286 | -54.2949 | 2026-03-24 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fd1ac0c-f9fa-330c-b5a7-bce0d4f2500b | -10.67177 | -54.30198 | 2026-03-24 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 347fab2d-03e0-36a6-8d5b-03e7b613bd7a | -10.67232 | -54.29844 | 2026-03-24 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35dd5c75-917d-3272-9144-883185aae529 | -16.58087 | -57.81008 | 2026-03-24 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f3a55f52-9888-3d58-8e43-6f6a8b6ab6fa | -19.49123 | -52.70836 | 2026-03-24 05:01:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f89b9c3-9382-3665-b909-0c0d73b88433 | -16.84675 | -50.66565 | 2026-03-24 05:01:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README4.md)
