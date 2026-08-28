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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b405a36-3700-31ab-8275-810bd4bbf8e7 | -4.5507 | -44.0668 | 2026-08-28 20:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 07c5f796-9bb6-34b5-9dd5-9d272344f767 | -10.7407 | -54.0401 | 2026-08-28 20:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| faa316e4-c696-338f-ad0a-4fb117dfe56f | 0.1367 | -60.412 | 2026-08-28 20:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 87.6 |
| e6bc09aa-5f88-34d1-bc85-52a83b1a8d0f | -5.1414 | -44.967 | 2026-08-28 20:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 156.3 |
| e83af4f0-91f5-3042-87b9-20c1fd268211 | -12.3611 | -50.5846 | 2026-08-28 20:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 301b1527-050e-31ea-b5a6-c4c30f3a84e9 | -11.4968 | -45.1071 | 2026-08-28 20:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f647a6fb-575f-3f23-ac68-05de0812ecbc | -9.0012 | -57.5585 | 2026-08-28 20:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 6c6a2609-f659-3d4a-8610-a83042d3bf5f | -6.3465 | -44.1013 | 2026-08-28 20:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 245.7 |
| 8b1aee2f-b34b-3802-94d2-199b46d06179 | -5.2709 | -45.1173 | 2026-08-28 20:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| c3aa10c8-66df-3088-9033-4f15f0037a55 | -4.5695 | -44.0427 | 2026-08-28 20:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 5ae8a83c-9fa2-3aee-abe3-75b395f3f4dc | -8.0301 | -48.0145 | 2026-08-28 20:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 90fc9041-56b4-3049-82e8-d9782f0a1ad6 | -6.857 | -59.4371 | 2026-08-28 20:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| e23f2f6c-ec70-317c-8293-7ce84f044ae2 | -2.7119 | -47.043 | 2026-08-28 20:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| b4c2305a-79d2-3596-9886-491bdaefe8d0 | -3.913 | -60.9395 | 2026-08-28 20:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| e7ecac59-ed5a-31e1-897c-0d2dd1458dd2 | -2.7304 | -47.0424 | 2026-08-28 20:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 3776cda3-1761-3b31-9ab5-8d61e0bfc279 | -20.9606 | -57.6086 | 2026-08-28 20:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 80dbfb45-80a2-36fc-8ffb-6513104e62aa | -9.9102 | -60.4287 | 2026-08-28 20:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| b1ac38f3-726e-3e6c-abcd-f08189577e6f | -7.5289 | -61.3825 | 2026-08-28 20:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| ebfb3f7d-2e83-332d-92e0-ecc6f6a8f63e | -6.7247 | -60.0189 | 2026-08-28 20:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 2997ca56-d8e4-3209-b29b-4c126a0d153f | -7.529 | -61.3635 | 2026-08-28 20:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 120.4 |
| cd556187-b8ee-331a-b064-5fdfe0329583 | -12.3803 | -50.5823 | 2026-08-28 20:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 5f849805-4633-3e64-b3d6-bb1a98a8f495 | -6.7652 | -63.054 | 2026-08-28 20:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 859d8fd1-c00d-324a-ae20-0c4c75d0ce62 | -5.2446 | -43.7457 | 2026-08-28 20:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 160.5 |
| bba20746-5da7-3330-8b4f-e00bb8fa4352 | 0.1367 | -60.393 | 2026-08-28 20:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 45a3a360-bb28-3410-84f2-7bdddbf8afe7 | -5.9078 | -57.77 | 2026-08-28 20:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 9dfa7d57-7c33-34a1-814f-9090190eaf57 | -3.6216 | -60.547 | 2026-08-28 20:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 141.7 |
| b37a8d05-f155-3277-9da4-25b468b8f5cc | -9.971 | -53.9214 | 2026-08-28 20:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| e9ed1744-f066-390e-a5fa-66c3cabc7ae6 | -9.9708 | -53.9419 | 2026-08-28 20:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 42403bac-f9fa-3427-8e67-d61ef9439f16 | -14.9193 | -56.3237 | 2026-08-28 20:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 4bbedd3f-3c82-37fe-bc75-49174d8473bf | -8.5366 | -55.2625 | 2026-08-28 20:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 8e23d88d-e26d-32dc-9ab2-a59185270d48 | -11.4972 | -45.084 | 2026-08-28 20:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| b17d38eb-fe23-3833-8aa7-d15244445d71 | -14.4856 | -58.5074 | 2026-08-28 20:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ca96d59c-aedc-3fc2-b2c6-7a999a80a52f | -6.7699 | -55.6644 | 2026-08-28 20:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 211.5 |
| c9e039e3-6ccb-332b-af40-8461e5aa3ba1 | -6.7833 | -59.4208 | 2026-08-28 20:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 29fdd848-3465-36f7-a660-390698a398b5 | -11.1729 | -51.2516 | 2026-08-28 20:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 86e0f5d4-08f9-30c8-9620-1f8242f3f7e1 | -10.4085 | -61.1915 | 2026-08-28 20:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 0a5385ee-120c-3f01-84fb-c449f37fe325 | -6.4908 | -53.2629 | 2026-08-28 20:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| cd9c4827-8809-322c-90bb-193c9161dfdc | -3.6033 | -60.5474 | 2026-08-28 20:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 224.4 |
| 92e000f8-fa22-399d-8d5a-92280eaaf0fe | -14.3569 | -51.6995 | 2026-08-28 20:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 176.6 |
| cd411e27-1932-39aa-87da-dc52c50510c7 | -6.0391 | -44.9042 | 2026-08-28 20:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| dc31f0ba-38c6-31f2-bad2-a09d66f3ae81 | -7.5516 | -69.9963 | 2026-08-28 20:30:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 137.5 |
| be25e4bc-8e71-3658-82a1-e7e98f5dad0b | -14.5032 | -52.17 | 2026-08-28 20:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a7b41f4b-e69b-3002-8b3a-13a745eede08 | -12.7797 | -44.2576 | 2026-08-28 20:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 34ee6f01-ff35-3264-82fe-b2e2644ba7e6 | -11.1726 | -51.2728 | 2026-08-28 20:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 8e07ab2f-468d-3c1d-8e84-540c12a4eaa9 | -8.6156 | -54.7743 | 2026-08-28 20:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 2683fb20-7f11-31c4-ae3b-7751dadd87b4 | -14.622 | -50.9117 | 2026-08-28 20:30:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 6b856b09-3239-3dde-bd05-1efd898aefcc | -4.9778 | -49.623 | 2026-08-28 20:30:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| d7fc09d8-9df0-3b6f-bede-ce4f09d22193 | -6.9521 | -58.9506 | 2026-08-28 20:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| db9678b0-11de-3927-ae95-830b749b0e26 | -9.8739 | -60.2955 | 2026-08-28 20:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 5ac7110f-0e5d-3766-b4d5-ef27cc35e385 | -14.9011 | -52.6267 | 2026-08-28 20:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 7b4ff668-b8ad-37f2-a7a2-8f13df242b9e | -10.4502 | -46.1826 | 2026-08-28 20:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 41c045c4-c4a6-328e-8067-dbbfa95e3467 | -9.8028 | -46.373 | 2026-08-28 20:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 65eebe85-a31f-37a8-9139-36093f02f98e | -12.7603 | -44.2608 | 2026-08-28 20:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 0aceef26-fd75-35b2-85a8-20ce48a29eb2 | -8.5971 | -54.7553 | 2026-08-28 20:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 32e43164-bbce-3dfb-883e-8fec2b2f5b90 | -14.1597 | -53.1219 | 2026-08-28 20:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 6d50a1b7-b65c-3ce7-a0ef-d86340858182 | -8.5785 | -54.7566 | 2026-08-28 20:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| cfa62ef5-fc1f-36b1-8b8c-332826b4fa81 | -9.1425 | -61.0069 | 2026-08-28 20:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 5f9c03b4-9ab1-300f-99b8-9fbb29fed575 | -9.4329 | -51.6926 | 2026-08-28 20:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| a3fceb39-54c8-3300-a3c2-6d5179da3a15 | -14.9389 | -56.3011 | 2026-08-28 20:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| df793e25-5ab4-30c8-a7d4-d86adc3f4eb6 | -14.1982 | -48.7451 | 2026-08-28 20:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 141.2 |
| ccaaba1a-4234-3373-b169-8c2debf03fe9 | -14.3762 | -51.6969 | 2026-08-28 20:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 2f2b3069-c23e-3f8f-9421-8223a5c9b83f | -8.5969 | -54.7755 | 2026-08-28 20:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 1347cca2-f083-3548-9218-cbc451059948 | -9.02 | -57.5377 | 2026-08-28 20:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 74803238-0a81-353b-b963-c09c351b7fe1 | -10.5523 | -59.6161 | 2026-08-28 20:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e2869bf8-a815-3922-9cc0-92355372026a | -8.5968 | -54.7957 | 2026-08-28 20:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 86022cd1-b19d-3519-890b-e55619aa9cd7 | -14.9011 | -52.6267 | 2026-08-28 20:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 5dce502c-4d42-33b1-9409-9138d33ad5c8 | -9.02 | -57.5377 | 2026-08-28 20:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9fd5aa9f-6d57-3059-99a7-d5057861cbf6 | -4.9778 | -49.623 | 2026-08-28 20:40:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 57657450-8230-3c32-8e7d-a4983be4385b | -11.0244 | -49.6872 | 2026-08-28 20:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| af8b1f70-49b3-3802-82b1-dceb36c4eab1 | -6.3279 | -44.0797 | 2026-08-28 20:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a4aa856b-88ae-3108-b831-83d3b933f5d4 | -11.1913 | -51.292 | 2026-08-28 20:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 51a5b102-bc1c-3084-8453-475f6712895e | -10.5523 | -59.6161 | 2026-08-28 20:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 2231cee0-1240-3641-a546-17b9ad6bbf30 | -14.9015 | -52.6055 | 2026-08-28 20:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 087e1b1a-81cd-3aaf-89d0-573412903a86 | -8.1617 | -64.0047 | 2026-08-28 20:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 8206546a-6c63-3e08-b030-4126ed464f99 | -9.1425 | -61.0069 | 2026-08-28 20:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 01469853-30ae-319c-aae0-a838cd6fbc67 | -14.4856 | -58.5074 | 2026-08-28 20:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 2ea3a369-ccda-3293-87e6-f9530456c0e4 | -10.4085 | -61.1915 | 2026-08-28 20:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 71c06bae-22cf-31eb-a427-75c42055c315 | -9.1239 | -61.0078 | 2026-08-28 20:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 6d7db803-332b-3fee-96f8-5ea6f183df58 | -14.1784 | -48.7703 | 2026-08-28 20:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 123.1 |
| ed0410b8-e108-3d3e-b618-c70c939d5d7d | -4.175 | -54.5761 | 2026-08-28 20:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 2d342adf-0244-33d4-866f-f2beb616f98a | -9.4329 | -51.6926 | 2026-08-28 20:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 936dc597-52cd-3290-a024-45f19e3113b6 | -5.4179 | -43.1752 | 2026-08-28 20:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 4582164c-4b33-3f7f-a2f7-a87bc1934e7c | -3.6216 | -60.547 | 2026-08-28 20:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 337593cb-204b-3898-986d-111e394e45b7 | -6.7248 | -59.9998 | 2026-08-28 20:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| a5f2c712-b503-33ff-ab2f-56360873a67c | -6.3465 | -44.1013 | 2026-08-28 20:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 192.9 |
| d0ad3425-1e74-376c-b5fe-249485f00da5 | -5.8711 | -57.752 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e3a7d683-5b65-3d2b-8b26-21e7c877544f | -6.857 | -59.4371 | 2026-08-28 20:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 880ff6fa-1c05-3f30-9fb4-f5e6c958c2e7 | -14.9196 | -56.3032 | 2026-08-28 20:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 6457a46d-dee7-3750-85db-4a331880847c | -11.7165 | -54.5449 | 2026-08-28 20:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 188.9 |
| 0a1fd5dd-9957-3132-bd1a-04c6bcce8920 | -14.9193 | -56.3237 | 2026-08-28 20:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 522f6827-ba96-3ea6-b0b0-b585d921ef8b | -4.5507 | -44.0668 | 2026-08-28 20:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 45a747ef-4138-32fb-8e6c-5761327682f8 | -7.5289 | -61.3825 | 2026-08-28 20:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 27778905-c5b9-34e6-b628-36aec101ee92 | -5.399 | -43.1999 | 2026-08-28 20:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 12ddccca-31ff-3476-90bd-a08804ef8503 | -20.9207 | -57.5723 | 2026-08-28 20:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 89ffeffd-a1c6-3266-b721-3f7bda925906 | -7.5516 | -69.9963 | 2026-08-28 20:40:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 927b73c5-fe5f-392f-b0ba-4f2392c5c948 | -6.1657 | -57.7793 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 645d8bbd-9cc9-3940-a31e-361cc53dbecb | -7.4953 | -55.2862 | 2026-08-28 20:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 20fb9b29-b500-3199-8702-72d815929f58 | -6.77 | -55.6445 | 2026-08-28 20:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 3aee1d7d-0eb2-30b1-9c13-e50c403791ae | -5.871 | -57.7715 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| f5ee2557-5539-31c6-8d2c-a72b5d8eb5b8 | -9.1525 | -49.9639 | 2026-08-28 20:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |


[Clique aqui para ver as próximas entradas](README183.md)
