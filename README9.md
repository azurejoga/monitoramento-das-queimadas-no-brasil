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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0c3b550-b95a-34e3-8496-72df4dc6ebc6 | -9.66326 | -47.55626 | 2025-05-15 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32440767-135b-3481-bbab-b1082d512e4d | -9.66271 | -47.56021 | 2025-05-15 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bbee1173-0d22-3d71-8ae4-eb16ab2b671d | -8.70977 | -50.24986 | 2025-05-15 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2951aa85-8737-31c0-ba26-321dccf01fae | -10.33792 | -47.6782 | 2025-05-15 04:53:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13b2ce0d-1fc2-3037-9ad2-90d6a960213e | -8.33422 | -55.09403 | 2025-05-15 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e07af709-5729-32a9-8549-05b3f62b86bf | -8.80302 | -49.82092 | 2025-05-15 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c9ac8e5-353a-32da-93de-92bf8cba2402 | -8.79998 | -49.81608 | 2025-05-15 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d43ed3d-e924-3aa6-a432-c092785106c8 | -10.334 | -47.97767 | 2025-05-15 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b33fae7-4c0d-32cc-bdb4-c1c642f21318 | -9.659 | -47.5556 | 2025-05-15 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42ead6e1-c6ec-3f23-91e3-0e768233ce12 | -10.46939 | -49.14323 | 2025-05-15 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79b3c8ba-9b66-3fbb-8cdd-3f6b248da87b | -8.72061 | -47.97199 | 2025-05-15 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0112698e-3e63-3506-b592-0932c900e103 | -13.671 | -53.9341 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2b99920-2a18-3ea3-9882-a7020fb79607 | -13.27534 | -45.41876 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 065e5503-3050-3aa5-9c38-0923ebcc1997 | -11.68377 | -44.84842 | 2025-05-15 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab975cc9-9b39-3b1f-86d1-6f04492fe607 | -11.78545 | -47.35558 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43b6c02c-32a8-3ed6-a8a0-f9b547e8014d | -13.0489 | -53.71722 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aab01a0e-9d4e-3591-86a4-c90b85ec57d7 | -11.94899 | -46.59085 | 2025-05-15 04:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74a46010-4610-37d0-a499-6ffea2feba42 | -11.88961 | -56.41569 | 2025-05-15 04:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7df737f8-9c21-3700-88f1-da33748acc4c | -12.16067 | -48.80206 | 2025-05-15 04:53:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1171580-badd-32ed-baa2-5ad27afb66c0 | -11.24467 | -49.48779 | 2025-05-15 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86003765-f781-37de-99af-bab42374c3e6 | -11.68254 | -44.85108 | 2025-05-15 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f6d31c5-e905-3e79-8ab2-ffff7455b8f4 | -12.35692 | -52.47805 | 2025-05-15 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa63b046-5095-3f7f-a773-692a77190f97 | -13.28016 | -45.42257 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85ac744e-fe7d-34eb-8451-328371a3aaff | -11.69617 | -48.81738 | 2025-05-15 04:53:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d715b699-77d3-3bda-a77f-24154fdc14a1 | -11.65077 | -48.10579 | 2025-05-15 04:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 427ad980-9975-3b5a-a5f6-3a14af763a20 | -11.91598 | -54.40889 | 2025-05-15 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 163083cc-1b7a-3f53-9ca5-8911bd04c8eb | -13.27898 | -45.4321 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 448e82ce-e08e-3fe9-9e5e-5c2f13c85b2f | -11.78484 | -47.36001 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ab110381-7746-35e6-9302-f6d4cf6b2253 | -13.26897 | -45.42754 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfb0b6cd-e819-3821-a9dd-3ebb3e720050 | -11.68012 | -44.87099 | 2025-05-15 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b7d5623-e081-3e84-9f5d-66e864a4e34e | -11.68052 | -44.86766 | 2025-05-15 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcb164e7-28bd-3256-82a3-ddf972b4e4d7 | -12.68591 | -58.13289 | 2025-05-15 04:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18ecf0f9-daf6-3a7b-a28c-71c13a330146 | -11.55853 | -47.61058 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee1b448-c4d0-360d-b7d0-0f4e110d4eca | -11.38471 | -57.82315 | 2025-05-15 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06afc937-edde-3838-835d-2dc98299ff85 | -12.19785 | -55.22083 | 2025-05-15 04:53:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c8e8c25-bbda-3b86-943f-18ef1ee6f97a | -13.27495 | -45.42195 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2d62112-dd71-31dd-a96c-d938924c3b41 | -11.94104 | -61.99634 | 2025-05-15 04:53:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0482508-33d2-3c75-9f1e-41d42330264d | -10.66311 | -57.63438 | 2025-05-15 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1ea07c8-b0f3-31ef-8a08-c9b3227c3bea | -11.1662 | -48.67658 | 2025-05-15 04:53:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d6e2cc2-6110-3500-9188-14a5990847aa | -12.87221 | -55.0683 | 2025-05-15 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bbd08bf-1f4b-34d8-9ccf-5aa10b8de354 | -12.10604 | -44.74446 | 2025-05-15 04:53:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c5f5b62-3e04-30d2-93cf-edee9792fadc | -13.28419 | -45.43266 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d965955c-ecf9-353d-bc42-4d4eb855c73d | -10.76678 | -54.7811 | 2025-05-15 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c18c5c83-2fa6-3bcb-a49b-8002fa913bd8 | -11.3877 | -57.82842 | 2025-05-15 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e8b5a13-3265-3100-af0a-bdcf40847b00 | -13.27339 | -45.43458 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d537207-003c-3973-9959-3b42fd59aa6d | -11.77651 | -47.35442 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50f0998d-78b4-3bb5-ab39-e732a9369209 | -11.61121 | -48.01477 | 2025-05-15 04:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0de1254e-c9d3-3352-9a90-bdf633f4d6c4 | -13.04556 | -53.71668 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 71e1bea1-0dc4-36e2-915d-5a91d51f6cc7 | -11.55361 | -47.61411 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0456ccad-62bb-3eb6-8d23-febc935f7da7 | -11.60045 | -58.96444 | 2025-05-15 04:53:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1535984-7d3b-3741-bf67-4aef13f15341 | -13.03889 | -53.71561 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2861b8b1-2f7e-3eb1-a8f4-1dad256f20da | -11.68334 | -44.85171 | 2025-05-15 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e2ab626-0303-34f3-b2cc-ed8da131e82a | -11.51356 | -57.72913 | 2025-05-15 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1011aa0f-e8e0-3115-9813-fbc26c68e136 | -12.6897 | -58.13354 | 2025-05-15 04:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3b57c09-6ea8-3495-bb91-11535068345f | -13.29611 | -47.79324 | 2025-05-15 04:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8eea789-b34d-30a1-8718-a37261d4f5cc | -11.84053 | -46.63735 | 2025-05-15 04:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f608f1a-ff54-35dc-be13-78093c65620a | -11.66227 | -54.94963 | 2025-05-15 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a96e0d4-5bd4-3143-a304-fec03de3d17b | -11.01032 | -50.76251 | 2025-05-15 04:53:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbcc7998-b8de-3953-b565-41192e811d4d | -13.0895 | -54.87183 | 2025-05-15 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 663b46a2-084c-309f-9b85-3f1f2e8d4e9e | -11.56882 | -47.43793 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d9ffe707-60d8-3ef5-b362-f0b74577c255 | -13.27976 | -45.42574 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e29cb81-0f8c-3658-a3f8-551d5c75e16b | -11.42676 | -54.33255 | 2025-05-15 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73cc8551-52dd-36d4-8e91-0880d5f2ecd9 | -13.27378 | -45.43143 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc0a9699-0a9a-3a2b-a0b6-4265917d9401 | -12.86943 | -55.06414 | 2025-05-15 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f05e74f-813c-3fe5-b73f-46e2e533607d | -12.34973 | -49.95673 | 2025-05-15 04:53:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7fa1aee-85bb-392d-a1f0-f5ef2a032dc0 | -11.57984 | -47.61787 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 773cd681-9cbd-3e8e-94dc-7efaf7dcd67e | -11.41953 | -54.335 | 2025-05-15 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 183926ea-9e5f-3c0f-868b-2e6a0a2295ad | -12.49869 | -57.21733 | 2025-05-15 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| daf4298d-826e-3fb3-89dd-0b6bc4d6dcc1 | -12.18144 | -48.68095 | 2025-05-15 04:53:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b24f51d-edd6-38e9-a628-0810c4a9851f | -13.27574 | -45.41554 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c177043-e4f7-3bb9-a760-f3d482f25909 | -13.59649 | -47.38016 | 2025-05-15 04:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90dddb64-68ae-34bb-b432-14cef60a10ad | -11.7833 | -47.35756 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| abe1a8d3-85c4-3e86-9975-6e403497cf20 | -11.64968 | -48.11368 | 2025-05-15 04:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 399acbba-beeb-3807-80e6-542285f04425 | -9.79578 | -56.1325 | 2025-05-15 04:53:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78a71cfe-15fe-32e6-85d3-96c8441a06ce | -10.53913 | -56.39042 | 2025-05-15 04:53:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fdc277a-9ec9-3463-8d30-efd68b9efbc5 | -13.21964 | -49.86192 | 2025-05-15 04:53:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ba107d2-269f-3fcd-8347-639ae0976db9 | -11.78777 | -47.35814 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 13276368-a0b2-3144-ae24-1c0b5ad891b5 | -13.28459 | -45.42945 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85994394-b9cc-3604-9e22-81fe50b10350 | -13.62272 | -54.87908 | 2025-05-15 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23a33ca9-fbe3-3190-b418-6a97b11c93cb | -11.96675 | -48.11939 | 2025-05-15 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5547b7ec-0977-3678-8f78-4979057a0d77 | -13.67156 | -53.93053 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd5342d1-76a2-313f-9b73-6cf577c50aef | -10.69664 | -59.11448 | 2025-05-15 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f86fa514-c184-3062-9502-ec0eeeef719a | -12.60719 | -56.02843 | 2025-05-15 04:53:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f15fc2ff-cef0-39bd-9694-f0b4e8dfdc66 | -11.65832 | -54.95269 | 2025-05-15 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8614dfae-e1c1-3ca1-b77a-9567017d4a7e | -11.78097 | -47.35501 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8769e218-d428-39bc-8872-3e8453851510 | -11.38391 | -57.82775 | 2025-05-15 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fee57915-7bfd-36a9-b260-c48df08de248 | -11.6075 | -48.0101 | 2025-05-15 04:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e44d009-11a9-3eb2-bab2-4c7588687fe1 | -13.27937 | -45.42891 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5277a14-7d4e-3205-b2eb-3cf5cce7a779 | -13.28339 | -45.43909 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a6875a7-9a34-3e1c-b77c-a5fbac91c518 | -11.16215 | -48.67599 | 2025-05-15 04:53:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 473317d6-c02d-309b-b6e2-85a58a330b90 | -11.5721 | -47.44058 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2c87a98f-e8b8-310c-b610-1759f0910370 | -11.42009 | -54.33146 | 2025-05-15 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f82b3bdd-1428-356d-9f16-546fd4e6f0ac | -11.7893 | -47.3606 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 67ef10f0-38cc-3a12-a8bb-e656898c8e0d | -11.94206 | -61.99072 | 2025-05-15 04:53:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d9b1a3f-d11d-33a0-8cd0-ae5e45cec3d4 | -13.2955 | -47.79783 | 2025-05-15 04:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e65288e7-96fc-3627-a077-9210d702595a | -11.97046 | -48.12394 | 2025-05-15 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce9e64c1-79d0-310b-a22a-5f4bac28c5b6 | -11.04556 | -56.19356 | 2025-05-15 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 408373f3-2685-3df8-8d45-c243c5ea6149 | -11.91264 | -54.40834 | 2025-05-15 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc3766c2-54ca-3410-9329-5e60e3e14aca | -11.55416 | -47.60994 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9998c28-3202-36a2-8d49-30ded9570679 | -13.2874 | -45.44929 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README10.md)
