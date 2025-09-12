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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4aa65042-717e-309c-88f1-c4906839bc84 | -7.72549 | -50.75397 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 051e1180-dbf3-3b7e-9c59-ce68bf52d699 | -6.82888 | -52.79153 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74a39195-c810-33e3-bbd2-5a9be5569aaa | -7.24467 | -44.47834 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96704e3d-fca5-3d02-a17e-fc3ab6c5287e | -12.14194 | -44.86682 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee179c77-b897-37c4-8718-0348932cb724 | -7.07211 | -44.1437 | 2025-09-12 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa83fbaf-f713-3633-989d-bcde68e8f885 | -5.36437 | -45.97581 | 2025-09-12 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3b2afd0-3ea5-3093-90cd-4d94fe7ce98c | -11.42723 | -43.54265 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f0743d59-6cd8-342d-9946-2aa5eba7a55b | -7.07331 | -43.9023 | 2025-09-12 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d4312ec-30a0-3e40-926c-d99265650129 | -5.60462 | -45.78748 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb7732e1-23b7-3632-a637-5c155a2f2b63 | -6.68398 | -44.13694 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8e73b43e-edb4-3900-9b9a-245e0670a14e | -8.04082 | -52.32717 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3d71d27-285c-3adb-9132-df3064892c02 | -9.66168 | -43.53299 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c0988d3-4a5a-3c1a-a16f-749839175c8b | -9.0606 | -50.50151 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9139f0bd-d6ee-37f2-9bd6-50fc31c7a09e | -8.88078 | -49.53729 | 2025-09-12 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e5b077d-e8e9-34c2-b4a2-9a9e286470fc | -9.21477 | -59.39625 | 2025-09-12 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa58c5e6-776b-3df4-97fe-5ee192d9dd92 | -10.6702 | -48.59832 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34c8be28-62c1-3911-a829-c9d7db1427c7 | -10.48048 | -49.37373 | 2025-09-12 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1a1289f-4bf6-32b8-997f-939dec8817d5 | -11.43586 | -43.5627 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef6aa316-63de-39ed-9c86-738b07790fd2 | -10.12687 | -47.90129 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2914f25f-1b57-336a-8606-28a603f52c68 | -11.68485 | -46.56875 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 025b55ea-5f93-3f00-962a-1f8e67930b97 | -8.62355 | -53.12411 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 084660ac-918d-3e87-befe-00a964389ddb | -11.67265 | -46.58141 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09476775-9214-3199-b41c-3ad9f41eae7a | -5.94289 | -52.05947 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29062425-0509-3608-9256-746e7a8d1ecb | -7.45288 | -51.80271 | 2025-09-12 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd26e505-b14f-3650-90da-7c65309b16ad | -5.43648 | -44.86619 | 2025-09-12 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 362320b2-0ff1-3dd3-b730-a297d394162a | -11.1056 | -51.96798 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97b30b5f-0bba-3b57-b08d-9e2281ac61d5 | -11.52898 | -50.58946 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e7a553c4-ffb1-3352-a6e5-d5f60ae43b5c | -9.03569 | -47.09615 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a00bd47-092c-334f-8cc2-df58b991a397 | -8.18491 | -42.41507 | 2025-09-12 04:25:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 98e579fe-6f05-3e34-9788-13f95f8a25d1 | -9.96258 | -51.68436 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f15cbbd2-f450-3e8d-9f53-195302525541 | -11.6599 | -46.5976 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 148fbfe5-ffb5-3ee6-a8b9-594e5c318008 | -6.25592 | -46.11642 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ddf8097-db21-3f42-912f-99daf1388cd7 | -10.85631 | -44.79284 | 2025-09-12 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6555e183-e07b-37f4-a612-5f523f712a6b | -10.53757 | -51.52401 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c68380eb-1ad4-3e22-8045-21c175a9dcc1 | -11.68933 | -46.60601 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17974648-255a-3349-a267-e23697671a53 | -6.33265 | -53.46438 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80f397a1-a09d-342f-be85-fc768a4bc252 | -6.4966 | -44.49252 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de5445c3-f4de-3921-991f-24b821dfb541 | -9.07761 | -47.04573 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99a77296-35a3-3137-93cf-71bea096cc76 | -5.9592 | -45.84287 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5ca9dcc-9465-3ee5-a16e-a70f4dc5afc8 | -7.54761 | -44.39682 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6424dcf-dcf8-3cfd-9df1-c244c55180be | -9.89156 | -46.46679 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f4d89a8-a35d-3e41-b465-1a22412e6da8 | -8.19357 | -46.10256 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 727fee7c-af76-35f6-982a-81bb26720ce7 | -8.48001 | -45.68168 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f551cacc-88cc-3fe2-8cf5-c2d1f5266dcc | -8.92594 | -51.06579 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32f76fcb-f5e3-36c4-83b9-d9e2350f3567 | -6.83554 | -45.62454 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5416f2fc-a0d1-3744-be2b-38c8553bf444 | -9.99171 | -51.72613 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96b1ea61-d124-313c-a58d-ac1be1cfcf86 | -8.95475 | -46.72626 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48bfc4a1-a9b5-3694-80d8-49b000eed1a7 | -11.68813 | -46.52544 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46b27fdb-dc69-3609-9c1a-604835e7db27 | -8.22345 | -49.50008 | 2025-09-12 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c181da7-3e15-3c8c-ae1b-1c2382ad68c8 | -5.40892 | -45.92978 | 2025-09-12 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5915dce4-df6f-3f2a-b8dc-5c0e6b6d0d43 | -12.10484 | -44.87365 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e39cb141-2a89-37d6-85b1-59d396106091 | -8.47403 | -47.27378 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc9c5884-22ff-37a9-99bc-845b8479dac0 | -10.34703 | -50.54504 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 84cea645-2fa0-3245-8341-3454103d5102 | -10.67535 | -48.58784 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9512a5c9-42a4-30b3-920c-3830dcfeb2ab | -9.06138 | -50.49685 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ef89d64c-6cc0-3004-a2a7-b130f37ae661 | -7.32397 | -44.37117 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8048bd97-0d31-30d2-b71f-5e23c61ff7e0 | -11.529 | -50.6111 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2d6eaba7-3619-3dc3-a9d1-987a9a3aa1f3 | -10.67079 | -48.59469 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 59212b36-2ff8-3c2f-9cbc-2e9b1437695e | -11.67819 | -46.56768 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96e31969-509b-3fef-90ac-3192588ffb8e | -11.67042 | -46.57374 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23b6ced9-4222-3d08-9bf9-732de4b0b812 | -5.36383 | -45.97927 | 2025-09-12 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b1a2577-2a81-3d05-b4a1-a8a283298eac | -7.31937 | -44.16782 | 2025-09-12 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4816878-2ab2-3e6a-b168-0de61db63f25 | -6.33262 | -44.84712 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 204d57a8-eb10-33d7-95f6-586ab663b4ca | -11.68047 | -46.61913 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89cb3838-7f34-37b7-8cbe-7ce54d1f9451 | -11.68377 | -46.59784 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95a6c1fe-0852-3a3d-b65e-a652daffc98a | -10.67719 | -48.64035 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45c30ace-a1e5-3d5d-ad10-5059d132c87a | -11.68598 | -46.58355 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0614e52-69ab-3e16-af14-7e736da84c3e | -9.09354 | -46.94487 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67223246-3134-3f87-94f1-f2dbca38ce56 | -10.41678 | -48.57616 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea3f6dbe-06ec-3b2b-b132-eda298052407 | -10.40985 | -50.59525 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31f637a6-3e2a-33eb-8bf3-9d5b1ee6e616 | -10.39637 | -50.49633 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db7fd336-5deb-3103-9f83-171b7c09c469 | -7.04416 | -44.69057 | 2025-09-12 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0334c3bf-d51e-37f7-960f-6388c5bd6cce | -10.6675 | -48.65742 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 514cef6d-a9c4-3300-90f4-9d008e211270 | -8.48785 | -47.27241 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3665e7ee-8c32-3ad2-8801-6249bb367dcb | -6.48122 | -45.15464 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2081d5e5-4740-33aa-8c45-9bdc88824107 | -8.42948 | -47.25596 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 536d0012-0ae4-3804-9665-23c4fa28ff48 | -12.11605 | -44.96893 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4411b60c-ff6a-36cd-beaa-363f9c19f99c | -11.66821 | -46.588 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 067698e9-e296-3777-adf8-9183f10cd731 | -11.6743 | -46.57071 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 498fe756-27ab-3609-a5ba-56539957c8e9 | -7.71834 | -50.353 | 2025-09-12 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9ac0562-8a69-30a3-a9ca-01b2c75bd78b | -6.82735 | -52.80042 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7780128-75cc-3648-a779-b8c2f53f62a8 | -11.16691 | -45.3075 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93d19fd1-0186-38bf-9d5e-5ee0147b4c69 | -7.79104 | -50.77765 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 85c8d3e7-84ba-333c-92b7-a315cbe74ee4 | -6.63499 | -49.7865 | 2025-09-12 04:25:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3316a622-af34-3fe9-8c74-65da659c31bc | -7.40619 | -50.64473 | 2025-09-12 04:25:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 18057f2b-0277-3b43-9473-ce132fff86e9 | -10.68041 | -48.66317 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fefdaa4c-9684-3e63-8893-c87d7592973b | -6.31166 | -43.32526 | 2025-09-12 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa4bd432-5607-3645-ba56-a33b112200ab | -11.52467 | -50.59303 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e48cafb-a4d0-3968-a13e-21f00b5892f2 | -7.44719 | -44.43559 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4988f005-f709-3e69-b952-06b02d5497f8 | -8.43888 | -47.26104 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| facad311-9147-3ecb-9f11-7f70c1682482 | -4.48777 | -48.11657 | 2025-09-12 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 18740cfa-e8a1-3acf-a02a-c53162ef9387 | -5.73661 | -45.59519 | 2025-09-12 04:25:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f3e2265-a57e-32d3-b53d-ae1b7450cdec | -11.16747 | -45.30374 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a9c41db-8acf-38c3-96b1-317d83ec1f83 | -9.07148 | -46.95561 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 47976d56-00c0-3814-96d8-d74e1b5fc7a2 | -12.11486 | -44.8545 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7561c88d-e155-3a10-ac57-6c9f4dec76da | -6.95333 | -44.77824 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a50ef89-dd56-33ec-804b-5adc46e5f961 | -9.99731 | -51.71679 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 616fb7dc-e828-3a38-a263-13af6894de37 | -8.95058 | -46.10246 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f27020b-925c-3808-a83d-a97918e748d4 | -7.40871 | -44.36415 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd1eeb6f-fb77-31c2-82df-c53f087c1de8 | -9.99909 | -51.7299 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README71.md)
