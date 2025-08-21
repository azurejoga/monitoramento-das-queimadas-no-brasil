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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f808f4a8-ebc2-3d3c-8be4-846d0818991b | -9.26228 | -44.5368 | 2025-08-21 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa02c06d-1118-3510-9daf-1b26a75f1da0 | -4.86834 | -42.53852 | 2025-08-21 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d37f697-29b7-375d-9152-4b7cce273952 | -6.53425 | -45.46616 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e3f5744-2366-38e3-8149-651817384c3c | -4.63498 | -42.53439 | 2025-08-21 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3ed9b0f4-0c95-3b24-a988-df81f181d7b8 | -6.06637 | -44.14344 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 457d886f-5f63-3189-a934-b2226397dc67 | -6.4294 | -44.67311 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92b37ce6-de99-3cd7-80ea-127b79d3edd9 | -6.61595 | -43.88167 | 2025-08-21 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0987c0e0-cb5f-37a4-a327-03dd9cf0be3b | -5.87516 | -48.11857 | 2025-08-21 04:38:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2853b413-5cba-37f0-9117-1eb1b690a404 | -3.55071 | -49.97785 | 2025-08-21 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 942edd58-c13d-3c6f-898d-df5f00e77adf | -5.89756 | -46.16044 | 2025-08-21 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 761c092a-8605-34f6-af9c-25f0bd707bed | -7.61882 | -45.27366 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a07f796-0ed8-30d0-bfa6-dca8befdd78d | -7.70585 | -44.01557 | 2025-08-21 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc99d238-bd71-3aa3-bcaa-88c45667f0fe | -2.94725 | -48.05796 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42e8e13a-7446-389a-82ad-00ec7d992422 | -7.5966 | -55.19631 | 2025-08-21 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1f70790-433b-3646-9a86-1de370fe833a | -5.37899 | -42.34743 | 2025-08-21 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0715c713-cd9b-37f7-8e7e-e9702d0e89be | -6.2221 | -44.12553 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3d9dadd-0589-34ec-9854-242325534ae6 | -7.64279 | -45.24693 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce1f1b58-d700-3179-8b9f-c9b4db59717c | -5.98981 | -42.84889 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b79d954f-a545-33c8-9a09-6fe48db93b8c | -6.21634 | -44.13614 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8131a2d-af0a-341b-bc00-7f6617b1c28e | -6.27577 | -43.72763 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13a6cc05-8c61-3427-b840-366c41dbfbb8 | -5.96038 | -44.15784 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8951f6f8-1d84-360d-993a-b833dbab92a6 | -8.38362 | -44.60181 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 282066f9-365c-3209-8562-c61b3cb4f523 | -5.95438 | -44.14212 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0db2d3c1-856e-3546-b6e2-f812668aa4d8 | -5.98535 | -42.84808 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 602db54a-ca22-32f7-85f0-cfcc6e958bbb | -6.02962 | -44.3592 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e44ece5-e094-347c-96fc-403ad97cf388 | -6.95258 | -42.86249 | 2025-08-21 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 42ec76f7-7a04-3e40-abcc-f0b3b3c583e1 | -8.17894 | -47.32835 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 726df337-56f2-3637-8983-7ca820838e5b | -6.53114 | -45.46082 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cf8d133-8a45-3e04-832a-4885398d6bb4 | -8.8306 | -52.06049 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35ca6c3c-ae3f-368e-9b9c-5dff8d8334ab | -5.97189 | -44.159 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e6528f7-ceae-3a3f-8464-1caa60f38231 | -7.38476 | -45.98486 | 2025-08-21 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1a62296-400e-3e29-b041-413a28aa4ba5 | -7.38849 | -45.98541 | 2025-08-21 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbb23b15-9c4e-3447-a78b-c09bd0e74767 | -7.86381 | -46.72984 | 2025-08-21 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab2894a2-9ec6-30ff-8bac-c08179aa2704 | -3.01733 | -49.20863 | 2025-08-21 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0587fdc0-2ad5-3834-8aa4-55f8bec5dc29 | -6.02587 | -44.38405 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e21205f5-17f5-3d77-b350-b4d1390f062c | -6.02049 | -42.82689 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3bf173fe-1d5b-3798-b29f-643af6334c37 | -7.03014 | -44.62215 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cac555ca-a5a2-3665-84e6-5e11e324371c | -2.37552 | -47.65508 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c23a602-292e-3347-beee-182f1b85d9b0 | -5.96776 | -44.13676 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74487ae1-d83d-3c1a-a96f-605565b5bdc8 | -9.41385 | -48.31628 | 2025-08-21 04:38:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 298ab8ec-71b5-334a-ad04-dfd0036cebbc | -5.4406 | -45.10236 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| caad63e1-c9ed-3c85-97ad-49ee5a82cae0 | -6.54568 | -45.52021 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e0fee34-02f3-3354-9047-e63ce8054836 | -3.96073 | -48.09098 | 2025-08-21 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c114d7e1-fe1b-35b9-babe-17b47fd02d50 | -7.38781 | -45.98992 | 2025-08-21 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02b10e31-4f96-3a92-8f8f-fd9d86df4f6b | -7.01853 | -44.61704 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 2936471b-0681-358d-85f7-247e4d8631fb | -6.49261 | -42.97116 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55c06b1a-06aa-3f80-8bce-767259a28fa4 | -6.86405 | -44.42341 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94e7dddd-e649-3377-accd-9fd73541ac12 | -5.95739 | -44.14992 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d7e1404-a70e-37ba-b036-a7f0ae1f7bc5 | -9.29524 | -48.42728 | 2025-08-21 04:38:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e495f512-499e-3aad-a03e-80ed02cb0297 | -2.90297 | -48.2531 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18d9fd88-2ec1-3d52-ac9b-a0838abd749d | -4.64663 | -43.1227 | 2025-08-21 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f34d03cb-d164-3411-819a-8894419d533e | -5.96116 | -44.14638 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72c6d522-508e-321a-a672-74040c0f0b36 | -8.29154 | -47.61535 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1958fc05-08ff-3a5a-a549-d8093fecc440 | -5.66452 | -43.50908 | 2025-08-21 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e37b7938-b53d-38dc-b106-58d64cc2ed5b | -7.3053 | -43.68548 | 2025-08-21 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc32ac65-e0bb-3aae-8547-031ea48b4a4a | -8.07335 | -43.68528 | 2025-08-21 04:38:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aebd5631-4b48-3f12-9a4e-7283712e9c6b | -6.06663 | -44.11384 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0679202f-9347-3a05-895b-419f673e56b2 | -6.74544 | -43.93872 | 2025-08-21 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f4ab0bf-e5bc-390d-a5f6-87a515cd08d1 | -6.44968 | -53.37773 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 33324043-92ae-3eec-a1a2-fbfdc94dd250 | -5.5456 | -45.20261 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44aab994-f542-3e17-a8ca-bffee0e54916 | -7.99033 | -47.33673 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35661670-7e35-3894-a06a-9a0aaf918643 | -4.87218 | -42.54358 | 2025-08-21 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a91d8cb-03cf-31e3-af08-c3c9124c4146 | -5.95629 | -44.15723 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d97c337-d955-3973-8ae8-c6f3a2c855e4 | -3.94426 | -41.82905 | 2025-08-21 04:38:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea064715-8b19-38cf-8318-8c201d92bc7c | -7.6042 | -44.38932 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e56288d0-811c-390b-a4d1-d5497ea531c7 | -8.14493 | -47.3393 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 700bf228-3b28-3914-a209-5a730c4005f6 | -6.04347 | -44.35406 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eee17263-361d-3791-8254-842568dc2174 | -6.29618 | -43.88189 | 2025-08-21 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfde4f51-e873-329d-b7df-312ab13f0ab1 | -6.10175 | -45.41253 | 2025-08-21 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef461b1d-c7fb-37f1-9dcf-e18e03f54fe5 | -8.78208 | -45.4527 | 2025-08-21 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ab77c1f-738a-3d7c-9fe9-4d4d98765843 | -4.86385 | -42.53786 | 2025-08-21 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 574f2abe-e89f-313d-b9f2-3510e44db97d | -8.83246 | -52.04899 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3f34869e-4a79-345d-ad6c-12620f0fc201 | -7.99798 | -44.79437 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e56413e1-c3f1-3a79-af64-aa6fb909bdf7 | -2.69522 | -48.21332 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 193886ca-72cd-3e3b-9b32-55824f169eee | -9.10154 | -45.17833 | 2025-08-21 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d299bf55-92e3-3b57-9bdf-e03bedf6f63f | -7.02717 | -44.6143 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4988c492-716f-34a8-ae8c-b32cc9f22a57 | -6.42541 | -44.6726 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea7bce54-8cc0-3b3e-b9fd-c06b2baf8ee9 | -2.25952 | -47.85123 | 2025-08-21 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0649a1f1-e574-3b62-93e9-99b859389daa | -6.01136 | -44.37069 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1a64fb4-cd6a-3e50-aa42-26d34400c7c3 | -6.19943 | -43.57112 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 62e8d25f-2c86-3d61-baee-97de87940f1c | -7.02451 | -44.63243 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 49c98af6-3ca9-3d19-b9d9-fbc77b5409f0 | -6.44594 | -53.37711 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5fc6df4-03c5-3fba-ac8a-5e1869a722c2 | -8.77817 | -45.45206 | 2025-08-21 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89e593fc-e8a5-32c5-bfee-2ad31356fa4c | -6.49644 | -42.97625 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d02ebecf-b1d0-3f1b-b179-a72c34b5acff | -7.62963 | -45.25478 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed0a5644-16ad-3288-a15c-4ebd19b9afef | -6.45717 | -53.37895 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 292a2014-974a-386d-b7f9-2c5c588a9b54 | -2.69907 | -48.21038 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d26c5df7-6a3c-3966-a18b-8ef5129bdd6f | -5.68053 | -43.86351 | 2025-08-21 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b03b51f5-62a3-3ba1-bd1a-21d232225fe1 | -5.92952 | -47.31456 | 2025-08-21 04:38:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fca10c2-d537-31c8-aca1-af30aa859481 | -4.16923 | -48.58186 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa4beef8-a5b4-30a4-982e-0445d9995dd8 | -6.95192 | -42.86713 | 2025-08-21 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 70228545-eac1-3ee4-a443-9b6a72359358 | -4.77668 | -45.32277 | 2025-08-21 04:38:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b484a935-4139-35f9-9da2-8998f1f96670 | -7.65915 | -45.24693 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 755b0ec9-eecc-3eef-9b0e-664416a07de4 | -7.02663 | -44.61801 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| aa0866c5-84a1-3955-9b6f-07591c4626f1 | -2.53831 | -47.72001 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c5c9d22-76da-3749-8d3b-d2c8c60e5778 | -6.1119 | -45.42162 | 2025-08-21 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a3330f2-ec48-3b31-9dba-ffb7678c537f | -7.63893 | -45.24872 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 740b6311-dc63-307c-8ab4-23a1a0eadbf4 | -6.5729 | -43.00226 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40f10ad6-a63a-3a87-ab52-46ac5afc6607 | -8.36263 | -47.49921 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a85e463c-202a-3bd3-ae00-87a556bce4db | -8.43168 | -49.5755 | 2025-08-21 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README41.md)
