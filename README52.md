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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a464a70-5641-3e0d-927d-b928a8374b1b | -11.80824 | -44.70428 | 2025-09-16 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6339ed12-6698-36b9-934a-d1c680414ec8 | -12.1129 | -44.8406 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d97a8a3c-bd07-33c9-8fe2-979dc4378e9c | -11.91144 | -46.74802 | 2025-09-16 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afebb88c-35c0-3fae-babb-8bb59a424aa9 | -9.05353 | -44.8398 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 343c3f13-f1ac-3e37-bb66-3ad8ac4db6d9 | -8.12262 | -48.26998 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b87d62b-0ae2-3929-9308-28b5d103fa3b | -10.64126 | -48.74458 | 2025-09-16 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04523aa9-0cdb-3b43-aca5-39039e2d537b | -9.05295 | -44.84357 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6a6a9ca-ad54-34cc-982c-04771b6e4db9 | -9.09619 | -44.84975 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 407af71b-e91c-3955-bdbf-790bed1d1459 | -10.71664 | -44.76741 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ce5583a-2c82-3e24-bb4e-249c5921062d | -11.04926 | -48.27934 | 2025-09-16 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80393573-a9a0-38e1-83f8-ff222c4a28d2 | -9.15154 | -46.96919 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ba447a9-8785-3738-97dd-49528ac39759 | -11.23879 | -49.9511 | 2025-09-16 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c48e1e1a-f7b4-37bb-8d6b-9e48df510071 | -9.45868 | -48.58274 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8527e8a9-54c0-3a55-834f-7d5a93cfa6da | -8.17295 | -46.75919 | 2025-09-16 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47394ba0-8307-3da8-bc5c-480e72c24249 | -12.11888 | -44.81547 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e14fc89f-5097-34af-9715-77611ab4b0f4 | -12.05168 | -46.56463 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc706b27-937c-3c87-908c-6889a7fdae0d | -7.68176 | -46.29219 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1226c76-e2e9-3d0f-8855-b5b2eb89e07d | -9.04663 | -44.83875 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b6e75569-8d08-3d9b-871d-b44aca291e3f | -11.29975 | -50.8501 | 2025-09-16 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef5d76dc-43d1-30c1-8a0f-5ee598cb743f | -7.67357 | -46.30524 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40993dd4-b262-3e13-8866-222b81b967d9 | -10.72602 | -44.75298 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 14485f93-a93e-3116-8050-4334135d3dcb | -12.43919 | -44.74828 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8b034d91-15fd-3d22-b684-a034eb700c7d | -10.74345 | -48.18137 | 2025-09-16 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2206fd18-993e-3f93-8d88-cf9221374ec7 | -11.27576 | -45.30518 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5aba81dd-8e4e-3570-a62c-23b2a5274c44 | -7.68839 | -44.67075 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 307dc815-4ffa-3d26-adba-a79707850428 | -11.12888 | -45.35305 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09fa9ff7-dee2-36b1-bbfa-8dbbfaa98155 | -8.87774 | -46.17552 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d05aa0e-cabd-3b48-8748-95170656b948 | -7.67667 | -45.13195 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 82594728-5dc6-38d9-a35a-14d34b358200 | -9.86125 | -46.45366 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d0de473-47d3-3d30-a202-1644cdc4f8c9 | -12.05895 | -46.53996 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cfaba6d-f1b3-3dfa-aa55-117600a63533 | -7.39563 | -50.00291 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f009de30-f00c-37b1-b743-33231d9c5919 | -7.68285 | -46.28522 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2014857f-aea4-3c60-9a61-c85a9a4fc3cf | -8.08814 | -46.82806 | 2025-09-16 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 70665370-cab9-336c-ab54-52c161f687d0 | -9.72981 | -46.04062 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56a14c56-1c4e-32d3-93db-7442818ef4ed | -11.12543 | -45.35252 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 585ae5ee-8208-38d7-b7bb-5c95c5706016 | -10.6406 | -46.46376 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a959a89-7cfe-3390-a771-06578d24d0e5 | -11.7032 | -46.88662 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 443c97be-db45-3118-af85-4fb5d5796f32 | -11.11623 | -45.34335 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 977a5c85-88a9-3dff-bb7e-c66bce08b17e | -7.14563 | -47.98256 | 2025-09-16 04:29:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07ccac12-7908-3232-a74a-5aac81389482 | -12.80992 | -47.18697 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4a258b24-1528-3918-a980-eb4c5ff17194 | -8.88737 | -46.1918 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f790acc-d515-3081-97ce-140fd4a89b4b | -11.29774 | -43.18692 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc0fdad4-f265-3094-b282-9619294c71d0 | -9.0983 | -46.93915 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44e088d9-5e85-30f0-acbc-6104cfc9eb39 | -7.70761 | -55.45262 | 2025-09-16 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d7bc33c-8231-3781-94ec-605b4b28540f | -13.20639 | -47.30914 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c1bfe59-81ca-34bb-9dfe-08e4b459ee50 | -8.60486 | -45.73414 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 477dffa3-94b2-3b23-8453-1334530cbf11 | -8.61516 | -46.38257 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcb29eca-fa48-33d6-99ca-c5e292fa4e98 | -11.66749 | -46.85947 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32128a0b-fb31-3e9b-b264-263bd0b5e47c | -12.62585 | -45.75558 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 276ffdba-d3e5-3210-b6a0-9e2f328ea301 | -11.07728 | -49.75005 | 2025-09-16 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddb90c37-5f9c-3cff-9de8-42c2441dfa84 | -11.71541 | -46.87418 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1b724026-6530-3306-8ecb-7e8303367cbb | -7.72247 | -45.30545 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73a06be3-fa8f-355b-863d-ff9768f56151 | -12.62298 | -45.75126 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbf5ebbc-7c18-335d-a0dc-71d232806065 | -12.0584 | -46.56569 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5f7830d8-b8e7-35b3-9d0f-c7e045346cd8 | -12.66609 | -47.92715 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 017c8df7-1c85-389f-93fb-c0f030eb1272 | -8.41669 | -45.7415 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0ea20ad-38ca-3ab5-8b29-d536f849ab2d | -7.85005 | -43.8491 | 2025-09-16 04:29:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17637afd-9536-340f-bd73-8e1e54242dde | -8.59068 | -46.34283 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62da0e19-8623-397c-ac2d-797ce41f1903 | -8.98324 | -46.2501 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ae4c428-0e9e-398c-9c15-302b3063434a | -8.66667 | -46.37261 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5757d43f-d42d-35a0-b03b-03992e383115 | -7.68066 | -46.29917 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e28fd7bf-24dc-364a-9289-a982e21e406b | -8.93366 | -45.79597 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01e867c5-57fa-311f-bc88-f1b17058a15d | -12.44277 | -44.74885 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6732289-d8d1-3aae-9e0e-3c51ab885d0a | -12.86234 | -47.14774 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2eb714d5-9a81-3842-891c-b44709233d41 | -11.10877 | -45.34603 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ad35d43-3012-3813-92f3-a03ba4a06a9d | -9.09387 | -44.84174 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4895c042-2030-34d4-9b12-f62a627f58c9 | -11.45947 | -43.56408 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8287807c-74e9-3220-95fc-247ef7ae70f8 | -10.40611 | -50.63806 | 2025-09-16 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb162212-492c-3c42-985a-be451282f73b | -9.05698 | -44.84033 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7564e245-8b71-38fd-91ba-f386765c6bff | -10.05277 | -44.34521 | 2025-09-16 04:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11784f20-182f-30dd-a9b7-0c950d69f4f4 | -8.12119 | -48.25916 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf6f135f-90b3-37ed-ab1b-7eab2ae937e6 | -9.09607 | -46.93163 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78718320-5137-3e5f-8d33-c3fcfe0b5dc8 | -12.29296 | -46.4029 | 2025-09-16 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 336efc49-fd72-3fda-8cec-04e67c2aa069 | -9.7042 | -47.40675 | 2025-09-16 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 306dfd96-f0fc-3b15-9dfd-b7a91f0a89f2 | -7.7129 | -45.30028 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 730add91-2fea-32a3-8ea3-529ce353edaf | -7.71909 | -45.30492 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94bb2576-ae62-39fe-b76c-9711d79104de | -10.79713 | -50.68632 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 430f60cd-ccf0-3f30-881d-a6829e123bca | -12.12657 | -44.81254 | 2025-09-16 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da9ed135-dfd8-3254-9e51-329815de8982 | -8.66776 | -46.36561 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8ddeea2b-294b-3c13-801d-c76812e86d1d | -11.23504 | -49.40641 | 2025-09-16 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9125a1f9-f6d2-3612-99e0-7b91ecd2a9c2 | -12.62867 | -45.77459 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d971e0f9-c665-3767-8973-b3671421beeb | -7.67569 | -46.30909 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5628fa9d-9b28-3eb6-be3d-377459207abf | -12.54228 | -45.86643 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1505ee73-b2b3-39fb-ae4d-34f901d3445a | -13.19305 | -47.30693 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c071e75a-93a3-33a9-a6eb-91444c5470d1 | -13.21359 | -47.28487 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bb7fb70-0c93-3794-a592-52ce732bfca2 | -11.47563 | -43.58531 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a9b961e7-74e0-30b9-9a23-09af12d8fb18 | -8.09054 | -50.151 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d72c90b0-53da-3da5-8739-9a420e803c12 | -12.62527 | -45.75937 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d27d9d9-9e93-3014-9a45-81c5b8902942 | -8.32862 | -44.72475 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d0a14d0-0e1b-3ff7-8c0a-eedc791ba94f | -12.93245 | -47.97066 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6efcc744-eb6f-3533-9128-fa2d6d04e6f4 | -8.6135 | -46.39307 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2f6be09d-88e4-3788-b95c-9cc4250a4acb | -10.47436 | -45.16255 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dc6a1d7-4ba1-304a-89ec-9d4adefe2c4a | -8.97646 | -46.25634 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ecbc4d49-8611-3dc5-8caa-343e63c9a2f9 | -6.55927 | -54.98615 | 2025-09-16 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10e31f21-6320-3172-a059-f731b0571543 | -12.67308 | -47.73214 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83f5ae0f-ebbd-3c1b-9972-5c5d0031b13a | -7.835 | -46.11217 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32c6539b-26cb-3931-9c4a-01daa5fd7f58 | -12.95021 | -47.96631 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b36341f1-d5f0-31ed-a45f-cf92b5b7b966 | -8.7651 | -46.09308 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aec49f8b-ea22-3891-b069-3527f3dc9736 | -11.64322 | -46.59632 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7c8b989-681a-322a-a460-e56d10799c7a | -8.8744 | -46.175 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README53.md)
