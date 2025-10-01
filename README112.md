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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b5c5f3d-6a14-3c9e-bbc5-72870d15e69d | -12.24353 | -47.81916 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 89d94f08-200c-3e5f-9939-fafda9992ff0 | -13.24555 | -47.311 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08461876-42dc-36b5-818f-d52cc159f041 | -9.57088 | -50.95051 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83745f85-1a11-33c9-863e-f5a23308f95d | -14.14368 | -49.19616 | 2025-10-01 04:51:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b381cb00-f44c-3c3f-a310-7d15970065f7 | -9.40254 | -54.71303 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afdd0465-562f-3e47-8b5a-a5567b102b6e | -11.94209 | -43.91499 | 2025-10-01 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cbfc08c-7334-34a3-8a04-107ca72a3c54 | -13.75924 | -47.92916 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67c27e9b-cd92-392c-abf4-3707a5b4d7be | -16.39779 | -47.04315 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1978eefc-0750-3121-b8e9-f4780f93ce95 | -15.312 | -46.41429 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bff99580-a0ce-3cb3-bc8b-73f88a50a473 | -13.33562 | -48.14713 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ec011f0-e49f-32ed-af3c-1a3b3a4f39fb | -12.77715 | -46.88161 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b89e0f8-112b-3ac9-bdd4-cc83c79e94ee | -11.15661 | -54.11852 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aeae86d6-dff7-3c8c-ae14-745963658818 | -11.43664 | -55.05119 | 2025-10-01 04:51:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04350b62-e382-3e5e-9ab9-6e9ecf9aba4c | -16.0232 | -50.90545 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5745093e-0422-3b7c-bebd-ae7cc495158f | -9.80117 | -45.94184 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 292831b6-a93e-30b8-ab09-ace9e420f5df | -11.38073 | -45.06667 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7f9f863-25e8-37f8-b6f7-e8e7e4a5f061 | -15.31929 | -46.40828 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cbbcfa2-e576-3225-8198-035d189edc92 | -10.73809 | -45.38146 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83763cdb-d2d6-389b-85a9-2ade44781a82 | -14.59819 | -48.22438 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 543a86d2-9f83-3404-8fb2-04bd11f292e8 | -11.14799 | -54.31252 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9e512d48-922d-352c-baea-c1162d585554 | -15.93392 | -43.30975 | 2025-10-01 04:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a68efcd-e0dc-394c-a796-264137bfc5c1 | -10.80369 | -45.35041 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b0069a8-89d0-3546-83b2-d89ac9cf3df7 | -13.63272 | -47.6455 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cb849d5-d30d-3ddb-904f-a64b26226df7 | -14.90294 | -51.6723 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fae93633-a99a-3730-b313-1b64216009bc | -15.2993 | -46.19083 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3eab5fc1-7c70-3c49-951f-ea698b35e6bb | -10.09129 | -50.19919 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| baf85667-2621-3059-a0bf-5b21b89c134f | -14.35231 | -45.93355 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 0c7f6925-1f60-35fc-9436-7a7c3f30f618 | -14.90971 | -51.67339 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4658387-d3ce-3c96-b252-52cea29baa8c | -10.62562 | -51.59459 | 2025-10-01 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50665047-eeb7-3520-80cb-b21c48d873f7 | -13.75782 | -47.93954 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 240b4f6c-c7a3-3a60-8aa9-f48c7d76fb07 | -15.94174 | -48.11901 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a5f2fbb-e657-395e-b8dc-365fd89b13df | -14.21889 | -46.10383 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22ab0aef-0d61-3bfd-b13a-1e90e24cbe5c | -13.71235 | -48.63487 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4222169c-1330-3f1b-bba2-47e6ade5ebd2 | -13.30642 | -50.66666 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25af5261-f519-3cc8-84a3-c0bb7cb4d252 | -10.91076 | -46.5697 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 59198497-0f41-355f-9449-b1306300e90e | -15.23895 | -48.74858 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ca168562-fa89-3945-85b4-3aa4625ec4d6 | -12.66521 | -46.88184 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6c11c46-deb8-3efe-9059-491345904938 | -10.81606 | -45.36123 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3d509439-d766-3497-a260-ded3abc241c4 | -14.92618 | -47.81818 | 2025-10-01 04:51:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d732744-5ffc-3dc4-ac32-431b1b8494f3 | -10.64731 | -48.53429 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec663507-9f48-32ef-8c93-ba54444a4d76 | -14.10032 | -49.75422 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdaec40b-f93b-385b-8ad2-0422b4188ddf | -12.87413 | -44.60229 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c34068ba-f335-3e8b-bdd6-64ac0c26ac45 | -13.64925 | -47.3124 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff110d56-bfaa-3af6-bfe6-20ba90e5a7f2 | -16.00222 | -50.87733 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97e0bcfe-94ca-3ecf-9cc9-cacd23412289 | -14.658 | -48.14294 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37d77730-a122-30cf-928d-0b8d2cf0ef89 | -12.82416 | -47.00783 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9aadde6-a6bb-3caa-b12d-10718079848c | -10.90984 | -46.51237 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d314d6f-44f7-39a6-a333-e8241bcc8fcc | -12.84451 | -46.95218 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29de1796-fe75-343d-b479-d4a1995513cf | -11.83185 | -44.95934 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e25851a8-acef-3126-9572-8cf67326abc1 | -14.86786 | -49.71529 | 2025-10-01 04:51:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc98e344-58ec-3893-b4e4-141228d7fae6 | -16.01969 | -50.90496 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a21b633-eb59-37a0-bea3-f5e7051a4233 | -12.83671 | -47.04036 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce3e1207-67fc-3408-9913-549688490401 | -14.73217 | -46.82772 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d151651e-0d95-36f3-86b4-bafd130659a5 | -13.72001 | -48.63573 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04862bba-4adf-354c-9ea3-c0495617ef19 | -11.68493 | -44.3003 | 2025-10-01 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4266fae-52a7-3e22-b008-a1eb1b1d12a9 | -16.12991 | -49.14644 | 2025-10-01 04:51:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c467a6db-2ac7-336a-93b4-9f703c494e9d | -13.78761 | -47.98808 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e513dca-cb23-3f52-89fa-9c6b43d1db9f | -15.2721 | -49.28983 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4716892b-ed0b-319b-aca8-377779108b82 | -11.83739 | -44.98999 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9368f8aa-e967-33f3-a9cd-c174ae0bccdf | -10.90399 | -46.52342 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 594c6548-0f37-344e-922e-8ab7f287739e | -11.64789 | -47.50248 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d05b5d82-762d-36eb-90e5-608898b7e615 | -12.76512 | -46.90679 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77b33bb9-1624-34ff-9eee-626d8ea99897 | -9.94484 | -43.59399 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| afde6022-2be4-37c0-8936-2a29bdcabd58 | -13.73173 | -48.82172 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4de0e69-de5a-3b60-bfc9-acd065f3198e | -13.21014 | -47.3248 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eff82671-3432-3bd8-8ce0-945f57b9c24a | -13.58512 | -48.04393 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37103467-6fa7-38a6-b8ed-e3b1f67d5a6c | -13.73099 | -48.68795 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c707e69a-ab3d-3351-85fd-57d4b44b6f03 | -14.90575 | -51.67655 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32aef259-ceba-31e2-bdab-29024885c970 | -11.6831 | -46.84721 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfa7e602-6f7a-3a0a-bc3c-9788a0aa928e | -15.41488 | -47.05774 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4bafe6f5-695a-3823-9b07-a2f51189076f | -12.87531 | -46.94545 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbf106f1-4b45-3f94-ac0d-fa1d90fcc2ad | -12.77616 | -46.88879 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 972a015d-f03c-36f0-9339-2b80c3fd3c69 | -11.64858 | -47.49771 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83e75a4c-2d9c-3ca1-b0eb-f1555c681625 | -11.05316 | -47.8339 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4edf7b33-dc9b-3712-9a1a-4015ca3ba9b5 | -11.74056 | -46.8694 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a95952b-6485-3941-ac9c-d1af036738ce | -11.6422 | -47.49789 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f34caff5-acd6-37dd-b637-e15e975cc121 | -15.48868 | -45.91282 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 82ab43b4-31dc-3b20-8d4c-9ea50c071c11 | -12.21753 | -47.80481 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86c7d6ef-d8ca-30a4-9411-cc2afaac73cf | -10.43881 | -50.86549 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3fdf7bf3-27ae-313a-9c33-b8370eff60a8 | -10.43544 | -50.86495 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2daa7df4-7aaa-3af3-b300-2d80ac0aa18a | -15.28628 | -47.83662 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a39ac8f6-ad18-381d-b83c-3234ec9854db | -12.17766 | -51.41683 | 2025-10-01 04:51:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02b1b254-5205-3618-a285-3ff52be7913a | -11.52483 | -43.55296 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d9ff215-587b-31e1-9734-a639789eaebc | -12.77093 | -46.86459 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 246a6905-849b-3bc6-b2e3-08e3567b6268 | -13.74237 | -48.68982 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4d687e1-f2d7-355d-92bf-b13606b06438 | -14.67135 | -48.1345 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7dcfbb3e-424c-3677-b36c-9e7142105a3f | -16.08162 | -51.04707 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2b99b2d-d34b-3d1a-a4df-9e827d2ac6d4 | -14.96719 | -46.87008 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c550d60-e7ca-30ec-8754-d009c635c9fc | -14.59426 | -48.22364 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dfe111ac-78a9-380e-a7a9-89676a33bcc0 | -13.9761 | -44.91768 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6440615a-8a77-3cb7-abf8-a6e19c3040c3 | -10.03907 | -52.1023 | 2025-10-01 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a6249b00-67ce-34ff-9862-e071aae7f824 | -13.70275 | -48.64765 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78920f20-57aa-3818-911e-99f063cb799b | -16.19671 | -50.00529 | 2025-10-01 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1316d09-e699-3d13-bb6b-44c66fef9d78 | -15.93767 | -48.11858 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f23d29ba-010d-3ea3-971f-3bf52af9bd00 | -16.08367 | -51.02826 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c99a9c2c-8b78-31d0-a761-a303c60e44eb | -13.09442 | -47.04372 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ecf8b54-77d8-3958-a14f-47a05e0e8a37 | -11.20409 | -47.20026 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dfba27e-af72-390b-b848-8b2778e7eeab | -13.34668 | -47.8656 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 273ec43a-f60b-3391-a691-7d87358d3183 | -15.28268 | -47.83237 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e63634b4-cbe7-3f35-86e0-bc6a8f24cd5b | -16.29335 | -48.97996 | 2025-10-01 04:51:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README113.md)
