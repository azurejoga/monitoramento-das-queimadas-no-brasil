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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9668a793-763b-3d90-92fa-36a4bf17106d | -12.07528 | -47.59037 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a799d13-83b4-32b5-9ff0-ed4b7f0a33ef | -7.44725 | -51.83608 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4efa04ff-cede-356d-85d4-9df588824493 | -11.37376 | -43.5096 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e04ee066-9250-3c27-a555-19832652bb54 | -6.86921 | -51.97053 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a8e03bf-996d-3d8c-a657-36422716c17d | -11.66824 | -46.60989 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 098761b0-a54e-33e9-b095-daa15e96a5c5 | -11.5254 | -50.61046 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b11f190-40f7-339b-892a-3bffead30724 | -11.14627 | -45.23959 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 829588e8-d23d-3af1-9399-95e384a44cb8 | -10.40769 | -48.58969 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 730fbffc-05f3-365a-9d8f-bf5c7a148af2 | -12.10602 | -44.86557 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd687c96-8a95-3c54-9aec-47c1a85045bb | -9.34318 | -48.94768 | 2025-09-12 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30f75b32-64c0-3cbc-86b1-b26854425db9 | -6.57256 | -42.93612 | 2025-09-12 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7550f49a-cb4f-32a6-9a92-0e36b45a4767 | -9.93904 | -42.32872 | 2025-09-12 04:25:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5be6a7a8-71ce-35bb-b8b6-9c2bfa3760ac | -5.32399 | -55.88839 | 2025-09-12 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3421b273-c918-353e-b0e0-6e6a2637f2d1 | -8.17699 | -46.09991 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 678d34bc-876d-37dd-909a-1a28fcc34a57 | -6.28007 | -42.40689 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2534482d-0ecd-3fd0-9572-1a9f5febeb37 | -11.15548 | -45.31332 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e922923-fd64-3e0e-b095-302f595a7acc | -11.69874 | -46.56733 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0a6a25e-378a-3d7f-b4bd-1d635bdaca27 | -7.30159 | -44.35595 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8e144f4-ee02-3a2c-801f-00edb79950c7 | -7.15121 | -48.90156 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 941c17ce-494a-38b6-afdf-f20367b73c08 | -6.88235 | -42.83686 | 2025-09-12 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 044c017b-4b69-3516-8aa3-886c5ec5242a | -9.00621 | -46.11512 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af6066c4-7157-3e34-a485-b7cc94b3685f | -8.95331 | -46.06316 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b62ebffd-5858-36bf-87bc-9f5bdac361a3 | -7.6214 | -46.54618 | 2025-09-12 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d6ce431-dda1-3dec-bbb1-7f2b9e07297f | -11.85928 | -46.75673 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8566cf3-c578-3ef0-ab76-980ec9f654b7 | -8.57904 | -51.34903 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f10cdfbe-3faf-3ee1-b1ea-05c8d331adbe | -7.22079 | -43.97587 | 2025-09-12 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c857ebf0-9a41-3327-be50-2a8fde4b9151 | -8.0636 | -52.31996 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d45e6a1b-61b1-3698-a85b-4febc5cd51d3 | -11.66213 | -46.60525 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a98d432-ead6-3e69-8199-8049e3406a7a | -6.82118 | -45.65105 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b80cd339-ac91-30f3-a772-6e8552a377fe | -9.89623 | -51.88121 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e77f7768-6076-30a9-a38f-82c417a7e6f8 | -8.08575 | -50.19193 | 2025-09-12 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7e951d82-6c30-3d9a-83f5-22bb447e5c9a | -12.11133 | -44.85391 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0b7ae09-e824-3a10-b8c8-a4f69ca41bee | -6.87801 | -42.84073 | 2025-09-12 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 81584d6a-6f06-3cf9-b810-ef5a05cc1e75 | -10.53675 | -51.5288 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ab158e72-4093-330a-9f65-e2ad076703b8 | -10.42099 | -50.59605 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59aec8a1-53d2-3599-a10a-c181279fc979 | -11.70147 | -46.50553 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09e94614-3a51-307f-869c-93d8f6cb79a5 | -7.91199 | -44.87471 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3befb045-244a-3b9d-9ff1-796b8eeccae6 | -10.13905 | -47.91052 | 2025-09-12 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c813fac-69d3-3286-b4a6-3506c40bffef | -10.12297 | -47.90429 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9efc05a6-672f-3faa-95d9-e71d41aff221 | -9.06713 | -47.11189 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 649c946b-b47a-3120-8c03-8276d5b6b212 | -8.94646 | -46.71424 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4993c462-86c0-3a28-975b-650d4c916ccb | -5.76164 | -52.37535 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b1fbe22-9c13-37e4-9fbf-1b4633257fd2 | -10.67997 | -48.64456 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26d99f26-b120-3b24-b060-d83632e32152 | -9.8081 | -47.81305 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45c66f60-b30b-3d7c-b845-953a48e0fc27 | -11.67212 | -46.60688 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adcaa221-9980-3c47-8088-4d843b61d05a | -8.02249 | -45.41053 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c9969653-dcf0-3e96-8db1-42e871d3ed61 | -11.69321 | -46.603 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50438d2c-e3c1-33f3-af74-3d142536ffe0 | -6.31185 | -42.22491 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4a175373-1b2d-37f4-a88c-aef75f2218a1 | -6.44774 | -44.78386 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8368706c-9ab7-344a-ac37-100eb281c5f8 | -12.07749 | -47.59795 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2bdd326-c0c9-303b-ba65-a9b4559f042f | -11.68369 | -46.53205 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e223c5c2-b4a2-3c6b-b6ac-1c1d9522c4c5 | -7.06981 | -43.90176 | 2025-09-12 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d693d04-b9ca-3cce-8abe-3866660d9fd7 | -10.41341 | -48.5756 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 692f5b97-7658-375c-8b95-f652e1187493 | -6.62634 | -44.08162 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3fa54b6d-0f64-33a8-ac9b-a5d695d71669 | -11.66268 | -46.6017 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a56c5a9-7dbc-3921-93d9-f680c97f667f | -9.21586 | -59.39063 | 2025-09-12 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| de08097a-cb9b-3867-a873-b15da6c0091c | -9.11783 | -46.96302 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b42935c-6183-3ff9-9619-28ccbed9d8a4 | -10.5646 | -52.02322 | 2025-09-12 04:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f41cd0c-30cc-30d3-9428-262738dd3dcf | -10.67938 | -48.64819 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d67383f9-0cf1-32f6-82d4-09f0455a5bd9 | -6.17179 | -41.04271 | 2025-09-12 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 948393c1-727a-3c8f-bb3e-31a23adecc1a | -6.36168 | -42.54304 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| be26f6e4-be11-30c3-b0b4-509fbe3277ee | -12.08964 | -47.5855 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bfaf560-bbbd-3485-bf5e-ed58a6d1409f | -8.89539 | -49.93741 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 17dfa38c-cced-349c-8ef2-9b544830b9ec | -6.74944 | -45.93583 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 758d0d18-27a4-31ae-89cf-a6227f920dfb | -10.37473 | -48.30288 | 2025-09-12 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0aab2e70-a9af-3a54-9779-ffa820c1d932 | -8.04474 | -44.5078 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82d04671-022a-3d39-baf2-638096082565 | -9.87796 | -46.4688 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de49f542-490f-3f3c-8ae3-687fab94ec7c | -11.52107 | -50.59241 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 204fcddc-e65e-3083-a19b-3bb772be0803 | -6.47861 | -46.01715 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 416c8af1-7cb5-3023-bace-1b5a72a98f51 | -12.00002 | -47.76562 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35755b40-4fe8-3c4f-beba-76933b324ed7 | -8.643 | -55.25057 | 2025-09-12 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6513b0c-4d46-376d-975d-c9d45e059237 | -12.10251 | -44.86491 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30cbaa82-2359-39cc-bcbb-65258ce5b376 | -11.70038 | -46.53469 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63685764-dcda-3e69-9bd5-90d79060c456 | -6.82295 | -52.79958 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ba0e43a-1359-3c6c-ae48-6e5620bcc07c | -11.1514 | -45.2985 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22f730e6-950a-3486-8499-f859446cc334 | -12.09129 | -47.59659 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ad28e3bf-d950-3221-a7be-9bbb1dacdd37 | -8.93206 | -51.07595 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9a3aa1e-ce03-39cf-8750-33e376c3cc89 | -11.70203 | -46.50196 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 023f144b-0e98-381b-a0e3-1cd8a7409e64 | -9.03348 | -47.08865 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be8e9488-fc76-37e7-bf30-e7c5ea580d98 | -10.70465 | -49.16062 | 2025-09-12 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77e330ea-0662-3256-bf4d-c21d41367c7a | -9.05776 | -47.04251 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ad5241dd-4810-3704-b3c9-2b18488aa4d4 | -10.39202 | -50.49997 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1a4e7c9-e7f7-3778-89c6-99a2237e5c74 | -11.16978 | -45.31178 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e153e165-07c5-38e2-b9ee-dc92f5e87c4b | -10.40689 | -50.02106 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96bfe731-515f-3bc9-8736-8600e61233a2 | -10.38587 | -48.57486 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97eb3251-3bed-38bc-8ba8-2d7d83befc24 | -6.15257 | -53.68787 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c3d47ca-3220-3d4a-893d-13d6ad5bda09 | -10.67476 | -48.59151 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f8b2285e-32e6-3af7-9fdf-393517ffb866 | -6.14697 | -53.69205 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2b2b304-0b1d-323f-98a5-c67f5263f9d7 | -9.97171 | -51.70155 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 152c4493-2644-3b64-8992-bd2632384f66 | -7.21729 | -43.97537 | 2025-09-12 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcc742fe-c5e2-3cf8-8143-7f357946fc23 | -5.65471 | -45.94395 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0c92f56-178b-3762-9eb6-82d2704188ca | -8.07142 | -42.94933 | 2025-09-12 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6da8d07b-cd35-3519-82c5-4b94eb80a685 | -7.14974 | -44.34509 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c8c2d8c-0869-31de-b302-0f2edfbd8e6c | -8.87967 | -49.56583 | 2025-09-12 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca44497d-e779-3de5-9bd5-f1cb32bbc215 | -11.67381 | -46.61806 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a740eef4-7200-3d05-91da-0125493c7d34 | -6.68858 | -44.1299 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cbef7f6-9d13-3d5b-91aa-c91580d428ec | -11.69703 | -46.51217 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2137b484-35ab-305e-a570-39d1ae66c131 | -12.12192 | -44.85563 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8344d22-b2e6-37bc-a11e-5c359d50b586 | -7.29814 | -44.35542 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 299485d2-4311-3927-b00d-7b2eef652e19 | -11.1069 | -51.98372 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README74.md)
