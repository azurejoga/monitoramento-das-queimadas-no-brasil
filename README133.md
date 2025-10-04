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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2feea304-37b3-310b-bb35-e47f12ee963b | -14.89398 | -48.33859 | 2025-10-04 05:38:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7b20c696-fe0b-309f-94ba-e4580706be24 | -15.79276 | -46.25578 | 2025-10-04 05:38:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a920e560-86e4-39f4-858c-87dfaaba9aa1 | -17.08125 | -46.23802 | 2025-10-04 05:38:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9a8b5364-bdaa-300e-8ed1-edeed320d265 | -21.19406 | -45.14456 | 2025-10-04 05:38:00 | AQUA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| ef0d05fc-4b7e-3d1c-a779-d8701277666b | -21.71853 | -50.74568 | 2025-10-04 05:38:00 | AQUA_M-M | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 43.2 |
| 4d1e1e70-8595-398d-91c5-94fa10a938cc | -14.9281 | -46.86467 | 2025-10-04 05:38:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 46c9471a-dffc-3264-bbc6-0c2c48c08e5c | -20.13252 | -44.00205 | 2025-10-04 05:38:00 | AQUA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 5a119516-6709-353a-80f5-4a946021f09e | 4.56294 | -60.64804 | 2025-10-04 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97d6f703-2deb-3116-9d92-938cac6babd4 | 4.56358 | -60.65189 | 2025-10-04 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87bb23d6-49a4-380f-8ed5-91897e11f72d | -9.4545 | -56.65868 | 2025-10-04 05:53:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5a2d0b6-b658-3938-8526-83c5c25dffb3 | -9.45394 | -56.654 | 2025-10-04 05:53:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea004b03-f02e-39f8-bc92-b59efab2ac32 | -10.04861 | -62.46387 | 2025-10-04 05:53:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 082fc58b-8b49-34e4-b575-64d0b9528a70 | -10.09792 | -67.23138 | 2025-10-04 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dde38fd-4940-3260-ae73-2604f80d8196 | -9.52815 | -68.29375 | 2025-10-04 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 715939c8-0708-3571-8d66-99f7e75d69a9 | -10.05311 | -62.46453 | 2025-10-04 05:53:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37a1f6dd-65c6-3014-a42a-f08dbd1ee7f6 | -11.12772 | -55.45383 | 2025-10-04 05:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7acd3769-7381-3419-b870-0cb0e859f583 | -9.92773 | -62.22281 | 2025-10-04 05:53:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af2f37dd-801b-312b-a4d5-6a05c1aaf24a | -9.37005 | -67.91315 | 2025-10-04 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58f6812c-4848-3515-a1ec-a29286b6d0e3 | -8.62219 | -54.9663 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b60f74d8-67a8-3bf8-a14b-5f049bf6ca4c | -8.62494 | -55.0019 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bdce25b7-99b1-36a4-b248-266c40e79e97 | -9.45519 | -56.65317 | 2025-10-04 05:53:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c10b25aa-3c81-3d14-ba3f-4b67158982d5 | -10.82965 | -57.17785 | 2025-10-04 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ede7c7f8-a3f0-3f65-837d-949f6f8bba68 | -9.45328 | -56.6595 | 2025-10-04 05:53:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccd5b48d-2815-3871-b6ec-0513f99add74 | -8.62171 | -54.99428 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a20d1818-0bb7-3edc-aa42-efd29d634b00 | -8.61622 | -54.97951 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a35a9b5c-9418-39e6-a6c3-39f0ace89505 | -9.14613 | -62.37138 | 2025-10-04 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9caedda-20ca-3e18-bcce-c6a146b7156f | -11.12689 | -55.46116 | 2025-10-04 05:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8feca1f6-f44b-3947-9662-47241255b194 | -9.19385 | -59.55514 | 2025-10-04 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d4c130e-3c37-30ed-b707-19cb9ae3d760 | -8.62808 | -55.00168 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 927cb82a-d39c-3ee8-8de2-d42a898fe62a | -8.61948 | -54.98765 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09f040e2-5c43-3ab3-acc5-2cd935701d9d | -9.44792 | -56.65804 | 2025-10-04 05:53:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5661c5e0-c2aa-3a6e-adcc-7dd0571d4ece | -8.6141 | -54.97273 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49fed390-78e6-31ca-847b-ace554c33e22 | -9.31052 | -61.84409 | 2025-10-04 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c2d2b03-37b1-320f-9bc9-8c62b2a950d1 | -9.22397 | -61.82938 | 2025-10-04 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a65fab0c-26a0-35fa-aed3-2981970f9890 | -8.62008 | -55.00775 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f21f692-550e-3e3f-855f-5413089f4aec | -9.66473 | -62.39441 | 2025-10-04 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57778cbd-0c67-32ef-8f6e-20ac2edda7a1 | -9.53093 | -68.29781 | 2025-10-04 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6af807a-7f3f-3cbb-82ed-6f4699a45a38 | -9.99772 | -60.01397 | 2025-10-04 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97569168-7516-3bc9-b23d-759586ed5ad5 | -9.92512 | -60.19543 | 2025-10-04 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0124d346-d000-3aa8-bc4a-02562fbecd88 | -8.62578 | -54.99522 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8396cf1e-cf63-3449-9b13-f4a452abae9c | -8.62724 | -55.0086 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa92eee6-17e5-32ce-b113-652ecae58636 | -9.19017 | -59.55535 | 2025-10-04 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ae30262-0a2d-392d-853a-8d7de5d88ee1 | -9.99618 | -60.0147 | 2025-10-04 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b549c776-8f4d-3f32-9f79-aba57b7bf711 | -8.1081 | -55.07992 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f637567e-7f86-31c7-9c55-5d72bc859061 | -8.60991 | -54.9715 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcb39037-2b0d-32fa-9cef-c2bbc629da30 | -9.86123 | -60.27359 | 2025-10-04 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31a3639a-bbe3-3dc5-b759-2bc5d5be59a4 | -8.61862 | -54.99446 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 530f3139-fb3b-3269-8db6-f1a5a33bf1a5 | -8.63297 | -54.99584 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2af0b62b-95a9-3a41-af64-7a853c2c7325 | -9.02024 | -63.58946 | 2025-10-04 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3527af8e-80f7-354c-aaf0-c34d677ff85e | -8.61793 | -54.96527 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a474adb-f994-3f8f-8d0e-11cd12613196 | -8.62254 | -54.98739 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a27edb8-57fc-3f05-80a7-b120bb225873 | -9.71244 | -67.46592 | 2025-10-04 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce0d16c4-ee0a-3314-b05f-a17dbea1da04 | -9.70905 | -67.46539 | 2025-10-04 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0cc6324-64ac-39c9-bf85-6f801bdaada9 | -8.6289 | -54.99492 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab0722d5-df8c-32c3-9e66-4e3fa6e0089f | -8.61499 | -54.96568 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf6f6958-b9b5-3374-af84-840ee3e84871 | -9.667 | -62.39304 | 2025-10-04 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a582b22-e635-3fdd-a2c1-bfcf9188a33d | -8.6213 | -54.97333 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5f7464b-b3db-3ae0-a645-4ce2baed310d | -8.10724 | -55.08679 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cad2ab5d-2a8d-3efd-9fa3-d66d9517379b | -9.92555 | -60.19218 | 2025-10-04 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3331892-7c13-3f87-a6ea-eb6a1c4dde12 | -8.60907 | -54.97851 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69d48af2-7868-3226-8efd-b1660a682359 | -10.09848 | -67.22763 | 2025-10-04 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1f909b1-1a63-3619-9a5d-5af05f45e578 | -9.99576 | -60.01803 | 2025-10-04 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c081f294-7d7f-34d2-94e5-3c75b68cab28 | -9.31168 | -61.84667 | 2025-10-04 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4795c900-2335-3930-b960-f30247757c6a | -9.19062 | -59.55185 | 2025-10-04 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14f3c2b4-e99d-3a0f-aa81-e33f4951ec1b | -8.6234 | -54.98025 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d20f260-c356-3d10-8174-75b840d897c9 | -9.22594 | -61.82774 | 2025-10-04 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bb9f3f7-23a4-3376-bfc8-a56005719d22 | -9.19562 | -59.55598 | 2025-10-04 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9144f28-cbac-3ed3-b14b-25a54acc705f | -8.01116 | -70.5815 | 2025-10-04 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb8ad435-b1bb-37cf-b362-3031edb48bd7 | -9.01612 | -63.58887 | 2025-10-04 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fecec22f-2dff-337b-8af1-ce0beecbd970 | -10.83357 | -57.19991 | 2025-10-04 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62755081-a87e-3c82-ba76-23269a88f747 | -8.62091 | -55.00094 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2956c031-f298-3af4-88db-47cfbaf977a9 | -9.1884 | -59.55453 | 2025-10-04 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e824d8ec-e733-390b-bbe3-3d396c7b3640 | -8.62667 | -54.9883 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| baa4e9e5-12fd-3742-aacf-829890d75d73 | -9.22862 | -61.83003 | 2025-10-04 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4664a9ac-a957-3b53-a6d4-e6efe53d367d | -9.14338 | -62.37314 | 2025-10-04 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 668523ce-b8b5-3a22-8228-453c6cffe68b | -10.05427 | -63.32358 | 2025-10-04 05:53:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 887022c8-7eff-34c1-90b1-df7499a4e9b0 | -9.99728 | -60.01728 | 2025-10-04 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 376fd51c-ee6d-3f36-8328-1fbb957b9553 | -9.63459 | -63.24259 | 2025-10-04 05:53:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2fcb454-2c9a-3d8c-af22-fdf53c1da021 | -8.6132 | -54.97981 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91b78251-aa43-3056-b3b2-813a614e2a3d | -10.83614 | -57.17841 | 2025-10-04 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27ae0ac5-32c2-324e-ab07-ace3ed5176f1 | -10.8271 | -57.19921 | 2025-10-04 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3f019d7-bc39-3e95-a13f-87461f2ee5ff | -8.71584 | -70.26318 | 2025-10-04 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97d81c72-e00f-3c0a-8742-21cd297a067d | -9.85601 | -60.27281 | 2025-10-04 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| afa718f6-52b3-30d2-8ecd-2314395b1687 | -8.62406 | -55.00879 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| edfc5443-d731-3f73-823a-c0d0342eaff7 | -8.62037 | -54.98063 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c648efe-9ab4-33e9-94ff-598cf20d8da2 | -10.0015 | -60.01547 | 2025-10-04 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e98e29d-7929-34c3-8f58-4949d07335db | -11.12608 | -55.46835 | 2025-10-04 05:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b2dc87d-9aa3-3edd-a745-2b8ad4a5144d | -10.00108 | -60.01876 | 2025-10-04 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eea029dd-05ba-370f-8af9-f3d77c348381 | -8.61708 | -54.97231 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 29045096-9d0f-32f0-9c5e-2410bc6ef8b6 | -10.83031 | -57.17236 | 2025-10-04 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b5128ea-1abf-3e88-9be6-8181c46e00e9 | -8.61075 | -54.9645 | 2025-10-04 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f84c38fb-9b51-302c-930e-e1bd5a971d1e | -3.58519 | -64.33808 | 2025-10-04 05:53:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a92408d4-5d63-3fb2-bd46-fe47364ddb3f | -10.6354 | -69.54694 | 2025-10-04 05:55:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f9bec06-0dd7-3a63-a781-c1f893d364f3 | -17.88786 | -57.63803 | 2025-10-04 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b477765c-ad9a-3af9-83f0-5b8e4da9153c | -10.84909 | -69.20456 | 2025-10-04 05:55:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 0228ea99-dc65-32d8-b59a-5b3e28a8ebab | -17.8883 | -57.63304 | 2025-10-04 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8c21910d-e4ba-3f69-a0ec-413ab4c0d22f | -8.10986 | -55.08566 | 2025-10-04 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a293679e-21cf-33a7-8b03-ef0146604192 | -6.93737 | -63.12132 | 2025-10-04 05:55:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02b717bf-60ef-3e9d-880d-d8bdd9ee1a3c | -8.10896 | -55.09253 | 2025-10-04 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3382f7c0-a626-3d0c-9344-7ac73628c3b7 | -6.93683 | -63.12502 | 2025-10-04 05:55:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README134.md)
