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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fc7b385-238b-310c-afef-31d524ad158b | -7.11264 | -47.8713 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e4ba5cc-e790-34a7-aa98-02cda03a1d3e | -7.11189 | -47.87639 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4dcd17f3-dd2f-3c54-a1e6-207c5ff35e97 | -7.11115 | -47.88144 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2f442c3-0c65-385f-b6a8-e198c7c878ef | -7.11042 | -47.88646 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20675867-2e14-3f74-b122-fd2d553e98d0 | -7.1094 | -47.86552 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68c1220d-c971-32e7-9d06-3af78ac8882d | -7.10866 | -47.87058 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0f2bf5d-f347-34d7-b870-4fd830932e1c | -7.10719 | -47.88064 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c2151ed-170f-32cf-afbd-ff909c4c401c | -7.10645 | -47.88573 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b25c12b3-87e9-3f34-99fd-1516f1b607f6 | -7.10145 | -47.86398 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4cfc97cd-902e-36f5-bd22-159bd8d1c4de | -7.0722 | -48.03706 | 2024-10-03 04:49:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04e4fc66-471c-387f-830a-83dbf85c85d9 | -7.06899 | -48.03137 | 2024-10-03 04:49:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de999583-71ab-310c-a7ac-864f87994c58 | -7.06825 | -48.03647 | 2024-10-03 04:49:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17a78a0f-1e28-31fb-b317-1c451276174c | -7.06503 | -48.03081 | 2024-10-03 04:49:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b8ff225-05d4-3961-b2b2-a13a23a50657 | -6.94741 | -47.67089 | 2024-10-03 04:49:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69a71e6e-dba4-3c12-a6da-42fa4b955ff9 | -6.9469 | -47.67439 | 2024-10-03 04:49:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4066245-2e5f-35e9-be63-9daff0869f4d | -6.60923 | -47.90823 | 2024-10-03 04:49:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7842388c-0607-355f-b065-5f57cb6c7987 | -1.91217 | -47.88565 | 2024-10-03 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81605c17-f03d-393f-8153-467754289439 | -1.90845 | -47.88506 | 2024-10-03 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 76ec8f4f-662c-36eb-8525-55b324fa847f | -1.49173 | -47.33561 | 2024-10-03 04:49:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a2d0bc4-9444-36cb-8c38-38a3b25ac393 | -1.44185 | -47.58164 | 2024-10-03 04:49:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4ae2235-d3d0-3f28-8168-f303dbeba62e | -3.49081 | -48.90924 | 2024-10-03 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbb1503c-443d-3d78-b018-88cb0fbdcf6d | -3.31629 | -49.04265 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 622e664d-d643-38e2-a7a0-588d3bf40204 | -3.22624 | -48.92616 | 2024-10-03 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0602d408-f133-3006-976d-0726099543c7 | -3.22266 | -48.92562 | 2024-10-03 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aa8b18e0-1aae-3b98-9002-d19467386c2e | -3.13579 | -48.99073 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 242ef9c7-8ac0-3bd1-813b-00af99e201f5 | -2.90347 | -48.9178 | 2024-10-03 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| faec5b20-2563-39a7-8cc1-084e65de2ee9 | -2.76511 | -48.9463 | 2024-10-03 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c293cef-995e-318a-86c3-ebd39f3553ae | -3.46926 | -47.65767 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05f0d944-a305-3f73-ade0-b33cf9e773cd | -3.46853 | -47.66248 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e87eadbe-ab70-3786-a02c-0a15fecb4bb6 | -3.46541 | -47.65706 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7a75bea-6d23-3204-a8d2-ea3223a3dda7 | -3.46468 | -47.66193 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c7cee072-5da1-38a6-9491-29fc449019e5 | -3.46395 | -47.66671 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1e3191f1-d024-3dbc-9cf1-3271929df47c | -3.08886 | -47.77443 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6506f743-0528-374d-ac8f-d6b164d70f5c | -3.08437 | -47.77845 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbef1778-b7ea-3739-b988-d018a300f7d6 | -2.9935 | -48.55606 | 2024-10-03 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ce44431-007b-3cc6-aa1d-99c8d483e7dc | -2.99286 | -48.56025 | 2024-10-03 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cb3fcb5-e055-3e5a-82a5-e7765e2e4222 | -2.9492 | -48.60233 | 2024-10-03 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c81feb1-4128-32db-a1be-37261d1ab566 | -2.88436 | -48.61367 | 2024-10-03 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 186777fb-1b2e-32c7-a0e4-17ee4cd27a85 | -2.51352 | -47.58191 | 2024-10-03 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ddaac3b-e85f-322a-9fdf-1446e283665f | -2.48468 | -47.59176 | 2024-10-03 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae0ebfa8-1843-39e1-9883-451d4f80b6d3 | -2.45986 | -47.83154 | 2024-10-03 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4247ff92-bbd9-3131-9130-63f72b5e2e47 | -2.45917 | -47.83603 | 2024-10-03 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e569a30-b607-324b-959d-6bdc2c1e677d | -2.3031 | -48.56189 | 2024-10-03 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 847b4d52-262e-386f-a4f8-6edf0211f25a | -5.00112 | -48.42966 | 2024-10-03 04:49:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72b525e7-bbd8-3dc5-81a8-b09cf317b0b4 | -4.80095 | -48.47709 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f8c31095-d7be-3251-ac3e-0bc87fdaacf3 | -4.79723 | -48.47647 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3f058fb3-439b-3b92-a392-cc2ad0015bc1 | -4.58237 | -48.01044 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9eaf8ef0-ad44-355d-b912-3548270fa1a8 | -4.57785 | -48.01454 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 8436b457-1548-37ed-ae35-1e432328d7db | -4.57402 | -48.01396 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 2b228b41-60d5-3a0b-98b0-2a45de466ee8 | -4.57333 | -48.01863 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| d6f6fc4d-3fb9-38c7-a2b7-e5bd97399b5a | -4.57164 | -48.01635 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ce8831ab-c139-3872-9dc1-ceb17388dc1e | -4.5702 | -48.01338 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df771731-ed5f-314a-8500-b0be402693b4 | -4.5695 | -48.01805 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3612be85-bfed-39d1-b462-144b341ca056 | -4.49121 | -48.10861 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20befbd3-41e7-3021-9354-ebd397b9e6f6 | -4.49051 | -48.11324 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7be248a-0722-32cb-8725-5637af78c65d | -4.48741 | -48.10803 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90c77d23-45a1-3da5-b5c5-03d21c76d0dc | -4.28176 | -48.0671 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e155a198-7462-3a38-8241-efd4e36e03c7 | -4.27796 | -48.06654 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67c7293c-d361-363d-98e3-de51a32277dc | -4.19521 | -48.22864 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef3e2359-d7f0-310e-9306-a6c462d23905 | -4.15417 | -48.39542 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eda83f68-6bbb-34bc-8b97-71010462e7b6 | -4.14605 | -48.3987 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0aaaa624-eb6f-35a2-9470-68a9c0a5c727 | -4.14538 | -48.40306 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39d7d4fe-f81a-3477-a7fc-a21d449b763e | -4.14233 | -48.39815 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 160a0d83-bbd1-325b-b26e-9b811edfeafb | -4.10604 | -48.48661 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| bb5bb12d-11f1-3b8a-b805-e73ced745796 | -4.10299 | -48.48174 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad602f8e-3f80-3cd3-8424-903a86f05fb0 | -4.10234 | -48.48605 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| e8574ce2-6d60-3a03-9be3-d64447364faf | -4.09929 | -48.48116 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93ac5932-dce7-3440-aa92-925dd06c4f94 | -4.09864 | -48.48546 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 99a4733f-6a23-3557-ad64-d35e99560d6a | -4.09691 | -48.47188 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af09b73c-3700-34ab-89d7-3709d8def4e8 | -4.09625 | -48.47624 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a2b9dfd-7acf-3e7e-b038-c21a19480911 | -4.09559 | -48.48058 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 652c226d-1690-3c19-9ab6-d8931f62f2e6 | -4.09494 | -48.48487 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e7ae5dd0-2237-3fad-8a59-8ff830cd441f | -4.09387 | -48.46693 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 35bbf60e-8560-359f-92ef-3e2eb872f6ef | -4.09321 | -48.47128 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ee607680-42ba-3514-b96a-ff4dc956d02d | -4.09256 | -48.47563 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8cc0b405-9f06-328c-9c51-e1d9e13ee9e7 | -4.09193 | -48.27703 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7c4d917-c8b8-312c-8a56-2325ee43ca2c | -4.0919 | -48.47997 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e3768f1b-da01-39ea-816b-a103910e41d9 | -4.09114 | -48.27925 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e326234b-03b7-352a-bf00-bb98c5865c67 | -4.09017 | -48.46634 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a7d8e2ec-f983-3e78-af78-200d807b9114 | -4.08886 | -48.47502 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6683f279-d817-3aef-a34d-f479c1c4f5f6 | -4.08821 | -48.47935 | 2024-10-03 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7eab1b7a-bd58-3cb6-87a4-0c90da614208 | -4.08819 | -48.27647 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7855665-d7d1-33d0-afc1-4db04d836dfc | -4.08739 | -48.27868 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81d54c4f-c0e5-3e0c-88b3-a6f122efefe3 | -3.94896 | -48.02331 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cc8dbd5-ae07-308d-9544-ea11e29abd1b | -3.9466 | -47.96156 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8dffc0a-0f98-32d4-bd0e-ac8679721741 | -3.90235 | -48.35646 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d233a78b-ff97-39fb-a341-76e5b98c0d67 | -3.80672 | -47.79718 | 2024-10-03 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84f4fb2e-09ea-3c90-b83b-b38fe22cb32d | -3.806 | -47.80186 | 2024-10-03 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 4239e51e-8169-3a76-9a22-be6463c9f328 | -3.80217 | -47.80128 | 2024-10-03 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5905f1d-3b8a-3c84-8e79-3700ef686212 | -4.72645 | -48.83912 | 2024-10-03 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af9ec02d-01e0-38b5-8053-97ae74494fd2 | -5.22098 | -47.95795 | 2024-10-03 04:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ea0a50d-c508-3c64-a724-62238a23ff9a | -5.22067 | -47.95597 | 2024-10-03 04:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f043d0cb-a0a4-3fd3-8b45-d3084b8f8ee3 | -5.21781 | -47.95259 | 2024-10-03 04:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8b6863e-bcd0-3660-aaac-6e207a978936 | -5.21711 | -47.9574 | 2024-10-03 04:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6353a9e-b169-30a4-8265-25f07a50dad3 | -5.21679 | -47.95543 | 2024-10-03 04:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e5c9869-09f5-3fab-b7cb-b7d5054d0956 | -6.16985 | -49.28627 | 2024-10-03 04:49:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 502bc531-c558-3bc4-a7f9-cac9985d6c89 | -5.4694 | -49.02243 | 2024-10-03 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c25f2ca-6381-3542-bd69-4cd0eb01a968 | -5.46575 | -49.02185 | 2024-10-03 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f9b3c8d-3f91-3ed1-a053-18a12cbeb4c3 | -5.42688 | -49.08094 | 2024-10-03 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55a91948-1d2c-395e-ae9c-69878c7727b3 | -7.73808 | -49.89222 | 2024-10-03 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README116.md)
