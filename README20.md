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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f00b9f2-1def-3805-98a8-210950762a44 | -0.92775 | -47.19194 | 2026-09-16 04:12:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d9b5bd9-ba82-3740-94d6-5a41d1d0ec23 | -2.90644 | -40.39231 | 2026-09-16 04:12:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d7cb3bc0-0f5b-36dc-bf5e-2fe81fe5f992 | -1.33215 | -46.21965 | 2026-09-16 04:12:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b7d852a-ac5b-36f8-b0cc-a40ba3d64466 | -3.88455 | -40.93185 | 2026-09-16 04:12:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9f6b1679-5079-3aaa-9888-20523ef757f5 | 1.18622 | -50.94744 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7ff80791-4960-378f-974b-b6664373eb4a | 1.18551 | -50.94294 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 70286f86-744c-3654-847c-ae2531178c1d | 1.18303 | -50.95537 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b6917477-88cc-3abc-98f2-4caf48c6619c | 1.18234 | -50.96191 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9bfc2f1-c86e-3116-a278-7a3c1828ef68 | -1.2149 | -47.8973 | 2026-09-16 04:12:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c7764931-10f0-3c59-a8b8-4fac4edf7ef3 | -1.33075 | -47.7851 | 2026-09-16 04:12:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6529595b-3caf-3d5d-8b52-92e9c92f2e37 | -2.10561 | -52.04377 | 2026-09-16 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69a8ab82-6c14-3e39-93ea-71f7773fe61b | -1.21655 | -47.89419 | 2026-09-16 04:12:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a2051534-aeb7-3ef5-a37a-ffabc49d732d | -2.10403 | -52.05328 | 2026-09-16 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd2ff61e-6ee2-37f5-b19d-015cb7e54871 | 1.17701 | -50.9673 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 30c06a34-5b74-3c72-a795-c3af44fa73a0 | -1.21182 | -47.89342 | 2026-09-16 04:12:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aedf4269-10f5-3678-a79c-ef906ec57ab1 | 1.18481 | -50.93851 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 82d8bed8-3a30-393c-8379-f17fdbe349b6 | 1.1756 | -50.95831 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a87eb085-0db3-3948-9240-1772f6c7e302 | 1.92304 | -50.8291 | 2026-09-16 04:12:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2034b9b-8e48-31ee-8781-27b344f1cdce | -2.09868 | -52.04748 | 2026-09-16 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9286f3a6-6351-3fd0-afdb-051b79e9a08f | -1.2157 | -47.89226 | 2026-09-16 04:12:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06c85ec2-eb2e-3527-b963-9ae723e856e9 | -2.81491 | -48.65305 | 2026-09-16 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0525f80c-389b-3d0e-86d4-79b89367c734 | -0.97992 | -47.50766 | 2026-09-16 04:12:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3023d0b8-6b56-3317-bb19-a7a595afdb05 | -2.81379 | -48.64879 | 2026-09-16 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c1364e5-0613-3323-a926-2f9d1583ef8b | -0.9753 | -47.50694 | 2026-09-16 04:12:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cab369b5-40da-3c1a-96bf-6e5d65c38932 | 1.24699 | -50.89029 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08f5c254-d8f1-3bfb-8afa-2d528b1bcf37 | -2.09947 | -52.04272 | 2026-09-16 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c697d48-af39-36cb-ae49-5145fcbe336e | -11.14044 | -40.48616 | 2026-09-16 04:14:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| be7d593e-db99-30b0-b5ac-67f5b830fea7 | -2.91848 | -50.41952 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6223e384-6441-34f7-ba8e-8b7b8eee076c | -2.88761 | -50.43605 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bc2028b-8aa1-342d-b8cf-9de8e3c23dc2 | -8.09978 | -42.94773 | 2026-09-16 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bbde267c-184c-3118-a74d-98e018aacf0c | -7.17586 | -41.81419 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b851fc04-d024-3e8f-8e19-579a11edad17 | -9.33716 | -44.39002 | 2026-09-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e7847ab-ccc3-3677-bcc2-5bb4ddf3bad4 | -4.67555 | -42.09082 | 2026-09-16 04:14:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab355eef-5447-3cec-96dd-4d0d47c2b442 | -3.15358 | -49.22251 | 2026-09-16 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc05f823-f3a6-3ba0-8859-3e14909df93d | -10.82084 | -46.17847 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8326724-9ec8-3131-942e-c1fe9088d990 | -6.77722 | -42.97445 | 2026-09-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c0791ba8-58b7-3b35-9f5c-30e5569328cc | -5.71642 | -46.19726 | 2026-09-16 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae3592db-3646-3b88-a8dd-7b989ed5d75e | -5.7299 | -46.18914 | 2026-09-16 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d23d2de1-2352-307e-a8c9-0a61d86a91b4 | -6.18727 | -44.02977 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 018d5d2b-3dd4-33a3-92fd-0fda93996aa0 | -11.17175 | -42.79134 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3f1c4465-d3af-3d84-84a0-48ec54db048d | -4.1983 | -47.89035 | 2026-09-16 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c93d983-5e4e-30b2-9e8d-3349468b69db | -9.53634 | -45.42426 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3e369a1-a11d-37ee-8745-048da4310015 | -3.75678 | -51.1497 | 2026-09-16 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ec51f77-f368-3803-8bb4-591b3e7f9338 | -6.30341 | -41.68215 | 2026-09-16 04:14:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0255b461-8c20-30d5-8bdc-025d24a8e7e4 | -9.49219 | -45.44661 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be7f0f26-926f-3ccc-8ca4-048cb5c58352 | -7.18107 | -46.12521 | 2026-09-16 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02a163ec-7006-39c5-adec-0f6771a36d07 | -11.36392 | -43.946 | 2026-09-16 04:14:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b53b0529-babe-3e81-bee4-81f98457b56f | -6.10982 | -46.10583 | 2026-09-16 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d56b8c5-339f-3b0a-b5c9-927ad471e7e7 | -9.791 | -46.48607 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b7ad138-a3d1-3a22-be5f-2f723765c1f2 | -3.48123 | -54.68426 | 2026-09-16 04:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6adca8a8-3a64-3f32-b8f2-dfc82e91c53a | -2.86612 | -49.63185 | 2026-09-16 04:14:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 333afc0e-fe30-3a1a-a625-3d80692be915 | -6.33162 | -41.76099 | 2026-09-16 04:14:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c2f7ecb4-9ff9-356e-b514-c4e928f5632b | -7.47644 | -42.10331 | 2026-09-16 04:14:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 22f16327-a121-30b2-b460-43277f843227 | -7.09512 | -41.76554 | 2026-09-16 04:14:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 33bc0f6e-0565-3ee9-99b6-bc2e6565807c | -10.7902 | -46.20406 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2d165198-d290-3274-9407-778c51d3a431 | -7.55303 | -41.83512 | 2026-09-16 04:14:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 43514c08-857d-35ef-91ee-c520a5ec7a70 | -7.26075 | -46.1807 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d901f17f-4dbb-3247-87f2-cb49b1d567aa | -9.34058 | -44.3906 | 2026-09-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c682fc3-8d49-32f1-9afb-b0a70d323c65 | -8.47581 | -44.57626 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 884ecc05-e31d-38b8-8d81-448927c10193 | -8.84745 | -44.89736 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05dc2252-fadd-32e5-ad3c-89bd66a7a70c | -3.08094 | -50.56469 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96da8f5c-3c23-32cc-a121-aafa53128489 | -7.33881 | -44.48523 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e6668c9-4ed1-36bd-a779-a09c2cca0202 | -6.27359 | -44.14612 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 152697c4-e1e5-3bfb-8bd5-1acaf9f25cae | -8.56052 | -44.48277 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a3c6740-3fbd-3acc-8873-baeaab89f5e3 | -7.64127 | -45.83759 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e95c70a-0579-3373-8d4f-f9040cf2f259 | -5.71402 | -46.18914 | 2026-09-16 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74ab5b29-70f8-3b33-974a-c01e65120a6a | -7.44036 | -49.47306 | 2026-09-16 04:14:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87788982-073b-3c7d-b0c0-b2deba7ea988 | -9.54484 | -45.4172 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5cf89b0-efda-345d-ad82-b9986c47f05d | -11.36159 | -43.96035 | 2026-09-16 04:14:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4531285-2f22-35b3-995f-b8b94f4f8cc5 | -5.62814 | -40.8589 | 2026-09-16 04:14:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a110c29f-dbc8-33aa-ab08-be79c0ed034f | -2.90934 | -50.40706 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3277b226-3d97-3948-9dfd-4a06849086df | -6.83457 | -43.51657 | 2026-09-16 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2428977e-bdb0-3ef9-9c67-6c06c63e907c | -10.41336 | -48.66074 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b854ff8-04d2-3b75-a279-5dd111060df7 | -3.01995 | -51.34563 | 2026-09-16 04:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ade9edee-17ca-329c-8b99-f52ef1094e05 | -9.69829 | -52.01241 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c606e21c-3a78-3710-bf84-55999e6a81be | -5.7806 | -45.09026 | 2026-09-16 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 462de867-d8a0-3712-8910-f989e5e42759 | -10.59147 | -47.7581 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5fc8a26-52ea-317d-8a0c-48a279cdfbf6 | -9.96115 | -45.22136 | 2026-09-16 04:14:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df7d91a5-1a64-3e15-aca5-dba1e383d53e | -10.58683 | -45.74699 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc5489ad-dd0c-3880-85f3-085de96c299f | -11.19928 | -42.81016 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b2e8a706-9338-31c0-ad38-fb7ef2793379 | -5.1243 | -47.61266 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bbada58f-0fa3-3a4b-b185-5954e15b3bb6 | -7.10032 | -41.81996 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f33ef877-28ec-306e-b49a-57152f49f511 | -8.48184 | -38.12442 | 2026-09-16 04:14:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3d835401-5ac6-3333-ac8b-b29e1f2c1c06 | -7.13475 | -42.13777 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dc698076-6b7e-31bd-a120-b50fe40d89a2 | -11.16733 | -42.79781 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cd0a2c11-4dfb-3e81-967e-6f50811fd12d | -7.85542 | -55.45476 | 2026-09-16 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a04a1e12-b030-3e9a-bb5d-d48542b2b360 | -2.89118 | -50.41489 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bf5a4db-9598-3ab9-925a-0ad5cc009ffa | -9.54658 | -45.42087 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c1b5504e-3656-3f1a-b1be-de43150a38d9 | -4.83256 | -43.55664 | 2026-09-16 04:14:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b12cde5c-5521-3489-a7e5-2ba3490bac23 | -10.82378 | -46.1834 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6ad4adf1-8aac-32f4-bd76-b4d98b7c96d9 | -10.40475 | -48.64439 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f90664a9-c04c-378d-b55e-8ba8cad34d4f | -8.78762 | -49.40199 | 2026-09-16 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f57c287-efea-3047-a372-1567ebc5e123 | -8.62156 | -44.4922 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1b088e3-bfd0-3a4e-96bc-24a2918370e5 | -11.13696 | -40.48569 | 2026-09-16 04:14:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| ac3e1034-6238-3546-ba21-5bc73fd0f793 | -6.73378 | -43.07365 | 2026-09-16 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aefc65c1-b8a8-37ec-a3f9-44733b2d4b03 | -7.07831 | -45.2405 | 2026-09-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8abc9834-1286-3d1a-a3b3-0da58ea0e3a2 | -10.41405 | -48.64153 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b88aad6d-1650-3585-939c-68580e743f6a | -8.7834 | -45.89715 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ed6cc0e-774d-3095-ac04-55c91f5d5866 | -4.83602 | -43.55719 | 2026-09-16 04:14:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97dc9ac3-ac0e-3126-94cb-31ff45e369e4 | -6.39293 | -44.05812 | 2026-09-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README21.md)
