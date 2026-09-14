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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1459c9d6-138f-303f-be43-759fac3c0547 | -6.28725 | -55.28784 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 671eafb8-ec2c-3ee2-9a9b-ca2bfb7679cb | -6.28936 | -55.27635 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3352af03-8444-3943-9413-af83cc8575a5 | -2.91953 | -50.44358 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| b6d12348-6535-3b0f-85da-262733f9fde9 | -2.89179 | -50.41625 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 165d66f3-c70f-3eca-90a2-a0ddeed1ff49 | -9.44617 | -47.87706 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b89d723c-79f0-3ece-bf91-6ef3f24adb53 | -8.54472 | -54.69466 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd69163e-9ced-300e-a360-6d7778eac505 | -6.29305 | -55.28925 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13657a07-3e29-3f19-b948-ac489b1092e2 | -9.44918 | -40.38831 | 2026-09-14 04:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3c93fed9-d79c-3b9b-9ed0-e45a07d78150 | -4.91096 | -49.33384 | 2026-09-14 04:32:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c60972d1-f554-358d-9765-7faa4f38c179 | -9.40339 | -50.19349 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f9e14ab1-fc34-34e7-baa3-d3985361f216 | -5.61931 | -45.24634 | 2026-09-14 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54f62fac-b6e6-3121-b71e-a9c8f03ac955 | -9.36774 | -50.13975 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8608280c-118f-3f70-8de3-e8e60ad74285 | -8.53999 | -54.71516 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eaa6f94-a4c0-3f80-8ae0-afa6b4ffddd2 | -3.39312 | -50.75576 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3343ab1-0ddf-3709-93f9-079ebf886b5f | -9.31792 | -44.35551 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7a903fb-c388-389d-906a-0002882f2964 | -6.28276 | -55.27935 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75cba6b5-4699-3438-a290-3cc9d2b6efd2 | -8.99671 | -50.82046 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb93059b-41a5-37cc-a246-216b20ca0475 | -9.4192 | -50.1488 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d44b252d-f1c1-3ccb-9f5b-b71879f3e362 | -3.38437 | -50.39003 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2cbe98dc-633f-3700-ac35-626770a73554 | -9.43368 | -50.13554 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0da28d1-5eb7-3685-a6d8-e6d58facf649 | -8.00045 | -43.78409 | 2026-09-14 04:32:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5e96fdba-522e-3be7-aa09-33a52b9c1ad3 | -6.37073 | -55.26078 | 2026-09-14 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 549ba51a-3b08-328e-aba4-96280bac1fa2 | -7.09605 | -42.10585 | 2026-09-14 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b6240ab5-e90d-35d1-bff4-a2420071225c | -2.96528 | -50.39998 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ee5c621-a6ef-3b99-b19b-66947c91bf23 | -9.44726 | -50.12743 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dd635e16-f3db-37f3-bc6a-db9def395794 | -2.92217 | -50.41099 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 192.3 |
| 6b63290a-9145-38ce-ac65-3e37baa6d487 | -6.57762 | -58.83878 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc87e17b-3182-3769-82f6-a2c38faa0e08 | -3.22547 | -50.58678 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91328e18-bbf3-3e85-b1ee-8c57d533dfed | -7.46355 | -45.96368 | 2026-09-14 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63fb4fe1-7666-3946-89db-f06d896a2a70 | -3.37853 | -50.39773 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7376f235-cf56-3204-a796-e0d10b9bc14c | -2.97001 | -49.56216 | 2026-09-14 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 607dcddb-c7b2-3fd4-99c6-62109d16f5ab | -7.83406 | -47.93484 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11ba0d45-c09c-38db-b814-30b4c3fcc978 | -7.11621 | -41.79691 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 75579b91-6e6e-359c-b0e9-a0f5acf4f4b1 | -7.47323 | -49.78039 | 2026-09-14 04:32:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9d967c3-a32f-3071-86f6-a941ebb115ac | -2.90001 | -50.42213 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 189.2 |
| 1bf0d129-13b1-3f67-9ec7-2c83f15584e9 | -5.80543 | -52.11353 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| debbe883-cc17-3fe6-a0be-1679ddcfa328 | -2.91741 | -50.45677 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a638baef-6aae-34aa-b837-635237e551d9 | -7.11273 | -41.79891 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c8aaaac2-c35e-39a9-bd3d-403fbd5c4160 | -5.80151 | -52.1077 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7c8b6cd-11f4-35dd-9cbe-ad933c302022 | -2.26976 | -48.74616 | 2026-09-14 04:32:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 029ddcfd-915e-38d6-b3e1-c7b53b5b7c7a | -8.54408 | -54.69807 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de8c925f-a0eb-3163-83ce-33aeea1a3cb5 | -3.1602 | -48.61131 | 2026-09-14 04:32:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70949ac5-741c-31ab-9655-e09070502870 | -6.30765 | -55.27559 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 977782c5-efb0-35a0-82a5-712f31f007d1 | -2.94816 | -50.3927 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fd64ac6-d8d6-3177-9107-ecdddec1ee6c | -8.57486 | -44.46459 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c522175c-6e2d-3979-a8c9-b9f85060b53b | -6.79772 | -58.78827 | 2026-09-14 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79095e95-0f48-3eda-8eb0-fbc99d3364a9 | -8.54759 | -54.70937 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3b83fb3-dc4d-37f6-abb7-22283927b188 | -2.93852 | -50.39557 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74592824-0e20-36ae-bc79-e252c84270f1 | -2.91846 | -50.43304 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 274.4 |
| c5a8df40-98f2-3f21-a830-120330393981 | -5.49095 | -45.60515 | 2026-09-14 04:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a35a6fd0-3fb3-3abf-a3f6-a4ddbade1fba | -2.9179 | -50.42513 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 648d7587-d8c5-3f3a-97f5-ac8fe5a0feae | -8.23244 | -49.96111 | 2026-09-14 04:32:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| afbc6d96-bf05-3f0d-9f63-04259452f40f | -5.81159 | -53.79649 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55f48888-0749-3428-a43f-06071ea20bac | -2.67334 | -57.57233 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c5f09dbe-1cd1-30e6-b739-dff4437b3c9d | -2.94298 | -50.39632 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b379491-16dc-39fb-9b38-d06f43eae5af | -7.87106 | -54.72813 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e088c262-73dc-3987-9d25-28644e507398 | -7.08664 | -41.79681 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f51b2b22-f60f-3ed9-acca-328a2c4c58be | -2.93636 | -50.43591 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3db81cbb-3b56-3526-84a6-03c1b7f05163 | -6.8544 | -55.56668 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 476db133-822c-32fc-870b-424069a15870 | -9.45323 | -40.38887 | 2026-09-14 04:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.2 |
| 7a79763d-b55d-3536-81b5-070662e1b426 | -2.91128 | -50.43771 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| b82f3cbb-bbdf-3d58-bfde-5bd13587c8dd | -2.89983 | -50.39498 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d09002bd-3739-31f9-8c19-ed0d6d727527 | -9.33416 | -44.36169 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13f871fd-62af-3661-9c09-c8c0b08d481f | -4.34594 | -48.9647 | 2026-09-14 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e4964a56-a262-3aea-9979-22902a656f95 | -3.73879 | -40.42064 | 2026-09-14 04:32:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5ed2cd10-cbe6-3192-b8a6-abb5e5cde1a0 | -3.33595 | -54.1889 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d5d57a67-229f-3f23-9309-b28a01d2413c | -3.22281 | -50.59299 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fe98ade-b98b-30ce-b0d1-4fad4ead992d | -3.77582 | -51.35443 | 2026-09-14 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0daa027-0a60-3af8-9d38-407df7e94f57 | -6.10461 | -55.66394 | 2026-09-14 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a4e8784-9262-361a-8dd9-376daef74b0e | -6.29643 | -55.27938 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3df0280-c9b4-3bbc-8f69-d36ef07c15e3 | -2.67869 | -57.56292 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf661308-a414-3d23-8ddb-a76c547acc44 | -5.89887 | -42.68575 | 2026-09-14 04:32:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d9b942d-300d-34af-874a-4715e05fa7be | -3.86365 | -51.97833 | 2026-09-14 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2564fb33-f02e-3843-b9da-409ebded08fe | -4.13762 | -54.01105 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3fb2307-5aa9-3d72-a3aa-a3ef74d4123b | -6.7848 | -47.89047 | 2026-09-14 04:32:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5aee21b-8251-3dbe-94df-b9ad24a3064c | -2.91393 | -50.39278 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 26e1885a-976c-3076-9ff9-997e67f0364f | -2.93258 | -50.40366 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c564edff-1bc5-3cd9-9f53-85e21588c96e | -8.45702 | -46.86097 | 2026-09-14 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9fecbbd-0898-3e70-ae12-601af167bc7a | -7.1182 | -41.787 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b44a09fd-227a-3408-b5ab-f4e020742437 | -2.91505 | -50.44284 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| bddc8ad7-63f0-3b64-a82b-72ea50688277 | -3.41161 | -58.21733 | 2026-09-14 04:32:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7e37d32d-5060-3d2c-af11-bb1c433e4053 | -6.66477 | -54.98199 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3074a832-8f7b-3ed0-9f65-6e3d8296e155 | -2.93488 | -50.44478 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f218eb57-85bc-3438-b0cc-40698666fa20 | -6.33907 | -43.36271 | 2026-09-14 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d83489e2-9343-3e64-b4f0-60daa4694f41 | -4.40218 | -55.23395 | 2026-09-14 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98e03f07-7439-3b31-be4e-d52c50bef44d | -7.07513 | -41.79954 | 2026-09-14 04:32:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 467f8e47-fa71-3ac2-b10f-1197c38f408e | -9.39985 | -50.16648 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| a2a35787-ea3d-3076-ba63-2d8d4665d959 | -3.75877 | -51.15371 | 2026-09-14 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 718de0c8-774c-372d-a997-03612f87fae7 | -4.13569 | -54.02245 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17bc15b7-08c0-3c99-bb0c-1bafa3d9e490 | -6.46598 | -46.18965 | 2026-09-14 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43ae8e11-a739-35a1-ad70-80a59682a0cc | -2.91249 | -50.44115 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| ca2d3964-f5a3-36d7-94b5-098bbcb2cece | -6.10375 | -55.66857 | 2026-09-14 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5befa129-946d-3ad4-81b0-bbfdb06eb309 | -2.92613 | -50.43103 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 458105ce-d7b3-33d6-a3c9-ad62a9d90d1d | -7.09982 | -55.63022 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 825ac37d-4073-38bd-a9f4-96f6a62e8f09 | -2.90089 | -50.44508 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf236a5b-ab60-302b-b06e-c175283b0cc9 | -4.27303 | -46.53241 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9a98e40-5c47-3cac-8324-b63ed4f3621d | -7.77602 | -46.66469 | 2026-09-14 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 684d6e70-2052-3063-b548-36135aa7efff | -3.4664 | -47.46294 | 2026-09-14 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77c71adc-6171-32d8-ad44-6dc291a2cae1 | -2.93108 | -50.40014 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a658a7f-0aae-358f-b479-2957025a4742 | -2.9304 | -50.44405 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README21.md)
