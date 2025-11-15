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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43281d4c-ec5d-31fe-b92f-a0d5733ab12a | -4.01371 | -48.80734 | 2025-11-15 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08d97bf9-4de0-3def-9741-3da19508e497 | -3.90911 | -45.80144 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa24c167-6496-301b-9169-ae587590f477 | -6.28186 | -44.74434 | 2025-11-15 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 391cb968-89d2-31f9-846a-2e7a2ff1b4fd | -5.04219 | -43.60897 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a5226f3e-bb79-38f5-8d26-bdb4cc433fae | -6.46328 | -45.65564 | 2025-11-15 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ed79628-979e-3a35-9e6a-a40ff8bf10bc | -4.33529 | -45.29697 | 2025-11-15 04:25:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| def26a9a-8e08-3d5b-9f3b-f1735fa80567 | -6.16206 | -48.04679 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c13312e7-3af1-36e6-9878-435504d54475 | -5.27338 | -44.10142 | 2025-11-15 04:25:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26289246-94dd-365a-b668-5d3ec2d40756 | -8.38491 | -45.81325 | 2025-11-15 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e67c5700-3d4d-3f52-8137-4fb89be034d0 | -5.08863 | -43.28896 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0a54b57-7233-353b-a069-b74bc1ecabb0 | -8.10716 | -40.88058 | 2025-11-15 04:25:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f7c61fa2-171f-3ab1-8c25-cd74f20f95c0 | -4.10481 | -48.01721 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4cf9a8f-bf5a-3fee-a134-0909686f44f0 | -3.8776 | -47.17724 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e81d34b-5db8-393c-b0ce-ff0e52b99c93 | -4.46385 | -45.64609 | 2025-11-15 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7d4d0a5-8242-3160-8a26-648df84301f4 | -3.76125 | -51.95782 | 2025-11-15 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4485991f-8992-3b0e-987a-e077c21c8531 | -5.23437 | -44.35121 | 2025-11-15 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 217554de-323f-3548-96e9-69362bfad759 | -9.12035 | -50.30621 | 2025-11-15 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44e7cd78-032c-3b34-ac7d-e4938ee01d86 | -1.8338 | -53.80141 | 2025-11-15 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56b3df0f-888d-378a-86e9-a55dd6834b70 | -9.75331 | -43.97651 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 936732c7-761d-37b5-a8c9-84d05e90e095 | -5.44678 | -49.46275 | 2025-11-15 04:25:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 496bfbb9-204a-3125-99a5-8f88a403e52d | -6.28473 | -41.76164 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2767fce9-93ed-3a99-bfce-fd07b3a32ac1 | -9.66556 | -43.89968 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 577e7151-321f-37eb-acd5-8b625f8e9282 | -8.45873 | -45.13884 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaed34d4-5acf-3d41-9c31-60cbe63acfce | -6.27602 | -41.74029 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fbe7272f-e1c7-3318-9715-1f511412c517 | -8.99892 | -44.18423 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f952608-3dea-37e9-8a83-724ccc4f175f | -3.46025 | -50.11698 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 606642ab-2469-321b-bae9-4e6b346a55a3 | -4.22441 | -45.48469 | 2025-11-15 04:25:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62c990ee-26af-326b-b7cf-71d1dc29f669 | -7.07922 | -46.55467 | 2025-11-15 04:25:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21f04209-61ee-3cb6-b117-e697256fd6d2 | -3.31919 | -45.68748 | 2025-11-15 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 296d78fc-9850-35de-a171-06b852d0dc6e | -5.2338 | -44.35484 | 2025-11-15 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 1666825b-ba2d-3abc-b7b9-6d34bd53bf34 | -3.89108 | -47.17941 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 294c4d3a-3ffa-3836-aa52-e4afd3912d5f | -9.05862 | -48.85862 | 2025-11-15 04:25:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bce11d0b-9cb4-3e2d-9bbf-b9269c3ef4f2 | -4.88552 | -49.38831 | 2025-11-15 04:25:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e5718a5-edc2-3d57-8abe-b57b102e8c30 | -3.71007 | -47.6332 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| b48ab35b-b9e5-39de-9bc5-9ae1c23d71c8 | -6.4805 | -43.9531 | 2025-11-15 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a5fbf9c-d649-3008-9dea-23f225315de3 | -8.58495 | -46.07467 | 2025-11-15 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91255a5a-4f97-3722-b5ce-a0e84ab82bee | -4.47217 | -46.43103 | 2025-11-15 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34871934-a71e-3608-aec7-2cd78819d315 | -6.7331 | -42.96369 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4e5cd479-7aff-3cd5-9b92-fda149a52825 | -4.81114 | -41.6102 | 2025-11-15 04:25:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5832e491-6946-3116-bc71-a79a0e8cb113 | -2.79956 | -52.96468 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa6f25f7-5338-3b22-959b-dff3376b9de2 | -5.17895 | -44.23782 | 2025-11-15 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 773d625a-97fb-3ef1-8cb0-76d9e276388d | -4.60602 | -43.29886 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1fcaa43-7ca0-3afa-b12a-66980a133788 | -3.99044 | -44.26516 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57a166d7-d531-3259-9334-508281fe9730 | -7.45966 | -42.55941 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4b3ba588-94d2-31d1-ad51-ee9c1b7bf3e6 | -3.09602 | -51.10217 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9916fa5e-379f-331b-af89-133f0c0783c9 | -4.24523 | -48.38681 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c84efad2-4b23-3c1e-ad8b-82faaa050f8d | -6.70756 | -42.95975 | 2025-11-15 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 819785b2-1eca-3d96-ba7a-37303c55726b | -5.5122 | -44.39307 | 2025-11-15 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23e0dc72-1a78-341c-86c4-69585a31d3f4 | -4.36108 | -47.57618 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e8e05e1-5bb5-30ee-b53e-60443e75b1f3 | -4.75776 | -50.6879 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da757136-44a8-35dc-baee-ce788a3e7296 | -4.38568 | -50.42938 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e3eb9228-ccaa-3ad4-85e5-9b63642f27c0 | -3.36758 | -45.44522 | 2025-11-15 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4da8c0cc-63e3-3781-bb08-7d22cd3752bf | -3.87289 | -42.79498 | 2025-11-15 04:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4464ee91-f869-3e90-bb54-cc337f837567 | -7.71093 | -49.38409 | 2025-11-15 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db7ed9c4-4afa-302c-ac49-14917cd5dac5 | -3.53118 | -52.99829 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c84e47f-4151-3153-b789-71754bbfc93e | -10.10874 | -40.8952 | 2025-11-15 04:25:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b225d0ae-f2b6-37b6-a13f-851012ca1d72 | -8.74457 | -44.23695 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13af91c4-143f-3183-9747-ee67885af738 | -2.51121 | -47.8089 | 2025-11-15 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6209dd3-8439-37a8-9ea1-2a60bd3c130b | -7.07961 | -41.58401 | 2025-11-15 04:25:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e2009e88-3008-3b31-81bf-72d0addbdaf3 | -7.42165 | -45.2343 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56435d5a-3033-3541-9959-3727b994777a | -5.72852 | -46.54501 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e320049e-af34-32e8-84ae-327f970faa50 | -4.58738 | -44.31934 | 2025-11-15 04:25:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d5ce1065-1185-3008-bdbc-1c56afe32b94 | -7.39878 | -41.00766 | 2025-11-15 04:25:00 | NOAA-20 | BELÉM DO PIAUÍ | PIAUÍ | Brasil | 2201572 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ed4efe12-54e3-3dd3-97da-3d72d221c232 | -7.2921 | -45.11219 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb64b799-a1ac-3a2e-a53b-3d9506060a70 | -5.08281 | -42.65293 | 2025-11-15 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f425825-0680-3924-a181-8f375b705146 | -7.10002 | -42.73853 | 2025-11-15 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2f600896-4bf6-3d9b-abdc-e52d86eac53f | -10.18282 | -44.38562 | 2025-11-15 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 548efe36-63a7-3b3c-90ba-d973fa23bb79 | -5.77595 | -44.38475 | 2025-11-15 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9b80d81-ea70-3a29-8e71-d4ed9537ebd5 | -3.65256 | -44.79937 | 2025-11-15 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f53bd660-9b0f-32bf-9b94-f9fc0ae0ceec | -4.60992 | -48.34669 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbaea284-b3ba-3ea9-afe9-1a5c47cdce28 | -6.26022 | -41.41309 | 2025-11-15 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ed568218-ec2f-3c0f-b038-ec7a3b4ad172 | -3.46106 | -50.11211 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d76e7be-a368-399e-bb49-f2d65f516a0a | -3.78974 | -45.97645 | 2025-11-15 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 111f52e7-8a39-3790-b94c-58a24cf5900d | -7.44005 | -42.76475 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 24b8ee31-3e8a-3295-858b-d341eb13b376 | -9.75754 | -43.97286 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27031077-705d-3e01-b980-cbcdb41e6784 | -5.36941 | -44.07041 | 2025-11-15 04:25:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c603346-6022-30d2-90c9-ed5d410e8cc9 | -6.07699 | -41.6511 | 2025-11-15 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e4d99587-2c24-34d0-8c02-7042217b8d81 | -4.64877 | -46.85881 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 901ea317-d089-3b73-bee3-afe6249318a3 | -4.9077 | -44.04307 | 2025-11-15 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 890f6ee9-eb6c-3960-942c-6997389bf3cc | -4.0044 | -47.67835 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d0b786d9-e947-3f31-a071-58244014ea0c | -2.57529 | -47.49258 | 2025-11-15 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2ce8f7e-6744-3878-93e0-1097feb68489 | -6.81541 | -48.82814 | 2025-11-15 04:25:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 936f888b-11da-3c2b-a6f2-765376bf71c4 | -4.06514 | -46.42688 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61e206cb-fa65-3c67-833f-3a9e3e31abcd | -4.20248 | -48.56269 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5a868df-c8e2-3eac-b5cf-92f58c599c46 | -9.66903 | -43.09528 | 2025-11-15 04:25:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 769bb4b5-04c1-3d48-8246-9f5db435716e | -4.80351 | -45.43061 | 2025-11-15 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3220cd2-97ff-3d9a-b46e-1c5366e4c99d | -6.17341 | -42.13579 | 2025-11-15 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f61775fb-86ad-33d3-a15d-30c96f63eacc | -4.83803 | -44.75695 | 2025-11-15 04:25:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8e2d7ae-731a-313d-a2fb-3cc59abf0440 | -3.53643 | -45.27787 | 2025-11-15 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18eb70aa-0542-39de-a363-5518606db2d6 | -9.75036 | -43.97178 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51a398a2-a37b-3570-a4d4-93aa6133623d | -5.09388 | -37.78622 | 2025-11-15 04:25:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3d6fdeed-3a97-3b4c-92f6-1fa1177f3058 | -9.48837 | -47.28577 | 2025-11-15 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 836ff131-30ab-3401-aafc-e89d0c7f6b73 | -5.5175 | -41.77039 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 12017d1a-a55d-3ff0-9904-107f657886cf | -3.35563 | -46.86885 | 2025-11-15 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97272038-613d-3841-89d8-cbc7a04c94aa | -4.17377 | -50.42416 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4af7371-71b5-37ac-9702-9355fe2132b4 | -4.80965 | -41.6198 | 2025-11-15 04:25:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea4c2b20-b822-389d-bbc1-55b06474291b | -4.64599 | -43.36474 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd18c767-e13f-30de-bf93-8845dd2cea4a | -2.73743 | -45.3038 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db8e8843-1a39-32c4-b3e6-59787c888f17 | -4.29633 | -45.99646 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48335506-e613-394e-a402-9ba0535f0d1d | -3.52878 | -56.32431 | 2025-11-15 04:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README42.md)
