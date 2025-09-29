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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63c28ae4-ccb3-39d1-95d1-7793236e6d28 | -8.83465 | -46.19482 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d3ece2c-9e12-3afa-8826-2a774bd06251 | -4.58373 | -50.16497 | 2025-09-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fcbcd2a-60de-3ab4-9baf-78a704d11fc6 | -9.04893 | -46.70302 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d5b28db3-c826-3d26-907d-7a100a034e88 | -6.91385 | -44.00318 | 2025-09-29 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddca6551-8d4a-3d37-8fd0-24007ddf7278 | -7.73598 | -47.00013 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 667602ea-a2b1-3684-b829-934b0ab805fd | -6.74987 | -44.74899 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87520962-ea70-39bd-8e59-b9b93d3aca78 | -10.31987 | -48.20594 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d967b32-9371-3223-bc9e-533c20fc7b2b | -8.86531 | -46.62181 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a87f8bd8-2341-3308-9cd2-23d1f148c9a7 | -9.31404 | -45.71781 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c9399b9-101f-3ef5-8f42-2dddbc85f4e1 | -9.4598 | -45.50012 | 2025-09-29 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 525afda7-c980-324b-b213-96933f434384 | -9.27525 | -45.73728 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10369896-6625-393a-bca4-24466013e100 | -5.38338 | -42.30552 | 2025-09-29 04:57:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0ed921ac-6448-371b-b3bb-a06e07f1ca78 | -7.22151 | -44.76208 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5284024a-55f8-3a79-b2b5-5e4b32606b31 | -7.13787 | -45.49782 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e09f3223-37ae-37d4-a902-3536057ad845 | -3.34904 | -49.22574 | 2025-09-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5a01769-28f0-3718-8103-a5df68df7245 | -7.76874 | -45.74397 | 2025-09-29 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2878d6fc-7939-3178-82a2-e8bb009ade52 | -6.57448 | -43.40469 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 00a4aed1-700f-376c-b2ba-663cea9bc4b5 | -9.77278 | -46.18146 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89b34b1c-e4cc-334d-b112-ba1e3f8656ea | -6.48857 | -44.26374 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e0ebc0d-ac63-3ed0-aa3a-c1626cd843bc | -4.30833 | -48.08876 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6f23a13-fd65-329c-9905-65bb479e4ce2 | -7.46717 | -46.29732 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0426f188-7b4f-33fd-a0ca-8aefd8696cad | -6.89366 | -44.52842 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea759527-245f-3603-8290-050a4e453657 | -9.41453 | -54.692 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57fb5ed0-5644-34fb-8781-ac360c3f62f2 | -11.42713 | -44.91288 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf879674-7a66-3cc8-b6ee-84022b622586 | -8.14352 | -46.39944 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 10ed798f-fe9b-34ab-9749-dad8ef505959 | -9.40522 | -54.70832 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 945e7429-9546-3b15-bb7c-7abded814ae1 | -9.39917 | -54.70382 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3101dd5-57fa-3202-a05a-c5c6a51d5226 | -5.91191 | -45.85562 | 2025-09-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04f44485-44f4-3e12-a19f-829b4d134a40 | -8.30513 | -45.50033 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a5a1644b-aae5-3834-b610-d031aff5553c | -6.25892 | -43.63375 | 2025-09-29 04:57:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a538d010-f1d3-37ec-8f23-df13079024a7 | -10.81914 | -47.94213 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c5d037e4-2926-3142-8c5e-619ebf9931b0 | -10.82249 | -47.93554 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 152bc8a5-9c78-3dc6-a3df-0bd82feb9afa | -9.7677 | -47.761 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72264d52-32f9-3031-a926-915e655d0ddd | -6.28242 | -42.49097 | 2025-09-29 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eceb1f88-ded0-30c9-959e-e1d73a12679f | -9.77403 | -46.18071 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf603538-9096-36da-8040-57b7214558ba | -5.84713 | -45.95206 | 2025-09-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5fab9c2-8d00-3371-bc79-cfd775dc1bae | -7.8128 | -46.90403 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53ef6b59-05db-39b9-ae5c-e0077c0c5c6d | -7.73671 | -44.94825 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e20d743-d141-3d5c-ac0d-d419936d6778 | -8.30377 | -45.51056 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 7b23bbaf-113e-3b39-ba30-50ee50854aeb | -10.76168 | -45.37849 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3672ade8-f24b-3a29-b156-73fd2e9785b9 | -10.62608 | -48.53406 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5710a7e8-83bc-3b34-a3fa-e51593a27fd8 | -10.18311 | -44.88406 | 2025-09-29 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02cc203f-aecf-302b-abe5-8c849fc15796 | -4.31372 | -48.08159 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb5a97a3-8517-378b-b16c-d22a13d055bb | -11.40495 | -44.90606 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8f17358e-ed3c-31a4-a1df-38fabe39127f | -8.71815 | -50.04844 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 595b0a05-7aa6-37ce-8210-7be23098f200 | -8.2636 | -45.48487 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce435abc-a378-34c2-8ee5-63889cdb13f7 | -3.66449 | -53.68572 | 2025-09-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64dc68dd-966d-3d35-85ce-af0b3f9ff225 | -9.39749 | -54.69287 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cdf2a8c-a8f2-3770-9655-29c0d379d4cd | -10.03829 | -52.10416 | 2025-09-29 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 939e356e-2ea0-3430-bea4-db257fa32edf | -11.43433 | -44.9565 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af1b071e-c265-35db-af12-321f7ff4e59e | -14.68434 | -48.16439 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a279fd9a-1e42-39b4-9ed0-93a5a07c11eb | -12.69655 | -46.89383 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a1c31f9-eb75-32ed-a856-8ef808d4b6af | -12.85184 | -46.97004 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f570731a-4f2a-3b84-a930-e291d5668fcd | -11.16543 | -49.93798 | 2025-09-29 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b3b692b-d421-39a2-881f-61d7d6ed7376 | -15.2556 | -48.76321 | 2025-09-29 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 022b9460-82a7-3b0c-b259-8fb9921df413 | -11.45583 | -51.49648 | 2025-09-29 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0e0c3c5-3f08-3a98-a35e-5c58a916a856 | -15.91146 | -46.1983 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c828daf0-4e9b-32ab-8d1a-b1b9e4c1db75 | -13.3618 | -47.29842 | 2025-09-29 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf37c368-2a29-38b3-909e-43e3b4624ce2 | -12.94422 | -45.17734 | 2025-09-29 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12950781-64f5-3e69-b305-be7ae0114b87 | -12.47597 | -54.42258 | 2025-09-29 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 266d4d98-a580-30ce-8248-0a4e998b1fdf | -13.65748 | -48.08127 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f8cee65-2e31-3d3b-b364-d44a1b2c4a29 | -12.6543 | -46.92168 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e0a9704f-35ad-3021-a12c-7a21a01cdfb6 | -12.70037 | -46.90566 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c82da82-cda0-3e16-9745-44c8e178fd8f | -10.8891 | -53.74599 | 2025-09-29 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 832aa78e-dada-36f7-84d2-d97fee54ae7d | -11.83422 | -51.80378 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c60a337c-61d3-3b29-baf1-115065a17cdd | -12.76392 | -46.85962 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd84f9b4-3e1a-3048-9cc6-e3d18cefdff1 | -11.91691 | -48.03742 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9144722f-cd73-37db-971a-d3b05258197d | -14.52546 | -48.39201 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae1645e1-1485-3dc5-ac9f-8b810dc4b066 | -13.62633 | -47.33663 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c444c35-2efb-31c9-a539-8a7e38169647 | -13.75142 | -47.90614 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1295f86e-dc66-3f42-ba52-82c488ad408b | -13.17943 | -47.44971 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0b6b0ac-d7ae-307a-87cb-e75a8de95387 | -15.07883 | -48.33374 | 2025-09-29 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddb6658b-6363-3aed-ba13-688ccde71b8f | -14.53373 | -48.4036 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 567f5ee5-fc71-356b-82be-a327d5025f42 | -13.82335 | -47.47802 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b82163a9-c1ed-3821-b552-a011c8022d6e | -13.26573 | -48.44605 | 2025-09-29 04:59:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 395fe630-5918-3469-9dcd-7ced01babc00 | -16.20976 | -52.82512 | 2025-09-29 04:59:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45ee6b5c-157f-3391-8f13-2daeb2afdf7b | -16.50668 | -46.03603 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 928254dc-9497-3ea4-89e7-2be3c8a8f74a | -11.9365 | -48.07225 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 206429b1-f0ee-315e-ba9c-afbde4bbffd0 | -15.26029 | -48.76411 | 2025-09-29 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 89fe0e75-38d8-3c35-b1cd-b75ab859cdb4 | -15.94651 | -57.48796 | 2025-09-29 04:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e90be94-af53-3f9f-89bf-c801d20bb41a | -13.17979 | -47.44676 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e7520b9-dc30-353c-9560-ad5e3b808401 | -11.62098 | -52.85638 | 2025-09-29 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c319ff0-f1be-32c5-aafd-fa1b949aa3a5 | -15.54333 | -47.87696 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb7eddef-63d3-37fd-bde9-8eebb8f7bb79 | -13.57669 | -47.29154 | 2025-09-29 04:59:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| aa18a6fb-f30f-34f4-9f46-7cac37046e16 | -12.98063 | -45.22129 | 2025-09-29 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 146c7b6c-43fb-3f1b-b656-cf792f14715c | -15.17072 | -46.41665 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a14c972-facb-3456-9581-07cb1b241c11 | -15.2744 | -47.86775 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cf43735-7fbc-343c-a182-e9a496bc38a5 | -11.41533 | -55.06178 | 2025-09-29 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f99fa34-036c-3c96-92a3-c00a63e3e9ab | -12.97068 | -46.24445 | 2025-09-29 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e015bbd7-7914-3500-9a0d-c69680c0a8cd | -15.28606 | -49.5063 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f0410f0-a55b-3604-b02a-6be97c72178c | -13.57886 | -48.08694 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6d24d432-781f-36fe-a66a-eb9340c044c7 | -15.28447 | -49.51905 | 2025-09-29 04:59:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a04b6233-12a5-326d-b0c0-ce62768010f7 | -11.62157 | -52.85238 | 2025-09-29 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e5db792-4a0b-3791-bc23-53e865a6a743 | -16.52495 | -46.945 | 2025-09-29 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b3ab8c9-c6ac-36de-8190-60562c2f825f | -13.60853 | -48.03912 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 00769607-c650-3f3d-8b2f-a19cd4e8362c | -14.55346 | -48.40185 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2eb9a2d7-32ad-30a8-a3fd-b398ebf5f961 | -13.22986 | -50.95853 | 2025-09-29 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7aa1e4f7-6d78-3243-96d6-2968cc9e5817 | -12.21915 | -54.2976 | 2025-09-29 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25d41d1c-a5eb-3ac4-b8a2-57ddf619f299 | -15.33542 | -47.91067 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0227b81a-f012-3d5e-8c0c-6a75beed00ba | -14.83616 | -45.56593 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README65.md)
