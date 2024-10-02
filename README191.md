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

## Dados Diários - Página 191

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1dcc286-b9b9-3b7b-92f6-695578f1d9b4 | -11.65792 | -64.01855 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cf58864-d682-3955-80e7-ecbc9615e7b7 | -11.65466 | -64.06165 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ec03064-d5aa-3203-8bdd-4588d76e5fd7 | -11.6546 | -64.01799 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b85b5a3-3232-38d4-bceb-88a65037cc05 | -11.65405 | -64.02155 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50908634-e439-3019-ba4f-da08925dc8af | -11.65129 | -64.0174 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66a8de17-5007-3c68-b527-688d6a01f80a | -11.63302 | -64.02534 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5639a56d-7266-31f0-9c3d-05166f052d9e | -11.62692 | -64.02073 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b342c53d-fd28-38b3-8d5b-45f48e49eb32 | -11.62598 | -64.11499 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7377fed8-a09e-3bfb-9887-f6ba275afc6c | -11.62262 | -64.0927 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa08d6ee-6ba3-3981-a625-44d0b3b314d1 | -11.61958 | -63.95767 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9107ddbd-de71-3947-9b43-c9a598569762 | -11.6187 | -64.07394 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0425786b-19bc-333f-83a4-d5460f41d635 | -11.61816 | -64.07748 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e1c49e3-3bdf-3f8d-a423-c82fc5027ddb | -11.61646 | -63.67147 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdc392b7-b5ec-3426-a116-a52a9b1330ad | -11.61401 | -63.9495 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf096905-3f12-3b5a-b220-f43594105a89 | -11.61237 | -63.96016 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 610734b3-cd33-35d0-968b-60c9bc721e09 | -11.60809 | -63.68127 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d68095a6-66c5-3aad-a9dc-f58543c47173 | -11.78066 | -64.27739 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d44900b-7235-3b3b-a3ca-3ce909e16d8d | -11.78011 | -64.28092 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a08ee12e-6b80-3305-aa89-285ca4eb59a3 | -11.77734 | -64.27686 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00a61a5f-e947-3555-ab92-868dad32b732 | -11.77566 | -64.26574 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28cc92d9-30c2-3b7d-942c-7bb8a093f396 | -11.77503 | -64.2258 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e807f30f-b494-3881-81d3-9f004b01466e | -11.77456 | -64.2728 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7372bb4e-5cff-3fad-95d1-aadbe0e3af23 | -11.77448 | -64.22934 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cae666c9-9066-3485-9b9b-3639d46590eb | -18.89437 | -54.50859 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 579390d0-9ff9-38cd-bc3e-fa47c3a8a0fb | -18.89382 | -54.51424 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08756fdc-f8ab-381e-b637-cfc334795eab | -18.89235 | -54.50695 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 119b51ad-d3da-3727-b7e7-2beb3f1defbe | -18.89185 | -54.51255 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc73b48e-99e5-32fe-a367-dcd435dd5248 | -18.89136 | -54.51799 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25e2d912-6355-304a-a84e-c55ab57d9bb1 | -18.88814 | -54.50776 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2302982f-1e02-3cca-b04a-176fe2fde414 | -18.8871 | -54.51862 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f6e14700-bfc1-3502-8e5e-e54145ebd866 | -18.88657 | -54.52408 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4ec88f3f-5331-3719-857d-7ca808a49589 | -18.88609 | -54.50637 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc9816cf-1a4d-3778-8b2a-e22da3b59951 | -18.88511 | -54.51738 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ce256cf-548b-3773-9ef9-00cb3813a344 | -18.88463 | -54.52286 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da6ffa07-43a1-37d2-ae11-91d30d717ce3 | -18.88075 | -54.51901 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8bebf54d-e062-3f88-80cf-c0bf849d53f8 | -18.87879 | -54.5176 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fd4d0cb-5fa1-3855-a5bb-ee2a4c178628 | -18.87721 | -54.48996 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1bb14446-a3ac-3c36-8135-a8dfa7b23e79 | -18.87508 | -54.48819 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0d1f3581-a193-32c0-a9d9-0362563a59a9 | -18.87463 | -54.49324 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dcc10335-83af-3c21-a943-ad39e48aaa03 | -18.87103 | -54.48859 | 2024-10-02 05:38:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82de3475-eaca-392e-a973-46eb9e679976 | -18.81 | -54.48604 | 2024-10-02 05:38:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e617734-59e7-3830-911b-f464a5879a8a | -18.80882 | -54.47856 | 2024-10-02 05:38:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e7c1345-b179-36d4-bd94-7abb40d46f0b | -18.80835 | -54.48373 | 2024-10-02 05:38:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2f7aefd-d148-3a2d-987d-4a201e806a45 | -18.80789 | -54.48881 | 2024-10-02 05:38:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aae5dc68-b69c-3b9c-b41f-3520c2e345b2 | -18.80469 | -54.47574 | 2024-10-02 05:38:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c74a1883-52a5-359d-afd0-e6f4c744ad45 | -18.80417 | -54.48101 | 2024-10-02 05:38:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49ba2267-4673-3871-a93e-1ca817df35ec | -18.80368 | -54.48613 | 2024-10-02 05:38:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d25aa789-c998-3430-ba97-2a9064c2836b | -18.80205 | -54.48369 | 2024-10-02 05:38:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 755f7e7d-a5b1-346c-8c40-b23f2717c57a | -20.013 | -55.46646 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc9398fc-c310-394b-af16-73f3f4a386cd | -20.00702 | -55.46599 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe31a566-f03d-3f21-be0c-3b3f2f55549e | -20.00108 | -55.46506 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d93aa66-d892-3b9b-96bf-c2e8b1f97492 | -20.00063 | -55.47002 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8375b360-c74a-344f-96a4-864e06f2a6ad | -19.98234 | -55.47246 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 41466ae0-81a7-3829-8ac6-7396a0455e8d | -19.98189 | -55.47742 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fb5bbe57-2f93-39c0-90c7-7ad45503895c | -19.97889 | -55.47367 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0f0dae37-037d-3a00-9a49-1d7a94819621 | -19.97839 | -55.47869 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cc343f54-d29a-3f8a-a923-afca4c59284d | -19.97594 | -55.4766 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cda03ff7-23ad-3a0e-9d7a-246e791da477 | -19.96564 | -55.48613 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20d9ec2b-0c97-3989-8894-32594062ca57 | -19.96524 | -55.4902 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02e21463-c039-3858-b911-5db82c33daa9 | -19.96488 | -55.49398 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0270274e-8251-3b41-962e-a55fdd012387 | -19.96286 | -55.48821 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1beba569-9651-3b9b-94eb-8df9f7be4ff6 | -19.96251 | -55.49216 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b541cf8a-73dd-377b-97b9-a92693c890d6 | -19.96215 | -55.49614 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29bca53e-1180-39bb-8c47-542471bba067 | -21.35693 | -55.6901 | 2024-10-02 05:38:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a98a56ff-cfec-3452-b69f-85a8b7cd625a | -21.35654 | -55.69452 | 2024-10-02 05:38:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 03e8ba2a-6c3e-3c20-815f-0fe0ccb81fd2 | -21.35134 | -55.68515 | 2024-10-02 05:38:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3326f186-bb65-389a-8826-8f8485b8e5ed | -21.35093 | -55.68985 | 2024-10-02 05:38:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 172203ca-144e-3370-9847-fd253e5937a8 | -21.35055 | -55.69419 | 2024-10-02 05:38:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2b80d653-4c72-38a8-a5d9-60d331c272f8 | -21.34494 | -55.68946 | 2024-10-02 05:38:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b580ae37-f993-3e43-ba05-0a469a2b235f | -21.34456 | -55.6938 | 2024-10-02 05:38:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b6d60456-0dfd-30e0-b10b-1a59054bfb84 | -21.33825 | -55.69703 | 2024-10-02 05:38:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 347b7557-f943-3f84-9f65-4d3368e844d2 | -20.04769 | -55.96894 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 907fafc5-7745-3676-ad32-d0f49f9365df | -20.04729 | -55.97319 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b171710e-0622-3b3d-9a31-c52f8309ec4d | -20.0419 | -55.96829 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d09988c2-a8c0-3f3a-bad0-e4bd28e37951 | -20.0415 | -55.97255 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6c34a500-08ae-3cb1-b408-c0ad6106a615 | -20.03612 | -55.96766 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 46a20c02-4e26-3cd4-8a22-f66b57aa6320 | -20.03572 | -55.9719 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1aff2d54-5c65-35ed-99e6-4d52c838ddeb | -20.03563 | -55.96951 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ffdbca01-982c-3779-bf24-a12f5b25c951 | -20.03532 | -55.97616 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3755463b-5a04-3928-8218-b198115e63ba | -20.03478 | -55.978 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d355f6f7-7376-3b0e-8a1e-2c8088633830 | -20.03453 | -55.98466 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 058beb92-285a-3175-94e2-8b9c519e5a03 | -20.02994 | -55.97126 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1dc3cd20-2b12-3dd8-a6dd-a8803d2c5263 | -20.02942 | -55.97313 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1adb8396-7fc7-35fc-867e-3d4a10748b45 | -20.02915 | -55.97977 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 915b774c-684b-36e0-92e6-e61bd3b2b8da | -19.65492 | -56.47394 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3620e317-15a1-3ffe-9430-382daf132996 | -19.65384 | -56.47372 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b116fa03-6d98-3abd-9a63-089d8638916e | -19.65347 | -56.4776 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6d0c2307-4f5d-34e5-a859-e49924d187a5 | -19.64935 | -56.47331 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| df58a3e8-3508-3b00-8dc1-58ed028ab120 | -19.64894 | -56.47719 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2e0c4af8-5f6c-3f76-8942-4e7f0ea4cb95 | -19.63976 | -56.5659 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e5216e10-aa29-3148-8095-28237303a1ee | -19.63933 | -56.5658 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7e9bcbe8-1031-3b6a-a7fb-fc66a7ac71c6 | -19.587 | -56.53285 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 5b924688-b4b2-380a-8236-fb57ceea6783 | -19.58145 | -56.5322 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5c777066-e39a-3204-95c2-901b4256548f | -19.57552 | -56.53542 | 2024-10-02 05:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d662d74f-7772-3fd3-bad5-ae7ef95209e4 | -21.42411 | -57.24545 | 2024-10-02 05:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b9884f5-acfa-3fc2-af9d-ae25350083c1 | -21.41833 | -57.24858 | 2024-10-02 05:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc793338-f45b-39ce-9f09-f560c9fd3481 | -21.41288 | -57.24819 | 2024-10-02 05:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0e2a55b-f4cd-3876-aff4-83720414072c | -19.1097 | -57.49773 | 2024-10-02 05:38:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 29ed9cd4-b76d-3d2f-84eb-377b0970fb8d | -19.10915 | -57.50273 | 2024-10-02 05:38:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 68f01a03-b09a-3094-9a32-94412c9e9859 | -19.10887 | -57.50529 | 2024-10-02 05:38:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |


[Clique aqui para ver as próximas entradas](README192.md)
