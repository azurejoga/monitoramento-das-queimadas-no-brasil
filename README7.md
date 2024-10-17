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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c556454-192a-3ac0-9f24-377e36049b66 | -1.2361 | -47.702301 | 2024-10-17 00:22:31 | METOP-B | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd94ae3f-f5b6-3f2e-bd8f-33748aec4190 | -0.9975 | -46.780399 | 2024-10-17 00:22:32 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3800f072-ada9-3b08-a6e8-f931c0d1be36 | -2.0031 | -52.088799 | 2024-10-17 00:22:35 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e248b37c-9ed7-3fae-869f-80c08c93c106 | -1.9934 | -52.0909 | 2024-10-17 00:22:35 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 785a234c-de3e-3f47-bd18-8d892e91f8ae | -1.0542 | -47.992401 | 2024-10-17 00:22:35 | METOP-B | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d5dd844-df63-3533-aaa3-68464ce50211 | -1.1305 | -49.155102 | 2024-10-17 00:22:38 | METOP-B | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8182e2c-e58e-350c-906c-c6b2c26a86c0 | -1.1207 | -49.157299 | 2024-10-17 00:22:38 | METOP-B | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33ea62ff-1e01-3e99-ae0f-81f8f1781d6d | -1.1225 | -49.165401 | 2024-10-17 00:22:38 | METOP-B | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b9a4dd6-658c-33be-ba95-2ae8aa789f15 | -1.7026 | -52.668999 | 2024-10-17 00:22:42 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6671c5ce-12ee-34fc-a290-5f99187c42ce | -1.7056 | -52.6824 | 2024-10-17 00:22:42 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d671dae-ebcd-3cc5-a901-19809c946051 | -1.3795 | -52.277199 | 2024-10-17 00:22:46 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7994ee0c-02b7-3f33-9d48-5f2f3e5d382a | 1.0064 | -52.203899 | 2024-10-17 00:23:24 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 78aa64f2-5c58-3569-a91a-9659f1272000 | 1.0162 | -52.2061 | 2024-10-17 00:23:24 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b49432db-758a-3352-a089-28c39dca8d38 | 1.7573 | -50.852001 | 2024-10-17 00:23:31 | METOP-B | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4d145f48-9981-37f5-8e18-01d5a48fd762 | 2.1894 | -50.852798 | 2024-10-17 00:23:38 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| db3c8070-2489-3b95-b24a-976f144762ef | -2.6147 | -48.2629 | 2024-10-17 00:25:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9237e8ac-38ec-3b66-b5df-501988510b0f | -2.8979 | -51.6896 | 2024-10-17 00:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 52b7a213-602f-31b2-b452-c17bcd0dae58 | -2.9674 | -47.9931 | 2024-10-17 00:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| df9a2616-acae-349c-aa72-14abd58e4962 | -3.0581 | -53.2395 | 2024-10-17 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 08ee831a-d137-3622-a5b6-7e0c61382ae4 | -3.204 | -48.9312 | 2024-10-17 00:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| fc7fa2ba-3368-34bb-b2cb-3f9ab8abb67e | -3.2041 | -48.9098 | 2024-10-17 00:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 3d20ef69-20fc-306d-ba29-c1cf32b3eb3e | -3.2225 | -48.9306 | 2024-10-17 00:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 5edce9af-9714-36c0-a5b4-b2bef852bb21 | -3.2226 | -48.9092 | 2024-10-17 00:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| abdc738c-4f55-34db-952b-dc405824ae3b | -3.5086 | -51.1122 | 2024-10-17 00:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4fbfb902-2675-36f7-8be5-8ac34b0aed82 | -3.6822 | -45.9231 | 2024-10-17 00:25:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 16003b03-2d9f-38d9-8169-66d0d95d7200 | -3.6823 | -45.9008 | 2024-10-17 00:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| cab7ec24-4feb-3fd7-aa8e-99f80a826f52 | -3.7007 | -45.9223 | 2024-10-17 00:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 238.2 |
| 6b7bbc46-70de-33c4-8f08-51be3e10a9bf | -3.7009 | -45.9 | 2024-10-17 00:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 6b084745-f3bb-3cd9-905e-4db925d2f395 | -3.7193 | -45.9215 | 2024-10-17 00:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 244a004c-7ee2-36e0-98b2-662091856de7 | -3.7195 | -45.8992 | 2024-10-17 00:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 5175b129-66ae-30f8-8e05-e92f607f86a7 | -4.4845 | -42.8631 | 2024-10-17 00:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| bdd7c8a8-154e-3bf7-b342-1ef7e8cc9184 | -4.6331 | -45.6069 | 2024-10-17 00:25:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| f73fe838-3181-343d-9c1f-cb4af9adac48 | -4.8892 | -48.9882 | 2024-10-17 00:25:34 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 35b59332-4568-366b-9a4c-62952d9b00bd | -5.6714 | -48.6872 | 2024-10-17 00:25:38 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f1eb02d4-c534-3f39-b1c6-4d9d54280048 | -5.7135 | -45.7861 | 2024-10-17 00:25:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 3cf8d43a-c64a-3014-af21-679cc5e4e7e7 | -5.7137 | -45.7637 | 2024-10-17 00:25:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| db1a2b21-eea2-3288-b7f7-9c8709c45878 | -5.7448 | -46.4979 | 2024-10-17 00:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 730edd91-938d-397a-ad8c-b9d85d650354 | -5.9788 | -45.3621 | 2024-10-17 00:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6b406f7b-d986-37f5-89a6-af41433eb73f | -6.7086 | -43.5605 | 2024-10-17 00:25:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 611a99ba-33ee-3af8-8c87-25fee3c79a4f | -6.7272 | -43.5822 | 2024-10-17 00:25:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8320363c-fbeb-3dd3-91e0-f24d2754a7c4 | -6.7274 | -43.5589 | 2024-10-17 00:25:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 188.0 |
| b9541fd3-1506-3e52-bbbb-1108b53a16ef | -6.7277 | -43.5356 | 2024-10-17 00:25:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f6401e9e-f26d-3784-aa39-7812b3ce8702 | -7.8539 | -45.3611 | 2024-10-17 00:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7ec8fa0a-80d9-3dc8-862b-0960da7ddfc9 | -7.8541 | -45.3384 | 2024-10-17 00:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 60d5b8ac-ce2c-338f-89ce-1c393072efee | -7.8727 | -45.3593 | 2024-10-17 00:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| fa364381-4e24-3059-9f58-6144d152b8e3 | -7.873 | -45.3366 | 2024-10-17 00:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 163d69ce-29bc-3052-ac51-146fd514b6fb | -9.6232 | -68.6714 | 2024-10-17 00:26:01 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 8954e6a6-b493-3190-bb3c-9c5390653393 | -10.129 | -56.7722 | 2024-10-17 00:26:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 149.3 |
| d46b6f3f-a707-3a1a-9764-a48d8483e55b | -10.1292 | -56.7523 | 2024-10-17 00:26:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2f135cf9-be10-3b98-8d54-3a917991bc20 | -10.1477 | -56.7709 | 2024-10-17 00:26:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ea77cb88-8bff-3140-ae42-c35500515d89 | -11.6915 | -65.2432 | 2024-10-17 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| cf98b3bf-6295-3d57-84a5-05e3011a0bfe | -11.7103 | -65.2424 | 2024-10-17 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 4cd98357-d8f0-3307-a21a-89f7b3d935bf | -11.7104 | -65.2235 | 2024-10-17 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a6c01daf-c06b-3d1c-869b-4680f02cc43c | -12.1528 | -40.8943 | 2024-10-17 00:26:14 | GOES-16 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 0ff4f403-1268-3309-ae3d-b09c04f804ed | -12.1533 | -40.8694 | 2024-10-17 00:26:14 | GOES-16 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 79.6 |
| b1569ef7-ac76-3aa6-b6d4-14410db1b701 | -11.8812 | -64.9513 | 2024-10-17 00:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 73621bf5-8b8b-30cb-985e-d24511a97f12 | -11.8814 | -64.9323 | 2024-10-17 00:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 5f288ea9-6d8b-3456-a12c-410c5594b9b9 | -11.9002 | -64.9315 | 2024-10-17 00:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 156bf6cf-14bd-3b1f-b651-3ed1f6516bb2 | -11.9383 | -64.854 | 2024-10-17 00:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d2d1dac6-3265-39ed-9c3d-0dc84aefdbe9 | -11.9571 | -64.8531 | 2024-10-17 00:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 51809ab4-d177-3501-bbfe-0b4c653d77f1 | -12.5045 | -55.205 | 2024-10-17 00:26:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| daf075b7-367f-3dec-abf7-7deaf8a26fad | -17.1667 | -56.8232 | 2024-10-17 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| a526960b-b58b-37f2-b814-424299038338 | -17.1671 | -56.8026 | 2024-10-17 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 8828b7a8-dccb-3fc7-8b44-e1a0af59aca8 | -17.8049 | -57.4655 | 2024-10-17 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| ca11037a-f8aa-3dd2-bc8d-4c4399f175f9 | -17.8052 | -57.4449 | 2024-10-17 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 664c3bd3-60c3-3eaa-9e3e-eb6af040cafd | -17.8246 | -57.4631 | 2024-10-17 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 8945f6d5-043d-3512-b44c-9e489337fcb1 | -17.9237 | -57.4304 | 2024-10-17 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 2b30919e-3b97-3ace-8314-b24d45ffce98 | -2.8333 | -49.1562 | 2024-10-17 00:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 78148439-330d-35b6-a408-a5bd9fc799d3 | -2.8979 | -51.6896 | 2024-10-17 00:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 82c9116b-ea70-335b-bda7-20a66ec5b3f6 | -2.9673 | -48.0147 | 2024-10-17 00:35:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 0ac482d7-adef-3063-b84e-8720acb1156e | -2.9674 | -47.9931 | 2024-10-17 00:35:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 5d927e1a-768e-3776-a98d-d7f64611b81f | -3.0581 | -53.2395 | 2024-10-17 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 412e07e4-dc90-3e71-9b39-a842f6785c76 | -3.2225 | -48.9306 | 2024-10-17 00:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 5fb9f870-337c-3ae6-b372-9b0697e23211 | -3.2226 | -48.9092 | 2024-10-17 00:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 9cf2b84d-2c0c-3800-ae1e-4424c57949b7 | -3.5086 | -51.1122 | 2024-10-17 00:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 9e57b748-a44c-3795-9691-0d3b5531c9ec | -3.5087 | -51.0914 | 2024-10-17 00:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5e45c7ad-84c7-370c-8791-0b05dbdf246f | -3.6822 | -45.9231 | 2024-10-17 00:35:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| c8f84be2-7c10-3de9-b685-7eac3a2085b6 | -3.6823 | -45.9008 | 2024-10-17 00:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e5eb3cfc-6909-3bd1-b0e7-2d86ad280c72 | -3.7007 | -45.9223 | 2024-10-17 00:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 298.3 |
| 8f394749-e187-38da-8c22-97003541184b | -3.7009 | -45.9 | 2024-10-17 00:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 253.2 |
| c10266f7-bac9-371f-82b6-0f6f93f6b040 | -4.4658 | -42.8643 | 2024-10-17 00:35:31 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 26db4530-4d63-38c8-a59a-daa635e6c93e | -4.4845 | -42.8631 | 2024-10-17 00:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 0fa73797-62f2-3409-8bf7-8c3b3a65ca5d | -4.8892 | -48.9882 | 2024-10-17 00:35:34 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 5fd09e68-bc04-34b2-b3b7-f2d6d4b88c40 | -5.6528 | -48.6883 | 2024-10-17 00:35:38 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a2e0b863-58fb-3dd4-be0e-8808dd917dee | -5.9788 | -45.3621 | 2024-10-17 00:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 0ad9d4ea-3a8b-3f41-b79a-d8ab135a9df8 | -6.7272 | -43.5822 | 2024-10-17 00:35:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 74aee160-625b-376a-94bd-f72a810828db | -6.7274 | -43.5589 | 2024-10-17 00:35:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 6549c887-ae86-33f1-91ac-5d7fa8e8648a | -7.8539 | -45.3611 | 2024-10-17 00:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f07acec6-d46a-39b6-9882-ef505b89fb7f | -7.8727 | -45.3593 | 2024-10-17 00:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 090019a1-ceda-36e7-87f9-953a910421bc | -7.873 | -45.3366 | 2024-10-17 00:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| a30be6c1-66fd-3517-879a-ce9039d065f6 | -8.703 | -41.1547 | 2024-10-17 00:35:55 | GOES-16 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 893dba1b-8cfb-37f6-a1d8-1c66c9075975 | -9.6417 | -68.671 | 2024-10-17 00:36:01 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a1ca371b-5561-33b7-9456-d7d7e0ed8e6b | -10.129 | -56.7722 | 2024-10-17 00:36:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 4c5770cb-5a29-3ada-897d-badd56b005b4 | -10.1292 | -56.7523 | 2024-10-17 00:36:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 6b3375bf-bb00-3aa8-99be-02133242e83f | -12.1334 | -40.8978 | 2024-10-17 00:36:13 | GOES-16 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 38c042c6-ec06-34ee-a42d-58313ace431d | -12.1339 | -40.8729 | 2024-10-17 00:36:13 | GOES-16 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 1f559b99-f2a0-3802-bc8f-93e528ce4e63 | -11.6915 | -65.2432 | 2024-10-17 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5448ac25-752d-331a-b533-87b2874726dc | -11.7103 | -65.2424 | 2024-10-17 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b7bf6c23-d406-3086-900a-ef811f73f709 | -11.7104 | -65.2235 | 2024-10-17 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e4f9986f-bfdb-30fb-b36e-7a3cb9fb9251 | -12.1528 | -40.8943 | 2024-10-17 00:36:14 | GOES-16 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 90.1 |


[Clique aqui para ver as próximas entradas](README8.md)
