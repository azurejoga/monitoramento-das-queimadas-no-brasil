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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7892114b-96c7-37d3-938a-591343bf4530 | -4.38798 | -43.47556 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e3bef5e2-4b26-3481-8b70-cc920a1d7898 | -4.38786 | -43.4727 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c8429a6d-7214-34a1-bda5-a8867308ef52 | -4.3849 | -43.47041 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 27d5fc6d-fd32-3023-8501-9cbdf852957b | -4.3848 | -43.46756 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f1f708a3-f07b-3a66-ab1f-2b72f9b8fac6 | -4.8168 | -44.35465 | 2024-11-01 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6194568-d70c-3266-9911-eb8e25f821a3 | -4.57526 | -44.63737 | 2024-11-01 04:29:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5629092-7500-3a67-8d35-47d450ca8f39 | -4.55993 | -44.41219 | 2024-11-01 04:29:00 | NOAA-20 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03e522c6-4b0e-3406-8b27-a9bc85467a5d | -4.44908 | -44.16356 | 2024-11-01 04:29:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 237a6487-0b02-3ac7-8b7e-25ece2e958f9 | -4.44843 | -44.16778 | 2024-11-01 04:29:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 266c01b5-ea48-3805-9898-b42e8ef9740e | -4.44545 | -44.16299 | 2024-11-01 04:29:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 461e861e-11cf-368f-a1e7-de195bbd4f25 | -4.44481 | -44.1672 | 2024-11-01 04:29:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf1867ea-c229-3998-b3b3-80b07fa2904f | -4.44183 | -44.16244 | 2024-11-01 04:29:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0d41777-9aee-3f7b-8e42-ab9677706603 | -4.44118 | -44.16663 | 2024-11-01 04:29:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cf2cdaf-265c-3eb9-b609-0bb298525c4a | -6.11432 | -43.95634 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bb5dfeb2-1c57-3159-8235-81926ba0d501 | -6.11363 | -43.96092 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d958188e-f991-3c68-9f3a-1094470c62f5 | -6.53625 | -43.95516 | 2024-11-01 04:29:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d86ed50-06b5-3410-80dd-b8af9bd2b6c8 | -6.53559 | -43.95962 | 2024-11-01 04:29:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43c40b07-fb1d-3237-b38e-29d8ad41ee9f | -6.13236 | -43.96365 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e87a5c8f-fba8-311d-9f7f-a80c1610520a | -6.13167 | -43.96823 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73f89c7e-4c1e-38cb-bc3d-ac40a3a27fbf | -6.12488 | -43.96249 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 829d7ac7-b410-3f3f-96b3-8621e89070e0 | -6.12044 | -43.96648 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e846005c-65ae-3d5c-b01e-99eef0206f3a | -6.11807 | -43.95684 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c2826bf4-50b5-3fea-8a8d-cd6fce1043eb | -6.10988 | -43.96037 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c17b056-8dbd-3b32-8155-968b395892db | -6.10682 | -43.95525 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd79013b-13a8-3f2a-aacb-239ad14d6f8c | -6.10614 | -43.95979 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b24b7f6e-5ac9-3db8-ab5b-f0e8fcc90bc1 | -6.10308 | -43.95467 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 000b7c0d-aac3-3c24-adc2-de711640bb1b | -5.62406 | -43.95444 | 2024-11-01 04:29:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3eb5736-78fa-3fad-9c75-5a10efd6e532 | -5.621 | -43.94938 | 2024-11-01 04:29:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc321a8f-ee34-325a-a524-30df1195792d | -5.62034 | -43.95387 | 2024-11-01 04:29:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9943753a-c7ba-3344-86b3-9f685749096a | -5.54574 | -43.93129 | 2024-11-01 04:29:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 851bc14c-f635-3d01-88fa-5511a348f76b | -6.26134 | -44.96316 | 2024-11-01 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a26ec46-514d-3d0c-bb53-6263ab32f0f3 | -6.14835 | -44.75072 | 2024-11-01 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2fae771-02af-39de-88fe-ea71ee4eeaf3 | -5.52958 | -44.83061 | 2024-11-01 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb278d21-5ddf-3728-8302-d1f4b2cbfd1e | -5.32156 | -44.86676 | 2024-11-01 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ad09816-a707-3f78-9b42-f6f2703163fa | -5.27921 | -44.31166 | 2024-11-01 04:29:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dbbef00-42d5-329a-8b0f-95cfe71fefd8 | -5.26404 | -44.7235 | 2024-11-01 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4349cfd4-3986-358d-b66c-6b706a6d56ab | -5.08406 | -44.04407 | 2024-11-01 04:29:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c725b3b4-9052-3bfb-97ae-1cd67b103763 | -5.07091 | -44.2307 | 2024-11-01 04:29:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5589e37d-7740-39f8-b301-99d44ab47396 | -5.07027 | -44.23493 | 2024-11-01 04:29:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08ad37d8-237c-3f59-93b9-1289d51e485a | -6.13305 | -43.95911 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0ea11d2-6983-328c-bf28-006de4c8178a | -6.12419 | -43.96706 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23048277-456c-369e-ba0e-b3ffd0cd4e72 | -6.11738 | -43.96142 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 49383df6-ce4c-38d1-8e58-9403ef3dd2d5 | -6.11295 | -43.96543 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| adaabd01-29e5-3608-8e61-8de66cf5caf7 | -6.1024 | -43.9592 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 094dc211-84de-3496-ae07-e2eaf046cc88 | -6.12113 | -43.96193 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17a79a18-c975-3956-b27d-ccc8f5b79ef8 | -6.1167 | -43.96595 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 09ad5b3e-47f4-3999-b2b7-838dace1e8a0 | -6.11227 | -43.96989 | 2024-11-01 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04091fed-fc7d-3369-a13e-c1cee37910a9 | -6.39961 | -44.76602 | 2024-11-01 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 290ceeac-a424-32d7-861e-9dacf1368ca4 | -6.08644 | -44.83035 | 2024-11-01 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96c4f4ff-fd51-374b-a8f6-71e32bccde17 | -6.63079 | -43.7855 | 2024-11-01 04:29:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9d4cbaf-60f7-3541-b63b-b662f19f5e0a | -6.53074 | -44.4641 | 2024-11-01 04:29:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dce5aacf-300b-363b-be7c-1f686424bd04 | -6.52707 | -44.46359 | 2024-11-01 04:29:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 000d22e5-15b5-3161-bacd-8b52a2ae8c01 | -6.53807 | -44.46511 | 2024-11-01 04:29:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3598b449-a4fa-362c-824a-e895067e5770 | -6.53441 | -44.46461 | 2024-11-01 04:29:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ca001144-8b00-3775-9dbd-3bb565afd56e | -6.53376 | -44.46893 | 2024-11-01 04:29:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c406d0b6-4c81-3b66-8855-b877530f67b0 | -6.53009 | -44.46845 | 2024-11-01 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bad82b2-322c-3dfa-ab9b-ec80e69cedec | -1.98442 | -45.61542 | 2024-11-01 04:29:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfc22567-4ff4-3a03-a026-f4c89cf238e0 | -2.62365 | -45.14367 | 2024-11-01 04:29:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8078073-f1e8-39c4-9d83-e88d815162db | -2.62308 | -45.14735 | 2024-11-01 04:29:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30be419a-50d9-3f08-820b-8a3d8b653362 | -2.62024 | -45.14315 | 2024-11-01 04:29:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfbfd815-9b42-345d-88b5-013ef4e00d62 | -2.56884 | -45.33375 | 2024-11-01 04:29:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 327d10e0-3217-3a45-b751-3de71ca87908 | -3.4688 | -44.93605 | 2024-11-01 04:29:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 769dfa38-b58e-3695-93ed-9a7483716e9e | -3.37064 | -45.91129 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 769f611b-b645-3ec4-b871-285b79ae0763 | -3.36201 | -44.78729 | 2024-11-01 04:29:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 623e3ebe-8135-38f8-b6f8-8e2273024fd9 | -3.33727 | -45.40073 | 2024-11-01 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e27529d8-1cf0-315a-90c5-653e5caf0eaa | -3.28305 | -45.97384 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b539e819-4365-3d1a-bd7e-575fca088a70 | -3.27694 | -45.71435 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55575169-b902-3081-b3f4-eecfed928293 | -3.2698 | -45.79358 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db44bb2b-b874-3a90-b131-e3943e6d8ca1 | -3.26051 | -44.55437 | 2024-11-01 04:29:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01de827f-9714-3c08-ab6e-920181316436 | -3.25238 | -45.97271 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ff85fdb-719e-36e1-9685-9c367c45d75e | -3.16176 | -45.31106 | 2024-11-01 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0189dc1-76c6-3aa5-bc14-de4a8c327a98 | -3.16119 | -45.31473 | 2024-11-01 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca651c03-8711-365a-b7ec-76e06fded1c4 | -3.15607 | -45.52664 | 2024-11-01 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0297cc23-816a-3f6c-a48c-90d6a6110980 | -3.1555 | -45.53026 | 2024-11-01 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28868345-d9c8-3f43-b167-a599d32046cd | -3.15268 | -45.52613 | 2024-11-01 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8bb391f-09d3-3cad-a115-b55fdf76dc08 | -3.15098 | -45.38066 | 2024-11-01 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c0d288b-a17d-3999-b69e-bf415f819e66 | -3.15041 | -45.38431 | 2024-11-01 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d05d20b2-822a-3e5f-a2b0-4c9eda55d55a | -3.12259 | -45.11239 | 2024-11-01 04:29:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa3dcfef-db92-39c6-b18c-e29da8ee2b7e | -3.11916 | -45.11187 | 2024-11-01 04:29:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 10a11bee-eb4f-3cc4-a661-fbd324b25d77 | -3.11858 | -45.1156 | 2024-11-01 04:29:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7f0b6179-928c-3910-ac25-f4b8534c39de | -3.11573 | -45.11135 | 2024-11-01 04:29:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 43d6b6fb-50bb-3849-9abf-08626178f043 | -3.11475 | -45.2967 | 2024-11-01 04:29:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82398b49-9bf3-328d-9547-90ac73ffb189 | -3.09467 | -45.56533 | 2024-11-01 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9614079a-afc3-3468-92a2-567fa840ca36 | -3.09411 | -45.56894 | 2024-11-01 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c213ae90-4506-31ce-a114-d1274c47da35 | -3.08854 | -45.93711 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2ad8c14a-5d97-38ec-9988-d8820aa39730 | -2.31425 | -45.73831 | 2024-11-01 04:29:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0bd9b92-7743-3932-a2ac-e315d193f080 | -2.3109 | -45.73779 | 2024-11-01 04:29:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93018112-1a79-339f-9f8c-a7b125d68c14 | -2.98779 | -44.3982 | 2024-11-01 04:29:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccf23d93-1544-3e6b-8e78-a093b0e22d0f | -5.01136 | -45.83658 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0359996f-4437-340f-934c-12aa7b1f3e08 | -5.00796 | -45.8361 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8e723fe-beec-32ff-be7f-4d83c2256121 | -5.05366 | -45.53674 | 2024-11-01 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a85d9492-3601-3f38-be2e-c9679e98fb5b | -5.05023 | -45.53621 | 2024-11-01 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbd05ece-833c-379c-a1fa-0de277852f3b | -5.02361 | -45.25449 | 2024-11-01 04:29:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aeaab609-ddca-33e5-9b7e-52426dc3b062 | -4.31425 | -45.63047 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fb89744-adb0-33a5-a56c-f06078cc9308 | -4.31145 | -45.73833 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcc3ea4e-c1ab-3880-9ffa-863886bde5d4 | -4.31027 | -45.63368 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0514532-f528-3ae4-b7ad-091752ea7dc2 | -4.30466 | -45.71494 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29096935-b069-3337-80a1-f61349097e07 | -4.30127 | -45.71441 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cb6fbaf-fc0d-31b0-8c9b-34081a1e2e5d | -4.29789 | -45.71385 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39235c39-6246-3c60-ba4f-c53383fb8128 | -4.22097 | -45.82133 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README27.md)
