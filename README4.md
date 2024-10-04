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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ac1bc06-b9fb-33e3-8177-fffae4203ffb | -4.095 | -48.4679 | 2024-10-04 00:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| a40fd4ef-5e82-3a59-bee9-4a09dcaafeb8 | -4.4657 | -42.8877 | 2024-10-04 00:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| d88631ba-c6c1-3c9a-87ee-0f19e8341b8a | -4.5375 | -43.304 | 2024-10-04 00:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 132.6 |
| b248c2d5-712c-355c-9fe4-f7a322cd17da | -4.5949 | -45.7436 | 2024-10-04 00:25:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 34.1 |
| c8c5619e-ffb5-3c3f-9a72-2d70b365aa40 | -4.6684 | -45.8961 | 2024-10-04 00:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1ff6f99f-c73b-3cee-a73a-a8cc52c32a5b | -4.6686 | -45.8738 | 2024-10-04 00:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 92.6 |
| a28fb465-584c-34ec-9c1e-3dbaff41f1c4 | -4.687 | -45.8951 | 2024-10-04 00:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 416689eb-9094-3204-94b9-529983ff9b52 | -4.6872 | -45.8727 | 2024-10-04 00:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 0cd7e039-dc0d-34b7-97c6-e9f887cb69ee | -4.6873 | -45.8504 | 2024-10-04 00:25:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 254ddce2-8da9-3181-adca-67a530d90142 | -5.5033 | -48.8046 | 2024-10-04 00:25:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 698e3cb8-a40a-3b20-8bcd-e589620581bc | -5.8214 | -44.1426 | 2024-10-04 00:25:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| b8f73bfb-e7fd-3241-9c00-52557519d653 | -5.8216 | -44.1196 | 2024-10-04 00:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| d984ff2d-4f70-30dd-939e-10ff99782560 | -6.2524 | -44.132 | 2024-10-04 00:25:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 425b6a02-caad-3d36-a044-6faaebe6a2ee | -7.4557 | -72.6984 | 2024-10-04 00:25:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 1d4ca578-e99c-3a14-886a-82adf657950e | -7.8539 | -45.3611 | 2024-10-04 00:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 18701466-7d99-3c8f-bc65-b9c860b8fa9e | -7.8541 | -45.3384 | 2024-10-04 00:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| cfc15ee3-19d1-3ef1-83ff-88369458faac | -7.6325 | -67.2198 | 2024-10-04 00:25:50 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 27e80cff-b7c1-3c5a-82d2-fcc191189b17 | -7.6326 | -67.2013 | 2024-10-04 00:25:50 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| edc5d030-8b8b-3a7e-94a7-4a23ed393244 | -7.8164 | -50.543 | 2024-10-04 00:25:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| a6d9a88d-423d-3b60-af88-33d81726273b | -7.8166 | -50.5219 | 2024-10-04 00:25:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 010ea4d9-5772-3178-9e47-0df146b9701e | -7.8351 | -50.5416 | 2024-10-04 00:25:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 88af60cc-9d61-3ff4-8d76-da692fac8422 | -7.8353 | -50.5204 | 2024-10-04 00:25:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 98acba2b-cbc0-3207-b695-227c946bac4e | -8.2986 | -50.9059 | 2024-10-04 00:25:53 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 4426ce60-91db-3f74-8849-ff02b0ec8f21 | -8.6448 | -50.0518 | 2024-10-04 00:25:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7005c29f-983c-3603-8680-7c444adf8593 | -8.6636 | -50.0501 | 2024-10-04 00:25:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 22b7d42d-568b-337d-86f8-0807e870b431 | -8.6492 | -66.621 | 2024-10-04 00:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| f37db881-11d4-3236-a1f6-944bdc6043ee | -8.6677 | -66.6205 | 2024-10-04 00:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| a6310291-84d7-3d84-9592-28182fc30178 | -8.6677 | -66.602 | 2024-10-04 00:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 1cc23822-c6df-3afe-b3b7-421401ca67f8 | -9.1158 | -51.5315 | 2024-10-04 00:25:58 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0bfc99a0-9074-3a3c-ae67-a0c8a6045384 | -9.2927 | -50.8219 | 2024-10-04 00:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 9edb24a2-f043-3743-85be-931bb5a73fb4 | -9.293 | -50.8008 | 2024-10-04 00:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| dd5b189b-ae84-36df-a628-07f0be88406a | -9.3115 | -50.8203 | 2024-10-04 00:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 397.1 |
| 75d41aac-5126-3921-85ea-15f5f6df59ac | -9.3118 | -50.7991 | 2024-10-04 00:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 462.4 |
| b34c18ab-f83d-3ad0-a020-77dad49a6919 | -9.3303 | -50.8186 | 2024-10-04 00:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 196.0 |
| f74c7ccc-f134-3143-a4e3-1ccf12bc92d0 | -9.3306 | -50.7974 | 2024-10-04 00:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 237.7 |
| 5c66f2f6-178d-37d9-a362-b764b8c7bc82 | -9.5686 | -64.2171 | 2024-10-04 00:26:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 5e222d8c-b758-3e9d-9cc6-034d56cc6421 | -10.9 | -46.5991 | 2024-10-04 00:26:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4340402e-2f33-36da-afea-416db48e93b2 | -11.0532 | -46.5344 | 2024-10-04 00:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 293c3f5f-6e2c-37d5-96b6-f3762f1401ab | -11.0536 | -46.5118 | 2024-10-04 00:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 3b72e3a6-a568-36a9-9bd8-57e840e1afbc | -11.5238 | -65.0615 | 2024-10-04 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 46d56f87-0e55-371e-a06f-615f8c815907 | -11.5425 | -65.0607 | 2024-10-04 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 4f67ed7e-89d5-3e9e-9c20-598c95a26530 | -11.5803 | -65.0212 | 2024-10-04 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 202de8a4-fa9d-32e0-9f3e-61d9c1e1724d | -11.5991 | -65.0204 | 2024-10-04 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| b356e38b-4d4a-36fe-b155-b0ae5e61db66 | -11.5992 | -65.0015 | 2024-10-04 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 88c0dc49-63cd-3df1-bdda-c22c82d5fdab | -11.618 | -65.0007 | 2024-10-04 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 5cafea6a-04c2-3aa8-9270-1e3fd4dd0a08 | -11.6181 | -64.9818 | 2024-10-04 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.7 |
| c67a02ff-687e-3e22-a311-9446bb0ed99e | -11.6369 | -64.981 | 2024-10-04 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| b91737fd-28fb-3209-9ed4-6f458eee1f1d | -11.6932 | -64.9785 | 2024-10-04 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 74e7e59c-0404-37fe-b49e-6bd5edac4d5e | -11.8052 | -56.6024 | 2024-10-04 00:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a626ae0c-3590-3ebf-a364-2b250c1213ab | -11.8242 | -56.6009 | 2024-10-04 00:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| cdb294b4-9590-353a-9008-57f451ddb5b6 | -11.8244 | -56.5808 | 2024-10-04 00:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b0afeb83-0b31-30e1-b571-03e3958d72c1 | -11.8957 | -56.9554 | 2024-10-04 00:26:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 5e0aeabb-423e-3dab-9a16-327da0a460c3 | -11.9147 | -56.9539 | 2024-10-04 00:26:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d3084e60-7324-3b04-a28a-14c697680137 | -11.874 | -63.2784 | 2024-10-04 00:26:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c80b8612-6d64-31ed-9167-61eafb7d297d | -11.8928 | -63.2774 | 2024-10-04 00:26:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2c409b82-2aa2-32a0-a253-4af9af630e2b | -12.4225 | -63.019 | 2024-10-04 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 61a68c78-bc92-3a50-b446-c61e5b82bc57 | -12.4227 | -62.9999 | 2024-10-04 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 425f4291-708e-37d4-bf94-7df22a1844a6 | -12.4416 | -62.9988 | 2024-10-04 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 6dc49c3f-1cff-399d-957d-d377ff80fedc | -12.5898 | -53.1359 | 2024-10-04 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| a6ec1e50-d953-3dfa-bb38-a41ddf878c36 | -12.5901 | -53.115 | 2024-10-04 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 31873d7d-b583-3b62-ab98-f77559e62ffe | -12.6295 | -63.1225 | 2024-10-04 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 525fc5a7-43e6-3b60-9eec-7efdb0fd5fb9 | -12.6296 | -63.1033 | 2024-10-04 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5c2c7bee-7124-39dd-b5d6-e1caf931268e | -12.6484 | -63.1214 | 2024-10-04 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ba1d3084-6224-3337-9af3-9c5827f0b20a | -12.6486 | -63.1022 | 2024-10-04 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 9dba2c90-043f-360e-ae5e-d03e85575b4b | -13.1587 | -48.6764 | 2024-10-04 00:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 89b4d7d1-add8-3613-9be3-8ca4184147e5 | -13.0594 | -51.1409 | 2024-10-04 00:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4c87be79-9e49-3f66-bad5-933c225fe5a2 | -13.0786 | -51.1385 | 2024-10-04 00:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 1a28e348-db57-39ac-a055-1510c189ae0d | -13.0971 | -51.1789 | 2024-10-04 00:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 23031810-0ddd-308e-b93c-78f62125c851 | -13.0975 | -51.1575 | 2024-10-04 00:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 231.6 |
| db83ed3e-1aa0-3186-a83f-ae12b8537827 | -13.1163 | -51.1765 | 2024-10-04 00:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 9cc69dde-7e5d-3406-895e-510b712873c0 | -13.1166 | -51.1551 | 2024-10-04 00:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 45a3dc11-3e75-3b9a-973b-bdb816c23a4b | -13.3976 | -61.957 | 2024-10-04 00:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a55b104a-4c44-3ef9-bb14-1a47e5e9808e | -13.6143 | -51.22 | 2024-10-04 00:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 0b2655f4-ca2c-34ef-b68c-3ef1fb985d21 | -13.984 | -44.0474 | 2024-10-04 00:26:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c9cde9e8-7b1b-37f2-be77-e0b2897b3928 | -13.9845 | -44.0236 | 2024-10-04 00:26:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 1353797d-6212-30bb-8e43-2a884aabc8dd | -14.004 | -44.0201 | 2024-10-04 00:26:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| cf34b159-c0fb-3653-9dee-e3b4a6f8bea0 | -14.7939 | -48.0275 | 2024-10-04 00:26:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| a204a727-9d23-3153-a2ab-364e4b0c4a47 | -14.7944 | -48.005 | 2024-10-04 00:26:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 20a58016-6771-392d-bce8-5578a72e0e98 | -14.8134 | -48.0243 | 2024-10-04 00:26:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 49a72f22-fdbc-3c41-87ce-350b5d98ccfd | -16.4554 | -57.2962 | 2024-10-04 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| d4e7e460-fdd8-3c98-87ba-7a92d72dcf3a | -16.475 | -57.294 | 2024-10-04 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 7b76be1c-dd75-3125-9af5-8050b3549269 | -16.5783 | -58.198 | 2024-10-04 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.1 |
| 21f0dfd9-cb6d-3a82-aebc-25da3565a7e8 | -16.5935 | -57.1988 | 2024-10-04 00:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| d96236e1-90a3-343a-a2d4-2522f2d02899 | -16.5938 | -57.1783 | 2024-10-04 00:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.0 |
| 1336a443-a732-3c7c-a0db-ecfb25a6edec | -16.9302 | -47.1224 | 2024-10-04 00:26:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 4e37c360-9346-3774-8912-4b9f9edc59cc | -16.613 | -57.1965 | 2024-10-04 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 52ef2be1-a517-3834-9b1c-55afe3302e12 | -16.6133 | -57.176 | 2024-10-04 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.8 |
| 21ead4a6-212c-3000-9832-78ca739a75dd | -16.6527 | -57.151 | 2024-10-04 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 9a408b68-14c3-3ca1-961a-6684b533c5a3 | -16.6727 | -55.9141 | 2024-10-04 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 127cebd1-9912-3f77-92ca-f7927e3fca85 | -16.7606 | -57.7512 | 2024-10-04 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| db171f2b-6bf9-3622-8b9f-4a251cc4cf6a | -16.843 | -57.4767 | 2024-10-04 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| ae64cf8b-486d-3392-a4c8-c53a36bf0ec6 | -16.8433 | -57.4562 | 2024-10-04 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 06ed8474-c8f6-380c-8e4a-f4f9ac5d2769 | -16.9087 | -55.843 | 2024-10-04 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 2aa8de5c-f077-3ada-ab49-274ae930a8d4 | -16.9283 | -55.8405 | 2024-10-04 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.2 |
| eb125649-99a9-3713-ac6f-22d62f6a400f | -16.9287 | -55.8197 | 2024-10-04 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| da7d356b-7092-3901-8df4-57b22683872d | -18.8413 | -42.8985 | 2024-10-04 00:26:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| b1e1128d-97ee-3229-b3e3-9f62478758b6 | -18.8617 | -42.8932 | 2024-10-04 00:26:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.8 |
| 7769e506-2422-312f-a95c-c40f75610b1e | -18.8613 | -43.5837 | 2024-10-04 00:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| 53ef05d0-c0d1-352f-97fe-87ad8c82943a | -19.0344 | -43.1944 | 2024-10-04 00:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.4 |
| 80772229-b003-35f4-bba0-c84b3b2cbdb1 | -19.0352 | -43.1695 | 2024-10-04 00:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.1 |


[Clique aqui para ver as próximas entradas](README5.md)
