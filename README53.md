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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0ce79d0-7215-3d00-8cfc-af6d08f00d90 | -12.58285 | -60.3526 | 2025-08-22 05:14:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04f806d3-da37-34e9-8f10-7c143a4f1d57 | -14.62699 | -54.85153 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 864523bf-a81c-32df-a473-f8df782bc524 | -20.24196 | -46.60174 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e08fcb7e-99db-300c-bc60-a925c9fbb3ff | -14.77026 | -55.99934 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0de2849-b02f-389c-ba91-0ec4f403f53d | -14.65029 | -54.88493 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 793f875d-bab2-37a9-93a2-c28b45dcdf7d | -15.16074 | -47.9548 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54605330-786d-31c7-b300-14a2be3e5e1e | -16.18964 | -47.98855 | 2025-08-22 05:14:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d17ce5fe-04bf-38cc-bbfc-1c6ebe80fb8b | -15.1383 | -48.10753 | 2025-08-22 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1528c357-0206-30d8-94c6-bd678041df09 | -14.89471 | -48.06006 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29706011-e546-3c30-8570-abf814d212ee | -14.88742 | -47.95446 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e6952d61-a629-348a-9b79-7df2e88c6dc6 | -20.43133 | -46.50822 | 2025-08-22 05:14:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f338d8d0-64e2-35ad-8699-d1b1f6893196 | -14.86681 | -47.97301 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96c02035-b7d2-36aa-aff9-7c2b30206db2 | -23.20129 | -46.86036 | 2025-08-22 05:16:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 930f949b-69f7-3f9a-aba6-ff1cc0202ce6 | -26.75476 | -52.47056 | 2025-08-22 05:16:00 | NOAA-21 | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0e951604-cb2a-304b-bb72-d2935e7729df | -22.55237 | -49.76853 | 2025-08-22 05:16:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89b60e81-3c1e-3617-aa88-1bc34a38a01c | -22.55835 | -49.76922 | 2025-08-22 05:16:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f1a4585f-57e8-31b4-ab40-3a8ecbccc24d | -22.55487 | -49.76929 | 2025-08-22 05:16:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 700f3184-2fb2-3fc0-a877-10a9801e367a | -23.28866 | -47.47411 | 2025-08-22 05:16:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 09d791aa-02c7-3a84-8ae6-c877388e8e2f | -23.29515 | -47.47107 | 2025-08-22 05:16:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 228379df-6eb1-350f-bc98-131437511de3 | -23.29595 | -47.46838 | 2025-08-22 05:16:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f2869e0a-0d22-3823-a4ca-404c672d3e12 | -23.29552 | -47.47508 | 2025-08-22 05:16:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| b83e293a-c710-3f8f-bfd5-1fa45cfd2d13 | -23.29468 | -47.4777 | 2025-08-22 05:16:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 9d8f83b0-043c-39dc-8f59-0f0173351ec9 | -23.30283 | -47.46898 | 2025-08-22 05:16:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 93e53d24-e25f-36c1-890f-917f44394c8a | -27.68534 | -48.75357 | 2025-08-22 05:16:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8900a480-1d82-3f25-a0e4-1ed7e4aa1f8b | -21.59537 | -48.98792 | 2025-08-22 05:16:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab9c6f25-08d5-3003-81f8-9ece15f52c57 | -23.19757 | -46.85994 | 2025-08-22 05:16:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 81f92a99-7fca-3bf2-af72-4092d134d799 | -15.8955 | -43.4523 | 2025-08-22 05:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 70.6 |
| cf64e3a9-e0e6-3670-870a-55460e9eb250 | -10.8757 | -50.8376 | 2025-08-22 05:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| ab208b11-b308-3703-a781-c709645473ac | -15.8955 | -43.4523 | 2025-08-22 05:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 50959ef7-f5e9-3d06-bba7-10c6764a89a7 | -10.8757 | -50.8376 | 2025-08-22 05:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| a8f529b6-4ade-327f-82d2-0a6f4eff4c41 | -4.3294 | -55.13661 | 2025-08-22 05:36:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0c95f54-4be9-3248-9f2e-b1d14b79639f | -1.97228 | -56.51694 | 2025-08-22 05:36:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dec656b-1458-39ed-95ac-1f5f55fc70b9 | -2.93386 | -53.70053 | 2025-08-22 05:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01a512aa-aaeb-3372-82a5-5637eb7a3cd1 | -3.25878 | -60.6575 | 2025-08-22 05:36:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61884d5f-f54d-336f-ac63-5b34f104627f | -4.24786 | -54.92756 | 2025-08-22 05:36:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e5418d1-33ba-32ab-9a6f-78e68fffbacf | -4.32527 | -55.13027 | 2025-08-22 05:36:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c803ae6d-14d7-3fbb-9a97-c556b880e100 | -4.32445 | -55.13581 | 2025-08-22 05:36:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e8edfb7-1219-30ed-88e2-f3434a1165f6 | -2.93436 | -53.69719 | 2025-08-22 05:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6c05cb4-097e-30bc-8d7f-3f5c7e13e113 | -1.50298 | -55.92292 | 2025-08-22 05:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 118cdd1b-02c4-3526-9b5d-a79eab6818df | -9.18339 | -59.58865 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c66fc9d-24d9-3d8f-a322-af7b4a76f425 | -6.27552 | -53.70672 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1b3346e-13b4-34e2-8cbe-34dff4d66470 | -8.88414 | -62.40581 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66fba8a7-e8dd-3129-a6a3-a27b8605f430 | -9.22486 | -59.76941 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9137ca51-4fc5-3d0d-91b1-514aa93e4834 | -7.30258 | -59.62816 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6a3c187-b8af-3986-bbc6-fea35209d313 | -10.03704 | -59.35504 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10c22743-4f6f-3d27-9057-1bf39e68126d | -7.54936 | -63.84592 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1705ebc1-4f25-3d09-b539-af927a96ea3c | -8.86819 | -62.41848 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aedbd6e9-f38a-3808-999a-d11b2d361d75 | -6.26977 | -53.68759 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e9d67eb-f5ea-35a6-8654-07e47d30de0e | -5.88 | -53.63645 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 085679c9-718f-326f-8b21-7b80268fb58e | -5.88409 | -53.62808 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19f66c33-4234-3560-a3b4-a6872e3b4357 | -6.62978 | -58.54464 | 2025-08-22 05:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cac7af2a-d8b5-3c4f-ba59-e3c9de4d1104 | -7.55323 | -63.84297 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f847304e-181d-3242-8759-5418115b25dc | -6.44836 | -53.38949 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4b2dd87-b5e0-3f0c-a685-de1ecb1f6ac6 | -10.87135 | -50.84764 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a5b91b5e-50fb-3862-a2f6-25e39412fbbc | -10.86579 | -50.83282 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b0ef0c3e-341a-3f20-9c2a-264931e1e5d4 | -9.91326 | -62.14148 | 2025-08-22 05:38:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9ac1134-10f2-37fb-9902-73ab5ce4a515 | -5.8785 | -53.62709 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e26d30ea-6f32-38c1-be03-848c314470d5 | -8.8877 | -62.40187 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71a7e76a-16b3-306f-b4bb-e9b6b897cfc3 | -9.21537 | -59.47043 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea8bdc35-5a91-3db8-97b9-5a05df18dd54 | -7.55545 | -63.85045 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd09acc0-18a6-3beb-80d6-42ba541ea2f7 | -9.15831 | -59.59509 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7985e01c-a6b2-3be4-8445-27cf2e5ce1b6 | -9.21284 | -59.45961 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e8f7705-94cb-3af5-a211-733d67d3ce97 | -5.8059 | -59.22779 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcd1f625-0a66-3b47-98cc-bfa301d5ed73 | -8.60308 | -62.6217 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d007dbdb-4e28-3ca8-b2a0-66193c2f077a | -9.52 | -60.5421 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bee104ee-5e47-32e5-8ed4-f6bbec23aa05 | -9.227 | -60.33317 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9403d046-d4be-3723-a670-d437ab22d73d | -9.52924 | -60.55729 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18833402-fc69-3004-a3c3-e5b588739fa1 | -9.1846 | -59.63492 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d747acb5-d99d-3f0e-95e0-a1544aad62b6 | -7.05795 | -59.82383 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a6dbcb6-c6a7-38d1-92be-cffa4c1a2eb6 | -9.59504 | -55.3526 | 2025-08-22 05:38:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12e83e13-39db-3fec-a233-4477631c866e | -9.0615 | -63.93245 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e25a9fb-0288-3c89-a910-b82dd2c29c1a | -8.87105 | -62.39999 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed86b478-e048-32d3-aa45-93ab07363464 | -8.46871 | -70.08711 | 2025-08-22 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e606dcc-ebdf-3109-86b5-b7e8a39f4d26 | -8.54436 | -66.94907 | 2025-08-22 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 847632b9-376a-368f-b4e3-b8e4067d593c | -8.88812 | -62.40265 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37f84a69-82ef-34d1-842b-f029e53480bb | -9.21104 | -59.78242 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff66c67c-cfef-3f35-bfbf-121246d5cc72 | -4.8861 | -55.9851 | 2025-08-22 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9993a2c-0547-3622-ad88-d3690c255bc6 | -6.44123 | -53.39041 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 046aec35-9fbb-3000-aa3e-13b25795d4b7 | -7.44349 | -60.62813 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a73f11ad-c892-3ca6-8c68-d9c592a9eebd | -9.10491 | -61.43456 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0244542-d1b3-33f2-8e1f-b4accaec6667 | -9.59461 | -55.35588 | 2025-08-22 05:38:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a60455b8-4384-3e04-8ac9-9a260d7ce664 | -11.03876 | -59.17118 | 2025-08-22 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48947e9a-532c-389c-a306-3fcbd4885779 | -5.87654 | -53.62077 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd9d6976-bcc9-3d07-bc8a-4b4e22832a4d | -5.81057 | -59.21095 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5610035d-6a40-34f2-b191-d4dda2aff6c7 | -8.88776 | -62.42458 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdc627ff-0665-39ce-b200-0effb0d43be5 | -5.43594 | -60.16503 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2bcdff84-ef74-393c-af26-bb4c0e20cfba | -8.86136 | -62.41742 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7a95a4d-d832-30cd-9693-645d31236213 | -9.51122 | -60.54995 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b8d67b4-59b1-36b3-b4ed-4df884dd2baf | -10.09927 | -68.96057 | 2025-08-22 05:38:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 320ad1de-a76e-3d65-9ddd-ac6511324096 | -9.52617 | -60.55222 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0004770a-fdee-375f-b24e-e773c26f0011 | -5.88004 | -53.61589 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6237e449-7c84-3629-b236-d35aa9c1b289 | -6.57306 | -59.87489 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70b6f520-2bc8-309e-b0f1-cff48c7bee0f | -9.51578 | -60.51849 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aad68883-a8c8-3960-82cc-46c966953fd1 | -11.90318 | -55.89568 | 2025-08-22 05:38:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a95ebe74-2642-3c78-863c-123904747502 | -8.60364 | -62.61807 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bd51a44-e6ce-3ce7-8426-26f49bbc532c | -5.88307 | -53.63548 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d564d153-0952-3b23-ab8a-585bc90ca1d8 | -9.27727 | -60.78019 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33d0f4b4-fae4-373a-8e10-905b5cf90d1e | -9.6568 | -59.64708 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78c55edc-5874-3b57-80d2-e6fab2565fb9 | -11.03824 | -59.17496 | 2025-08-22 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94fd3b0b-c3fa-3d2a-9217-a6647dd0a946 | -9.18385 | -59.63995 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README54.md)
