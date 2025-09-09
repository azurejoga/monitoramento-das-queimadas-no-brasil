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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48b7429d-bf41-33fe-ac40-16f62af87a1a | -5.00802 | -43.65292 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57181d13-cb1c-34bd-a47a-acde37812c67 | -6.85379 | -45.91768 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2de9fac2-a7b6-3ba2-9cd0-e7dfae12610e | -4.31214 | -48.10864 | 2025-09-09 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce147667-6a21-3b05-9c9f-19bd15d4dc8c | -5.8528 | -43.85901 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79588a31-d19d-3ec2-aac2-8aab5d0ecc73 | -4.50345 | -47.82434 | 2025-09-09 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b4d6272-ab52-35bd-b2ea-43cba4ad6e6a | -6.07478 | -45.5306 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b83243d6-7b98-39cf-a1ee-fb0930b63bb7 | -5.63277 | -45.43829 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44da7079-27f1-3ba2-b856-a434419b9bba | -6.17762 | -42.65061 | 2025-09-09 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cba62102-b287-39c6-ab81-938b6fabb24e | -6.48197 | -41.7618 | 2025-09-09 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4cc8bf64-0268-3a6f-a358-cdb3384aeb1c | -5.26794 | -44.45034 | 2025-09-09 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a397553d-6fe0-3a5b-81e3-032a5f389b88 | -5.0144 | -48.46875 | 2025-09-09 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cdd18e24-693c-3208-b52f-9fe4a971e083 | -6.21881 | -45.57932 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b8688cd-a541-38cb-bcc9-d6910e2d7826 | -5.66704 | -45.40008 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1a6615a-16c2-397a-a258-49ec16617838 | -5.51679 | -42.6731 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 217d562b-5ca0-34e0-ab8c-5af55797a4e9 | -6.40024 | -44.43906 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 502087f6-578d-35b4-ad17-efddf9518376 | -6.26188 | -43.49969 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d26557e-ca79-314e-a403-cba7e7344506 | -6.49225 | -42.4235 | 2025-09-09 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 168487a4-1109-300a-a851-1a04f75a98df | -4.61973 | -46.59716 | 2025-09-09 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c3f613d-d8c5-3ae2-bc84-a93f442dc3da | -5.54719 | -45.16659 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8bbdd843-5d4f-3afc-9cd0-cf7b55652208 | -4.99386 | -56.25358 | 2025-09-09 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dbba945-a310-33f2-b2d7-44f487c3ee4b | -6.40708 | -44.43873 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0134946-06c9-31da-9ba5-993c3eee2d72 | -5.41722 | -51.53507 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4ae192f-ff85-37ed-9602-81dc7f6f066d | -6.92091 | -45.51715 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 836de426-2bec-3a32-bc8b-812cd7710731 | -5.71246 | -45.41806 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d201941d-420f-3200-a548-9f7ca833d35d | -5.81802 | -43.96553 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 064ab595-fef3-3555-bc6b-c0df850baa2a | -6.9508 | -46.31861 | 2025-09-09 04:32:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a3d730f-a2cc-3e7e-b1de-fad1920d1d22 | -6.79408 | -44.78419 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d3522c0-11c5-3014-86d9-19e89c9e7776 | -5.19122 | -43.0328 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d01629c5-1491-399b-bcb8-84eda031b139 | -5.82746 | -44.81681 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2235ea2a-d4f2-36f9-bf13-83efe766aa11 | -5.75031 | -45.26058 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07daa0cc-fe6f-39ee-94ad-4149c301b69b | -3.79268 | -48.87661 | 2025-09-09 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f36a28e7-7dfb-3702-988e-8ee92008d970 | -4.90015 | -49.92474 | 2025-09-09 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0665a573-1407-3e69-a562-c68c9ad420e1 | -5.45878 | -43.44139 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9dbe7e3b-56d1-34c4-b303-b32b7c1a94aa | -4.97308 | -48.94469 | 2025-09-09 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45978e42-664c-350d-9b40-a412929260d6 | -4.40455 | -48.94322 | 2025-09-09 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8093089a-91ed-399d-b881-a103f51bb0dd | -5.68338 | -43.90296 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 66206bbc-c7fb-35d0-9891-6cd40dbfdc23 | -6.49067 | -41.76341 | 2025-09-09 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6104dad5-0eb5-3863-8a1c-eeec25806355 | -6.32212 | -44.38195 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9651cbe4-d55e-3d29-a9bf-33b4f5a3af2a | -5.65765 | -45.46176 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edc3853d-0693-3941-9cbb-b031a1ddb079 | -5.863 | -45.30479 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6e4cba9-ad24-3085-84dd-b073fa51c8c1 | -5.66054 | -45.46614 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f5121a8-da5a-3bda-abe0-7dfe437e0c08 | -5.73219 | -45.40531 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5eec75dc-5e9d-30f5-a8fb-0f0bf70827e0 | -2.34207 | -47.58989 | 2025-09-09 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5b986b0-e2c7-30f6-a0c9-19c1446dd202 | -5.80886 | -44.84336 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d9e7cb3f-9368-31e8-835c-7faeb79e26b5 | -6.14628 | -43.30246 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c3d2f82-fb2b-3525-a5fd-bb655157534d | -5.35985 | -44.80135 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95c7aade-4bed-3bb3-9e1a-88e9b1103b51 | -6.84185 | -44.88646 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4bd159e-2e08-34da-ae27-6e32e04f83f7 | -6.30214 | -44.2193 | 2025-09-09 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6a641e3-75ca-38cf-91fa-73b2c5fa0b50 | -5.6762 | -45.45674 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 349be74a-9a15-3337-9f47-88cb4e44abca | -6.3462 | -47.7244 | 2025-09-09 04:32:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 821895c8-fec7-39bf-938f-a6fb59bc677c | -6.20628 | -43.54389 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 867a21db-6fda-3ce5-9b66-3f2c67e44a1a | -6.40521 | -44.45152 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da34e8ef-4432-3e49-acad-86dc72d5e2ad | -6.22646 | -42.5753 | 2025-09-09 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e5a9821-9a17-3eb9-9840-329c8f7febd5 | -5.67967 | -45.45728 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa338f8a-03b8-3d2e-b6ac-12b43586d1aa | -6.20756 | -43.5464 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 038ed2e7-487b-3af1-96ba-227a572e0e84 | -6.7066 | -45.13659 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1771f90-ddd7-3f55-8c9a-a09a3f17aa53 | -6.40461 | -44.38551 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0373df98-ea64-3632-8892-de7c23900b0a | -6.11724 | -43.95454 | 2025-09-09 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fb7b5d9-1676-3826-a4c3-0f700407fcbf | -4.42062 | -47.95957 | 2025-09-09 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e900e040-1f41-3069-9575-39c710686d54 | -2.43134 | -49.30927 | 2025-09-09 04:32:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5035092a-fce5-311b-939e-9dbfc50958df | -5.73497 | -45.28328 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee286fce-ad8e-3af8-b2ee-28a302a7ae40 | -3.33202 | -54.90977 | 2025-09-09 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2e4b930-c678-37e9-aad3-45dec5c525c3 | -5.81924 | -43.9767 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6cb9ee1d-b400-30ac-968a-fd3f78c3bf33 | -6.8681 | -45.59829 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f90ffbb0-4695-389d-bf14-133b36742a75 | -5.81914 | -43.98414 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58839cb4-6663-3f1b-b95a-0099b8685821 | -6.56687 | -42.94983 | 2025-09-09 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e24f758-bf75-3dc6-a185-fa92fcd50d3f | -7.19707 | -44.88776 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 719b86ce-5765-3bf2-8586-cadcc445af41 | -3.32722 | -54.90902 | 2025-09-09 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bc744e1-7ae1-3cf9-9307-bee9df910517 | -4.97539 | -43.63852 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5a66a39-213f-3d59-81d0-3977dc23f553 | -5.39648 | -43.2411 | 2025-09-09 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d595db6-6c28-3613-bf39-24d84a094259 | -5.6755 | -46.34853 | 2025-09-09 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15747da0-d77b-3e97-8955-4ae8080889f1 | -6.92384 | -45.52156 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2d257aa-1391-36e0-baff-5478f7101504 | -5.57055 | -52.16181 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7f5ebd6-5c45-3b8e-82ab-92c1ddaaed93 | -6.06079 | -43.11679 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9d1c4df1-ebfc-34b2-8d0d-c6ac345dd87a | -5.8433 | -44.20758 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7d4f8c5-107f-38cb-868a-c8f40fe79aec | -5.86947 | -45.66064 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef1801c1-b822-3983-afe7-b0eaa881dfd1 | -6.43513 | -44.05685 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e5a2e3e9-ad21-31d7-bdb5-5c0541c2230a | -5.96931 | -45.78774 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ca0fb93-e64f-3c86-b493-f234246681f3 | -2.43539 | -49.30603 | 2025-09-09 04:32:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e5ee23c-4ec7-3eae-8bda-6008a4cdce69 | -6.40264 | -44.44805 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb243be0-5dd0-3bc7-93cb-3ea836a8f2a1 | -4.70107 | -42.82441 | 2025-09-09 04:32:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 62dfa323-13c7-340c-a115-878fa9ca1b69 | -2.91391 | -48.67312 | 2025-09-09 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b709a24-5279-3edf-a2c8-ce02fa2b8da6 | -5.91659 | -45.76421 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db60e59d-384a-35bd-956f-88d4938796d3 | -6.20864 | -45.03033 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| accbddb8-4b9b-30bb-8e5a-f2cf53cc4040 | -5.65714 | -45.41834 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98dae825-fb71-317d-b807-81b38ab11dbd | -6.05354 | -44.25274 | 2025-09-09 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ef4cffe-bfd5-3ffd-b159-6d47a1739822 | -4.69711 | -42.8238 | 2025-09-09 04:32:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fdc320c2-0cda-351c-8f63-77a41118fe7a | -6.20575 | -43.38832 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35e2117c-6729-38c8-a647-9b7a4dff0be0 | -5.81617 | -43.97166 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a0a2d00-36a0-3385-8e9b-dd4157213e36 | -5.81806 | -44.12188 | 2025-09-09 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1ee5c9b-ea41-3f9f-9db1-625b71de5779 | -6.07884 | -45.52733 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb937462-813b-39c1-afa0-00d15d753261 | -6.19878 | -42.47612 | 2025-09-09 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 044cc605-c029-3b43-8911-4b3530dc1841 | -6.35891 | -43.0317 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e431d173-c6ba-3d1b-a372-b3eb08cf958c | -6.06368 | -43.31931 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9ea5cd08-eaea-370b-b8a0-cc21a2e26b6d | -5.68374 | -45.45394 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fbf848f-31b5-3749-b6b2-4b68cfd85d65 | -5.19318 | -43.04489 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65129d27-8a8a-3cae-b086-8438317079c3 | -3.48696 | -40.677 | 2025-09-09 04:32:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8d8fd6fa-0910-3351-b14f-82a455c394c5 | -5.83965 | -45.38892 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62de8c04-a41d-3f1f-87e2-350ab7fe6db7 | -5.5809 | -45.03794 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 6c482b01-f860-3243-bfd9-a6ecec1d58f1 | -5.63742 | -43.6427 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README28.md)
