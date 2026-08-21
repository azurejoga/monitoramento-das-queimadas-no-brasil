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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18bd3da2-f185-3cec-87fb-a65ae6a1bb11 | -9.4069 | -60.4362 | 2026-08-21 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 195.7 |
| 5d837ce7-101b-3e02-80b7-820d0d407001 | -9.4257 | -60.416 | 2026-08-21 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 1902c629-d1a6-3aa0-937d-8e3c3c19dca8 | -13.3734 | -54.3779 | 2026-08-21 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 5b063a85-9437-35f1-b159-7da2d4866621 | -9.4071 | -60.417 | 2026-08-21 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 373.6 |
| 4163b272-05a4-36a8-ac92-c88ff65ae8c5 | -13.3923 | -54.3965 | 2026-08-21 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 2338157b-7da2-3b56-8f5d-bcd7dbdf8bd9 | -11.1747 | -54.0216 | 2026-08-21 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 167.9 |
| 1ff3308c-7bff-3694-a7f4-1cf46dd0240f | -4.0481 | -50.2984 | 2026-08-21 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4f644800-74c2-3921-8398-c037c822e09a | -3.5406 | -48.1889 | 2026-08-21 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 5c696ee1-ee32-35d2-b190-e3d5d5da6f89 | -13.3926 | -54.3758 | 2026-08-21 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 591.1 |
| dc2834b9-ccfe-3f06-b6f9-19d042b905f7 | -3.5407 | -48.1673 | 2026-08-21 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 40884a25-8825-3fff-9005-f6b7771b6bc8 | -9.4069 | -60.4362 | 2026-08-21 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 145.9 |
| be393c70-d78b-33fb-816e-8283976cb89b | -6.2341 | -55.6109 | 2026-08-21 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 157.6 |
| b285b759-1958-3113-9292-b371c5e839cc | -9.3885 | -60.4179 | 2026-08-21 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ba377037-4e47-3bd7-af77-216450c4ccc0 | -6.1177 | -59.9069 | 2026-08-21 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 188d7045-d6db-30d6-94d8-c4fde38fae34 | -13.3737 | -54.3572 | 2026-08-21 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c963907a-3d25-3bf0-ac56-25d20a27d956 | -9.4256 | -60.4353 | 2026-08-21 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| bd7bb5df-c587-36c1-bb57-a92a8b0f1ef1 | -11.175 | -54.001 | 2026-08-21 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 971ed817-8356-352e-b784-90811eafdf5b | -9.4257 | -60.416 | 2026-08-21 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 143.9 |
| f05faf39-616b-32ce-94db-0b1c3f4ce70c | -13.3929 | -54.3551 | 2026-08-21 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 151.3 |
| ea8908db-902a-361c-9405-5fcaf49e6357 | -6.1361 | -59.9063 | 2026-08-21 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9726dbe3-e47b-36ed-bcf9-b665e4c53dcf | -13.3734 | -54.3779 | 2026-08-21 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 207.7 |
| c0225873-6a4e-33d4-ad3a-4263b2f910c5 | -11.1558 | -54.0233 | 2026-08-21 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| f37d63d6-0bde-3c6a-b3da-3f0adf76537a | -9.4072 | -60.3977 | 2026-08-21 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 6d11806e-593b-3f73-a198-9c37dd0502c4 | -6.2156 | -55.6118 | 2026-08-21 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 3c1a2412-b628-36a8-8955-1333b26f0197 | -9.4071 | -60.417 | 2026-08-21 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 316.9 |
| 31c520b1-4630-393d-a99e-954a0c905331 | -10.8166 | -51.0135 | 2026-08-21 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 1ae40021-eb1b-340c-b8d1-3a30d6ea71c9 | -13.4117 | -54.3737 | 2026-08-21 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 876476b4-6553-33b1-bfd3-cfc5877b2d6e | -10.8355 | -51.0116 | 2026-08-21 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 41b7b678-954b-3a13-bbc5-4609a5df200c | -13.3926 | -54.3758 | 2026-08-21 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 291.0 |
| f5da0963-21e3-3ba6-a282-1b23439dbcdb | -3.5406 | -48.1889 | 2026-08-21 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 27418a0f-19ef-3f5a-8bf4-3203590921a4 | -6.6938 | -58.942 | 2026-08-21 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 83a2e1e7-4cd5-3144-98bf-672a44ae3b80 | -13.3923 | -54.3965 | 2026-08-21 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 71b5c19b-ac0a-36d3-8e30-fa3f0c150015 | -9.4072 | -60.3977 | 2026-08-21 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8bdbdddf-15a8-3611-bad0-2067ca2b8fc8 | -9.4069 | -60.4362 | 2026-08-21 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 155.3 |
| c5aba744-6542-3eb3-8740-fd208e62f497 | -9.4071 | -60.417 | 2026-08-21 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 361.4 |
| f399a60b-88bd-3a02-84f1-f33fddc63953 | -9.4259 | -60.3967 | 2026-08-21 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 8dda876c-4889-36d9-b485-4a8e5d58babc | -13.4117 | -54.3737 | 2026-08-21 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b5c0fffe-a60e-34b2-b739-6b0ddcc6f44b | -6.2341 | -55.6109 | 2026-08-21 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 9de106e9-97da-3156-8a04-0ec23f3e21cd | -3.5407 | -48.1673 | 2026-08-21 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7aa575b5-d0c9-32d1-99b4-0eba5abde98c | -11.175 | -54.001 | 2026-08-21 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 4dde12c4-552b-36b5-9ed2-688b9c843df5 | -13.3737 | -54.3572 | 2026-08-21 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 920b521f-6a19-3ec7-9dd5-0aaa77466edd | -6.1361 | -59.9063 | 2026-08-21 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 630bdba1-53ef-3a7a-a80a-2dbfe71001d8 | -6.6939 | -58.9226 | 2026-08-21 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| aa844865-e95d-3d2a-b1d1-4ee0c77e8bea | -13.3929 | -54.3551 | 2026-08-21 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 59dd3fb2-1830-345a-b1ba-2b2dcb5b16c7 | -6.1177 | -59.9069 | 2026-08-21 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 124f70cb-6122-3ef0-b023-55fe6296c0e6 | -7.3415 | -45.8152 | 2026-08-21 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 14ff7956-1977-386e-9e64-1756610164de | -7.3791 | -45.8119 | 2026-08-21 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 264.0 |
| 129d8916-5f14-39c5-8996-e5e55a5d1edc | -9.4257 | -60.416 | 2026-08-21 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 85e2d402-09ca-3c46-b221-a0164995cc36 | -7.36 | -45.8361 | 2026-08-21 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6ab49a9b-ec9b-3b65-93c3-9a7d29b407c7 | -10.8355 | -51.0116 | 2026-08-21 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 5abf07e9-d24b-363b-92ad-e8c975cfd513 | -6.2155 | -55.6316 | 2026-08-21 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ae867b87-2b61-3bc2-af7b-938e971448ab | -10.8169 | -50.9923 | 2026-08-21 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 1667ab40-275e-39fe-8de0-1232d8e27264 | -7.3603 | -45.8136 | 2026-08-21 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 487.3 |
| 6203596f-d86e-3ae1-b859-0364972f1a3c | -13.3734 | -54.3779 | 2026-08-21 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 7077ae64-bf34-3009-b744-d6019dacc6e7 | -7.3793 | -45.7894 | 2026-08-21 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| d4bf09b7-19f9-3a64-a43a-04dedb09ec82 | -10.8166 | -51.0135 | 2026-08-21 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| f5ded8a6-9376-36c6-98e9-ec1887600ddb | -7.3605 | -45.791 | 2026-08-21 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 93d634e5-1ee7-3fc1-92b3-478f89db4e42 | -11.1558 | -54.0233 | 2026-08-21 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| fb9e3938-8c0e-3ac2-be04-88584296f535 | -6.2156 | -55.6118 | 2026-08-21 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| c25f1589-44b4-338e-a347-eb8fd049e76b | -11.1747 | -54.0216 | 2026-08-21 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.8 |
| ffe10dbd-b8c4-30bb-993f-e16a087f047f | -15.44528 | -41.38911 | 2026-08-21 03:08:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 7c1a1c8f-7191-33ee-912a-d3b08297cfd5 | -19.85818 | -41.08873 | 2026-08-21 03:08:00 | NOAA-21 | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 790d301b-c8b4-35de-bfe8-aa486b2c9251 | -19.85891 | -41.08733 | 2026-08-21 03:08:00 | NOAA-21 | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f175f13c-c832-3d4b-9bc7-71b882cec516 | -18.87796 | -42.02991 | 2026-08-21 03:08:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2f4cce92-be8b-30d9-bbcb-3becc386f37e | -18.87494 | -42.03352 | 2026-08-21 03:08:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8f36c146-6abb-3ae9-b049-ee5a9a24b275 | -18.87139 | -42.02846 | 2026-08-21 03:08:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 599fc687-e113-30b5-b85e-ac09804be01b | -15.4386 | -41.38735 | 2026-08-21 03:08:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 40f21073-cca7-37c6-b4b3-abf04fbe0818 | -18.87628 | -42.02785 | 2026-08-21 03:08:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c85c8117-6496-3f00-879c-3a379ab93e0d | -15.44045 | -41.38834 | 2026-08-21 03:08:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 71724112-c654-36df-ba1e-965a66623391 | -13.3734 | -54.3779 | 2026-08-21 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 208.7 |
| a5cad289-423c-3a78-9311-f817951f75b3 | -6.1177 | -59.9069 | 2026-08-21 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b4148cca-a2a8-323f-869e-ca83c844689f | -8.3718 | -62.697 | 2026-08-21 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c010a1dc-98e6-347b-8580-d8d8406adb7b | -10.8358 | -50.9903 | 2026-08-21 03:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 1bdaeb00-a2ca-3043-b535-7854c4cafc8a | -6.1361 | -59.9063 | 2026-08-21 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a526a49b-0741-3e32-a394-ebeb4a3e2815 | -9.4071 | -60.417 | 2026-08-21 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 338.5 |
| e4e1d557-c551-35fb-abed-3b8f44c1ced8 | -6.857 | -59.4371 | 2026-08-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 643320ec-8715-31ab-aa50-a09cc59c44ed | -3.5406 | -48.1889 | 2026-08-21 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 36bb6188-0d17-3840-b8e7-c721ec309d45 | -6.8755 | -59.4364 | 2026-08-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 09f75c0a-41d6-395f-9ee9-18de9d967566 | -13.3926 | -54.3758 | 2026-08-21 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 386.8 |
| ee1a54c8-8dbe-38d1-8854-3c611d21ea4e | -13.3923 | -54.3965 | 2026-08-21 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 46e6abd8-ab43-34f8-9b3f-b1cf22ee8eb9 | -8.3903 | -62.6963 | 2026-08-21 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 169.5 |
| 7d4d31bd-8b7f-372b-9c9b-7fef1f61f57d | -9.4257 | -60.416 | 2026-08-21 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 0dfae523-ad35-3ac6-9bb0-0a0419f1269f | -11.175 | -54.001 | 2026-08-21 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 239ca48d-1f0c-3103-be9e-01eb68de2cfc | -6.8388 | -59.3993 | 2026-08-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 0e7f656b-e269-3f6a-83c0-7e6cbfd85d65 | -6.8939 | -59.4356 | 2026-08-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 4d34094f-51d4-3fda-a420-e72f82308502 | -8.3902 | -62.7152 | 2026-08-21 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 83bdf43b-077e-3a9b-bc5c-96df1b5ee769 | -10.8166 | -51.0135 | 2026-08-21 03:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 915274c5-b01b-3736-a8de-c685d734171d | -6.2156 | -55.6118 | 2026-08-21 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 8518ede6-db2b-3d85-b1c0-ac2c8b3a0baf | -3.5407 | -48.1673 | 2026-08-21 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c1b493d3-a9ce-3931-951b-38dc3c482b66 | -8.4088 | -62.6956 | 2026-08-21 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 495a491b-b01f-3a85-8828-46434976bd0f | -11.1747 | -54.0216 | 2026-08-21 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |
| c9fed9c2-3fef-3411-96f7-51997a906e4f | -9.4072 | -60.3977 | 2026-08-21 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| f3b4bd60-9045-37e4-af01-b0c2f3d49bc2 | -10.8355 | -51.0116 | 2026-08-21 03:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 132.8 |
| fde2f407-e59b-35fe-8134-5cd273add418 | -10.8169 | -50.9923 | 2026-08-21 03:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7173640b-4941-3e54-895c-2d7c7beeb191 | -13.3929 | -54.3551 | 2026-08-21 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 138.4 |
| bc3039d0-7a56-3345-9d84-2d23b52d818d | -13.4117 | -54.3737 | 2026-08-21 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| dc0c0440-c689-381a-bcd7-9da07913d9a0 | -6.6938 | -58.942 | 2026-08-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 26bb31e2-8c24-3ae5-9411-b0019c734c6f | -6.8203 | -59.4001 | 2026-08-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 98f76fb2-6252-349e-a2ab-f87017bf3468 | -6.8756 | -59.4171 | 2026-08-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 8268ba9f-7696-33c1-b45f-86577a35b428 | -11.1558 | -54.0233 | 2026-08-21 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |


[Clique aqui para ver as próximas entradas](README20.md)
