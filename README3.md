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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 049c46bf-f713-33dd-93e6-e06673ed7709 | -8.056 | -46.314701 | 2025-08-09 00:44:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1f44ac3-88c2-3237-a39a-d9e628b3d5af | -14.3489 | -47.093201 | 2025-08-09 00:44:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 89e6d625-89f5-3038-8d54-bcd30d1e7642 | -4.8024 | -42.841999 | 2025-08-09 00:44:00 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 42a54592-dee2-3e3f-b6b3-6169efb71f6e | -11.9347 | -44.544201 | 2025-08-09 00:44:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c322a05-364a-318c-b54a-c8f90622ad95 | -6.0619 | -43.7505 | 2025-08-09 00:44:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 119d3029-b56f-3a0b-b7d8-1c36272947f1 | -6.5779 | -44.5681 | 2025-08-09 00:44:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8c7e66c-aa9b-3acd-a6af-9d45ee12c491 | -7.8963 | -45.551102 | 2025-08-09 00:44:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7173cf3c-4116-3ccf-a32d-607d6d53b09d | -4.2907 | -48.051998 | 2025-08-09 00:44:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca25e10b-2133-32c1-a45e-b880c515ba5a | -3.4275 | -49.050098 | 2025-08-09 00:44:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a3b4a5d-cd0b-3df2-9bd7-403a7c5a65c4 | -12.5564 | -47.105999 | 2025-08-09 00:44:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a0a48fe-b65e-3256-bc86-e073a0e94051 | -12.5679 | -47.110699 | 2025-08-09 00:44:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f286500-a78c-3aef-8e37-b93adb2b885d | -11.7576 | -47.492401 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b64ed36-ac45-3e0b-b5db-cc28a5e7d4b6 | -13.6236 | -49.0107 | 2025-08-09 00:44:00 | METOP-C | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 077a608a-f66e-3ecf-be2d-15f19ac8e821 | -7.0447 | -59.142799 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dfa0cc92-4964-3fad-8456-93332068efbf | -8.9266 | -60.720798 | 2025-08-09 00:44:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89d91eb5-78a5-330e-a179-6627d61d409c | -14.3603 | -47.098 | 2025-08-09 00:44:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7117193e-3976-3b9a-a4f9-0ca38830971b | -17.528299 | -50.293701 | 2025-08-09 00:44:00 | METOP-C | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 15a25ddf-d4ee-37de-a358-52af0660b07b | -4.4791 | -48.108002 | 2025-08-09 00:44:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3db18761-b708-3a3d-a55c-8f9d242d194f | -7.2621 | -44.666401 | 2025-08-09 00:44:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2196d0c-001a-3122-80ce-617803339fde | -10.0054 | -48.131302 | 2025-08-09 00:44:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8bb01d88-9850-36d3-a6e9-a334c27cf23e | -11.111 | -50.491699 | 2025-08-09 00:44:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8467d981-5630-3b79-b1d3-aee8d493bf49 | -12.5613 | -47.127102 | 2025-08-09 00:44:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb7c3018-8c76-3a5e-9fa7-d98c28fd502e | -12.5548 | -47.0989 | 2025-08-09 00:44:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7fa4d10-519b-356c-aa64-9dbb537c44ba | -17.5203 | -50.304798 | 2025-08-09 00:44:00 | METOP-C | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 392a7f27-1a31-388a-ba74-6ea16c2d912b | -4.8057 | -42.855801 | 2025-08-09 00:44:00 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fcfe1abf-2067-3eff-bc7a-5c43f8f2427a | -9.0635 | -45.073101 | 2025-08-09 00:44:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3cbccba3-f14a-35fd-9ac2-38e743e4085b | -6.1692 | -46.150902 | 2025-08-09 00:44:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0d3ba20-3333-3521-bef7-5dc7186e72b0 | -6.9422 | -46.058102 | 2025-08-09 00:44:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c11ac891-ac0e-383b-a411-831d5877bb05 | -7.1103 | -46.114101 | 2025-08-09 00:44:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50f8feaa-4d52-3b1c-b61c-24f0ff3d3ab9 | -5.0828 | -48.308498 | 2025-08-09 00:44:00 | METOP-C | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 851f0c64-729d-3d17-ad3a-ca29d0369ac2 | -9.0723 | -40.491798 | 2025-08-09 00:44:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| ceca140d-49ee-3818-9122-863a50c0a14a | -11.3795 | -54.349701 | 2025-08-09 00:44:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efdb75a0-56ee-3ea3-880c-0a0e0c5272f7 | -19.8211 | -47.055801 | 2025-08-09 00:44:00 | METOP-C | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d94e406e-245b-3341-8972-f2fa097ff50b | -6.5755 | -44.558102 | 2025-08-09 00:44:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca2618f5-c3e4-35aa-8107-ce9cf67be442 | -7.0786 | -59.159901 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a850ce5-812c-36be-a3e9-ec9f3ab410b1 | -7.0641 | -59.186798 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bac27f8-5494-32f7-8c2a-5b899212299f | -9.082 | -40.4893 | 2025-08-09 00:44:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| b0d974f7-626b-3662-9ecf-8c1f8f5c32e7 | -12.7243 | -47.797199 | 2025-08-09 00:44:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c001255-e1fa-346a-b4c6-2bb75446f005 | -6.1321 | -42.975101 | 2025-08-09 00:44:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 659034b3-3867-3ca6-bddb-42ea35e703c8 | -11.7478 | -47.494701 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92b92ec1-8379-30c3-8817-2dc9550d39b0 | -11.7775 | -47.3992 | 2025-08-09 00:44:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 905a485a-3abf-3e41-a1f3-43921301124f | -16.5506 | -47.5825 | 2025-08-09 00:44:00 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eaaf17fe-c6f6-30e3-b019-b48c90129ff1 | -7.0689 | -59.1618 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6aa42ca0-0c83-35fc-9aa9-d074d9be4a29 | -3.9621 | -47.8806 | 2025-08-09 00:44:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df61bda6-809e-33a4-a431-6857738b8dce | -22.1493 | -49.452801 | 2025-08-09 00:44:00 | METOP-C | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b672534e-2f01-3ce1-8c4e-3e6d4cddea1f | -18.4506 | -50.711899 | 2025-08-09 00:44:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| badcb8a6-ef82-3f89-a61c-d64ca6fcdd63 | -13.0411 | -43.855598 | 2025-08-09 00:44:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b619f67-cd1b-38f1-9d4c-ebd8b458c27e | -8.917 | -60.722698 | 2025-08-09 00:44:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c9ef2a3-6a74-36f7-b5ce-2dd8cdcb9c15 | -3.6507 | -48.318401 | 2025-08-09 00:44:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a92cb889-a707-3002-8929-e6f205b4ebad | -15.1828 | -48.710602 | 2025-08-09 00:44:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 56235a24-78e9-3547-b26b-71e7ceda272e | -11.9368 | -44.552898 | 2025-08-09 00:44:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c57997c5-88fd-32eb-8f78-99700a38aa91 | -12.0355 | -44.018101 | 2025-08-09 00:44:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c80e0518-79d7-3877-b7b2-703d4f6c454d | -3.8395 | -47.752399 | 2025-08-09 00:44:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29c3388e-9f2b-3a28-9ec6-264db742fe3c | -3.9834 | -47.883499 | 2025-08-09 00:44:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc59cd32-c49b-3b8a-b0fb-c70f6b06c7e3 | -12.5662 | -47.103699 | 2025-08-09 00:44:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a6a0c9d-7d50-3461-a58e-5c1f898f74e4 | -7.0834 | -59.134899 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ce4886d-bf7c-34a2-bbf8-0ec61087516d | -13.0389 | -43.846401 | 2025-08-09 00:44:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ebe9104c-745c-3d66-9250-cc4656706b57 | -11.7396 | -47.503899 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8dbff492-6378-3d47-91f0-b0bb74c5bbf1 | -7.0593 | -59.115898 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a42e0f1a-3bb9-38ee-9637-3c602a788ab8 | -16.5522 | -47.589699 | 2025-08-09 00:44:00 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e402e04e-cf7d-3cd4-bec9-b098a598ebeb | -11.7282 | -47.499199 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 373972eb-9870-36d7-9dd6-1d8282b0d331 | -12.493 | -47.505402 | 2025-08-09 00:44:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8688afcb-aa64-30f3-8bec-f67cd48a016d | -17.516701 | -50.286999 | 2025-08-09 00:44:00 | METOP-C | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7abb0978-9f1b-3d0e-8c57-402b6be43274 | -12.0429 | -47.521801 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2d17aa2-c2ae-39e7-be59-d04c6755aaae | -19.5926 | -42.680099 | 2025-08-09 00:44:00 | METOP-C | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b53cb7bb-6d5b-32b4-8a73-0799a71c3726 | -11.7239 | -48.342701 | 2025-08-09 00:44:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7829dac-fa86-3e0a-b850-8e1f3321f31e | -7.0689 | -59.209999 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7ccf5f-9f97-3cd1-86e2-c9a8a2530e85 | -13.6267 | -49.025299 | 2025-08-09 00:44:00 | METOP-C | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b598ecdd-e821-310f-ae61-c7ced1a80da3 | -5.2208 | -46.0681 | 2025-08-09 00:44:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 868a228d-9a60-30e3-81cf-7de81b2bcfcc | -7.4024 | -47.139702 | 2025-08-09 00:44:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e1b5578-2c29-30de-94bf-8ecb39c24906 | -7.9637 | -49.399399 | 2025-08-09 00:44:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b92a3c8-4853-3f9a-828e-431d90c9441a | -13.6252 | -49.018002 | 2025-08-09 00:44:00 | METOP-C | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 163747d1-6c26-3348-b8b4-8ac43f56494d | -7.069 | -59.113998 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9346d1fc-9300-3605-b1db-d1ed15a394cf | -11.7347 | -47.482899 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95b8a366-300e-3b5e-8213-460531e35050 | -12.0397 | -47.507801 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0efa02cb-869b-3006-80cd-b0fc38977070 | -3.4357 | -49.041 | 2025-08-09 00:44:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b793a8dd-108b-3f63-ab2e-481e059ff06d | -7.064 | -59.138802 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3e7227d-46fc-3293-9cea-80f556c3ab34 | -9.0777 | -40.472198 | 2025-08-09 00:44:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 9c8ebaec-c880-3159-b829-27bb66c3b19b | -7.0593 | -59.163799 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f85506f-c0ca-304e-855e-32a1be3d2424 | -4.8711 | -47.751301 | 2025-08-09 00:44:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9ac6ba1-d183-3f8d-a122-80affb5771d6 | -4.4808 | -48.1152 | 2025-08-09 00:44:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d413580-a0da-34ab-848b-8a0258af07f1 | -3.4259 | -49.043201 | 2025-08-09 00:44:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3a5b05d-1a4b-3ec5-b5b1-2a64f0aea800 | -7.9622 | -49.392601 | 2025-08-09 00:44:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 896a4f8b-977c-396e-93d6-3ff601320178 | -12.0495 | -47.505501 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fb39743-d9b5-3e57-92b1-575050ad7818 | -3.4243 | -49.036201 | 2025-08-09 00:44:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6510e80-0c77-32a1-a117-166bc87d915b | -11.7363 | -47.489899 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb977e72-3977-3e49-8fc9-5540ba30ab63 | -12.6918 | -48.201302 | 2025-08-09 00:44:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a765270a-b15a-3ed3-a42a-27d02ef6e184 | -8.0578 | -46.322498 | 2025-08-09 00:44:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df5edd2c-0a3e-3d0d-bb48-4cc423f354fd | -7.0737 | -59.136902 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20799ec0-95f8-3f9b-93b7-480ae1948240 | -10.183 | -49.508099 | 2025-08-09 00:44:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| caa98e4b-f782-37cc-9e64-c4e0983a6c50 | -19.822701 | -47.063099 | 2025-08-09 00:44:00 | METOP-C | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ec39e03f-3a83-3b63-be5f-05f6dc20fd25 | -10.0038 | -48.124298 | 2025-08-09 00:44:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96ca3722-cb89-3f25-8849-e85f23a57927 | -13.5506 | -55.243198 | 2025-08-09 00:44:00 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ca20d5b2-140d-3740-899c-0af646784799 | -13.635 | -49.0158 | 2025-08-09 00:44:00 | METOP-C | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e53b5811-bae8-3e4a-a6e0-fe9a32aebb33 | -16.053499 | -49.029999 | 2025-08-09 00:44:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 61a77004-3ca0-34b4-97a1-e6d2e2203de0 | -13.0508 | -43.853199 | 2025-08-09 00:44:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 521bc8cf-bf97-331d-9eae-ed8f2115d89b | -6.1418 | -42.972698 | 2025-08-09 00:44:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e333a847-bd7d-3ba8-a033-e81498f14f4e | -13.0464 | -43.8349 | 2025-08-09 00:44:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa2e4ba8-8ccb-319d-bee5-4c27980e5e3b | -11.799 | -44.928101 | 2025-08-09 00:44:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64f75ea1-1967-372f-aca6-b4fe7bad1dec | -3.8412 | -47.7598 | 2025-08-09 00:44:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
