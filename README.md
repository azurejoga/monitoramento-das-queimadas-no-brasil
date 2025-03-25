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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e1e7473-59ac-3127-9bbf-00b9122040da | 1.6503 | -60.1386 | 2025-03-25 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 5d4e9307-9f27-3847-a760-1a7f134e597b | -17.8455 | -39.8705 | 2025-03-25 00:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 103.9 |
| 3b053962-1146-3af1-8eee-e6ccf0b2085b | -17.8658 | -39.8648 | 2025-03-25 00:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 155.3 |
| 5acfacb7-558d-30bb-b9ca-7e3ea089c058 | -17.8463 | -39.8443 | 2025-03-25 00:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 99.4 |
| ebf980fb-3c3e-32ab-855f-960269187c17 | -17.5621 | -40.6183 | 2025-03-25 00:00:00 | GOES-16 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.2 |
| 02b4ae48-f43b-3e9d-aa1a-46736e61df2a | 2.9275 | -60.4455 | 2025-03-25 00:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9f228e1e-b5ad-3b61-a7d8-ceae3ec05b68 | 2.9092 | -60.4458 | 2025-03-25 00:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 95abaf11-8ef6-378c-b486-b9bee888a278 | 1.6686 | -60.1385 | 2025-03-25 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| dfd13684-32f3-3b4a-a1dd-32172d70f606 | -17.8666 | -39.8386 | 2025-03-25 00:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 122.3 |
| ef5d62bd-4379-3912-9086-ded708f829ba | 2.9275 | -60.4265 | 2025-03-25 00:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 21f5f759-184d-321a-b9e9-db4ff47c0f78 | -17.5613 | -40.6441 | 2025-03-25 00:00:00 | GOES-16 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.1 |
| 635b74d2-42b4-3855-87bc-0faa9219c397 | -17.8658 | -39.8648 | 2025-03-25 00:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 183.1 |
| 797a533b-3914-306f-8934-6c995a1cb2b5 | -17.8666 | -39.8386 | 2025-03-25 00:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 141.2 |
| 9a4f1121-ddba-39b9-a662-7514108aac46 | 2.9275 | -60.4265 | 2025-03-25 00:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ba7966fd-0f8f-316b-83ae-64c58dab38d3 | 1.6686 | -60.1385 | 2025-03-25 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f1482f92-ea7d-3eda-9287-107dc50a4daf | 1.6503 | -60.1386 | 2025-03-25 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| eb12603f-1fea-3fe4-b30c-2bf937a72a4e | -17.8463 | -39.8443 | 2025-03-25 00:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 99.6 |
| 82404ab9-53f6-3473-afe3-86e16dc3ad0b | 2.9275 | -60.4455 | 2025-03-25 00:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 03d19e14-ac3c-3c04-af11-dde27387a4d8 | -17.5613 | -40.6441 | 2025-03-25 00:10:00 | GOES-16 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.1 |
| b7066de6-eac3-3594-89fd-37747857d4d3 | 2.9092 | -60.4458 | 2025-03-25 00:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| fb17edde-d1da-3054-8236-e329e53432b8 | -17.8455 | -39.8705 | 2025-03-25 00:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 101.3 |
| 15588825-4553-3af2-8c35-0a4375eb1522 | -17.8455 | -39.8705 | 2025-03-25 00:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 91.6 |
| 96f26921-1283-3cd4-a0b9-5b57209478d5 | -17.5613 | -40.6441 | 2025-03-25 00:20:00 | GOES-16 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.3 |
| 871797d0-a9a0-3480-ab0c-5f1599cd3f4d | -17.8658 | -39.8648 | 2025-03-25 00:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 179.6 |
| 8a979fd2-fa74-3125-b14d-f6b10744c451 | 2.9092 | -60.4268 | 2025-03-25 00:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 81de2645-3744-31e7-b66b-2f6d747cb79e | -17.5621 | -40.6183 | 2025-03-25 00:20:00 | GOES-16 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| a17e928b-6a07-32fa-8b28-8e9cfbab60dd | -17.8463 | -39.8443 | 2025-03-25 00:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 108.0 |
| 0da6aaa5-2c79-3ffa-ad26-4e7de37e2271 | 2.9092 | -60.4458 | 2025-03-25 00:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.7 |
| ae338d68-2469-35c4-83d1-98bcc1020efb | 2.9275 | -60.4265 | 2025-03-25 00:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e13cedf4-b2fc-3ade-916e-14a5cca605d4 | -17.8666 | -39.8386 | 2025-03-25 00:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 155.4 |
| d8586c8b-a2ec-3057-8fa0-d62057e241cf | 2.9275 | -60.4455 | 2025-03-25 00:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 363148ed-9b61-3061-bcd6-67005c69af5f | 1.6686 | -60.1385 | 2025-03-25 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 55185415-867b-30dc-9668-2f5a71aee1e3 | -17.8455 | -39.8705 | 2025-03-25 00:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| da1fe40f-133d-3b8d-abc3-f9c6544ecb17 | 2.9092 | -60.4268 | 2025-03-25 00:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| be20547d-a29c-3b29-8821-551b62d1fef1 | 1.6686 | -60.1385 | 2025-03-25 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c3f15f0d-9424-3fe7-89f3-84e0f6ecb23c | -17.5613 | -40.6441 | 2025-03-25 00:30:00 | GOES-16 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| e851fadc-9c4a-3778-9685-d030056e9331 | 2.9092 | -60.4458 | 2025-03-25 00:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 53d95138-7eee-3090-972c-80426fa54ae8 | 2.9275 | -60.4265 | 2025-03-25 00:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 82.2 |
| cb53a588-c733-3a23-b7fb-c986443040ad | -17.8666 | -39.8386 | 2025-03-25 00:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 94.9 |
| 36a8024e-0441-3648-bfb3-0d104dbc187c | -17.8463 | -39.8443 | 2025-03-25 00:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| d5f6146a-d109-3ea8-9c46-6fcaedd83506 | -17.8658 | -39.8648 | 2025-03-25 00:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 112.3 |
| b8891a4d-867f-3548-bd0d-9ace0cd8b035 | 2.9275 | -60.4455 | 2025-03-25 00:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d404a921-6051-36a7-9181-beff4b3f696b | -17.55636 | -40.65115 | 2025-03-25 00:39:00 | TERRA_M-M | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| e1a55661-fada-3b0a-89eb-1e5721c88d8c | -15.5085 | -42.59776 | 2025-03-25 00:39:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f9a2099e-bbf4-33ca-b6e7-e27ef00c345f | -17.86484 | -39.87771 | 2025-03-25 00:39:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| e92405f9-da46-3551-bb4b-7cde611af047 | -15.5104 | -42.60978 | 2025-03-25 00:39:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| 9f946a21-bd46-332c-aa9f-ba5f50e7b55d | -17.55388 | -40.63604 | 2025-03-25 00:39:00 | TERRA_M-M | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.6 |
| 1d4df66a-389a-32f8-b7ce-f6ff65147a41 | -15.5095 | -42.60347 | 2025-03-25 00:39:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f1049ea4-0895-3957-8e71-3648550ead85 | -20.01684 | -49.75152 | 2025-03-25 00:39:00 | TERRA_M-M | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 28816f7f-6de5-3087-8a09-953e57933e58 | -20.78169 | -49.85763 | 2025-03-25 00:39:00 | TERRA_M-M | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| a15c8b8f-388b-3b12-9469-6cf61391b10b | -20.25812 | -40.80132 | 2025-03-25 00:39:00 | TERRA_M-M | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 4f81b60e-2f63-3b62-a328-83cb8bf59fcf | -19.8393 | -40.86552 | 2025-03-25 00:39:00 | TERRA_M-M | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 1091d792-6e0a-36b8-ac80-20986d634a4c | -15.51131 | -42.61543 | 2025-03-25 00:39:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 95307ef2-008c-3d81-80a4-bad479bf1ae7 | -20.01514 | -49.73649 | 2025-03-25 00:39:00 | TERRA_M-M | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| 47e20cd0-8dfb-3b82-b5dd-88ea0e8b88c7 | 2.9092 | -60.4268 | 2025-03-25 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 5f8663a8-6006-3ed3-bb8b-e80fb4390650 | 1.6686 | -60.1385 | 2025-03-25 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 6cc567ab-6d2e-35f6-84d7-e691404d7814 | -17.8463 | -39.8443 | 2025-03-25 00:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| d7569cf9-c338-352e-b923-5a696bcdbe29 | -17.8455 | -39.8705 | 2025-03-25 00:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 79.6 |
| d32db077-5a7e-324c-8eec-dba92a78f4c7 | -17.8666 | -39.8386 | 2025-03-25 00:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 81.5 |
| 533e4a1b-0ccf-36c7-bb13-701711208196 | 2.9275 | -60.4455 | 2025-03-25 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| cb045c85-0765-39b6-8be4-50a21c43b10c | -17.8658 | -39.8648 | 2025-03-25 00:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 138.1 |
| a9e6208c-7af3-32da-8ffe-c1281114f8cb | 2.9092 | -60.4458 | 2025-03-25 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| a2bd1bef-6572-3a36-b3e3-42796c21ae1c | 2.9275 | -60.4265 | 2025-03-25 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c7fc534e-c168-3980-b43a-45bd9821294a | -8.10776 | -43.13798 | 2025-03-25 00:41:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1ea22c38-7f29-389a-b7ed-6af3c5304ab3 | -8.10569 | -43.12409 | 2025-03-25 00:41:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f5b536c8-7aa6-305a-bfbe-e64ce3d93e03 | -3.25893 | -49.13354 | 2025-03-25 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ba36793-c1bf-32aa-b637-2fae5de5dbb7 | -3.26016 | -49.14243 | 2025-03-25 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a2232423-4acd-3ef0-924b-14770e52d8fe | -3.78508 | -41.60364 | 2025-03-25 00:43:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 2a5a877c-e1ea-34c9-a459-0598fb4d6643 | 2.9275 | -60.4265 | 2025-03-25 00:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| cc88aef5-58a5-3c8a-aceb-0fee465a5363 | -17.8463 | -39.8443 | 2025-03-25 00:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| 38c1a6cd-4b2d-315e-bdfe-c910d922ba71 | -17.8666 | -39.8386 | 2025-03-25 00:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 126.3 |
| f232b31c-0085-3308-9a8d-6a327d1ee3e9 | -17.8455 | -39.8705 | 2025-03-25 00:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| ed76508f-ba72-3b6d-a30a-6ced89896fb7 | -17.8658 | -39.8648 | 2025-03-25 00:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 149.9 |
| e4c751a7-2bfb-34d4-9008-23f0dc28870f | 2.9275 | -60.4455 | 2025-03-25 00:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b3a79850-0076-3e61-b7cc-cf2b1ece32aa | 2.9092 | -60.4458 | 2025-03-25 00:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 7f9696c8-099d-31b0-97c3-fbc322092a2e | -17.5613 | -40.6441 | 2025-03-25 01:00:00 | GOES-16 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| ab34413b-bc9a-3e5d-b98c-23dfcc4136ae | -17.8463 | -39.8443 | 2025-03-25 01:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 95.6 |
| 6d2ff2cc-ece2-39b2-b48b-057e3303def4 | -17.8658 | -39.8648 | 2025-03-25 01:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 181.5 |
| 068aa736-ca5b-3145-8386-7aacdc40147a | -17.8666 | -39.8386 | 2025-03-25 01:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 133.3 |
| 86a9610e-4038-3b9b-ae88-24871023e20a | 2.9092 | -60.4458 | 2025-03-25 01:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| fc5620f9-d290-3602-a662-addc409cbd41 | -17.8455 | -39.8705 | 2025-03-25 01:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| c409fe1c-034b-3545-9663-0a8ccd353dee | 2.9275 | -60.4265 | 2025-03-25 01:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c739ff6e-2536-3a4b-85cd-6d0b7ca841ff | -17.8463 | -39.8443 | 2025-03-25 01:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| f2eb9533-6cf5-331d-823d-d8685c22338a | -17.8455 | -39.8705 | 2025-03-25 01:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 77.3 |
| 9e450530-ec62-3046-b457-5e367566f1be | 2.9275 | -60.4455 | 2025-03-25 01:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f76b03c4-2688-34a7-8d12-2bed6b15757a | -17.8666 | -39.8386 | 2025-03-25 01:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 121.1 |
| d921517e-c772-31f7-ab0e-4f6aa76248f1 | 2.9092 | -60.4458 | 2025-03-25 01:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0ac11bc4-9a07-313e-b41f-a4495079f3b5 | -17.5613 | -40.6441 | 2025-03-25 01:10:00 | GOES-16 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| 9f4c1aab-dd65-3272-b0f2-5387e6282ef1 | -17.8658 | -39.8648 | 2025-03-25 01:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 177.9 |
| c5f62e7c-5d28-3fa1-814e-d24710595f50 | -20.805099 | -49.846199 | 2025-03-25 01:16:00 | METOP-C | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c5aa01f0-4d41-3efe-af75-a401d18d8fa4 | -22.915501 | -53.507801 | 2025-03-25 01:16:00 | METOP-C | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0dad00c7-2659-3b41-913e-26b04c9d0644 | -22.9139 | -53.500301 | 2025-03-25 01:16:00 | METOP-C | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9db0fe08-def8-3032-93a3-7c8a81daebe2 | -22.9172 | -53.515301 | 2025-03-25 01:16:00 | METOP-C | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 410d5ca3-a209-39a9-b8f1-77a0276adc14 | -17.8455 | -39.8705 | 2025-03-25 01:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 113.7 |
| 2f4f272b-55b5-32a7-9cd7-4d936fd0689b | -17.8861 | -39.8591 | 2025-03-25 01:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 74.2 |
| 7ce3adcc-581b-3323-a8e5-1d27dee6e9e4 | -17.8463 | -39.8443 | 2025-03-25 01:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 117.7 |
| 422c4f25-63db-3071-a0da-d391d4de8d45 | 2.9275 | -60.4455 | 2025-03-25 01:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d89ff2f1-199a-39a9-8756-76335c4c6c9e | -17.8658 | -39.8648 | 2025-03-25 01:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 226.8 |
| ccc7b258-fe51-3e49-90ad-47f970f880ab | -17.8666 | -39.8386 | 2025-03-25 01:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 131.1 |
| dcaf68c9-ce07-3e48-8a92-6995e91a1ed8 | 2.9092 | -60.4458 | 2025-03-25 01:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |


[Clique aqui para ver as próximas entradas](README2.md)
