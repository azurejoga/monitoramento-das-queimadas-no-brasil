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

## Dados Diários - Página 395

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b659e9e4-50cc-34f2-bb85-8a45239370f9 | -5.9587 | -55.3448 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| cf1a868a-3a36-39bc-9fed-7bcf51e72615 | -11.8696 | -43.5568 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ef9d8153-6c35-3d3b-bcd3-88d0aa7579e6 | -3.1484 | -53.7225 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 366f5fd7-cb65-37ed-8577-86abe5a693db | -2.8433 | -57.4891 | 2026-10-08 18:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 45e98b37-59b5-32dd-9cf8-26d76ecb8d2c | -11.6365 | -43.7113 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 285.0 |
| a3f07b56-28a7-36cd-b93f-e3de1803efe1 | -12.62 | -44.5414 | 2026-10-08 18:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| c055b374-cb67-3d6f-8564-b7ba9404f14b | -11.6173 | -43.7142 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 421.9 |
| 94960fa6-4002-3859-81c4-ba4777bab5ed | -11.7738 | -43.5482 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| bda405e8-8c81-354b-9629-83eea490eb34 | -8.6133 | -44.896 | 2026-10-08 18:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 8cd9ac72-8d30-3018-a02e-b9021501d673 | -9.0705 | -67.7225 | 2026-10-08 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 06244934-7f15-3869-ad45-1a413120b73f | -8.5124 | -46.9128 | 2026-10-08 18:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| a329dda7-2226-3597-9297-d9cfd6bbed0c | -2.9818 | -54.0689 | 2026-10-08 18:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 185.0 |
| 5afd5992-7488-3ddb-9abd-03757edfcc91 | -6.0447 | -53.49 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0cd2f1e2-9583-3e24-bf1c-2c5f9178d183 | -2.0576 | -56.8786 | 2026-10-08 18:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 996ed5eb-db89-33ae-a7c6-8874278e7727 | -11.1992 | -49.408 | 2026-10-08 18:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 06925599-f9f9-339b-b8d1-0eacb825508b | -3.9483 | -56.0138 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 5641d340-262d-344c-9d13-f87427c438aa | -9.0592 | -65.9209 | 2026-10-08 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| fa537dd4-f8df-3c9e-aaba-e25ba501ccd7 | -5.2847 | -45.7249 | 2026-10-08 18:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 14e40105-b338-3933-8534-3cbf1cbf4017 | -1.3264 | -56.398 | 2026-10-08 18:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 16f0d342-6183-3baf-9032-305686aeeb8f | -3.2761 | -54.0011 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| fc071d0b-c8dd-37bb-93cd-29d63d785612 | -3.1114 | -53.8041 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 44c4d819-d9d7-3ac4-b2c3-de2ce34056a7 | -3.3319 | -59.5043 | 2026-10-08 18:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 99878a04-b113-37f0-8abb-2296c7e595c6 | -6.9328 | -43.6799 | 2026-10-08 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 999019cd-a9cb-339e-a341-ff8840e643fb | -3.784 | -44.3602 | 2026-10-08 18:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 51a32ab9-33dd-3df9-9c8f-a83809854a5b | -7.7022 | -45.4663 | 2026-10-08 18:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| d6fcf8bb-3901-3127-bb25-457f754c7fbf | -2.572 | -56.1646 | 2026-10-08 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 0186a4e7-b504-33e9-8670-a42941c4a1fa | -8.948 | -65.9429 | 2026-10-08 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 574.1 |
| 9ae7985b-4f28-3abc-a884-525708fa3aec | -2.9451 | -54.0497 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ea1b09f3-ebee-3ed5-82c7-421fa9aa52ec | -3.2717 | -50.3893 | 2026-10-08 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| a9b3e445-eb7f-3d28-8e63-c1c8c0c343e7 | -11.47 | -43.3824 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 3026fc81-10b5-366e-b34d-e1af7b452ce0 | -2.9271 | -53.9295 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 553ecd0f-c3ac-39f9-9997-db3fbc272ac7 | -3.1879 | -58.6433 | 2026-10-08 18:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 177.8 |
| c469de91-c314-3488-a433-0774fb07dfbe | -11.2816 | -41.1194 | 2026-10-08 18:40:00 | GOES-19 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 156.5 |
| d7ccddb5-dd21-3738-8223-add634d12077 | -11.4507 | -43.3854 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c8234849-0aea-3994-928b-de1a4cbf07d4 | -6.2162 | -52.7876 | 2026-10-08 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 4abb8917-c594-3336-b4ed-fcc31a65e7c9 | -7.4697 | -42.8315 | 2026-10-08 18:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 949bcdde-98a8-3b99-b92d-8a2f200716ff | -2.4942 | -58.0768 | 2026-10-08 18:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 3f0a6940-efd4-35e0-be94-e1108546b89d | -8.5368 | -67.0135 | 2026-10-08 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 467889b2-344d-3c44-a8cf-a4f3632562fe | -9.8817 | -44.8632 | 2026-10-08 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 342.9 |
| 9b132b39-2534-31fe-a36d-c7dd87b2bdfc | -3.2215 | -53.8616 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 617c58a1-47ef-3746-b381-910968d0aa94 | -14.4345 | -43.9157 | 2026-10-08 18:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 535.6 |
| 3fe387c8-4df6-3de3-8ecc-086682db3363 | -8.6136 | -44.873 | 2026-10-08 18:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 0c2d8563-0cf2-3765-92eb-6ba9751481ec | -6.6899 | -45.3746 | 2026-10-08 18:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 77f59179-09d3-3228-b521-b763209ced4c | -4.7404 | -55.6522 | 2026-10-08 18:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 62597a4d-f77e-306b-8aea-91d02e43fdf0 | -15.1057 | -43.6168 | 2026-10-08 18:40:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 187.9 |
| 9087b50c-e15a-3a4d-8c64-6246b6acba60 | -3.7057 | -57.0998 | 2026-10-08 18:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 14ee8447-9477-3dce-8b0f-e7ce9c08a722 | -3.86 | -44.1274 | 2026-10-08 18:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| cdf10cef-6063-3ca4-88e1-a5d4aa206998 | -6.8762 | -43.7083 | 2026-10-08 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 6c5057a8-7a60-3fab-90bf-49c1bed3bfa7 | -1.1094 | -54.1601 | 2026-10-08 18:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| e7f4c248-c7d7-3637-95aa-960ea30232b1 | -6.4752 | -55.48 | 2026-10-08 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 4973fd47-264b-3271-9eaf-2c9f56692ee8 | -2.8228 | -58.361 | 2026-10-08 18:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8286acb4-85c5-307c-bf43-fb7d8b3aea7d | 3.5448 | -51.2772 | 2026-10-08 18:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 51cffd6b-903e-36ca-9d25-155a6b4ab8c7 | -2.5721 | -56.1449 | 2026-10-08 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 95a12d40-e63a-38e9-b5eb-03ed41ba6907 | -7.5849 | -55.7005 | 2026-10-08 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 3736deb8-65f8-3894-aa69-ed5893b34800 | -3.2085 | -57.87 | 2026-10-08 18:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| c6e3228c-5022-3727-9783-d6d23ea372a2 | -12.7678 | -44.8671 | 2026-10-08 18:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 0f59e277-b631-3753-bffc-9fda1e0dce2b | -3.2268 | -57.8696 | 2026-10-08 18:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e535dc5d-94de-38c4-a7e7-ed8d729bc7e7 | -2.9819 | -54.0287 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| a05c97b3-c074-31d7-b04a-88f0e5f0c198 | -3.2137 | -42.953 | 2026-10-08 18:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 418.7 |
| 9d0e095c-51af-33c1-a782-8f01122df69d | -2.9449 | -54.13 | 2026-10-08 18:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d1c81f43-72ff-32d7-a3a3-f0c86d378506 | -6.1001 | -53.5075 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 1a00078e-a34a-3b71-a66a-f54783e58bd1 | -9.3394 | -65.4638 | 2026-10-08 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 2d6ba36d-a9d2-38b7-bc9d-6be9e57fa273 | -6.6711 | -45.3761 | 2026-10-08 18:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 50c22f5b-bbff-38e9-95d1-d5b19295418c | -8.9775 | -45.9023 | 2026-10-08 18:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 265.2 |
| 97fc7ced-ebb5-3a7e-8a73-1146b3d9631d | -7.0281 | -45.3008 | 2026-10-08 18:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 6b5822d7-fc6b-3f15-9eef-4690490cba97 | -12.2508 | -44.7397 | 2026-10-08 18:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| dcee609f-ff13-3004-b8e6-c7b2254ee457 | -9.1257 | -67.8322 | 2026-10-08 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 124.3 |
| e484ae70-da52-3c69-8127-0ee2ec2c08a5 | -14.3608 | -55.032 | 2026-10-08 18:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 2dee3a75-bc43-301b-8924-a352eded771a | -14.0472 | -43.8222 | 2026-10-08 18:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 06cf4068-0a80-3f3b-87cd-71a009a588f9 | -1.7864 | -55.0306 | 2026-10-08 18:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 4b2a0fb6-2c90-30ba-8a2c-7140f930867d | -3.2945 | -54.0006 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 9b8baa42-bc5d-3f7c-9d83-0adc7c2cbd02 | -3.2533 | -50.3899 | 2026-10-08 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 004ca65c-a2c0-3e4c-9f9e-deb3d820792b | -11.0762 | -44.0065 | 2026-10-08 18:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| cdd28669-cb30-31a4-96a8-df12c4312f53 | -3.1951 | -42.9538 | 2026-10-08 18:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 555d06d2-c061-3299-a21b-d4894925e9c3 | -9.1362 | -65.3022 | 2026-10-08 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 9e194d3f-32bd-3f2e-8c1e-62e5319f660c | -3.1973 | -50.5382 | 2026-10-08 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 22bed652-c8f5-3fec-844e-2e2e7a3079b7 | -4.3542 | -55.6455 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e37471a6-b7ad-38d0-9933-71bc04876623 | -7.0706 | -52.6764 | 2026-10-08 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 151.4 |
| c92f1cf3-8c1f-313c-aeec-bcc1d0aec1b3 | -6.3283 | -55.3276 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| f2731b72-9486-3a71-8aec-e301845b93c7 | -2.9267 | -54.0702 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a063ff7f-190c-307d-bae2-87b539024618 | -9.0065 | -45.15 | 2026-10-08 18:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 347.2 |
| 3cee7e8f-faec-3eed-a458-de10ea6660c3 | -6.3133 | -54.8084 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| f2b64037-3e58-3e8d-9090-d409159a3f08 | -5.4806 | -44.6029 | 2026-10-08 18:40:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 051f8051-a866-315a-9ad2-ff560f6a2ac5 | -3.724 | -57.1189 | 2026-10-08 18:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 6523da5e-9f51-30c8-91cc-de01a1f9405e | -2.5903 | -56.1642 | 2026-10-08 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 90e539e0-b54e-3be4-adf4-20dfbb94baf2 | -3.0799 | -58.0083 | 2026-10-08 18:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| eb7362cf-7426-3ed8-a377-9320b568dfbd | -3.195 | -42.9772 | 2026-10-08 18:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c6c8777d-8a38-3be9-96cc-dd665a849a98 | -11.7742 | -43.5245 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 211ff862-88d0-323b-bfaa-8d5ceacbd754 | -3.1787 | -50.5597 | 2026-10-08 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 28b2214b-6191-3a7e-b243-599f84361db3 | -2.9979 | -54.7692 | 2026-10-08 18:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 10e1273f-9c62-3f3c-bc24-fba53131a1b5 | -2.9449 | -54.1099 | 2026-10-08 18:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 47d734dd-3fb6-331c-b543-12f1535d151e | -11.2849 | -45.2063 | 2026-10-08 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 3f5b9e58-c9e4-3071-92cc-bd96fca56aa1 | -7.6033 | -55.7194 | 2026-10-08 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 2301b517-dbae-3f4d-bca1-8a2148ac5e2d | -13.885 | -44.1365 | 2026-10-08 18:40:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 334.7 |
| 8ee2ce46-5c48-3ce5-8783-393f6eae379c | -12.2316 | -44.7427 | 2026-10-08 18:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 616727f0-a12d-3ffd-a8e2-edb04dc6df90 | 3.7462 | -51.6224 | 2026-10-08 18:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 01ecbc65-839d-3380-824d-4458d28e4178 | -3.1114 | -53.7839 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 18d0475e-2dba-39ed-8207-f78f6822ae20 | -6.1484 | -51.927 | 2026-10-08 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 207.4 |
| e0f757ae-8ba0-3b8d-880c-6d13690cc466 | -9.1294 | -45.8405 | 2026-10-08 18:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 0f0656b4-0aa3-3891-bc34-0e23313f74e3 | -3.1697 | -58.6244 | 2026-10-08 18:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 110.6 |


[Clique aqui para ver as próximas entradas](README396.md)
