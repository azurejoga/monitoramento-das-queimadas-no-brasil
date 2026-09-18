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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5984af56-7cd1-3857-a590-1afa1f3d0cbf | -12.42922 | -50.67887 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59d176fd-3792-3c15-8fc6-c06a2ef154b8 | -9.39597 | -46.86674 | 2026-09-18 05:18:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| de9b4bc6-d115-32d8-9bf6-c3adfdbb9d15 | -9.856 | -48.37687 | 2026-09-18 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 067c15ad-e364-37f5-9740-dd811d214981 | -12.16731 | -46.99261 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 45b8e84a-55ad-3c61-89c8-04e75586fe3b | -10.53817 | -44.85191 | 2026-09-18 05:18:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 753c353f-aac2-3e25-943f-4b4dd8f39e98 | -10.50773 | -46.27908 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfd5c47a-be39-3fa6-994f-25eca70a1181 | -13.43 | -51.90124 | 2026-09-18 05:18:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35d3b736-ba36-3cec-8f71-6b7ac4fb4078 | -9.9299 | -46.5278 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65a78775-5644-3fa1-8fa7-827e514b1185 | -10.66848 | -50.26863 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f28952cc-0417-3af1-a16b-950736c8dc6e | -14.17118 | -47.85853 | 2026-09-18 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ab9c634-de33-3c30-b865-8c69cde0499b | -8.8624 | -62.39808 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3258d710-a55a-3b1b-8fe2-e1eddbfe23a8 | -9.90875 | -46.56911 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92609f48-5e22-369b-98a8-06070a7ff01e | -8.90336 | -62.40287 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2135b07-1345-3ad8-ba72-e43c7c5ce4f0 | -9.191 | -46.76256 | 2026-09-18 05:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6e58ad1-e6ae-3eac-9c7b-f10610db3a1e | -10.65073 | -50.24843 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| fddd9e47-883e-33e2-b729-c82e79d061db | -9.9473 | -45.33663 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10d3e7a3-81a7-3d39-a992-a7a443361207 | -9.15542 | -49.99091 | 2026-09-18 05:18:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b8123d5-4c5c-3c3a-9efd-13e429c7115a | -10.65708 | -50.46685 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de74c884-9be6-3fd2-b2c0-42e8c84bffce | -10.49139 | -46.3056 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1783d6e9-0afa-3cb1-9ca6-0bad52600b4d | -12.17108 | -46.98939 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7d2f539-9dc2-3f43-aa85-82799091d45a | -9.74415 | -46.10238 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 763d6085-09b7-3c52-8bb8-bb3211365998 | -11.12592 | -47.71165 | 2026-09-18 05:18:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd093021-5871-325e-80df-a88f6289003e | -9.91411 | -46.5518 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e294b94-8d4f-3147-9782-bf1be5a82651 | -9.76583 | -46.0852 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8858817e-4649-34fb-b8b2-224a8d00bd3c | -11.31425 | -46.7618 | 2026-09-18 05:18:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27d51671-9932-3550-b14e-ebdd494e5d1c | -8.48601 | -57.62291 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee701c7d-d538-3b94-b580-82c51b60ac6e | -8.50095 | -57.63598 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f45582a-b31b-3290-98ce-158f500191d0 | -9.0918 | -45.71969 | 2026-09-18 05:18:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 518aea28-e003-3201-b5cc-10bf5ec65419 | -10.91399 | -53.98714 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 086a00aa-8736-384b-afec-043b2428027d | -7.87886 | -54.72399 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9534f4f5-32ac-3481-82e4-5fb875ea5fe9 | -8.48878 | -57.62693 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e35cf66-1f4f-3525-aea2-3f8393dc9c0d | -12.37952 | -48.47291 | 2026-09-18 05:18:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b99761db-56c5-311d-89f1-4bedc5f998fc | -8.16749 | -54.81928 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f35ac821-9455-33d2-a716-f189460e1519 | -12.39588 | -48.48323 | 2026-09-18 05:18:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7af8b21a-cb54-360b-8788-33ec5ee4dfb9 | -12.26678 | -50.75516 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2987c1b5-9251-3e05-9475-828183fbd0ad | -10.13375 | -45.57607 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d9e00a4-e24b-3c39-ad66-07948ac52e75 | -9.48697 | -54.4783 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb98e39e-a59b-34b4-be3a-ec8743517a09 | -9.94657 | -45.34279 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49894db0-8d4e-33ec-99af-e5a59f60c06b | -9.72246 | -47.14188 | 2026-09-18 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18f55ca8-a636-3885-b25e-5e033b68f057 | -9.70478 | -54.82899 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6b86dba6-93d1-31ef-a7c9-a0d72355c99b | -12.26304 | -47.13522 | 2026-09-18 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0846a85a-bd08-3e15-8f42-be143c393c6e | -8.4827 | -57.62239 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58368644-303f-339f-bb96-2044a26c3911 | -9.91236 | -46.54107 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 774847db-04fd-39ac-8c12-a5a8260879ad | -12.39128 | -50.69743 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96d6f94b-ad9d-3b68-9731-d24e9cf3d8e2 | -10.11729 | -45.65348 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c1b5a15-53dc-3687-84a7-13cac6fca7d1 | -9.75732 | -46.10011 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c1f21473-68d9-3911-9c87-1f1edbdb1a63 | -8.16388 | -54.81874 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f718a095-a1fb-3693-a8e5-01699a4b2767 | -8.89872 | -62.40701 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1bffabb2-349f-3fe2-ab43-cd5b8a4e2b28 | -12.78696 | -47.56309 | 2026-09-18 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81b5750c-4d9b-36c1-a5b7-783ede78ad87 | -11.87621 | -47.57442 | 2026-09-18 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd250240-6b21-39cf-bf04-cbb32705b835 | -10.66324 | -50.46952 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f082b9fc-7dad-378d-8a91-f8ebe0fb1cc5 | -7.75507 | -54.75327 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54151883-3ad6-315d-8f13-1baac0fef108 | -9.93053 | -46.5227 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b96f74c4-8634-3e88-80d3-a920593e653e | -9.91472 | -46.54674 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76ed59e9-6edc-3cc6-955b-5615d2d107c4 | -12.25976 | -47.13336 | 2026-09-18 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d9669bc-57e5-37d3-91a3-8ea7e652fb51 | -10.09375 | -48.18727 | 2026-09-18 05:18:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c574e1c-0ef8-3af1-8aec-97698f18a702 | -8.49486 | -57.63145 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84c59078-0f0c-3dae-991e-33340aa85998 | -10.66697 | -50.46819 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 758a31cd-e3b2-378f-bf24-b90c99c764af | -8.49209 | -57.62745 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd7a121f-9cb8-36c3-984e-a6df324c9220 | -8.48869 | -46.88308 | 2026-09-18 05:18:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7cc8b5f7-eb43-3085-ad6d-c09005044db3 | -14.17107 | -47.86025 | 2026-09-18 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 741168f4-859e-39fc-8a3e-b43d84ca4558 | -9.95335 | -45.68593 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8c6cee99-2d4e-3d63-b30b-2786f55279bd | -10.65961 | -50.25855 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 042ad2ac-66d9-3741-bd36-6be6961b3f1d | -9.94067 | -46.54498 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85f69164-a8df-3baf-8172-ada134a2b21d | -12.15872 | -48.95698 | 2026-09-18 05:18:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 433cf93c-3fd8-3c6b-90cb-fe422cce4a9b | -10.67272 | -50.27514 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| af9d773f-5901-3f38-a457-3a4d2efeca0f | -10.61271 | -46.56932 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5574db5d-07d9-3136-9afb-adcd90a337f7 | -9.59504 | -45.8652 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eceaba6b-1270-3d0d-bccf-3b08148a69a3 | -10.65111 | -50.24551 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 0dee67c0-54aa-338e-9322-c2c6c969b696 | -12.57489 | -47.09449 | 2026-09-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 941a8f6a-749e-3d07-9cd0-d715fb71680f | -9.18656 | -45.69993 | 2026-09-18 05:18:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c343b80d-e609-3ec4-88bb-350279b00877 | -11.80464 | -58.17699 | 2026-09-18 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4d34731-e8c1-36aa-a3b6-93aa55c23aa3 | -12.55577 | -50.72639 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd00fdf6-3ffa-3937-ae8a-a789aec68cc5 | -10.01885 | -51.10604 | 2026-09-18 05:18:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c61238b5-80aa-3d1f-a57c-86e6b02613e9 | -11.5186 | -46.87405 | 2026-09-18 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ec68336-fe28-31c7-9515-845b311df1d7 | -12.29804 | -50.74771 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 620a3f14-6aef-3b08-9595-54d81558ab8e | -10.81093 | -50.19706 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f03f8e82-3ef8-3cb7-b8d0-1609d264aa27 | -14.17163 | -47.85429 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81855244-f2f9-3284-8b93-f894ca47faa5 | -11.19674 | -55.0393 | 2026-09-18 05:18:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6099d2e-4e8e-374b-ad1c-7a949ba40608 | -12.56898 | -47.0902 | 2026-09-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8322e170-5917-324b-ae29-8204a16c0991 | -12.55648 | -50.72058 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3cf26f3-264d-310f-b55a-9c4983bc4aeb | -12.39151 | -48.47089 | 2026-09-18 05:18:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8084483-d5c7-3b67-b208-3df78014b327 | -13.74399 | -48.80839 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5dc7f70c-f556-3e66-9d37-4dcb0cc2fa00 | -13.25057 | -46.90841 | 2026-09-18 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d0ca1bbc-8398-3b23-b4b9-97c3cc01c83f | -14.32678 | -46.69894 | 2026-09-18 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d308568-8c08-3428-ba66-5aa364f41442 | -11.87637 | -47.58222 | 2026-09-18 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7106539b-32ef-3058-b036-e59c7766f813 | -10.66347 | -50.26796 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 99389dd9-940f-30e3-b7af-3e4a1d8c7565 | -14.22422 | -48.51252 | 2026-09-18 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68a5fc99-adb1-3bba-b615-624900445b20 | -12.26545 | -47.13906 | 2026-09-18 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77c5c256-dad3-3de2-b00a-d1f27fcd0cd6 | -10.10474 | -45.64496 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8322142d-1e72-30b8-8ece-0f832681e0c7 | -10.67389 | -50.26639 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 439f2447-e2ad-30c9-9629-25c273423582 | -12.47846 | -50.69127 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfd01e26-50fa-3bc4-a092-69a419f91e1b | -13.6179 | -48.30624 | 2026-09-18 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95f77c7a-67b7-3b67-94b3-9a83e42dd361 | -9.72273 | -54.80944 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| baa25f7a-79d6-30fd-abb6-29dd2a0c0d88 | -9.38876 | -55.96995 | 2026-09-18 05:18:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae6877c7-713b-3e8f-835c-71f2651d5af3 | -11.01807 | -54.15082 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba920f70-57aa-3caf-84bb-895855e5d0d3 | -13.74537 | -48.7905 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba848d38-44de-3017-9377-1415a82b5b4a | -10.80411 | -46.66468 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29e781fe-4975-3d8e-9b0c-274ac607a2bd | -12.17377 | -46.99229 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8c27742d-80c0-3b80-aa6d-19de981483d2 | -11.32702 | -46.76284 | 2026-09-18 05:18:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README85.md)
