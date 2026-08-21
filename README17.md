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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22a108bc-5ae3-396d-9f1f-727de9a98ecd | -9.41491 | -60.4002 | 2026-08-21 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 05ff12eb-c500-37bf-bd81-8fb7a34492a4 | -9.39275 | -60.40926 | 2026-08-21 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 7f99441b-70ca-37e9-bd3b-d07f0060cf90 | -9.39878 | -60.44506 | 2026-08-21 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 221.0 |
| 1547f082-37bc-391e-93cc-e8bced9329ba | -9.21233 | -59.78004 | 2026-08-21 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e114dc18-d165-36af-bb0d-45d82bc40d84 | -9.40471 | -60.43864 | 2026-08-21 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 654.1 |
| d1eaed07-b449-31ab-b10e-7687c46d2b30 | -9.4092 | -60.40652 | 2026-08-21 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 301.5 |
| 47bb232d-cb44-3025-a124-0e913d7bca2f | -9.39845 | -60.40292 | 2026-08-21 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 299.9 |
| 7a96c383-909f-3af7-8e5e-425014fd8a4b | -9.40043 | -60.55438 | 2026-08-21 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| bec239c8-677c-3990-9f61-649ef2c09bf7 | -9.41518 | -60.44231 | 2026-08-21 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 322.5 |
| d411b047-96af-39bf-81fa-719b86cf1dd3 | -9.21386 | -59.77278 | 2026-08-21 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0c83a00a-32f4-330d-996b-a5460e0e7cd2 | -9.42112 | -60.43595 | 2026-08-21 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 41c5f726-8538-3512-98b2-572cd57aab22 | -8.39086 | -62.69147 | 2026-08-21 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 33.0 |
| e236daf9-331c-36b4-8796-02b440771cbd | -8.73408 | -63.94953 | 2026-08-21 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 00cbf32a-8f61-3669-a28f-d5ec5790793a | -7.77818 | -61.16357 | 2026-08-21 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| d2c2a380-e985-301c-860d-8af88bfcbaa3 | -7.86392 | -63.75959 | 2026-08-21 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ce7d7a2a-29a7-3f13-b648-be510f477ae4 | -8.73379 | -63.9553 | 2026-08-21 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 22badc3b-974d-35fe-bd3a-195ce608fe33 | -8.7372 | -63.9691 | 2026-08-21 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.1 |
| e5d5084c-e5f0-3289-904d-9e3fda4f489c | -13.3923 | -54.3965 | 2026-08-21 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 6f4558c3-9b47-3f2e-ad00-5db0b8aa689d | -6.2156 | -55.6118 | 2026-08-21 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| f77d3c36-3475-3e38-908e-40a21272d5af | -10.3151 | -50.3634 | 2026-08-21 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 3e026b66-a510-3fe5-be59-7d4a5e6daea5 | -13.9367 | -53.859 | 2026-08-21 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 34811415-abf7-3bf5-94e2-56f2f0649718 | -6.6938 | -58.942 | 2026-08-21 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| f24b3849-ca73-3ffe-ac1a-3754f6ca8f50 | 2.5983 | -60.697 | 2026-08-21 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| ff68e795-e917-37f5-bc66-a3799893f1c2 | -8.3903 | -62.6963 | 2026-08-21 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| d030c291-1819-3381-8b01-8923e75e23b6 | -13.4117 | -54.3737 | 2026-08-21 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 061950bc-2ca7-3037-8199-9f0da0f174bb | -10.3148 | -50.3848 | 2026-08-21 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 8165e4e2-d9a8-3992-a1af-e5f3b5168499 | -3.5591 | -48.1882 | 2026-08-21 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e9ba0bff-4a3c-3459-bfa9-c366a94de3b9 | -18.1934 | -50.7554 | 2026-08-21 01:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 56c93fe8-97aa-3225-b35b-9cd7f244e426 | -18.0285 | -44.6113 | 2026-08-21 01:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 91ec2870-db8d-3bf2-b70b-a679882ba020 | -10.7501 | -50.3396 | 2026-08-21 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 090ded45-9142-37dc-be37-5d3695141fcf | -6.2155 | -55.6316 | 2026-08-21 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 2e77d77f-4d86-3502-ac08-cc47d929ff02 | -6.2341 | -55.6109 | 2026-08-21 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 5d4d2aeb-0b21-3f89-8515-b18742c3737c | -3.5407 | -48.1673 | 2026-08-21 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d7785be4-b3e1-3f4a-a527-2c553d336d8c | -11.1558 | -54.0233 | 2026-08-21 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| fc8caa08-592d-3fb0-9211-4001088c95dd | -13.3926 | -54.3758 | 2026-08-21 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 253.8 |
| 823d1e27-16f7-3066-aff1-225f58277b1b | -11.175 | -54.001 | 2026-08-21 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| dde7aab0-51b4-3fe9-9048-18f14d0937d8 | -10.7311 | -50.3416 | 2026-08-21 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| b1feb8e0-fb51-3ec5-bb80-5faaa0264404 | -11.1747 | -54.0216 | 2026-08-21 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 192.1 |
| d5873675-c9dc-3126-ace9-03dc221cc11f | -6.1177 | -59.9069 | 2026-08-21 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 002ee617-f582-31c7-ac5e-86576cab7d29 | -10.7504 | -50.3182 | 2026-08-21 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 1bead598-9240-3881-a696-73fb41ca6e7c | -3.5406 | -48.1889 | 2026-08-21 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 461cda90-a97d-341b-9396-a8fbe1876a83 | -3.5221 | -48.1896 | 2026-08-21 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 1bd98775-578b-364f-a040-212c7a72eb8d | -10.7693 | -50.3162 | 2026-08-21 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 76ea31a6-b4c5-3c92-8adc-08ef70c6f963 | -13.4114 | -54.3944 | 2026-08-21 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 08d597fd-d251-30ca-9cd9-85415778f300 | -18.2134 | -50.7518 | 2026-08-21 01:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2ec7610d-e022-3f48-8e0c-e28513a947bd | -13.5879 | -51.6502 | 2026-08-21 01:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2bd8bd0d-fccb-3006-9628-96db0d28d54e | -6.6938 | -58.942 | 2026-08-21 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.4 |
| c08d146d-6376-3376-9385-c193ae006b6a | -4.0943 | -42.5097 | 2026-08-21 01:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 01484549-d98d-3704-96d8-ba4eb924fdba | -3.5406 | -48.1889 | 2026-08-21 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 1be9ff66-46b9-35ae-ab48-66f1f7e9e98a | -11.175 | -54.001 | 2026-08-21 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 6a3d3642-6e64-32a6-9869-0c9711ff2a62 | -18.2134 | -50.7518 | 2026-08-21 01:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 5285eeb4-9276-3798-9e87-32e3a5de207a | -3.5407 | -48.1673 | 2026-08-21 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 68b2ac19-9966-33e1-b010-4784f50a861e | -6.2341 | -55.6109 | 2026-08-21 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 2ea948ce-5b41-34d5-94a0-9b4ae7aa6074 | -6.2156 | -55.6118 | 2026-08-21 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| a183e886-c50d-3ba8-b8fa-b1555360edc3 | -11.1558 | -54.0233 | 2026-08-21 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 7eabdc58-f153-367f-8698-36e6db773196 | -20.9552 | -49.1439 | 2026-08-21 01:40:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| 5211d607-91fc-34b2-a7c1-275fd61488bd | -4.0481 | -50.2984 | 2026-08-21 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 7c34b9a2-e74a-3d36-bdfc-45d3571e8df5 | -6.6939 | -58.9226 | 2026-08-21 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 915c9ac4-8ad4-3229-9b67-553efd532cfc | -6.2155 | -55.6316 | 2026-08-21 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 1fc088ec-013e-3e30-853e-28d15f2d6c64 | -11.1747 | -54.0216 | 2026-08-21 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 245.9 |
| 02c65d77-3b3e-317a-8240-f7eb098965f4 | -10.7504 | -50.3182 | 2026-08-21 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1ea983bd-2552-3700-8854-adc5cd6b4f8a | -6.7123 | -58.9412 | 2026-08-21 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 62bd2096-fc95-3ae3-8fe1-a17cf9b4dd2e | -10.7501 | -50.3396 | 2026-08-21 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 1652e057-0792-35bd-a648-a7cc65673f20 | -11.1561 | -54.0028 | 2026-08-21 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 94c320f9-4ffe-3d24-bcd8-93f2dd01586b | -7.3788 | -45.8344 | 2026-08-21 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b69a88c7-3946-39ba-a7ae-b25c82b06916 | -7.3603 | -45.8136 | 2026-08-21 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 551.4 |
| a8a51375-0337-3355-8446-d8df84052abc | -3.5407 | -48.1673 | 2026-08-21 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d102d28b-e384-3216-9c41-39142f90849a | -7.36 | -45.8361 | 2026-08-21 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| f7dc8dc8-01e4-38fe-a015-567a217fdb46 | -7.3415 | -45.8152 | 2026-08-21 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 81cd75d4-f3a0-346a-86bd-0734d2993cac | -6.2341 | -55.6109 | 2026-08-21 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 162.8 |
| 56fdda4e-c39f-3d4b-b43e-fc7ad4136b0b | -10.3148 | -50.3848 | 2026-08-21 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| d27645e7-861f-3dce-b59c-cac7db177639 | -19.7438 | -57.9633 | 2026-08-21 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 755b854b-1e9a-3461-b511-bf76fe9df541 | -6.2156 | -55.6118 | 2026-08-21 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| e22c7d75-bf80-3dd5-9d28-58f7fe4ba9de | -11.1936 | -54.0199 | 2026-08-21 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 2616e950-2e8c-396b-8b90-7b7bfe0c9625 | -7.3791 | -45.8119 | 2026-08-21 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 292.9 |
| f99929b5-66c6-3085-b262-58c9d3d171b8 | -6.2155 | -55.6316 | 2026-08-21 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a6d4e586-672f-300e-8012-6caa69d84d37 | -11.175 | -54.001 | 2026-08-21 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 158.5 |
| 8031cd5b-484e-39f6-88f9-d0a508349aad | -7.3605 | -45.791 | 2026-08-21 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a97a3105-2f9b-3e5e-9b01-ffb433f5d4e7 | -11.1561 | -54.0028 | 2026-08-21 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 8dde589f-d9e0-34d5-9548-fcd01d9a3a3d | -6.1361 | -59.9063 | 2026-08-21 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ed290a1b-f8b5-339d-a3ce-24ea1bcda085 | -6.1177 | -59.9069 | 2026-08-21 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7e996022-3a06-34ea-9465-d2ce8397394d | -3.5406 | -48.1889 | 2026-08-21 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| e6b11d9a-7008-3827-9147-16038ff59b3c | -6.6939 | -58.9226 | 2026-08-21 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b65e6a6a-21cc-35a3-a2de-996f3abdce8e | -11.1747 | -54.0216 | 2026-08-21 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 242.5 |
| 04a7cc81-8b99-320d-939d-bd9918a39b20 | -11.1558 | -54.0233 | 2026-08-21 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.8 |
| ef06c751-7d72-35c6-8f51-a05aea6f1f2b | -6.6938 | -58.942 | 2026-08-21 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 5ce8fc71-143c-3525-9dcc-3ab8d36f3d7b | -10.3151 | -50.3634 | 2026-08-21 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 91a895dc-6340-3c62-86bd-745310346aa5 | -4.0481 | -50.2984 | 2026-08-21 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| dcc42155-f06d-3fd7-ba5f-368f47fece76 | -20.9552 | -49.1439 | 2026-08-21 01:50:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.0 |
| 3cc5e701-3c4a-351a-9d8d-d6731352ad07 | -6.2155 | -55.6316 | 2026-08-21 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ca8dca8d-4650-30b6-bc20-ed710c7ff007 | -7.3603 | -45.8136 | 2026-08-21 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 510.1 |
| a4669cad-6ef8-3170-a5b2-2c720ea45048 | -3.5407 | -48.1673 | 2026-08-21 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 166f1ca5-1b78-39a7-83a7-fd1eb2485227 | -6.6939 | -58.9226 | 2026-08-21 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 9d95ab39-25c0-356c-b090-bb042b7f6706 | -8.3903 | -62.6963 | 2026-08-21 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 43311bfb-7470-3767-9524-125b2027f10b | -7.3415 | -45.8152 | 2026-08-21 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 6f01032b-ed60-3143-89c0-782e74366d36 | -7.36 | -45.8361 | 2026-08-21 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 87902f3c-dec4-38ea-a674-b634a27ccb5b | -4.0481 | -50.2984 | 2026-08-21 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| cd4b43d0-981b-327f-ad5b-f8f2befa9ed3 | -11.6719 | -48.3467 | 2026-08-21 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 7cdda1cf-a4bd-3f52-abb2-24d3fc5b9ffd | -6.2156 | -55.6118 | 2026-08-21 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 510545f9-62b6-3373-84b4-4a0f5cf62e6e | -7.3791 | -45.8119 | 2026-08-21 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 244.2 |


[Clique aqui para ver as próximas entradas](README18.md)
