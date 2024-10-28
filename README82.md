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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df7af99f-74e9-3adb-8ad1-fa65848a09dd | -3.95524 | -52.20405 | 2024-10-28 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 747d496e-f962-3262-b6fa-f00e8c4b0551 | -3.93496 | -48.33906 | 2024-10-28 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d4c5122d-432c-3ad2-b274-87527c1e8589 | -3.93323 | -48.35102 | 2024-10-28 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 48a0f080-2654-32a3-a8f6-b576c7190572 | -3.9229 | -52.11825 | 2024-10-28 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bea5d935-57f1-3fc8-9ac1-32256ba4f179 | -3.8666 | -50.88724 | 2024-10-28 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 334942fc-44d2-3c89-9ac5-4a08bdebaf87 | -3.85501 | -51.70025 | 2024-10-28 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c03a060a-e290-32f6-a062-41198780429f | -3.83328 | -52.40549 | 2024-10-28 05:44:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 19929501-7cf8-3370-9ce3-f5d6dc17ef01 | -3.81732 | -48.87384 | 2024-10-28 05:44:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cf8f8a5c-d212-3260-8001-1420b370f523 | -3.81546 | -48.87823 | 2024-10-28 05:44:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c5c8e6b9-e680-3551-8cd2-a671349eba09 | -3.80093 | -50.96054 | 2024-10-28 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ebbee226-d6e5-370d-bc6b-b8d76b3d79ac | -3.79333 | -51.37835 | 2024-10-28 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2b5c244d-78bb-321c-a390-364ef33a45e7 | -3.67701 | -50.29718 | 2024-10-28 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2eb8e16f-0fee-3db7-a002-21510dd68d80 | -3.66791 | -50.29586 | 2024-10-28 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2be23a11-4070-3cec-8c6a-4982d700936b | -3.65221 | -50.14915 | 2024-10-28 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 921c1cbb-5115-3d69-acd0-af870c8df52f | -3.65082 | -50.15864 | 2024-10-28 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2f1f655c-c865-363a-aace-736a1832b1f7 | -3.58964 | -53.77576 | 2024-10-28 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| acd7cb5a-bb3c-30cf-a0a2-56b3b39835a7 | -3.58813 | -53.78564 | 2024-10-28 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 12aef066-505d-3394-a3c3-ddb6f6c105aa | -3.5148 | -45.78058 | 2024-10-28 05:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 06661a84-9666-368f-9fc2-a199ec40a299 | -3.51228 | -45.79896 | 2024-10-28 05:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 8e613268-306c-3ae4-9a9c-ed195a0d1a36 | -3.51077 | -45.7915 | 2024-10-28 05:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 7f2acdec-d321-3eaa-84ac-03ae599f1dac | -3.50811 | -45.80986 | 2024-10-28 05:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 850bcfae-3402-395c-9f89-77046d844d61 | -3.49855 | -49.93868 | 2024-10-28 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b8680ea5-d067-3248-89dc-8fed771b4f4e | -3.45854 | -46.3175 | 2024-10-28 05:44:00 | AQUA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9dd3ee62-e23d-3f95-8d30-0e599d7d9d56 | -3.45609 | -46.33408 | 2024-10-28 05:44:00 | AQUA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 20.5 |
| ea134134-666a-37c5-a584-b511dfa609d7 | -3.45202 | -46.32376 | 2024-10-28 05:44:00 | AQUA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 28.0 |
| b1b9af18-27d3-37cb-bee0-c27b92b581b2 | -3.40835 | -54.48425 | 2024-10-28 05:44:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 724638fd-1663-3453-8c9d-b4d606aac92a | -3.40675 | -54.49486 | 2024-10-28 05:44:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b43ccba0-b539-3729-be51-8473e6be6e8e | -3.34153 | -50.75558 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ac62497-efb8-3e82-bc15-cfab51c5c967 | -3.33503 | -51.61105 | 2024-10-28 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 971b89ba-af33-3fed-99d6-a71bd339f356 | -3.33371 | -51.61985 | 2024-10-28 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cf9084d7-c750-39b8-8e0d-af03797fbd17 | -3.32609 | -49.92124 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| db85923e-0ba3-36a2-b9b4-52ff3607621b | -3.25774 | -51.56704 | 2024-10-28 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 254777cf-929b-34f9-a2a4-84bf00d24d0f | -3.2547 | -50.65396 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0dfd88a8-03dc-35ce-8ac6-1715427b741a | -3.21634 | -50.17063 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f3627521-9e86-3dc3-8fe5-88467318bd96 | -3.17418 | -50.39275 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c85293fb-e70e-314f-b22d-532851522879 | -3.1665 | -50.3822 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e386855f-4c2f-33dc-bb1c-28f3194fca91 | -3.16143 | -53.91056 | 2024-10-28 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3f551ad8-b329-3e6b-b2e7-0d5284b1366d | -3.15441 | -53.9141 | 2024-10-28 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c16d31bd-0c7a-3303-a5ae-810f18a9a022 | -3.12535 | -54.27104 | 2024-10-28 05:44:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8cfe707a-e65d-3691-9602-6e3cadac0e98 | -3.11539 | -50.35024 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 37394f7d-be33-3373-b527-e9e84160119e | -3.11414 | -54.28006 | 2024-10-28 05:44:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0921b22a-11ba-3153-b407-5c473e627fb8 | -3.09728 | -49.46782 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d40f733b-07c2-32a7-877c-079153d78d19 | -3.07821 | -54.16277 | 2024-10-28 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c4018e58-2757-302b-966c-6a42cb47c860 | -3.07665 | -54.17303 | 2024-10-28 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8ec33283-5cb5-3126-af7a-51264483242b | -3.05022 | -50.41614 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ae72a1b8-d75a-352e-a79b-23a8f91535ca | -3.04988 | -49.48611 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 3c6eeec8-1604-3fe5-a0ef-6fddd28fb2bc | -3.0484 | -49.49612 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 24ae36e0-d498-3d0d-9ea9-e4f21af48abd | -3.04119 | -50.41483 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 2b9ba412-2a00-3a43-ac9a-7725bca14ac4 | -3.03984 | -50.42399 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| d5764311-fe49-3607-8713-cb9d49888392 | -3.03366 | -50.40708 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| c87836e4-9668-30b5-b3b5-577d5009ce47 | -3.03228 | -50.41625 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 69f3e336-64cd-3cb6-a3b0-3875f0b8a78a | -3.03092 | -50.4254 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2df75dcb-da45-35ed-96d6-8c209b34a445 | -3.02463 | -50.40578 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 2cec4496-abd0-3a88-a19f-3b7cfda13b35 | -3.02325 | -50.41497 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 3b5f9771-1885-3034-bb9b-8bb728b66b64 | -3.0123 | -50.48827 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bab1cb28-772d-3718-acba-9d3a52805015 | -3.00329 | -50.48698 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8802d7da-693b-3e82-b4ff-a0264f92de4e | -2.97765 | -50.47385 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| b6a7dcfa-c8ea-3369-bf72-e415f2566ba4 | -2.97629 | -50.483 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| eda86e8c-fcf8-349f-af65-4edd461b9380 | -2.95736 | -50.42422 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 253c4d63-d2e6-3f96-9aa0-c9ebd9e39da5 | -2.92367 | -51.75409 | 2024-10-28 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 91809795-1963-373f-84c3-4170cdaddcc8 | -2.91483 | -51.7528 | 2024-10-28 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d54a64d-04d4-3cbf-94ab-f1c0d5360241 | -2.9135 | -50.28032 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a077c737-a5d2-3647-b2b6-7a0885c93ff3 | -2.91213 | -50.28956 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1214a16d-4951-3ffa-9c33-7f1e3d3facbf | -2.8853 | -51.82935 | 2024-10-28 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 118f3688-5f45-326e-b139-a39da99992d4 | -2.88239 | -49.50053 | 2024-10-28 05:44:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e9321b26-abe3-3199-9266-7c00ba9a394d | -2.882 | -49.24279 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 97a2b5f2-3e4d-34e6-a90f-fa96d623d7a9 | -2.88049 | -49.25301 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 5ab03442-861f-3927-86f8-74b10b04ee32 | -2.87899 | -49.26323 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9900ce92-a08c-3995-8f90-5acc840f556f | -2.87249 | -49.24142 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e12d549f-6fa0-3632-b3d4-8de38e929156 | -2.87152 | -51.30864 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f5b210fc-3a33-3de9-b916-a63de6b600ff | -2.87099 | -49.25164 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 0e8b7aae-0a96-3058-a5e3-0d246ae20965 | -2.866 | -45.45029 | 2024-10-28 05:44:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 520390ad-92cb-3b30-848d-bdbf6e214c60 | -2.8636 | -53.32753 | 2024-10-28 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 76f1c8ae-9384-36f8-b441-3bd29bdb380f | -2.86299 | -49.24004 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8c3b61bd-c755-36bd-9e7f-db641808ce08 | -2.86218 | -53.33699 | 2024-10-28 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 614e5585-dbe0-3473-a786-cffe7b9e060f | -2.86163 | -49.44663 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| eb053093-7cc7-35c5-9226-93354b1addfe | -2.8615 | -49.25026 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4ac1b550-0e9e-3ff5-8522-bedb325f5b77 | -2.85443 | -53.32612 | 2024-10-28 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 20bdb0e5-ee5c-38c6-952e-b78f726c2106 | -2.853 | -53.33562 | 2024-10-28 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 09705b6a-ed44-3e66-bea5-5513c0e85e61 | -2.852 | -49.24887 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b5aa100a-933d-3e1c-8f26-6849cd340f5f | -2.84526 | -53.32478 | 2024-10-28 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 9ab6b358-3f38-3606-bd9d-65bcb1f18de1 | -2.84398 | -49.23729 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c6cc53ee-a985-3d4e-9ff3-7de0ae96eaf6 | -2.84383 | -53.33428 | 2024-10-28 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e6ae92e4-1390-3e26-a4fa-b394560fc474 | -2.84373 | -51.80531 | 2024-10-28 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 939d0dcb-8a1b-3641-9b6a-8b0da2d1c6b3 | -2.84346 | -52.54511 | 2024-10-28 05:44:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8417ede0-e22f-3f6f-8b3f-8dbdc07208e6 | -2.84249 | -49.24754 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1f479629-844b-31e4-bcc5-57affd6757d7 | -2.83921 | -49.24039 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b82e66f2-6db6-355b-8418-e5960294439f | -2.83489 | -51.80402 | 2024-10-28 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e46a9656-1bcb-38bf-9a67-45563041dfd7 | -2.82971 | -49.23903 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| c56b8284-d5e5-39ae-bd61-cc2b9f0fd023 | -2.82021 | -49.23767 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 58ddd854-a45c-39e8-950f-eb2ea17ca160 | -2.81222 | -49.22607 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| beb7cca4-5e42-358b-8f3a-0af38e52e2e7 | -2.81043 | -51.59628 | 2024-10-28 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 659455b9-5356-3a4b-9f44-e50e51fdfe37 | -2.8067 | -51.8022 | 2024-10-28 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 077f01e3-dc94-3fde-8490-1c12e09f0cc7 | -2.79785 | -51.80092 | 2024-10-28 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 2e88bece-7bf1-373f-a064-1a9461fb7d72 | -2.79654 | -51.8097 | 2024-10-28 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7d0c2c19-bc7a-33b2-9b2f-2a21f27b1c2f | -2.70713 | -49.30938 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| fafd426d-3119-3b1e-8915-46e8aa9605ca | -2.70682 | -49.0468 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5d4d47f6-06cd-3860-b1bb-efc107ed776a | -2.70563 | -49.31949 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| eb36bd90-386d-3995-80d5-7f95493a4657 | -2.64942 | -51.73984 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e1870e5d-c421-398d-82a3-b6b4f064069d | -2.6481 | -51.74863 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |


[Clique aqui para ver as próximas entradas](README83.md)
