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

## Dados Diários - Página 223

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 789d98bc-82d1-3479-b4c8-1cfb33a36ebc | -3.21275 | -53.87465 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 071f481d-2c2c-3418-8ccd-25e6ebaa01fd | -3.44572 | -56.93076 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 230.2 |
| be4e6125-15b9-3428-a5b0-31953bf886df | -2.37307 | -56.13433 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae1c375b-33ac-32ed-be02-f414bffc5d98 | -4.02914 | -52.13448 | 2026-10-07 16:39:00 | NPP-375 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e0800c0c-b33b-39fa-834e-03f373262679 | -3.53932 | -54.63357 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2d16b85f-c99d-3a35-a8cd-239e7ce0cdbc | -3.02663 | -57.47704 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 88a62870-4da6-339a-a8bd-b3a566049524 | -2.93923 | -54.16978 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7ea25578-e7a7-385c-8eab-275298850b72 | -2.90526 | -54.01794 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 02eee001-a918-3467-bb07-e0e496b6aa57 | -3.19969 | -53.95174 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76deb93e-87d3-361e-9dd1-e65f7411b6d1 | -2.99107 | -54.13334 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 402441ec-977c-3db2-9ef5-947812538769 | -2.4665 | -56.09277 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 79b49fa4-a928-374a-ac8f-16734236e173 | -3.67509 | -54.28011 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 925eed3c-dbd2-3d6e-a812-b77e0a156b4e | -3.56533 | -54.22325 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6ddd0b03-7085-3b25-8801-3b912b4d3586 | 1.7625 | -55.5846 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b555ffc9-70ea-3c99-8aff-af46fb5cda46 | -3.08672 | -54.28922 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5cb45545-e845-3156-9c25-b377c80dd438 | -1.80105 | -57.11959 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 29df5900-204f-3bda-a19e-ad1b17e74c49 | -3.01943 | -54.17499 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5fc1de8b-37bc-3b6f-9b3e-9881dfb2a0bf | -3.17596 | -57.24417 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a0cece09-d443-3b93-95b7-d224798e8862 | -3.10221 | -53.76948 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0c4ac9e2-7ced-3a0d-be1e-cf8ef30fb06a | -3.10753 | -55.24955 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f94f2638-4e7f-3fa9-ab8a-a811a63cb864 | -3.50662 | -54.66193 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7249d14d-8ab1-33ba-8665-ae55ef60d800 | -3.04172 | -53.90369 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ef964b55-c912-3c77-8f6e-2c21515e73e6 | -3.96482 | -55.83872 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 73020df6-f6df-387a-bc49-26b5448ede69 | -2.93588 | -54.17298 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6abf0e01-8e60-3150-9fc6-5b792cfcf544 | 1.64789 | -55.79911 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b3b290a3-6a52-3544-b540-f2dd5241f2a7 | -3.28257 | -54.05415 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| babfeff7-9792-3115-b352-f4f441732384 | 0.61673 | -54.4229 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3930337-c212-3d49-9e08-8f476e91c7b4 | -3.16082 | -54.72186 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| f5e98c5c-cb5b-3793-b695-a2de0a814fd1 | -3.51066 | -58.59087 | 2026-10-07 16:39:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 11190600-f93f-3b1c-ac4b-c7e612dbb5c0 | -3.2865 | -54.04314 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 362a06f6-0e19-3452-8169-26d5ecacc171 | -3.98625 | -56.21604 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| b9037d37-0a21-3931-9034-dcfafc37eb23 | -2.65707 | -54.30656 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8a3ca0ed-6cd7-3056-8b39-6021b22cc447 | -3.54683 | -54.66022 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 6d08996c-fdba-3a37-b956-365ef75ec670 | -1.78159 | -55.03441 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dab7e5f0-067f-3623-b917-6f62845f2bb9 | -3.05336 | -53.90871 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 252a6d7b-e6f0-318d-bbca-1685e5db6c71 | -2.88761 | -54.12084 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f4da2f53-42d3-3f4d-a97a-867b178b32fa | -2.95025 | -54.19571 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 75351f8b-56a8-3c56-a8ff-141afe41bc65 | -3.29935 | -54.05539 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9968e1e6-e655-3d45-ac89-0fba4a6a1a06 | -3.21591 | -53.87725 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b7fd8fc4-bca7-3107-8851-3e7a71f296d2 | -3.98696 | -56.22107 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 918907ab-8cde-300a-88ec-4d38deaacbe2 | -3.53632 | -54.6532 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c6e82158-de1f-3ec8-86e3-82b55ef03114 | -2.98841 | -54.76269 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4e0e568-db4d-3515-8d36-0b706b0b50e2 | -3.44697 | -51.08408 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b5ea3170-64b0-3bf9-b3fa-c225de18eec3 | -3.28934 | -50.44405 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8481cd95-d3a5-37bf-9f5b-f87ff38776e8 | -1.56094 | -55.70932 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3e7740fa-e9f2-3917-8ed4-b2b3fe0e37c1 | -3.16494 | -50.59715 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5cbfe033-4256-306d-ae93-1bcbb86e3dd2 | -3.19185 | -50.57302 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e21818cf-e78d-33c8-8bca-c6c34cb4321c | -2.9119 | -57.63274 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1cf21e53-ca3c-334c-8178-31f4ecd5be52 | -3.19493 | -50.56447 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 38502810-b49e-372d-a332-cd271332de9c | -3.26676 | -50.40778 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| caa777d4-366f-33ab-8e62-624f1270cbf4 | -3.13727 | -54.36604 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 3a70916e-5632-3c45-b07d-528fa07b6b1c | 3.22471 | -51.29721 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80f0e7ef-37db-37df-bcfa-e04e6b8b9c2b | -2.98184 | -54.03366 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d8f9e339-5bde-334d-bcee-347173fb3fee | 1.75855 | -55.56963 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| abe09162-675a-3173-933e-1ff8dff38efc | -1.9851 | -56.25514 | 2026-10-07 16:39:00 | NPP-375 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee52e84c-b498-3b3c-a6a0-06d05dc7d6c0 | -3.85669 | -55.99066 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a499f679-ddea-3f38-9e04-e5505312ba89 | 3.4071 | -51.30113 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c29c2099-8210-34d2-a54f-de7b39f842c9 | -3.51248 | -58.59243 | 2026-10-07 16:39:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 96f22a6a-e475-3e24-817d-7b42dc6e9d8a | -1.58206 | -57.64119 | 2026-10-07 16:39:00 | NPP-375 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a3e4cc50-f031-3350-839b-138dfdc1302d | -1.47573 | -53.61312 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3bbaca09-94ef-3a59-896c-e0110c85b9b2 | -3.00641 | -54.23727 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 33cd64af-dd34-3c2a-80d1-4e292a6aafbf | -3.63033 | -55.50821 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 7f82dc58-6d85-384a-b504-b1ac9f491d7e | -2.94256 | -54.1552 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 9a6d2daa-47e3-3b69-a7a8-8be184854249 | -3.97027 | -55.83298 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 09c3f980-f31e-3f0f-be18-7c334beeae55 | -0.22166 | -48.96411 | 2026-10-07 16:39:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36938173-c084-366d-8978-e70bb193870d | -1.7189 | -55.45237 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 65817d68-59ac-3730-ad61-bba0b622fd1f | -1.47484 | -54.52289 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5e41da8-9930-3d1a-b08c-a66b1ab38821 | -4.13347 | -54.90823 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| aedd2741-e0a1-3dc7-b1a1-eb066972c220 | -2.06119 | -45.97444 | 2026-10-07 16:39:00 | NPP-375 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5d30c08b-f1ee-33a0-8911-17349f418bce | -3.26336 | -54.03595 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 524ddab1-528e-305e-a97a-76f7c0296db6 | -3.35852 | -50.76315 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a70c0a4c-a958-3f5a-b49f-79c564253aff | -3.6237 | -55.50467 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c2ec7932-3859-3b47-b84d-e4fb771460af | 3.40644 | -51.30378 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 092b50fe-8108-3931-b2d9-64ecc0d062d1 | -1.82464 | -55.09068 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 466f3716-6694-3339-b063-7b2b41b40ae3 | -3.0617 | -54.38295 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0705ff15-cabb-34ca-aecb-7e2126020ca9 | -3.84146 | -55.97315 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 3d34fa12-17ca-3548-a42b-fe9d72e4661f | -3.58993 | -55.56787 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7e08cf57-b778-34da-ac6b-f1fd0f2c37f6 | -2.75511 | -49.53057 | 2026-10-07 16:39:00 | NPP-375 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| df0d6b64-0574-3c44-a37a-be871e0f7a86 | -1.97488 | -56.05984 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fa287a8e-7144-3574-b160-04d91c0cf51a | -1.33075 | -55.43163 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f4702351-2c1c-3422-886c-0e236e212fa5 | -3.80073 | -51.02782 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3863d5b8-bd18-336e-812c-51c2e977b2e5 | -2.75531 | -57.67443 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5b2d1de8-656d-39b6-9952-cfd7e08aee1c | 0.80481 | -51.22897 | 2026-10-07 16:39:00 | NPP-375 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bb6c9575-8027-352c-8052-ea6e74f715d2 | 1.75614 | -55.58422 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2ec57695-240c-3b8e-805e-a7dea4fb1c20 | 3.22357 | -51.30429 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 279e80de-94d6-3abd-a56c-64aeb473da2a | -2.88784 | -54.15971 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2d4e5f0-a99e-39d7-a077-19014e343a2e | -2.78601 | -51.68485 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 432dc9e3-406e-30cc-98ac-fc44929d499a | -2.54217 | -56.42128 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| adea1a63-c423-3f78-a2e4-37ca3a57ba3f | -3.53364 | -54.63416 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ef982050-4c5c-308b-998f-d4a513075bf6 | -3.10797 | -53.77193 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bdea93da-a17f-38ca-82da-8573d2c950c8 | -3.85051 | -55.99167 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 44cf0823-3b2f-39f0-b1f6-2d1dc76ac3c8 | -3.51734 | -54.65627 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4035a259-ae9a-3fcd-a195-05efed43a85c | -1.13319 | -49.23397 | 2026-10-07 16:39:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d1eb2833-de64-3210-a9da-ac372a5262ba | -3.84362 | -55.98783 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 001eac99-0a44-3c90-b86e-04590d46a22d | -4.13362 | -54.90826 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5ca99e9b-4cf8-3e81-9e2d-e0534da86c34 | -2.73042 | -44.88355 | 2026-10-07 16:39:00 | NPP-375 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2d894e88-88f4-3c90-9817-2b23e302588b | -1.26645 | -55.39745 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fb70684d-8f3b-33da-8108-588065dc4780 | -3.08087 | -57.49683 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e302d91d-3604-31ef-b2ac-577527391d6c | 3.21433 | -51.31012 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 64d6df95-f175-36a0-822a-0b526af9e890 | -3.98066 | -56.22203 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |


[Clique aqui para ver as próximas entradas](README224.md)
