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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51767718-4a17-3a93-a383-592ac74753e9 | -10.66187 | -49.28629 | 2026-06-06 11:53:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9e8ea1cb-1485-3241-b074-b4b0d91e6708 | -12.64364 | -45.93668 | 2026-06-06 11:53:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4cf88da7-e148-3bc3-b127-75a3b480c482 | -12.64758 | -52.12373 | 2026-06-06 11:53:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| fbd3d214-0d8b-3500-aa41-c3010e6a3bf9 | -8.51409 | -51.56237 | 2026-06-06 11:53:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8e17a377-9133-32ce-8b5c-db4afc3cde09 | -8.71504 | -47.00021 | 2026-06-06 11:53:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fca3ca16-c2e6-3627-9659-7eedb15fb352 | -14.22786 | -45.79172 | 2026-06-06 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6e8ab3d0-036f-3609-9bdc-c4800ba43831 | -18.7609 | -44.70485 | 2026-06-06 11:55:00 | TERRA_M-M | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1d5de92a-4c38-31aa-bd8e-aa6783c6b5e1 | -14.27401 | -58.44749 | 2026-06-06 11:55:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 14526eea-320f-31e0-a36a-6325c740e7b7 | -17.77077 | -50.46326 | 2026-06-06 11:55:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 5bc665d6-477a-365c-936f-e115f2ebefc8 | -15.4103 | -51.04923 | 2026-06-06 11:55:00 | TERRA_M-M | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0311b11b-2a4e-3275-9b65-18728d6b1d55 | -15.00033 | -45.4383 | 2026-06-06 11:55:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fe1d6c87-b732-35dc-a8fe-9c9fa50291de | -14.27743 | -58.45557 | 2026-06-06 11:55:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 139deaf3-52cb-336f-952c-031af4d6f2ca | -15.01007 | -45.43966 | 2026-06-06 11:55:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 913f5d16-74fb-3925-802e-0e0ac53b158f | -16.07313 | -45.89207 | 2026-06-06 11:55:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c35a9e5a-257c-3a8b-bb62-86f195c87738 | -16.62604 | -48.31365 | 2026-06-06 11:55:00 | TERRA_M-M | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2103bf69-7cd5-3f91-80b3-b3db6e2872de | -17.13195 | -47.72639 | 2026-06-06 11:55:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| baccea96-6f3f-36e8-b366-b602fd4f405e | -16.07602 | -45.89896 | 2026-06-06 11:55:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ce787c79-1d9a-359c-b0f4-1c47118f344d | -15.40866 | -51.05995 | 2026-06-06 11:55:00 | TERRA_M-M | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 50afb0da-3e89-38d5-be7a-7330908297a6 | -16.62475 | -48.32279 | 2026-06-06 11:55:00 | TERRA_M-M | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 242905aa-8e55-3019-8f6c-dfe7de5ba800 | -17.13066 | -47.73582 | 2026-06-06 11:55:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 39c9cfd9-8d35-3607-b6ad-4715d55f149d | -15.41818 | -51.0615 | 2026-06-06 11:55:00 | TERRA_M-M | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| ad22499d-1090-3752-aa41-427f7e2a5ae2 | -18.87218 | -46.37061 | 2026-06-06 11:57:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 808c8605-d13f-3781-87aa-eed32b12d420 | -21.29467 | -47.76215 | 2026-06-06 11:57:00 | TERRA_M-M | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d82841cf-ff9a-3bbd-a07e-e8867a45733f | -14.3593 | -45.5726 | 2026-06-06 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| e92a1ffb-c42e-3d7f-b0c7-30369747af1d | -14.3593 | -45.5726 | 2026-06-06 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| a2a9b90d-1bef-3cd0-886f-f2ac6cb41b15 | -14.2118 | -57.4299 | 2026-06-06 12:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 929c1c7b-094a-3d4e-a51c-a320b6a4b3f9 | -14.2118 | -57.4299 | 2026-06-06 12:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| fe2bd367-7bde-3e34-b5d3-e9c281fe70da | -14.3593 | -45.5726 | 2026-06-06 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| a391c83f-0a54-3535-86c7-91a3c621a92d | -5.7939 | -45.1267 | 2026-06-06 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 893f7400-f527-35b0-a6c0-8f682fc63517 | -14.1926 | -57.4318 | 2026-06-06 12:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d00e33f4-ec7a-3101-a07f-9f28eca98126 | -14.3788 | -45.5692 | 2026-06-06 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 066bbc19-2733-3f16-bfe3-c8977b7ffbac | -14.2118 | -57.4299 | 2026-06-06 12:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 51825b8b-cacb-3038-8ee2-da6400bae3e3 | -14.3593 | -45.5726 | 2026-06-06 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 02731c73-1ae1-39d9-b7a4-5c589e9dd8e7 | -14.3593 | -45.5726 | 2026-06-06 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| b06635b3-3f42-3422-a4c6-da6d7168a6b9 | -14.2118 | -57.4299 | 2026-06-06 12:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 162.1 |
| edc3c923-24d8-343c-bc62-77aa91117b71 | -8.9427 | -45.68 | 2026-06-06 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9bf5c089-3747-3da3-91de-539aec2b5fcd | -14.6368 | -58.6933 | 2026-06-06 12:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| fb5ff91b-2f19-36e3-8488-0dd1e88863df | -5.8126 | -45.1253 | 2026-06-06 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 403f59fb-f421-3f1b-9d25-8f5ff149d3a0 | -14.1926 | -57.4318 | 2026-06-06 12:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 4630c366-2de5-328a-a7fe-5f0ee2cb6506 | -8.9241 | -45.6594 | 2026-06-06 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| c4ed9119-f8f0-35fd-b237-060e538b8418 | -14.2118 | -57.4299 | 2026-06-06 12:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 170.5 |
| 1a8b5674-90da-335d-88d6-772d99b42e5e | -9.4259 | -50.683 | 2026-06-06 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c3c5495f-107b-39c8-b23f-4fb14a4f848e | -8.9433 | -45.6346 | 2026-06-06 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 9820ba3a-2ba4-3e80-a986-5bd6f8510176 | -9.9007 | -47.4767 | 2026-06-06 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| fbc76917-c17c-3bdb-b286-6c1e000c4d83 | -14.3593 | -45.5726 | 2026-06-06 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 79f966cc-9fd0-3582-a7d0-317cfb9a1ade | -14.3593 | -45.5726 | 2026-06-06 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| c0c0812f-2f0e-3485-a8d2-3cbc6f11e608 | -8.9241 | -45.6594 | 2026-06-06 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 4c8a8b8e-d7a5-3b21-8163-b434c0824217 | -8.9433 | -45.6346 | 2026-06-06 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 64aafd29-4546-3cf5-bc55-92430e428560 | -14.2118 | -57.4299 | 2026-06-06 13:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 238.0 |
| 93a5251a-0526-3f4e-aae8-bad798f85bdf | -9.9007 | -47.4767 | 2026-06-06 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| d295910b-e9e2-30d6-9ae7-cf686740cd9b | -14.2121 | -57.4098 | 2026-06-06 13:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 1e3c9c03-6c81-3a8d-9567-f76ff3e93260 | -14.2118 | -57.4299 | 2026-06-06 13:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 230.4 |
| bbf85719-8587-3b3a-b51a-3e31937399ae | -14.6368 | -58.6933 | 2026-06-06 13:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 6bdb7b88-ed52-3dd0-9edc-9cb35b1837bd | -5.8126 | -45.1253 | 2026-06-06 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 329.6 |
| 913022cc-a027-3f19-a55d-9560ac6e1413 | -8.9433 | -45.6346 | 2026-06-06 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 3b0fd094-da0d-3e9d-aa3c-b9e5281c093d | -8.9241 | -45.6594 | 2026-06-06 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 0ef61990-ffa7-31f1-b61e-bc42704ef54f | -5.7939 | -45.1267 | 2026-06-06 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 91e49efb-d733-34db-a6b4-e9d48ce2df5c | -14.2116 | -57.4501 | 2026-06-06 13:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5d017129-0c25-395f-859b-74931afc2282 | -14.3593 | -45.5726 | 2026-06-06 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| bdcb95da-a519-313c-b94d-2db34315ad77 | -14.1926 | -57.4318 | 2026-06-06 13:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 6303cf1e-986b-37d1-b9b0-4f9b4a7b281d | -8.9241 | -45.6594 | 2026-06-06 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4ac5cf15-a8a9-3b89-be9c-a2fc83805106 | -14.6368 | -58.6933 | 2026-06-06 13:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 9686abfd-7303-3215-833b-4755a95cee14 | -14.2118 | -57.4299 | 2026-06-06 13:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 186.5 |
| f1e138ea-162f-3392-bcc2-ef0f3e4eabda | -8.9427 | -45.68 | 2026-06-06 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| fdb25e00-1d9e-3856-b577-7294b23c5f34 | -8.9433 | -45.6346 | 2026-06-06 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 7ea8e959-f311-3b67-99d5-0d4bd3604b4b | -14.6368 | -58.6933 | 2026-06-06 13:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| da3bf561-fee8-3ba1-b50c-f9207d0212ec | -8.9433 | -45.6346 | 2026-06-06 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 29cd8d8b-87a3-3108-b4dd-46b6443c6dc5 | -8.9427 | -45.68 | 2026-06-06 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| e82e9278-b0f9-3a5a-b994-34c94938dc0e | -8.9241 | -45.6594 | 2026-06-06 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 19b88500-0d32-30e1-81e1-d3601dbb6244 | -14.2118 | -57.4299 | 2026-06-06 13:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 263.2 |
| 1cdc7f75-afc7-3a92-89c9-5658170ab242 | -14.3593 | -45.5726 | 2026-06-06 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| cd93b5c3-4ac0-303c-81b0-e4075091d7de | -14.2118 | -57.4299 | 2026-06-06 13:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 242.2 |
| 89916431-79dd-3f18-af29-adf2b0c7db9e | -14.2121 | -57.4098 | 2026-06-06 13:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 4fc54ec8-df3e-37bc-9ec1-eb215091c46e | -10.8573 | -53.7425 | 2026-06-06 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 45849522-b2d5-3c0a-9a78-0d033b88032f | -12.0747 | -45.9862 | 2026-06-06 13:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| ca6f29db-1698-342d-aeb1-9924cae1b016 | -14.1926 | -57.4318 | 2026-06-06 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| cac9ced3-32b5-38db-b438-a1424be75387 | -14.6368 | -58.6933 | 2026-06-06 13:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 2b981d6a-b486-39b4-bfdd-104b3745b293 | -14.2118 | -57.4299 | 2026-06-06 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 205.2 |
| 39936742-36e8-3f1a-9031-36aecfa6d505 | -9.4259 | -50.683 | 2026-06-06 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 77b79b59-2c91-3fde-b89e-43ff1d0c0813 | -8.9427 | -45.68 | 2026-06-06 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 075c89be-456f-3b1c-a688-80a3ab8c76f8 | -10.8573 | -53.7425 | 2026-06-06 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 3c3d7850-caca-30e0-be2b-ed73e9ef428d | -14.2121 | -57.4098 | 2026-06-06 14:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 11036379-67b2-3e89-9683-3b9012beeb80 | -8.9433 | -45.6346 | 2026-06-06 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 24686561-5e4f-33dd-bf19-ed32c3cf4b5b | -14.2118 | -57.4299 | 2026-06-06 14:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 209.3 |
| 5bf3ccab-7815-35ce-96a2-99c63dedbdba | -14.6368 | -58.6933 | 2026-06-06 14:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| dc11baca-b01a-3e6a-b74f-c38c0195dfaf | -8.9241 | -45.6594 | 2026-06-06 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| dd7907be-db94-38d0-ac1e-2ade86525186 | -8.9433 | -45.6346 | 2026-06-06 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 87b76fbd-94ad-3474-84a6-5470a317c221 | -12.0747 | -45.9862 | 2026-06-06 14:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d5ff37eb-a038-344d-a781-85c306f34e9b | -14.6368 | -58.6933 | 2026-06-06 14:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| caa6f16b-5ee5-3fd5-943c-efa054a9049c | -8.9241 | -45.6594 | 2026-06-06 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 9da57a1f-d4e7-3afd-ac85-b47e2ca15f27 | -10.8573 | -53.7425 | 2026-06-06 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 36c08123-5a07-3f1b-9d73-f32a6192b8da | -14.2118 | -57.4299 | 2026-06-06 14:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 8f3c5e2b-2699-38df-8ce3-7c1ec0c3a11b | -8.9427 | -45.68 | 2026-06-06 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 4ae63cb2-2e71-3b9a-ab23-a80cf382f620 | -14.1926 | -57.4318 | 2026-06-06 14:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 18e96bec-f5b5-3ac5-b334-d7a9584a42f9 | -11.7323 | -54.7885 | 2026-06-06 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 175f35f2-5fb5-3f6f-a3e8-8b2f88796fdc | -8.9427 | -45.68 | 2026-06-06 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| bb927d02-0b55-3529-ae91-08615c20f583 | -10.8573 | -53.7425 | 2026-06-06 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| d7cd2611-4d02-3ae2-b903-b28efdaa1b29 | -14.2118 | -57.4299 | 2026-06-06 14:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 3b7daa6f-0718-3924-b74a-100aa0fa96f4 | -14.1926 | -57.4318 | 2026-06-06 14:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1fa81d47-d4b3-33b0-a0be-402b2206727e | -8.9433 | -45.6346 | 2026-06-06 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.0 |


[Clique aqui para ver as próximas entradas](README15.md)
