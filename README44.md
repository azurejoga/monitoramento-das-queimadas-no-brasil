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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5e8bee0-76f8-338b-a811-f34f4bc96551 | -9.39913 | -60.558 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42751873-91c6-351a-8cb3-a7f41afa09fc | -7.36565 | -45.81418 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c2c1b426-1739-3e63-9295-c2e6ee22e776 | -8.11681 | -50.04302 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 72f8663c-e353-3c51-86df-22c4b5ba4a8d | -6.95427 | -52.81342 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd93d150-5579-371d-84b4-07ac30119497 | -9.40131 | -60.41483 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 8647df87-ec80-34be-b8f6-160570dfa2fd | -3.84344 | -59.38019 | 2026-08-21 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c36c7c6-1268-3408-8d04-f05e42c65ae2 | -6.58192 | -59.00031 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6caa2c51-7b9d-347d-ad5f-1179069a8c30 | -6.11729 | -59.90992 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 242dbebd-d51f-30d2-a345-05977525b8f7 | -9.40409 | -60.41684 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 954623bc-5d0a-365c-a041-d01c6ac35d02 | -9.20379 | -60.76517 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e22ac55d-b57c-3efd-9356-5e2df46b7687 | -8.44695 | -46.95164 | 2026-08-21 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e0a5db8-b0bc-3329-9707-83406aa2ef4c | -6.08806 | -57.91545 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf1a0122-bbd9-3647-89c5-5b3bbecf87c5 | -9.11959 | -61.6039 | 2026-08-21 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 764c139a-9001-3b47-bbb6-cdcf7b906c2f | -6.70293 | -59.10086 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a3597a8-1fd1-3af1-9092-7aecfe685fd8 | -7.78036 | -61.15555 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0c41063a-316d-3f1f-a5c6-2bca0cec7755 | -8.58402 | -54.78971 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ff73165-054c-3b0d-af25-0990403d3d6f | -7.36455 | -45.82178 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 63f7e5e1-52cb-36b0-ba88-ad3ecec6226c | -9.21431 | -59.66149 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a503445-2984-352a-b347-6e37d55b6825 | -8.5486 | -55.30519 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f5b2713-d0a8-32f0-b550-e4ada1d6952e | -10.65949 | -49.0262 | 2026-08-21 04:46:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 059508d7-d252-3f78-9c04-6ce77fc152c1 | -6.85763 | -59.43693 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 04a40391-648b-3c52-848a-bf7247fe1676 | -6.66965 | -52.88423 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2509a24e-a7d4-3323-bfbe-ee4fcc6077ff | -8.5775 | -54.78436 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfe9f87e-7a3f-3440-8084-c13daebfca45 | -10.28788 | -48.2163 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 69d3e6bb-9112-3efb-97d6-d5ad2caae67f | -9.46574 | -51.63853 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d254ac6-2411-324f-a7a6-e8103c355d9c | -8.54943 | -55.32348 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c32a7d9f-705b-3e02-b438-b832d3779828 | -8.54803 | -55.32172 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1708a377-c366-3fac-91d2-e4fba97c1e68 | -5.868 | -57.66275 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e58199f-c6b8-361d-8b24-231666b8956c | -8.64428 | -54.72602 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 165a7bc0-e50d-32c7-9238-f21137d8b8a3 | -6.4289 | -54.92817 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f9fec89-d6f6-3d9c-88cb-4450e6e0cd43 | -10.52508 | -50.78096 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b91ba00-f25a-3dbb-a473-9d5b1179f12d | -8.11116 | -50.03473 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0c6ac05f-1875-3dbd-aac0-f6a63a36e8cd | -7.39034 | -47.606 | 2026-08-21 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 126f0e0c-7c20-39f1-aaa3-6bca38f066f8 | -6.64697 | -56.4098 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c96cfae-bdf2-33d2-8e0a-dc74db6bbb0b | -8.38152 | -62.701 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 829fa453-0a71-341e-98fb-60127664cded | -6.21714 | -55.48468 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b863aa4-260f-3b1f-be52-f18102a6d438 | -7.62911 | -45.75292 | 2026-08-21 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e652cd3f-025d-352f-afd3-4fa79478c5c5 | -10.11257 | -54.27124 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40b24494-8e77-3468-8cb1-fcf43d198558 | -8.06876 | -50.10985 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a88e17f-8dbb-3bdf-9fce-e697f19ac52b | -6.69478 | -58.94375 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e3b7b527-83ae-3295-9ba2-532f239fedef | -10.75443 | -50.3317 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71d1d7c2-3fd5-37b3-93fc-73cf79713d8a | -9.0142 | -40.99594 | 2026-08-21 04:46:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7c6f0a8c-35bc-326f-8c9c-e165e01c899b | -7.25515 | -49.90108 | 2026-08-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f640457-296d-39b0-838d-b6bf7a74ffbf | -6.55382 | -49.84908 | 2026-08-21 04:46:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 854420ce-67fa-3faf-b551-85bde614a997 | -7.45802 | -46.15205 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 72d74865-a31f-3fc2-9cd5-d344c2713bdb | -6.89246 | -59.44289 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6ebff432-7120-311f-b38c-265f08ecf26e | -6.33329 | -46.51817 | 2026-08-21 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d483478-804d-336c-a261-41f66258e42c | -7.60732 | -60.94956 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 298ab18a-4885-370b-b109-4de11bbe8b9e | -7.63199 | -45.76884 | 2026-08-21 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1fe8da1-3bc9-39f8-8ff6-1701c3fec802 | -6.71052 | -59.08568 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff26f07c-ad6d-3a59-a06c-dd93dd52a066 | -6.88092 | -56.63689 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 569dd980-4379-342b-9569-67e38b528621 | -6.578 | -58.99403 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5fd4cebc-d1d2-3f5e-a942-a5560709b513 | -8.58729 | -54.74731 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4372ece4-a5d1-3b7e-b419-b62902632035 | -6.93918 | -52.77761 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 200fb662-093a-3532-bb80-2b253988ef06 | -4.0468 | -50.29881 | 2026-08-21 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a4a7a1bb-3438-3cfc-b4ed-33fb0b142c73 | -6.57593 | -58.97702 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1eb240bb-fd3d-3386-bcc9-59ee8f8e1ed5 | -8.54938 | -54.77547 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b9b04d6-45f1-34b4-8844-76b2daa45c76 | -9.20902 | -60.76612 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c598a40-fffd-3a9b-ab15-da4bdc6479ae | -6.65143 | -56.35875 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a29f37b-55ed-3729-b671-26e9f5843850 | -6.11207 | -59.90914 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6e7e9013-1f14-3aa7-8df1-66fe0df10438 | -8.5384 | -54.86395 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f8c29b3-dfd6-346d-abc8-71dd37c3e882 | -6.86773 | -43.73952 | 2026-08-21 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 18b20bb3-99a9-3248-b786-c233c063693f | -9.47013 | -51.63209 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9a02b0b-818d-3b19-a08b-5bb6ecd4c636 | -6.38917 | -54.95119 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6633ab6-30f9-3e03-ab98-94d90d89ee31 | -6.8086 | -58.99862 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fddc7959-5ce8-303a-bac7-8455eb303764 | -8.65335 | -54.63533 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aeadea4-db33-3c4e-bc0a-7572a90be067 | -6.4317 | -54.9489 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4f9bf8f-6873-3be0-9de9-ef493b552b5b | -4.95404 | -56.26489 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4651e056-b0fc-3097-8625-6821c90df187 | -3.90183 | -55.88166 | 2026-08-21 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ed077a7-8c7f-3d72-bf17-46ae2b9eabd3 | -11.48777 | -45.1101 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b17ae0be-d0fe-3e73-9138-62c3bb4ec94a | -6.22661 | -55.40184 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bd5c205-4816-301e-bdac-b79fbdf4b07b | -10.6206 | -51.62111 | 2026-08-21 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e8d7a91-c5f2-3fa9-ba81-3734ad8e8630 | -5.80927 | -55.71627 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d19b19b6-9208-3505-86fd-8ae20464a45f | -7.77485 | -61.15469 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d3f470c6-6c45-379a-a27a-78c8589421eb | -4.94195 | -55.77948 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 49866434-e8e3-3376-b451-1c238acf54b0 | -6.71706 | -59.09398 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 123d73ed-2c7b-3b52-bdef-a5350e74e62c | -9.12029 | -60.92524 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03bf5ea3-1ddc-337c-ae53-f114607dfca8 | -6.66535 | -56.35027 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 48ee76d7-10e9-34c3-a78f-f234192f12ec | -8.49895 | -54.87135 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0ee4539e-2c73-3d6c-8244-2a7379464a41 | -6.42891 | -52.73795 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acc14d15-dd23-34e3-88b4-99f1eafca4e4 | -4.00927 | -48.06052 | 2026-08-21 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ca73f52-58df-357f-9171-c8c532f29d49 | -7.88853 | -61.7111 | 2026-08-21 04:46:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec28f81e-7542-32c6-83fb-e58ac4ff8e8b | -8.58471 | -54.78553 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4e546cd-7573-36d5-8525-a4bc70be248d | -9.39514 | -60.55084 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba711b47-3e62-3582-aa69-e0e547503a8a | -8.05632 | -50.11181 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38864b38-f081-3fe6-b635-475ddaa3dd07 | -8.33458 | -46.50679 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6be1b837-f77a-312e-b6f0-5774006b2368 | -7.24439 | -49.8811 | 2026-08-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08863872-a5f1-3936-a601-6ef46a7174d2 | -6.88866 | -56.43909 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22abd3e3-5d3d-3c38-9f1d-bd795d5acc87 | -5.7174 | -53.72194 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e3e6ab5-381b-35e0-a6ff-1f19919c4efb | -4.92024 | -56.26353 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1ab634b-338e-38c1-8745-b7852a276221 | -6.24735 | -55.39556 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d189fbb8-3687-30d6-a59a-27d7bbee1282 | -6.66132 | -56.34951 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35a51182-3254-3d3c-9f5f-23a84a470c65 | -10.23994 | -54.36705 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef7bb9a5-e3be-308e-9a44-7b5ff6a5b3b1 | -9.50717 | -51.67716 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c70114dc-c1b5-3a31-86e4-c4bcc1a3293a | -6.11567 | -59.9194 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84d648f2-9d29-35f3-bdda-fb5ca95893f2 | -6.05742 | -57.70119 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e80fd137-d8b3-3fff-9614-defab2f8e6c5 | -5.60641 | -44.2215 | 2026-08-21 04:46:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b0c1648-60ab-31d5-9cb9-c7d8648d1785 | -4.95881 | -56.2617 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d008fdbe-a46f-30d6-9ea0-f7dabe6ab7e1 | -8.5679 | -54.66371 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f87ee42d-bf88-3ee8-a00f-761d2bf7abfc | -8.58659 | -54.75153 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README45.md)
