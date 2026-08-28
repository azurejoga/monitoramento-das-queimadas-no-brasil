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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cda6421a-4df8-3556-a096-8a8c2fb21815 | -13.64267 | -51.70013 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 03b8a0a9-68e2-3228-ab2a-ef25c5ce877d | -9.26309 | -63.70926 | 2026-08-28 17:45:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2fa561e6-432e-3398-b7f4-b9ab914ce1b9 | -9.85292 | -65.00376 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e1501b71-52e4-3548-a59a-d01e9ffe7c81 | -13.25172 | -51.56839 | 2026-08-28 17:45:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ec09a03a-2cfd-32f0-9444-0c225b98ee10 | -10.27874 | -68.86388 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 109983a8-8607-3f21-a586-b0d6a36531af | -12.98567 | -60.08894 | 2026-08-28 17:45:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d95c5e42-ad83-3286-b25e-99524f078bba | -9.69581 | -65.09472 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 11454708-f06a-3536-b1da-c470409c0ba9 | -11.27276 | -54.02384 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 716bec39-844e-3e16-8525-2dd156853cc9 | -11.27449 | -54.03725 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f398ec4a-e091-3424-bce0-955af2ef39de | -10.2727 | -64.50011 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 1854271f-a3fb-34f8-82b3-d634c39f8e1d | -9.20423 | -61.11417 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 161383b1-edcf-3cbc-8d18-60c8b1e92f04 | -14.43658 | -53.38964 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4a3eb1fa-0aad-3687-9223-3c6b2f0ef1c8 | -14.1809 | -52.8563 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 510f09dc-8591-397a-8bb2-b73ead3729f7 | -10.0767 | -69.09908 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| daf937d0-fd19-3ed3-917c-e5533735d351 | -9.6894 | -65.09966 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b9879c1d-45e4-3225-911e-dfc2264a212c | -14.43163 | -52.60793 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aecc76af-005f-38cf-ab59-e9fbcf2929eb | -11.62798 | -54.57521 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 60ae4043-ae96-306b-8bd6-429737c4125f | -14.91349 | -52.60864 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7e7518c3-e63f-3e91-9e5f-411069916bb9 | -9.86797 | -60.26474 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a008fd15-d7c7-3b64-bf99-c22434171501 | -10.1976 | -69.35419 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f7c66fdb-dc16-365f-b493-2d462fb076f4 | -12.92076 | -59.8821 | 2026-08-28 17:45:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1cb56297-5f95-3c22-af54-89c38376bdd8 | -14.65256 | -56.99562 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 986c4a0b-8c6a-3554-9454-23681f681aba | -10.07782 | -69.09745 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8cd031a5-11c6-3b9d-8fbe-3a01f2232f7a | -14.90972 | -56.32043 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 83de35f5-cdcb-3264-bb20-2328c8d6411b | -10.83979 | -50.50769 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bd990ee3-9072-329f-8b7d-d7999de3e9b1 | -9.10241 | -59.41386 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 80ca9f9a-0e0e-3032-b005-1a5b161527d0 | -12.39003 | -48.1862 | 2026-08-28 17:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e9d9bfbf-1519-3116-8be4-c2f69594c9e7 | -11.27031 | -54.01421 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 859a14af-6971-3c8a-a8f9-3886e89b4a67 | -13.47648 | -57.03958 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| c5f71a13-0d7b-33a1-a1b4-da517b8d923a | -9.90448 | -60.15878 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8dc864c7-f047-305c-8a55-993823a32fbc | -9.69232 | -65.09524 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 911426a6-eaec-3d5a-b6f2-c960414ed443 | -14.63881 | -57.00835 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7e55d527-706e-3913-b445-3dbe498ab6d5 | -14.87594 | -52.63318 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a4d651c0-34e0-35da-ad15-9a903dbd5c4e | -9.19565 | -61.08163 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 79346147-1c54-36e8-8077-f8e7c4ff2975 | -13.46574 | -57.04454 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 89baa25e-f695-3d19-bc84-06f4ca2d162c | -9.22363 | -59.77366 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1ac764fb-635b-3e93-ac64-53ca4ec71075 | -10.76916 | -69.51055 | 2026-08-28 17:45:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 63135d10-cc01-3d14-b8b5-dc19e213b8f2 | -13.10382 | -50.04673 | 2026-08-28 17:45:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8db00dba-602e-3da7-a2a4-dbb56d24789a | -8.21728 | -54.95441 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6d41bb5b-f6a3-35fb-a15b-ad37bb9f37f5 | -12.69262 | -48.42685 | 2026-08-28 17:45:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adedd45c-33fe-305f-a95c-42ebddbb4672 | -10.50129 | -64.50864 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1c2ebfe-3d50-35d3-b639-44501f26ea3a | -14.8736 | -52.62123 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 3f631420-5bfa-3b8e-99d0-57f14a257da6 | -13.42115 | -51.76179 | 2026-08-28 17:45:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5efb169d-e97e-384e-8fa1-f41cb2dd31f1 | -8.24567 | -54.98997 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8990cb31-0c8d-3f33-8c57-17268d040264 | -9.41922 | -50.44324 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 310ef336-7b2b-36c6-867d-2656df61073d | -14.38704 | -53.28814 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 654843d1-d990-318f-aee3-2591a67d6117 | -14.91246 | -56.31253 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| fb131464-30ac-342e-b899-fb5897aeba0d | -9.86733 | -60.26085 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 674f007d-3a7f-3f93-9594-85c58d9298d5 | -14.87303 | -52.61827 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b9e1f215-f6b8-300d-a178-9ff5315cec7e | -14.46125 | -58.52298 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53ab576e-784e-3654-92d6-56994c2b25a6 | -14.91655 | -52.60983 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3187ba54-08c3-3788-8642-8a20c5b81104 | -9.76197 | -64.97716 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e0a8186f-a6b7-311c-96f5-accf70090b91 | -11.40891 | -59.42463 | 2026-08-28 17:45:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 1cba1704-9728-34df-9dd6-33fcb3b629e6 | -13.877 | -53.24062 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 7ef7ccc2-80b4-3d88-bd1c-6532fc64e1d4 | -9.50938 | -56.93076 | 2026-08-28 17:45:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 94661e23-7aef-37a5-9764-fcdf4920738e | -8.56498 | -54.90361 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| bc4bf781-7313-3728-a7ad-9deb0948b3f6 | -8.6072 | -54.78984 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 689236f4-8971-36ca-bf53-0e85e1a3de64 | -9.0102 | -57.53976 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| aac5d6c1-0dac-3067-b0c9-99c0ad152a05 | -14.64267 | -57.00764 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| d5941e39-26cd-3039-8e51-6930a88fb48c | -10.31984 | -68.4605 | 2026-08-28 17:45:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 7a715722-53c8-3bec-ad68-72fe5c67770e | -10.35476 | -64.46465 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b8952812-f062-3c29-bde9-20e92a10d4ff | -9.12525 | -61.05499 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3ce98cc5-5cd9-32d4-889a-599e9e8e434d | -14.92247 | -52.60028 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e7f8aa4e-3cc9-341b-af35-48ffdeeacdfb | -10.28746 | -68.53415 | 2026-08-28 17:45:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 240e531d-9bd9-36a7-a89d-a9f8bc1b8fa7 | -10.50806 | -59.63188 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 1f5b0008-6129-314d-ba3d-7decfca0b2e5 | -10.50609 | -59.61962 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a92ba6af-b932-3c9b-811b-ce3860910fcd | -14.42795 | -52.58908 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 148f1f64-837d-3e5a-8de0-0cee18439d31 | -10.49451 | -69.16479 | 2026-08-28 17:45:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a5731091-aa8d-34dc-9f57-325151df63b0 | -10.49107 | -64.487 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 79bf3dbe-6f15-30f2-abf8-2e2b7f6c6768 | -10.50528 | -64.51188 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b7b59cb-9a09-3def-93fa-7dd6d7245008 | -9.11539 | -60.92728 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8f0d74cc-79b5-353e-8884-204e16a4692a | -14.65039 | -57.00625 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 2d14dcff-e18f-31c9-91c2-2144f7b9c103 | -13.87616 | -53.23626 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 82add112-875c-34ea-86c2-2a529c439dff | -12.38454 | -48.19437 | 2026-08-28 17:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| ed3bd042-b047-3080-9aeb-91942586ae3c | -14.61436 | -53.14841 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9bec7221-c7ad-3c95-867d-75b1121758c3 | -10.4728 | -64.48204 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 17.8 |
| d3da9c56-efb2-3827-be4e-82d254ca4683 | -10.83451 | -50.51394 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 42cd6557-75df-3114-a761-f97bdddaf408 | -14.17822 | -48.76247 | 2026-08-28 17:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7e898bef-6bdb-3213-9592-33c5fe98db53 | -9.01142 | -57.54692 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 202992d3-502c-3adc-8cf0-f35fc660dc43 | -14.59029 | -58.64668 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 266be752-04d0-3325-aaa2-448dc95a0cce | -9.45966 | -60.47289 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9133da8b-5d01-35a5-8d61-d203a8f4313c | -8.80008 | -49.99105 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b718b978-46f2-3838-8d89-8286a975abc9 | -9.17 | -59.5774 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fddc497a-f5c9-3e23-a9f8-f8e9e6279091 | -10.58124 | -63.54325 | 2026-08-28 17:45:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5f0b4eb8-182b-36e2-a07f-9abe302f3492 | -14.60332 | -53.14446 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bccf1123-60aa-38e2-b26f-3d9378df183f | -10.50584 | -64.51567 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 134b0e79-6fe5-39ba-ba90-63048e91476d | -10.5032 | -59.62431 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a7c5b0fe-845b-3aae-97d1-3c248a6b32ca | -8.79575 | -49.98713 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4155ac8e-9d1d-373c-9d85-860e6856bb04 | -8.95835 | -50.7979 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| c44842f4-7f69-3ffc-8811-822309741d8d | -10.27326 | -64.50388 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 850839bd-21a3-3e0f-b797-213911a8857f | -10.50073 | -64.50486 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4200c9c6-3752-3268-8a85-c971c193c30c | -10.77315 | -50.6295 | 2026-08-28 17:45:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c3354efa-c32d-3cd6-8563-cdd287290887 | -9.46052 | -60.55921 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 071b73c3-2d97-3bbe-a227-c92c6b63ace5 | -10.40626 | -61.20255 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 18c9171c-599d-379a-8189-5fb434e91a67 | -14.17164 | -52.83557 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 22912b7b-4a34-3dd2-99ca-140c4c1e9ea6 | -8.21468 | -54.95813 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| dbdfea4f-3b15-3f78-a7c3-6f7eba184d93 | -9.02243 | -57.53762 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 650c8360-e12d-38cf-a298-53945ad0f616 | -14.41016 | -52.58019 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9e02f786-5e4c-32f9-9096-6ef313fa2b1c | -10.84604 | -50.50649 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 644286d9-0125-3dce-9915-4df3a9d57140 | -14.42531 | -52.60292 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README143.md)
