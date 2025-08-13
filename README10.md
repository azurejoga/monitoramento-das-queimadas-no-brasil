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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aabbd87-7ddb-3c87-9dbb-2726bc43d693 | -9.1894 | -59.6558 | 2025-08-13 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5f495010-200d-371f-a6e8-e3e559042e79 | -12.4788 | -46.9694 | 2025-08-13 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e18f43f2-cb0a-3bc6-9b1c-b9aa3d4860c6 | -12.4985 | -46.9441 | 2025-08-13 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 43c195d3-e9f9-3ca6-8692-3c9132a401dc | -12.4981 | -46.9666 | 2025-08-13 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 3286a243-55e1-3838-8e06-1bdeb8f35869 | -9.208 | -59.6548 | 2025-08-13 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e0b62103-1bb8-30ff-9000-44352800abbb | -12.4793 | -46.9468 | 2025-08-13 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| bc00aba3-fe25-3b1c-ac87-17ae8b7b534c | -2.9108 | -48.254 | 2025-08-13 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| af5016d8-42e7-3341-a950-a1020fefb06b | -8.106 | -55.5701 | 2025-08-13 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| cfebff5d-28b5-39c9-add4-a45171bb25ca | -7.0935 | -60.0237 | 2025-08-13 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 0825f5e0-36e5-3c86-959b-261e5559b307 | -2.8923 | -48.2546 | 2025-08-13 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f19d0cc9-dfff-36b8-87f0-aa358686ee30 | -7.1298 | -60.1374 | 2025-08-13 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c64802bd-510a-308e-a0fb-66d19fe0a125 | -11.7699 | -48.18 | 2025-08-13 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 22e61007-91d6-3efb-a851-e194a9daf6b5 | -11.7695 | -48.2021 | 2025-08-13 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ddb5efb9-f6d8-3e2a-9a52-37cfec604602 | -12.5173 | -46.9639 | 2025-08-13 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 060e084d-f6b2-31da-989d-d4be233dab6d | -6.6112 | -43.8941 | 2025-08-13 02:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 297ff703-8662-3e90-8dd5-5597a4a4a2fb | -7.1299 | -60.1182 | 2025-08-13 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 8ee174fe-0fa7-3210-99c4-a1db99b554f7 | -8.1246 | -55.569 | 2025-08-13 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 7d6c27b2-01dd-3ebe-afd0-e9afee98aa96 | -2.9108 | -48.254 | 2025-08-13 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b15a3605-265f-33e4-84eb-9c6092ffb401 | -7.0935 | -60.0237 | 2025-08-13 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 5e576ce7-cd60-33dd-8622-30261fc50019 | -12.5173 | -46.9639 | 2025-08-13 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 92f5fe90-0523-3ed9-8e06-464ad23af653 | -11.7699 | -48.18 | 2025-08-13 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 33b7aa21-588b-3fd1-aad3-4dfa166bb5ce | -12.4981 | -46.9666 | 2025-08-13 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 223e414a-8fc5-34f5-8570-84fdfe4a6d45 | -8.106 | -55.5701 | 2025-08-13 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| bd433992-d666-390e-a606-e0c28c63022f | -11.7695 | -48.2021 | 2025-08-13 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 36865cf8-0871-38ea-b86b-f681c46032a0 | -2.8923 | -48.2546 | 2025-08-13 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 53902bcc-1120-3e5f-a686-55c119a55fa7 | -7.1299 | -60.1182 | 2025-08-13 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9f64d35e-c235-3c3f-9506-82d76522a1ef | -12.4788 | -46.9694 | 2025-08-13 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| cb07ba34-7296-3acb-8616-a21614f08929 | -12.4985 | -46.9441 | 2025-08-13 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 9ebdfad0-6fb2-37a5-8308-ad7328460ad5 | -12.5365 | -46.9611 | 2025-08-13 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 1ee37da0-f1c9-3f3c-ae0b-a6fb229c71b8 | -7.1298 | -60.1374 | 2025-08-13 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 36493031-dad5-3b43-844a-3d86b0bb9ccf | -9.1894 | -59.6558 | 2025-08-13 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 02a63a56-a3ac-38bd-a7b6-b134b205aa1a | -12.4793 | -46.9468 | 2025-08-13 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 67eb012e-3e00-34f8-af99-0d11745092bb | -7.1483 | -60.1174 | 2025-08-13 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 47fbb062-3d3c-3fd8-8740-5bc08cc5c24a | -2.9108 | -48.254 | 2025-08-13 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 0e3c1766-584b-3787-9238-a5df14f1bdec | -11.7695 | -48.2021 | 2025-08-13 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 74ea41d6-6881-3aa7-8ac1-198c8ff39900 | -20.896 | -49.0653 | 2025-08-13 02:20:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.3 |
| 9f06ee90-9b07-3a75-a9c4-e0ffb7c079ab | -9.1894 | -59.6558 | 2025-08-13 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 191752c6-a9af-3f0d-bb0c-b23eb320a87f | -7.1298 | -60.1374 | 2025-08-13 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| b5fe3d0f-d8dd-32ff-ba21-731aa13d5cb0 | -7.1299 | -60.1182 | 2025-08-13 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a5c92859-58e4-3a7c-96b7-5dff6e9ec6e5 | -22.3869 | -45.4716 | 2025-08-13 02:20:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.6 |
| ab6e94d5-f4e9-3d91-a5e0-6cc86d20e7d7 | -7.0935 | -60.0237 | 2025-08-13 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d60851b7-0370-3658-a07f-d49eeece2c8a | -20.8755 | -49.0699 | 2025-08-13 02:20:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| 44d74fd5-f643-3e2d-a03d-39f0d19708ae | -8.106 | -55.5701 | 2025-08-13 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7ac8f3c8-900f-3e14-9bfd-e093f115897a | -11.7699 | -48.18 | 2025-08-13 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f4763aa4-fc3c-30b1-a6bb-20094befca03 | -2.8923 | -48.2546 | 2025-08-13 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 20953621-115b-39d1-89a8-98ec0d6c477d | -12.6901 | -46.9612 | 2025-08-13 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 8ae6aed8-50a5-3ec2-8e19-f07ac937cd93 | -8.1061 | -55.5501 | 2025-08-13 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 488d3558-f797-361c-9f99-e7f10ece1e0c | -7.1298 | -60.1374 | 2025-08-13 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| dc01f1a0-99c5-3fed-a825-b44e7d2faba1 | -7.1299 | -60.1182 | 2025-08-13 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 9785d5b7-88e9-30c0-aeb0-b935add6ebb1 | -11.7699 | -48.18 | 2025-08-13 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| d812811f-3531-3ca5-91fd-35c60d1fbd22 | -2.9108 | -48.254 | 2025-08-13 02:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| a2e669e5-980b-36f3-bd45-096975f8e82b | -8.106 | -55.5701 | 2025-08-13 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |
| ee7aa99b-83f6-3349-8b68-9d2713a2ffc7 | -7.0935 | -60.0237 | 2025-08-13 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| cd91249e-35c1-33ca-8203-754db46561d2 | -11.7695 | -48.2021 | 2025-08-13 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 16dc1bad-c2fe-36af-98ff-f33273fe4d44 | -9.1894 | -59.6558 | 2025-08-13 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a54a3b89-0848-3103-9b63-f85c12439117 | -8.1246 | -55.569 | 2025-08-13 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 2631a977-80ea-393f-8c70-297ac0047074 | -9.208 | -59.6548 | 2025-08-13 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 4a5581c3-70ad-307a-a97a-9312ee1a19f6 | -6.6112 | -43.8941 | 2025-08-13 02:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f0a5bea0-33d3-31d9-befb-d0aaa6622cac | -2.8923 | -48.2546 | 2025-08-13 02:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6aa73313-7c6e-36dc-b150-be429091426b | -12.5365 | -46.9611 | 2025-08-13 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 53765e22-0bd1-331c-80d6-944938062771 | -18.5505 | -46.0369 | 2025-08-13 02:40:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 869d129c-c504-3c12-a54a-6fc408cbc7da | -2.9108 | -48.254 | 2025-08-13 02:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f0b4755a-3a06-36d0-8740-131914a96133 | -7.1299 | -60.1182 | 2025-08-13 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c16a111c-dfa4-3131-b04a-adc0ee1c0164 | -7.1298 | -60.1374 | 2025-08-13 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e7aee448-b4c4-34b2-9378-e844e7794410 | -8.106 | -55.5701 | 2025-08-13 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 8a0eee1c-1755-3f79-86cc-f26cbff8c37b | -11.7695 | -48.2021 | 2025-08-13 02:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 6948fe44-cb82-3f44-a300-4bc410d079a3 | -11.7699 | -48.18 | 2025-08-13 02:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 0c832980-b863-337d-a070-504ea9e964b6 | -12.5173 | -46.9639 | 2025-08-13 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 41ecf336-657a-39d6-adcd-34252c662e5e | -8.1246 | -55.569 | 2025-08-13 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 31fa2114-fed2-31a5-ba70-6c3ee19280ba | -12.4981 | -46.9666 | 2025-08-13 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| acf7bb12-44bf-37b3-84e0-e5fa0c2d8e99 | -11.7699 | -48.18 | 2025-08-13 02:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 6730314c-a1b9-3b51-afce-df6e3e7b816e | -12.5746 | -46.9781 | 2025-08-13 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 871f44af-ad13-3113-93f6-c43dbd7a8d15 | -2.9108 | -48.254 | 2025-08-13 02:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 606b38a1-4176-353c-a1f6-121a83a0d745 | -18.5499 | -46.0606 | 2025-08-13 02:50:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 34dff21d-3012-3f25-b093-5e7a91fd28a9 | -7.1298 | -60.1374 | 2025-08-13 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b483ec61-1306-3b28-9b8c-6da683bf227c | -7.0935 | -60.0237 | 2025-08-13 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 469bfdda-416d-3102-bace-d813a876e3c4 | -7.1299 | -60.1182 | 2025-08-13 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| d9d78f20-dccb-3749-b6fb-4c8cdcbb40a8 | -9.1894 | -59.6558 | 2025-08-13 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 2b2079f2-3414-38e7-9932-f3f83ea863e2 | -18.5505 | -46.0369 | 2025-08-13 02:50:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 3c81926a-8654-3148-b2a8-9ffe3105e5a0 | -8.106 | -55.5701 | 2025-08-13 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| d89bc392-0ad0-37c9-8974-e9dccc29c557 | -5.18179 | -37.65815 | 2025-08-13 02:58:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bdf81e82-5036-3aa2-ab46-bef6cc061823 | -5.26285 | -36.17101 | 2025-08-13 02:58:00 | NOAA-21 | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 73c8cc81-cde9-3e28-ad07-0702dda643c5 | -5.18628 | -37.65939 | 2025-08-13 02:58:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 27c3e552-0202-3ae6-b07e-9bf6433d0979 | -7.1298 | -60.1374 | 2025-08-13 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 5e19c1ca-81fe-34e7-8660-4f3cd8ac8f68 | -11.7699 | -48.18 | 2025-08-13 03:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| d779915e-49d3-3704-8a21-c64422df3107 | -18.5499 | -46.0606 | 2025-08-13 03:00:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 4963ac3e-a395-3ad9-9f20-be13a2c203d3 | -7.0935 | -60.0237 | 2025-08-13 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ced90eac-4d10-38a5-811a-e0b216b869d9 | -8.1246 | -55.569 | 2025-08-13 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ac9735d0-f131-3501-8750-0bc70990b15b | -8.106 | -55.5701 | 2025-08-13 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a5762a99-1fd5-394e-8763-bcf9d6155380 | -11.7695 | -48.2021 | 2025-08-13 03:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 8990b6e0-12c7-3971-96c3-d3d50d023000 | -7.1299 | -60.1182 | 2025-08-13 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ad184b40-4525-39ac-8b97-c7dfef0d9eec | -18.5303 | -46.0414 | 2025-08-13 03:00:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 344daf1b-e1cd-379b-9828-3e55c4a3c032 | -2.9108 | -48.254 | 2025-08-13 03:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| cd5d8ce5-a065-3dc0-8023-31609aa4b8d9 | -18.5297 | -46.0651 | 2025-08-13 03:00:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 58e2a90f-ca8a-3e6a-a361-36ed8378ee33 | -9.1894 | -59.6558 | 2025-08-13 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 660c1f2e-2e76-3727-8ba5-e0531652a9d1 | -9.49962 | -37.72438 | 2025-08-13 03:00:00 | NOAA-21 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ba06052b-1d30-32f5-824e-77fb27762c39 | -18.5303 | -46.0414 | 2025-08-13 03:10:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 0fa22b16-9196-3e0b-a586-c49ba9880d20 | -18.5505 | -46.0369 | 2025-08-13 03:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 4c36f477-1032-3ddf-8aac-147caca461cf | -11.7699 | -48.18 | 2025-08-13 03:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 233c8e34-f01e-3946-923a-97db438852b4 | -2.9108 | -48.254 | 2025-08-13 03:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |


[Clique aqui para ver as próximas entradas](README11.md)
