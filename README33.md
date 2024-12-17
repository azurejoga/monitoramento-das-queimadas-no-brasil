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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e06b971-8521-3f24-867e-2ea4a4585bc6 | -6.9424 | -42.8126 | 2024-12-17 13:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| e1c5a6d7-68ab-3d55-9e98-b8dc6c73bebe | -6.9801 | -42.809 | 2024-12-17 13:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 6608dd2a-7b3e-3682-bf8f-731d3cedeb4e | -6.9799 | -42.8326 | 2024-12-17 13:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 132.4 |
| 82e491e5-d53b-386a-b3b8-48b12f9bb80a | -6.961 | -42.8344 | 2024-12-17 13:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 172.7 |
| 6a2754af-ad94-3f70-9fc2-a097d13e9d98 | -6.9422 | -42.8362 | 2024-12-17 13:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 1772f7c4-59fe-33c6-aebe-f9aa6578b9da | -6.9422 | -42.8362 | 2024-12-17 13:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 00fd1a71-f2d7-3ce0-8c1e-198a36463f81 | -4.2152 | -43.9939 | 2024-12-17 13:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| a0e8d43c-e397-323b-9aff-e5de70a530e9 | -4.9643 | -43.7182 | 2024-12-17 13:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 66cf4d74-6cc3-35c4-9ce2-97526441df88 | -3.5935 | -41.8489 | 2024-12-17 13:30:00 | GOES-16 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| f6a52916-7219-3cbf-bb2c-178de38730cd | -4.9024 | -42.08 | 2024-12-17 13:30:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 148.0 |
| d0ba77a8-f394-3e85-b0a1-d1d24b24cdb4 | -7.2397 | -41.5667 | 2024-12-17 13:30:00 | GOES-16 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 5fed2efa-49e4-3997-a1b6-c5aad2d32ebb | -3.704 | -42.1287 | 2024-12-17 13:30:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 490b155f-dad1-35f0-badc-e012ecb48064 | -6.9801 | -42.809 | 2024-12-17 13:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 444b11fe-1b77-3b5c-ac9f-4317d3cd0e7b | -6.9424 | -42.8126 | 2024-12-17 13:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 2738c0b5-ec56-3024-8385-8f3fcb3ab3e8 | -6.9799 | -42.8326 | 2024-12-17 13:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 701ecc73-acd4-3555-9eff-dca2d7e5184f | -6.9422 | -42.8362 | 2024-12-17 13:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 41c0111c-76fb-36f2-aec6-89821f64c1d6 | -4.9643 | -43.7182 | 2024-12-17 13:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 53ed7678-d1d8-3cfc-9384-4f9dbe4dcd37 | -6.9424 | -42.8126 | 2024-12-17 13:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| d13c3376-9872-3265-bbc6-e638414006b7 | -6.9801 | -42.809 | 2024-12-17 13:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 24fb6fbe-2a54-325d-81b0-a2698fabcb50 | -7.2397 | -41.5667 | 2024-12-17 13:40:00 | GOES-16 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 7b3af3c6-195e-3662-873d-2f098ffabc94 | -6.9799 | -42.8326 | 2024-12-17 13:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 129.0 |
| bbdc7272-abc1-33fd-aeaf-824c47192a10 | -3.704 | -42.1287 | 2024-12-17 13:40:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 27dedea6-5ef3-3817-94a0-f4d053351e2c | -4.2152 | -43.9939 | 2024-12-17 13:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 23fb7330-b67a-3d45-a3a8-3bf6bce14077 | -4.8707 | -41.3639 | 2024-12-17 13:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 5c03927c-fdbe-3e5b-b14e-a686a366db8f | -3.5935 | -41.8489 | 2024-12-17 13:40:00 | GOES-16 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 72c10212-da44-3985-8659-beba6b733c71 | -3.5583 | -44.7581 | 2024-12-17 13:40:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 51bb7cf4-15d8-38a7-a290-6e28b8147d90 | -4.9024 | -42.08 | 2024-12-17 13:40:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| 57708172-e693-3ed3-ad03-507c2d93e120 | -4.9024 | -42.08 | 2024-12-17 13:50:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 133.9 |
| d2f22744-17ce-3463-a0d0-7de3d7909641 | -4.9643 | -43.7182 | 2024-12-17 13:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| c1be29ad-e04d-3e79-9c22-cc7663e056c6 | -6.9799 | -42.8326 | 2024-12-17 13:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| 040f035c-b3cb-359f-a8e5-75dd032e6ed8 | -10.167 | -42.4558 | 2024-12-17 13:50:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 88fe49b0-2a9f-3e52-b73c-bac4750397d0 | -3.5935 | -41.8489 | 2024-12-17 13:50:00 | GOES-16 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 0b2f23ff-704c-37ff-bf07-d92c4f562ad1 | -5.8127 | -43.0517 | 2024-12-17 13:50:00 | GOES-16 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| a1631499-78f9-3ad4-92bb-e60146906694 | -6.961 | -42.8344 | 2024-12-17 13:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 189.7 |
| 21152b13-87cb-316c-8fcd-b2de36dbd9ca | -6.9801 | -42.809 | 2024-12-17 13:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 37e22228-1a6a-354a-84b5-cd87a9ddd2e6 | -6.9424 | -42.8126 | 2024-12-17 13:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| 54f9e160-509c-3a80-a469-59b9d6b4aeaf | -6.9422 | -42.8362 | 2024-12-17 13:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 9a2c0dd9-a988-3932-9730-6e864c120d6b | -3.704 | -42.1287 | 2024-12-17 14:00:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 773f5830-b353-360a-81a8-299c472ffb31 | -6.9799 | -42.8326 | 2024-12-17 14:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 112.4 |
| bc66b37f-58b6-396b-9006-a31071481643 | -3.4616 | -42.0221 | 2024-12-17 14:00:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 69f8bf13-e101-3297-923c-c55d199c7c0b | -6.7673 | -38.3904 | 2024-12-17 14:00:00 | GOES-16 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 5b7ec79b-eb06-3bbe-a8e6-838116b180c5 | -4.9024 | -42.08 | 2024-12-17 14:00:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 0def9ff9-125b-3831-80a0-60c60549d4ba | -2.8635 | -42.0488 | 2024-12-17 14:00:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 10e4ef4c-0c7a-3fd9-937c-c424fc679cec | -3.4915 | -43.3368 | 2024-12-17 14:00:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 2f12467b-0964-34eb-9214-5b9a258c61d0 | -4.8707 | -41.3639 | 2024-12-17 14:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 24e6ed7d-67fc-305e-b1e7-a322c4a895e3 | -4.9643 | -43.7182 | 2024-12-17 14:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| b388e069-4369-395b-a4ac-4e4acdfdfa1e | -6.9424 | -42.8126 | 2024-12-17 14:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| fbffd72b-f056-3d4a-8a48-714056ead869 | -5.9373 | -43.7642 | 2024-12-17 14:00:00 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2553dcd2-4696-3891-a649-9d0fab3ab65b | -3.6296 | -42.0613 | 2024-12-17 14:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| a6439fcd-3d95-3852-84bb-92174adb86a1 | -6.9613 | -42.8108 | 2024-12-17 14:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 196.1 |
| 67231108-27e7-31c3-9f66-6a0737114b5b | -3.6111 | -42.0385 | 2024-12-17 14:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 1a96b9af-01e5-3d74-bd16-d59680393151 | -6.961 | -42.8344 | 2024-12-17 14:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 179.9 |
| 94ab32c0-c71a-3153-9c9f-e1b3279eec8f | -6.9422 | -42.8362 | 2024-12-17 14:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 9d18c8f3-0ce9-34e7-8719-a09fe4ca27f0 | -6.0836 | -44.1454 | 2024-12-17 14:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 36dc3e60-da41-3677-9981-3cc39e896f4b | -5.8127 | -43.0517 | 2024-12-17 14:00:00 | GOES-16 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 807593dd-ae82-3892-b24b-ec975451527d | -3.0 | -42.16 | 2024-12-17 14:00:00 | MSG-03 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87f86049-9b45-37c4-92da-5b66e05744ea | -3.6296 | -42.0613 | 2024-12-17 14:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 7c40ccc7-35f0-3247-b258-dadc331579c2 | -6.7673 | -38.3904 | 2024-12-17 14:10:00 | GOES-16 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 85.9 |
| f8146050-e103-36e0-9c9b-fa48882d3991 | -3.6111 | -42.0385 | 2024-12-17 14:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 4fd18f6e-4d8b-34de-925a-d614d0f9140f | -5.0936 | -43.9176 | 2024-12-17 14:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d2f0971b-bad9-397e-84d7-a2dcfff83e4b | -6.961 | -42.8344 | 2024-12-17 14:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 173.0 |
| 6ccac4df-1d55-332d-8fba-1b3bb66e564f | -3.5922 | -42.0632 | 2024-12-17 14:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 022cbcd6-2cd5-3744-8ab3-5cf010712ee2 | -10.1287 | -42.4612 | 2024-12-17 14:10:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 871e1e62-7f9c-3f47-af47-e5909b752755 | -3.4658 | -44.6486 | 2024-12-17 14:10:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| e97a87be-c980-32b0-b643-cc4da0a6f71c | -4.9643 | -43.7182 | 2024-12-17 14:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 26770e84-0536-34bd-84f7-02fab8660a8d | -7.1486 | -41.286 | 2024-12-17 14:10:00 | GOES-16 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 3e8c665f-819e-3248-8d50-2028432f92e5 | -4.9024 | -42.08 | 2024-12-17 14:10:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 114.0 |
| adf16846-f30f-3898-8b3f-3e93efc76e8f | -6.9613 | -42.8108 | 2024-12-17 14:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 177.4 |
| d232023b-d6a1-3614-9e28-2d61ab8fef89 | -3.4915 | -43.3368 | 2024-12-17 14:10:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 4451429a-559e-3781-b72d-cfbdc9d87afa | -10.167 | -42.4558 | 2024-12-17 14:10:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 92.0 |
| bae01dc9-14dc-3b41-97af-32b6d58d476a | -3.4616 | -42.0221 | 2024-12-17 14:10:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| f536aac7-f365-3cb3-bac4-d7c223f64929 | -5.9373 | -43.7642 | 2024-12-17 14:10:00 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| a95c1e84-1fb8-3875-b21e-11aef8709a24 | -3.704 | -42.1287 | 2024-12-17 14:10:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 0dc0d705-e555-3058-8cd3-34dc96b16993 | -6.9799 | -42.8326 | 2024-12-17 14:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 7b987fec-3477-3826-96b6-d295a07a9208 | -4.9643 | -43.7182 | 2024-12-17 14:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 177.4 |
| e1890e87-e949-32fb-b2f7-8eba9c92aa25 | -5.9373 | -43.7642 | 2024-12-17 14:20:00 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3d0f34a3-7b32-3886-8aab-1dc257cc4e50 | -3.6296 | -42.0613 | 2024-12-17 14:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 4228e416-475d-3fa0-90a7-69b22732e673 | -3.087 | -42.1817 | 2024-12-17 14:20:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| b5554d23-77b3-3ae5-93f2-ad4c38da7d50 | -6.9613 | -42.8108 | 2024-12-17 14:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 167.2 |
| bb5b31cd-1705-3ee8-bfe0-444acd30b613 | -3.4616 | -42.0221 | 2024-12-17 14:20:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| de786116-d2b8-3b6a-980d-0f5e2707923b | -3.4915 | -43.3368 | 2024-12-17 14:20:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| dd0293db-6722-356b-8b12-b90cf306c656 | -6.9422 | -42.8362 | 2024-12-17 14:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 04a736d9-5576-3eb0-ac0a-3abcc1d8026c | -7.8711 | -38.2066 | 2024-12-17 14:20:00 | GOES-16 | SANTA CRUZ DA BAIXA VERDE | PERNAMBUCO | Brasil | 2612471 | 26 | 33 | nan | nan | nan | Caatinga | 76.0 |
| cc61c631-eca2-3519-b5c6-cd1c693591cc | -3.6111 | -42.0385 | 2024-12-17 14:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 795af76a-80e0-3581-9fe2-a6b966f08992 | -6.9424 | -42.8126 | 2024-12-17 14:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 91d6cebf-914a-394e-9993-86c2a4f6e8bb | -3.5922 | -42.0632 | 2024-12-17 14:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| d3e1ff69-146d-35f1-9e32-f6a94d3663cb | -6.961 | -42.8344 | 2024-12-17 14:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 176.0 |
| ec1c152f-3ea6-3b48-94ff-3cea2a56b90d | -5.0936 | -43.9176 | 2024-12-17 14:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| aedd92ea-37fb-329d-b50a-20bd44fc0a4d | -3.704 | -42.1287 | 2024-12-17 14:20:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 70fddf9b-ef10-34f4-b80b-c4cc35ed7e61 | -10.1287 | -42.4612 | 2024-12-17 14:20:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 46424368-d3fc-3dc9-b7cf-e131a2ab6918 | -7.2397 | -41.5667 | 2024-12-17 14:20:00 | GOES-16 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 7baf7a7a-7cd2-3600-a5ff-84cc5027d88a | -10.167 | -42.4558 | 2024-12-17 14:30:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 95.2 |
| e7d27bb3-7c1a-323d-9ca8-bbfc34a22f81 | -10.1287 | -42.4612 | 2024-12-17 14:30:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 91.7 |
| f27ec13e-dea2-330e-b6d9-28790af4f5f6 | -3.4616 | -42.0221 | 2024-12-17 14:30:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 69d3c859-45ef-3cf8-a0b0-24206a5bb34c | -6.9424 | -42.8126 | 2024-12-17 14:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| aa75bd3e-2537-33bd-93ac-17499f94bf80 | -6.9799 | -42.8326 | 2024-12-17 14:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 91308e68-ced9-38d0-8f42-9149adbe356d | -7.1297 | -41.288 | 2024-12-17 14:30:00 | GOES-16 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 9242c4d3-506f-3aa4-bc48-947d5207bc25 | -6.9801 | -42.809 | 2024-12-17 14:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 5c88d355-aac5-30b9-8021-b7bbdd50d6f0 | -5.9373 | -43.7642 | 2024-12-17 14:30:00 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| d3988c85-ed4c-34fb-bd27-80b24c3bf701 | -3.5298 | -43.1721 | 2024-12-17 14:30:00 | GOES-16 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |


[Clique aqui para ver as próximas entradas](README34.md)
