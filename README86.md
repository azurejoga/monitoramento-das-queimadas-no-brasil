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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72a83692-172d-38f5-a188-5bb2872e9bd5 | 3.16832 | -60.34196 | 2025-10-18 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a25285a-51ba-3777-b3db-0c3c77dc5cc2 | -2.87611 | -50.7243 | 2025-10-18 05:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e3665c3d-fa00-3ca5-9ec1-61f66d4eea56 | -2.12013 | -56.88442 | 2025-10-18 05:40:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e495731-793e-33b4-b963-b1ead1004a16 | 1.75695 | -55.98405 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a696f6cd-d704-33fd-b742-1d1af82d0b9c | -3.20233 | -58.9117 | 2025-10-18 05:40:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bfe9bd9-0e1d-31f2-8bbc-79ba71a7590f | -2.12313 | -56.60839 | 2025-10-18 05:40:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3fbc983-ba4d-37d4-a724-193ac2714d69 | -2.86697 | -50.73722 | 2025-10-18 05:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2c4dfb9a-1857-3b86-8956-ea324a60d801 | -2.53248 | -57.83469 | 2025-10-18 05:40:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ca6e046-4aed-36a7-8e66-09600fe47a32 | -2.81392 | -54.38107 | 2025-10-18 05:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f76aabf-e0f3-304a-aff9-417f223ee46f | 1.8026 | -55.71556 | 2025-10-18 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15c61f08-fff3-3601-baf6-5df1875be820 | -3.86465 | -51.90556 | 2025-10-18 05:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a4e0007-af25-3b23-bb7c-35b7ae033c0b | -2.87407 | -50.73836 | 2025-10-18 05:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac075e58-81aa-3851-8924-c5300c9111c2 | -3.41406 | -59.63046 | 2025-10-18 05:40:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60552a5c-d0c5-3c8d-9091-4e39de3e43ff | -2.81452 | -54.37706 | 2025-10-18 05:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc305328-58aa-3015-84d9-2794fa7f32cc | 1.76174 | -55.73872 | 2025-10-18 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c8e9167-3ea3-3637-b4b2-698e4f39c0bf | 1.76479 | -55.97237 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c95d8fc6-cc4d-3c75-84c6-942a722b8170 | -2.81669 | -54.38108 | 2025-10-18 05:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79ee4d3b-d79f-3813-99de-edfbc0b446c4 | 1.75448 | -55.96878 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2750139c-859c-3b7d-b1fc-2a7f46b305c5 | 1.76935 | -55.94015 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0959475a-4a26-30c9-aa9b-ad138b4fbfd3 | -3.80159 | -51.65003 | 2025-10-18 05:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8090e741-f865-31c2-a30a-77607654ea74 | 3.72099 | -60.23161 | 2025-10-18 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84ce95a9-05da-3a79-8b2b-963ee30e7f06 | 1.16322 | -60.67229 | 2025-10-18 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d216d464-5329-3857-b00a-4277abe5a03f | 1.76168 | -55.98323 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54c8cecd-63ac-3963-9e19-b095bd0f6b46 | 1.75778 | -55.98916 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 68e38848-2d5a-33d8-a9a7-272e5da89b8d | -1.42328 | -60.40075 | 2025-10-18 05:40:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0268571d-42b2-35ed-8d2d-243582cceae6 | -2.91585 | -52.72963 | 2025-10-18 05:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d43e562-bb18-3494-a977-ec1bb3efa163 | -1.56011 | -60.14215 | 2025-10-18 05:40:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84efa54a-337d-3e52-8cae-9deeacea6050 | 1.97444 | -55.93059 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7f4b487-49ab-3e51-8e1c-10c2808d2ba0 | -2.90959 | -52.72825 | 2025-10-18 05:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8f6aea13-f48f-3c4f-9ec4-8091a7e8cf00 | -2.69796 | -59.42911 | 2025-10-18 05:40:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0b2a940-ec6f-33ff-8df7-776214baed4b | 1.76086 | -55.97818 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd6ddebb-a2f0-33dd-8bd8-dde4f527cd83 | 1.7656 | -55.97739 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 536065b7-333c-3855-b6fc-1b77feaa91e8 | -3.79256 | -51.76265 | 2025-10-18 05:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8273afca-97fa-372d-80c5-aae252830b1d | -3.77371 | -58.5378 | 2025-10-18 05:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d73fb21c-c6cc-38e4-8fa9-fe6abc54b4bb | -2.48816 | -58.06556 | 2025-10-18 05:40:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1571581b-c59a-3814-bb91-d1dede48685f | -2.12097 | -56.88694 | 2025-10-18 05:40:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23758000-b6df-31e4-8b89-02dfd1eeed3c | -1.41956 | -60.40018 | 2025-10-18 05:40:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 39f6535d-03d7-3243-9ab1-00bfcca9d477 | 1.7553 | -55.97387 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 00d4134b-14df-3e3f-83f6-c42fa7b74c01 | -2.78268 | -58.14267 | 2025-10-18 05:40:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b35f964d-5ace-38b0-9822-56720f75976a | -2.3285 | -57.0282 | 2025-10-18 05:40:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e65df50-c1c5-37a7-8fdf-41610445346d | -3.97912 | -59.16636 | 2025-10-18 05:40:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d742254c-0e75-37af-a2a2-bb79233af462 | 1.16315 | -60.67088 | 2025-10-18 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 796b734c-b555-3285-9795-d716464008c1 | -3.65736 | -58.7962 | 2025-10-18 05:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 786aab69-ad26-355d-a903-b28d07b58d11 | -2.86596 | -50.74419 | 2025-10-18 05:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 95f0b154-5bd1-3859-a60f-b1a5d4b0fbef | -3.482 | -59.45947 | 2025-10-18 05:40:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cddc649-a436-34b3-b143-afe451f32d93 | 1.7657 | -55.73249 | 2025-10-18 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8702cf7-420a-30f1-9504-07c52e248efa | -2.60756 | -59.41908 | 2025-10-18 05:40:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1637f40-5552-33ee-a11a-63a5bbb0f1ee | -1.56081 | -60.13752 | 2025-10-18 05:40:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7e97eea-3794-3746-a13f-0b66adffd8a8 | -1.3819 | -55.34975 | 2025-10-18 05:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25fc4436-8ead-3ed4-87e8-f6076c0d3781 | -0.7906 | -60.25136 | 2025-10-18 05:40:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc8b5286-919a-3b46-99ee-4a5f7a0baa1e | -2.81726 | -54.37707 | 2025-10-18 05:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b421e63a-0d47-30d2-bb31-6f20b893e2f3 | -3.48606 | -59.46008 | 2025-10-18 05:40:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7281aeab-5172-33a6-9d06-53790ef08ccd | -6.36547 | -58.21055 | 2025-10-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f66886c-fb6a-3dc6-933a-0f2d4f5e6a5d | -6.93283 | -59.52861 | 2025-10-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9c1f8b8-06f3-3ba4-853f-5e494fffbf29 | -8.94435 | -65.9326 | 2025-10-18 05:42:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d952c59d-330b-36e3-99bf-7901236d4c0b | -8.652 | -63.74675 | 2025-10-18 05:42:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe231eaf-88bd-3073-8946-d69ea8ac65e1 | -6.36076 | -58.21348 | 2025-10-18 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c078405-b9ab-370f-a794-574c8bf914dd | -5.57861 | -61.49335 | 2025-10-18 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1f55d4c-fa03-355f-96d7-261f0ac6d5e4 | -3.51433 | -65.18249 | 2025-10-18 05:42:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4076537b-dcfb-3d0f-8c29-0356bed6e7b7 | -10.33961 | -57.38501 | 2025-10-18 05:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ab92962-1091-3f76-8938-af1197bb9ed1 | -6.93223 | -59.53264 | 2025-10-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 831bfd6c-cebb-398b-a8dc-16a61644b30c | -4.19009 | -63.16356 | 2025-10-18 05:42:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3944d018-8aeb-3fbe-ac27-eb9bf45b6726 | -9.29895 | -64.22385 | 2025-10-18 05:42:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09fa0782-9aeb-355d-9aca-35112821e83c | -7.80093 | -54.93419 | 2025-10-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5fe287a-418c-3552-9c20-16e1d411c8ac | -6.94211 | -59.61298 | 2025-10-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72c64f69-801a-37a6-8e26-aa3d26de20b3 | -7.60132 | -60.97478 | 2025-10-18 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d68b904c-9f67-3295-b2b0-dfb726059c55 | -10.46901 | -55.58952 | 2025-10-18 05:42:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9423a508-d89e-3fc4-a381-31582b958169 | -6.76457 | -56.86255 | 2025-10-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3321f47-ab89-36f6-be6e-17704e66dd3e | -7.80037 | -54.9385 | 2025-10-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e8ded92-01a2-38ba-b84f-2a603a040a3e | -9.36057 | -60.85983 | 2025-10-18 05:42:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 435327b1-7f62-357f-93f1-becb6a7c8be2 | -6.97034 | -59.86232 | 2025-10-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3e8a97e-5249-3c5c-860f-17c0acb29c24 | -9.70959 | -61.92006 | 2025-10-18 05:42:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdca0c6f-7486-38a6-979d-369dc9d105dc | -9.72137 | -63.23227 | 2025-10-18 05:42:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb45b584-4e28-3502-89dc-8fbe93d26b5b | -7.68385 | -61.04409 | 2025-10-18 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 746e4037-e439-35ee-aaaa-2d617b90030b | -8.62786 | -63.42121 | 2025-10-18 05:42:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4833cca8-a7b1-365a-aa87-73f173c4cfb8 | -8.94765 | -65.93312 | 2025-10-18 05:42:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aaf32051-22ea-3a3b-aac5-7bdcacda1287 | -7.86771 | -55.3766 | 2025-10-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbfea89d-d1b1-3cec-a981-15cb462cb915 | -7.68684 | -61.04306 | 2025-10-18 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4bba8acd-b861-3b3b-a82a-27ff4f1053c3 | -9.22364 | -61.82851 | 2025-10-18 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62d5430b-cf78-3d78-9c21-203859e3c5ab | -6.36607 | -58.20941 | 2025-10-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 833f3db6-c99f-332d-b7ab-739f4f2249bb | -9.29556 | -64.22332 | 2025-10-18 05:42:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b5aba28-383e-34d2-8864-cec473259e16 | -3.53165 | -64.46368 | 2025-10-18 05:42:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb7e8aa2-6027-38c7-8f95-b661296eed99 | -8.63537 | -54.71403 | 2025-10-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a621f11-5962-3d01-904b-071cb6021663 | -7.49483 | -63.5139 | 2025-10-18 05:42:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 892a9d7e-7101-3695-a723-51725357b64b | -5.74677 | -63.15386 | 2025-10-18 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 417ea6ff-5c47-3b42-a03e-2d88e798229c | -9.53777 | -62.95797 | 2025-10-18 05:42:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1114861-d13b-3536-a3f7-4c389f02fd95 | -5.74335 | -63.15334 | 2025-10-18 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6fec33f-05df-361e-a02b-0e14cb2c0705 | -9.5342 | -62.95742 | 2025-10-18 05:42:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d46ca9e-1360-33ff-a6de-3fb0aec6852c | -6.36086 | -58.20985 | 2025-10-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bce444f5-539c-37f0-9f0f-da72c97aee0e | -5.10112 | -56.15472 | 2025-10-18 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be0dfe33-4133-3f10-a496-78cd145b9847 | -8.58569 | -63.37135 | 2025-10-18 05:42:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4075855e-ca0d-3d9d-b5bc-8bca08e4f607 | -5.74733 | -63.15014 | 2025-10-18 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b1f85bd-032d-35b7-8b86-2adb03146840 | -7.68773 | -61.04469 | 2025-10-18 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f5ae9ba7-f687-37c9-871c-29a0afa63f07 | -9.71784 | -63.23172 | 2025-10-18 05:42:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d7a5590-9a58-3f83-80f2-c98879665e46 | -9.43902 | -63.68921 | 2025-10-18 05:42:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 497bc3b0-68e1-3656-9032-c7ba534d43b1 | -8.10696 | -55.08646 | 2025-10-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 87e4f9a5-2812-3006-8e02-c383ab0846bc | -6.76967 | -56.86329 | 2025-10-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7410f91-dbbb-390d-b60c-9c95a052a703 | -9.16007 | -62.08591 | 2025-10-18 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ae6bdc6-2eda-3b37-bc0b-70043d296137 | -8.62939 | -54.71283 | 2025-10-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 432e360c-b8e3-36aa-aaf1-bdecc0c596e1 | -10.46953 | -55.58993 | 2025-10-18 05:42:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README87.md)
