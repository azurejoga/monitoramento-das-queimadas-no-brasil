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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60fdce48-1083-388b-8245-424479d05428 | -7.30453 | -60.60748 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b315c1b6-85d9-3c82-8501-80ea36cf9f98 | 0.13947 | -60.39958 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc6c18b4-41b6-38ad-a585-fa7c9486b6cb | -7.57595 | -61.30994 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c539923-27ea-393b-b2dc-3bc7cb050e03 | -7.30805 | -60.61158 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cff70d5c-d9ad-3fc1-bc52-2b6e6a7ba56f | -6.93465 | -55.7103 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b553287a-1ab4-3ab6-b5b7-6d6082d4aa2f | -1.20703 | -54.2103 | 2026-08-30 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 488cb3bf-dd02-388e-9e26-f224dcdc8a70 | -6.67995 | -58.747 | 2026-08-30 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fbf474e4-f9c1-370d-9114-37207f132a95 | -2.75019 | -60.23578 | 2026-08-30 05:53:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d9f2fb4-2674-39c9-8d44-668aebc6bc50 | -6.78762 | -55.67022 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41ddfafd-37a7-3478-bd78-f287c14d5de1 | -8.22978 | -61.42695 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96959c15-0e1f-35ed-82b0-20e818adc186 | -6.78711 | -55.67396 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a19867cd-7feb-36fb-a596-fc6135d7003b | -7.58948 | -61.35152 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 489f42c4-78cc-36ee-a1fb-4a7a9f36a972 | -8.95018 | -62.37724 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf4a3a50-bc43-3185-8db9-15f5b78030df | -8.65794 | -62.84142 | 2026-08-30 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35f5508c-4f52-3569-ab94-29c36e283228 | -9.08873 | -65.48837 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 25ed0945-afcb-36ed-adce-246bf0f328c2 | -8.61592 | -54.78872 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a533afd-63b8-3a1c-8b34-ce42fe01c04e | -8.58102 | -66.94983 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0978bcc2-2131-3038-a129-068aeb2c68b2 | -7.24654 | -60.63172 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f8e45ba-43ed-33bb-8d64-9386535cb1e3 | -7.39857 | -60.58506 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7eabe94c-63c0-31c4-824d-997976d6e0f5 | -1.25152 | -55.70563 | 2026-08-30 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84c43c52-47ac-3f51-8f91-9285f244878f | -9.18004 | -59.6316 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4bc0e6f-741f-35d3-afb7-6d42740da2e5 | -9.0727 | -64.24718 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41d5e932-2083-3616-8bcc-7dc3538f3877 | -7.47619 | -61.41523 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 946f674c-e885-3015-ab41-16d985df2d35 | -8.17881 | -54.93517 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e43a50a-fccb-3c67-af02-0c840285bcf6 | -7.33031 | -60.6005 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 212f2a3e-aee9-3ad6-93f4-c4cad1e50e41 | -6.82702 | -59.42027 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4b6dbe1-cb0f-3efb-bb6e-7b71219cafac | -9.89626 | -60.27079 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a78dc4c1-1050-3f8a-929e-7930f36f730f | -7.85451 | -72.2833 | 2026-08-30 05:53:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fa0a5f6-160d-32d8-bd84-f2b271b26c71 | -9.89721 | -60.27661 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| cfc70844-8800-3ef9-8b51-b41225d7fc90 | -6.88279 | -59.40301 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c452db0-add0-3d6f-bbbc-7ef7d001dc93 | -3.20836 | -61.14307 | 2026-08-30 05:53:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b70054d9-e334-3f35-8446-7f303e2f1e84 | -9.8941 | -60.26783 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8426171-3fa3-3fdc-9311-870fc97d1d33 | -7.31261 | -60.60865 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0f94ea6f-8557-3455-84ae-ff34306e9da6 | -6.80267 | -59.45526 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5221478-770f-3a8c-a52c-12893bf66ad6 | -7.06807 | -59.72211 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a832f35-c1cc-3fc4-b280-e3e0dad5b768 | -8.14801 | -64.00191 | 2026-08-30 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85607c2d-1817-3994-9f34-418e1d96ea4b | -9.05149 | -65.44287 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf4146bb-7613-358f-850c-677c62b59560 | -9.05311 | -65.41072 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 750ca58c-07bc-3569-bb2a-e97ebc610963 | -8.49917 | -55.30046 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75ebebe4-cdf1-34f3-a50c-497451a1edd8 | -9.87176 | -60.30172 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e9a942e-9cc4-3bf2-9bfd-90051d7492f8 | -8.65009 | -62.84447 | 2026-08-30 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8774a0d-c90f-3c14-97ca-1abeb6c88172 | -7.55585 | -61.31185 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44263750-8bc4-3971-a0f4-36539dc5f09a | -9.61064 | -55.13002 | 2026-08-30 05:53:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bef05a5-fb22-371b-a2ea-887b1dafc938 | -9.07896 | -64.25197 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 026d0b9b-2af9-3d04-9947-ba6f6876fd33 | -6.86808 | -59.47282 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00b3a1ed-3549-3b01-a662-96121efe445f | -9.05699 | -65.40774 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4c8911f-d2d4-3b6d-8d26-f9325bf36920 | -9.04259 | -65.43426 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf2e12c9-7b88-32af-a503-8ce8b576fdf0 | 0.1972 | -60.50068 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64f3c294-7e05-3c9e-a231-65ef27c485bd | -7.301 | -60.60334 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d7ee5cc-f286-3c9c-a10d-ecd49bb104b1 | -9.0722 | -60.4847 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fb3492c-f6a3-3586-85cd-574fc60640b8 | -7.29697 | -60.60273 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 494555a1-025e-30e5-8375-91877ab17cd8 | -9.01542 | -65.39786 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee98ae5a-59d2-38ea-b36b-d466824616eb | -6.71125 | -58.56739 | 2026-08-30 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99628fac-0aec-3929-9847-aaef11549839 | -9.78857 | -59.4395 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2421cf81-2d74-301f-a286-9767e5d7c492 | -9.15582 | -59.5115 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65e192f3-12a1-3332-a3d3-90269ff2ea14 | -3.40479 | -61.32026 | 2026-08-30 05:53:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7ebc13e-284a-315b-ba22-ff0b34f076c0 | -8.65858 | -62.83726 | 2026-08-30 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 264a603d-efb1-301d-acce-b90c5c6b4d84 | -8.95615 | -62.41421 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f18ee7e9-a682-3157-93c0-4c5446de7d58 | 0.14316 | -60.39901 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e979de19-24ea-3c81-869a-8c0dabfe7548 | -9.06201 | -65.41934 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3799aa99-20bb-3158-8a99-2c7ef57fd96a | 0.14532 | -60.40101 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a40210b-d9cc-3496-aad4-2cbdd0fc0ced | 0.13648 | -60.40447 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 583d0c7a-c726-38d4-878f-35107411abce | -10.73584 | -54.04897 | 2026-08-30 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 05b25d2d-c3cc-315b-8944-e5c198447aea | -9.71019 | -60.73966 | 2026-08-30 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cbfb3ce-59df-3b8e-8ec8-ce88027178c3 | -7.32524 | -60.60692 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4f949ea-3d93-37e8-bc97-54d73db0c3db | -7.5544 | -61.32158 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5f00c64f-172f-3bdf-9b91-e5b6189678fd | -7.23602 | -60.6194 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d1a6b2e-8bc3-3ed8-9c2c-3cf6c411f7d4 | -8.25085 | -62.75879 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f31d0cb4-7f86-3e97-b7b7-f79d89fcc033 | -9.05977 | -65.41178 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b76b3295-f162-3de1-91d4-4af49a77b14f | -3.23801 | -61.24501 | 2026-08-30 05:53:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93ad387b-1e8d-3664-81fe-6423bcb39554 | -9.15256 | -59.502 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd344979-dba4-394d-b711-4eacc24cc85e | -9.22409 | -59.76036 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4eecda35-1782-3158-871d-dde6d385d226 | -6.80009 | -59.60742 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6616fb63-9db3-38ed-af46-179b88bfb6cc | -9.88922 | -60.27131 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1253b28c-54c6-378a-85c1-de31139d6e47 | -9.15967 | -59.51661 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2117a42-8f75-3a5f-983b-2add79010677 | -7.56602 | -61.32331 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ea225a8-7ad4-3e12-91c5-22baacd49816 | -8.22542 | -61.42424 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5ea67d7-ed81-3624-9563-6bd309c03dd3 | 1.95965 | -50.98924 | 2026-08-30 05:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9947e08-9a8b-3eb8-842a-00809563a327 | -8.10698 | -70.21306 | 2026-08-30 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3f6de6a-f14b-357e-ad14-fcae33998355 | -8.17963 | -54.9417 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2dfde0b-d532-3d7b-8fe8-fcd40db0818b | -7.01703 | -59.65307 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95dafb12-51c0-31a2-90de-70438e95728a | -9.0182 | -65.40191 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c26a754b-27ca-3396-9e44-efd1254c48bf | -9.21957 | -59.76508 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9210de50-f1b2-3765-ad3e-de5d359713ca | -7.31716 | -60.60572 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a007d48-7d9b-3a51-8bef-b3632740da22 | 0.87759 | -60.486 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20e094e0-1f58-345f-885c-56b9f623d8c7 | -9.00403 | -60.60606 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 866b2f30-b759-307e-8a9b-8f87fbefc131 | -9.61191 | -55.12687 | 2026-08-30 05:53:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 478da79b-8470-3552-ad05-5733db951319 | -6.77121 | -60.01307 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5a13db6-af93-33a3-94c3-277dd9b4d268 | -9.06644 | -65.41284 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07dfd664-5abd-3c77-8c98-20af4275d07d | -9.23616 | -60.41792 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a494b7a-4476-3704-ab0e-f8219c5d0a9d | -8.64161 | -62.85176 | 2026-08-30 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a71fc825-0697-38b9-bd04-94187e1b160f | -8.46889 | -62.71354 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 646edaee-9d0c-38ae-a003-1f09212a692e | -7.85527 | -72.27886 | 2026-08-30 05:53:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 360abe5a-d2bd-36b0-bc10-0a5bab97b22c | -9.06366 | -65.4088 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1979a689-42a4-39fc-8e1b-e3f7d4ea46cf | -9.06145 | -65.42285 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90db35b1-ed03-3be4-ac74-59e4b74d4147 | -8.46953 | -62.70935 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18fe99b9-eee1-398e-b725-3ee19b49fafe | -9.15642 | -59.50709 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 263ab133-ac69-38a6-a4f1-7a8f773c3e81 | -9.16474 | -59.51286 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43bd2147-47a1-39aa-8fde-1b4ec15f7b91 | -9.00325 | -65.4535 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63003149-3598-395a-9151-6f2fbd154fee | -7.33083 | -60.59698 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README66.md)
