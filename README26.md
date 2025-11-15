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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73e13d72-e26f-3e27-b39b-d618efc21a5c | -9.93659 | -47.84288 | 2025-11-15 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f18e5374-3c59-331a-9a43-32de2161c21c | -12.15417 | -46.67136 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef52092e-145a-3461-b300-e5da8f30ac64 | -12.60141 | -48.33435 | 2025-11-15 04:06:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26e5b95c-79f0-3daa-93b5-6edbbde94aeb | -9.44965 | -46.97168 | 2025-11-15 04:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d266998-1e85-34a3-a81f-0b4add04d599 | -7.52883 | -47.19543 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ecb2dcc-dd10-375c-8007-c54f92b06aa7 | -8.53722 | -49.5915 | 2025-11-15 04:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c314df15-de6e-3581-b76c-4e7fbbcb6c59 | -12.99592 | -49.79373 | 2025-11-15 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15a6c6e1-2a59-39ff-b228-a692b02366d8 | -11.79051 | -40.19751 | 2025-11-15 04:06:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 28ddea5c-dbca-3a65-95cb-698aee5eebfb | -12.80961 | -46.45452 | 2025-11-15 04:06:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 713cdfab-8ea7-3587-b61f-fa8f34430841 | -8.85188 | -47.33376 | 2025-11-15 04:06:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2700d720-4cc4-3494-b693-b7e7026ae66c | -8.3236 | -45.40467 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3a64c53-8869-3eb2-9fd3-fc1c5017a320 | -11.85116 | -49.20977 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5c622031-72bd-372f-ac2f-f5772d7248bd | -9.85114 | -44.17417 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e9206e2-6c8f-397a-be8b-f89230cf2a3a | -8.73312 | -45.66092 | 2025-11-15 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ba841fe-4092-3ac8-8eaf-1fcf73ca90ed | -10.3562 | -48.92058 | 2025-11-15 04:06:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0814f733-0d2b-334c-b2b8-cee99ff36d6f | -10.05052 | -45.35049 | 2025-11-15 04:06:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fe55cf7-0c7c-3e4d-acc8-3c6d3ee26b53 | -9.19496 | -38.32916 | 2025-11-15 04:06:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 8d8717e8-f446-38e8-a377-6e36a65c6fe5 | -12.93138 | -41.10184 | 2025-11-15 04:06:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 158d52cc-66f4-3df4-960b-b671bf6b8f83 | -11.71913 | -48.87169 | 2025-11-15 04:06:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdc8ff48-3152-39b6-9a09-c1e677efb456 | -8.3763 | -45.05406 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1bd9015-1098-3a85-8778-071683600baa | -12.3893 | -48.10847 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e1a5bb3-3957-3ea1-8e54-412844e3c630 | -8.33038 | -45.41348 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34fe963b-8446-30f9-b5bc-3b5fd0c8e196 | -12.42123 | -47.89742 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| faceb061-6fc0-3749-a24c-68192ab3d079 | -9.12652 | -40.72987 | 2025-11-15 04:06:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 965238e3-de3f-39ae-863c-7db69049d511 | -9.01804 | -44.17762 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5501ff93-e166-38f9-a559-f5ace39fe579 | -11.17473 | -48.14103 | 2025-11-15 04:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac150673-c461-3db3-814d-48533e090551 | -12.66915 | -49.12899 | 2025-11-15 04:06:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e26e2baa-2d47-324f-9dc2-41f8af95937b | -12.92178 | -43.46936 | 2025-11-15 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71834e42-5a24-37a1-a129-53cc44a535b0 | -11.84628 | -49.20882 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| e8891acb-b848-3f1d-8f44-2252d35d2576 | -8.32423 | -45.40109 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35551dbe-e300-3fc3-b747-4445804856d4 | -7.46936 | -45.93279 | 2025-11-15 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdb8b533-c7a7-31a3-b403-832832dda430 | -11.84032 | -49.21342 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 08d9d723-f4d7-32f5-b776-220faaff5234 | -8.99796 | -44.18351 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f9ec17fd-0641-3642-af68-0db35b568751 | -12.43749 | -43.18561 | 2025-11-15 04:06:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2592e34c-0af5-3ba1-95a8-4620c8b678c5 | -12.76179 | -43.6521 | 2025-11-15 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d799f3ef-912a-3ec3-9f8b-9cc5030c1184 | -12.67145 | -46.76139 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfe29408-2b3c-3d81-8025-b7ab028fef04 | -10.23411 | -48.07166 | 2025-11-15 04:06:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d18c1568-09e7-3902-baeb-c5b6675aaf96 | -11.32761 | -48.51829 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b341f893-66f2-3a7b-b0f6-7fd989a489ab | -8.54037 | -49.59 | 2025-11-15 04:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3f2e655-aea7-3684-a8a6-33c9c15894d2 | -7.88776 | -48.39895 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 791fe70b-c525-3021-b509-722817232ca7 | -10.34633 | -48.91882 | 2025-11-15 04:06:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1658c699-0ca2-3870-bcec-089083e7c5f5 | -12.23253 | -49.39259 | 2025-11-15 04:06:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 219154be-1c89-36fa-8498-9b9918b60fdb | -8.24919 | -41.14161 | 2025-11-15 04:06:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 73dd831d-7c7b-36d7-ac2b-dddf68590c8e | -12.66735 | -46.76064 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57fef039-fb1b-3c14-a324-89c91ee9911d | -9.03074 | -46.89018 | 2025-11-15 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 019184b1-3407-37ee-be01-9accc56f6f55 | -10.10096 | -47.52086 | 2025-11-15 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11e1a59c-1a16-31a9-9de3-d6045d7ba05a | -12.66048 | -46.75175 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d89b847e-4db8-377a-b778-1a02e480f8dc | -11.92055 | -46.20213 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4dfe870-39e8-3497-bad2-375f72cdcf4e | -12.14938 | -46.67436 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2654807-002c-3dd6-80d0-a1ef97e20443 | -11.67684 | -44.74134 | 2025-11-15 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 378f8dc8-b54a-3734-a713-2292264c525a | -11.32575 | -48.52863 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a1b878a-5fe8-3105-8b94-c22c14ce5522 | -7.52423 | -47.1946 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fdd0c84-841f-3fab-bdaf-ff5c69dcaad7 | -9.85847 | -44.17547 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cfb0bb0-47bc-3cc8-b1c0-948497217108 | -10.70237 | -44.49082 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76c9bb49-9fc8-38e7-bec8-bc35ef6df692 | -11.17432 | -47.45919 | 2025-11-15 04:06:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 695b94fd-377f-3a70-a07c-e8c53d5f58c0 | -11.20307 | -44.66505 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40817b01-302d-343a-8e6d-97c141c4ef33 | -8.85974 | -40.38301 | 2025-11-15 04:06:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e3b220a7-ebb1-39f8-bf54-6b46ea0e93c4 | -9.66543 | -43.9029 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 177e7e3c-e10c-3dc0-8aac-b719b0ceb554 | -7.21965 | -47.9761 | 2025-11-15 04:06:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c45b044-6832-3d61-803e-2a0a99c258c8 | -9.3524 | -46.59951 | 2025-11-15 04:06:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51b4b16d-9cca-36b8-956c-1a4f64f6aef6 | -11.93058 | -44.62739 | 2025-11-15 04:06:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a307ae29-7ded-3637-b4dd-3f5be73928a2 | -8.46156 | -45.13879 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42c17fd4-7246-3d88-9b62-e9f495a9887a | -12.43924 | -47.88998 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6810eb70-7d67-3cc4-bb39-93a86a4e43e7 | -13.89723 | -42.89558 | 2025-11-15 04:06:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0027d940-e12f-37be-adb6-b73b17d4a40e | -11.11451 | -48.3417 | 2025-11-15 04:06:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4066a14-4220-33ad-b0b5-b8ea97491167 | -10.70971 | -44.51489 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29e85fd9-0572-3147-8917-fe99a1ebbd6b | -7.39598 | -48.65876 | 2025-11-15 04:06:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3714338c-d617-3804-b129-00fcec5b1003 | -7.76462 | -45.16733 | 2025-11-15 04:06:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c1ca7b9-955a-32fd-a41e-e013d2117fc2 | -12.68309 | -46.76738 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7430cea4-b646-32db-b4f0-ed23a64f6ace | -9.85921 | -44.17115 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3e37b36-8ccf-3612-aa47-1cd786bb40be | -11.84139 | -49.20784 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 72c8aab7-65fc-3880-9df7-2ee895500970 | -13.46994 | -46.49295 | 2025-11-15 04:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bd889f1-70fe-376c-b110-e047608d5984 | -12.77446 | -46.95714 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7000ef90-e27f-39c3-91c4-f50b88c370f6 | -12.77516 | -46.95322 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7db33cef-8971-3f33-843c-7237d358a8ad | -10.63004 | -45.00929 | 2025-11-15 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59997de7-92db-3b54-9f63-c858ab04974b | -12.65101 | -43.24855 | 2025-11-15 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae767936-b0b0-3b39-bea9-4d1492c45e4a | -9.66615 | -43.89865 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec706ec2-3c25-344b-aa13-0dce9514977a | -9.71767 | -48.90091 | 2025-11-15 04:06:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b28bb16-08cb-346f-84c4-442d57da6ed7 | -12.67833 | -46.77033 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| afccceae-ee5c-377d-b898-1a31fa3a275e | -11.36716 | -46.17413 | 2025-11-15 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fa84314-5493-3fbf-a517-99e9e885b7c5 | -8.74936 | -48.31569 | 2025-11-15 04:06:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8d1a669-55e3-320f-9acc-42a1b84fe82a | -7.51963 | -47.19378 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f8789dc-b213-3775-81cd-62c552b793d7 | -9.44467 | -46.96971 | 2025-11-15 04:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 177247d0-f4e5-3e83-9f49-56fdc908665f | -11.81316 | -45.28062 | 2025-11-15 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d20a20a1-8c87-3540-a901-fe8f194a5de9 | -10.12282 | -43.8938 | 2025-11-15 04:06:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60be0de6-d5c5-3b6c-9650-dfde7e624d74 | -12.62018 | -42.39204 | 2025-11-15 04:06:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 07728dbf-53e3-38aa-ab50-40824120dc54 | -10.55785 | -44.92896 | 2025-11-15 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d725f115-35b5-35cc-b3a9-e8206e28a26e | -10.71045 | -44.51047 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 508b419f-7885-34e3-bd7e-68418b0de805 | -10.69794 | -44.49451 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45144790-0435-38ff-ad16-0e1abc7d23c9 | -13.48266 | -47.40919 | 2025-11-15 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4729098-63c2-3ced-a531-cba2097b39ac | -13.89327 | -42.89867 | 2025-11-15 04:06:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cb38bd11-f362-3fe9-9b59-b6c3e50abc9b | -9.84895 | -44.16489 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5d2e167-f2dd-3fc2-a724-7ccc139f931a | -8.32825 | -45.40184 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 828006fa-afd5-326a-92da-2c650e20bb29 | -12.47573 | -43.73824 | 2025-11-15 04:06:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4cba1fbf-e0e8-36bf-b94b-398395888842 | -11.79785 | -44.42086 | 2025-11-15 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fcd87fc-8e21-3666-bdc5-246ce0c50f9d | -9.75495 | -43.96894 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a232b95e-c8ac-3319-b787-7ab9b6530479 | -11.70572 | -48.39275 | 2025-11-15 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 10a02d00-3aef-39d1-ad06-622f2597f7ac | -12.90764 | -45.10583 | 2025-11-15 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2438832-6f63-3191-9943-9f6ab2ada770 | -10.69939 | -44.50842 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1788aaff-2ef9-3bc3-bffa-200a4f72df98 | -12.46264 | -43.75214 | 2025-11-15 04:06:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README27.md)
