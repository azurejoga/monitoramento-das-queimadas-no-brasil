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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e5c50a9-8e16-3ce9-a4d9-db85ee76f19b | 1.06116 | -59.25161 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71638bea-6ed6-3348-b827-d5f767ab68ac | 0.08231 | -60.55745 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d45035d6-1d30-3ddb-bc9c-0461aa3756ab | 0.63112 | -60.56303 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56d295e9-d754-3d8b-90d0-176288fa8656 | 0.07527 | -60.54472 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f42dc45-b28b-3b66-b24e-8861a9cad6a9 | 1.13015 | -60.51655 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edca3e83-0392-3ead-aa8e-637ed106bc43 | 1.4896 | -59.91695 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 501951db-8e13-309e-8efe-2e097ec8debf | 0.05759 | -60.97388 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dd5a1fce-3be6-3e6a-8222-f53b357e238e | 0.87321 | -60.47236 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebdae63f-f5a2-31cd-a523-2fceefb738b7 | 0.49522 | -60.50906 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dfa7bc1a-a736-39b6-8f0d-b0282d1a1dbe | 1.51648 | -59.9302 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30966d0c-dd70-3c83-9764-f26770bb1b95 | 0.89213 | -59.78879 | 2026-03-03 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b721090-03dc-3807-acf3-b66c905f1215 | 0.49818 | -60.49707 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cb3a656-1a5e-3bc3-a9a6-ee443d53e753 | 0.08856 | -60.6272 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6c3980c-0cc9-377f-9ac0-222d19827ea3 | 1.49502 | -59.90902 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32693ad9-228f-35c0-b6cf-46a38069e402 | 1.50565 | -59.90727 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cb442fd-bb3b-3970-88d2-8030c106c3bd | -9.72198 | -60.20356 | 2026-03-03 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b6dbdec-111c-3799-8113-be35401960d6 | -9.51397 | -60.18809 | 2026-03-03 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d30f85d8-3838-329a-89a3-852d9901797e | -9.5134 | -60.1916 | 2026-03-03 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd86a846-22b1-3679-8782-d23438d705bd | -20.46591 | -55.04475 | 2026-03-03 05:27:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ea8dedf-b11d-3eee-809d-9cbf44af77c6 | -18.79496 | -57.64509 | 2026-03-03 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 81f8030d-aab1-3b24-9bf3-d2726f23fa49 | -20.80855 | -49.83334 | 2026-03-03 05:27:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c3ca654e-137f-3ce4-af58-3a3bf93b88b4 | -18.80075 | -57.63097 | 2026-03-03 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 0d84d497-01f5-3fc1-9864-c87740607db9 | -18.79114 | -57.64452 | 2026-03-03 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 225d1ef0-4cc1-39d4-862c-9d142c2c4621 | -20.80809 | -49.83884 | 2026-03-03 05:27:00 | NPP-375D | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d7177126-b19a-3b35-8e8f-a677592cfcc0 | -18.79693 | -57.63041 | 2026-03-03 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 39d19338-2339-3380-9167-3927148abbfe | -21.70171 | -48.4307 | 2026-03-03 05:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0038f7f4-6ca2-344d-b327-20814594df2b | -21.70579 | -48.43557 | 2026-03-03 05:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64fec90f-b4d4-3e90-b6b2-356b25095185 | -21.80122 | -52.72481 | 2026-03-03 05:29:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be811357-24d3-3e26-8599-c786717dd7bb | -21.69875 | -48.43535 | 2026-03-03 05:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd9bfb91-1c1b-30ec-b383-8655deebf76c | -21.80159 | -52.721 | 2026-03-03 05:29:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75e7d197-249c-35bd-9a61-b030ef86b2f2 | -25.21779 | -53.28465 | 2026-03-03 05:29:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0b2d19d8-4ff3-382f-b773-e0af8b571a2e | -21.80233 | -52.71331 | 2026-03-03 05:29:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5895be68-816a-3aff-8988-0436909990a3 | -21.80086 | -52.7286 | 2026-03-03 05:29:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3995b04-ba77-3573-b856-9fad18a4060a | -25.21745 | -53.28861 | 2026-03-03 05:29:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b4e83173-2c63-38a2-b9f3-7ec266c37bd0 | -21.7012 | -48.43748 | 2026-03-03 05:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 554bf84e-4c43-3650-934c-af1790561de2 | -21.80196 | -52.71716 | 2026-03-03 05:29:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8cd5a5f-947c-3908-899b-16e074d762c7 | -22.24644 | -56.75434 | 2026-03-03 05:29:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b7d7cf2-5976-3db1-8a55-9abe0771ccbc | -21.79689 | -52.71267 | 2026-03-03 05:29:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df4b0445-279c-3571-bab1-ec48507c3179 | 1.5047 | -59.9116 | 2026-03-03 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f7dee2fd-dd51-3815-a7df-36e4a389e749 | 1.5047 | -59.9116 | 2026-03-03 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d3486f2c-1b75-3cd9-8e05-5a818fadd78a | 4.64369 | -60.70274 | 2026-03-03 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4dcbd9c-5671-3796-8bba-ffe9660b22c9 | 4.64715 | -60.70224 | 2026-03-03 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ef93c6a-1759-3787-a842-f21adc863ad9 | 4.64657 | -60.69861 | 2026-03-03 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41d4ace3-7923-379a-b7ef-eef720c873ef | 4.64598 | -60.69499 | 2026-03-03 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 444e6ca1-ae7c-34e5-b5d6-ceec5c66412b | 0.08768 | -60.62857 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5165ec6f-e996-3c1d-803f-18ea89172244 | 2.86562 | -60.80962 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2710d990-e874-3c4a-9917-70c80ba3e626 | 0.77149 | -60.47863 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd91c085-1fe2-31f1-9d5b-782238f19621 | 3.15663 | -60.70259 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4db2df4b-6203-337f-a9d0-6777e4a7f1e4 | 2.88845 | -60.63398 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5a9125e-5c21-3fd2-a0c2-16764b23e19e | 1.00173 | -60.41681 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 907dcef1-5ee9-3a3a-b877-2d63654cfd9c | 1.35532 | -60.03234 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed2ba872-9708-36f4-89c8-fcdbe0795cb3 | 2.52508 | -60.98889 | 2026-03-03 05:42:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23245458-7b10-38b4-a0b0-347405e78ed6 | 0.93554 | -60.42595 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfa4e40c-53ae-34cc-b938-9f1fecc709b0 | 0.45842 | -60.39346 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3734f3db-d497-3e32-ace1-44d8c345b879 | 0.89267 | -59.78846 | 2026-03-03 05:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72579095-87c2-313a-9fac-397b416810d8 | 1.49037 | -59.91378 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4d35bcb2-998d-32fd-8a32-e26f2fe09c26 | 1.02498 | -60.53816 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfba601d-b16c-38a8-bf3a-f384264731e7 | 1.12319 | -60.51992 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c72279ad-c1b7-3a41-bc48-d9e0fffe478a | 0.49219 | -60.51085 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71465745-117c-3320-a833-79da0bf17114 | 2.64993 | -60.11418 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bd4594b-d9af-3cde-a70b-bf5ec07418db | 0.09497 | -60.62744 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0251a606-407e-36ce-9fa4-53238d6c99d8 | 1.45519 | -59.96743 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2fa12ac-d03f-3a65-8a72-357d6612fd8b | 0.63103 | -60.55962 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9348d9a4-e2f7-3354-b6a3-a1da8eadcd6d | 3.1525 | -60.69928 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 98427d3f-1b6f-369d-ae40-7916a9c45bac | 0.05991 | -60.97626 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c9535b79-ca57-34b1-b84c-67d84651927f | 1.11899 | -59.20111 | 2026-03-03 05:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23f13e77-3a33-392c-803f-e481b45d8b34 | 2.90833 | -60.62271 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 477b36de-fe1b-31a0-a046-a9f49a8229bb | 1.50296 | -59.92094 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2033497c-c7c4-36a0-8168-b8d5fb04155c | 1.13043 | -60.5188 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 343dc052-8070-3212-a6e1-56d3126a5e28 | 1.12614 | -60.5152 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c457392e-677f-3b7f-a35c-68879eb0c3e8 | 1.115 | -59.20293 | 2026-03-03 05:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9673f3df-164a-3ac4-98b8-705b4204b099 | 1.72063 | -60.29689 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44387e53-d03b-392a-8042-d1629d56fd80 | 1.51111 | -59.92426 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2722f3bf-34ae-34a7-9463-09606655f2fb | 1.86119 | -60.40077 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 258d014c-4e6a-3d34-9ac2-1f6134426a2e | 0.50044 | -60.49215 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 242bfb96-76b2-3c01-9caa-59639d29fa34 | 0.70002 | -59.97062 | 2026-03-03 05:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03e50bfc-7336-35c6-82bb-0a8b49f08c31 | 1.65156 | -60.24107 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba593464-297b-39ca-8f6b-a9b338c2a1fa | 3.23521 | -60.13613 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e0702dc8-6fbc-3206-af08-440183885de5 | 0.6317 | -60.56383 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ada31e3-9dd1-343f-918e-ca53b1c1deba | 4.27378 | -59.90422 | 2026-03-03 05:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 521af9ad-52c8-3aeb-a549-0fe89cbd3983 | 3.17067 | -60.70052 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bb52a70-01b4-3a35-a2ea-7856ad9fbb50 | -0.15574 | -60.74873 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a35a30bc-3182-3752-ac8b-7bfe0973413c | 0.77082 | -60.47438 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9576984e-7cc9-305b-b1c8-20c503915a34 | 1.86841 | -60.39963 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cd7693f-eeab-33fc-baf5-228e723462e1 | 0.92193 | -60.52748 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 230f7ab7-6722-37b0-b33f-e2021efcb307 | 3.37173 | -60.43896 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0878ad8-827f-36c5-8fc2-bd1ac3c8f4f0 | 0.0943 | -60.62321 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf67912b-6ba6-3111-afd4-0f485d818c63 | 0.46209 | -60.39288 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a38ba46a-c735-3be4-9012-43264015a4ec | 1.48594 | -59.90994 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5efcedff-6769-3022-beb8-ab8958dcf1a5 | 3.11826 | -60.48578 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 605c41b5-8727-3972-9032-915d04997aac | 1.71693 | -60.30029 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6092e5e4-fce8-3402-95c0-f72172cd5603 | 2.86686 | -60.81741 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a02c9671-481c-3b92-9328-152865100016 | 0.49584 | -60.51029 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 967a37e8-0d71-31a3-84f2-d4c1f399553a | 1.12975 | -60.51463 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f8ed377-8dfe-3cb2-8acd-06de21e3683e | 0.87484 | -60.46868 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2919690-1e41-33b5-ad5e-5f5a2492a3a5 | 3.16795 | -59.90875 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96af5dce-3194-32b6-8ef1-7cd27070bd8a | 1.51251 | -59.93302 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44fb8adc-7c1a-3d8f-9a20-0792326046ad | 1.97529 | -60.70061 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ec6caa5-071a-3082-8131-51b61bc392c6 | 1.48808 | -59.92329 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47182671-bee6-391b-8d03-a51cf84ee4ec | 2.88781 | -60.63002 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README9.md)
