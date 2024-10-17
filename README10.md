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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98f7dc27-c587-3712-a0a0-2cc925de9e61 | -9.8356 | -57.714298 | 2024-10-17 01:15:54 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83afaf5b-149a-35af-86dd-4cd9f44899fe | -9.9686 | -36.3072 | 2024-10-17 01:16:01 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| 2c60c3af-ceb8-34a4-903d-a62b435bbba4 | -10.129 | -56.7722 | 2024-10-17 01:16:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| b0356780-5962-35b4-82f0-60438790918d | -10.1477 | -56.7709 | 2024-10-17 01:16:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| cd194715-c557-3515-aa0b-15baa0fb2e66 | -5.9934 | -45.364799 | 2024-10-17 01:16:09 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8719ebe-0ca3-3786-9bbe-c152612d0110 | -5.9838 | -45.367199 | 2024-10-17 01:16:09 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1d470a4-295f-3c07-80ad-9c6b0e0460af | -9.188 | -59.360001 | 2024-10-17 01:16:11 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b399a8f9-1960-39e4-89c1-89c2f643a025 | -9.1901 | -59.369801 | 2024-10-17 01:16:11 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a58e6666-234d-3d82-88b0-930ffd1739bf | -11.7308 | -64.9769 | 2024-10-17 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 262a3e5f-2422-38c2-b7e5-3caf0937238b | -11.7309 | -64.9579 | 2024-10-17 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 959b9c50-b469-3cbe-8506-de53b98e6fe6 | -11.8812 | -64.9513 | 2024-10-17 01:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4f11e324-57c7-350f-be34-3806a90b0cf4 | -11.8814 | -64.9323 | 2024-10-17 01:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 7647fb02-37a2-39ae-b26a-ca8d09a65710 | -11.8815 | -64.9134 | 2024-10-17 01:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| cde8f1de-2801-375b-820c-f2287480816e | -11.9 | -64.9504 | 2024-10-17 01:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 87efe3a4-6885-378d-b091-c5b536109790 | -11.9002 | -64.9315 | 2024-10-17 01:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7ff56854-3ea1-3bd5-a09f-2a03eec48b43 | -11.9571 | -64.8531 | 2024-10-17 01:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| bba0aebf-c6be-362b-bf85-315125d457ce | -5.5874 | -44.891399 | 2024-10-17 01:16:14 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9d0b7c9-45d2-3b33-b9cd-6194efb9d6e1 | -5.5713 | -44.868 | 2024-10-17 01:16:14 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b2aa7d1-003e-3e17-a98d-a3fff8637ec2 | -5.5778 | -44.893799 | 2024-10-17 01:16:14 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 535ad90f-dee9-33b6-ae9f-024ca6d60b12 | -5.7173 | -45.774399 | 2024-10-17 01:16:15 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3deb1fa7-11f2-3e51-a862-be122c8535c9 | -5.7076 | -45.776798 | 2024-10-17 01:16:16 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 896112f9-8443-3d13-967d-7c37046b1384 | -5.8611 | -46.4324 | 2024-10-17 01:16:16 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06da0c8f-882b-3e09-9634-c3eef24d7de5 | -5.7905 | -46.190399 | 2024-10-17 01:16:16 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80dc6f05-2a1f-323d-adb4-643b41921925 | -5.755 | -46.5009 | 2024-10-17 01:16:18 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 319ed87e-8fea-361d-b9ce-144df40a21bb | -5.7283 | -47.388699 | 2024-10-17 01:16:22 | METOP-C | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d778320e-1882-3ada-9425-c26f63dc634a | -5.6721 | -48.670898 | 2024-10-17 01:16:28 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5556551d-0740-35d4-b685-a914aa286dae | -5.6755 | -48.685001 | 2024-10-17 01:16:28 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25140216-a588-3c42-9af6-78659b27234e | -5.6623 | -48.673199 | 2024-10-17 01:16:28 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d02b1c3e-f654-3615-b439-7749d4e3ebff | -5.6657 | -48.687302 | 2024-10-17 01:16:28 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4667f49-a090-3728-bb51-660d053c045a | -5.229 | -47.950298 | 2024-10-17 01:16:32 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b996ee51-a5c6-3033-b9bc-619f2396344e | -4.5555 | -46.667599 | 2024-10-17 01:16:38 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 83126abd-8069-361f-abc9-e23b3446043c | -4.5605 | -46.687801 | 2024-10-17 01:16:38 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1dffb875-64b2-37c2-8892-f7abc0183766 | -17.1664 | -56.8439 | 2024-10-17 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 4d4b6e43-1c61-3e8d-90eb-a61944c16b01 | -17.1667 | -56.8232 | 2024-10-17 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 046bdcd9-712e-3928-a6cd-c4438b31817e | -17.1671 | -56.8026 | 2024-10-17 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.3 |
| 44719c2e-8d33-38c2-8b21-76f91063a379 | -4.8953 | -48.9897 | 2024-10-17 01:16:42 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a35afc5-9c8d-37af-80a4-b327f569a0e3 | -17.2177 | -57.3102 | 2024-10-17 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 84bb19d6-9e15-3d0f-b806-e82f6f943b69 | -4.5746 | -48.005199 | 2024-10-17 01:16:43 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1104e7ca-ef3e-3461-8eeb-08534b227d6f | -4.5785 | -48.0214 | 2024-10-17 01:16:43 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fefa491c-92f1-38dd-8c73-3212b56ba014 | -17.8873 | -57.2496 | 2024-10-17 01:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 49609cfd-5066-3694-868c-92d757d34161 | -17.8049 | -57.4655 | 2024-10-17 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 320b8b4b-b046-3efe-9454-3f298cb2ae56 | -17.8052 | -57.4449 | 2024-10-17 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| ecbde8b4-f227-3941-8fb6-00ce576efea8 | -17.8246 | -57.4631 | 2024-10-17 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| cd515378-c28e-3cbe-a4fd-db480c989bc4 | -17.8249 | -57.4425 | 2024-10-17 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 5b83ae9f-318a-337b-bbc9-0396c3cb48a7 | -17.8444 | -57.4607 | 2024-10-17 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 83c5c6e3-6704-3a83-827a-3df1f5e0781d | -17.8641 | -57.4583 | 2024-10-17 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 7d006fbe-26e0-3e78-b878-d97952c1da40 | -18.254 | -56.6029 | 2024-10-17 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 634a3dde-1749-3449-81ef-6627abb95e9b | -3.7128 | -45.902599 | 2024-10-17 01:16:49 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ce5d4f6-f9a5-3931-9704-14f80637dcb5 | -3.7186 | -45.926102 | 2024-10-17 01:16:49 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 171c673a-8fc8-33c4-abb3-ad4eb4e4ad95 | -3.7031 | -45.9049 | 2024-10-17 01:16:49 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6096c92d-7ce9-33f3-a7c7-631fe3461461 | -3.7089 | -45.928398 | 2024-10-17 01:16:49 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31eb306a-41d7-35a5-9a2d-11348cf66429 | -3.6935 | -45.9072 | 2024-10-17 01:16:49 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 923d6950-f2b3-3b52-a259-4edaacf9e1dd | -3.6993 | -45.930698 | 2024-10-17 01:16:49 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ad3ca99-cf8b-3649-965a-b44d1679b00c | -3.3037 | -45.400002 | 2024-10-17 01:16:53 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69d37dd0-d7e9-3809-bcaa-7954b671188c | -3.9281 | -48.346401 | 2024-10-17 01:16:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 588311cf-3320-3929-8c88-62d2031d8d88 | -4.3521 | -50.980499 | 2024-10-17 01:16:58 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c2d1c40-5fe6-37ce-9951-824440b61a19 | -4.1038 | -50.758301 | 2024-10-17 01:17:01 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40bca010-7345-3426-b8b3-0ccd7b0997fd | -4.0739 | -51.110699 | 2024-10-17 01:17:03 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce33a52-e830-30ec-b66e-1cd13732344a | -3.6529 | -50.203499 | 2024-10-17 01:17:06 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4540c61a-fbdd-39d2-a81d-2c3393537b33 | -3.6501 | -50.191601 | 2024-10-17 01:17:06 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7053be30-0dd6-39ec-b122-2c607d96562c | -3.8075 | -51.2911 | 2024-10-17 01:17:08 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03f08a6c-7554-35b3-a775-7742e1e8c230 | -3.8099 | -51.301201 | 2024-10-17 01:17:08 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6bc1514-a204-3ea1-b4a3-50473b217e02 | -3.2196 | -48.902199 | 2024-10-17 01:17:08 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d93c7b1-f764-3c43-989e-b054834f5645 | -3.2231 | -48.917 | 2024-10-17 01:17:08 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 386eca2a-0ded-3d65-bf25-1a6f62307246 | -3.2267 | -48.9319 | 2024-10-17 01:17:08 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df776430-2e02-3197-98b1-d566af5e33fc | -3.2134 | -48.9193 | 2024-10-17 01:17:09 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa69bd20-4896-3b32-95ea-8898edd94115 | -3.7996 | -51.388401 | 2024-10-17 01:17:09 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aba59a55-8c7b-3135-ae6e-ecaea0d7f487 | -2.9815 | -47.993301 | 2024-10-17 01:17:09 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b623ee6-d45d-3583-be5e-280738e8a1c2 | -2.9676 | -47.978298 | 2024-10-17 01:17:09 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4341205-1c13-3426-beee-7da2937cc9a6 | -2.9718 | -47.995602 | 2024-10-17 01:17:09 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 926b19bb-27a6-36f4-b9eb-ec9c3bef7a31 | -2.9759 | -48.012901 | 2024-10-17 01:17:09 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3bf0399-adef-3ec1-9fb1-2e98e2830bc1 | -3.7001 | -51.054699 | 2024-10-17 01:17:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50c6794f-80f2-31e5-a4ad-f68267338067 | -2.9621 | -47.997898 | 2024-10-17 01:17:09 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd6e305e-1be2-340e-a83e-13f3ab7956ef | -3.6706 | -51.017101 | 2024-10-17 01:17:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6692e90-1d22-3d06-abf3-9955ffdc4fea | -3.6731 | -51.027699 | 2024-10-17 01:17:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6adfcf9e-9fe8-37fd-86ed-22a6e4cff481 | -3.8371 | -51.898499 | 2024-10-17 01:17:10 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77487839-31cc-33b3-b577-5e3d76323ba3 | -3.8393 | -51.907799 | 2024-10-17 01:17:10 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52d24b8f-06e5-3657-bf20-534b8859608c | -3.5146 | -51.097698 | 2024-10-17 01:17:12 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2ec574a-61df-3419-ae8c-3d9639303e06 | -3.5171 | -51.1082 | 2024-10-17 01:17:12 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d80e29e5-a79c-368a-983f-110d59061158 | -3.5023 | -51.0895 | 2024-10-17 01:17:12 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91581bbe-9099-390e-b9d2-c89fe9cd2633 | -3.5048 | -51.099998 | 2024-10-17 01:17:12 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e3b3068-b802-3ae1-bbf2-fdaeaf4cdbb8 | -3.5073 | -51.1105 | 2024-10-17 01:17:12 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d64d012-73ec-392e-9a7d-29081d308607 | -3.5098 | -51.120998 | 2024-10-17 01:17:12 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e0822e9-d925-330e-a392-fa6a8132f7f2 | -3.5488 | -51.286598 | 2024-10-17 01:17:12 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1cd77d9-b0b5-3b3d-841e-d2c78db65bf4 | -3.5391 | -51.288799 | 2024-10-17 01:17:12 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90a63656-f85a-3e4a-876a-95ef3ccb37a8 | -3.5048 | -51.318199 | 2024-10-17 01:17:13 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d676321f-64a6-3773-8a08-f90582d29872 | -3.2255 | -50.353298 | 2024-10-17 01:17:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 235fa0da-6a2a-3272-aef6-d5c75e4826c4 | -3.4941 | -51.666698 | 2024-10-17 01:17:15 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c425734f-ba0f-3303-83e2-debca06cf1a0 | -3.4964 | -51.676399 | 2024-10-17 01:17:15 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2779db5f-b801-3a80-a80e-d7d0fa50b51d | -2.8461 | -49.1446 | 2024-10-17 01:17:15 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9a9a24b-6f81-37af-acd8-2f1f6909cd0a | -2.8496 | -49.1591 | 2024-10-17 01:17:15 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d8d7b31-0e1a-399b-9d08-7c1ec2e930dd | -2.8364 | -49.1469 | 2024-10-17 01:17:16 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 366084f3-3a87-3c32-a24a-1c10aff86faa | -2.8399 | -49.1614 | 2024-10-17 01:17:16 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 908f5f29-1462-3919-bd1d-2bf87b6c9c90 | -2.6108 | -48.243099 | 2024-10-17 01:17:16 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 598de86b-227c-3040-9a98-cff922361123 | -2.6148 | -48.259899 | 2024-10-17 01:17:16 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 528b3e4a-8b4b-39a0-85cb-6f15a66b1abd | -2.6188 | -48.276699 | 2024-10-17 01:17:16 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab56faab-3508-3df8-939b-275367c0db11 | -2.6051 | -48.262199 | 2024-10-17 01:17:16 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5554ec49-7e04-3313-b461-667adca4b559 | -3.0735 | -50.3634 | 2024-10-17 01:17:16 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26a3c2b4-c38a-3f8b-b085-a3131ff3048c | -3.0763 | -50.375301 | 2024-10-17 01:17:16 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa0dae6-808f-3767-a4b5-c3311a33afbf | -2.8324 | -49.519199 | 2024-10-17 01:17:17 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
