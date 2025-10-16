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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec1dea96-6c11-33cf-8f0c-28e5ea5df4a7 | -11.59145 | -44.0739 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b850a77-2cf6-33bd-b60c-520129f3af09 | -12.15812 | -45.01428 | 2025-10-16 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddd204bb-e115-3cfb-937c-af1be98bdf3e | -9.11439 | -46.04625 | 2025-10-16 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21bae1f6-2e1f-38cf-88c1-8a7d752ba9db | -10.51137 | -43.38356 | 2025-10-16 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7eb8b92d-3380-3089-bba8-1f548943b8eb | -9.15295 | -41.05599 | 2025-10-16 04:40:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| da8545d9-3c18-3a9e-868b-7f8316f05ea6 | -10.12733 | -52.34663 | 2025-10-16 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 727489e2-bc9f-370a-b44c-104bb13121d3 | -12.42576 | -48.69326 | 2025-10-16 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da9e34b6-651a-3b78-9c01-02c906196d90 | -12.60921 | -56.50862 | 2025-10-16 04:40:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6da0b90c-93d2-31dd-9a47-8501ce71d15b | -12.63983 | -44.22631 | 2025-10-16 04:40:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87167e69-7070-3ba4-95bd-19db71782fc5 | -10.70493 | -44.43118 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 281c12c9-14e6-3dba-9a95-184de8ad0862 | -8.8163 | -47.30759 | 2025-10-16 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a1e9e86a-3705-3af9-8325-5e96c74dc5a6 | -9.86301 | -48.11158 | 2025-10-16 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ca92ac1-9ac3-3397-a1f1-ec2f53794bee | -11.43677 | -44.15894 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4f948ff5-7e82-3f01-a168-f7eb50d1af1a | -11.43085 | -44.06892 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 635ddf34-34f0-3b15-b48f-e4c2d8e97c25 | -11.47473 | -44.14486 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92aa9ae3-5468-3c64-aef0-8b3923e897cb | -9.26872 | -44.35759 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 651e827d-89ab-325b-916f-b8576e8e649e | -11.45257 | -44.17443 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15128969-7de6-3775-bd90-362ce51cfbc2 | -10.81875 | -44.01371 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37114128-e309-358a-b6ae-0fa177f008bc | -11.32852 | -45.25547 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2a6f9b0-0bda-34bf-ab17-d173a4490640 | -8.27668 | -48.00503 | 2025-10-16 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63a70621-81a8-3f3a-a294-14a52bbe0a00 | -12.06293 | -51.20797 | 2025-10-16 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b508354d-2948-36d1-a69b-dd48a467aaaf | -11.59429 | -49.80785 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7be8280d-a729-312b-800f-225dd0d0f336 | -11.59089 | -44.07831 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 769d9118-1fe2-3932-8de1-5e583c08af83 | -10.84624 | -47.86952 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0100b34-d55b-3618-9417-4c808cb79ecc | -12.04668 | -47.6572 | 2025-10-16 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4399cc19-da6b-3225-8534-aef2d179cbd1 | -8.40173 | -46.26448 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7542c90d-0c0e-35d8-945f-92743e822b9d | -8.45923 | -44.18185 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 89130b5d-28ca-3975-9135-abaf5b82fd17 | -10.88494 | -47.93098 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0313c7d9-5cca-3c4e-a291-54c15d564c55 | -8.19789 | -47.01208 | 2025-10-16 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ebd279cc-7cae-31fb-b353-f08f0cf9f65c | -8.27724 | -48.00133 | 2025-10-16 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a10c12da-37ff-3ffc-ad36-394be1d12453 | -10.87391 | -47.93324 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0167f875-5418-3f7e-bad9-d82e29361255 | -14.22622 | -52.8064 | 2025-10-16 04:40:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e31fb2a8-4a65-3ad2-a71c-cc56a7fe2190 | -10.96133 | -59.12255 | 2025-10-16 04:40:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09026ff8-328e-34c4-a288-599763bb2c27 | -11.43354 | -44.14961 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 897bcbf0-6aea-3506-9ed6-62125c142a01 | -11.37397 | -49.383 | 2025-10-16 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ede03f8f-2f1b-3a0b-9046-e5410117bee6 | -8.39498 | -46.25913 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 33a2cd87-f242-3415-aec6-035f81df4466 | -10.1294 | -44.57312 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 55ff463c-f627-3caa-90ab-91da648f8ede | -10.04078 | -43.82403 | 2025-10-16 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce442de4-84df-378a-9ed7-d3d4b475cc9e | -11.46283 | -47.29997 | 2025-10-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fa53249-d470-359d-bcde-3575043f910a | -10.615 | -45.24647 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5f85a61-d49c-3dcf-8d09-a94e2828d7a6 | -10.81816 | -44.01802 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1c6bef2-04e9-373c-ab4c-0930019b4817 | -10.1239 | -52.34608 | 2025-10-16 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18380357-d29a-33bf-9822-563d752908ef | -12.38701 | -44.06206 | 2025-10-16 04:40:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11dc8188-f912-355d-8951-a1591c41c4d9 | -11.47416 | -44.14923 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80829ee7-aca0-375a-92f6-0df3f0375e3f | -12.15392 | -45.01368 | 2025-10-16 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c74f2d97-bb9b-342c-b8a8-c67d1d660ade | -10.13075 | -44.58534 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9af3f734-997a-3c16-a29f-c0cd3ea7a4ab | -9.35358 | -46.93503 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbe901e3-c832-3a4c-b00d-235fc8cf80bb | -10.67073 | -44.11342 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 052b60a6-ae61-3788-a73c-d685b6212091 | -9.81853 | -45.26952 | 2025-10-16 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 907e20b2-e2b5-3399-b998-2ab59f9819fc | -10.05341 | -43.83026 | 2025-10-16 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba343407-3e82-3003-9289-bb1869a7d28c | -13.71764 | -40.98689 | 2025-10-16 04:40:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| e633f1b9-27b4-3435-927e-ee9a17107908 | -8.46405 | -44.18487 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 18d4fdd8-2d86-371e-a433-e92be4d3dabc | -10.60781 | -47.42794 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7f906362-f82d-3b0c-9220-255cfe76147c | -9.15252 | -41.05925 | 2025-10-16 04:40:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| a5cff84d-673d-369f-98f3-2e890c28a573 | -9.54466 | -47.68901 | 2025-10-16 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2813873-e2f0-3aed-b52b-d34ce59cbbcd | -12.73088 | -50.64008 | 2025-10-16 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22b3aea6-e6fd-31bf-b37f-faaadb54b092 | -10.71319 | -44.53061 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 780891ad-fe3c-3c6b-9286-a0c1ddd64161 | -11.75373 | -61.07714 | 2025-10-16 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91998170-a9bf-3d11-9b5b-b5c666d527a8 | -10.16183 | -49.39412 | 2025-10-16 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3be2762a-d476-3235-ac6e-381fec8a58fd | -9.16271 | -46.87022 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fe169e8-207e-35e4-bac3-d10c8d01e3dc | -9.68046 | -47.9019 | 2025-10-16 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ae123b7-7345-3eed-9d8a-fcf2eb586a24 | -10.12815 | -44.57357 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9767d265-c035-31eb-bdf5-c111a6b71779 | -12.64427 | -44.22699 | 2025-10-16 04:40:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7ba5c70-d9fa-30e5-90b8-d76813f6a1a1 | -10.278 | -47.75044 | 2025-10-16 04:40:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89c11e75-b4a5-3759-9bbf-a983613171fc | -15.5947 | -42.39028 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00cab42f-9864-31ac-bdd7-8ac7ed84d272 | -9.71986 | -44.50476 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c6307891-5c1a-3e7e-b5f7-4f0da7762dc8 | -10.70121 | -44.42648 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6eca5324-4b78-316b-a1f6-c7b2a71230b5 | -10.12676 | -44.56099 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e507b2a1-3ce7-309f-b57a-5cd0071cfda1 | -12.06735 | -51.20147 | 2025-10-16 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5c77588-331f-3260-b07e-97f0c9615d3c | -9.71621 | -44.50024 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b306b4a4-71f9-30d8-80d2-5b72cf7854a4 | -10.88151 | -48.79847 | 2025-10-16 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8235c30c-8797-3ed6-a1c1-576331e1b643 | -10.84025 | -43.955 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94170dc5-3af3-3b14-b63d-af6a2db16c91 | -10.62178 | -48.98636 | 2025-10-16 04:40:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94201ff2-0de1-3fd5-bf33-1053f1bc9aa6 | -8.46826 | -44.18539 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| f662ca17-0be2-3472-9409-c76bbbe081df | -11.43618 | -44.16328 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4e41785e-0b58-324b-bf6e-1fd96331378a | -15.78505 | -43.64625 | 2025-10-16 04:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd2aa87b-8abe-3465-b8bf-128190a1cb70 | -11.47641 | -49.82209 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f0bb1b7-4493-3a56-b65b-bd68a8f71659 | -8.55056 | -44.5805 | 2025-10-16 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c22447e-e0c9-3a23-b757-6e3896f31b8d | -10.5109 | -43.38244 | 2025-10-16 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2db4c3f7-0cd3-398e-897d-2e9ff7772451 | -10.62709 | -45.24837 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 31c1d3e9-a4ca-36e5-b174-34103d2430ed | -10.87332 | -47.93724 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 183b8e74-d9f5-3948-ac52-dbeae1744490 | -14.12875 | -42.62553 | 2025-10-16 04:40:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d9ababb-cf10-3dc8-be41-95e187dc9572 | -10.60425 | -47.42739 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0fdae59-70fc-36f6-b8cc-afd2254530a3 | -10.88726 | -47.91527 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ada3599e-f5bd-3014-b1ef-57f11afbe997 | -10.50633 | -43.38184 | 2025-10-16 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9800981f-2cd2-3ecf-afc4-b1e92188292e | -15.97076 | -43.01961 | 2025-10-16 04:40:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e37d6c4f-7d7d-36a4-97a7-8a53378ad6f2 | -11.45181 | -44.01337 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 619c18b6-0422-3463-b9fe-013b7502e06c | -14.65025 | -42.38689 | 2025-10-16 04:40:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 810bca75-3b09-3235-af1a-abada77851ec | -11.45696 | -44.17509 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9d169d7-8cc3-325c-b4b8-29d71ae0aeb3 | -9.26452 | -44.35695 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1bcd11f-881c-3b48-aac7-dc3c272be175 | -9.69463 | -44.5223 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3ff4089-f76a-3f0b-a689-fb2716bf1e09 | -9.72699 | -48.1303 | 2025-10-16 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b134556e-d019-3d8f-befe-41a4a98cf0db | -11.59831 | -48.55481 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d2534e08-cf2a-3389-bcb1-b83b709f4896 | -9.25625 | -45.25837 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2337d1f-2b87-3713-9557-d4191d88ba8d | -12.17683 | -45.06526 | 2025-10-16 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70600017-afce-3302-b12d-4592616dc50d | -11.76021 | -61.07424 | 2025-10-16 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1715f9b7-4ca8-362b-8236-21be507c989d | -9.90132 | -48.1603 | 2025-10-16 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 699c5a0d-0d13-3d04-aa37-195dd9fcc7a6 | -10.53088 | -44.50684 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 292b5993-2d40-3c82-9d43-d810058b141f | -9.96068 | -49.81483 | 2025-10-16 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7162ea8e-e26e-3b47-81a9-8dff36c9fa79 | -8.29475 | -44.97285 | 2025-10-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README64.md)
