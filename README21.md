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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fda34f2f-abde-35a6-b847-e6b89c4b015a | -11.72439 | -50.632 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e2cbc5d2-160b-3b39-9634-463d009df82b | -7.31461 | -44.36205 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b919e821-74a8-34ff-a722-fff2b79e26ab | -7.84622 | -45.40368 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92a66c87-80af-3d8d-aff8-b27c211578c3 | -6.35214 | -44.09211 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1581f069-260f-358f-9f70-813e642f77c5 | -11.29929 | -38.93977 | 2025-09-11 03:55:00 | NOAA-21 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 93167da4-5a30-3e57-8a31-b08d86338f16 | -8.75114 | -47.11625 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55eca3d6-6337-3e86-9be2-f4131344efe2 | -11.03606 | -46.04229 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d182a84-98d6-3ab4-985f-fe7aa9089e7f | -9.71952 | -43.518 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb3379cb-5307-3d0d-b0dd-76b327af8d7f | -11.48559 | -43.63481 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 03c4a91a-40f2-348e-ab9d-d8b6a18faa88 | -7.53997 | -44.67509 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f8b45b01-4cc6-3243-9966-55acd42d8906 | -7.2668 | -44.61734 | 2025-09-11 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 091ea30b-5c1c-387d-8efd-ed52033ff33a | -11.46489 | -43.59778 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2c0fdef-2529-3f6d-96f5-0ea9c97b8abe | -13.26096 | -43.77552 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e61c9b9c-e930-3891-bd44-cb21e1afd379 | -11.96081 | -46.65076 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a1f203b-7e3e-379a-82d3-f7998a64120c | -7.73474 | -43.90608 | 2025-09-11 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5bec3c8-1c44-37c9-a4a3-d137811a1048 | -5.98629 | -43.70976 | 2025-09-11 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f025a4e5-92e8-3fdb-b327-0abc3d6c13d8 | -7.47977 | -46.09462 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cddb3fc9-42b8-39e1-a532-025dd6b6fb42 | -10.56605 | -43.66436 | 2025-09-11 03:55:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f07dcad0-3080-3f16-9ae9-bdc741af160a | -10.89447 | -47.25483 | 2025-09-11 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 662e0433-0fc4-36e5-9ef5-4e873127697a | -5.6022 | -45.78865 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94aecbb5-4a60-3d6c-85c1-bf020ce3632b | -13.2478 | -43.79352 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 411370fa-52d9-37af-acca-0ab36aac5b2f | -7.15291 | -39.41506 | 2025-09-11 03:55:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c23e18b-10c3-331c-83b1-f119c703cbef | -5.76687 | -45.5212 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1c5db62-8998-3d6d-871c-030805cd05b7 | -11.07271 | -51.32852 | 2025-09-11 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2d5a7b5c-95d9-3f47-b034-b28be29b5920 | -8.20241 | -50.10344 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7cb4789b-7035-3a80-8901-2a31b56385b8 | -12.40973 | -47.50374 | 2025-09-11 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63a68f8f-0bf8-3c24-a38b-a6f7358a7fa9 | -13.16175 | -45.28256 | 2025-09-11 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d45f0ee3-9991-341e-9136-b18920ee35e1 | -12.05769 | -50.9458 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db4f8a9f-1183-3956-9d56-24193a7c4bcf | -11.44184 | -43.57496 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a5a24084-c3c6-3489-817f-d7c6e5cb1a46 | -8.6642 | -45.73327 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 386cb8ef-0fb9-358c-8357-12f8b4c320a2 | -11.45898 | -43.58731 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9a77efb-df79-3705-afe8-22be8af8855e | -13.15301 | -45.28485 | 2025-09-11 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56f648b2-2fa1-3670-9229-254451e8d613 | -8.03841 | -48.67871 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aea5f8d-3aef-3c98-b74f-ed423e0dc4dc | -8.75848 | -47.11337 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8062e5e8-a2b4-3002-9fa7-4cc4971d052d | -12.03437 | -47.55508 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 231ebde7-4d1d-380c-b4aa-b68b2121e004 | -9.07949 | -47.06759 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fe5a16a-07e5-39c6-b95a-c05481c7ef59 | -9.67555 | -47.5225 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eb1b7d1-d9d8-3948-8ef4-9f678f16707e | -7.20593 | -44.97301 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d4d436fb-cb99-36b3-9e81-66a7c57dc5af | -8.73197 | -47.0918 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 6c5b9e3d-9fde-35f7-bfdb-cb871df3b0bf | -6.35061 | -44.07588 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 264907eb-a59f-33cb-9f72-904e4d18618e | -9.44962 | -46.42742 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0df18b31-377c-3733-8189-ec2668b5492f | -11.38455 | -43.51966 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3940a44-d736-3397-9766-5e0a62ae0b8c | -6.85824 | -47.8656 | 2025-09-11 03:55:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85b47032-d6eb-3ab6-a830-3224037cdd87 | -7.56132 | -48.21001 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ef6640b-e4f4-36bc-a7ba-1b3401217c53 | -11.47614 | -43.69051 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3c6ca330-6fd8-32b2-843b-36acc7340972 | -6.20128 | -43.49598 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| dbe38c9f-593e-36eb-84c3-5153cdbaaf4e | -11.4898 | -43.67846 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 15eeaf21-0699-34d2-a641-24ad0503afce | -11.45523 | -43.58666 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 52a9c646-e9c7-30a2-ad7e-5add3c51057e | -11.77285 | -46.48586 | 2025-09-11 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01bcbb4b-18d5-3491-aaef-e6e309c62939 | -8.6551 | -45.71983 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2a4ceb28-6b52-38e0-9534-ba65896fa79b | -9.06814 | -47.04632 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c1f87a97-3d87-3781-bf0b-50554f1330ef | -8.80613 | -48.09509 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2bcccbc-311e-3db1-bb2f-dec726d2acba | -11.39911 | -45.59353 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a62937fc-8cf0-3f78-a696-e046c418be29 | -5.8649 | -44.2233 | 2025-09-11 03:55:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 240403b1-0960-30e9-bd44-fb24ddb31fc8 | -11.37786 | -43.51383 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34b52743-b0d0-3ff9-8505-d480aea60d6e | -10.39746 | -50.52037 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 58787f17-f021-33da-93a0-c6fb385cf47d | -6.4391 | -43.65327 | 2025-09-11 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2b11ad7-fa43-3c98-be84-4541a8365fdc | -11.47357 | -43.63739 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 53263ff5-6510-3e3a-864a-ee5712d6462c | -7.49438 | -48.25922 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a71c9853-dc9d-332b-9cc7-3a362f1d8931 | -9.08242 | -47.07958 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| adee6902-1cdb-355a-99d8-a0cdff1f4fc0 | -11.35828 | -46.50314 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f6cf372e-7fb7-301c-8006-004342be851f | -8.57711 | -50.8024 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9dbc8f96-c395-3ac7-831e-55a01fce6061 | -6.25495 | -43.40583 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 477049b6-b137-36eb-9ad8-ac1eef6a8a91 | -10.93703 | -46.80083 | 2025-09-11 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e8f9406-143d-36e2-a4ac-5a7784d8d6e8 | -13.15641 | -45.2892 | 2025-09-11 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab2e2928-0980-34e1-95ed-00ce36f0ce81 | -9.674 | -47.53096 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4baf2229-1c6e-3309-b74d-be0a27d237a0 | -7.71798 | -44.80401 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10877b9a-4156-3382-8f50-163d4d61661f | -6.31888 | -43.4164 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f6859146-760a-34c3-8776-b4892b507d05 | -11.64346 | -46.91602 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e25c6cae-6ce8-31d3-bce2-0ddab4799feb | -11.6336 | -46.76367 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7393c0c-3d4b-31bd-a743-075f7446a489 | -6.41147 | -44.38093 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7b374c2-63f6-3520-ad37-7f3331e46cdc | -12.04432 | -51.13648 | 2025-09-11 03:55:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72b4766a-7269-3ea0-bf53-142f6fb32dec | -12.03868 | -47.61114 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e87f9472-b699-31ab-af5e-bb916991091d | -6.4494 | -44.0584 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d0a6359-b8af-341a-92f4-704efbfe8674 | -12.12718 | -44.85245 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16ca7f2f-1bdd-3880-b7ee-2d4d4b6b31f8 | -8.10931 | -44.85131 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85f30611-085d-35e5-a9e8-925b72f7dcdb | -11.4884 | -43.6639 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0309c47-e389-375b-ba3c-9a3efb4e218c | -7.8038 | -41.248 | 2025-09-11 03:55:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7533f413-f470-3af9-b2c7-50d7dabc24a0 | -8.07348 | -50.17667 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e959203c-1f49-379b-b249-eb816fe67b7e | -7.16564 | -44.13355 | 2025-09-11 03:55:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 347b8dbb-3ab2-3862-8746-bb0310cb1f13 | -11.38004 | -43.5236 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17a99521-0792-3485-aeeb-9adb2ce1949f | -12.12469 | -44.86662 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b20e7dbc-e3f2-34d2-a11d-5db6070cef54 | -7.5394 | -44.67399 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dfda8cbf-e4ed-3912-8a01-4898376736e2 | -11.35011 | -46.50611 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6feea113-fe41-3eb1-92b1-8c6617f9513e | -11.35655 | -46.51297 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f9d0d456-d568-34c3-a3db-37a7518c41e2 | -11.7908 | -47.32302 | 2025-09-11 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85ab6f28-ffec-3183-aef0-eb68fc3fd568 | -11.48106 | -43.63875 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 678d0bd5-0532-3c51-9298-97dd60198efb | -11.70426 | -48.25763 | 2025-09-11 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8020c1f9-794c-3939-b0c4-11c448ad85ae | -6.39652 | -43.50467 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f29f58f-8367-3ff5-aac2-0ce0d458f068 | -11.38377 | -43.52423 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b68e95e-befb-3726-805a-5d4f285fa553 | -6.83823 | -45.60215 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9eabe661-0556-3905-a01f-c3002b5bc74f | -9.05549 | -47.06101 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d2092340-84c1-3053-ae29-43921c597336 | -11.45445 | -43.59124 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf347a23-f191-3771-abc9-76ec901f9fb3 | -7.26316 | -44.89985 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 94a03f3e-a26e-32a5-8135-6f2ee56ae9bf | -9.50235 | -43.16896 | 2025-09-11 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c1a83559-2b5b-36a7-a384-cbc3e3146c76 | -11.72856 | -50.64182 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| dbbbaf6d-2835-32fc-8f17-2d9d06991e9a | -6.47313 | -44.12029 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19373e7b-270f-30f4-a84c-a38730a07b1d | -13.28755 | -43.7756 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 145d3ab1-f0b8-30da-9e7a-63cfc2cab0b1 | -6.55656 | -43.97835 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b85e1ffb-a9af-373e-9f60-2a696d927d94 | -6.90447 | -47.90265 | 2025-09-11 03:55:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README22.md)
