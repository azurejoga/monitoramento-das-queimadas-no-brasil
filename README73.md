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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f3d8e24-7e83-3999-98b6-fdc96d2f6235 | -11.66558 | -47.6735 | 2024-10-05 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| bf03219c-4b6e-34c8-8a24-f2360bb7c631 | -11.66482 | -47.6779 | 2024-10-05 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 047c9dae-1147-37e1-b613-2b4820bb2477 | -11.53615 | -49.64324 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c9c5b1c-1e27-3a87-a7cd-ecc76ace1cd6 | -11.42224 | -47.19328 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07188c67-bf75-36a8-9e62-7811002fd92c | -11.41506 | -47.192 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23d7466f-b0ba-3595-961f-382ce48936e6 | -11.41435 | -47.19618 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fead771-81ed-32ac-bc2c-0345d5112dba | -11.41411 | -47.19283 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3327df82-e6a8-3cf6-b0b2-cb9e2fd7bd1f | -11.41221 | -47.20874 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63683c80-a469-3745-83d3-cb2e28806c7b | -11.41203 | -47.20543 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe0a0f67-b9ec-3cd3-9fe7-d52d4ce660bb | -11.40861 | -47.20812 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 053bf09e-8717-31c6-a0ac-dc41cdd0b14b | -11.40716 | -47.19492 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b75f15f3-4b09-3389-b06f-43a2253cc9aa | -11.39889 | -47.89663 | 2024-10-05 04:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63b72b3f-ce56-3a08-9f46-e0c7586a1f67 | -11.3981 | -47.90117 | 2024-10-05 04:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e751697-0f83-367f-aa12-f74bd37eb219 | -11.36097 | -47.20083 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7e4a5f50-91ca-3604-84f7-2bc6a00227f1 | -11.36027 | -47.20502 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 14d01ad6-6a64-32b4-b5ee-2433bfcd4661 | -11.35667 | -47.20438 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 738562e5-fccb-34ac-8d53-4ef1d9a1099d | -11.35182 | -46.84504 | 2024-10-05 04:14:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e2add79-470f-36ea-886f-4eeef5289b57 | -11.2608 | -46.99676 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7e1efcd-279d-3957-b2f2-57d6790f51a6 | -11.25367 | -46.99551 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 426e3a56-1e94-3d7b-a8e6-ebd6794404eb | -11.2508 | -46.9908 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61796b16-24f3-3f5a-b4a1-6c6d103e8a94 | -11.24723 | -46.9902 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a854629-6cd6-381d-81dc-05ac5439042e | -11.24653 | -46.9943 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d7fb34e-f0c5-3d9d-ae52-7ccea83c1f22 | -11.24366 | -46.98958 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c08a4643-2f0d-31cd-b63b-5f0acfe16439 | -11.24297 | -46.99368 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 571272ce-9a8e-3042-b324-683ac09d7aae | -11.24227 | -46.9978 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 65ab2c76-32bd-3312-9503-245ced794767 | -11.24078 | -46.98489 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| feed2b25-137a-3b5a-aef8-c5eff594992c | -11.24009 | -46.98896 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b75081f9-dcfa-35b1-bf23-9bc9639f7760 | -11.2394 | -46.99305 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a2d0d852-d6d2-332b-9207-7964386fada0 | -11.23721 | -46.98428 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cd7dd7f5-af70-3bf2-925b-9ae15a521b4b | -11.23715 | -46.6207 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dc6b7ed-730e-3eda-a5f7-d6502b49bda9 | -11.23653 | -46.98835 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1557ed8-f57a-31f6-a147-f939fd1e4678 | -11.23584 | -46.99243 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8d3e8022-615b-383e-a6ee-44d65698f973 | -11.23364 | -46.98368 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a90d3ec3-dc4d-3816-86c3-75f39c4c9fbf | -11.23363 | -46.62012 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f5ac5814-4178-32bf-921e-c3825812c4ad | -11.23296 | -46.98776 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aba125b9-0ba0-375b-b565-31697a1dc9e2 | -11.23163 | -46.98489 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5174a721-5df2-3014-994c-8f58609e1551 | -11.23078 | -46.61558 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b74f8224-d5a4-33a2-9db1-e9b5bba2d619 | -11.23012 | -46.61954 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28bcb2ea-ad92-3c2c-a317-eb03d4caec8b | -11.21938 | -46.59734 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fe94a7a-2b04-3706-9a65-e2d4cd496529 | -11.21872 | -46.60131 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a711ed7-8f27-3cde-9723-48ecc7b6bc48 | -11.18965 | -46.99463 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f24e162-0799-3230-81a6-d64b19906f72 | -11.1756 | -46.92489 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 973ccf4e-3270-3d03-bed1-c1ea75a2480c | -11.17204 | -46.92432 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 48b950cd-bfae-3e00-ac2b-6fd4e25ca167 | -11.17135 | -46.92839 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76ea7cbd-2164-3011-88b2-8937c5ad460f | -11.16113 | -46.51109 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cfc5b78-885c-36e4-ae43-72397f00fe6d | -11.15761 | -46.51067 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdad433a-0bca-38f4-bdde-a049eb8146bf | -11.15059 | -46.50967 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bcdfebd-2ac3-3b87-8bbb-b5b935144a33 | -11.14708 | -46.50911 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7302dc5-1520-3396-ad01-46d2b1c4e8ca | -11.14293 | -46.51249 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be580286-5ca5-3263-986b-7f487cc49e88 | -11.13943 | -46.51188 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63474de7-697a-3f03-abdf-5bcec54e8c0d | -11.13878 | -46.51582 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c039710-87cc-3ff3-bd15-95c0348df127 | -11.13593 | -46.51129 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f976ed76-15aa-3ac8-9ac1-ed80d3ffe104 | -11.13528 | -46.51524 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5cb51182-d5bf-3300-ad1c-c57b385fa0c2 | -11.13243 | -46.51072 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cce7fe16-5e67-3f36-8292-a88be17147b2 | -11.13178 | -46.51466 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9a4107e3-2014-3776-8520-34d6d6f4231d | -11.12063 | -46.51679 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 66073f2e-094e-351d-abdd-f19a1e12f7f8 | -11.11779 | -46.51225 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 02f3abe2-2c57-3a14-a387-1338620a1b12 | -11.11713 | -46.51621 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e6ea71fc-e55f-3a7d-9af5-63d2313d1729 | -11.11647 | -46.52016 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6e6b2d26-95a9-3527-a229-200f6f0937a6 | -2.9014 | -50.7142 | 2024-10-05 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 2687c64a-d7f1-3f50-b8cc-5ba010b4a7d1 | -3.3084 | -50.451 | 2024-10-05 04:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 8ece0116-cefc-3ab7-a203-de6609752e15 | -5.8214 | -44.1426 | 2024-10-05 04:15:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 5083d3c4-fd6a-35ac-bef4-606f3211523e | -5.8216 | -44.1196 | 2024-10-05 04:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6e714262-6cc9-3ef2-9db7-75326261d3bb | -6.9514 | -59.0666 | 2024-10-05 04:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| de3fe883-faa1-391a-ae91-d99b5845af45 | -7.5193 | -63.2558 | 2024-10-05 04:15:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 00c2d7b9-a5e4-32de-8949-c5c1fc43fd45 | -8.7652 | -44.8335 | 2024-10-05 04:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 4b1e80e1-af2d-37f3-9069-1b041e2cd988 | -8.7655 | -44.8106 | 2024-10-05 04:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 426af25e-8a05-35d0-8fd4-75fdd1fda8ef | -8.7841 | -44.8315 | 2024-10-05 04:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 8023094c-fa5b-348d-8e9b-ec35e7ab6a5f | -8.7844 | -44.8085 | 2024-10-05 04:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| cfbd8c29-da87-3f5d-950e-528824322e7d | -8.7772 | -49.955 | 2024-10-05 04:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 913518d9-c7e9-3569-af27-6c81f1ddd63f | -8.9853 | -49.8083 | 2024-10-05 04:15:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 09b0c1ce-c5aa-3af4-8e3b-e5b030a1708c | -10.3131 | -50.5128 | 2024-10-05 04:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 1c04da0c-1a41-3cf9-b39c-45e242a89b1e | -10.3134 | -50.4915 | 2024-10-05 04:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 092c8119-4bd7-387b-8c1d-004b580c4a21 | -10.332 | -50.5109 | 2024-10-05 04:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| c62a592b-0f7a-3b50-b48f-fe4ec43a213e | -11.2365 | -46.9821 | 2024-10-05 04:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| c7579b7c-a1a5-31f5-88bb-2c49faa1ee67 | -11.2361 | -47.0046 | 2024-10-05 04:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 62145522-043b-3dde-bdfa-a43641f30008 | -11.2556 | -46.9797 | 2024-10-05 04:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 95889588-987e-305f-96cd-6a7997c76ffb | -11.2566 | -60.5825 | 2024-10-05 04:16:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 451ac3e7-8f05-3006-a2e7-88ca7077ac27 | -11.6995 | -47.8131 | 2024-10-05 04:16:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 4563399f-27e0-33f9-9da0-af7ce83f346b | -11.896 | -56.9354 | 2024-10-05 04:16:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| bdd8ac2a-0682-33ae-b887-4bb763cd69fe | -11.9149 | -56.9338 | 2024-10-05 04:16:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 3f90e371-4fed-3e5d-96b6-5d2384e88219 | -13.6328 | -51.2604 | 2024-10-05 04:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 852eec60-3f02-34d7-8e5c-7cdaa2f4a5c8 | -16.554 | -57.2237 | 2024-10-05 04:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.2 |
| 8b7c3be1-5e60-3f9a-b189-3379a100fe38 | -16.7647 | -57.4856 | 2024-10-05 04:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.9 |
| 60523245-24fd-3675-bd03-cca6705d74b3 | -16.6594 | -55.5427 | 2024-10-05 04:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| ea024817-dc45-3013-b5e3-49fc5fd0d4f7 | -16.7843 | -57.4834 | 2024-10-05 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| aebc2fc5-e5a9-3fea-8f87-5626d30a4c84 | -17.1375 | -57.4221 | 2024-10-05 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.5 |
| 852cda1d-7be9-36b0-9ee8-512f8465ea8a | -17.1433 | -51.7206 | 2024-10-05 04:16:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 65542961-51a5-3727-9feb-2906590c7e5d | -17.1378 | -57.4016 | 2024-10-05 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.8 |
| b9c13e6e-c1c1-33c2-8e39-91044291f0cd | -17.1182 | -57.4039 | 2024-10-05 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.2 |
| 6a53210e-a41b-305c-9bbc-1d99f64a6517 | -17.1085 | -56.7892 | 2024-10-05 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| eea2ea20-2048-3e74-b7ff-14aaaf46a5ea | -17.1178 | -57.4244 | 2024-10-05 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.3 |
| 21aeb2e9-12c6-3a8b-abd6-07636ee978b4 | -18.5058 | -52.841 | 2024-10-05 04:16:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 635acbd6-f21a-3c34-ac21-67cef1435c23 | -18.6582 | -57.2967 | 2024-10-05 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 1d6fa17a-e4d1-376d-8adc-de1fd92ff9b6 | -18.6586 | -57.2759 | 2024-10-05 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.6 |
| e99b508b-62bb-337c-b90d-222c7fec1286 | -18.6782 | -57.2941 | 2024-10-05 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| afda41aa-a793-34dd-b8fb-5d6f67a94c08 | -18.6785 | -57.2734 | 2024-10-05 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.3 |
| 89587033-e755-3a5a-bcca-8284db90a3ba | -18.6981 | -57.2915 | 2024-10-05 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| d5dcbfb0-38e5-3542-a4fe-dec8cf04c510 | -16.41265 | -57.3591 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a59d49d2-15c6-3727-9729-ae9be86d16cd | -17.11818 | -57.40594 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |


[Clique aqui para ver as próximas entradas](README74.md)
