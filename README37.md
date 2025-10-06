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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62c269a2-7b32-3a6e-ada8-2c0574d788bd | -10.26061 | -44.93753 | 2025-10-06 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff31893d-f5ab-372b-8ce0-b29bfe678983 | -14.46498 | -46.3341 | 2025-10-06 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a263a51d-d627-3954-b44b-aaa97d9e9fcc | -13.10509 | -48.00014 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f82263e-9364-30cd-a8bd-832abaa2cb9d | -11.70795 | -45.40949 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1245e771-2f07-3f03-97cd-2094f4ea6b91 | -14.74312 | -54.66992 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cca6595-23b2-377b-81cb-c6d71c5e6937 | -13.27505 | -47.84744 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2de4d0e-f40d-34ac-982b-c7f0ba660dc2 | -13.32561 | -47.17149 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23dc3f7a-8247-31f4-8cd1-f795f8a5e1d4 | -11.4926 | -45.04308 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07ef9eba-c328-3f53-b4ec-4be60f682cff | -15.2627 | -47.14805 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11f6b1ba-dc8f-3313-be24-cc30957cd517 | -11.94273 | -46.43385 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1feb0cda-ca08-38c3-94f4-7cd6f2056d05 | -14.54833 | -46.95272 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd6cc680-2ca4-39f4-ad1d-e4e25c4fc3b9 | -12.25204 | -49.20446 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42ff017f-1634-329b-95bc-e84d338b19f8 | -12.48795 | -45.56032 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e7f96956-7e2d-3337-bbf4-2043e399040c | -10.62268 | -46.35139 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04c6916b-d317-3601-9443-294ac3a1713f | -17.08047 | -43.38744 | 2025-10-06 04:27:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d21e066-2470-38c4-9e62-999c3c66ca35 | -11.91479 | -46.23407 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8b4e55e9-a8ee-39e5-942b-629b83d4a50f | -8.6259 | -54.97173 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fb31a86b-bf9e-35bd-8f5c-8d1fd0577e6a | -15.28728 | -46.31836 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f44fe384-5acd-3ac0-8884-ff5b147b025f | -13.2624 | -47.84177 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9570174e-2760-3508-b3ed-81ec0f68ce13 | -14.61205 | -52.50115 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 394c6ca7-912c-3682-81cd-8b324ee4ab99 | -13.63452 | -48.71908 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f294f8a2-d1ee-3b59-b997-346db39b4f9d | -13.4983 | -47.24297 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2b4a4e1-8b6d-368e-842f-53f19a3d7dc4 | -14.2664 | -45.85083 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 786c1278-6e92-34d2-8e89-aa47b174bfbc | -14.84677 | -51.47781 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35a5f68f-d698-39c1-a3ce-672503fd552f | -11.71252 | -45.4023 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e596cebc-54b4-304c-b150-9d0f0e040a2b | -10.28009 | -44.35766 | 2025-10-06 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afb89133-296b-33a0-9a21-5d2b916112ec | -10.32257 | -54.1562 | 2025-10-06 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c7f4123-5b65-3521-b5ed-dc0379fe22bb | -10.41579 | -50.33533 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f922cece-b73a-38aa-8b28-4f7c5cd4535a | -13.72051 | -48.09058 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d7154cd-2312-34b0-a0cc-1fedbb25bc76 | -15.35175 | -47.99212 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2adbf74b-29e1-3ec8-be6b-c3d014fdc36d | -12.98468 | -51.06794 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0090d7ed-6543-39d3-be46-349fbd20d49e | -8.61011 | -54.97451 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cd76f56a-96c8-3c6e-9c3c-8dfe212b00e3 | -10.3615 | -48.15046 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a1ea43a-748d-3245-9569-b0edac7d5b7c | -14.91338 | -46.85282 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0fe9cac-51bb-3574-9c27-bfc6ee817f68 | -15.22989 | -49.28158 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc71190e-bc77-3bd9-965b-8281a11df7ba | -15.28674 | -46.32206 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 394de4b4-d180-3f74-87bc-979694342be4 | -9.62859 | -50.54691 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d44b2b5a-ce86-3d0a-be50-2ea553c80d25 | -13.26196 | -48.49314 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc971ae3-0876-3847-b1d6-b23bfa216ab7 | -14.5534 | -46.65345 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ecc0e38-c283-3f70-976f-141293bb7aae | -13.26478 | -48.47541 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f1f7b3b-4dc6-32e9-af49-958aa218f524 | -15.57778 | -52.43665 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2a7f280b-f98d-3d69-a84a-a3cb02c4de45 | -13.14942 | -50.87168 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe0d7f8f-b9d1-39f5-a7f4-78c59fb05de0 | -12.15119 | -46.6053 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01730ae8-d3d8-3ad9-9158-dbe49a0172ca | -9.68314 | -49.95727 | 2025-10-06 04:27:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f29da4d5-4e83-3256-8c26-04bbf9e00c1c | -9.53783 | -51.70196 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0675f3d-1510-3f5e-8a20-94cb1084598e | -14.92446 | -46.82489 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fbc74c60-2a1f-3f87-ad26-74f4b756482e | -9.67461 | -48.40109 | 2025-10-06 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 764f5a52-fea5-3408-8ee3-e52e85601f40 | -13.34155 | -47.59877 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c23931b-a59f-3321-a61f-00ff527278d6 | -13.68798 | -47.3135 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30dd0d5f-64cb-3198-8ce9-e468b9d7cd5b | -16.06171 | -47.77401 | 2025-10-06 04:27:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 235cd4d6-bf6e-3f23-90e5-0a679f2fba1a | -8.62975 | -54.62458 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a89c7215-62cd-3ba4-a4b4-04e8e566ed94 | -13.09967 | -47.86223 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e027ff5-7f44-3af0-a7e4-8f649a90e25d | -13.36155 | -47.20277 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c50d36d5-4d35-3beb-af1d-d3d7c800eb4a | -10.47454 | -50.44836 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07bed107-3885-3892-8b8e-e0a1ce2a306b | -12.57181 | -48.14339 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b24a31cf-e710-37f0-b450-7e525d43b22c | -11.579 | -46.7666 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f890159c-8b2f-322a-a92f-ac3a5e694258 | -14.67124 | -48.27661 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ff6c5f9-3c8f-3756-b55c-ce743cca5973 | -11.51855 | -47.67971 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 191e05ed-b03f-36d6-831c-b4ac15731f82 | -9.37408 | -45.91272 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9ae3588-1125-31c9-8724-66046efe5f57 | -15.16406 | -45.74322 | 2025-10-06 04:27:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b593f39a-b57c-38ac-86be-f86e01b22951 | -13.22889 | -47.81833 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d95186f2-9ff5-35a5-9e24-c87a8549083e | -12.89697 | -54.75134 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 95484431-23b4-3b71-9757-40a20c054544 | -14.84262 | -54.79188 | 2025-10-06 04:27:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47cd6dec-32f2-325e-8d07-d7ea425cdf89 | -13.09912 | -47.86575 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01c27d44-4785-3f52-aeb8-7ba6191ce102 | -11.8372 | -44.91555 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95b75f24-e35b-3c21-a43e-5130b315ad57 | -11.00887 | -50.67573 | 2025-10-06 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c9dc03a-0bb5-39cc-bded-45dc2a28a633 | -11.80928 | -45.10505 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05bc5186-92bf-3514-871d-4eb15a8cf618 | -11.85875 | -44.93948 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b3f989b-30bd-37f4-9afc-0e257d719421 | -13.25648 | -48.48491 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff27ac66-be86-371a-8c8d-f26c5efdcf39 | -12.48447 | -45.53629 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf75f047-c53e-3894-86eb-4097d166c5fc | -13.49776 | -47.24661 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63bcd020-b4a2-355c-94f6-ef245264e73e | -10.02242 | -48.2919 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7966dab-c61a-3a09-ad57-bb6f79ed9444 | -13.23988 | -47.8129 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a358a2b2-04f0-33db-a14e-cc6c222a7afe | -16.09999 | -43.62663 | 2025-10-06 04:27:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60ecc5bb-8bd3-38bd-85a3-5177a9242025 | -14.93213 | -47.13238 | 2025-10-06 04:27:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96bca6d2-7f2d-3dad-b967-e60252ff777e | -13.24607 | -48.46501 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f60913b-2f7d-3be5-88c3-750e4105d6c5 | -12.15174 | -46.60172 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0274f35d-eba1-360e-93db-96ed4c8e5da6 | -15.35835 | -47.99321 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71b3f145-a669-31e0-9540-551740d26ec5 | -12.99289 | -51.05322 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e37bda0-7c9a-3216-b7df-941f79f9a7b5 | -13.68742 | -47.31714 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1b0fe59-3bff-34c1-96e6-4539b456df6c | -15.36826 | -47.99486 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5570567-c1a8-3d5a-a180-b9aca1b156f6 | -14.32463 | -52.97886 | 2025-10-06 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 377a01f7-ea9e-312f-af83-fdca250a8596 | -15.87649 | -46.26421 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a006e99d-2ee4-3d67-8a21-d51b6857d308 | -12.24531 | -49.20332 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 860d8867-6c52-37f0-919f-4931b52e79ee | -10.73553 | -47.8752 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa1991d9-cf4f-3ec3-ade5-09214b4654be | -13.24757 | -47.80695 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6da4bb7-fc0a-3e74-9dae-6fcca0b7caac | -15.22081 | -56.82618 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1677898c-6fbc-3c12-aed7-67f0dfa35bb2 | -14.34086 | -47.71068 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4992c5f-450f-3066-afcf-de4599af93bd | -11.05912 | -47.76648 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e76c136a-3daa-367c-b495-e618c0621af4 | -14.70522 | -48.34029 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82f2e070-d03b-30f0-bbf1-dcc8f6441c50 | -11.47691 | -45.05307 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68e66d7a-fba7-3eca-919c-fe2ba16901ef | -13.0788 | -47.88766 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a67b8887-5ae0-3c69-8d5b-3934350ffc0c | -13.08266 | -47.81982 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d26c29ed-d0f9-34b8-87f8-e4691aca4909 | -9.6841 | -48.40625 | 2025-10-06 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15565085-0668-30f0-aeee-676cc9027326 | -16.02661 | -51.05499 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 900940b5-c10b-3d3e-a037-971a60e3ac9d | -14.67161 | -48.38198 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 805f5685-f431-3a5d-a755-1c8bd437387d | -14.92623 | -47.21694 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3a7e48a-0c06-3e20-8251-6e9b81e959cd | -10.80601 | -48.81933 | 2025-10-06 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c272c434-3309-3fdc-8e8d-14583615a7ef | -14.91611 | -46.83466 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 222f8bfe-5c90-3a38-bdb7-b5ac4ffd594d | -14.74704 | -54.66656 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README38.md)
