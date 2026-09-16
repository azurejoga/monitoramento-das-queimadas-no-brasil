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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e3cf3e5-8c94-314f-b194-a0c37fc9a1fa | -13.2874 | -51.2618 | 2026-09-16 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| aa429999-f9fc-3cd0-bc25-d0b55ada355b | -8.4565 | -46.8739 | 2026-09-16 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 0f8f4906-312b-304e-bd18-d8de179788ae | -9.3379 | -50.1814 | 2026-09-16 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 24717d3e-c11b-3918-b690-26460e10bb68 | -6.75 | -58.8043 | 2026-09-16 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 142.8 |
| d1d6ec98-ae41-3aed-8650-01e830e038ef | 4.1516 | -60.6878 | 2026-09-16 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 23841cf0-9af6-3427-b547-1a716c6d952b | -3.1174 | -57.6779 | 2026-09-16 14:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 1551fc5e-2292-3f22-912b-4358b3fa9e24 | -14.4479 | -40.8379 | 2026-09-16 14:40:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 130.2 |
| f5f3b493-5f25-396a-8b51-dade62c54a26 | -6.174 | -53.524 | 2026-09-16 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 24064af3-1ff1-3e9a-a5a9-a814300a6d1f | -10.8571 | -50.8183 | 2026-09-16 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 64785e91-aaf6-3851-9238-45ad0c30a708 | -6.7684 | -58.8035 | 2026-09-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 213a9fb5-f10f-3501-94aa-3ba68944ac89 | -9.8099 | -45.8759 | 2026-09-16 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 403a8626-36d6-3b75-a87a-aef50ee1c541 | -5.7615 | -57.5807 | 2026-09-16 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ab86004e-fa36-3beb-9c44-ee3441414437 | -2.6783 | -57.6087 | 2026-09-16 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| be777dd9-741b-3a1d-aa6f-5e2df2f22efb | -3.4645 | -58.0001 | 2026-09-16 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 02d2727f-508c-36c2-a369-5c43a3a9dad9 | -12.6636 | -54.6782 | 2026-09-16 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| b3c6f4bd-44ab-324f-a156-d7b8f78c4e0b | -13.395 | -51.7169 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| a7a1487d-213b-3dfb-8e27-e671e614c0fe | -12.7709 | -51.2403 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 37a38f20-3e55-34a8-b6cd-a495bafaa8dd | -1.6206 | -55.5679 | 2026-09-16 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c108dfca-469c-39aa-afb4-7bf02d4bc474 | -11.2578 | -43.4621 | 2026-09-16 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 4b46b8ac-fec2-3a76-b54e-1bb831916fd4 | -6.602 | -58.8684 | 2026-09-16 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 078cd50a-2924-3c74-afdd-69bcd3da584b | -9.7608 | -60.4561 | 2026-09-16 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 43e303bb-e0fd-31e0-b9bb-a742012de48e | -13.3946 | -51.7382 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| efed4098-a113-3d92-b9aa-bee78b4ed34a | -6.6021 | -58.849 | 2026-09-16 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 73c6ebcd-3d1b-3f66-90d3-c2b4b1066db4 | -9.3577 | -50.0943 | 2026-09-16 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2a13d017-0a99-35aa-bd54-b4a81663468d | -9.3765 | -50.0925 | 2026-09-16 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 458a873d-4163-3b6b-80a7-4c4ba71a43e7 | -6.2916 | -55.2895 | 2026-09-16 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| bdd03dcb-971f-3e03-9e34-efef60d015ca | -9.3569 | -50.1583 | 2026-09-16 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| ad598e32-86e1-3a64-b25e-0891fd9a61b6 | -10.331 | -45.2883 | 2026-09-16 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 4a50638f-3e3d-3e2d-a44d-706107740578 | -6.0993 | -59.9076 | 2026-09-16 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8bbd366d-a506-3b63-933c-7af287c79c74 | -8.5415 | -54.7187 | 2026-09-16 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| fc9b6a2e-98c1-3dfb-a23d-d4c438c9634c | -2.7149 | -57.608 | 2026-09-16 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f39ea643-da62-36a4-889e-cf1ae6fe6e85 | -10.6829 | -54.1475 | 2026-09-16 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f2003a6a-9875-31dc-86ec-b9fe43adbabe | 3.8957 | -60.6174 | 2026-09-16 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| b25a060d-f800-33ed-a58b-d8e50818a106 | -3.4462 | -57.9812 | 2026-09-16 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 00613e17-d2a7-3cee-86b3-3fc3cf5bc71f | -15.3804 | -52.9227 | 2026-09-16 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| bf072898-11d8-3fa7-a1dc-233fb55ca619 | -11.5095 | -50.2559 | 2026-09-16 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| f5eb1060-7a69-3bc9-9564-454f523cb544 | -3.7645 | -61.7548 | 2026-09-16 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 8b9d628d-0af1-34c5-b4a8-1f702b1004cf | -9.3892 | -60.3215 | 2026-09-16 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a7d09651-ce67-3acf-892d-084bc8a3a910 | -10.3955 | -58.2962 | 2026-09-16 14:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 4ee7a43e-029b-3c81-bd93-bdd466948af2 | -8.5617 | -44.5112 | 2026-09-16 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 350.6 |
| f0b83022-241b-3bc0-9b9a-6581f7e73579 | -11.1925 | -42.8305 | 2026-09-16 14:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 176.4 |
| 563b22d0-8a73-326a-947a-3c99d495dd30 | -1.6022 | -55.5682 | 2026-09-16 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| d78e8eb4-1e2f-393a-862d-5f78ae5bd75d | -9.376 | -50.1352 | 2026-09-16 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 1353391f-b338-36a4-b05e-24d0f36c464b | -10.3953 | -58.3159 | 2026-09-16 14:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 231.0 |
| 8aa61f37-2b4b-317f-ae74-f853fc42f812 | -6.7869 | -58.8027 | 2026-09-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 7a0a3689-4efa-349b-b883-117a90d797da | -12.1072 | -44.2021 | 2026-09-16 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 16a92c24-48c6-34d4-a5d7-6b40e6b0de9f | -10.5535 | -57.4567 | 2026-09-16 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b082a6a1-4199-374c-a0bf-2aaffcd42073 | -6.7705 | -48.6577 | 2026-09-16 14:40:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 61e677ab-a982-35a5-92c3-c9d8d539888e | -10.4772 | -50.9634 | 2026-09-16 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| d48a7025-d88e-3f0d-ade0-95fcff237fd4 | -3.4461 | -58.0005 | 2026-09-16 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 089c8dcf-cdf4-37be-a96b-85a036feb13b | -11.2115 | -54.1003 | 2026-09-16 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c55401cc-104f-312f-8c25-322365eddbc9 | -6.7498 | -58.8236 | 2026-09-16 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| bcc3079c-9d35-3727-bcd5-db61160a7564 | -13.5127 | -51.5532 | 2026-09-16 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 56581fba-3b39-3935-a1b4-1ac35644e346 | -9.1337 | -65.844 | 2026-09-16 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| f763e98f-dd81-3d2f-b767-b2007726affb | -11.8941 | -47.5876 | 2026-09-16 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 9751bce9-01a8-3c1f-91f2-8bcffbcc0ac7 | -12.7706 | -51.2616 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| a955285b-f665-3850-8a6e-1bd53a2fe103 | -11.417 | -51.416 | 2026-09-16 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 69abb39d-f3b6-3733-8ccb-8f48074b0b21 | -12.126 | -44.2225 | 2026-09-16 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 1f3dccf0-eeb3-3413-8afc-5c2cdece0bcf | -12.6826 | -54.6763 | 2026-09-16 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 45628afd-f086-37b1-84c5-75e814b7b6f9 | -6.2731 | -55.2904 | 2026-09-16 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 52e30f00-2fe8-312e-bbd7-9c6b0f7152d9 | -12.7518 | -51.2426 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 685d14c3-1145-3b69-a521-841345c1d4ab | -9.3954 | -50.0908 | 2026-09-16 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 0de077c6-7655-305e-95ac-813b3ba12f06 | -6.1177 | -59.9069 | 2026-09-16 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| bd3a6935-0910-3567-9834-32674cd35456 | -8.5428 | -44.5132 | 2026-09-16 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 388.8 |
| 5fdc1df5-a197-3bae-99fa-ec2f12ea57d9 | -10.0295 | -52.0991 | 2026-09-16 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 80f6d335-1142-3428-90b3-de72a0cb23ec | -13.3059 | -51.3022 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| dd59b24a-5417-3eba-bb0a-b9f6be92e590 | -9.3567 | -50.1796 | 2026-09-16 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 69e58f4c-ea12-304a-aac8-86f5956d8799 | -15.2583 | -49.1107 | 2026-09-16 14:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| fbfcc809-90a7-3a65-b77b-81b112f73449 | -11.2574 | -43.4858 | 2026-09-16 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 2edc21c0-2b5a-3b37-8c6d-6376996d24d4 | -13.4468 | -54.5968 | 2026-09-16 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b17bb4f9-525b-3194-9071-6e8a43e3deb2 | -11.9033 | -43.8112 | 2026-09-16 14:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 347.1 |
| 2741a95c-9922-31c8-be21-ee9d80335209 | -6.7683 | -58.8228 | 2026-09-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 84689fa1-a2cb-3bc1-b617-03cab2ce92fe | -11.4167 | -51.4371 | 2026-09-16 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 714aa445-b801-3122-804c-046dca58c004 | -10.9107 | -54.0045 | 2026-09-16 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| a1c048a1-3360-3220-858e-a1573bf3aa35 | -11.9715 | -52.4715 | 2026-09-16 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| fec792c4-57a6-389a-9457-255b5e5a8e09 | -5.1255 | -55.955 | 2026-09-16 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d2a67ec4-e1ca-3669-acaf-4794eaf459a3 | -6.858 | -62.8819 | 2026-09-16 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 77fb3572-8e1a-3e99-a390-602380a75fdf | -2.6785 | -57.531 | 2026-09-16 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| bdd48c22-1e5f-3a25-875f-f9f75eeba159 | -13.5719 | -51.4605 | 2026-09-16 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 380918b5-669b-3a37-abbb-1bb74879d99c | -11.2386 | -43.465 | 2026-09-16 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 6615cdef-414a-30de-9b06-6c402081d2c0 | -8.8459 | -45.8713 | 2026-09-16 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 75b445b2-152f-3e79-82d6-64d688476b89 | -9.3707 | -60.3032 | 2026-09-16 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a70261b1-74cf-31bd-bcce-652375713acb | -9.7322 | -64.9067 | 2026-09-16 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 504b350f-d048-38e6-b527-cb32d54e02ea | -9.3758 | -50.1565 | 2026-09-16 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 2f3a09b6-24dc-3702-ad7c-8b2a70144b38 | -1.861 | -54.4315 | 2026-09-16 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 20f80611-7052-34f5-ad03-0ca26d9531d3 | -12.6821 | -54.7174 | 2026-09-16 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| c2c60c6a-3acc-3902-93d4-7f2abd63143c | -3.7129 | -60.6022 | 2026-09-16 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 0d0e0f37-dd30-3365-adc0-465646bd6cb1 | -8.8456 | -45.8939 | 2026-09-16 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 264.3 |
| e6330dc1-ddab-311a-bfa3-171f6f3bce11 | -3.4279 | -57.9816 | 2026-09-16 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f05e0e5e-97c7-3536-b487-d9a47bebc733 | -9.0962 | -65.9384 | 2026-09-16 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d81939e6-cf15-3693-8964-a1b9f523bcdc | -6.7703 | -48.6792 | 2026-09-16 14:40:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1c7aebac-8dc6-3ac1-92c1-82a35c9dc62d | -13.287 | -51.2832 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 151.1 |
| a5e84cd4-a883-3d21-908b-40cd216670b3 | -9.7793 | -60.4744 | 2026-09-16 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 9ac23f56-0dfe-35e6-bef0-01fb0a49afca | -9.3893 | -60.3022 | 2026-09-16 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a27a7f12-3a34-3425-bfb9-8cbfa16508df | 3.7498 | -60.4684 | 2026-09-16 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 3dc71d5e-44f7-35f0-9f0b-4a0335a6982b | -5.1256 | -55.9352 | 2026-09-16 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 97310d83-20ca-3d05-a502-894ab321a692 | -7.3561 | -44.4956 | 2026-09-16 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 346a5bab-37aa-3058-9a37-ffffcff509d0 | -12.7515 | -51.2639 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| a99e21c2-ca8c-3bf3-833b-129d51ad9e56 | -10.6827 | -54.1679 | 2026-09-16 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| f12a7806-aeb5-39ed-9f93-d06cafaa40d6 | -13.2867 | -51.3046 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |


[Clique aqui para ver as próximas entradas](README78.md)
