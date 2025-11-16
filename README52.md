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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14f75be9-8557-3798-ace4-8c8b28c2591e | -1.22036 | -55.8327 | 2025-11-16 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 677b4fa0-d9d2-322b-89c4-def03558e114 | -2.80503 | -52.9654 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7f557619-b8d0-3ad5-bcea-5fd9fad597f1 | -1.64793 | -53.66338 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e35b71f-7c3d-39c0-805a-9c361a22093d | -2.93326 | -49.35017 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a6f6b1a-9967-39cb-b3f0-54b9813afa57 | -4.16531 | -46.83952 | 2025-11-16 04:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4749fa39-74dd-3077-8788-58772149aae0 | -2.84432 | -52.36587 | 2025-11-16 04:55:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 316a0554-7b14-39d6-aaa6-fcf8b599c971 | -4.07414 | -46.34254 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8304aac0-1cf5-363b-842b-2929725954b1 | -4.25076 | -50.05505 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5a58cbe3-90c1-36a0-a0b4-b656c0b4b28e | -4.05167 | -54.84424 | 2025-11-16 04:55:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 335aae34-ba6c-3451-8858-c39925f98ece | -3.10527 | -51.51754 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 325c5162-586d-3306-bed6-ac72499bc0e0 | -3.40055 | -50.18295 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea52bd1d-61a5-3a08-8d0c-37c4954b3be1 | -4.02069 | -48.809 | 2025-11-16 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0948869d-7e91-39d0-9749-3ac91467be7c | -3.67844 | -52.29698 | 2025-11-16 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 334fb0ee-b7c2-35f6-b1ea-1e565b097555 | -1.8471 | -56.37146 | 2025-11-16 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 978f9299-9a40-3704-bc9c-ead0f1fa650f | -5.21547 | -44.51391 | 2025-11-16 04:55:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dc69ec7-10e5-3a84-a490-5665c672268a | -4.20675 | -48.5606 | 2025-11-16 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18d40371-d521-3d26-8a7c-f49795bacfe0 | -5.4291 | -47.32384 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7411d80-33a6-3b51-ad03-ea7624737822 | -4.49837 | -50.49431 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f744e11f-3db2-3ca4-bfc8-2a1284f03825 | -3.34138 | -46.28921 | 2025-11-16 04:55:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe84f659-6b1d-3419-81f2-d24b4ebe3c15 | -3.41934 | -46.15092 | 2025-11-16 04:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edbb994d-c6e1-3747-993d-26570a71569c | -3.94488 | -52.17456 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02368d06-42cc-34c8-a500-81294c36e34b | -2.54497 | -47.45641 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bd77a82-3f6e-3856-9b8e-ef6ef1993e0a | -3.59952 | -47.52373 | 2025-11-16 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e80fe950-5426-36fc-b8bb-46e58a52cceb | -3.22178 | -43.35497 | 2025-11-16 04:55:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e5196be-5826-3131-b166-9cbf9f7cd150 | -4.73968 | -46.37782 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| eca708dc-646b-3292-8f8f-28af5749cb29 | -1.34957 | -54.6123 | 2025-11-16 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d88049bd-3f51-3467-aaee-73305baa2b11 | -3.5463 | -55.49131 | 2025-11-16 04:55:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d027c01-7fee-3bf7-b02b-df07674ad6c0 | -3.28958 | -53.82625 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fb2857a-9c03-3700-9143-d46fd34ad464 | -4.39672 | -49.66702 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16302327-39f4-3e7d-bed6-0795f736ee8d | -3.13127 | -50.29401 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7a561f4-2e27-3021-8f53-92a6351186bd | -4.05223 | -54.84068 | 2025-11-16 04:55:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce618335-1084-3875-8222-a9264fe475b2 | -3.96109 | -44.84827 | 2025-11-16 04:55:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f0d850a-2434-36a8-ac51-51e6d57a0961 | -3.85789 | -40.76789 | 2025-11-16 04:55:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5bec5d78-fd7c-3c49-96c9-becb6b02d223 | -3.26932 | -50.77975 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99e3c611-91e7-3e78-ae1e-43eab5dab3c8 | -3.45814 | -51.02097 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54d3d990-5c80-317e-a034-2ca86ebfa476 | -4.66232 | -46.74908 | 2025-11-16 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2583577d-e8ee-382f-89d0-92da175e5634 | -1.6463 | -53.67374 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a85211d9-ca55-38f5-beed-b759ca9fa3cf | -1.34675 | -54.60818 | 2025-11-16 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5d32a97-de2f-397e-b745-19abab187a75 | -3.49372 | -54.04255 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b5a5b55-1ff3-3cff-b280-05242b350ce5 | -3.33678 | -50.27605 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9f361abc-7cc0-35a7-aa54-ff926d4d24c4 | -4.89075 | -45.02091 | 2025-11-16 04:55:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d105bb7a-6643-3514-9a2a-dec51f49cbae | -2.12684 | -51.08317 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f982190-c298-35f3-a566-cadfb0a817b5 | -4.84554 | -45.42815 | 2025-11-16 04:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15974d4c-0b3a-36e2-99c6-ca4f8bf7807a | -5.29853 | -48.61199 | 2025-11-16 04:55:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b04c044c-018f-382f-b6c7-2b65ea8cefe0 | -3.10994 | -53.12593 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a243a8d-c8a6-344b-9645-35f82253c16f | -4.22663 | -44.64191 | 2025-11-16 04:55:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 280e2322-0669-35f3-9ce1-1345c7427574 | -3.45756 | -51.02481 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4df2afae-ea4b-3450-ac59-8c667ed34d2c | -1.32511 | -54.22041 | 2025-11-16 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5961adf-e331-3c9e-bc60-72921e808a0a | -3.18264 | -49.23946 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57d8a558-01cb-32ef-a89f-d7b1a7d1d5b5 | -3.38218 | -50.13275 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 167c3df8-d43c-3854-be90-862834456de1 | -3.49317 | -54.04601 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2077f570-eb73-3aa1-b1bc-3406e9cdac69 | -3.77258 | -44.95707 | 2025-11-16 04:55:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 456fc589-4acf-3b0a-b536-5df9375d681d | -3.15231 | -50.26625 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3906f7f2-f2de-3d10-96c5-57e784e8481e | -4.84217 | -47.55288 | 2025-11-16 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cf6bcc1-7810-3983-8037-ddefc343b638 | -3.02148 | -51.62493 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4240aea-3f23-3572-a9f9-d1e9839f5f70 | -1.14926 | -54.10668 | 2025-11-16 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d19d44c-829d-384b-a842-eb5a71318dbe | -3.7679 | -44.95323 | 2025-11-16 04:55:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db468b6b-7e1f-3823-a391-7771642ab7b0 | -5.73169 | -42.73259 | 2025-11-16 04:55:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7ad8a224-1f02-3058-9eff-6e836bb50d2e | -2.57926 | -51.85926 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb36c89f-1273-3f3a-8ea1-7ad0a56688f3 | -4.67187 | -50.36761 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7771d410-124e-32b1-966d-5d9d5a713add | -2.29458 | -56.43966 | 2025-11-16 04:55:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc8465fb-8c65-30e9-a242-d87012f5d0ce | -4.19236 | -51.02207 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84866a27-658f-3c35-9678-d37b8c921c12 | -2.25381 | -46.067 | 2025-11-16 04:55:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c096209-9649-38e6-a59f-331be195e91e | -3.3034 | -53.84602 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2852c6e6-9f74-3d3c-857b-ecab836bf6c5 | -1.17209 | -49.20396 | 2025-11-16 04:55:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98c7aa83-55f5-31bc-ae90-ab20f20d935e | -5.1577 | -46.12926 | 2025-11-16 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec4623c1-b8a2-336d-b692-015c7b2236bd | -3.33792 | -51.12076 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6923e1ea-895a-3d82-ad13-759bd4063d2c | -4.39966 | -49.78177 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12a8a48f-e0fe-35b3-9aa7-d697c794b244 | -3.82287 | -52.04648 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74a995bb-fa13-3b6d-94a7-6a2974475763 | -2.14213 | -45.35033 | 2025-11-16 04:55:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4b781273-5879-3298-bb54-be356deaee63 | -3.69761 | -52.01944 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe0684ff-58a3-3bf9-869d-391843ab3b89 | -1.22118 | -53.36633 | 2025-11-16 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fda1972-6414-3b0a-8f78-a5f42622c63b | -3.76745 | -44.95628 | 2025-11-16 04:55:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d744371-1edd-34d4-af84-68c05285c51d | -3.24341 | -51.34966 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 439e0040-fc1d-3815-bb40-dd4e3df3e975 | -1.98943 | -47.35139 | 2025-11-16 04:55:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef6132e4-cd9e-3dde-aca1-eeaa6ac83e44 | 0.14358 | -51.07134 | 2025-11-16 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12a3b77d-6a2f-3957-9387-35c33e3eed78 | 0.82907 | -51.37994 | 2025-11-16 04:55:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfb472f7-dd9c-3ed8-9a16-51fc9033853c | -3.76838 | -51.19575 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fb311eb-af28-3ea2-9fb7-d81835a65fff | -4.12655 | -46.37607 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c037fc3-a032-303a-8082-6e82796e6ccd | -4.84361 | -47.55092 | 2025-11-16 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 526a72bc-0700-3a6c-a6de-ac9f3cc215b9 | -4.42618 | -43.40453 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 68040b08-a284-30c1-8c29-077190864bbc | -4.40839 | -43.40601 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b74ed6a2-0480-3034-bff4-56b12c6ce7d7 | -4.34781 | -44.35265 | 2025-11-16 04:55:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02d665c0-e9f0-3dad-8f1a-830e0edbf43a | -5.42091 | -43.25432 | 2025-11-16 04:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 448b9467-ab7b-3b5c-8e6d-b6021962d4db | -2.13936 | -45.34762 | 2025-11-16 04:55:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b5e6a158-e163-3903-82e8-81bdedb19115 | -1.64961 | -53.67425 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 215e77ea-dedf-302f-8239-55e7a2174aa4 | -3.32708 | -45.85408 | 2025-11-16 04:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 533786d2-3ce5-3561-af3d-2c7fdab3eeb1 | -2.58097 | -51.87047 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd26e147-9434-3472-b363-2aa361d604a3 | -4.11257 | -50.05585 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3660d46-df0d-3c94-8bce-d6e135bf90aa | -0.87878 | -48.07977 | 2025-11-16 04:55:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 765d00a8-995b-3010-b15d-0a45553a155e | -5.23873 | -44.34823 | 2025-11-16 04:55:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| db537670-db2b-3565-8014-777240003f38 | -3.85117 | -40.76689 | 2025-11-16 04:55:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7b276440-df4c-39ed-9f4a-d6b332aaec9d | -4.84151 | -47.55723 | 2025-11-16 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3623fd4d-37c8-3b2e-a433-594a30cea3cf | -3.60948 | -54.71241 | 2025-11-16 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a95bd75-e45a-33a0-9f24-2d3768040fb5 | -2.69207 | -49.07619 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c84ee538-a045-3aff-af38-a823780f075f | -6.00577 | -41.91056 | 2025-11-16 04:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9e704b1f-437c-3870-bcb8-08488d5ab1ba | -3.87136 | -52.27981 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f35c37d6-a499-38c2-ae3a-d3223feeca16 | -2.59039 | -51.83175 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33512bf8-26d0-3623-8a17-9c19b8f7cd47 | -4.74839 | -46.38415 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba42cb7f-d782-3ea7-abb2-349e98fcb51f | -4.2952 | -49.74689 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README53.md)
