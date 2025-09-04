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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5149268f-709a-3ede-b7a9-efd8a3e66930 | -6.22297 | -43.54579 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22d1b527-042c-3678-89c5-ad9da7a9686b | -7.72445 | -44.61661 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca3057d5-3de6-3ad1-b817-365fc941a98a | -6.2979 | -43.60123 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03531067-d269-371f-a642-b2bb69fa7397 | -5.69675 | -45.17295 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1598e856-9cf2-3c3a-aae0-63e4f3322bf5 | -7.36865 | -44.3277 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79689825-c49e-34f8-acc8-3447fe502699 | -6.7902 | -44.44396 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0625eee-4066-347e-9c23-93775b5ef564 | -6.24918 | -42.63478 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 226f7504-f578-3eb7-bfb7-5b29e73cc00c | -5.70063 | -45.16994 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c315ad12-2707-3cee-85df-881d4de2b59e | -5.68377 | -45.12389 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4eea9df3-829b-3ddf-98ed-f0e711691a7e | -6.92848 | -44.31752 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 615456cc-141a-3fe5-8b89-84daf914a9a6 | -7.76303 | -43.96862 | 2025-09-04 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc47b653-ce5c-3c0e-bca3-afac3868cba9 | -6.09111 | -46.72639 | 2025-09-04 04:25:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99465537-2be4-30c8-beef-3df90aa55ded | -6.21731 | -43.39122 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6330c48a-cd11-3cb7-8773-025a131c3ce8 | -5.4535 | -42.82093 | 2025-09-04 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3718a420-75da-3b47-bc3c-2aa2ac9e0b98 | -5.69365 | -45.93969 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92dc2738-81a1-3648-a86f-443e2ff92a9d | -5.98393 | -43.81352 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dba8d9ef-46ed-397e-a4c5-f714a111fb47 | -6.40913 | -43.266 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f99f13b8-2b0c-3c13-8d4f-674289c5cba9 | -4.99769 | -56.2594 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 831ac79b-ffdd-3e35-a80c-64d966449bd1 | -3.16798 | -49.47835 | 2025-09-04 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c05a0346-09d7-3ccf-80d9-0a7dc3810977 | -6.78554 | -44.08484 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 54c44750-2ce6-3216-9c40-a50d8b2c450d | -6.78783 | -44.09315 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d71feb3-1a09-355d-a8e8-5179542b9634 | -5.87801 | -43.23842 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9801c86c-a0d6-314f-81a5-ddd839444bb1 | -6.1247 | -44.11803 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3e67352-3f6f-3dfe-9ad6-de9698d97669 | -6.15274 | -44.11381 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a786efb0-9473-3856-9170-30f97401baae | -5.44621 | -42.81984 | 2025-09-04 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 02325342-c011-3b64-b638-0004543d4b62 | -6.96575 | -43.95127 | 2025-09-04 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e52056f9-fe9c-3cd6-942c-0a501fb527c3 | -6.33384 | -45.64906 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae647d99-4dd4-3068-a06a-bc6d82fc2382 | -8.09596 | -42.42796 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9096b89a-2f66-3598-b6de-abd5d688b34e | -8.01936 | -44.14323 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d869e032-4aac-3cc7-a202-af36a756edfe | -6.54254 | -42.94494 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 817d11cd-a295-36bd-bae1-f35c5bdfec96 | -5.69532 | -45.40283 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c29b7e5e-fd1b-36ee-b0de-8d2511e953e4 | -6.95971 | -45.55976 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a87a7f-83a8-3951-bb74-5d9829fdf4eb | -2.93621 | -48.8203 | 2025-09-04 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7960ffe8-90b1-3bf9-9e69-4f5024316998 | -3.80162 | -52.33174 | 2025-09-04 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8024a405-ee18-3972-a60b-9e297aae09e7 | -6.28523 | -43.51678 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b684e740-23f3-31ae-85e6-3cdfacc623c3 | -6.22824 | -43.55879 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 195df11e-f315-34a3-8d42-8615bf0f00f8 | -5.9833 | -44.14749 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ded714d9-9635-32a1-b759-4482b07e40a6 | -6.73536 | -42.26151 | 2025-09-04 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b7e8f08e-c1c2-3efe-a13d-e874e4a5c106 | -4.84008 | -42.74147 | 2025-09-04 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f2625a1a-9cf8-3264-9236-ad528736b64f | -3.13592 | -40.06773 | 2025-09-04 04:25:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 51615616-ee30-39d3-be26-5855ddcc81ee | -6.45638 | -42.39185 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 05108b5e-19b0-37f2-bc4f-622485d1be1e | -6.26138 | -43.57907 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ab6cec7-b3c5-32cb-a817-355a9db7686f | -5.68867 | -45.40181 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b765d9a-ed2e-31fb-8535-ce3119af74a3 | -3.95423 | -49.30119 | 2025-09-04 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7260d266-33a5-3615-817c-e01e9fcef3f3 | -2.58585 | -51.92253 | 2025-09-04 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c637ef72-f212-3861-87cd-3a8f92455758 | -5.9105 | -45.94516 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02477fee-be0d-3321-8998-a847a3210059 | -5.92467 | -44.16561 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7dd5144c-5d81-384c-96ba-814decb691d4 | -5.68876 | -45.59814 | 2025-09-04 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6113ea73-0de1-3f02-9442-2c84d2e4dba2 | -5.71814 | -45.25558 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3e4fc7f-6d2d-3b49-8547-004c0b909c28 | -7.51291 | -45.36547 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d748f468-7fe3-3944-932b-502b8d2bc8f2 | -5.95259 | -45.56452 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2a6eba8-170f-32e9-8afe-9dbe66440cfd | -6.04098 | -46.00142 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0186b293-b31c-36ef-829b-ed2d3e93c704 | -5.82228 | -46.35862 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6256a190-5933-3f05-a845-0e4c38c470d6 | -6.34222 | -45.68255 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca2f7608-4ed5-3a1c-b72c-afc024956811 | -5.94775 | -43.04413 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 951dee5e-c638-3174-9ee3-a78d5b50d1ed | -5.89627 | -44.34939 | 2025-09-04 04:25:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 648e9504-b212-3f81-b035-d9dbb8e92d3b | -6.27806 | -44.51321 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8136bb9d-3419-303c-a42e-f3d31f20ac12 | -6.20874 | -45.05259 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40889d81-7fe0-3cec-8f6a-800c2f0712ff | -6.02394 | -46.67685 | 2025-09-04 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0936030-6e2c-3386-a954-7a852b1d0092 | -4.89048 | -43.13686 | 2025-09-04 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b669a400-d0e2-3911-a16e-c044d3a7beaf | -5.69892 | -45.15882 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c9e89d3-1946-3a5d-8e52-1746a5c4a376 | -7.71294 | -44.03808 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 394d9531-58a7-3df1-848c-9ac74d3043c0 | -6.59743 | -44.06916 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37430e2b-54fd-382e-bb07-0d1fb5dadea8 | -6.37463 | -42.9935 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc64d2ef-b190-32b2-907d-0867258d4c23 | -6.08162 | -43.27938 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad3af8ba-ad75-3194-b923-fcb05524315a | -2.42996 | -49.30972 | 2025-09-04 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bb1648e-ac16-34d5-bbe4-108dd7d5bde1 | -2.81394 | -48.68446 | 2025-09-04 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a065809a-ce1b-35cf-bcf5-14e9f5c7a344 | -7.55574 | -45.70639 | 2025-09-04 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecb80eb9-62e8-32a1-bf91-8c7c0038a45d | -5.7751 | -44.86467 | 2025-09-04 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 014da36b-292c-3804-8338-f886f8791425 | -8.0059 | -44.03907 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f21a34a8-0f7c-30f0-9c08-def802fbdf40 | -5.69254 | -45.39883 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ba756b9-0d3d-31d7-aa52-ca42709a1dee | -6.17482 | -45.33759 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61f238ee-072e-3545-9cf5-5737066cb897 | -5.99503 | -44.98291 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e7ebbc5-5b6f-349e-bb82-3158dbae2ac9 | -6.83269 | -44.27966 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68006e50-4580-3d57-b2e0-477c3838b93e | -5.31642 | -55.85765 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 539cac9c-63e9-3682-ba62-0ee17851a50d | -6.21793 | -43.38714 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab62870a-8d7e-30dd-a54f-d10c8e7b3b9b | -5.48394 | -45.23038 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2669fadd-1d8e-3ad4-b0cc-cec7bb3f5c48 | -6.97807 | -43.28809 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d17c16b3-b6e4-3410-baac-1a4f6fc8fcde | -6.23495 | -42.6282 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 951a5a35-77fb-370d-a2e7-6330906e64b4 | -4.15849 | -46.78994 | 2025-09-04 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53305260-725c-35e3-8a34-16d37e5c6e2b | -6.68568 | -48.41695 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f997dd57-5b65-352d-b7aa-14aaa1f415f9 | -8.01219 | -44.77821 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b534bc0-1f62-3863-af43-8a4ca2ea2076 | -4.68841 | -43.65276 | 2025-09-04 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1f06ccf-d897-314f-95a7-8b6cd7d774a9 | -5.18956 | -46.07176 | 2025-09-04 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df096f47-1aa2-3054-b1e0-3376c20a3f96 | -7.47774 | -45.66191 | 2025-09-04 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f0c6324-3888-32da-84ac-48ace486acbd | -5.8979 | -45.96088 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b924eea-4241-3472-840d-45b034e151aa | -6.68351 | -48.4088 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b9ac844-7628-342a-9a2d-3b28781c694d | -6.78963 | -44.4477 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 713b6fe8-6559-3c6e-b06c-47085058fe46 | -6.27094 | -43.32762 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 980cc08d-02bd-371c-a067-6513b44283e9 | -5.6865 | -45.94211 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de6af81a-1fda-3f1f-8d6c-bb2cf3eba178 | -5.02359 | -56.10923 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afc77c4f-ce87-3fe1-aa42-e4455fc1c302 | -5.18626 | -46.07125 | 2025-09-04 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b234a16c-3d96-3db4-bf28-344e6b0dc3af | -6.53953 | -42.94216 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e58279c-7d3a-3f0f-9160-902b8cce0833 | -5.68844 | -45.18249 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47a3e406-0f75-38aa-8f07-f2c2930c970a | -6.79138 | -44.48254 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 538ea1e9-2831-3fb4-b44f-d97461543349 | -5.74611 | -45.53624 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dd01ee3-b3f3-38c0-b5fe-c8a9f67cfcb9 | -5.78418 | -43.8401 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3918330e-03a5-39a8-9eed-46b0663f9f3f | -5.27685 | -55.95607 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94c26d52-ba94-30ed-8821-56718d6a521a | -3.30534 | -42.39555 | 2025-09-04 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 395d10d6-afc8-323f-a1ce-a301f9a73743 | -3.23051 | -47.12896 | 2025-09-04 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README34.md)
