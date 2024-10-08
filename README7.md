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
| 03cff040-a7ce-39e6-aa5f-e55071e1b393 | -9.4087 | -66.5438 | 2024-10-08 00:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 75eebc95-45f0-35de-aa6b-6d566cfe76b1 | -9.445 | -66.7289 | 2024-10-08 00:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c8740154-b9b9-31eb-9c2b-8cb8f07bc7e9 | -9.4635 | -66.7283 | 2024-10-08 00:16:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0f76beb1-e6c1-32a5-a66d-da4014223155 | -9.572 | -67.4315 | 2024-10-08 00:16:01 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 39436f9a-96e2-3500-9eff-e253b7edfc28 | -9.7241 | -66.5716 | 2024-10-08 00:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b2a39ef8-47d3-324b-a1bf-9ce431c4ac0d | -10.1263 | -55.1891 | 2024-10-08 00:16:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 9e863ecf-71ac-3a21-bea6-b8eb6b859b6e | -10.1451 | -55.1876 | 2024-10-08 00:16:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 76f761ac-c22a-315e-9392-6c0c1321a5c7 | -10.8754 | -63.9169 | 2024-10-08 00:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 31868cff-27c0-3f2f-9e21-ab8c8a9a03a1 | -10.8755 | -63.8979 | 2024-10-08 00:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ff7844da-044f-3944-b9f5-e318071fa38a | -10.8942 | -63.8971 | 2024-10-08 00:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ec1608ea-c463-3208-bdb6-31c1c8b8201c | -11.0991 | -54.0285 | 2024-10-08 00:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| e532c443-1300-3240-b62a-805ca43c945a | -11.0994 | -54.008 | 2024-10-08 00:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 7e04b6ef-f72b-3114-9332-2abd1f9f0372 | -11.118 | -54.0268 | 2024-10-08 00:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| bb3c159a-f4ce-3830-8c55-f5e42a6d195c | -11.1183 | -54.0062 | 2024-10-08 00:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 210.3 |
| f27a8fe3-b3be-37b2-931c-00b1be4ecbcf | -11.1185 | -53.9857 | 2024-10-08 00:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 04e9344c-b964-39e4-85e1-373d2c271d1d | -11.1372 | -54.0045 | 2024-10-08 00:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 2599e748-576e-3829-aaca-d9508933da45 | -11.5233 | -65.137 | 2024-10-08 00:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d150a7ce-f495-3f5b-bae4-2ee39c2ed760 | -12.3616 | -47.0986 | 2024-10-08 00:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| a9577219-2ecf-3ca3-a5d7-3177708b5451 | -12.362 | -47.0761 | 2024-10-08 00:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 4e4d9eb2-c52d-3450-b4c2-2476125dbbab | -12.1913 | -63.6628 | 2024-10-08 00:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1c3383bb-a868-36a5-b38f-549ecbe10e96 | -12.4414 | -63.018 | 2024-10-08 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.7 |
| a247aa4b-cd2b-300f-aedd-9df32921a60f | -12.8242 | -62.4573 | 2024-10-08 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 762260ca-8eb7-3b32-919f-4dc68c1aa190 | -15.5996 | -57.3699 | 2024-10-08 00:16:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 2a2b4994-8b98-38f2-8386-cfcc5ada2670 | -15.619 | -57.3678 | 2024-10-08 00:16:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| d39e4222-8c93-32e4-90ad-18034a38e1c2 | -16.0951 | -50.1883 | 2024-10-08 00:16:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| e70aedbe-e8a6-3da4-be39-eb206288b504 | -16.4353 | -57.3393 | 2024-10-08 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.9 |
| 599d82aa-80d9-366a-9e7c-ec6ef630f2d2 | -16.5267 | -57.7365 | 2024-10-08 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.1 |
| 73172584-4ce2-39ff-abad-2410ecb778b9 | -16.527 | -57.7161 | 2024-10-08 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.0 |
| 63f2ec05-a809-3921-97da-de17e3fc89a8 | -16.5462 | -57.7344 | 2024-10-08 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| bc8b64f3-5aef-3eed-b129-ff14bea0d60f | -16.5466 | -57.714 | 2024-10-08 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 19c06505-6ce1-3b18-8c36-6ae9111c8983 | -16.992 | -56.721 | 2024-10-08 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 8c9a0960-a270-3d1f-ada6-32c50df1fa2f | -16.9924 | -56.7003 | 2024-10-08 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 3ba47c0f-4844-3e6d-b08d-d5c2c8a12062 | -16.9927 | -56.6797 | 2024-10-08 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.2 |
| cd230971-2e78-3db4-9877-33957f476b54 | -17.012 | -56.698 | 2024-10-08 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.5 |
| cb980a37-fdc3-380f-b9d4-c0931dd47513 | -17.0123 | -56.6773 | 2024-10-08 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.7 |
| 2afeb5b6-b958-3be8-9f7f-aa5ee2261020 | -17.0127 | -56.6567 | 2024-10-08 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.6 |
| d1e361e2-086d-3bae-b131-52f8d84a4829 | -17.1274 | -56.828 | 2024-10-08 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.4 |
| 755c0a1c-b7f0-3a19-a791-04ccb6ba4f9b | -17.1588 | -56.1222 | 2024-10-08 00:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 35.4 |
| 47e754d3-dd60-39e1-92cb-be00eb4e0abc | -17.3353 | -55.0156 | 2024-10-08 00:16:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 8dd06408-7342-3c51-970a-a175f1c3b848 | -18.6192 | -57.2603 | 2024-10-08 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 7faf1a56-6432-3537-96ca-3470fbbaf425 | -18.6195 | -57.2396 | 2024-10-08 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 0efc3f82-f337-39a3-bdcd-851ab5bd3429 | -18.6394 | -57.237 | 2024-10-08 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.6 |
| 9420075c-9810-3b8f-906a-005eb4457984 | -18.7183 | -57.2682 | 2024-10-08 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.0 |
| aaeb1e93-c59f-3ae5-a52f-8419102e5648 | -18.7187 | -57.2475 | 2024-10-08 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 36d1e91d-18ae-3b3e-924e-0d9e19b801ef | -20.3732 | -43.9468 | 2024-10-08 00:16:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 210.9 |
| 900279c8-96fe-3566-b44d-c2a364cad0f3 | -20.374 | -43.922 | 2024-10-08 00:16:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.7 |
| 99fd9cfa-0a9b-368d-9dda-a5c9f065ff59 | -20.3938 | -43.9412 | 2024-10-08 00:16:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 272.7 |
| f3b45c1f-244a-32df-a8b9-067df192350d | -20.3946 | -43.9163 | 2024-10-08 00:16:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 164.1 |
| 72e11518-772d-304f-89e5-4f8c81e584c7 | -20.4144 | -43.9356 | 2024-10-08 00:16:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.4 |
| 19b845a2-5f39-3e9c-9cfd-7bd887978ad2 | -20.4152 | -43.9107 | 2024-10-08 00:16:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| 72deebc6-5b92-322b-a640-24384371f34d | -20.4251 | -47.6688 | 2024-10-08 00:16:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 111.2 |
| cf4513ab-0ca2-35ad-94ae-6e62adfa553b | -20.4258 | -47.6453 | 2024-10-08 00:16:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 6ce78daa-8985-3b3b-be40-2424923817a6 | -20.4264 | -47.6218 | 2024-10-08 00:16:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a0e7ea59-4af6-3583-90c2-cb146ae21120 | -20.4463 | -47.6405 | 2024-10-08 00:16:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 7c08df0f-0e4c-3595-be5a-6e54dac26004 | -21.0712 | -47.2331 | 2024-10-08 00:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 852b83c0-e9a9-36c9-ada9-8245c9281db0 | -21.0719 | -47.2094 | 2024-10-08 00:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 52221d79-5722-38a4-b45d-e82d4a787c81 | -22.8035 | -46.7612 | 2024-10-08 00:17:11 | GOES-16 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.6 |
| 786dbec0-5b90-395d-b6c6-7c32deba7778 | -2.7985 | -48.5801 | 2024-10-08 00:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 70697328-62f2-39bb-bc5e-3e4c9c62f656 | -2.7986 | -48.5586 | 2024-10-08 00:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 1c492fed-cabd-3b7e-9d03-ca8ab5bede6f | -2.9797 | -49.5342 | 2024-10-08 00:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| fa5fab4d-f6db-37fa-a874-eb0026103398 | -3.2862 | -47.133 | 2024-10-08 00:25:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| af4fc9d8-8920-3899-b87b-49030f4af05b | -3.2863 | -47.1111 | 2024-10-08 00:25:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| ab35146f-ace4-3819-83b6-5737ac306b3c | -4.4468 | -42.9123 | 2024-10-08 00:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| d3a9b4d9-fc4a-3e79-bbe0-93c711cf9f36 | -4.447 | -42.8889 | 2024-10-08 00:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 2a613ea9-ea1a-376f-8ac3-3b45723a9400 | -5.5716 | -44.8927 | 2024-10-08 00:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e2a06cea-3db0-3659-b473-695760795987 | -5.5718 | -44.87 | 2024-10-08 00:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 79b9e1ef-64c8-38d8-a8f5-b58812eba456 | -5.8216 | -44.1196 | 2024-10-08 00:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 9f4ed600-5343-3897-b194-366266ee8257 | -5.9225 | -45.3888 | 2024-10-08 00:25:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| b57ce888-fcfc-3673-ac9e-996cef477d82 | -6.4213 | -38.8347 | 2024-10-08 00:25:42 | GOES-16 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 2d9872fe-1bf5-31a8-89e8-4d9878712a99 | -7.0104 | -47.0244 | 2024-10-08 00:25:46 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| a16bd70f-1873-3e0c-a572-ad14c0610253 | -7.0106 | -47.0023 | 2024-10-08 00:25:46 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 2399cf06-af0c-342d-b323-7427e05515c7 | -9.4087 | -66.5438 | 2024-10-08 00:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a86198b8-d439-32a2-a570-c0c243e17bb7 | -9.445 | -66.7289 | 2024-10-08 00:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 95768488-8458-3bca-b396-81cb6160fac0 | -9.4635 | -66.7283 | 2024-10-08 00:26:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| a8be862c-f1a9-359f-ae54-145f3a1ab847 | -9.572 | -67.4315 | 2024-10-08 00:26:01 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e8b61cb7-9b93-33fc-802a-126d29e33a66 | -9.7241 | -66.5716 | 2024-10-08 00:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 84d73f3c-06eb-353f-ab6c-34f27b5e3b3f | -10.1974 | -36.4278 | 2024-10-08 00:26:03 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| 27a571ab-eb90-3e3c-b312-0cef77240ec0 | -10.1261 | -55.2093 | 2024-10-08 00:26:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 72e76c47-2973-3d03-be34-a731b22197f0 | -10.1263 | -55.1891 | 2024-10-08 00:26:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| e0bfd832-4448-3fb5-a909-683dee4908ec | -10.1448 | -55.2078 | 2024-10-08 00:26:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 7bc8a20e-50fe-31bf-8562-3d83ce5fad19 | -10.1451 | -55.1876 | 2024-10-08 00:26:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| d11e8608-7251-34ea-aad3-7f60888b7b3d | -10.8568 | -63.8988 | 2024-10-08 00:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| e750eb61-ed8c-34f7-b3f8-8518ccc4ae14 | -10.8754 | -63.9169 | 2024-10-08 00:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 96.0 |
| e89f2ffc-8be6-3cbf-8094-6486486b53a6 | -10.8755 | -63.8979 | 2024-10-08 00:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 29bd897f-e6a2-34e3-a61e-8d8188d10025 | -11.0991 | -54.0285 | 2024-10-08 00:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 490b1f4e-fd0d-31e5-bb0b-532d198cfff3 | -11.0994 | -54.008 | 2024-10-08 00:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 263c42b6-f86b-337d-aa9a-b875ddd4081a | -11.118 | -54.0268 | 2024-10-08 00:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 24070ddb-67df-3d9e-b726-1f1d7c1d0742 | -11.1183 | -54.0062 | 2024-10-08 00:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| d7bd9910-8ff5-3fa9-8413-9e923d9e7f63 | -11.5233 | -65.137 | 2024-10-08 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6430c8c4-5513-34c5-bf93-6984f064763f | -12.1911 | -63.6819 | 2024-10-08 00:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 416a8618-c759-3739-9596-68662a9d8088 | -12.1913 | -63.6628 | 2024-10-08 00:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 0aa1fb68-0f01-30a8-ab4f-40dfa3f27706 | -12.2101 | -63.6618 | 2024-10-08 00:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 8169af4f-a8e8-3863-883d-939cdfea9b63 | -12.4414 | -63.018 | 2024-10-08 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 3c2d16d8-235c-31f9-8c94-ed6e6de71043 | -15.619 | -57.3678 | 2024-10-08 00:26:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 9724bb91-c507-3d88-bee4-b17b0b26f0de | -16.4353 | -57.3393 | 2024-10-08 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.2 |
| e301385e-c026-3836-854c-7990f3bbff5d | -16.5267 | -57.7365 | 2024-10-08 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.4 |
| 5cfbd953-d6b5-3bea-92f6-cd9a720bcf52 | -16.5462 | -57.7344 | 2024-10-08 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.6 |
| a4c8727b-6967-3a6f-8ce6-54588804454b | -16.5466 | -57.714 | 2024-10-08 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.5 |
| a5bba4d0-107d-3dbb-a066-f7bc29c1f949 | -17.4789 | -40.0493 | 2024-10-08 00:26:42 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| 32bf0104-7e81-32b3-8f92-a5153d331c97 | -16.992 | -56.721 | 2024-10-08 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |


[Clique aqui para ver as próximas entradas](README8.md)
