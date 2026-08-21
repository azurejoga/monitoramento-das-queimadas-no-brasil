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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e29a36d3-4ee2-3bbe-97eb-4d2f01c3b63e | -13.4516 | -51.7736 | 2026-08-21 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 8ffa000b-9c8a-364c-8abf-a580cea6d589 | -11.1561 | -54.0028 | 2026-08-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 347e4e3a-3e12-3471-9074-44cadc316bcf | -11.1558 | -54.0233 | 2026-08-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| b54312f7-9418-3c76-abb4-45b3b151fd43 | -5.6024 | -45.6815 | 2026-08-21 14:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 622bc525-dab3-364b-b46a-f92076012316 | -11.175 | -54.001 | 2026-08-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 152.2 |
| a513310f-b9fc-3b64-8222-2ff83c1b6987 | -5.6166 | -44.0196 | 2026-08-21 14:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 244.7 |
| 55e5ef74-2a79-3c8e-a0d0-e37c20410c2a | -8.4554 | -46.9628 | 2026-08-21 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| c172b413-c165-390b-88ac-d442f6b095bd | -13.3926 | -54.3758 | 2026-08-21 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 72f7db03-5086-3567-a833-9a516a46a386 | -13.7384 | -51.8438 | 2026-08-21 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 5ad71908-68d3-3194-bcce-440d49fd22c4 | -8.5173 | -55.3441 | 2026-08-21 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| f75943bc-4ead-37bb-b22c-75cae79c03e8 | -13.3734 | -54.3779 | 2026-08-21 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 7151abdf-c7d1-38d4-aeb4-d0ee3c3dcfd3 | -13.738 | -51.8651 | 2026-08-21 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| b5caa1f0-1d9c-31d2-ad48-d39ccea1f65b | -6.8937 | -47.4738 | 2026-08-21 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9a79198a-65e8-3763-af21-dd86a327a48f | -9.0536 | -60.435 | 2026-08-21 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 21f49116-e5e6-37e1-bb51-ac2bcd2cdcc8 | -6.1177 | -59.9069 | 2026-08-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| f8195d76-e4b3-3b55-9106-c8836a2efddf | -9.4257 | -60.416 | 2026-08-21 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| af2c8800-c6b0-345a-b8a7-db80d81cff6e | -11.1747 | -54.0216 | 2026-08-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 6f2c7c4b-b80f-3b52-91f5-493b7f43ab92 | -13.432 | -51.7973 | 2026-08-21 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 6755dbf6-243b-3728-91e5-542a638e2cbf | -9.3238 | -56.9064 | 2026-08-21 14:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 15306c18-8c96-34b7-bad8-205b89b05eb6 | -8.3717 | -62.716 | 2026-08-21 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 8110bd22-d413-38d1-9401-07ed54be4a41 | -13.7188 | -51.8675 | 2026-08-21 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| a7647f1d-fdf0-37df-ae62-51071ebe11d7 | -8.3903 | -62.6963 | 2026-08-21 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 1c7e39d2-b9a5-370c-b1a0-8cc9062b0432 | -8.5359 | -55.3428 | 2026-08-21 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8f51c004-46b7-3608-85c2-dc3b145ed1c3 | -6.3654 | -58.3354 | 2026-08-21 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 1c6169ad-996f-3f90-a7ea-66e69de9ceaa | -5.598 | -43.9978 | 2026-08-21 14:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 333.0 |
| a5b3b1f0-84fc-311a-810e-fe0312127feb | -8.8856 | -60.5394 | 2026-08-21 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 49e097cd-2653-3049-b0d9-b35d6a310ec4 | -10.7696 | -50.2948 | 2026-08-21 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 111118ba-c096-3ff4-987d-a2126b6166e2 | -9.4259 | -60.3967 | 2026-08-21 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 085c460f-678f-354a-93a5-62dc6208fdb4 | -6.1176 | -59.9261 | 2026-08-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| fb444086-be6a-3b14-b20c-acb3ec457cca | -9.4552 | -48.3155 | 2026-08-21 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 118e9eaa-10d4-3825-9d2a-5578806eb5f9 | -6.95 | -59.2984 | 2026-08-21 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d10be813-a486-321b-b082-315a75430315 | -6.5829 | -58.9851 | 2026-08-21 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 4e387eb5-880f-3233-a50c-df4e6afbf14f | -13.3929 | -54.3551 | 2026-08-21 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a954fc34-8b55-3262-897b-7e08a8fb981c | -5.598 | -43.9978 | 2026-08-21 14:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 53663027-31f6-3cca-8c4f-d14aa588d924 | -13.4117 | -54.3737 | 2026-08-21 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| bfb21285-9244-34f4-b6d8-933032ed10b4 | -5.6024 | -45.6815 | 2026-08-21 14:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 48e5a662-c472-3e78-a328-1d84a59a82b5 | -10.3148 | -50.3848 | 2026-08-21 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 812fefb9-6043-39a9-aadf-25e29b39baf3 | -11.175 | -54.001 | 2026-08-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 65623839-6c0f-3316-9cfc-0f7b44529925 | -14.5469 | -53.0106 | 2026-08-21 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 71196d57-2d81-33f3-ac2b-b57c686a5a5e | -6.1362 | -59.8871 | 2026-08-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0e8790a5-c451-3406-bf8a-74344d2f93cf | -11.1747 | -54.0216 | 2026-08-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 92b83a52-5dc2-35ce-8c01-2f96dc614227 | -10.7696 | -50.2948 | 2026-08-21 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 8203107d-d1ac-34cb-a9ce-5443f074f41d | -8.3902 | -62.7152 | 2026-08-21 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ab38c58f-9482-3e86-b43f-0756a6c3706e | -8.3717 | -62.716 | 2026-08-21 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| dc2396a5-fa08-3ecd-84db-23be0902ad21 | -8.3903 | -62.6963 | 2026-08-21 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 32ec2847-3ff5-3b0d-b2d0-cb7b12b55003 | -13.7384 | -51.8438 | 2026-08-21 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 26f24fab-ae7b-3a0e-b753-7ca3444ce2fd | -13.738 | -51.8651 | 2026-08-21 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ed1cf1e1-1938-3e97-a25a-3031e8b8d834 | -6.3654 | -58.3354 | 2026-08-21 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 7606129e-b3cd-3130-bb5d-ae0d750f7805 | -9.4061 | -60.5518 | 2026-08-21 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| ea53a161-3a21-32c0-857b-c1b72108113a | -8.9041 | -60.5577 | 2026-08-21 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 4fe43214-45d3-3d51-9bc2-56d7f42ac8d7 | -9.4072 | -60.3977 | 2026-08-21 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| d7032d11-57ce-318f-b8c1-ab48633cb5f5 | -9.4069 | -60.4362 | 2026-08-21 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 131598bf-695e-303a-b208-6bd197b9c9b4 | -13.412 | -54.3531 | 2026-08-21 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| d43be062-ef14-3ef4-8eac-1063e6d57d4f | -9.4071 | -60.417 | 2026-08-21 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 218.1 |
| 9ca0cc34-86b5-3e77-be3b-3e485d004744 | -8.5175 | -55.324 | 2026-08-21 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| ab85deda-3070-3ade-873c-7f9e8b0e82ff | -14.3149 | -51.8969 | 2026-08-21 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b588dcd1-e08d-3455-ba38-6f8331e51c0c | -6.2156 | -55.6118 | 2026-08-21 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 3cf03456-e537-326b-bfff-0f8881e5b16f | -6.2341 | -55.6109 | 2026-08-21 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| a8d999b3-3189-3ac0-bd98-dead0765ed9e | -6.8937 | -47.4738 | 2026-08-21 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| eb9b93dc-93c0-3be7-b1ea-fb98cf5d45d1 | -13.3734 | -54.3779 | 2026-08-21 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c66e44df-be86-319d-8397-bbcfdaa87a83 | -14.5662 | -53.0081 | 2026-08-21 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| f64cd139-3a80-338c-8989-07a2dd60c8a1 | -6.5828 | -59.0044 | 2026-08-21 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| b476701d-7438-34ab-85bf-3272c64c0c08 | -9.4558 | -48.2717 | 2026-08-21 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| f9745dd5-7a72-3f6e-a7b7-cecfd60d9b69 | -15.1984 | -48.2296 | 2026-08-21 14:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 254.8 |
| 80b9cccd-d8e5-35d0-9dde-9c20946b528d | -11.1561 | -54.0028 | 2026-08-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| fd04329d-cd96-34f9-8720-4ba4acaaf9aa | -8.8855 | -60.5586 | 2026-08-21 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 85ab23f9-da50-3c81-9080-d7e5df6de9f3 | -5.6168 | -43.9965 | 2026-08-21 14:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 8e410de9-1132-3661-a00e-9ff2124fbafe | -14.3343 | -51.8944 | 2026-08-21 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| a08e3a65-9813-398e-849e-723aa9596633 | -6.1361 | -59.9063 | 2026-08-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 19c81c0a-9f1a-3e2b-bcf3-0c0f4292f39f | -9.0536 | -60.435 | 2026-08-21 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 8ed97397-17ac-3182-ad2d-66853e31270f | -11.1558 | -54.0233 | 2026-08-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 2cf13c64-faef-3f72-a80e-f26cd21c1c60 | -8.5361 | -55.3228 | 2026-08-21 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 190.0 |
| f46e76fe-5e98-3121-8690-95a5186533b9 | -10.7504 | -50.3182 | 2026-08-21 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 37759595-137f-3379-9d61-e8160bc7518a | -8.9042 | -60.5385 | 2026-08-21 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 165.9 |
| d8d92588-cb9b-34ed-9ddb-0193f1291402 | -15.218 | -48.2263 | 2026-08-21 14:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| acedfd45-2d67-3dbc-88d4-6230b7acbd49 | -8.5359 | -55.3428 | 2026-08-21 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 191.7 |
| 16c71bab-20f8-38e8-a2c4-15f3744dfc2d | -13.4516 | -51.7736 | 2026-08-21 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 4e1b495a-8d74-385d-97ed-3d7d6a06ca2a | -9.4257 | -60.416 | 2026-08-21 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 30373205-8837-3762-b50b-71da16904740 | -13.7188 | -51.8675 | 2026-08-21 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 3974a4d7-a28b-3be8-94fa-6a4be2fb37fb | -13.6243 | -51.7732 | 2026-08-21 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 9e5c0d66-4259-3ebc-b4a0-d68d920f20bd | -6.2487 | -48.6506 | 2026-08-21 14:30:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 7b9aca16-8e89-33a6-8c64-f174f56c084c | -13.3926 | -54.3758 | 2026-08-21 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 16c82703-83fa-389c-aa0b-05eb592046ad | -3.2178 | -61.2551 | 2026-08-21 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f25eb947-9687-3cd7-a6d9-68aea1b466ff | -8.0467 | -51.804 | 2026-08-21 14:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f7f5b24a-3f59-3088-97e2-0e649d124c38 | -11.367 | -45.9949 | 2026-08-21 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| f36ab8a7-49fd-325f-acce-b378910c9641 | -9.4259 | -60.3967 | 2026-08-21 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| c0989c98-05bb-3108-8ebd-a4b52a950a65 | -6.1177 | -59.9069 | 2026-08-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 3d1d418c-6f9a-3a2f-81ed-eb6e9ad468b9 | -13.432 | -51.7973 | 2026-08-21 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 7a546cbd-82ad-3358-a407-de100818bcfc | -5.621 | -45.6802 | 2026-08-21 14:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d5ccffc2-1890-3ea7-ae2a-6e13cecd594a | -8.5173 | -55.3441 | 2026-08-21 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| faf41e7f-1f50-3042-b70d-67aa68d2de1a | -6.2538 | -55.4109 | 2026-08-21 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0cd631c1-0030-3c4e-9d8d-8c3da152724a | -6.1176 | -59.9261 | 2026-08-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5b3d7f5b-dc67-3087-95fa-dd1970482e2a | -6.3655 | -58.316 | 2026-08-21 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8c2a442b-33b5-3c92-9e0b-f1bf75ac4d98 | -9.208 | -59.6548 | 2026-08-21 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 343503bd-1c7b-3846-901e-15d6691019f6 | -15.2263 | -52.8587 | 2026-08-21 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f7e60a99-56fc-3840-abcc-00264d427316 | -6.6014 | -58.9844 | 2026-08-21 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 03f22646-78c9-3e8b-83ef-6c3cb75db843 | -8.8856 | -60.5394 | 2026-08-21 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| dc5962e2-36f8-3a04-a034-93c55883442b | -6.583 | -58.9658 | 2026-08-21 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2424b7cb-fe9f-362e-924a-745245105d3a | -13.6624 | -51.7897 | 2026-08-21 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| a2209fc1-74bf-3b7a-b242-082102c6bbd7 | -10.3151 | -50.3634 | 2026-08-21 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |


[Clique aqui para ver as próximas entradas](README95.md)
