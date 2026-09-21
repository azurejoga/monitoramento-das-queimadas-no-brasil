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
| 48fae080-0570-34c8-961a-a826fc39b220 | -4.38481 | -56.32332 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7951a053-db81-3472-9dc3-fad5dee81c6d | -6.85072 | -55.28514 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5a7da669-2e82-3e4d-98d4-7735b3348b4f | -4.34739 | -55.65061 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e92ae9d9-ebe8-3805-9f0e-57a203ba42d0 | -6.49724 | -58.38127 | 2026-09-21 00:22:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bf905ce1-0226-3777-99ab-198ebb235585 | -7.25172 | -55.59142 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 25173187-d795-30ce-b4ea-79b3c8b0a0f9 | -6.19503 | -57.79059 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2c03a16a-7407-3519-b188-d7b2ef356640 | -3.76049 | -59.428 | 2026-09-21 00:22:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 70edd63e-5e28-3476-bdaf-687ecff51afc | -3.90259 | -55.83361 | 2026-09-21 00:22:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 509488f6-9637-3571-84a4-cdb43b47a40f | -6.69301 | -60.01092 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f35fe399-7b2b-33d3-aad1-fc6a988eb0dd | -5.73167 | -53.45532 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 90e6da3b-9990-35d1-a4b2-fc2ff7f8e0dd | -2.91159 | -54.19113 | 2026-09-21 00:22:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| abf03b6e-8729-37cf-8b7c-cd4b5c2955af | -2.88167 | -57.79469 | 2026-09-21 00:22:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0da3157c-abfb-34a4-acbb-0b101ac5148b | -7.57962 | -57.67617 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 58fc78d3-420a-37f2-afb3-ba8d94a47ff8 | -6.75296 | -59.1184 | 2026-09-21 00:22:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a7f1be9c-4a94-3c30-a1de-fa9cac68d14c | -4.56608 | -55.75589 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1c17ffdf-de94-398c-9f74-0530ae6b45d6 | -6.46157 | -59.97551 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| cd3b2500-1faa-350c-9bf6-6d02c1392fb6 | -2.8722 | -57.79599 | 2026-09-21 00:22:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8703c0ea-c080-3ea8-881f-507cba64f241 | -6.7219 | -55.08264 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 288af55a-43e8-38e4-96bf-fde50f4d5e0d | -6.73955 | -55.08011 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a6253b00-cf07-3585-9190-4c7bf7665488 | -5.76639 | -56.52396 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 76ee6bdf-e062-3672-9036-5d1d2bbb5b35 | -6.77665 | -55.48477 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 34261087-a717-396d-a052-1cab3b0fc446 | -3.53702 | -58.69634 | 2026-09-21 00:22:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| dc5aafdb-5d7e-32b6-a355-84c9fc067a57 | -3.08274 | -61.17801 | 2026-09-21 00:22:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| bb1302fb-7f87-3fbf-bd03-08d37ded7ac5 | -6.72952 | -55.07253 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1f04e920-8131-3646-8646-af2ae8ccd2c1 | -2.87641 | -57.82676 | 2026-09-21 00:22:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 701e83d0-578a-32dc-9ed5-3a46e4da0a58 | -3.00121 | -54.17224 | 2026-09-21 00:22:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c0b35ef7-347e-3d0c-848b-9d85465e9097 | -5.81329 | -52.09183 | 2026-09-21 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 51d0c4a0-a5f6-3eda-8452-7059744df540 | -6.22555 | -56.04089 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 54a692d3-01e9-3c2a-8942-a410b0c9c231 | -4.06677 | -52.12922 | 2026-09-21 00:22:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 1eb7eae7-3208-3292-bab2-6f0832f05bbd | -3.48906 | -59.62146 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| dd236067-9a3e-313f-aca6-841a4219d07f | -2.68404 | -57.62793 | 2026-09-21 00:22:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2e6a7a8c-2a1a-3c31-8df7-2f871bd96125 | -6.35578 | -57.76834 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 596a7451-d8ee-38e0-bb4d-e539ba11e5f7 | -6.25365 | -55.43841 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a934d34f-d972-35f3-a1f9-e411edcfdc26 | -4.30316 | -56.26629 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a2591c68-3519-3fab-ad41-5cc6de165e7a | -6.15641 | -57.9578 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 3adfb9cf-9499-3920-b9ca-65a91b722acc | -3.17522 | -58.59171 | 2026-09-21 00:22:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 9b105f26-8ea6-30af-b9f5-9bfd2678f8df | -6.94587 | -55.64315 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5abc6463-e916-3c86-ac31-bcfb1c0c1808 | -5.83291 | -53.51906 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 49d98ea8-4288-3565-af5d-452c87a5e09c | -3.66866 | -54.26632 | 2026-09-21 00:22:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f001ec61-eac8-39ec-bca2-9aaed4c62a54 | -6.73316 | -55.09914 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 6eb53411-cdc2-39f5-a554-650c893a37bb | -5.86501 | -53.48668 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ec1c469f-d09c-3bf0-89f4-4cbe836b9bb3 | -2.7456 | -54.58483 | 2026-09-21 00:22:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 80cc7757-adba-3235-8061-51db3d7db8a2 | -6.65613 | -59.97134 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 738b3f5a-efcd-3efb-9a11-62d330722fd0 | -6.14384 | -55.70723 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 893f7483-7e31-3890-a073-a7827b162d05 | -5.91367 | -57.67646 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 9ad73ca7-7dcd-36eb-84c6-c0dc759d242d | -6.44772 | -59.96061 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 38a292b6-1f8e-3d14-9055-d1c0f45b0ac0 | -5.84577 | -53.54532 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| babb2b85-1101-387d-ba0e-c21cc62ca2ea | -6.39447 | -55.25228 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f6623cf4-2e0c-3108-83c2-07b26125293a | -4.6778 | -55.63441 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6d95f1f7-f540-3acc-a8ea-0a42465a3c57 | -1.91296 | -58.25928 | 2026-09-21 00:22:00 | TERRA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 838bdf22-b06c-34d0-9bf7-95e8e2ba2e60 | -5.82011 | -55.70294 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cfc5c10e-3008-32af-8c18-adc6dc6a675f | -3.61169 | -54.05306 | 2026-09-21 00:22:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 782806ff-71c5-3b2c-b927-aa2711c7dfff | -5.84706 | -53.5545 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 55d36a28-618d-30d0-8246-9daed31c948b | -7.32829 | -55.61201 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 1ffc19cc-bda9-3aa8-aca3-11af0319385e | -3.07294 | -61.28947 | 2026-09-21 00:22:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 204ddac2-7a60-3694-8ff7-85ce0e5e6501 | -5.88671 | -53.64201 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| aa8cd274-8a36-30de-b491-d7c356bfe6e8 | -5.88044 | -57.72591 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 042cbb56-c8c9-3c59-8d69-4ba888007138 | -6.46368 | -59.99179 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 93f2c72d-cb07-3bbf-b0b7-bc95e853c3b1 | -3.08619 | -61.17185 | 2026-09-21 00:22:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2afa8b21-c406-3e74-9c04-3404a86878f4 | -3.39562 | -59.52891 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 17d11bfb-15c9-3c80-962a-0c4c504bf0d0 | -5.83671 | -53.48098 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d9a062bf-c7ea-3d80-b762-4c791d2baad0 | -6.82979 | -55.54182 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| aca3be30-279b-33de-ae5f-48fba7a014d9 | -6.22974 | -55.9369 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ea6f47b7-9626-3b4c-850b-ef347f462d95 | -7.37585 | -55.55904 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7bbcdfaf-c85c-33d6-8610-890b9807a7cd | -5.88193 | -51.58254 | 2026-09-21 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| dc4fdacb-98c5-3998-b1b8-cfec23a71db0 | -5.2083 | -56.08 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 66926746-f743-31ce-940c-33de8a4144ea | -7.58912 | -57.66915 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| b62778e4-2be1-3432-a3e1-62cca3ca575b | -7.62307 | -57.61767 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a96b1c04-0772-3448-8c20-9f13132e865c | -3.10032 | -53.17391 | 2026-09-21 00:22:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f394c30c-470d-3dae-8e51-883283347961 | -3.39746 | -59.54241 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3a36ced3-3468-3f7d-85c4-896bed5fb635 | -6.7987 | -58.7887 | 2026-09-21 00:22:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e5c82a6f-3867-396f-bfb9-d3ba5a575a5e | -6.08425 | -55.54726 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1029b3ca-5b1d-3ed7-b677-44add4e064d1 | -5.93914 | -57.70124 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 8992f9b2-e889-34ab-a57b-3b0da823cd9d | -5.8765 | -53.63417 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1246d727-d8c0-3fdd-aff8-fa2e3db31945 | -5.81045 | -57.74167 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4f3dd1a7-4e8e-35be-ae92-d9a255e57444 | -6.92287 | -55.61505 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aba48a98-17f4-32dd-899d-5579e633afa4 | -6.11503 | -55.62826 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 59cf5c07-abb5-397a-9abe-5d2326cf08f4 | -7.58273 | -57.69934 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| b2058597-0990-37e8-a71b-80c60e8a632d | -6.1286 | -59.96124 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2103d452-66c2-36a4-9d31-75741f8483cc | -2.85914 | -54.21376 | 2026-09-21 00:22:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 37abcc31-cdc2-3f69-a2c5-b52ff4222f0e | -5.89619 | -52.09542 | 2026-09-21 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| aa979fbb-d4e0-39ff-9285-1fc3d46e846f | -3.65251 | -58.87007 | 2026-09-21 00:22:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 7638764e-e0ed-38e3-a6be-4981931f67ec | -4.51402 | -54.98214 | 2026-09-21 00:22:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8fe56c7d-084b-371e-9cdd-2a3e88d9998b | -1.46705 | -48.99205 | 2026-09-21 00:22:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 37b79439-8b1e-3564-b313-66d5c9e1750c | -6.76397 | -59.11702 | 2026-09-21 00:22:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ee1d7b8d-3b75-3f8b-9bff-d707887f6227 | -5.82264 | -53.51116 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 16a5f05e-5b71-39e1-bb95-c112c0735895 | -6.19351 | -57.77932 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 25bd2a0c-0bd6-39fd-a429-cdd18148b7f5 | -6.09877 | -57.68433 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 2766bfc9-9cb2-348d-aace-308bb18fb265 | -6.21809 | -53.57 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| dc2e53b4-234e-364b-b421-edf0c09695fd | -3.89532 | -60.58897 | 2026-09-21 00:22:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 82fb83f3-78bf-3594-8bfc-8e5e8cc3b9f0 | -5.97663 | -55.368 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 1ac3bbd4-339a-3555-acec-c285fa69c0f9 | -6.32022 | -60.02315 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 26365e12-8333-3a63-bf12-457e59e0edcb | -6.92411 | -55.62413 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6f1746ef-57f4-3c4c-bff6-49b0dc4960c1 | -5.22102 | -56.10635 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 3367b63c-1c8b-31e3-ab34-a57ca67d59d5 | -7.5906 | -57.68072 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 2a968b28-1e70-3c75-a7f0-36cc4ef0d881 | -6.73072 | -55.08135 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9e09c17d-1253-37cf-8625-fdb2cd0822f0 | -6.77841 | -55.63209 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f6a26436-e5e0-373c-b019-8a620bf27acd | -6.31805 | -60.00674 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 00b1fc73-fa8e-359f-b40b-7673fd805541 | -5.83451 | -52.03448 | 2026-09-21 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d2b374b3-ff7d-3cf0-a5a7-910a45317e7a | -1.34198 | -49.31252 | 2026-09-21 00:22:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |


[Clique aqui para ver as próximas entradas](README9.md)
