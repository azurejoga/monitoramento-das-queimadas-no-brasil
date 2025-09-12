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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3f21b45-35a7-3ba9-9970-b215fd906151 | -10.56315 | -51.48959 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cfbe14e0-04d7-3390-b1ef-2e7f223d78aa | -10.70311 | -48.62975 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 97dae0dd-fbf4-32c8-a9e4-3c947af6c392 | -11.94139 | -44.29842 | 2025-09-12 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b4ff3ee-402d-3b94-841a-f82cf08d3e52 | -6.48855 | -43.87721 | 2025-09-12 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8ed15b5d-2eee-3680-8e23-53596d5eea36 | -9.72133 | -51.00418 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 844dc7f2-236c-3f57-9941-b707e7c89506 | -9.21692 | -59.38516 | 2025-09-12 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a6f43be-a196-33c1-8e7e-e50b32a4f7c9 | -9.6108 | -48.02868 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c117d5ff-06c3-3b9f-a736-375ac6298239 | -6.18753 | -42.73991 | 2025-09-12 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6ced250d-bb00-39a4-80d8-2b8507c49b99 | -6.82063 | -45.65455 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12548a0f-86fe-3c26-bf36-54cb0f6f61c4 | -9.85706 | -43.12663 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd85393c-7294-3802-898e-af6502c29204 | -10.5512 | -51.53672 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 092df81b-99da-3300-aa9a-62a378ae6b7e | -11.68425 | -46.52847 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a57c37ee-9135-33a2-913f-4373904a2e9e | -10.41164 | -48.58661 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 896addd2-90dc-36b7-a279-2989a1c5b811 | -8.07988 | -50.18161 | 2025-09-12 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef38e1e0-66de-3c73-837c-17f6b5e326c3 | -12.1037 | -44.88144 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b533177-2337-32b0-8d4f-4d74eb72c14f | -12.4132 | -44.71819 | 2025-09-12 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0038711e-0691-3c9c-836d-321c8450e435 | -9.08804 | -46.95825 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ab8475f-1eea-3e88-b429-995e949443c3 | -11.67207 | -46.56303 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b70d513f-562f-36ea-9871-8a0b58afc12b | -8.54396 | -45.59309 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6ebd60a-cd93-3019-af51-add4dd4cebcd | -10.85689 | -44.78891 | 2025-09-12 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d1799b9-b407-393e-ae91-b79aaef94bce | -10.84981 | -48.16066 | 2025-09-12 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cc53c18d-a2b6-34d5-95bf-d242785decd9 | -9.72917 | -48.34498 | 2025-09-12 04:25:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 544428c0-1185-3280-a02a-3bc2a2c4215a | -12.10695 | -37.97506 | 2025-09-12 04:25:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 03cb8508-0892-37c1-b109-5ef5d92e0964 | -9.08472 | -46.95772 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb0998ac-77b1-3a9a-9045-db36fd9b5345 | -11.08666 | -48.44532 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d60fe33c-edbf-3621-bd21-0dfefecfc58d | -10.08778 | -50.39141 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9d44e29-ba75-3f05-8f6b-21c51a21f7d1 | -8.73977 | -47.11948 | 2025-09-12 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15437df1-7d1a-3157-81cc-25308b061402 | -9.70625 | -48.30415 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8526a9a5-d121-3ad2-b656-252e91c17132 | -11.1186 | -51.98598 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5d4c00f-b02b-3283-bdbd-9f02a16a210f | -9.04563 | -47.05487 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6006eda2-03f8-37ed-8c82-7f5d08492f5e | -6.44461 | -44.05948 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e08f467-405f-3adc-b07c-6e8b4e1a48f0 | -9.5194 | -54.63182 | 2025-09-12 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b523c326-f69c-37d7-b1c7-a288e89e1fb1 | -8.96054 | -46.08236 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bed6eeb-aba2-3458-85d2-bd9897f7b37f | -10.65737 | -48.6559 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 53214160-4d36-34c8-97f9-302441a7182e | -11.68154 | -46.59016 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d41c572d-3671-369f-ab91-de06a261b93f | -11.47397 | -49.28289 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6d2863f-0c7e-3009-9289-0ecc4ae14724 | -7.29756 | -44.35928 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bba7a49-bce1-3d1f-b393-210a640a6531 | -10.68275 | -48.64871 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2979f4fd-35eb-37d4-8fe2-7abc3da34ff7 | -6.30358 | -42.22832 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| aa75c78e-a22e-39d1-a750-5a68af6084d0 | -9.85637 | -43.13122 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1258c7a0-ff53-3144-98d7-1c33557248e6 | -8.04987 | -52.32463 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1eb99fbc-d4a2-34b2-bdeb-ae6208263c59 | -7.46156 | -44.41087 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f692680-e313-3b76-9f84-853c1515dfc5 | -6.18188 | -42.7524 | 2025-09-12 04:25:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 874430d3-812f-39d5-9eaa-5c1701afd0a2 | -5.94438 | -42.79062 | 2025-09-12 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0c5f77ba-ad72-320d-82cb-5226fa94754f | -9.7432 | -48.34355 | 2025-09-12 04:25:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d37c946-1637-3ad7-ab30-e768dd699055 | -9.34983 | -46.58911 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a597f22c-869e-34b0-b766-902b0b7a8ac2 | -6.81745 | -51.88846 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cae710e-4744-3707-b84c-f15c3bdf2acd | -11.52826 | -50.59365 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b755138-76bf-34a6-b209-e0121270274d | -11.48408 | -43.62552 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ee3579a-90a9-3306-8139-aa624eccde33 | -8.36586 | -44.83681 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b358d8dc-3cb6-30ba-b697-fb358c0d2de3 | -4.48144 | -48.11165 | 2025-09-12 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5876beda-8e7f-3d1e-b5ab-8ad1ec473600 | -7.49349 | -54.94917 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af071de1-cb3e-3bde-9f4f-c64f10eea2d3 | -11.43615 | -49.29962 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaf33cce-408a-34a2-b8dd-6c9733977ab8 | -11.13939 | -45.23847 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 80d762b4-97bd-3401-aa92-073a4196dea0 | -9.80209 | -48.8866 | 2025-09-12 04:25:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2789e909-5db1-37f6-b2ec-ead0611c7161 | -10.79212 | -47.26434 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ba98e73-bd99-342a-9a62-a74846681f56 | -6.34474 | -43.03459 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14d391ba-7084-3577-9fa8-1889a2521de8 | -9.88182 | -46.46584 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51168cdc-8c9e-3e3a-8e2a-1d88e1e27064 | -11.52755 | -50.59786 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee4486bc-8c95-3b62-9323-bae8a05defc6 | -11.97848 | -46.64449 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 33192e55-df29-3867-bf02-e192fc2dee42 | -9.73 | -48.09124 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 253812c9-6a77-3363-9c75-73692fc584a3 | -8.49556 | -47.30945 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3403ab2e-450f-3c79-9d99-db96440e4924 | -10.67542 | -48.65128 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 122b532d-8adf-3763-a7d3-b8fd4c848541 | -7.49138 | -54.9537 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c4a9f2f-83cd-30dd-a5a2-d72670d8d6c4 | -10.08296 | -48.17419 | 2025-09-12 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70c4817f-9133-304e-9b9c-3286759f72f1 | -10.33844 | -48.8033 | 2025-09-12 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d4da987-3266-3f9f-ad60-d30bd7cec875 | -9.97475 | -51.70738 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca0f1e18-d90c-3aa4-98a2-43c5ce47dda8 | -9.03956 | -47.05032 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1c0ea4b7-71a5-3b7b-9006-7fd590e707f2 | -11.97628 | -46.65876 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a600f1ab-9a43-3719-9480-25fc4bc429b6 | -11.44363 | -48.56645 | 2025-09-12 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2862de2a-1214-3ce8-9d74-b8d1b627196f | -8.42174 | -47.26187 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c103c911-d56c-3465-9a12-861e7817bffc | -8.50673 | -45.65669 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50b1a0db-cc03-3d5e-8632-1acf18023feb | -10.37139 | -48.30232 | 2025-09-12 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5871716a-1924-3f42-942b-625dd1394233 | -11.17705 | -48.43059 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53937ab3-8458-3210-ad95-f8bb230a0bd4 | -10.36172 | -46.38982 | 2025-09-12 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37e769b8-d434-3320-a8f4-abfc766527a8 | -5.701 | -45.10662 | 2025-09-12 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a44025b-61a9-33ae-984d-4e00e3718cd4 | -8.49061 | -47.27644 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0c43151-57f5-3a67-b10c-dc8d6bccf312 | -11.14565 | -45.31311 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16f8c508-1888-3528-9c4c-253de11af327 | -10.11851 | -47.91079 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebacc75d-6e01-3af9-9d4c-df7c3dd2979e | -9.79545 | -59.10228 | 2025-09-12 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6a0e422-b1d6-3914-a6b9-d368d3354dc9 | -5.40121 | -45.93564 | 2025-09-12 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0c7c474-aed3-3bcf-83d2-30d3ff5b49e2 | -6.30528 | -42.21634 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7f130129-b000-303c-9a2e-7ba8a549e281 | -10.41224 | -48.58293 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d906099f-d1d9-3fd2-be85-1206ddae8e8b | -7.48737 | -54.95445 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f24e4153-b030-3990-a193-eb2744fcceac | -12.14252 | -44.86287 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfb639c8-2695-3255-8384-cc7945a2a4bd | -5.85143 | -47.35645 | 2025-09-12 04:25:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b6eafda-3d7d-39d1-a516-88d26598cfb9 | -11.46737 | -43.60925 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48b1ea3f-4eff-376c-84b4-a3d4ee1c814b | -11.68871 | -46.54381 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69690f27-a36c-3d8a-bb5c-d67c20fcef07 | -6.17875 | -42.62322 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 18e8fe19-1527-3a26-a34a-4276868e61f2 | -12.10075 | -44.87692 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c056722d-29c6-35e6-9ef6-0dbf07f05dd1 | -11.68986 | -46.58053 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f667a5fe-9a63-331d-8e1a-f1ad22611289 | -9.03403 | -47.10659 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f9121d94-3121-33b6-958e-32ffcdaa8e60 | -12.50761 | -44.68939 | 2025-09-12 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac3276f6-a7b7-3b68-ae51-086615ca7b0e | -7.28964 | -44.48109 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 333cdacd-b7d0-37b9-bb60-af175970217e | -9.72886 | -51.00547 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68d8de70-fa58-3da2-bc9b-58c553c6fbe9 | -7.4215 | -50.64676 | 2025-09-12 04:25:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f45f043-05fd-31df-8633-75e964b4e978 | -10.41797 | -50.61426 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 344309d3-5aa5-3f66-9ed1-1b277d4d38d6 | -9.04507 | -47.05836 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d459f28-75c3-37ef-b8c7-959c9f546ff9 | -11.67988 | -46.60085 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2bcf5f03-d415-3483-a449-9da091e25a94 | -9.06548 | -47.03661 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |


[Clique aqui para ver as próximas entradas](README60.md)
