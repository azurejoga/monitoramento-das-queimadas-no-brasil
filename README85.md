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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0cb5089-e4e1-35ed-af9e-f072d510d5c3 | -3.5406 | -48.1889 | 2026-08-21 06:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 14baf0d6-fd10-34ba-b523-791a4699c6cf | -7.3603 | -45.8136 | 2026-08-21 06:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 54dd8c6f-0cb8-32af-aa94-b27ae5fb4601 | -6.2341 | -55.6109 | 2026-08-21 06:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9bfcc44c-f21c-348b-bb4f-87ce1e8df835 | -9.4072 | -60.3977 | 2026-08-21 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 155a9aa9-cbaa-3859-b8f9-44b4505c61b1 | -14.3149 | -51.8969 | 2026-08-21 06:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 3113f84e-acc2-3efe-8357-2a1162ee0e79 | -14.3149 | -51.8969 | 2026-08-21 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 12c59e62-3494-3883-9d13-1a3b8746a5ee | -9.4072 | -60.3977 | 2026-08-21 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 1eee41a4-3f87-3d5f-b7d6-a657f4d201aa | -13.3926 | -54.3758 | 2026-08-21 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.2 |
| b738d6e7-36e4-3f51-bcd6-9df6fe82ec17 | -13.3923 | -54.3965 | 2026-08-21 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ecc0571e-0322-3d09-96f3-246087fca311 | -9.4071 | -60.417 | 2026-08-21 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 229.1 |
| cf3c4680-ed19-3a46-b7ef-620c44cb6848 | -13.7384 | -51.8438 | 2026-08-21 06:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| e7373bfa-4324-3f68-8210-27d1cd86a768 | -6.2341 | -55.6109 | 2026-08-21 06:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 0e8d2cb1-fbaa-3ac5-9eb1-dea3023fc605 | -9.4257 | -60.416 | 2026-08-21 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 7ecc8b8a-65a5-3235-913d-c45c4bad5a0d | -7.3603 | -45.8136 | 2026-08-21 06:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| bf723956-a898-3c00-8237-4d60326102e2 | -9.3885 | -60.4179 | 2026-08-21 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 888b8d01-05b0-36a0-9314-50c09f70d24f | -6.8755 | -59.4364 | 2026-08-21 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7c54fb98-9b2f-3724-9f82-b1ca4ac1baf5 | -9.4069 | -60.4362 | 2026-08-21 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 81363c20-747f-33bb-9a15-e903e3c480c6 | -11.1747 | -54.0216 | 2026-08-21 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 99799f70-6508-3daa-ac2f-8f08ca3936c2 | -7.3791 | -45.8119 | 2026-08-21 06:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 499c1d3f-e3dd-3375-b6f3-fbbac06de7d5 | -13.738 | -51.8651 | 2026-08-21 06:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 4825c172-1132-3d37-8fc1-4d95c8aa98b1 | -13.3734 | -54.3779 | 2026-08-21 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 6f514ff7-347c-31a3-92bb-dc7bdc93b372 | -6.2155 | -55.6316 | 2026-08-21 06:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 83fa0203-b1ce-3352-bd0c-b1bd058fdf18 | -6.2156 | -55.6118 | 2026-08-21 06:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 20bb4a37-5b03-36a3-87ed-b94ac58965e1 | -13.7384 | -51.8438 | 2026-08-21 06:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c73b9f10-37f2-3816-a9b3-582e8cd5c93e | -9.4069 | -60.4362 | 2026-08-21 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| bf80ab89-8273-3571-ade7-eee4e9ee01d0 | -9.4072 | -60.3977 | 2026-08-21 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 69ae49bc-fce6-3a9f-9ed7-e54bd94c34b3 | -6.1177 | -59.9069 | 2026-08-21 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1399a65c-c7ff-3647-a8ac-3c2f37d7682c | -9.4071 | -60.417 | 2026-08-21 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 219.0 |
| 6fe34a5c-bef1-3cc8-a335-dd2832249e13 | -13.738 | -51.8651 | 2026-08-21 06:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 73742d9c-a862-35df-ab81-54034ee8f35b | -9.4257 | -60.416 | 2026-08-21 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| a98d343a-d470-3268-81c6-956a6e414a58 | -13.3734 | -54.3779 | 2026-08-21 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 72916d2a-8ab9-35d2-8c4a-5140b543fd59 | -3.5406 | -48.1889 | 2026-08-21 06:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 873c31a0-2270-358c-8ac0-fbd46dcff5f9 | -13.3926 | -54.3758 | 2026-08-21 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| a866eaac-d959-3d6d-ab44-e126962261b5 | -7.3603 | -45.8136 | 2026-08-21 06:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c68423f6-843a-3129-8810-dae6537012a1 | -6.8755 | -59.4364 | 2026-08-21 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| ea3eeecf-7323-3c93-aac8-0d5a2a95f53f | -6.2341 | -55.6109 | 2026-08-21 06:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 425b5c68-2f5f-3479-beed-7884c1d55852 | -11.1747 | -54.0216 | 2026-08-21 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 6b9f375a-ba5f-3144-a190-5fdbf54cc5a0 | -7.3791 | -45.8119 | 2026-08-21 06:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b4085197-bbfc-35a7-a8bc-2b404bd694fd | -9.4069 | -60.4362 | 2026-08-21 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| b4812141-b343-35ca-a1d5-0b4dabe11113 | -9.4072 | -60.3977 | 2026-08-21 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 546f4eb7-326a-395a-88ef-25cd631522cc | -6.8755 | -59.4364 | 2026-08-21 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 83b4ff21-7010-37e3-818f-c9c117ef711f | -7.3791 | -45.8119 | 2026-08-21 06:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ce8a3779-2da9-349c-b4cb-776a3ad167a6 | -22.1805 | -48.743 | 2026-08-21 06:30:00 | GOES-19 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.0 |
| 71af90f2-70d1-3b46-bd28-9c3ce162ed06 | -13.3926 | -54.3758 | 2026-08-21 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| b02ac5e1-aaa9-3ea1-b14e-1a729b3f6355 | -9.4257 | -60.416 | 2026-08-21 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ac1db835-7411-30c9-b868-69682c3e465e | -9.4071 | -60.417 | 2026-08-21 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 234.8 |
| afa55fff-141d-3296-9494-8b8f69b71cea | -11.1747 | -54.0216 | 2026-08-21 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 999c3bf4-c7b6-304d-8a5d-6a900dcde61a | -6.2341 | -55.6109 | 2026-08-21 06:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 61dc2916-21d6-379e-844f-bca59427681a | -7.3603 | -45.8136 | 2026-08-21 06:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 06a2a5f6-c10d-3c55-ab58-e858e8a4cb32 | -13.3734 | -54.3779 | 2026-08-21 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| fdf72948-4d07-3213-aa74-33e7c29d0a62 | -9.4071 | -60.417 | 2026-08-21 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 253.1 |
| dd44a5cd-ae01-33b3-bb48-11adcde1e7fa | -9.4257 | -60.416 | 2026-08-21 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 0bdc5247-bddd-3a19-bf70-9e08e06410eb | -13.3926 | -54.3758 | 2026-08-21 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| d6cdd119-475e-3ce9-8c57-e7563a7c9d2b | -9.4069 | -60.4362 | 2026-08-21 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 7150e028-5d15-304a-a3a5-033091ad772e | -6.8755 | -59.4364 | 2026-08-21 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| aee63c07-b301-37c3-81ee-41645d8dfbe5 | -6.2341 | -55.6109 | 2026-08-21 06:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 5d0711ed-8920-3f4b-a124-ab5e26a27b6f | -7.3603 | -45.8136 | 2026-08-21 06:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 5f686c85-3a82-384c-94d1-b530c5074335 | -9.4072 | -60.3977 | 2026-08-21 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 8f723d0a-9273-3bea-915b-7582b35e4cf3 | -11.1747 | -54.0216 | 2026-08-21 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e9dc8e70-16fd-3a05-8eea-bf8d9a342cda | -13.3734 | -54.3779 | 2026-08-21 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 3815879d-ac3b-38bb-88d4-a2a64a19d8f5 | -7.3603 | -45.8136 | 2026-08-21 06:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 2b8625e2-3c4c-3e79-84f3-81d5262880d5 | -6.8755 | -59.4364 | 2026-08-21 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1a3de3e3-d6ee-3d68-9518-fb98d3e8e10f | -9.4071 | -60.417 | 2026-08-21 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 170.0 |
| fcbb381e-f6a0-3610-b583-dff75ba868c0 | -9.4069 | -60.4362 | 2026-08-21 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f61afdbf-60fa-38a5-8bcd-21e5472d5c7a | -14.3149 | -51.8969 | 2026-08-21 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 555146e5-3708-31d0-875e-9bf3deb9f391 | -13.432 | -51.7973 | 2026-08-21 06:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| b387545b-b548-3a08-b881-bb5c3d9ff0c0 | -6.2341 | -55.6109 | 2026-08-21 06:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a2313ae0-5958-37d3-b51d-4cc7fa44dca2 | -6.2156 | -55.6118 | 2026-08-21 06:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6b5ab4ae-a592-3103-8578-d1ed83330cdb | -9.4257 | -60.416 | 2026-08-21 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 9df797cc-96ac-3ec6-97f5-e739f1c6ed26 | -13.3926 | -54.3758 | 2026-08-21 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 745c29cf-485b-3416-9a04-86b3a43ac7de | -6.1177 | -59.9069 | 2026-08-21 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 4dace657-3ae0-3130-bedf-97ae2693811b | -9.4072 | -60.3977 | 2026-08-21 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b5c6d998-e9b1-3f70-912a-9502060a00fe | -9.4259 | -60.3967 | 2026-08-21 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 4b8ccd1f-1c6a-305c-b109-0b28f7594582 | -13.3734 | -54.3779 | 2026-08-21 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c4a596ca-6f7b-33bb-83bb-04f7daca43bf | -9.4072 | -60.3977 | 2026-08-21 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 8b2cad54-eddd-3580-927f-d7cd05a4c828 | -6.2341 | -55.6109 | 2026-08-21 07:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c51d607b-42e9-3bd8-a7de-7085e033f0be | -6.8755 | -59.4364 | 2026-08-21 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ea484260-90a1-32c9-81f7-0c5d90261c9c | -9.4069 | -60.4362 | 2026-08-21 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e582d0c0-33b9-3440-ac6b-1f0d263f9ac9 | -6.2155 | -55.6316 | 2026-08-21 07:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 543e807f-c628-32e4-bd58-a75557ff5f30 | -13.3926 | -54.3758 | 2026-08-21 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4d43e465-795e-3d8a-9e6c-1742acf646f3 | -10.7693 | -50.3162 | 2026-08-21 07:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| d889c66a-c9b6-391b-8cb2-776ba4ad05db | -14.3149 | -51.8969 | 2026-08-21 07:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 132d2f82-42c3-3f7b-a3ce-8024143a1e1c | -6.2156 | -55.6118 | 2026-08-21 07:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6723bc46-b07a-30db-9797-7ffe7e78fc2e | -9.4071 | -60.417 | 2026-08-21 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 421b684f-c9e6-3621-9075-7d16995c00bc | -7.3603 | -45.8136 | 2026-08-21 07:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| fae211f0-0e56-39bd-8c52-9e65c8485f83 | -9.4257 | -60.416 | 2026-08-21 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 77ac696a-f6e7-3a4a-84a9-deb845f4e287 | -13.3734 | -54.3779 | 2026-08-21 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 54127dcb-c44d-389b-82e3-f9756c0fdd94 | -3.26867 | -49.52291 | 2026-08-21 07:01:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 84d996de-8fd4-3767-8668-8a047000ae2e | -3.53768 | -48.17729 | 2026-08-21 07:01:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 4c342ca3-ee29-35a1-a8ee-0d94cb6892e4 | -7.00979 | -48.03694 | 2026-08-21 07:01:00 | AQUA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 30dcd1cc-537c-3cc1-aabb-5318a18a430a | -6.10961 | -53.06813 | 2026-08-21 07:01:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 71394e13-cb61-32ed-a21d-8e278ad26dd4 | -5.66853 | -51.64127 | 2026-08-21 07:01:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 65efeddf-ab73-396c-bc56-87626f91e044 | -4.93618 | -55.77486 | 2026-08-21 07:01:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5973e496-bb6a-3523-9298-de9d254fb5e0 | -7.34844 | -45.80295 | 2026-08-21 07:01:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 88d5a78d-c059-315d-88d6-0f1da5d4f5ea | -5.80763 | -55.71745 | 2026-08-21 07:01:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3f818a18-318d-3991-a56f-738d837537f8 | -7.0208 | -48.03829 | 2026-08-21 07:01:00 | AQUA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 0df38b02-d4a9-3cfc-b31a-c50b95401982 | -6.25593 | -48.64722 | 2026-08-21 07:01:00 | AQUA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 12fbc06a-c7db-34e9-a0d6-e35f8bcfd6ca | -6.86736 | -43.72559 | 2026-08-21 07:01:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 9fe517d9-f050-3a91-8bf7-dfb52a6ae3d3 | -11.20762 | -55.0475 | 2026-08-21 07:03:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6eca89c8-a7e3-33b5-ae85-aa801db2ac64 | -11.16563 | -54.00932 | 2026-08-21 07:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |


[Clique aqui para ver as próximas entradas](README86.md)
