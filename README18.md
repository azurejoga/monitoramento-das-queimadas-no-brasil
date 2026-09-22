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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e02fa630-9ed7-3915-82b8-fa03e1157014 | -5.9265 | -57.682899 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f157c7e6-e5dc-3f24-86f7-842c67cf4957 | -6.7242 | -55.054798 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 822e0c73-560d-35d6-9245-66e40147cd18 | -13.3002 | -51.791901 | 2026-09-22 01:19:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83983d61-dfce-385e-9c3a-3e60b03aba85 | -4.0809 | -56.228901 | 2026-09-22 01:19:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e711f07-a021-31eb-b8c5-2062d795d2a8 | -6.6959 | -60.0042 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bff3003e-6e27-3b78-94be-aa8b71e23053 | -3.3311 | -59.805901 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28e93396-0e63-3ff2-a81b-ba657df002b5 | -10.5858 | -57.4832 | 2026-09-22 01:19:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddf58ad4-fa1c-3dba-aea8-1d543421c8aa | -2.8762 | -60.115601 | 2026-09-22 01:19:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f763823-cb68-3e7a-ab6a-e955c46640b2 | -6.4496 | -59.9632 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b7f4895b-9762-34ca-97bd-68223e73838c | -3.4898 | -59.5984 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb3508ae-8bf2-3d10-86e5-044d4ac9a4dd | -6.0882 | -57.6236 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c683ff70-3d77-3e1e-99d9-393311388eee | -3.6869 | -60.593899 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 038859b5-40a5-3d24-8c74-adccb578ac10 | -6.1364 | -59.945 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c51858bc-0a0a-3675-ab32-7d3a34fb4ba4 | -3.4221 | -60.202301 | 2026-09-22 01:19:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfb2d4fb-fb68-3ce9-bc78-6a7b25078f00 | -2.9551 | -57.7286 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9967b7f-3af7-3a27-abf9-423f451a4d53 | -3.5051 | -55.488899 | 2026-09-22 01:19:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43407448-e156-3a99-9da7-03388ab42750 | -6.0899 | -57.630699 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e59e1be-9b4c-3fd7-b184-4cfe7564aeff | -10.5977 | -53.974899 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6370a9e7-e1f3-3ee5-ac05-5ab9da127d86 | -6.8597 | -59.908501 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b88d49b9-0693-3c04-bc38-f0103fec2459 | -4.9654 | -55.821899 | 2026-09-22 01:19:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e3157a2-3f26-3a3c-a77b-ec7d2be704b9 | -6.7326 | -55.090302 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7532ec0a-a159-345c-9850-c8d1083c8603 | -2.9534 | -57.721298 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d7aa943-2823-30ec-8fae-73174b164c4e | -13.2918 | -51.7579 | 2026-09-22 01:19:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8a8aba18-77b4-3102-84c1-99df7f0ed355 | -3.2859 | -59.429298 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| beaf08a2-d253-37df-950e-ad1d05275f9f | -6.0906 | -55.560799 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb12cc7c-4a72-3164-9685-9f13199da775 | -8.2531 | -55.275101 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19dfb45c-3ae9-3087-b2e0-006247347496 | -3.5384 | -60.575699 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fa023a7-bc83-3577-80fb-0d962bc36224 | -3.5272 | -59.941299 | 2026-09-22 01:19:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 087c50b0-ee8d-3786-abf7-c7fbd946df51 | -2.8754 | -57.785301 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e587b6f1-17c6-32a2-87ed-bd741f603fb8 | 0.2305 | -60.645199 | 2026-09-22 01:19:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e72fcaf2-8982-3a28-910f-86369f739eb3 | -3.1769 | -61.204498 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e06d1f99-3b19-36a7-8e4a-708a4611e104 | -9.8782 | -55.726398 | 2026-09-22 01:19:00 | METOP-C | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1edd3042-fd90-343c-813a-d1437ce38a9f | -11.8675 | -46.8498 | 2026-09-22 01:19:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62c462ef-e770-39bc-a140-cfa91cc6ec51 | -7.3951 | -55.2281 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad55fe79-7c13-31f8-a2d7-6bead212b101 | -6.1683 | -57.702301 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 658ce629-5318-338d-8957-c1f7c00a4816 | -8.2452 | -55.241699 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 959db7eb-1afe-3e9c-97a3-2a98bda12dd0 | -8.6009 | -54.610001 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3033386-f5ef-3fc3-b070-d3428b247532 | -3.0093 | -54.1717 | 2026-09-22 01:19:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2ad6b9d-18a2-3d02-b378-2e1e5e9dadb3 | -6.0523 | -57.825001 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4af52c9c-5abb-38bc-b663-656ef4263441 | -6.1348 | -59.938 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2042756a-49cb-3e0c-b051-0174b6d459e9 | -2.8673 | -57.7948 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2c0a684-8113-3a26-8fac-e1d784383d4b | -3.0625 | -61.290199 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 661d4959-4483-354f-8428-5f9941d3d269 | -5.4609 | -60.147099 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09776dce-6a0b-34cb-95e5-ad5fa0cb0fec | -7.3931 | -55.219601 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8811c2c6-3cc7-3d4a-8920-26d6b14a1dff | -3.0641 | -54.403702 | 2026-09-22 01:19:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39050cf8-a6f0-30da-864f-d87a290eba79 | -7.7138 | -61.236301 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fe4d0a2-e70f-3522-9618-5e8e04754b84 | -9.8685 | -55.728699 | 2026-09-22 01:19:00 | METOP-C | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd86bba2-ebec-358e-b3ce-a71a58f2e0b7 | -10.6021 | -53.993099 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b7ced9f-b0dd-3f4a-ae20-8fb0c6d632e7 | -6.3173 | -59.9706 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 832ec678-26e4-32c2-91fb-0920d51ad148 | -3.195 | -60.426498 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2958d955-e6f7-373f-a4ff-ad16e7244f2e | -6.0442 | -57.8344 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e857eb5a-6d42-3912-9926-66598c59b0cf | -3.6903 | -60.563801 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| acc6c61f-4d98-312b-8caf-4dbc4f736abd | -12.7922 | -54.027 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe195643-3604-33a7-91f0-4550114c8440 | -10.8752 | -56.234001 | 2026-09-22 01:19:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6cb45da8-1b3b-317e-bfba-f454a4895b59 | -6.0507 | -57.818001 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2bb646d-e917-3c4e-9600-958ff266b24b | -3.1101 | -61.408501 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51c6c7fe-4073-35a1-8734-ad220a8bbc0b | -6.0964 | -57.6143 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bef6739-fe83-3b82-b68f-f794e387da8b | -4.6643 | -56.033401 | 2026-09-22 01:19:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85506d25-b3f9-32c0-91a4-79a710e84a0c | -6.1602 | -57.711498 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 131c7176-d618-3799-be74-5ede657efa52 | -7.5761 | -57.676201 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7c41619-316f-303b-9a33-e0b10fc1f78c | -9.9471 | -53.9771 | 2026-09-22 01:19:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47856d83-20f4-357b-857a-e7ecae7102d1 | -10.6097 | -53.981602 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d62569be-c3d0-3fce-a790-b5a22c957546 | -6.266 | -55.4296 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1882bbca-fa41-3dab-8d5c-8107b0f7d3db | -8.2473 | -55.294102 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0954b7d2-d94d-398d-9114-09a459170000 | -4.0691 | -56.2229 | 2026-09-22 01:19:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cc904d1-eaed-39f5-a5b5-180e3410b6c1 | -9.5943 | -47.7878 | 2026-09-22 01:19:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf96b13c-46d3-3bd0-83ea-52829c230185 | -6.9773 | -47.514702 | 2026-09-22 01:19:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94163383-bbba-3104-a84a-12743cdc8e74 | -3.6821 | -60.573002 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df40ca5c-f07a-3281-a9b1-6b77b452c19c | -6.3575 | -58.297401 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 348fd1dc-7a2d-35f2-9c6e-932079a9a1f2 | -8.4888 | -57.6068 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e06fa2a2-cc6b-32a3-951e-1f2264775a43 | -6.5238 | -58.303101 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 842afbb2-7d9e-31c2-bbfa-0570c4b5c835 | -6.6246 | -59.916698 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 901fead8-f1c3-3d91-b839-d67cc966604a | -7.2867 | -59.519402 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c51d75b-e3e8-33c6-8684-b247f9e99232 | -6.1945 | -57.7705 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dcacd5f-d7b9-39ae-9e2f-c2b2eb182629 | -6.9301 | -59.628399 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 810fd7ef-6e49-35df-a645-3b3ee8f93c94 | -3.4949 | -59.575802 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91f60f14-0dca-364b-8f2b-11e7446fb8e9 | -3.7245 | -60.578098 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce42949-e6cd-3d69-a446-da2521e74ec4 | -6.4528 | -59.9772 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a9e06eb-9960-3c77-9424-c328fef91474 | -6.7793 | -58.606602 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0baa2ee3-c812-3137-9f66-1088562cc152 | -11.3334 | -51.376099 | 2026-09-22 01:19:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 26128146-fbac-3e33-b276-98ff69fc9ed8 | -6.6982 | -56.168201 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e88c0a1-d1aa-306b-9962-4ab473f5868e | -6.1313 | -59.968102 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0fb95292-4e2d-3453-925e-0de7dadabb86 | -3.0461 | -61.263599 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08b95cf1-8dbd-39ad-8986-315763bc4dc2 | -3.2261 | -61.058701 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9480db2a-fc6b-3adf-9981-9c4ddab7ac7e | -7.5778 | -57.683201 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4985746-8b37-3e3a-8347-3a7599e4bf50 | -2.792 | -59.883598 | 2026-09-22 01:19:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ead507da-ebc8-3b64-bbc1-b74ac2091998 | -11.3203 | -54.055901 | 2026-09-22 01:19:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ecc66ee-9735-3d2a-b745-7f6106b2a03b | -2.8625 | -57.819 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09e252ae-9621-3d44-a0f0-e490feb4c4e1 | -6.4494 | -60.0075 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20a0c9e9-590c-377b-b453-4ba105a9be7f | -3.6819 | -60.617001 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92a39ee2-0d83-30d8-8971-4d2d77e60efd | -3.9239 | -60.548302 | 2026-09-22 01:19:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6fc1f63-ed7d-3ef5-bc79-de35f021f3e9 | -9.6789 | -54.322701 | 2026-09-22 01:19:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0d530af-7bb9-3ce8-b3ea-76d9c6049e5c | -3.1081 | -60.722801 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5fc4374-d3cd-30de-ab23-e27b170384af | -6.0201 | -55.349998 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81fcd922-5bdd-30e9-a4ce-91beac0ccddc | -3.4675 | -59.5462 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aae49e97-bc0a-3358-a4b5-5c29cd1477e7 | -6.8894 | -59.857601 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af0dd38d-63d6-3010-93c4-08651d2e4b4d | -8.2414 | -55.2691 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2fcc208-ef82-337f-835d-082768dc07da | -6.1013 | -57.635601 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15f35192-2b40-3db3-bf18-302716a0fdbf | -11.3236 | -54.026798 | 2026-09-22 01:19:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a35b9dc-065c-3b21-82b2-180c081afe37 | -9.8703 | -55.736401 | 2026-09-22 01:19:00 | METOP-C | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
