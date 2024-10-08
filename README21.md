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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eee01dc-245a-3424-a0de-312f4f048c13 | -18.6195 | -57.2396 | 2024-10-08 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.1 |
| f5a71a02-71b3-33d1-9946-366f2c08d4f1 | -18.6394 | -57.237 | 2024-10-08 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.0 |
| dc60cfda-1a81-36f0-8fd4-8c2e7e6242f3 | -20.393 | -43.966 | 2024-10-08 01:16:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.7 |
| 15ed2a66-78d2-36d4-9532-93c4e68caa6a | -20.3732 | -43.9468 | 2024-10-08 01:16:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 169.9 |
| b3a7ac39-0d90-332a-95f1-242c93ceefcd | -20.3938 | -43.9412 | 2024-10-08 01:16:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 239.1 |
| 5b24caaa-d672-3932-baa6-0ad9927bc10b | -20.3946 | -43.9163 | 2024-10-08 01:16:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.4 |
| 21143757-c149-3ada-b20e-e72cf5fbcec8 | -20.4144 | -43.9356 | 2024-10-08 01:16:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.8 |
| cabdc132-754a-372e-8b39-df750a1d33c5 | -20.4251 | -47.6688 | 2024-10-08 01:16:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 108.1 |
| b2a0656d-ecb6-388c-a24a-3404843b6833 | -20.4258 | -47.6453 | 2024-10-08 01:16:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 106.6 |
| a87c4b39-8130-3cb9-8d95-a197ca0f0e07 | -21.0712 | -47.2331 | 2024-10-08 01:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 72.1 |
| dbd01665-8b2a-33c9-a508-61ab65c3e245 | -21.0719 | -47.2094 | 2024-10-08 01:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 60.0 |
| a6a5e5fe-4b43-3bd1-acde-f823bb2d9256 | -2.7985 | -48.5801 | 2024-10-08 01:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 858ce6c9-9699-3435-9506-36d3aa536d89 | -5.5716 | -44.8927 | 2024-10-08 01:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 8d7abd03-8762-37d2-8842-ec154fd2804d | -5.5718 | -44.87 | 2024-10-08 01:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 863f172a-0ed7-38ef-9e22-cdf28dc35ec9 | -9.3901 | -66.5444 | 2024-10-08 01:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| bb28e49a-6c04-33e5-b9db-1b8356b11326 | -9.4086 | -66.5624 | 2024-10-08 01:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 519c4fec-d845-3a5d-a3c8-d8bf35aa3cda | -9.4087 | -66.5438 | 2024-10-08 01:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 41660d63-4baf-34f9-b94c-e4f534b5f651 | -9.445 | -66.7289 | 2024-10-08 01:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| fe8bd700-d579-3184-8836-9ddb7185ce3d | -9.4635 | -66.7283 | 2024-10-08 01:26:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 564f8ab6-eb64-3295-a8d1-93bf1c0e8230 | -9.572 | -67.4315 | 2024-10-08 01:26:01 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 94e2b3fb-1fdd-3744-b34a-7973468028dc | -10.8754 | -63.9169 | 2024-10-08 01:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 94.4 |
| fd7985b3-479d-3c6f-9f09-c81371f82a11 | -10.8755 | -63.8979 | 2024-10-08 01:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 28110fef-670b-379a-9b6f-d0ab99dbece2 | -11.2091 | -51.3746 | 2024-10-08 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 0946f44c-fa45-334a-ac4e-3bb87ec73945 | -11.2289 | -51.3091 | 2024-10-08 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 22e14aef-82ce-3445-8db2-659281475e74 | -11.2292 | -51.2879 | 2024-10-08 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 290.1 |
| fa302e6e-950a-31a8-9489-4a8120618449 | -11.2295 | -51.2667 | 2024-10-08 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 42fd42da-7fc3-3452-92d5-9ad6d23f9545 | -11.2479 | -51.3071 | 2024-10-08 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| e7e24802-730e-3b5a-9cc9-61f5313be9b1 | -11.2482 | -51.2859 | 2024-10-08 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 316.1 |
| d7b13f6d-94dc-3a86-8c62-c38b66721b21 | -11.2485 | -51.2647 | 2024-10-08 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 9565b177-c84b-3eb3-9fb5-854a881c8d76 | -11.5233 | -65.137 | 2024-10-08 01:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 0bcf0c80-75e6-334b-8d1f-6a10fd643099 | -11.5421 | -65.1362 | 2024-10-08 01:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 67fa4bf3-db8f-3475-bc02-08ae9ae2a922 | -11.6806 | -64.0312 | 2024-10-08 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 3a832ad6-b8f0-331e-95e3-180e5395bc82 | -11.6808 | -64.0121 | 2024-10-08 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8618f060-f35b-3d79-bb0c-5df73cb8d8e3 | -12.3616 | -47.0986 | 2024-10-08 01:26:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| bd957ff6-09fb-34a4-ac15-ed866050064c | -12.4414 | -63.018 | 2024-10-08 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 1ca174d1-3440-3554-ac52-deb5697d62e8 | -12.4416 | -62.9988 | 2024-10-08 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 0370f5f3-ec31-3eb0-bab9-82113f52d12e | -16.5267 | -57.7365 | 2024-10-08 01:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.8 |
| 86e8db71-106d-33b4-aeaa-a8c0de9d6fab | -16.5462 | -57.7344 | 2024-10-08 01:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 0797526f-cec9-3efe-b25d-a8bd82a7035f | -16.992 | -56.721 | 2024-10-08 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.2 |
| 3cdceb2c-03fd-3e3c-9e10-50720ea39bbb | -16.9924 | -56.7003 | 2024-10-08 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.7 |
| 1b815abc-06cd-3c81-9b93-1435dc59efd8 | -16.9927 | -56.6797 | 2024-10-08 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.3 |
| e08a16d1-71d5-322d-909e-f68382f4551a | -17.0123 | -56.6773 | 2024-10-08 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 2f2162a2-9772-3e5d-aefe-84e555a4ffb3 | -18.6192 | -57.2603 | 2024-10-08 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| afa221a5-449d-3442-9aae-722b67c546e4 | -18.6195 | -57.2396 | 2024-10-08 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.2 |
| 3285c3d6-f83c-32c6-913f-e31256ff1c71 | -18.6394 | -57.237 | 2024-10-08 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.1 |
| fe0fa3d7-592a-3261-8a52-b40a31c21c23 | -18.7183 | -57.2682 | 2024-10-08 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 407ab7b4-95eb-3d5a-ab24-9207128d86b0 | -20.3732 | -43.9468 | 2024-10-08 01:26:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 190.0 |
| bb956cd2-6952-3a97-811e-8125af7a53a1 | -20.374 | -43.922 | 2024-10-08 01:26:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| f6c256f6-8c1b-33dc-b3bb-3f7de6bfae59 | -20.3938 | -43.9412 | 2024-10-08 01:26:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 281.9 |
| 931a8551-df84-3ec8-a1be-6dfaff0086bd | -20.3946 | -43.9163 | 2024-10-08 01:26:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.7 |
| c18cc3ae-492f-3144-8213-471a19e8edf1 | -20.4144 | -43.9356 | 2024-10-08 01:26:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.1 |
| e56ca5b4-7368-350c-90db-47917a587102 | -20.4258 | -47.6453 | 2024-10-08 01:26:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7ed57a81-fb58-3da4-b2c0-5623d5b5bb56 | -21.0712 | -47.2331 | 2024-10-08 01:27:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 1325a288-4538-31c2-91c2-4e2aa7ec0a8d | -22.6506 | -42.1051 | 2024-10-08 01:27:09 | GOES-16 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 88abc15a-38b0-3269-887c-86571e3d0e96 | -2.7985 | -48.5801 | 2024-10-08 01:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 51f335f7-2e1f-3884-8e83-9c187cba70f4 | -5.5716 | -44.8927 | 2024-10-08 01:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 827961f0-6cb5-3473-8a84-caea58d4fb17 | -5.5718 | -44.87 | 2024-10-08 01:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 08cf0afc-7890-3856-8b31-7ba8e897084f | -9.3901 | -66.5444 | 2024-10-08 01:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2da0a0db-49dd-3c86-be98-ffe284561c68 | -9.4086 | -66.5624 | 2024-10-08 01:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c8e66f8e-7013-3a23-a72c-a772d7226dde | -9.4087 | -66.5438 | 2024-10-08 01:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| c6ba61c3-eaf6-326b-9679-3b1562baeb54 | -9.445 | -66.7289 | 2024-10-08 01:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0ebfe34a-6569-3bf2-b242-a98b9d609326 | -9.4635 | -66.7283 | 2024-10-08 01:36:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 178e3025-37ab-3990-af17-5b4e337849d0 | -10.1261 | -55.2093 | 2024-10-08 01:36:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| e87287c2-45cc-300b-844b-94daaaa4762a | -10.1263 | -55.1891 | 2024-10-08 01:36:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 0ceb8426-a19f-37b5-b6e5-a9bfbe9b884e | -10.1448 | -55.2078 | 2024-10-08 01:36:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 23f0644e-c246-3944-be1a-f08a4ae42dc2 | -10.1451 | -55.1876 | 2024-10-08 01:36:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 8c5ae56c-7bf6-364a-bb78-510b47cdd3a2 | -10.6256 | -55.9154 | 2024-10-08 01:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0680d354-12cb-39a9-b3e9-e8537630e5cc | -10.8754 | -63.9169 | 2024-10-08 01:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.3 |
| a09e3474-f930-3cb4-83ee-83d3aeda73d6 | -10.8755 | -63.8979 | 2024-10-08 01:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.7 |
| f58b6048-18b0-3fbf-8ee8-96af2d346631 | -11.2289 | -51.3091 | 2024-10-08 01:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 8ea2d459-73a0-3980-b032-05993d3f7c43 | -11.2292 | -51.2879 | 2024-10-08 01:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 0e56b81e-56a6-3a7b-8870-b3ea4d408cc8 | -11.2295 | -51.2667 | 2024-10-08 01:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 204e209e-90b3-34a4-ad90-0c4d2409ac88 | -11.2479 | -51.3071 | 2024-10-08 01:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f8bbd8a2-ac94-3a74-b62a-bff6b8cb6c36 | -11.2482 | -51.2859 | 2024-10-08 01:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 431ddf0d-4230-34a6-a4b2-d91c4647143b | -11.2485 | -51.2647 | 2024-10-08 01:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 2a75bedb-7575-3a63-9824-c0da4dd0a71b | -11.5233 | -65.137 | 2024-10-08 01:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.7 |
| c04f9748-82b1-38f5-9b78-fa88efc62446 | -11.6806 | -64.0312 | 2024-10-08 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5b36aa20-0826-3051-9a89-34b4261398a6 | -11.6808 | -64.0121 | 2024-10-08 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b270f04a-0b6c-3440-9f05-31f26b37987b | -12.4414 | -63.018 | 2024-10-08 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 03271c69-4e25-3677-8a1f-df30a40fa299 | -16.5897 | -46.4979 | 2024-10-08 01:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 88ed82e3-bd85-3e37-82aa-9b9de5915710 | -16.5267 | -57.7365 | 2024-10-08 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 8487da30-1712-3400-ba01-e5d99f70bb9a | -16.5462 | -57.7344 | 2024-10-08 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 2acba216-eea3-393d-9f72-a2462e762565 | -16.5466 | -57.714 | 2024-10-08 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.7 |
| 825098de-7055-39fc-a408-e21a08d4340f | -16.9211 | -57.4881 | 2024-10-08 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.3 |
| b277d883-9e92-3937-9fc8-3375690f0d34 | -16.9924 | -56.7003 | 2024-10-08 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.3 |
| dc22aa94-ab30-37d5-b87f-05e9564c108c | -16.9927 | -56.6797 | 2024-10-08 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.8 |
| 20079b09-dcf3-381c-8e46-5e605b177eca | -17.0123 | -56.6773 | 2024-10-08 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 97e00b24-4719-377a-928c-4e9b4bf287d3 | -18.6192 | -57.2603 | 2024-10-08 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.1 |
| c808d335-808c-36fe-b144-844591fb4776 | -18.6195 | -57.2396 | 2024-10-08 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.6 |
| 349ff14e-f5f2-387f-9c23-0f53432d6262 | -18.6394 | -57.237 | 2024-10-08 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| f6050027-40fe-3f39-a72e-71b1c04ae6c8 | -18.6398 | -57.2163 | 2024-10-08 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.7 |
| 99f9a66c-3343-34ff-8b9e-bc2b98ad3f74 | -20.4251 | -47.6688 | 2024-10-08 01:36:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 97.9 |
| bf7ec3b8-b5e0-3f1f-9a69-39dcdec94745 | -20.4258 | -47.6453 | 2024-10-08 01:36:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 8c3e3393-5260-3cfc-96cc-4b9ac38aa048 | -24.24 | -54.2481 | 2024-10-08 01:42:44 | METOP-B | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| adcc462d-d713-39f9-bab5-97f224c97a8c | -24.2304 | -54.251301 | 2024-10-08 01:42:44 | METOP-B | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7755edbd-22e9-3c2d-bc85-7b6ee83ea9ab | -23.886299 | -54.2155 | 2024-10-08 01:42:49 | METOP-B | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 459ce323-088b-3851-a9b7-ef8a2b8b2162 | -23.891001 | -54.232601 | 2024-10-08 01:42:49 | METOP-B | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf52f571-5a32-3f6a-bb9a-6edece5c47d2 | -23.2313 | -55.4627 | 2024-10-08 01:43:05 | METOP-B | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b527412-f2d7-379c-b4a3-31fac8eb980e | -23.221701 | -55.465698 | 2024-10-08 01:43:05 | METOP-B | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c5edf56-0f2f-3df8-a7ee-e415cc50e616 | -21.3769 | -55.660301 | 2024-10-08 01:43:36 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README22.md)
