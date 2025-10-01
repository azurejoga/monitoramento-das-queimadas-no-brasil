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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8f8588e-a2d7-3202-9a92-0ecd89309d8d | -6.214 | -44.2272 | 2025-10-01 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 46be94eb-8f49-3f1d-92d5-552735b7715f | -7.7313 | -46.2065 | 2025-10-01 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 5bcabafa-0df4-303e-b14f-3da870f22f48 | -14.9738 | -46.8668 | 2025-10-01 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 0d23830f-2b80-3919-941b-8af3b79f7824 | -15.5384 | -45.214 | 2025-10-01 13:30:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 211.9 |
| cd0d0033-b708-356e-b687-8cf24f9d8c89 | -8.6911 | -47.6906 | 2025-10-01 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 01ce99f1-d464-342c-98ed-76d4622ad134 | -15.5379 | -45.2375 | 2025-10-01 13:30:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 5397d6f7-1c1e-3424-af33-64e21c898081 | -9.1248 | -47.6256 | 2025-10-01 13:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 8c84bfc4-ddab-33df-bf77-4ee2198c777c | -9.9186 | -43.6978 | 2025-10-01 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 426.1 |
| 6affb48c-0569-3dce-b4aa-0bf59598dd5d | -10.0712 | -50.26 | 2025-10-01 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 9d68642d-5fe5-344f-aec5-6214b27ac6a1 | -6.3 | -45.0205 | 2025-10-01 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 14cbeeb9-c280-35d9-964a-d0db27daf1ba | -13.3603 | -48.1605 | 2025-10-01 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 46c7f526-b8d6-3198-bc38-6e1f8a2e882f | -6.0978 | -42.6758 | 2025-10-01 13:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| f5e93285-bc34-3683-a3ac-0ba8b9b9eb1d | -5.9557 | -45.8588 | 2025-10-01 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 940db753-b651-30e8-9337-dfe83e4f6e7d | -11.3486 | -48.3211 | 2025-10-01 13:30:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| c50eb617-7fa8-3377-a55c-1e232605fcc7 | -13.7691 | -47.9435 | 2025-10-01 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| a2d6323f-41b6-3119-80a0-418d70c1fb66 | -10.1092 | -50.2349 | 2025-10-01 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| f0e5b678-46f5-3e54-985d-3ab4df75d848 | -7.1148 | -47.8068 | 2025-10-01 13:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 4f7224c5-e485-3b51-97d9-08cb112d0d9e | -6.2138 | -44.2502 | 2025-10-01 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b2ce2783-e019-3d14-930a-03538b4ec779 | -5.8889 | -42.9283 | 2025-10-01 13:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| a7448652-92e8-3416-9611-bb8f145d304d | -8.4827 | -47.8202 | 2025-10-01 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| daf75ae9-cd0c-3447-b5c6-b1f720834416 | -11.4784 | -45.0637 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 02fcc685-f838-3f5b-a2ed-5615b1079d9b | -12.1224 | -43.3977 | 2025-10-01 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 7ea0818a-95e3-3701-8737-23889126b33d | -5.9555 | -45.8812 | 2025-10-01 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 543d810c-de48-3778-90d5-89dfb468c104 | -13.2969 | -50.6821 | 2025-10-01 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| cd01ea13-27a4-3107-a101-6ff108adac05 | -11.1757 | -47.2134 | 2025-10-01 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| cf877cdb-e16e-3b37-afee-028a6a692b7b | -8.5584 | -44.7644 | 2025-10-01 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 135.9 |
| fc23c0c7-04ba-3935-89bb-85f89b0c7fc0 | -14.3514 | -45.9437 | 2025-10-01 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 72586446-6bf7-3b93-84ad-5a44d99f0519 | -10.1084 | -50.299 | 2025-10-01 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 854a7cdf-9b02-3be9-8948-71e5d75d0671 | -10.0903 | -50.2368 | 2025-10-01 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 092e7814-e48f-310d-830a-00ac23d4178b | -9.0239 | -46.6828 | 2025-10-01 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f3bebaa5-cb75-3b08-b9dc-a86bfd98fa32 | -9.8201 | -47.8386 | 2025-10-01 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 0fd71ce6-9f4e-3b37-979b-e4373e2896a2 | -7.7944 | -42.5132 | 2025-10-01 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 5aea563f-8d44-38b1-94c6-5ec185f139b4 | -11.6126 | -45.0443 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 46add4cc-6b13-3f21-92f0-22bb5dec8fe0 | -10.1081 | -50.3203 | 2025-10-01 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 0f871ebf-3405-388e-a8b8-de5a26b3ab29 | -11.46 | -45.0202 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 96910f79-0572-3287-8b94-6301c9337853 | -16.9037 | -47.4026 | 2025-10-01 13:30:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| c9549566-a159-3a3c-985f-b8676dd67c64 | -11.8478 | -48.0816 | 2025-10-01 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 0e23e62e-d079-3ebd-b9cf-a2b5222b76bd | -8.8923 | -46.6519 | 2025-10-01 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 3d6ed7c0-4070-3737-8f0b-6990a3bc0394 | -11.3834 | -45.0312 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 52fad4b5-d171-3a1b-b8da-d0c265540a79 | -8.5267 | -47.2879 | 2025-10-01 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| a551c7a5-4b4a-3228-a439-002847a1e571 | -13.3414 | -48.1411 | 2025-10-01 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 215.5 |
| c34f68d6-9e5e-37b7-82af-ac6038f8276f | -9.0236 | -46.7052 | 2025-10-01 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 55ff6910-d0a2-3424-b575-78e474953bf2 | -13.3611 | -48.1159 | 2025-10-01 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 15b86272-42fb-3e47-a637-59ffe1dc8c27 | -9.4644 | -47.6124 | 2025-10-01 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| bebf5457-c12f-31b0-8582-0062e7d7e36b | -7.5561 | -46.7795 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| badd3ca3-19c8-3d23-ad40-1b3c806d0d56 | -8.9182 | -47.5803 | 2025-10-01 13:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 2744ada2-f965-33fc-8fad-dd3dff5a6ef3 | -12.2536 | -47.806 | 2025-10-01 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 242.8 |
| d5315ca9-d551-3c7e-a1ff-72b82b721407 | -7.8735 | -45.2911 | 2025-10-01 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9a10bac9-5208-39e8-9133-fc55fa90b815 | -12.2344 | -47.8086 | 2025-10-01 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 9481c6d5-a382-3498-b871-84ecc3dc7335 | -5.9368 | -45.8825 | 2025-10-01 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 076282d2-74d4-3b30-aca3-daf10d91077d | -12.1031 | -43.4008 | 2025-10-01 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 68c6a3bb-2e9e-32d1-b8e9-aeb41434f413 | -8.8354 | -46.6801 | 2025-10-01 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 18fe15a8-aa9a-397f-a240-74b3da84e28a | -12.8774 | -45.1742 | 2025-10-01 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 6e0281b1-c59f-3fd7-9466-4c417ce8b6fc | -8.2105 | -47.0084 | 2025-10-01 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| f1ef045d-7716-300f-88ea-5b409cf95847 | -14.3519 | -45.9206 | 2025-10-01 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 141.5 |
| c8dcd891-2842-3473-ba1e-4527be9cb4f5 | -7.8882 | -47.281 | 2025-10-01 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 709f5b94-0db4-3aba-be3a-33d30a91a063 | -9.938 | -43.6718 | 2025-10-01 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 225.9 |
| 0e300910-0bcd-3cc2-915a-4ab3bf781944 | -7.5559 | -46.8017 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 12fa1b4d-c69b-361d-a5eb-33e22fa6045c | -9.9376 | -43.6953 | 2025-10-01 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 239.0 |
| da830f0f-b60f-38ff-9781-ec87e8faa41e | -14.764 | -45.7552 | 2025-10-01 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| dbf47f49-77aa-30ab-86a5-d7d9c8acf201 | -15.9388 | -43.2979 | 2025-10-01 13:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 994414f8-007e-375b-9d70-ecc82b8177e4 | -13.0307 | -45.2189 | 2025-10-01 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| cb0fa28e-7c77-3005-b19a-742f74d8347a | -10.0709 | -50.2814 | 2025-10-01 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 757ca493-3f76-3d7c-98c5-f9dda1cc7a31 | -13.0119 | -45.1988 | 2025-10-01 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 356.6 |
| 3e811148-c289-346c-8f1a-7fd1abce023e | -12.122 | -43.4215 | 2025-10-01 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| dbefcfe7-b22a-3b43-9c62-f072d15576a2 | -13.6703 | -48.07 | 2025-10-01 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 18f4e001-9974-303c-b956-dbde163f48e1 | -13.3607 | -48.1382 | 2025-10-01 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 6584e634-aaef-347a-927c-68c6c044c254 | -11.9411 | -47.0675 | 2025-10-01 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| b399e3e7-ff10-3dee-98b3-61cac474a561 | -15.2742 | -49.2852 | 2025-10-01 13:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 0a7aa719-629c-325f-9929-3024d24ae7d6 | -13.3221 | -48.1439 | 2025-10-01 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 91cb7bc8-9a15-3507-a0af-4a216f20eb24 | -8.5404 | -44.6975 | 2025-10-01 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| ae79733e-3084-3182-84f1-b0e119f62f15 | -7.6272 | -45.4507 | 2025-10-01 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 0b4dc7a3-c83f-3717-b36f-0194b0693181 | -11.8246 | -44.9669 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 8aaaca39-77dd-303f-ba85-2dc5b8844041 | -8.5018 | -47.7965 | 2025-10-01 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 392.6 |
| e0080c08-d6d2-317d-8745-f6d5ee08123e | -11.8482 | -48.0595 | 2025-10-01 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 5dfd9464-1a84-37c5-a452-a1e94db92043 | -14.9733 | -46.8896 | 2025-10-01 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 6a519def-4ff7-32bc-b833-d1370193c3de | -9.1889 | -48.5166 | 2025-10-01 13:30:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 22b6ed46-b18e-321a-abe2-7df2452eba5e | -8.4833 | -47.7763 | 2025-10-01 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d96fb07f-0f23-3e9a-a212-c28d3b64c0fa | -8.8926 | -46.6296 | 2025-10-01 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| bd0f3a63-7389-3570-9128-8c28a75ad986 | -8.8797 | -47.6502 | 2025-10-01 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| b923fc5b-811a-3c4a-b82e-f90b6c2908c7 | -11.825 | -44.9437 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 99fc705f-0720-383c-9510-db100a1fc30e | -5.8418 | -43.9566 | 2025-10-01 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| ff298819-42a0-39b5-821b-60eee7851e74 | -11.4596 | -45.0433 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 236.6 |
| 9251e8a5-2dde-347f-a099-abff620df145 | -16.0225 | -50.8771 | 2025-10-01 13:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| fc108bc4-45ce-30f2-bd10-62cc5c20b0fe | -11.383 | -45.0543 | 2025-10-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 0ad315ca-01e9-3ac5-9e3f-14695b78f965 | -13.8304 | -43.0737 | 2025-10-01 13:30:00 | GOES-19 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 0fc59178-5924-3d48-aad5-e34f0113f7b9 | -14.8021 | -45.7946 | 2025-10-01 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 538e08d7-3c43-3961-bfbb-6afbb4130022 | -15.3596 | -47.0724 | 2025-10-01 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| ee4e9f55-0f24-3845-9657-f5ffa9d5f795 | -8.8609 | -47.6521 | 2025-10-01 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c6d1c534-ec99-34ce-b829-4aa6cd69fcc6 | -10.8433 | -45.3815 | 2025-10-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 4316bc78-871c-31fc-94cc-f1c4c875f4da | -9.9387 | -43.6248 | 2025-10-01 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4b0acb65-5ec0-3e4d-93e3-5d2fda94891a | -13.3808 | -48.0908 | 2025-10-01 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 92bcc2b8-773e-3484-852f-d29636e122d8 | -5.8064 | -43.728 | 2025-10-01 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6718a2a4-b27a-35bc-839c-58cc4e34fcff | -8.5016 | -47.8184 | 2025-10-01 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 0285b29f-1782-385c-8100-5d1da9379abc | -10.0145 | -50.2657 | 2025-10-01 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 0dc4c6f0-1089-3761-a661-9827b819109d | -6.7165 | -44.5987 | 2025-10-01 13:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| e35ccbc5-1eec-3b82-9887-a0bb3b00c48a | -16.0221 | -50.8989 | 2025-10-01 13:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 91c38bb0-d93e-3166-a3eb-45a65b364679 | -11.1178 | -49.7845 | 2025-10-01 13:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4cde4d24-43a8-3e56-8de6-e7b54e95bd5f | -8.8929 | -46.6072 | 2025-10-01 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 051843e0-cf21-3580-b2d0-97eac7570998 | -8.9081 | -51.6743 | 2025-10-01 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |


[Clique aqui para ver as próximas entradas](README155.md)
