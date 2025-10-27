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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d2bc3a8-e9ae-3589-970d-1f5de1213de3 | -3.40243 | -50.27189 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58076041-e124-3ad7-8035-ade3b38a1e48 | -4.35573 | -50.7045 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d0d4d75-8f2a-399a-b1db-ddc98ba08076 | -4.20422 | -48.35763 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67f91df2-6716-3d7b-b5d0-ad544f68103d | -3.11615 | -51.21147 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4a03232-0ffa-30e9-b772-3ea8cb0b8eea | -0.96802 | -46.78266 | 2025-10-27 04:59:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b3e31c3-3c47-3bed-a388-d910d76d47f2 | -4.48133 | -43.42032 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 83eb9e53-6c9c-387c-88e7-590fa5178a91 | -4.44778 | -49.58279 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97652e59-db36-3cfe-b70b-2b5aa803bfb0 | -4.45556 | -45.46402 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5ad18bd-cddf-32fc-bf45-3c3d2c3370ca | -4.20366 | -48.36134 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6d9f353-01d2-38aa-a1c0-a42eb917473f | -4.83185 | -45.339 | 2025-10-27 04:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a72db1ea-bc58-3f2d-b611-4219d637bab4 | -3.999 | -48.31905 | 2025-10-27 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4efa1083-3b23-3c05-b036-b6a5dcd150a2 | -4.80744 | -43.29728 | 2025-10-27 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0248a2ce-273b-3cee-b11e-a3ef8da3ca79 | -2.68983 | -48.45723 | 2025-10-27 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6a0c3ab-a139-3d2c-9c02-330a0df24f08 | -3.13538 | -53.00136 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8339194-88a7-3b26-929c-1a51969d089e | -4.28567 | -49.66892 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e9feae3-7ae0-336a-a80e-32443721058f | -4.20489 | -48.71427 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7bd7516-ca87-38cb-bb9b-ef1ce035043a | -4.46969 | -43.41836 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cb95e41-1f9c-3d5d-995a-52c8a65afe1f | -3.46759 | -49.97293 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 88a7819d-fdc0-3f8d-a757-e114f64324af | -2.37927 | -55.96334 | 2025-10-27 04:59:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58a423e3-de6a-3575-9ca0-55a60a89feac | -3.92934 | -50.02678 | 2025-10-27 04:59:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6846c7f3-187b-36e9-aa2a-309165f71b43 | -3.24269 | -50.65127 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e068a0bc-e66b-3610-b84e-585a81ac80bf | -3.73952 | -52.43069 | 2025-10-27 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3c01180-0332-3980-a488-9f729f26e72c | -3.25221 | -50.04142 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef920715-1788-3a71-b695-bd670e105210 | -4.15978 | -51.08178 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4aedc18-056c-3912-bcfa-47aff55c9245 | -4.45146 | -43.43053 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04383108-c5f5-3fe8-8f07-a436a23f173d | -4.255 | -48.13216 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50e0bf07-6a9d-322a-b206-43ff1550a377 | -3.78241 | -51.93484 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 470650f3-37c2-3eaa-860c-65a4a1aafaf4 | -4.71085 | -48.62735 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f95f58a-2a88-3602-84c1-fa647e5bb7c4 | -2.27378 | -47.85289 | 2025-10-27 04:59:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acc965ed-a362-3382-bd6e-8ac1782728bc | -4.38904 | -43.32472 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2da113ce-b9f0-3bfb-8619-c5808f978ab0 | -3.06232 | -49.37176 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b5756b0-10fb-386e-8b66-451b18259034 | -3.47267 | -49.96471 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7473b088-6af3-329c-ba55-7d0d67dae6a4 | -4.45226 | -45.45109 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4f60382-8755-3f09-8db0-a671a402c851 | -3.15119 | -50.33072 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6646c55-a0cf-3aca-8306-a15f38bad0ff | -3.10375 | -50.17844 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2b192ce-5b79-32eb-949f-d704c501dcc5 | -3.75836 | -51.75414 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b69bed4-5cf1-3f2a-977c-ee9f521ae263 | -3.1013 | -49.44938 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d9ffb25-b968-3d63-b214-64a9735e4d20 | -3.57272 | -44.5256 | 2025-10-27 04:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f185ac4-3fca-3efa-8e62-c06cbbef2ab2 | -2.18994 | -52.49405 | 2025-10-27 04:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 607c0f9a-d342-3be5-97b4-db600a0c2ea2 | -3.54416 | -51.10051 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e9eba17-544b-35ed-a5aa-837c02593c7d | -4.34721 | -50.59248 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1213877e-f732-3de1-8deb-fbf568d4fdee | -3.77673 | -51.81341 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac0e100c-225b-38a8-88fe-6bd60a3fce73 | -2.77198 | -54.57442 | 2025-10-27 04:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be6b2aab-3481-3a6a-9509-1d63700ba168 | -3.14677 | -53.14151 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c77e62fb-c789-3328-aeac-6e201928de2c | -4.32586 | -48.09011 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b644504e-282d-3d15-9b19-05f84dc7f616 | -3.04672 | -53.02308 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49641c24-80ea-3a9e-b83b-e227157a1f32 | -3.13036 | -50.15208 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45777f86-3397-3b5f-bcee-fde3bde78e09 | -2.44179 | -49.03217 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 506e1652-988c-3acc-b18b-ac66edc58823 | -4.45287 | -43.66082 | 2025-10-27 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b24cade5-2473-3144-be8c-09dbe73ca1ad | 0.44037 | -50.81733 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17f87a9e-5f19-3592-9ce5-e51b524afb8f | -4.47718 | -43.41771 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c34d1b41-f5be-358b-8dc7-95d95475fd25 | -4.45346 | -43.65691 | 2025-10-27 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71abbd2c-a473-33a4-beb8-8583ad0b0241 | -3.39877 | -50.27134 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2561266-712d-37d5-937d-732b6cbb7216 | -4.45205 | -43.42647 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 157cda46-d462-3a2e-8fac-50cdb975cd61 | -5.03184 | -44.68337 | 2025-10-27 04:59:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b8dfa1b-f3b8-3abb-93b1-488758f88763 | -4.36873 | -46.80632 | 2025-10-27 04:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04c51550-42ea-33b6-87d0-53f84fa5fbbe | -3.57871 | -43.61227 | 2025-10-27 04:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffe3584c-d640-3526-b419-b4ac96f36e03 | -4.48017 | -43.42857 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5e6b5c77-2b82-362d-bd01-bca7c7bb3489 | -3.242 | -48.77381 | 2025-10-27 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| deb7fbf8-be62-3bf9-8d46-fd4bb0986e79 | -4.33011 | -48.09064 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc92cf8b-cd64-39c9-8f1c-531fd05d7300 | -3.57105 | -49.01759 | 2025-10-27 04:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8377deb-78c5-39a8-a89a-bef209d348b3 | -4.4805 | -43.4237 | 2025-10-27 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| aa420fbe-f06f-38f2-a295-9e59016c529b | -10.3594 | -47.18 | 2025-10-27 05:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8191c9d1-80ac-370c-b7db-16bd674b5e4b | -4.4618 | -43.4248 | 2025-10-27 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 345ec531-c405-3014-a496-0ae005a8fb63 | -4.3879 | -43.3129 | 2025-10-27 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 229914df-53ff-3b2f-9578-02bdb021d542 | -13.3163 | -54.3634 | 2025-10-27 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| fa5e98c5-f0f0-32c0-b361-1fc062c02d7a | -9.26189 | -45.57533 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3692d59-7fe1-3033-a4ce-ba1d4787d72d | -11.44539 | -44.67561 | 2025-10-27 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41c527c2-6689-378a-91e8-a7ab7647c7e9 | -7.97151 | -45.46878 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9f6c7dc6-4fcc-314d-b642-38aa13cda627 | -6.10168 | -41.78052 | 2025-10-27 05:01:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 98683b86-2a56-30f4-ab1f-e403aa6fc80c | -9.7337 | -47.8672 | 2025-10-27 05:01:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2179ecef-cc24-3009-bf2b-2e1175d1bf00 | -7.82649 | -46.44873 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16d455d9-fc99-3c0c-a37d-8ea05bd4843a | -9.46233 | -47.73064 | 2025-10-27 05:01:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cfdea87-d493-39be-bccf-e19ff30031cf | -3.97593 | -56.08878 | 2025-10-27 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd5c057b-5ab6-302e-b8ff-9a630d0a10b4 | -12.28271 | -43.75362 | 2025-10-27 05:01:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c12f77b-d059-3275-994b-c55a534e81a1 | -10.31311 | -47.19299 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63659d41-430b-304e-a1db-1b0d132c4814 | -3.93286 | -55.72746 | 2025-10-27 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7604be9f-b04b-3624-a352-6bd1310fedf6 | -6.88163 | -43.57336 | 2025-10-27 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8a50691e-5269-3403-b2eb-c303cb1521d1 | -7.81194 | -45.39806 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a364864-c4bf-3e5e-847c-f9b8b78fc81d | -12.33868 | -47.11297 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a353f899-41f8-3c59-8963-54d709661ad9 | -7.81107 | -45.40434 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52207927-b2bd-37bb-ad07-78347169266f | -12.53059 | -49.58838 | 2025-10-27 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd679538-2fd5-3b95-93c9-1fc3422ef237 | -10.35034 | -47.18351 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8ae284f-daf9-35e7-a1f9-86b6a19640de | -7.82764 | -46.47721 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f4c8f9f-7178-3e20-9f9a-a2e2ebd316fc | -8.65137 | -44.77005 | 2025-10-27 05:01:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb88e5a2-6356-3b4e-8077-29f3a5b736f1 | -7.85745 | -46.44615 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f956366b-2672-36b3-a118-a4a8252e3133 | -10.58019 | -47.99039 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6366a703-55e0-3668-954c-1f5186d68589 | -7.77346 | -45.3993 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02bc780d-327f-33f8-9a78-51eb2d06670d | -7.82959 | -46.49982 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f790bcae-7e26-39ab-b880-4d7432860b54 | -10.95589 | -49.81257 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5092cc79-9fd3-3552-b1e0-0e683c9dc93d | -11.04758 | -49.89437 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b96d5151-2729-3f73-a504-f89dda95488d | -11.70854 | -44.44591 | 2025-10-27 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6b84efab-6b4c-3068-bf48-a057b7932593 | -8.695 | -44.42812 | 2025-10-27 05:01:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 844169ca-0f50-3a17-9154-378bcbffca43 | -10.35457 | -47.18967 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 2fe7ca4d-562d-304c-9b6e-b89b23866efd | -8.31719 | -46.17401 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc5a509e-af0e-3d0b-aa82-6cc5438fcc86 | -10.7573 | -44.19679 | 2025-10-27 05:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f13d6907-4b62-3ec8-91ac-82c077d95757 | -6.8785 | -43.57552 | 2025-10-27 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ef0efaf-5dac-347c-8022-6c462731820c | -4.87624 | -50.85777 | 2025-10-27 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54bc9abf-6382-39c8-b99b-425a7f43dd08 | -12.32722 | -47.48491 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e28d8ce2-c7d0-3762-b7f2-d980ffea2f12 | -10.35253 | -47.16656 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README58.md)
