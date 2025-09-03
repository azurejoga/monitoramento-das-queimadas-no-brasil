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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7584bff-ea85-3154-83d6-78f4f7c18eb4 | -9.1375 | -49.6444 | 2025-09-03 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 41d7a6b5-269e-3ec6-bbd8-05d42ad841e6 | -17.941 | -47.1718 | 2025-09-03 01:40:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 0cdb35cd-a07e-3009-88fe-a3d9014e83cf | -4.9122 | -43.2103 | 2025-09-03 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c2e87436-6760-3554-99ac-fc1082b1cd26 | -12.9387 | -56.9454 | 2025-09-03 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 52e5daeb-50c0-329d-bcd1-c6e7baa54707 | -15.5656 | -48.3918 | 2025-09-03 01:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| d9a1d9df-5d91-3231-be76-bb0c80d25e9a | -5.6079 | -45.0265 | 2025-09-03 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 34ca7b48-ed1d-308b-8339-390c7a96f0aa | -11.6647 | -57.3533 | 2025-09-03 01:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 25398bf2-9c8a-3eef-bc22-c1ca52d1f1b2 | -10.4853 | -50.346 | 2025-09-03 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 06e05e00-cd9d-3cce-8eb8-2837eb32c1f7 | -11.1228 | -44.6288 | 2025-09-03 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 08a2b941-f62f-3634-8f44-84c53f8eac9a | -9.3394 | -55.2277 | 2025-09-03 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 5b9068c1-fb9e-3718-b35b-cf99791fc192 | -4.8935 | -43.2115 | 2025-09-03 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 195.7 |
| cbe17974-967d-31fc-8f01-fd07a8bc4a49 | -11.1224 | -44.6521 | 2025-09-03 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 1ad7a8ed-ce4f-3cab-9472-ace48233e4a9 | -7.7039 | -48.7371 | 2025-09-03 01:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 966746f1-90f1-3d9a-8aff-ba2ec0c6b2c5 | -17.921 | -47.1759 | 2025-09-03 01:40:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 4cfd7a17-8139-3e18-a700-a093d799b862 | -3.2306 | -47.1131 | 2025-09-03 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 0b19d779-f977-3e74-b41e-3f89db4e53ce | -12.9382 | -56.9856 | 2025-09-03 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 176.8 |
| c620de0f-0cd7-38e0-b2e6-d8d175d42276 | -12.938 | -57.0057 | 2025-09-03 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| ba9b9ff7-30cf-33e0-8d12-252496cd8361 | -3.212 | -47.1357 | 2025-09-03 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 7d0bfd71-5227-3570-893b-7033b8d16033 | -8.3644 | -48.3116 | 2025-09-03 01:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4d87fc82-9392-3e3f-9620-890a9088ab61 | -7.7226 | -48.7355 | 2025-09-03 01:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 155.3 |
| a386ecbb-1f9f-300b-817a-fc5a66898ec2 | -4.8933 | -43.2349 | 2025-09-03 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 5d786cc2-37a6-3de6-87c2-f50733bbe796 | -7.5477 | -61.3247 | 2025-09-03 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 92ddde04-0df8-35c8-8492-4f9e427e8188 | -7.7036 | -48.7587 | 2025-09-03 01:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 67.9 |
| c8c59af4-e89f-3a05-862a-2d30dd996bc9 | -15.5652 | -48.4143 | 2025-09-03 01:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 8a85a1de-104f-3e2d-9e76-b86cb98747bf | -12.9573 | -56.9839 | 2025-09-03 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 2f83b161-a2e6-3dd9-9c5e-7b34547040c6 | -8.0608 | -45.3636 | 2025-09-03 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| db796cbd-e1cb-3e26-bb87-42a6f40dba18 | -12.9385 | -56.9655 | 2025-09-03 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 7ede2dda-754b-329b-ac2f-d8fa993afb74 | -7.5291 | -61.3444 | 2025-09-03 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e0cd56eb-3967-32ef-95ae-b4db26f3ade4 | -5.6081 | -45.0038 | 2025-09-03 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| a95bbdd4-a5da-388c-a8ce-99604d14bf27 | -14.6398 | -48.9429 | 2025-09-03 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7e205a31-dad1-3a4d-9b48-7cf8b8c9cdda | -12.9575 | -56.9638 | 2025-09-03 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 5b4b8872-26c0-3742-9463-6dcb4045844b | -3.2305 | -47.135 | 2025-09-03 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| ad913a1a-0895-34ad-b57e-b181939afc5e | -4.1604 | -46.7881 | 2025-09-03 01:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7e1bc2f0-b0e0-3b07-ae39-6b7a581c6969 | -7.5476 | -61.3437 | 2025-09-03 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 0ec07050-6b15-3a06-bc87-f70ff1dd5139 | -7.5476 | -61.3437 | 2025-09-03 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 70fa6de0-d638-33f1-909c-1246a89c229b | -7.7224 | -48.7572 | 2025-09-03 01:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 9b825d1d-a0e1-389d-9179-b9eac8fc5a5b | -11.1224 | -44.6521 | 2025-09-03 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 8100c2d3-5ce7-3db2-9e5d-a06305d2599a | -5.6081 | -45.0038 | 2025-09-03 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 62a964bc-5527-304c-8abb-1c4a635733d8 | -4.8933 | -43.2349 | 2025-09-03 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 2f78ea11-3811-3a3d-8082-de15ba27dc2b | -7.7226 | -48.7355 | 2025-09-03 01:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 209.2 |
| 93be6e99-eb78-3923-80bb-bde78399c541 | -4.9122 | -43.2103 | 2025-09-03 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| a8ccf100-24e3-3492-a285-b5af9590b955 | -9.1375 | -49.6444 | 2025-09-03 01:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 9225518d-ea53-38d9-ac43-67b86bf0f161 | -15.5656 | -48.3918 | 2025-09-03 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 1be42897-0214-3b14-ab23-c4535c520209 | -7.7036 | -48.7587 | 2025-09-03 01:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 81c52760-89a1-3fd2-9786-2d4f992e1315 | -5.6266 | -45.0252 | 2025-09-03 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 97404ff5-8623-3b8c-86ec-cc326364febf | -7.7039 | -48.7371 | 2025-09-03 01:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 107.9 |
| aa1c792d-e9cc-30e9-a1ad-6e1778c59c8c | -17.941 | -47.1718 | 2025-09-03 01:50:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2404f451-3ff6-3fe8-8281-6d5824b2ff95 | -12.844 | -48.0127 | 2025-09-03 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| d71727f3-c5eb-33ea-82e9-384416fed417 | -4.1604 | -46.7881 | 2025-09-03 01:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| d72940c5-8476-3165-aeef-fb6ea00199fa | -12.6341 | -56.9926 | 2025-09-03 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 030415e0-7c75-336d-9267-fec3fbaf675b | -4.8935 | -43.2115 | 2025-09-03 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 4a395b42-e76b-3718-8bda-a7368d4c61de | -3.2306 | -47.1131 | 2025-09-03 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 47accf5e-6abe-3733-b373-01b182ebdf32 | -7.6783 | -61.0908 | 2025-09-03 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| de153053-9b22-384e-81e0-a50928e9ad13 | -5.6079 | -45.0265 | 2025-09-03 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| fef40312-175b-37b0-94f4-36f1ef48512f | -15.5652 | -48.4143 | 2025-09-03 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| da058b5b-27fd-353c-9767-f3b0a57477d6 | -11.1228 | -44.6288 | 2025-09-03 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 6d325038-7cf7-36cd-bb10-39d598ef9ce3 | -9.3394 | -55.2277 | 2025-09-03 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 0092d471-d69e-3802-8c7e-38d3d430824a | -7.5477 | -61.3247 | 2025-09-03 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 1f23760a-c294-32a6-9fdd-4a5069fd7957 | -3.2305 | -47.135 | 2025-09-03 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 45a2c101-be42-3482-807e-eaa026fe319d | -12.8436 | -48.035 | 2025-09-03 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 0b27c01c-2478-37da-b6fa-b5b7b05ea345 | -22.7661 | -47.2743 | 2025-09-03 01:50:00 | GOES-19 | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 2d112a32-845c-3ef7-89d8-1a47cf5dfd79 | -3.212 | -47.1357 | 2025-09-03 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| ba3af964-1518-32e6-a224-af16338e3534 | -3.2305 | -47.135 | 2025-09-03 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 73b54fe6-2e17-3e4e-918a-c9ccd13ff8bc | -6.112 | -47.2017 | 2025-09-03 02:00:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 49deacc2-2973-38d5-8c90-cce0782aecf4 | -7.7226 | -48.7355 | 2025-09-03 02:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 94.4 |
| e4331602-6992-3f7c-94f0-088e528aaf14 | -7.7036 | -48.7587 | 2025-09-03 02:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 185a8d2b-485a-3362-b881-a281dacefcc6 | -11.1224 | -44.6521 | 2025-09-03 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 245f88b6-c40f-3aa7-8b13-95786400e332 | -9.3394 | -55.2277 | 2025-09-03 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 755af265-7a48-35e2-afc1-e56c10ac83a0 | -11.1228 | -44.6288 | 2025-09-03 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 09041438-443d-3fff-b79b-e8c67d2a712a | -6.1118 | -47.2237 | 2025-09-03 02:00:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 22c2b624-ab63-3fd1-9a81-44dcb90a5cdd | -7.5477 | -61.3247 | 2025-09-03 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 169bd9c7-c107-3318-8a30-17bbe1855ddb | -12.938 | -57.0057 | 2025-09-03 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 65ba85d4-7fc2-34ee-a81b-d0e52ccee5ee | -12.6341 | -56.9926 | 2025-09-03 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| f1d60c3b-d5e1-3a17-8f87-9dc541f647d3 | -7.5291 | -61.3444 | 2025-09-03 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 730d457e-bd94-3301-8447-1d07c6ee618a | -7.7224 | -48.7572 | 2025-09-03 02:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b7b549ea-5c0a-3c2e-b344-cd8dc3663701 | -3.2306 | -47.1131 | 2025-09-03 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 1ef1d4f1-48bb-3deb-8302-198f420075e9 | -12.9387 | -56.9454 | 2025-09-03 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 59244cae-e3df-3d6a-91bb-fad65db71606 | -12.8436 | -48.035 | 2025-09-03 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 10f2bc3c-b1ad-33c2-b3d6-411d9c23b8b6 | -4.8935 | -43.2115 | 2025-09-03 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 54d099f3-ac35-3551-817b-311f5c892087 | -12.844 | -48.0127 | 2025-09-03 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 88b39b7d-6f42-32ba-8c73-ecfbe608b102 | -12.9573 | -56.9839 | 2025-09-03 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f9e130a5-1b8b-335a-a20c-ae7665e6acf8 | -12.9382 | -56.9856 | 2025-09-03 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 71b33d2e-028a-384e-b259-c45c6c5937b3 | -7.5476 | -61.3437 | 2025-09-03 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a0c76c27-da41-3254-a04f-2e7aae2e82f0 | -4.1604 | -46.7881 | 2025-09-03 02:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| d61ccf37-fd19-3bd3-8586-746d985d42b7 | -3.2121 | -47.1138 | 2025-09-03 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| de1f7c34-2bcd-3f7d-bd4a-47607e9aa24f | -4.9122 | -43.2103 | 2025-09-03 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 339d3406-7dea-3d5b-b3c7-6ebcf4c8c4b5 | -7.6783 | -61.0908 | 2025-09-03 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 29016d6b-6cde-3bf8-8a87-44382b53f098 | -12.9189 | -57.0074 | 2025-09-03 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| de517ddc-53af-35c6-b3b2-cc13b6d97605 | -12.9385 | -56.9655 | 2025-09-03 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| ae8ebd7e-4c2c-327e-9cc4-056b02accb2c | -5.6079 | -45.0265 | 2025-09-03 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 05d812af-cda7-3001-a6a0-e10d1a044695 | -3.212 | -47.1357 | 2025-09-03 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| e00a3606-42bb-358d-acda-cd60a5431f13 | -7.7039 | -48.7371 | 2025-09-03 02:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8abdcf27-cfd6-3dfc-8710-70b81eb7088e | -12.9057 | -56.9683 | 2025-09-03 02:07:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dccebb3f-e311-34a3-afba-9374965c66c8 | -12.8962 | -56.9711 | 2025-09-03 02:07:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e9f58d6-3ac9-32d2-9d31-ce532adb6326 | -12.9044 | -57.000599 | 2025-09-03 02:07:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24d6e329-0f2c-3015-a69d-7afad063dc04 | -12.914 | -56.997898 | 2025-09-03 02:07:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6218d355-285b-3d48-ac39-4a721f160a8a | -5.8711 | -57.763 | 2025-09-03 02:07:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ca80451-1dfe-3c45-ab0f-b25056b05ec2 | -6.8681 | -71.5112 | 2025-09-03 02:07:00 | METOP-C | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 779f0b74-86e2-3c6c-8ba1-bd267cd3567f | -3.2305 | -47.135 | 2025-09-03 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 93df5f4c-dcca-3cef-b887-8f3bc6e1533f | -4.9122 | -43.2103 | 2025-09-03 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |


[Clique aqui para ver as próximas entradas](README19.md)
