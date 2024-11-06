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
| d081b34a-e8a5-38f6-948b-662c85c68c73 | -2.84145 | -52.9109 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 04e8fb23-9524-3cc2-942d-00c5beaec7b9 | -3.59241 | -50.26835 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96ddb00e-0fc4-3fb8-a237-5c1bc03c4d04 | -2.94004 | -51.05534 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a3144d69-8968-30f7-85c9-b77cfa162d41 | -4.08693 | -51.04422 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60da6ec8-d233-3cb9-bade-4b6cacc548b8 | -3.22382 | -50.38564 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 822ac8a0-67c0-3e17-864a-b3635f7e382f | -2.6714 | -51.8215 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 89241ca8-2cf8-3b5b-9b9d-34d79892e5af | -3.48816 | -50.38363 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c1ed509e-4b45-30e2-8a70-8598e08576cb | -2.92382 | -51.04632 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1fb4769d-67db-32f5-8412-fcb1d2b45e9b | -3.48141 | -50.38726 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e932dd3f-38d9-3404-9f6c-4761927130f9 | -3.02902 | -53.26619 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 28e7f781-8290-3153-a86d-30a1db3a1e39 | -3.52924 | -52.99607 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44174ba4-a257-35e9-a035-025291e993e4 | -3.21513 | -49.22791 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 394b1715-ac7a-3815-8e01-feea37c08e44 | -3.52943 | -50.35686 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb06120c-765d-3bff-8c21-0874db433e6c | -3.62651 | -50.24957 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e351b6e9-128c-3444-88dd-fbcac3621614 | -2.3927 | -50.32464 | 2024-11-06 05:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 176a1889-2073-3c2f-a59e-9fd71a7f5407 | -2.99565 | -54.13015 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18c009c8-61d5-3e91-bda6-ee23f5f5ed39 | -2.88369 | -51.31191 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d393e55-b0df-3db3-a5f4-a3f274e00b17 | -4.27351 | -50.71698 | 2024-11-06 05:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4bd5431-402e-3523-bf0a-d694effff917 | -2.62293 | -51.73069 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 248f7cae-1a01-315e-bc54-f9b8308a6d3c | -2.38476 | -54.41136 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 59f5e70f-4a20-3ea9-9d6a-724d17992c11 | -3.17966 | -53.85186 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5529eab4-e5fd-3c56-b15b-ccbdd8cd4e7d | -2.58534 | -54.00071 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7e13980-6488-3928-938d-545389384635 | -2.8446 | -51.79622 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90ca46a6-8d6f-34c2-a269-ac2892a36722 | -2.95898 | -53.71849 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4fa18f6-2c03-3d5d-854f-f9f29e8925d2 | -3.02911 | -53.26666 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| efb5c0fe-1256-3fb9-930b-2e8ab85aefb9 | -2.83857 | -51.79892 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90b247f8-c65d-3b92-a756-c974076cdbd1 | -2.99802 | -54.12767 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89f7e951-4795-3015-9813-179796901d36 | -3.00568 | -54.09588 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66583822-1381-37ce-83a1-fceb899c69dd | -3.05673 | -51.07231 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72aadb40-a3f8-3f4d-8a7b-ff97510c3490 | -3.48206 | -50.38275 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 24220016-85f0-3399-b141-f207e59a876a | -2.48267 | -53.9866 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db754a26-f2bd-361e-a33d-8041a4a74a6a | -11.79145 | -64.85268 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9c7e776-5ef9-3b33-b83c-ea2184ab3054 | -9.44783 | -68.53374 | 2024-11-06 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 913e03e9-2331-3c3e-9e42-d4d1411b22e8 | -0.74755 | -62.89902 | 2024-11-06 05:31:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9233124a-9f8f-3cea-a7de-2cbd1e467275 | -2.75471 | -53.21576 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe0b554a-c9fa-371b-8d13-307c22545ae2 | -2.83076 | -52.91254 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 61fcf68f-a828-31d0-9777-037300274500 | -2.93423 | -51.05635 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d97749c6-43e1-3c69-9c62-77fe1fecf649 | -3.66179 | -52.34293 | 2024-11-06 05:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 834f4dea-046f-3a6d-b1ae-85448b7bfaba | -3.68287 | -49.85589 | 2024-11-06 05:31:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6432ee15-a2d6-33c6-8f2d-f242f0443582 | -2.60854 | -54.54487 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 982b17cf-af77-309a-af5a-abe016777b18 | -3.24585 | -50.02163 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 27c1c658-6e70-3167-827d-3218ebf733ef | -3.59226 | -50.27039 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 071e6d8a-ff66-3ce6-8e7a-ca4aeb7f6178 | -3.6662 | -50.23641 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d6f3a4da-0a67-3101-bbf6-e3a89143d9fc | -2.84322 | -51.3494 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| adcdab17-0e70-369e-a9c8-1ecb26384830 | -3.96645 | -48.1588 | 2024-11-06 05:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e226b5b-97db-30b9-af5b-3478266b02c4 | -3.22577 | -50.37947 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 15512888-5e73-3d7c-8a3c-f5071e0cfa38 | -2.65606 | -48.56875 | 2024-11-06 05:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 242ac7e2-2d84-369e-ad6a-af24ae8a960e | -2.84884 | -51.76707 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| df597e9b-8a39-339e-beb8-caf07142114e | -2.85382 | -51.7716 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| bdfd920e-b1fd-3273-b3e5-2311aad5eda7 | -3.02092 | -51.4399 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23755c34-5982-3376-910a-9c32a681fed9 | -2.82858 | -52.92714 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2a0ff340-6fc3-3099-9172-95e087947ea3 | -3.55776 | -51.50774 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21199e57-0b4d-37cb-96d1-6f78444cb820 | -3.72774 | -53.39296 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b107aa9c-c9bb-3f00-b1a8-8d245aa916c1 | -2.78212 | -51.60765 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0c603c2-f9ce-3188-af19-44b0419e6c02 | -2.81898 | -52.95648 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 71424d89-4a65-3dfa-9917-03d7d90ffecb | -3.53899 | -50.29121 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 349151e3-7a91-3d15-8c67-58661a10ee6c | -3.12565 | -54.2548 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f8ccc781-fbd9-3999-b24d-da21d038a32f | -3.01634 | -53.42546 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d1ef974d-b794-37e8-8875-3c3e8f522185 | -2.65194 | -48.5675 | 2024-11-06 05:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d396cff5-8e0b-315d-8311-706466905266 | -11.77035 | -64.98441 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4bfadbc-339f-3f80-8e44-0c5d8825f103 | -3.12322 | -51.10349 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2aa018f1-8710-3932-9a9b-26e46c56e847 | -3.03402 | -53.26696 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 71a7e98e-c139-325e-91a8-1cfda01153f1 | -3.96402 | -48.16267 | 2024-11-06 05:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6b1298af-4077-39d4-810c-dd85de0dd227 | -2.94066 | -51.05121 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 45f7cf03-c6a7-35c1-9e01-a2ca2841ad6f | -3.10262 | -53.71005 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 846e89b6-5feb-32eb-858f-d3187119c839 | -10.67661 | -63.01245 | 2024-11-06 05:31:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b8aa80c-9cec-30d6-a91d-56515afbab55 | -2.4848 | -53.98324 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62c52504-76c1-3655-bfaf-524ce0cbe68f | -1.49072 | -60.18547 | 2024-11-06 05:31:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db8913f0-9496-3f06-8aa8-aa92c0bb2d92 | -3.12305 | -51.10696 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e40621a5-8506-3002-994a-e06e5c7a5ea8 | -3.03878 | -54.21027 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0508211-329c-36ad-bf01-cd8eee7960c6 | -3.18244 | -50.58228 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d83280f6-03bc-35a5-aec6-5e2c09924988 | -3.0985 | -54.28978 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33ae7c4f-7962-3e4e-9205-59f060c64099 | -2.77748 | -54.73396 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9d6e1ea3-69a3-31ab-93f8-5b6fcd8d9746 | -2.78769 | -51.60853 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f08b325-478f-3e11-a7f1-187a42f7fd4f | -3.23468 | -53.39724 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c3671398-f931-3f88-b166-1d394e998e74 | -3.58627 | -50.26733 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9344712d-d4b6-3bc5-a1ff-ee34f171946e | -2.97967 | -50.29863 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46e74950-d62e-381f-8260-f5e23875bdf0 | -2.58381 | -51.9234 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50e26299-55fd-3308-931f-692682594cc0 | -2.8071 | -51.78282 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e9553d7-35e0-39fd-9bf5-f199a321e8e9 | -3.45047 | -50.38125 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 748d3593-4169-3173-8501-5794a6227ce8 | -2.88742 | -53.97297 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cde5812-061c-3c63-9381-64016b9f4a64 | -3.09216 | -54.51501 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0b1c02a-6007-36f8-b5c8-39812d163657 | -2.42856 | -53.66349 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02bbe364-339d-3134-85ea-09e6ef4dd31e | -2.82304 | -52.92926 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 766b0b59-4925-375a-9517-f26959f5e944 | -2.66371 | -48.56366 | 2024-11-06 05:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93c08aad-12b6-37c6-8dd8-7dde6e1f4081 | -3.09989 | -50.24761 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59a349ce-7596-3fc1-adc1-2b179ce4a6bd | -3.65729 | -50.2543 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea2837f4-6f83-39dd-8bc3-631d8f7dc816 | -3.01554 | -53.43096 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1fe5c14d-1bd5-3ac0-9313-ca483abf16ef | -2.9297 | -51.04533 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c80ab969-1f42-3c90-9e6f-c880f357c38d | -2.99641 | -54.12518 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0519c6f7-1240-381d-a5f0-79551c722087 | -2.82029 | -52.9477 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2eec9af2-a2b7-3883-91b0-f51a78e45e65 | -3.14994 | -51.32845 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d48a68a0-d65b-3ac1-a697-bb8e03c68ecf | -3.35054 | -50.25108 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2abd223-eb7b-3e1c-a53e-a4343137f8bc | -3.11618 | -51.11098 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4f9fae3f-6ceb-397a-91a6-cfdd9f1a1ba2 | -3.20811 | -49.22681 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48a6ec05-5583-3c2f-8734-d17100b7b095 | -3.03369 | -53.27037 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c4afdfe8-a78d-3d7e-894f-97f54cd86629 | -3.10059 | -50.24277 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1c33fb2-68d8-31ff-af91-6136d52e88a8 | -2.72732 | -51.71214 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0623c635-b37e-3dd6-9972-a64a9728a17f | -3.20441 | -53.22435 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c846049e-0931-35c3-a2c7-664d7948e627 | -2.81568 | -52.94372 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README64.md)
