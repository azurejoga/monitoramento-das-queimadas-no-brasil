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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a509f5e-a052-36eb-9212-63437ac187c5 | -20.061001 | -49.3559 | 2025-05-08 00:17:00 | METOP-B | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5c245e56-c66e-3cfa-a3e1-6406eab4a6b0 | -15.8337 | -46.5718 | 2025-05-08 00:17:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 88948a96-7650-305b-aea0-91befb886efa | -14.6509 | -45.140301 | 2025-05-08 00:17:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| de31e1c8-fa8f-3ea3-84b8-9f910368ff91 | -13.4977 | -52.9426 | 2025-05-08 00:17:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 138f6dff-9aac-3f30-8872-79281fe3d7f9 | -6.7065 | -42.1418 | 2025-05-08 00:17:00 | METOP-B | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cdcd30f3-bebc-3cf5-965f-59c1458c71ac | -5.1626 | -45.095501 | 2025-05-08 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8368726c-5318-3b00-80e5-0066983f561b | -4.0027 | -43.245998 | 2025-05-08 00:17:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae1880fe-0dd9-317a-a5b3-4a005fae2dd9 | -19.5301 | -43.908199 | 2025-05-08 00:17:00 | METOP-B | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ff5adb76-4389-3da7-9dbe-aff037e1fcce | -23.6019 | -48.996101 | 2025-05-08 00:17:00 | METOP-B | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 341140b4-339b-3dde-87ad-61b368c862ee | -13.0393 | -53.710201 | 2025-05-08 00:17:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e0142b8-78a2-351a-a9aa-2e08f3bc05a0 | -10.7269 | -42.3083 | 2025-05-08 00:17:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 614ddcaf-8c02-3cde-8289-63297134baad | -11.7819 | -48.694801 | 2025-05-08 00:17:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bcfc8cf2-3536-38a5-b41f-01d83b8ace55 | -14.6476 | -45.125801 | 2025-05-08 00:17:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c64a81f2-fe2f-3680-8f18-ee45a8ef099c | -15.8239 | -46.574001 | 2025-05-08 00:17:00 | METOP-B | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 26cbd24e-7a34-3d47-b16a-d85beda0fd53 | -6.7036 | -42.129601 | 2025-05-08 00:17:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3b6b32b6-8f80-3c99-8259-4f1953d04ba6 | -10.7196 | -42.321098 | 2025-05-08 00:17:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4c73ba54-caa9-34b5-b0c4-dc230e6aacf2 | -15.8223 | -46.566898 | 2025-05-08 00:17:00 | METOP-B | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 818d671e-a3c4-3421-b1b5-84152c7ae241 | -13.3639 | -54.2351 | 2025-05-08 00:17:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15d87cc0-5778-3bde-981d-65cc7d7e49f5 | -15.8321 | -46.564602 | 2025-05-08 00:17:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6c808e35-4a11-37ad-9b8a-f9155fbf5f74 | -8.0805 | -43.110802 | 2025-05-08 00:17:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 19b311db-9efd-3f2f-928c-131bc3144f00 | -14.1051 | -44.240799 | 2025-05-08 00:17:00 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52a80490-9812-32f2-9cce-35652a57b878 | -10.7171 | -42.310699 | 2025-05-08 00:17:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a77cadd0-4aeb-30d6-a0da-2569f99b586d | -14.646 | -45.1185 | 2025-05-08 00:17:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34e642e9-3b30-31de-9a8d-f1a1e1d56af8 | -6.9695 | -47.915401 | 2025-05-08 00:17:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91619368-ebae-32a3-9a23-9573528460fc | -15.8352 | -46.578899 | 2025-05-08 00:17:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3e6fd907-3ffe-3378-affe-00df9553b46b | -5.1646 | -45.103901 | 2025-05-08 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ced13189-bbe0-33ab-b59c-364871a27396 | -13.4906 | -52.9575 | 2025-05-08 00:17:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74d925b1-b1c3-3bc5-a229-b828ec21e3d4 | -5.798 | -43.616501 | 2025-05-08 00:17:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c86ccb85-5d9f-3ca6-82e0-bc5561bb31af | -20.7628 | -43.6548 | 2025-05-08 00:17:00 | METOP-B | SANTANA DOS MONTES | MINAS GERAIS | Brasil | 3159100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d9e86b11-7aee-3c9f-8579-9a99599370f9 | -8.07 | -43.1216 | 2025-05-08 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 2d5e1a00-fe2d-3777-89e3-fe47c5821c5b | -15.8208 | -46.5763 | 2025-05-08 00:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 61.7 |
| f6c576b2-2c49-3bdf-827e-3e434fa6348b | -8.0889 | -43.1196 | 2025-05-08 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 65e3a6fa-31a2-3862-bf22-94e1cef77b73 | -14.6414 | -45.1263 | 2025-05-08 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 6972b887-247e-3958-b5fa-3e57748ff3ea | -13.4901 | -52.9715 | 2025-05-08 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 45d34231-47d8-3e3b-ba87-da9a7b098803 | -13.5093 | -52.9692 | 2025-05-08 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 070d36f5-7120-3fe1-a3d5-bcc136c224b3 | -8.0889 | -43.1196 | 2025-05-08 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| ec52e1df-99ac-337a-a62a-2e7655048695 | -13.4901 | -52.9715 | 2025-05-08 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| fa701f9f-f184-3ece-a689-a38e55602350 | -14.6414 | -45.1263 | 2025-05-08 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| b0c70b20-05d5-3a64-bd6a-adb33ae1c97c | -15.8208 | -46.5763 | 2025-05-08 00:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 3208de06-cc26-3813-a2d2-88f71ceb392b | -13.5093 | -52.9692 | 2025-05-08 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 84402e0a-f5ff-3ab4-bde9-b2477d193550 | -8.07 | -43.1216 | 2025-05-08 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| a037d196-1f3a-31ac-a2c3-9c3f07af37b9 | -14.0964 | -44.2397 | 2025-05-08 00:30:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 5c91a782-e554-3532-b2f3-47b4546b348a | -13.4901 | -52.9715 | 2025-05-08 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 0c6a3703-a95e-3526-91a7-617554651e97 | -8.0889 | -43.1196 | 2025-05-08 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| a33717a5-9413-3a06-87f6-0131b219c671 | -15.8208 | -46.5763 | 2025-05-08 00:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 1bd42b30-0faf-39b4-9cd9-08331dca86af | -14.6414 | -45.1263 | 2025-05-08 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 4355997d-7775-3e87-8aea-ebe0d92d6f97 | -14.0964 | -44.2397 | 2025-05-08 00:40:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 7a9b7f37-5b1b-3505-beb6-988bbd38d324 | -13.5093 | -52.9692 | 2025-05-08 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 485daf58-da09-3bda-8793-a7cd2fbd9ab6 | -8.07 | -43.1216 | 2025-05-08 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 94fdb6c0-7da7-3538-a50b-266d47a77a3e | -14.0964 | -44.2397 | 2025-05-08 00:50:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| bb82bf35-7b2a-320f-82c5-17c126a90013 | -13.4901 | -52.9715 | 2025-05-08 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0b3edce8-f07a-34ca-8329-9d6f84f03ea3 | -13.5093 | -52.9692 | 2025-05-08 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 63ea2829-53ea-376d-9ad0-c65b6221b67e | -8.0889 | -43.1196 | 2025-05-08 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| f2eabd0a-70e4-327a-9e62-9e69e0acf45d | -14.6414 | -45.1263 | 2025-05-08 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 149a7a55-2d35-3ee4-b809-688b92297acc | -15.8405 | -46.5726 | 2025-05-08 00:50:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 5b827fe6-aa1c-3b0b-8311-ed334608e6c3 | -8.07 | -43.1216 | 2025-05-08 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| aaf271c9-b4ad-3c5c-bd5b-a830ede0b7d6 | -8.0889 | -43.1196 | 2025-05-08 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| e73cde6c-91d7-3545-b286-eb1aa0d01fc2 | -8.07 | -43.1216 | 2025-05-08 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| bb6dfa17-7e28-3ae3-b19a-282d2895cead | -14.6419 | -45.1028 | 2025-05-08 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| e5ea91c7-db4b-3684-b1f5-1fc90b6032d2 | -14.6414 | -45.1263 | 2025-05-08 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 3701f87b-9e7f-37e5-97d9-5eff0c62cd9f | -15.8405 | -46.5726 | 2025-05-08 01:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 98325fd9-b9a5-37f0-bc1c-444f3b6abcbd | -13.5093 | -52.9692 | 2025-05-08 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| d533536d-d71d-3e9c-843b-8bbe20b15c9a | -13.4901 | -52.9715 | 2025-05-08 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 35a30a99-bd9d-355d-a0e0-e31ce4f25bd2 | -8.092 | -43.117401 | 2025-05-08 01:07:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c31b2d85-810f-3ff9-ba8b-cd314cfb8882 | -20.566099 | -54.072498 | 2025-05-08 01:07:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1b8c7cac-5380-30f3-a173-007b75359b8c | -23.5996 | -49.0121 | 2025-05-08 01:07:00 | METOP-C | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 30588368-8052-3e85-a8ea-e81ff759c6b5 | -22.6817 | -49.827801 | 2025-05-08 01:07:00 | METOP-C | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3c839f7a-bdcd-3b1c-9a3c-be88ebc595d0 | -19.057501 | -53.453602 | 2025-05-08 01:07:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| eb454597-5375-3275-9a1e-38c96c82e882 | -23.607401 | -49.001301 | 2025-05-08 01:07:00 | METOP-C | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0cdf7a6d-abd9-3146-9af9-09a12c48bb30 | -8.0906 | -43.1507 | 2025-05-08 01:07:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3425c902-9c8f-3c6f-85c6-9e6dde968b6f | -23.5977 | -49.003899 | 2025-05-08 01:07:00 | METOP-C | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f2f210bb-a3b2-3f1f-b6f1-0b9f7b16b8b3 | -20.388201 | -55.395901 | 2025-05-08 01:07:00 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c4a25d4d-b4d8-3b7a-befe-aefac3eec4d4 | -23.609301 | -49.009499 | 2025-05-08 01:07:00 | METOP-C | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 06d4f477-a8c3-32e0-8292-888f36541273 | -20.0676 | -49.364201 | 2025-05-08 01:07:00 | METOP-C | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95a617cf-587b-3475-9aef-6888a8dd619c | -8.0824 | -43.1199 | 2025-05-08 01:07:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5a35fda0-9692-35ae-a94a-890a74e0a4db | -21.7959 | -52.752602 | 2025-05-08 01:07:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9766696e-5174-3304-97f6-2d8534423fbe | -20.069599 | -49.372601 | 2025-05-08 01:07:00 | METOP-C | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9222e385-e14f-3e2a-96f5-7d73b7f4e7fc | -20.386499 | -55.387199 | 2025-05-08 01:07:00 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dfdf4cb8-56fd-34d5-8cce-460f3173ec11 | -21.0606 | -56.001301 | 2025-05-08 01:07:00 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| eb84604c-ce22-354f-9737-fb2a9e9f015b | -19.067301 | -53.451302 | 2025-05-08 01:07:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| acb630d3-665f-34f0-95a3-7f05fbd0277f | -6.5866 | -51.115501 | 2025-05-08 01:07:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd6ef273-02c2-3037-814b-6950a1d2a93b | -23.6128 | -48.9944 | 2025-05-08 01:10:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9de50bce-f8d4-3b09-b1b9-5600c1f18a1b | -8.07 | -43.1216 | 2025-05-08 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| b9580ae0-b158-38bd-a6b1-22255a42f078 | -8.0889 | -43.1196 | 2025-05-08 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| e0a1e6e2-94af-3cb7-bb21-1795adfaf31d | -14.0964 | -44.2397 | 2025-05-08 01:10:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 724b49f5-83ac-325d-bf1b-f2d8ee7937c7 | -13.4901 | -52.9715 | 2025-05-08 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| ffc9396d-6825-3c15-969b-0686045c666b | -14.6414 | -45.1263 | 2025-05-08 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 63425b3d-773f-3d7e-be77-2d1e9886361b | -14.6414 | -45.1263 | 2025-05-08 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| c7f5103e-24f1-30f8-bf3e-08462136f7ab | -13.5093 | -52.9692 | 2025-05-08 01:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 1a1a97ce-5297-34f9-9b2b-494fbe6b0955 | -8.0889 | -43.1196 | 2025-05-08 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 2893d6ae-e0ec-3df3-a9af-379232453bd7 | -14.0964 | -44.2397 | 2025-05-08 01:20:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| c524a348-f541-3129-904c-da14384787e8 | -8.07 | -43.1216 | 2025-05-08 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| bb50827e-f260-3257-a677-36eb707245ed | -14.6414 | -45.1263 | 2025-05-08 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 3f855529-4074-3b73-8d9e-bec9a02b480e | -8.07 | -43.1216 | 2025-05-08 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| a99f51cb-856f-311d-84ce-9716ab484030 | -13.5093 | -52.9692 | 2025-05-08 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| ca73830b-92a0-375d-9df6-8d0efed8567a | -8.07 | -43.1216 | 2025-05-08 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 0fcdd170-fb60-33d9-8aee-245b0cee532b | -14.6414 | -45.1263 | 2025-05-08 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 23cad9c7-8f26-3939-b679-1f1cb4a14c1c | -8.07 | -43.1216 | 2025-05-08 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| fb2fb18f-1ac6-315a-af04-bd8ba33924b5 | -14.6414 | -45.1263 | 2025-05-08 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 8903ea8c-762b-36ee-bc1d-eb9cf0b25867 | -8.0889 | -43.1196 | 2025-05-08 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.1 |


[Clique aqui para ver as próximas entradas](README3.md)
