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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0707317c-1284-3b23-8290-77be20b24205 | -6.15352 | -57.70506 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ffdbb69c-60bc-31e5-9f46-0b1fdd8b53d0 | -4.35745 | -55.65829 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9ecd1847-edf9-36e6-b33c-724830a55c31 | -3.50184 | -59.19522 | 2026-09-21 00:22:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3d3113d5-77e9-3d81-828a-672376c417ea | -6.41855 | -55.01695 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 78afebac-d18f-3951-989f-2ca21683bf6d | -6.30847 | -60.02471 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| ec38505d-885d-38e2-8c55-d1f2afbc8da0 | -7.52168 | -55.27717 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3567ca4b-280f-3175-b8d1-da4e32effc21 | -3.61041 | -54.04393 | 2026-09-21 00:22:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 421c4b33-42fc-36f6-ba0b-713bfde3dbdc | -3.44576 | -58.24361 | 2026-09-21 00:22:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a39563bb-1a5a-368d-a8e6-e8a5b83b4f23 | -7.58059 | -57.68207 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 267.6 |
| cd8d8690-bf6f-3d59-befd-c3ef690631e9 | -4.01277 | -53.49265 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 209e9c64-110b-3f3f-81a7-b7db37bd4be0 | -5.83162 | -53.50988 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 7ec6c240-3ec0-3880-a1fa-cc890aa0bb53 | -5.37084 | -56.05484 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cbe04a67-5344-3fbf-abee-2b2c77242697 | -3.74792 | -59.41604 | 2026-09-21 00:22:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 05e9a52e-b39a-334e-ab0e-5b02ddd51113 | -4.09464 | -52.11388 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b84ef8f8-fe7b-3643-843c-b8b4e327ffa5 | -5.2133 | -56.11674 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 606ed169-bddd-38f8-900b-073c203d911e | -7.58207 | -57.69368 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 166a30a4-9c10-3a98-bbe7-2d9eb448b92c | -7.57117 | -57.6891 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ee7ab5a7-2ae4-39e8-896c-8c15d8b6aaa6 | -3.54554 | -58.68312 | 2026-09-21 00:22:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bc9225eb-c2f4-36e0-a881-f6f689ad0aec | -5.0164 | -56.09093 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 4bda62e5-310e-373a-8b8d-34b83a15ea1a | -3.33287 | -59.8249 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cd581476-347e-354e-81ea-9aefc3df0be6 | -4.54609 | -54.93561 | 2026-09-21 00:22:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9c79cfdb-4dd4-3fcd-bf32-6491994fea22 | -3.19624 | -60.43063 | 2026-09-21 00:22:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c9921d0f-5622-3b48-b941-ef1cd9872af5 | -7.25295 | -55.60056 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 54a86b90-67b1-3dea-9dd5-a96402f2cf88 | -6.45145 | -48.45332 | 2026-09-21 00:22:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 04c24074-498c-313e-a0b9-e9bc52095aa2 | -5.00745 | -56.09218 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3f65eeb1-29a5-37ba-a363-ee06aaeabc7e | -5.89566 | -53.6408 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a399dfb9-6ca7-37dc-a146-53558d803b46 | -7.59912 | -57.66782 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 31efd0c9-58b4-3ca6-972e-3f17f226bf6e | -1.91442 | -58.26991 | 2026-09-21 00:22:00 | TERRA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 64cd3443-2ddd-38c7-9f5b-8604e58dc3eb | -6.29563 | -59.92721 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2312b516-bd96-378b-acaa-310a97d1ad5b | -4.35622 | -55.64939 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 48851e97-b062-314d-ade4-4a4ec7590879 | -3.661 | -54.27651 | 2026-09-21 00:22:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4b1ecb83-2ff1-3225-a310-76baf92b39ae | -3.0127 | -54.18924 | 2026-09-21 00:22:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 963f116f-d03b-3dec-862e-e3a0dc17ee8d | -4.35587 | -55.49973 | 2026-09-21 00:22:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e622bbf0-0f05-333f-b9fb-8114a1f66d40 | -3.80321 | -51.36343 | 2026-09-21 00:22:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8215e774-d3ae-3877-a9b9-709dec080301 | -2.42074 | -57.12298 | 2026-09-21 00:22:00 | TERRA_M-M | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c4823c47-1b75-322d-adde-5954cc6369d5 | -4.26231 | -55.7683 | 2026-09-21 00:22:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f4e5795a-d109-36cf-826d-2630ac5464fa | -6.0674 | -55.62283 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 87e69564-b827-3783-91e3-dac256f13777 | -7.58118 | -57.68775 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 183.7 |
| e9c42677-b773-3166-8b86-2f68e3ffa806 | -5.76084 | -57.59286 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 0ef16a4a-1d6a-36ca-9448-c272a5ddab90 | -3.09891 | -53.16399 | 2026-09-21 00:22:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| beb0199e-cb89-3a03-a993-aba2f9b29391 | -3.23381 | -60.80526 | 2026-09-21 00:22:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 94bef54f-03f2-3d2e-b0a2-2367a5f21fcb | -4.68665 | -55.6332 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8807d00f-3717-332a-b7ac-ec35c4a50831 | -7.64095 | -55.06542 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 75b34079-cdfa-3328-a77f-d8ff3be1a5b5 | -3.75866 | -59.41461 | 2026-09-21 00:22:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e14a9aa4-f016-3062-b69c-beb52be4bc34 | 4.80884 | -60.32946 | 2026-09-21 00:24:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 549c8808-5049-338d-bd7d-22f5f8e6369d | 1.54785 | -55.81671 | 2026-09-21 00:24:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e35f1fc7-c14a-3a59-bfe9-2adac3090f4a | 1.54664 | -55.82549 | 2026-09-21 00:24:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| d66050de-9173-3bbb-b822-8bc7406dbfc9 | 1.44167 | -50.77272 | 2026-09-21 00:24:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3e826d10-042d-3cad-8c93-c29be7e5cd8c | -3.753 | -59.419 | 2026-09-21 00:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e380f124-065b-31f0-8ff9-f0cc703de93e | -11.0509 | -54.9106 | 2026-09-21 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| dfe3a955-249c-379b-a645-5c3b8f6962e8 | -10.9112 | -53.9635 | 2026-09-21 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 94f241c0-c942-3c79-8c89-3defd0d30b94 | -10.7626 | -50.8069 | 2026-09-21 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 4afb93c1-4614-34f3-8982-e03fe77d50f2 | -3.0717 | -61.2764 | 2026-09-21 00:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| c0365bfc-ad49-387e-a2f5-aec6195b0f8e | -3.0535 | -61.2578 | 2026-09-21 00:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 895fe5f3-44e7-3ed9-bf7b-52453c58b66d | -3.0534 | -61.2767 | 2026-09-21 00:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 4ae52679-2985-3d4b-a070-7136f12a6787 | -10.4664 | -50.3479 | 2026-09-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 92bfde88-36d4-3206-bcc7-571e65dad1af | -5.2168 | -56.1096 | 2026-09-21 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| d9122009-986d-3837-873c-cd81ac0f4335 | -6.4485 | -59.9909 | 2026-09-21 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 30630e84-b398-3c68-a54c-4a61c592da69 | -10.4853 | -50.346 | 2026-09-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 421009b5-54da-3620-b10e-66be71f968e2 | -3.6946 | -60.5835 | 2026-09-21 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| f466f2c0-8374-390b-bcc1-5d516e0e0f7d | -9.5593 | -66.0545 | 2026-09-21 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| edb74c1c-05ce-300f-9f11-716879d3c30e | -10.485 | -50.3674 | 2026-09-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 9bbfd06a-2d54-3bcc-a79a-e62e7bc2ed69 | -5.7615 | -57.5807 | 2026-09-21 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| c4783d13-31d7-3241-a727-4a0d03834fff | -3.0717 | -61.2575 | 2026-09-21 00:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| e66a5724-3621-37ef-aff5-b48ac44cab5e | -3.0716 | -61.2953 | 2026-09-21 00:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 95839352-0514-3e33-a238-d5afb0056a07 | -10.7816 | -50.805 | 2026-09-21 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 44a2daac-8eca-3e53-8b6d-837d950646d1 | -10.7064 | -50.7703 | 2026-09-21 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 6b25c89b-a4d9-3871-a575-c2d1e6fbb562 | -10.0712 | -50.26 | 2026-09-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| fa7b58e4-cfd1-37db-a1f0-2dcc3f90a672 | -10.7624 | -50.8282 | 2026-09-21 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 80dd5845-ff96-3e52-bd18-7580659bca5e | -6.4486 | -59.9717 | 2026-09-21 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 6feb3a03-8cb3-33cf-bca7-58aabd652103 | -6.4671 | -59.9711 | 2026-09-21 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 43088c45-3f53-339a-8b37-09b2a3386d5b | -2.8791 | -57.799 | 2026-09-21 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ac10ecf5-626c-39a5-b3dd-562aa42e86d0 | -9.5594 | -66.0359 | 2026-09-21 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 05cf4186-0044-3703-b94a-81e242ccca87 | -4.3541 | -55.6653 | 2026-09-21 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 6fcc6629-61f8-3657-8887-8d873bc3b294 | -10.7813 | -50.8262 | 2026-09-21 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 3acf5114-9e17-3746-8251-a102d5e51067 | -10.5908 | -57.4738 | 2026-09-21 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| cba70802-6970-313d-b888-e38675ee3ed4 | -2.8791 | -57.8184 | 2026-09-21 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 27f535e6-8efc-351d-a3e7-ee8c33355796 | -6.8754 | -63.107 | 2026-09-21 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| efe10e4a-a44f-3e9c-b3b6-e9923ba2df70 | -6.7464 | -59.4223 | 2026-09-21 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 5ca4a905-92d8-3cf0-8ff4-2964ddbca88b | -4.3357 | -55.6659 | 2026-09-21 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7c6e88a4-8ddf-38fa-b166-6371f15bed29 | -10.6875 | -50.7722 | 2026-09-21 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| ecfcb3f8-bb4b-30ed-9465-f98080b12d4d | -11.041 | -54.1567 | 2026-09-21 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 69bc345a-18d1-31fa-b96d-922a4f8ed26f | -11.8204 | -49.8106 | 2026-09-21 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 1ddb16e6-7f4c-3a25-b064-f6da91fff1ce | -7.2519 | -55.5994 | 2026-09-21 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b6061308-4681-33a6-8765-5ce4b4e830c3 | -10.7061 | -50.7915 | 2026-09-21 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ea139d17-8f6c-31b6-99af-80223de8e7ff | -4.3542 | -55.6455 | 2026-09-21 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b4cb6f49-5fdc-3d13-9d18-3737bca724bf | -6.2026 | -57.7778 | 2026-09-21 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 2e56cf0b-26b6-339c-9947-56a4f265c0e0 | -6.467 | -59.9902 | 2026-09-21 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ae2640d9-3593-3918-a59b-95a1713418c8 | -10.5906 | -57.4936 | 2026-09-21 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| fde29a91-3a68-3cca-9dff-c808b385da3f | -7.5888 | -57.6953 | 2026-09-21 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 65cd6f44-0aa5-3dcf-ac23-133e1761c014 | -10.7253 | -50.7683 | 2026-09-21 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c56d36bd-a372-3f5f-95d2-5c6a4a1ec365 | -7.5889 | -57.6757 | 2026-09-21 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 194.4 |
| 2ea631cd-c44d-38d8-80fe-034ee2475b42 | -7.5703 | -57.6962 | 2026-09-21 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 2b2a6cac-9562-3dbf-8327-fbfcaba46dc4 | -16.2967 | -49.9133 | 2026-09-21 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8220164d-7203-332d-8355-5d8bbab8a902 | -10.2173 | -59.403 | 2026-09-21 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 7d5db096-e99b-33fd-92a2-fddf632cdd44 | -11.8014 | -49.8129 | 2026-09-21 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 9deaecb9-22ad-3763-860a-d171e9402775 | -7.5704 | -57.6766 | 2026-09-21 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 150.6 |
| 333199ec-2107-3b25-ab64-880354160084 | -4.0944 | -52.1252 | 2026-09-21 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 30bb67b1-6af2-3cbe-aa6a-4d79367f76ba | -11.8014 | -49.8129 | 2026-09-21 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 214.5 |
| a01b95ce-22aa-30d4-8a43-167b4f83e7a7 | -11.0509 | -54.9106 | 2026-09-21 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |


[Clique aqui para ver as próximas entradas](README10.md)
