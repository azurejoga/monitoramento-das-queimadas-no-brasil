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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 178aacc7-a146-36ce-a79d-b37d7201461f | -26.72909 | -52.52593 | 2024-10-30 12:59:00 | TERRA_M-T | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 8348b5f1-d412-34f2-bfb7-de0274d4023d | -26.72769 | -52.53663 | 2024-10-30 12:59:00 | TERRA_M-T | ENTRE RIOS | SANTA CATARINA | Brasil | 4205175 | 42 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 31eb2304-ab81-36b8-8707-2a5607623b4b | -25.37252 | -52.56539 | 2024-10-30 12:59:00 | TERRA_M-T | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| abf118b6-cba1-3f87-9f52-764f36102800 | -23.99048 | -54.10711 | 2024-10-30 12:59:00 | TERRA_M-T | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 65.5 |
| 191438cf-3909-38bc-b48b-74c9c286c573 | -23.75736 | -54.50136 | 2024-10-30 12:59:00 | TERRA_M-T | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 14cf85e5-5f20-37c1-8aa2-41bb247adb30 | -23.75592 | -54.51107 | 2024-10-30 12:59:00 | TERRA_M-T | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 94b105d4-3381-3c77-a022-4d66cd5cbb4d | -23.74281 | -51.83101 | 2024-10-30 12:59:00 | TERRA_M-T | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 68faa32d-3998-3cdf-a6cf-a57c5250831a | -20.26437 | -55.42335 | 2024-10-30 12:59:00 | TERRA_M-T | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 21939862-53b0-3d9d-a318-445b2bc36ce5 | -20.26268 | -55.43395 | 2024-10-30 12:59:00 | TERRA_M-T | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 44.9 |
| d016761f-9e8d-3787-acbe-6ea5a4e42e21 | -20.25498 | -55.42163 | 2024-10-30 12:59:00 | TERRA_M-T | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 69dfceda-6819-3645-94d4-4ac8598fceb6 | -19.63118 | -54.1497 | 2024-10-30 12:59:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 89e98159-af3d-3bd5-ba18-5dab461105ca | -19.62731 | -56.68917 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 0f70dcef-43cd-3c96-8cf4-092db8d344a5 | -19.62522 | -56.70182 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 207.1 |
| 2e5998a7-94c6-395a-bd50-0e163495c69c | -19.62313 | -56.71449 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| ba1a23d3-5ac4-3d18-b5e6-151f7950bc14 | -19.61502 | -56.69996 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 48.0 |
| 58efd3b3-d92d-3f88-b3e2-f084fe708510 | -19.61292 | -56.71263 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 178.7 |
| bea5a6f7-d778-3986-91ba-21d44739bb6e | -19.61081 | -56.72532 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.3 |
| 42d6bfcb-d001-39dd-9497-05ae2e942ba3 | -19.60481 | -56.6981 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| faeaa0fb-9006-3b6e-bf4a-efe14c29be3d | -19.6027 | -56.71077 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 132.8 |
| 75f27822-c529-38fd-b33c-f126f4e2761b | -19.60059 | -56.72346 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 5a1a7ff5-c230-3b8d-a509-02a3d9f59e6e | -19.59249 | -56.70892 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 44.8 |
| b94a37a4-e33e-39b0-a120-1e1181317bd5 | -19.59036 | -56.7216 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 115.2 |
| 5e3637d6-09c7-3d6b-ab02-699a138f6b6e | -19.58824 | -56.73431 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 108b4adb-a4d3-3c3a-97cd-d862ade9a875 | -19.58227 | -56.70706 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 46.1 |
| 2aa657cb-6e6f-3bd4-a0de-bc073541416a | -19.58014 | -56.71975 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 183.4 |
| 8212db8f-351c-3b63-94eb-e39f952361c9 | -19.578 | -56.73246 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 34.9 |
| 80b60fed-de81-31db-aa62-b9b165417819 | -19.57317 | -56.71236 | 2024-10-30 12:59:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 44.3 |
| ec8d13c3-3066-333a-abf4-781e021b99cd | -19.5425 | -56.70678 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 136c85b6-4919-3dac-ad77-8f952fb08320 | -19.54041 | -56.7195 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 4cde7a48-29c3-3b7f-970c-956b50a8e2e3 | -19.53227 | -56.70493 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 8814f5ce-fa17-3f6c-a2e7-20933fdb9b19 | -19.53018 | -56.71764 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.3 |
| 43158c2c-eb9c-3d08-9303-9651ce5127fb | -19.51394 | -56.68853 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| c775187c-84f6-32a6-8fef-c16007d1779b | -19.51036 | -56.58421 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 53b445d9-1263-307f-8bcf-b3116c960a75 | -19.50372 | -56.68667 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 64043368-b868-3ac0-9301-fe2708d20175 | -19.50085 | -56.58884 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.2 |
| a08a1ddb-412d-3f52-8dcb-c2e0b5052a3b | -19.50021 | -56.58239 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.8 |
| 6b011a1b-df48-36c1-b55f-7e74b08795df | -19.48967 | -56.64508 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.5 |
| b01123ce-bc70-3de6-8261-ee89f64c8efb | -19.48755 | -56.65769 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 421b4328-864e-3d23-aa8a-85aa21761766 | -19.48049 | -56.64985 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| a6a00b02-3e84-39e6-bfd4-f442d446aa26 | -19.47844 | -56.66249 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |
| 2fae55d1-6834-3a81-84f1-221065a87537 | -19.47638 | -56.67515 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 9f551a6d-faac-3ebc-b687-5060a905f8f3 | -19.47441 | -56.6228 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 2d8d718a-2c0f-39ce-8e91-ac5475418998 | -19.46423 | -56.62095 | 2024-10-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.5 |
| 96bf4cd2-8146-3e08-a855-6339f341d499 | -19.35994 | -53.805 | 2024-10-30 12:59:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0404d7ac-7cf1-312a-aacb-5a0fa05c5906 | -19.35852 | -53.81451 | 2024-10-30 12:59:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3cd4eeb2-f88b-316c-a487-545a7c83d818 | -18.87596 | -48.31145 | 2024-10-30 12:59:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 24.0 |
| a1dda747-5f88-3cf3-9d5d-d31e92233b98 | -18.74207 | -51.76409 | 2024-10-30 12:59:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| eafe98dc-170d-3611-984c-596ff2de505b | -18.72398 | -54.76775 | 2024-10-30 12:59:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c68c0a0f-7ee5-34b3-806b-f4ac71459c72 | -30.3633 | -52.22174 | 2024-10-30 13:01:00 | TERRA_M-T | PANTANO GRANDE | RIO GRANDE DO SUL | Brasil | 4313953 | 43 | 33 | nan | nan | nan | Pampa | 57.1 |
| e2d5f20a-ab10-3c16-b814-728eea561ea9 | -28.81626 | -52.62943 | 2024-10-30 13:01:00 | TERRA_M-T | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 70f120de-fb24-31ef-aa08-1b8c1730c0da | -3.6648 | -42.4384 | 2024-10-30 13:05:27 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 146.6 |
| ab52358f-3d58-3e0e-87ca-ffad9f0599e3 | -4.2563 | -43.4368 | 2024-10-30 13:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 159.7 |
| c14d0449-bbeb-3821-82a6-528dbcc06e1b | -4.2749 | -43.4357 | 2024-10-30 13:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| d3976f0e-d0d7-31d1-819d-75ca6ffd11ea | -4.2561 | -43.46 | 2024-10-30 13:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| a75e968d-8fd6-32e3-900b-bc117421f085 | -4.8432 | -42.4634 | 2024-10-30 13:05:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 141.4 |
| 1a90d10b-e953-3d39-b25a-5cce9363c225 | -4.8619 | -42.4622 | 2024-10-30 13:05:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 5b679a0d-e4b4-30f3-9e1a-948eb93f6c33 | -4.8617 | -42.4858 | 2024-10-30 13:05:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 133.9 |
| 6cfe03ee-5e4c-359c-8b5b-315c40f12cfc | -17.7446 | -57.5344 | 2024-10-30 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| c878404b-b1c0-3a87-8429-dc7b4a37ba83 | -17.745 | -57.5138 | 2024-10-30 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| d4f00228-2571-3701-bad9-37a67c451282 | -17.7443 | -57.555 | 2024-10-30 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 2ca8ddf8-bacf-356f-8731-40850d6cbcbd | -19.5465 | -56.6983 | 2024-10-30 13:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.7 |
| f3b1a17a-510c-3f03-8133-a3e675c4949b | -19.5087 | -56.5779 | 2024-10-30 13:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 2a283ee1-45f3-3e48-98a4-f6bb1b695db3 | -19.4878 | -56.6227 | 2024-10-30 13:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 86192092-21cd-3f8f-8478-9a2b3d33a9a5 | -19.5083 | -56.5989 | 2024-10-30 13:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 5a2a9030-48e9-365f-827c-996b3ae47873 | -19.5662 | -56.7164 | 2024-10-30 13:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 2cac398f-cda0-3013-ac6b-ab5061183b7a | -19.4874 | -56.6437 | 2024-10-30 13:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.4 |
| cb432c40-0b86-3ab0-aa5c-cb3348398966 | -19.487 | -56.6647 | 2024-10-30 13:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 7ed253e1-a1cd-3306-b6e3-616b476a9f50 | -19.6067 | -56.6898 | 2024-10-30 13:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 125.4 |
| dd04e027-b560-315d-9403-e8d066b375a3 | -19.6268 | -56.6869 | 2024-10-30 13:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 125.5 |
| 1578f85a-08ed-3042-ac90-a78446a9b541 | -19.5866 | -56.6926 | 2024-10-30 13:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.2 |
| cf24a698-05c8-3f2f-9a47-02d7b593606a | -20.255 | -55.4318 | 2024-10-30 13:06:59 | GOES-16 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f12e6f5a-019a-3b0a-93bf-0289c9a13f79 | -23.9923 | -54.1106 | 2024-10-30 13:07:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| 881a2e12-6edc-398d-b3a4-c0f735d18432 | -3.6648 | -42.4384 | 2024-10-30 13:15:27 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| a31dda21-b378-36a6-a31e-45f87372582f | -4.2563 | -43.4368 | 2024-10-30 13:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 188.4 |
| f5f58bf7-cb70-347a-9680-f5ee0a02e505 | -4.2561 | -43.46 | 2024-10-30 13:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ef9bd771-671b-35e2-9225-06bf16b19d22 | -4.2749 | -43.4357 | 2024-10-30 13:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| ce9c60da-526b-3b3f-b0f9-df79a4f45c9a | -4.8432 | -42.4634 | 2024-10-30 13:15:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 203.8 |
| ea0caf19-2a36-386a-b575-58a71d0af652 | -4.8619 | -42.4622 | 2024-10-30 13:15:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| e1200ab3-8798-30da-abb3-07616ecd7c97 | -4.8617 | -42.4858 | 2024-10-30 13:15:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| e81bb753-8d43-3e6b-8c7d-9b9a3ff78789 | -17.7446 | -57.5344 | 2024-10-30 13:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 6895d115-e9ac-3cf3-aa5d-3576b0deef7d | -17.7443 | -57.555 | 2024-10-30 13:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 74a43f1a-414c-31f4-8ae1-32de4c73c64e | -17.745 | -57.5138 | 2024-10-30 13:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 0edc4682-72aa-3c91-b8a0-2f8599810ec4 | -17.7252 | -57.5162 | 2024-10-30 13:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| e0359956-666d-36d6-9fa6-00fb39ffea71 | -19.5087 | -56.5779 | 2024-10-30 13:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 6eb10d1c-b624-3778-8370-59f668f1af4f | -19.5083 | -56.5989 | 2024-10-30 13:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| ca5195a0-bc10-3366-8669-4e730eb5eb2f | -19.6268 | -56.6869 | 2024-10-30 13:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 145.4 |
| 80fa154d-575f-3bbb-a28b-d89f969c7e7d | -19.6067 | -56.6898 | 2024-10-30 13:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 137.6 |
| 7bc27b96-6c39-34f9-a652-b2ab2c552ec8 | -19.5866 | -56.6926 | 2024-10-30 13:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| d7999e5f-412d-3c14-886d-d511aa833a19 | -20.255 | -55.4318 | 2024-10-30 13:16:59 | GOES-16 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 23253a31-fd8c-3d78-a5a3-06514e9dab17 | -23.9923 | -54.1106 | 2024-10-30 13:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 81.6 |
| 368d843f-7c9a-3363-a302-dff70cc69830 | -3.9326 | -41.4957 | 2024-10-30 13:25:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 83f10946-698c-3f6b-a7a4-394b4be4b344 | -4.2563 | -43.4368 | 2024-10-30 13:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 351.3 |
| 820cfdb6-d7ce-3236-aa37-286b330e49fc | -4.2561 | -43.46 | 2024-10-30 13:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 090ed3d6-2b26-3264-8f60-14e8d622e6c8 | -4.2749 | -43.4357 | 2024-10-30 13:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 82445b70-0d9b-3536-8e1c-eb534636daf8 | -4.8617 | -42.4858 | 2024-10-30 13:25:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| fe6f8259-d467-3641-ac5a-2e9f8b7217cf | -4.8619 | -42.4622 | 2024-10-30 13:25:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 105.7 |
| f07ee732-eb54-3538-a491-d1c628678e53 | -4.9311 | -43.1857 | 2024-10-30 13:25:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 0da96336-8647-3637-8ff1-632ed77223ad | -17.7446 | -57.5344 | 2024-10-30 13:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| ccc41ac1-2a70-32b0-abfa-a19ee6edad51 | -17.7443 | -57.555 | 2024-10-30 13:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 579a66bd-6a1c-3ec9-8bf7-9788c42a365a | -17.7252 | -57.5162 | 2024-10-30 13:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.7 |


[Clique aqui para ver as próximas entradas](README104.md)
