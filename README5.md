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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d39051e-356c-343b-b21d-8dc5e6b4ec60 | -14.4875 | -46.50543 | 2026-07-26 04:36:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dab7b6b3-482d-33a8-9401-9155ce8a9ba2 | -16.4923 | -52.37966 | 2026-07-26 04:36:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ea5093e-ec07-3c1e-9a2c-947ad364ba0b | -18.25603 | -46.96703 | 2026-07-26 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 095eb5b8-9aa5-304b-9350-0aebf5ea4479 | -15.13302 | -47.64473 | 2026-07-26 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f405ad8f-ea08-378a-b93b-60d0a978ae82 | -13.3755 | -54.29143 | 2026-07-26 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd938ef1-db45-371b-ad99-ef331b816438 | -13.68464 | -51.90768 | 2026-07-26 04:36:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e08b5870-76f2-350d-b4f8-08768b32b8db | -18.49754 | -54.10035 | 2026-07-26 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7608a31-beb8-3779-855c-e204312f4cf8 | -16.24835 | -46.29139 | 2026-07-26 04:36:00 | NOAA-21 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc55291a-a079-3c60-a0b0-fea4852724ba | -13.69002 | -51.89672 | 2026-07-26 04:36:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a614ab80-4e03-3d55-b8ff-0b6fd1ba528e | -19.01763 | -53.89835 | 2026-07-26 04:36:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6416d47f-549a-33a1-a6ac-6ac85205042e | -18.69732 | -44.54776 | 2026-07-26 04:36:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b5b96e5a-4bfe-3183-a0d3-5acde78cc019 | -16.79405 | -49.29428 | 2026-07-26 04:36:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dad8505a-5622-3974-b7fe-30e389d89e25 | -17.20959 | -48.49998 | 2026-07-26 04:36:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9e1bdb7-884e-3f7d-b252-95dd8902a945 | -17.28526 | -46.50444 | 2026-07-26 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eebbdb05-7193-3db4-9143-f1b6cf76297e | -16.58698 | -54.65019 | 2026-07-26 04:36:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 325aec18-5578-3723-9542-e8c8b6f8f587 | -19.36949 | -42.54018 | 2026-07-26 04:36:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cf0ed387-c212-3d2b-b28f-b343d6dcb91f | -18.02683 | -54.3564 | 2026-07-26 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de3f8786-5665-34c8-b64d-3af4670b8a8e | -13.37156 | -54.29074 | 2026-07-26 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f000068b-200f-32a8-82a0-63fa717b5871 | -13.80489 | -53.86288 | 2026-07-26 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b2f5fbc-a415-3eef-a8fd-60e8fca6f419 | -19.36641 | -42.53962 | 2026-07-26 04:36:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9a680b8c-5627-3885-87fd-c3c614448ba9 | -16.04019 | -47.99805 | 2026-07-26 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 869a0c17-3f66-3d5d-95ba-9bf72cc21b1f | -13.93018 | -53.88253 | 2026-07-26 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcb9b944-17ab-398d-ab5e-7ef925906344 | -13.92719 | -53.87705 | 2026-07-26 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb2787bb-852b-3a4d-9e41-d58136b0d380 | -14.66165 | -46.95914 | 2026-07-26 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a9535122-0d5f-3e98-b88a-874f07512dfd | -15.40597 | -53.90223 | 2026-07-26 04:36:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11e6c64a-4043-3aa1-a0b5-df0aff3873ce | -13.68939 | -51.90057 | 2026-07-26 04:36:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb437767-8cab-3ea8-a3d5-55591831d7f3 | -15.81714 | -56.72364 | 2026-07-26 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4836b438-2178-3bdc-80f8-7bf39c0d43c0 | -14.28113 | -53.38425 | 2026-07-26 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0f76d05-a699-3580-942c-66b32ebcebb0 | -17.07469 | -48.89322 | 2026-07-26 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66469837-fce2-3402-a09b-4e30c9fb3f4b | -13.80191 | -53.8574 | 2026-07-26 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca304659-5bf3-3c01-83b3-26b1b5369a57 | -12.54192 | -57.21917 | 2026-07-26 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 53a099c5-d8c9-3a75-8c4a-079141629998 | -18.49315 | -54.10402 | 2026-07-26 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b809440a-cd95-3c90-b00a-485f18850d07 | -18.39193 | -49.21559 | 2026-07-26 04:36:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b204ff5-a502-329b-9f0a-73e166c0a428 | -18.49393 | -54.09961 | 2026-07-26 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d92daa1a-6ad1-39c0-ada8-4425dd68db43 | -17.20904 | -48.5038 | 2026-07-26 04:36:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 382bce21-0ecd-3410-b6b5-ba3830214a6b | -18.69679 | -44.55197 | 2026-07-26 04:36:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dcaf719a-9a37-3849-8381-bf346cb52a2c | -19.10303 | -45.06133 | 2026-07-26 04:36:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 661bb88d-cfce-310c-b279-c8b52762e37c | -13.67401 | -51.8858 | 2026-07-26 04:36:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c70b6e4-d6d1-3e79-8d49-7d7c8025310f | -15.81632 | -56.72806 | 2026-07-26 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f215f78-273e-3b36-b04d-559a0c00d5ed | -14.72246 | -47.5089 | 2026-07-26 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c7ce184-e664-3daa-916b-efcc21534eb1 | -14.73633 | -47.14422 | 2026-07-26 04:36:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0718cb12-d70d-3106-9337-ad510ca5c692 | -17.28154 | -46.50389 | 2026-07-26 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e44be66e-8ab8-37fe-adc7-88bc542e40d5 | -13.68657 | -51.89604 | 2026-07-26 04:36:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f383028e-2f3f-333f-8e29-ce2b01f42c98 | -16.24771 | -46.29605 | 2026-07-26 04:36:00 | NOAA-21 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abcd5b20-1610-31d3-b544-0c889acddde6 | -15.81274 | -56.72273 | 2026-07-26 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc1efcfe-6bf8-370b-9458-9432fb5daee6 | -21.28146 | -56.03308 | 2026-07-26 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98414b4f-05f0-3b55-9274-19ae0a976851 | -21.27762 | -56.03225 | 2026-07-26 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c63e6e52-5e0e-3cf5-a677-18b08c502b98 | -22.36594 | -49.09752 | 2026-07-26 04:38:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3410fb11-4386-395e-98d3-01553b6d0267 | -21.28052 | -56.03822 | 2026-07-26 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1170899-f4f1-305a-afac-62f9ef13e0bf | -27.91534 | -54.43707 | 2026-07-26 04:40:00 | NOAA-21 | SANTA ROSA | RIO GRANDE DO SUL | Brasil | 4317202 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4555813b-754c-3218-b289-4ea564df16b4 | -2.56603 | -51.88688 | 2026-07-26 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a08d6577-5d28-3014-ae92-90931c7e8294 | -3.83707 | -49.06399 | 2026-07-26 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b1754fa-979f-310f-a366-725d73e6a0ab | -3.72584 | -48.87672 | 2026-07-26 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ce3349bd-30f5-3ffd-8236-ad8d51e8bf65 | -3.24354 | -47.92273 | 2026-07-26 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dd60f8f-be19-3076-84c0-8568c6cbfb58 | -3.04974 | -48.74569 | 2026-07-26 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3562c642-da2a-39ff-aa19-bb14dd5942d4 | -3.72986 | -48.87734 | 2026-07-26 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3c0dab7d-9a03-30a0-a401-6e49f1fe3073 | -3.16005 | -48.5897 | 2026-07-26 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d591fdfe-70d5-32a0-9731-a3ac0070f034 | -5.93523 | -43.6572 | 2026-07-26 05:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 35332718-045c-3234-b71a-811b4e2ffc96 | -3.96233 | -43.11134 | 2026-07-26 05:08:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ce5a0e1-4317-38b7-b2be-2ef658d79b70 | -3.161 | -48.58679 | 2026-07-26 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cca4806c-4638-33f7-be4a-3b96b422d726 | -2.34805 | -55.96051 | 2026-07-26 05:08:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a8c15d70-a2df-3a79-b7dc-5f392aac088a | -3.41258 | -49.11689 | 2026-07-26 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f91aae10-8620-3e15-bf10-83880c7dc36e | -3.83517 | -49.06541 | 2026-07-26 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14ff8f43-31cd-3d8d-b348-35c3a6dcce9a | -3.06305 | -51.33673 | 2026-07-26 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b54674b5-fc6d-3765-b1cb-96b4643db5ec | -3.66708 | -48.99356 | 2026-07-26 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e25fa9cf-e922-33ca-90df-21e69d3a8d73 | -3.72638 | -48.87322 | 2026-07-26 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 04da8dc2-8d09-321f-a3fb-839a64601b2c | -2.97944 | -54.09178 | 2026-07-26 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe0f4250-dee9-3f17-98d9-381ffac110f4 | -2.82549 | -52.30238 | 2026-07-26 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1553baed-d272-3829-ba65-f7085898b197 | -1.527 | -52.62188 | 2026-07-26 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cc52531-497c-3ea7-ad33-fd1c937f319f | -5.93331 | -43.65653 | 2026-07-26 05:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d64eb4ff-6b09-3b81-baed-2dc397322191 | -3.72237 | -48.87261 | 2026-07-26 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 007d6488-429d-38a3-9cae-dc80adf31242 | -5.93584 | -43.653 | 2026-07-26 05:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff763796-2b20-3cc3-8e57-241c0dc95d38 | -5.93982 | -43.65311 | 2026-07-26 05:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df8db79e-3f53-33b9-814f-2d7f4078f0cd | -3.26128 | -49.53255 | 2026-07-26 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01bd8a66-f2d1-37f9-80b6-3e8c8342cf2e | -3.34864 | -49.22191 | 2026-07-26 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb7a3495-ae91-3d66-92f8-9af56365ee02 | -3.83914 | -49.06602 | 2026-07-26 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a72b8056-ba4f-3942-9565-048881e13532 | -3.34474 | -49.22129 | 2026-07-26 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 108b9c15-61e1-39a4-abef-65e0357d23b4 | -3.41651 | -49.11749 | 2026-07-26 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d34ac1f5-d0c9-3f1f-9bf4-47d94bcf7c0b | -3.79968 | -51.18758 | 2026-07-26 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3205d2f7-0885-3504-b79a-15af52be301a | -3.3494 | -49.21699 | 2026-07-26 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 244ec893-2f0c-3cff-ab86-731b5b42e886 | -3.24417 | -47.91872 | 2026-07-26 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd4c6a80-a244-3da3-b9a5-362740e2d585 | -5.67936 | -49.81819 | 2026-07-26 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 847842f4-9ba5-3440-942f-1ef9f7e6d540 | -3.84631 | -48.95231 | 2026-07-26 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 940f916a-f240-320b-80ff-e411d19df8d7 | -2.98276 | -54.0923 | 2026-07-26 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5a1f289-a5aa-31b4-a224-21b08f476406 | -5.9339 | -43.65226 | 2026-07-26 05:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15dd57e2-51e4-3a51-9117-cdbcff703cea | -3.23991 | -47.91809 | 2026-07-26 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 311d29fc-e9ef-377d-964c-31aa550943b2 | -5.93924 | -43.65731 | 2026-07-26 05:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f685a16-12ef-315a-b519-211d50d2b022 | -2.80761 | -48.66931 | 2026-07-26 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18889e27-7656-3b84-a7f4-8c8058469d8e | -4.41409 | -54.86491 | 2026-07-26 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dace210-8b80-38df-b6d6-413fae6b5936 | -3.05375 | -48.74632 | 2026-07-26 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e471446-d829-33ff-a961-4a5b9595d9cb | -3.16044 | -48.59036 | 2026-07-26 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cc55359-90ae-3b57-ae3f-f611eb6111c2 | -3.80028 | -51.18371 | 2026-07-26 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 515b3e63-b938-3ee7-895a-9643ed573da3 | -2.76879 | -48.5739 | 2026-07-26 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a33c46b3-761d-315e-aacd-b57a5f80623f | -13.68728 | -51.89661 | 2026-07-26 05:10:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34a6ddf2-a483-3700-ae77-3230c55f19fa | -9.9303 | -47.90678 | 2026-07-26 05:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70393e9c-9b13-32e7-8080-29345106f89c | -13.3381 | -54.29911 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a30ca794-6f3e-37bb-89ba-6810b395ad15 | -9.92625 | -47.90115 | 2026-07-26 05:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e39555e1-ab10-385b-9022-f179d0c1d4f7 | -11.06598 | -54.51074 | 2026-07-26 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8629e41-5bc5-31ab-b504-45b4bbf0cc7f | -9.93096 | -47.90185 | 2026-07-26 05:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94e029b5-f368-36cf-ac16-6f11233af525 | -13.80588 | -53.86308 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)
