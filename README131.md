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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52c9b0a7-8f4f-3fbd-ae0a-10026bd7c3ed | -5.47658 | -45.11862 | 2026-08-28 17:28:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ca8011c6-722a-3ab4-af25-197fd3aebca1 | -8.0146 | -51.79448 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2e4b4fe1-c5a1-3e6b-a4c9-b3e3e1aed7cf | -6.84621 | -59.93633 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 3c0e5611-ea2f-3d5c-a412-165b82d12950 | -8.64383 | -66.53777 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8451592f-6839-3fee-ae96-f7eed5a62f69 | -2.78598 | -43.6362 | 2026-08-28 17:28:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 3e22cc09-e6f8-31d4-81a6-f8aa45937490 | -9.9148 | -60.44345 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 37746e12-10db-38ce-bc4b-3b820eba51b8 | -6.12073 | -53.74334 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5fbc092f-ddbf-3a74-b497-b25160542eff | -10.57253 | -57.48762 | 2026-08-28 17:28:00 | NPP-375 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 6f5c0951-4669-3202-9a10-2aed4de3eb30 | -10.40737 | -61.19692 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 87f3f421-3540-3e24-a9a2-713bdadb7e05 | -8.14537 | -70.39481 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 2e2a5452-ef7b-387a-ae94-55a16477e743 | -8.784 | -49.96257 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0137db8-e9c6-3318-9ea1-0472713eb33b | -10.40788 | -61.20056 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| b5cea769-d032-3bd5-93b3-8611d030a53b | -4.05586 | -56.23299 | 2026-08-28 17:28:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 032bb3d4-efbc-3b1f-8d4a-af6d933c79ce | -4.3098 | -59.47511 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 8ce226f7-f203-30d0-893c-e0a35da1130e | -3.90889 | -59.6348 | 2026-08-28 17:28:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4ab81451-d884-35ef-a219-42525dde849e | -7.47497 | -61.38924 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f4692b3f-8364-3677-8c24-b1c003e41358 | -6.84503 | -59.95354 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7c635a34-7738-3a76-9cbb-84899e182495 | -9.15244 | -59.56363 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c836f5af-ae72-3fb3-8a8c-a8d53eec1603 | -7.58783 | -61.33952 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 8ee8a91e-1dab-39dd-aebf-14bbf46a754d | -6.41358 | -54.97338 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ac769491-d35f-3e49-8246-9a5088aa7785 | -8.53569 | -55.26586 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 19c146d8-1975-3bcc-ba39-9381a471cdb6 | -3.76547 | -57.97949 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 11c4874d-9ed0-36f8-b574-d5f58e90bb82 | -4.14343 | -59.39304 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 376f762c-9c8b-33f1-b998-7c00d2bcfb21 | -7.27299 | -49.86032 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| ce623209-d5dd-3b72-bf23-0269ad2e7f0c | -10.47216 | -64.48985 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| dd35c93c-8510-3bda-82b2-9fee5bace883 | -6.96852 | -55.64286 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6ee6b359-eb27-3bba-9364-2c6cee102c10 | -2.85641 | -48.5537 | 2026-08-28 17:28:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fee727f9-6add-3e7b-8487-82ba4e2914be | -6.79605 | -59.39939 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| ddae4bca-1f26-3433-afc4-fddeae030ffc | -4.9559 | -55.78133 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 74cb73c7-36b9-3142-a540-7cc31bc240ea | -6.41211 | -51.67678 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 7e901bb4-8d70-3c8f-8fe8-9ba08ced9324 | -6.70583 | -58.93705 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2da19f7b-3e84-30af-8b0b-97e6a1cf70b5 | -6.17903 | -53.50214 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0f74024d-88d1-33a5-b6eb-b001f05d2279 | -8.23738 | -54.9648 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 88ec331a-8bd0-3513-9494-ba85b7735f50 | -6.79713 | -59.60214 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| baba49d3-8db7-3692-9f6f-08fe868cd8e4 | -11.41523 | -62.11692 | 2026-08-28 17:28:00 | NPP-375 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 28.3 |
| c3dfd93f-10ce-3fe0-8739-0c9250a9e6b5 | -8.60654 | -54.78028 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 82feae7e-4de1-37a0-af0a-7191fb5ed6a2 | -8.01208 | -51.79217 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 437cb9e9-7f3d-3a26-814f-e99c3b4915cc | -8.12646 | -45.47516 | 2026-08-28 17:28:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bbcfcc73-8523-3936-bd45-53a37ee8e57c | -5.15365 | -59.79752 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1b2ecbe6-6591-3d45-83fa-d8e4727ddbcd | -4.14687 | -59.39252 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a23ada9a-48d3-3f9d-aed0-ea0e44093faf | -6.59653 | -55.42847 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a5d66a21-7405-37c4-9e7d-3a1e47299e10 | -4.39023 | -55.45918 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| ef685bf1-6243-3d4e-afbc-7e36c9f20004 | -6.4472 | -64.49255 | 2026-08-28 17:28:00 | NPP-375 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 52a31723-4e9b-364f-9b22-a08f6d12eae2 | -9.75792 | -64.97627 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 55b81cbb-b5bc-37ac-aac1-5170b0c1c0cd | -9.70292 | -65.08867 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 8a5dfe52-22a6-3764-9157-95dbaa82fb9b | -7.58494 | -61.31931 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 154e51c6-009e-3bfe-9515-df5733c76e77 | -6.62421 | -52.0291 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5ffe53b9-2fbd-38f8-a864-c8c010cfd15e | -4.39081 | -55.46292 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 453e6655-5315-3464-a439-7cd1767b0348 | -5.09298 | -56.14608 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ed7e0efa-8084-3b31-8aa2-cb9b3b3a9390 | -6.16009 | -61.77097 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 97e96534-19b6-317f-948a-0e9413793216 | -7.33613 | -55.70078 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| adb52eb4-7232-389d-88ca-319c19e12426 | -8.08916 | -51.66357 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9de2c8be-9d1d-3e1c-a81b-b73bf3681f3b | -6.69064 | -58.7175 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ffdc926f-293a-36a6-a87c-b00728b7e9fc | -9.23106 | -59.77129 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 894ffcff-0437-3b68-9835-03c0654dfc52 | -6.16563 | -57.79243 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ca172178-70ee-3a85-84f7-520ace9dab9c | -6.60107 | -55.45754 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 615c65bf-5a30-3c54-8efd-66c1ee7cb6f4 | -7.58351 | -61.30927 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7cd19d58-1703-358b-bde4-084b9ad0e26e | -8.6037 | -54.78452 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a8ec3259-5322-3325-8851-f742ae228bb1 | -6.8432 | -59.94102 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 25f68751-758b-3823-be08-39b41f3370d3 | -7.35458 | -55.16562 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b0b91a83-9d53-3a94-9338-0b625db75609 | -5.82032 | -52.32315 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6a3ef2ad-1e94-3118-b027-bbf509d13f5e | -8.82436 | -49.63725 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cdfc6050-495d-38d4-b73e-d25d9bfefa87 | -10.39973 | -61.20171 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 51a0ef25-99e5-315f-9cea-6c47816a0325 | -6.75908 | -55.68708 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| f9f8a1e9-966f-3584-939e-6962a76f6bbf | -8.82279 | -68.96966 | 2026-08-28 17:28:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 890a6a51-0776-3f9d-8eff-3f77df96ff79 | -4.33241 | -54.89993 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| c07e59c9-9914-3fd2-ad51-4fc8ef94417e | -6.11376 | -57.82609 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 635cb837-0ef1-356c-aa59-6e23b1fc0c6e | -5.94693 | -57.73003 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fcae957a-8d9c-304b-b0cf-29aa0f1d0a38 | -10.20508 | -69.35725 | 2026-08-28 17:28:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 36.8 |
| d410050b-adf3-3ae0-b752-f856ee246843 | -6.69407 | -58.71699 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6bab602a-2d7d-377f-b20e-c05000a75005 | -10.76304 | -53.96949 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fbdc89a2-1e17-3bb2-9bdb-90029c1cea98 | -9.43635 | -51.6847 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 330e172d-001b-3a4b-9078-f990961964b9 | -7.5845 | -61.3423 | 2026-08-28 17:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 277.3 |
| 7642ab78-3e3f-36b4-89c0-38dd9cf5f9e9 | -10.4981 | -64.5005 | 2026-08-28 17:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 77187c2a-2244-3998-bffd-12e5272fd9cf | -6.695 | -58.7291 | 2026-08-28 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 2895d694-1d17-3ae9-bbfc-654c6a86bd2c | -7.5104 | -61.3832 | 2026-08-28 17:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| b86911de-0697-3eea-ad05-3ff315eaac9e | -9.1525 | -65.7874 | 2026-08-28 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 809b5022-8a76-341f-b333-77800f3ad40e | -8.6495 | -66.5468 | 2026-08-28 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ae1ab64e-5dc3-3430-873a-568b5735f6f5 | -8.6924 | -70.7498 | 2026-08-28 17:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 41.5 |
| d09495c7-b0a0-3460-9508-0feec989e5db | -10.5601 | -50.4022 | 2026-08-28 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 35ad32ef-cfa1-3072-9b6f-a23cd226d9cf | -6.7833 | -59.4208 | 2026-08-28 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 424297fb-3408-3468-9b41-53ae402fd27d | -7.5851 | -61.228 | 2026-08-28 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 64ded344-6d3f-396c-9b93-dfcd68d34ea2 | -9.2081 | -65.7857 | 2026-08-28 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 4fb9ed88-f360-3795-9967-53cc85ca7641 | -7.5852 | -61.2089 | 2026-08-28 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| fe704f22-846b-3462-9b85-6e05d1f1ddfe | -6.7831 | -59.4594 | 2026-08-28 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| a1d33eb2-971f-3971-a06b-c60c477c5c11 | -6.018 | -57.8242 | 2026-08-28 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 92aeac80-cd24-34cb-8c82-fa56816cf20d | -9.0254 | -70.58 | 2026-08-28 17:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ae2b47f9-cf67-326b-be9c-273952c0284d | -11.1998 | -55.0805 | 2026-08-28 17:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| bb96c403-c0f0-3c42-ad76-69b82ac6abba | -12.2281 | -50.5578 | 2026-08-28 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6d7118fd-954b-3591-8e07-5290527fd60c | -8.6311 | -66.5287 | 2026-08-28 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 069d6865-5d8b-3e1d-b6d0-da4e1fa4f036 | -6.598 | -45.201 | 2026-08-28 17:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 1b80865c-05c0-32e2-a41f-9024b92bfd5b | -8.631 | -66.5473 | 2026-08-28 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 55e5065f-4b5e-39ec-aec0-dca190fc08f5 | -12.3999 | -48.2073 | 2026-08-28 17:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 4248fdbe-555b-3178-8711-8b1c44e2f5a6 | -7.4735 | -61.3846 | 2026-08-28 17:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| cfb876ae-1f0c-3162-a56a-806ad71b10fc | -7.5846 | -61.3232 | 2026-08-28 17:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| a868e50a-5601-3aae-affa-74bc9ac5589f | -11.2128 | -53.9976 | 2026-08-28 17:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 773fc205-8450-3fed-ba76-edb2bbad8676 | -6.8571 | -59.4179 | 2026-08-28 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| a4a7b11d-b4b0-376c-aa0c-78edd3a177e4 | -15.4788 | -53.9628 | 2026-08-28 17:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f51a8947-2649-30d4-9dc2-040296ab5eaa | -10.8422 | -50.5219 | 2026-08-28 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| b988b751-15cc-35a8-87f7-27ecec58a6bb | -11.2187 | -55.0788 | 2026-08-28 17:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |


[Clique aqui para ver as próximas entradas](README132.md)
