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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2bc6127-1856-3121-90ea-80505d6c7593 | -7.66865 | -46.00091 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| db9efd30-9792-3a40-addc-9d3e8c490e26 | -13.63503 | -48.08707 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e05027e1-c65d-3110-8e59-4dab0201c9a5 | -9.9933 | -49.26582 | 2025-09-26 05:04:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5db731ea-1688-3315-b654-a2e69ffd169e | -13.63469 | -48.08985 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57f27c24-4593-3bcf-94ff-4ea5030c18d4 | -10.45594 | -48.24103 | 2025-09-26 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ddda123-477f-3c4a-842c-79c8ba847b4a | -10.4064 | -46.1824 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c2f19d5-f58a-3b93-a958-12fa5df63cc2 | -9.70048 | -48.25334 | 2025-09-26 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18cab881-1834-3253-84db-219dba169e4f | -10.40739 | -46.17442 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1f582b05-436e-3dd6-8ab6-ec98a501df4d | -11.04603 | -45.88342 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 029edc45-eb13-3feb-aa25-7f2289caec52 | -10.11397 | -45.3089 | 2025-09-26 05:04:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbe36482-eef5-358b-9e00-3b1b46796685 | -11.23619 | -45.56125 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17fd510f-836d-39c9-b35a-e4d3a7d9abaf | -11.68211 | -44.45472 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c4d1897-589c-3f8e-9d2b-2610230ae32f | -11.21538 | -45.57437 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d75a0da-8366-3ab1-903c-ae96ba4390f4 | -11.25006 | -45.54877 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bad9999f-b63c-3200-820b-0d96d384a8f1 | -11.42278 | -44.98585 | 2025-09-26 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a610091-9d19-37d4-bd66-0e3b37bed676 | -11.95435 | -47.87974 | 2025-09-26 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b90edf31-a120-3ddd-abc7-0d06bca05d17 | -8.84499 | -46.61131 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50cfa218-09b7-3fcd-8454-499e1cfacf1f | -7.80155 | -46.01831 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8dc9ff6-c844-31be-9c66-169dad87cddf | -9.75655 | -45.95043 | 2025-09-26 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09c7f97c-e2bb-39ad-9b35-3e3c6b431a1d | -11.66898 | -44.45318 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3657720-6363-3b19-9282-8c877115c3cb | -7.31493 | -45.76264 | 2025-09-26 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2e4a4d9-f977-3c79-9ce7-de1da2b0f21f | -11.96911 | -46.627 | 2025-09-26 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b81d1ee-c251-36e3-918d-e440a9abd6ac | -10.2864 | -45.22328 | 2025-09-26 05:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 762271e5-cd02-3470-9789-fb06f534e75d | -11.21584 | -45.57642 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 94aa5846-f7b9-3524-9bc3-31f943c9502c | -11.66974 | -44.4537 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c570881-0c2a-32a7-80e3-5a1dd526d36a | -9.69186 | -48.94518 | 2025-09-26 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fbe56777-7c79-3e9a-856a-5f0eeacf12c0 | -10.4084 | -46.16621 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05f26349-9368-3918-9d03-c0fc9982de7c | -10.40169 | -46.16993 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b905540-6697-3812-9a77-deae69109b0d | -12.7319 | -43.45877 | 2025-09-26 05:04:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b7794ad1-f094-36e8-a3c1-650dbd28959f | -9.70547 | -48.25412 | 2025-09-26 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cf5b0ebc-779c-3504-af03-720065e5230c | -11.67042 | -44.44807 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b2faa81-6c94-324e-ae37-b5a36492fcd2 | -10.39302 | -46.14731 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c002246-71a2-3f86-b49a-b4b406e2da61 | -7.31385 | -45.7705 | 2025-09-26 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed48ba73-c39d-3cbb-8274-dc1314a1aa45 | -8.4952 | -49.54639 | 2025-09-26 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d7117deb-8f09-3767-963c-44551fb79bb9 | -11.9645 | -47.88454 | 2025-09-26 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5781a5ec-b591-3403-b98f-ee96fcf83d77 | -13.63434 | -48.09267 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe57d348-a9ec-3072-961b-eb9592bc36e8 | -11.61202 | -44.43537 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| adc3b51c-55cf-339d-8b03-caa79215bfd3 | -11.2434 | -45.55268 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cd0706b9-618f-366e-960b-265f3f06f381 | -9.756 | -45.95471 | 2025-09-26 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ea82b9b-f179-356f-888f-2da17df0cd90 | -7.316 | -45.75478 | 2025-09-26 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d19ebc6-6f77-30db-858b-3382e9d63afd | -10.89856 | -55.45573 | 2025-09-26 05:04:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7cdcd755-24b3-312e-adc0-c05711da9545 | -13.8466 | -45.62436 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 414f9509-1161-3d7f-b186-d1327fd4f69c | -11.96005 | -47.87725 | 2025-09-26 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a3a04cc-d586-3349-b890-b48283d1cb36 | -13.74521 | -47.87426 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f643d52-20e0-3a2b-8269-1a0d493c51fc | -12.84488 | -44.71278 | 2025-09-26 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bbdf69e-9a2e-3723-9ee4-0d8ac46fea94 | -9.95529 | -46.29758 | 2025-09-26 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a48fe1a-1e07-3b31-b650-fbfc0026c9df | -13.84826 | -45.60885 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4796779-7ddd-3769-897a-42ae5695a75e | -9.70516 | -48.25373 | 2025-09-26 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 79480f71-3735-3f71-a1d4-8b19dfcf59e3 | -11.67618 | -44.4483 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d34f442-ac99-3a8f-9a4c-f336f2ea9b38 | -11.97486 | -46.62768 | 2025-09-26 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f79c95a7-cc38-3b20-b6ea-443b02ccfccf | -11.23786 | -45.54726 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7d28c9df-13ec-34f5-8e3c-585786d7e55a | -11.2495 | -45.55344 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96a2f577-29ae-39f7-93fe-2608a3cbd7f8 | -10.2863 | -45.22505 | 2025-09-26 05:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f9f68a2-8590-315b-89d4-e97303d69f14 | -11.65265 | -45.3519 | 2025-09-26 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cd0c426-708d-3b78-a62f-1bb26684fb3f | -10.62308 | -53.88832 | 2025-09-26 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 700867fa-ef3c-30c9-8dc9-408b6b86b3fa | -10.7976 | -45.37491 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68ae1762-8c12-3dc9-b2d4-e8d641b52d10 | -11.64823 | -45.34868 | 2025-09-26 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a3c4fa4-3078-3715-a332-e882fdea76ee | -10.6041 | -49.64174 | 2025-09-26 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d63fe2a2-01cd-3c0f-b7ab-0cae56b2e536 | -13.85083 | -45.60651 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f14e31f2-4d51-35a7-a298-822e7c4120a0 | -10.39883 | -46.14803 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5c88816-7a61-3132-abd3-d8b11ce92e63 | -10.2857 | -45.22982 | 2025-09-26 05:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0179630-5db5-3c22-a92c-baa422c962fc | -10.40162 | -46.17342 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8dbb9d7-106a-3aa6-9006-18f1b3751ca9 | -9.91108 | -58.56308 | 2025-09-26 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc62b2fa-ff2f-3fee-ad1d-55dfc510673a | -7.66916 | -45.99707 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 59dd8d6c-ee95-3ca5-b787-ea6fc06967aa | -9.69256 | -48.9401 | 2025-09-26 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bc404e8f-2089-3826-a42b-cfa982d38e5f | -10.62603 | -53.89293 | 2025-09-26 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4057dd4c-1787-3c55-8e38-4e1456a03122 | -11.24229 | -45.562 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| abba378d-9d27-3ace-b385-b66eba06544d | -11.61858 | -44.43619 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5de1c0ce-13ff-34e6-8995-3081306eaff5 | -11.42214 | -44.99136 | 2025-09-26 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c39e3636-445f-3094-86af-4682997e3454 | -11.21633 | -45.57226 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f3c705c1-b67d-3b4d-a839-6f4f7bed7e78 | -9.97805 | -49.25613 | 2025-09-26 05:04:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abe27929-aadb-3c92-a0f5-7e03782dcbcf | -13.84142 | -45.61336 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e1d3e48-5ebd-3725-9515-9d7e335ae72b | -8.71579 | -50.05156 | 2025-09-26 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8809843e-33f7-3455-96ba-39b707349b43 | -11.97438 | -46.63164 | 2025-09-26 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66d7be47-2d23-3c86-9896-8507d464ad52 | -10.11346 | -45.313 | 2025-09-26 05:04:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c78f779-a293-371c-a6d3-4d89bed077ca | -10.40117 | -46.17395 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a9adaea-39fa-38ce-8459-a5ceb3417b2d | -9.56439 | -47.69525 | 2025-09-26 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfbc036a-56b9-3263-90b1-cb2193d57d86 | -12.8455 | -44.70722 | 2025-09-26 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6d0f65f-2032-38af-871c-1c8588676386 | -13.32824 | -47.89046 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7c36942-c020-3c04-b260-f42782803af5 | -10.62322 | -53.88914 | 2025-09-26 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b39f741a-b22b-3b69-aed3-54c49853b864 | -8.07987 | -55.2261 | 2025-09-26 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f91cb826-2932-3a53-ad63-3d0d583b039f | -10.40365 | -46.15686 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc31f720-fd18-3355-8cae-642d949b25eb | -9.47214 | -48.24128 | 2025-09-26 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13fb3643-54f7-377a-b02d-af82098d1cb8 | -8.84548 | -46.60777 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a66870c4-5590-36b6-b270-c713ba95bfb3 | -13.84279 | -45.62125 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb4baf25-6f15-3b67-a6ab-69c7319c1813 | -8.08091 | -55.19738 | 2025-09-26 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f1c77ae-33e4-3dfa-bbd3-425c2654301a | -12.56016 | -45.85074 | 2025-09-26 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5c4d7fb-cf5e-3191-a9da-aeca13fcec6e | -12.73671 | -43.45916 | 2025-09-26 05:04:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f02dfce1-35ae-36d0-94ef-83e478511a82 | -13.85594 | -45.61737 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 247909f6-cd45-329f-89e3-8a68fb9d854d | -9.70627 | -48.94886 | 2025-09-26 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1294f429-a5da-35ae-b771-2af5834522c8 | -13.65095 | -48.08987 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 227faaeb-44eb-3fa0-bc9b-8bc3cfa6f04b | -12.35511 | -51.21177 | 2025-09-26 05:04:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e39d4ca7-8224-3005-9ba6-26163fde6a96 | -12.4785 | -54.30804 | 2025-09-26 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26fae815-c876-3790-ba2c-bcf4f66b0808 | -10.8087 | -45.38573 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad49f818-138d-3e47-955e-9c0f8eb79397 | -12.1314 | -47.95539 | 2025-09-26 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cfadb04-e5db-38bc-a7e1-eea5494a4837 | -10.00712 | -44.1848 | 2025-09-26 05:04:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5fce8bb-bfed-3040-a89b-8cde8b12d3b1 | -7.30869 | -45.76571 | 2025-09-26 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10a9f60b-8337-36c2-9e82-3d3a3594ec9d | -10.0085 | -44.17378 | 2025-09-26 05:04:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 770ce974-3f7e-312e-8dcf-a05728b9bcad | -11.61136 | -44.44102 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 4d2e0a1d-d122-3c7c-83d1-41b1dc854d1e | -6.995 | -46.99279 | 2025-09-26 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README44.md)
