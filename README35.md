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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf82c222-9415-33c7-bbdd-54308e8dd7b4 | -5.69864 | -49.27328 | 2025-11-05 05:03:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56144ea9-22f8-37fc-a449-fb40d5bf4a0d | -6.86323 | -50.10085 | 2025-11-05 05:03:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ab12cdc-bf42-3232-9591-51d3ab9cf2b0 | -6.54992 | -44.47168 | 2025-11-05 05:03:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edaef8d6-960a-3c0d-8814-268fdace686a | -9.05237 | -50.29469 | 2025-11-05 05:03:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fae18f3e-a5b4-3f94-abf6-25940583c663 | -11.84631 | -43.7197 | 2025-11-05 05:03:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f82e0729-e576-3491-8ce9-59bf188610e1 | -8.09236 | -42.94827 | 2025-11-05 05:03:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 68f429bb-3496-38c8-be54-c7434ec54b31 | -8.05753 | -49.63738 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf9c809c-04b5-39b8-90d2-1b5febb23637 | -10.38078 | -47.74938 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f8af73c-2108-3736-abf4-9f6c3ebf048a | -10.37991 | -47.75594 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69edb84b-57a1-3b24-85c7-4b3f7380c4d1 | -9.06149 | -48.83226 | 2025-11-05 05:03:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df7ba61b-5f94-3faf-bc6f-7812b8140a70 | -9.59182 | -54.72393 | 2025-11-05 05:03:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0f02511-63af-3b71-9c5a-cd45ac1c6ef3 | -9.08868 | -50.6189 | 2025-11-05 05:03:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca3650fa-0f5e-39b8-9f2c-e8ed1bfb1613 | -10.98061 | -59.09694 | 2025-11-05 05:03:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b18d33f-5428-39c6-bc47-a17a981b958c | -6.62194 | -55.02071 | 2025-11-05 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0aa7ae25-49e7-3984-adad-858875f70881 | -12.02224 | -45.69092 | 2025-11-05 05:03:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bb12ea4-93de-361e-8f49-5b20899f657a | -11.84563 | -43.72597 | 2025-11-05 05:03:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc340826-b0ec-3750-bb5f-cb64c02b4107 | -7.32726 | -47.25417 | 2025-11-05 05:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35b16895-65e1-3eb3-8e40-53d449e1df45 | -8.23219 | -49.98779 | 2025-11-05 05:03:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 315cfec5-cd40-3476-b058-eed3af5087a0 | -12.40139 | -49.89788 | 2025-11-05 05:03:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 973fb688-6c19-36ef-96fa-ed78b20c032e | -5.69803 | -49.27747 | 2025-11-05 05:03:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 878048ee-242c-30db-8250-232fac61450d | -9.72186 | -48.91256 | 2025-11-05 05:03:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a093f136-37a0-3ae7-b043-154fbec9f78b | -10.37656 | -47.75502 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 651694ec-c2ea-332e-a0a2-648e76008d0e | -6.55075 | -44.47283 | 2025-11-05 05:03:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b18a4326-4159-3919-849d-a9b72c6394c5 | -6.31679 | -47.38059 | 2025-11-05 05:03:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e07e522b-1692-3c7a-b25a-e3d394b449a8 | -10.9353 | -59.02499 | 2025-11-05 05:03:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb910905-458f-3415-be41-57feab73d454 | -8.29089 | -55.07003 | 2025-11-05 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10ee2eab-ec97-386e-9321-4376acae25ab | -6.31639 | -47.38341 | 2025-11-05 05:03:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 36279e93-29fb-30ae-920a-de74c8ce06c4 | -6.07292 | -47.29574 | 2025-11-05 05:03:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f5a3d9d-0f72-37e6-b539-95ca49987f23 | -8.30713 | -49.65389 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fa65d701-1216-3da2-bcdc-204c8a6ce936 | -6.43288 | -45.66085 | 2025-11-05 05:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a6a9928-ed50-397d-8bfb-8bfd996411d0 | -7.94406 | -49.73861 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7c7d90f-a3e8-3e69-9572-715d6fb75219 | -6.8481 | -46.29358 | 2025-11-05 05:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11b53f10-150d-38b7-b5bd-bc2a0b4e9d40 | -7.3324 | -47.25476 | 2025-11-05 05:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b6d3edc-ec82-3f18-8cfd-6d2f35187fa4 | -8.04875 | -49.63612 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| af2a5aa9-81aa-3bd0-b7ca-8115753d4bf7 | -10.38594 | -47.75015 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20781ecd-4783-3c4e-b16c-dcaa392c4029 | -7.29206 | -45.4518 | 2025-11-05 05:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 313c5a3a-a469-3d39-b9b3-e45d5d3f4cd0 | -9.59238 | -54.72026 | 2025-11-05 05:03:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e98e5ba-bc18-31cf-bd79-329b727fadaf | -10.38033 | -47.75274 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6193f1f-41f0-3f50-9b6d-ddb7fe271a89 | -10.38172 | -47.75582 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7715575b-b96f-3748-955a-24727527b9b0 | -7.71333 | -47.18625 | 2025-11-05 05:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dde96bba-d754-3a6e-b8e9-4eed05f40339 | -7.0378 | -46.98517 | 2025-11-05 05:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc7f0d47-3a71-350f-adbb-3f8b23dbbc7b | -5.89194 | -49.149 | 2025-11-05 05:03:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8abe2260-7440-3e36-bf13-274c7eb39aa9 | -6.7769 | -55.48782 | 2025-11-05 05:03:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a127698e-69b5-3a5d-a36e-7998857562fc | -5.85282 | -50.04843 | 2025-11-05 05:03:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68836df5-e301-3359-88b9-da2fd75c08a8 | -7.54323 | -45.84528 | 2025-11-05 05:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8704d94-8106-3952-bcd1-6861143857ab | -9.87322 | -47.46209 | 2025-11-05 05:03:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8db04127-6e56-3968-8047-e6c9365d8b2f | -8.46187 | -49.6392 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e209fa9f-87b6-3973-8b0c-b3b09b9f93fe | -6.07793 | -47.29644 | 2025-11-05 05:03:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 902696fb-30e4-354d-83f3-375911b226c8 | -6.85352 | -46.29441 | 2025-11-05 05:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39d33a4d-f060-38ce-b926-0f39d85ed9ff | -8.06192 | -49.63799 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b3d026e-b584-3e6b-aa85-856e8b719f58 | -11.84264 | -43.73431 | 2025-11-05 05:03:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db570a7a-f76c-3106-8c51-16c745592b2b | -12.40076 | -49.90277 | 2025-11-05 05:03:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b7dbf22-45a2-3ebd-b698-5a9b6aa38646 | -7.72487 | -46.59023 | 2025-11-05 05:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d45df77b-6fb1-3d28-82a6-33e9f195447f | -8.85456 | -49.88479 | 2025-11-05 05:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7a1b8b5-88fa-3a76-9c77-c15516572f4a | -10.42919 | -51.3676 | 2025-11-05 05:03:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90adc121-e3ab-34d8-94f3-8a86321476ca | -12.24203 | -50.29548 | 2025-11-05 05:03:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 516d0f42-4dd9-3235-90c7-bab1349b3395 | -8.23279 | -49.98363 | 2025-11-05 05:03:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2c937b5-c453-36b6-beda-2d0197253dc2 | -10.38254 | -47.74921 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64a03d1a-7ed8-32e4-be5a-d938325cdad2 | -10.37475 | -47.75513 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fecdadec-cc00-36a6-bfa4-45ec811d3e1b | -10.38212 | -47.75261 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29dce8e6-42ed-3743-a782-e21bd34e2a12 | -8.22789 | -49.98718 | 2025-11-05 05:03:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b835c5ca-3d84-3fde-95dc-1d1d51847749 | -10.38728 | -47.75338 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 542627d7-1cff-3d33-869b-56c4466d0777 | -5.83184 | -51.57713 | 2025-11-05 05:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00631cbd-d06c-35d9-9e15-0c2e803540e3 | -8.05633 | -49.64579 | 2025-11-05 05:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0edbd3b3-0d8f-3b71-913f-56320e9e6d19 | -6.55683 | -44.47374 | 2025-11-05 05:03:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c6bd055-7322-37fb-8c9e-70f713e83e7b | -7.23355 | -45.69954 | 2025-11-05 05:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60211117-c9ff-37b6-887c-1f4bf5f63702 | -10.38687 | -47.75661 | 2025-11-05 05:03:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50c7df8d-d59e-3eb8-8b7b-3374b92a5c2d | -6.73687 | -44.15462 | 2025-11-05 05:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 87996e6b-f6f2-3cc7-b7d6-e2a43f35a008 | -18.11736 | -53.56324 | 2025-11-05 05:05:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 017200cd-6d83-372b-a5d3-ae6366a5dd85 | -18.51669 | -53.50502 | 2025-11-05 05:05:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ef07ba0b-2af1-3fdb-8fa4-f7ffd65156e3 | -18.1175 | -53.56431 | 2025-11-05 05:05:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 360e4a5e-d978-3e1b-85ed-8b99f496a91e | -15.37838 | -59.58569 | 2025-11-05 05:05:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9951375b-ff98-3bad-a0d9-1f4c32aff350 | -16.89185 | -52.85798 | 2025-11-05 05:05:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fb08b0e-a39f-33b6-9134-c8badeee05a4 | -13.37721 | -61.2946 | 2025-11-05 05:05:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b73df6ef-9307-3d89-846d-ae1094022a94 | -18.51736 | -53.49983 | 2025-11-05 05:05:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2c1bad02-80f4-32e1-959c-564354651eb8 | -16.06978 | -54.66911 | 2025-11-05 05:05:00 | NOAA-21 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10985dd1-f47d-3c26-924a-6c868827c22e | -18.51273 | -53.50448 | 2025-11-05 05:05:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2784949e-c3aa-39ce-92a6-591178fbb7e1 | -16.88784 | -52.85736 | 2025-11-05 05:05:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4103a431-a560-3c8b-8137-6c125d5428e9 | -16.00442 | -57.05451 | 2025-11-05 05:05:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58aa270a-e88e-3235-a337-ab682471da23 | -18.1162 | -53.57454 | 2025-11-05 05:05:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 168c6c2f-f0aa-372a-8ce9-d9f757743ac5 | -18.12076 | -53.56998 | 2025-11-05 05:05:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b17fc2b-5ad5-3734-a6fc-132be54e8f51 | -13.37344 | -61.29394 | 2025-11-05 05:05:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e86deff9-c0a4-36af-958e-4b4ed5b08dab | -18.51602 | -53.51016 | 2025-11-05 05:05:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c373373-705c-3f22-842f-d50556d43043 | -18.11668 | -53.56834 | 2025-11-05 05:05:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33c903f0-c97f-39d6-b551-0698d1aa41f6 | -18.12141 | -53.56488 | 2025-11-05 05:05:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7792f928-4c81-3f30-9d2c-8b1b595dee29 | -15.96807 | -58.22778 | 2025-11-05 05:05:00 | NOAA-21 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14d83dc8-9605-3100-a0a4-a92ad148fe6e | -12.86421 | -60.20557 | 2025-11-05 05:05:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17058a3e-5443-324a-9f8c-8c0d0f76f61c | -13.87994 | -56.3263 | 2025-11-05 05:05:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72e1bfce-88c7-3a6e-9877-4ad45469e627 | -14.87261 | -56.56937 | 2025-11-05 05:05:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e199a2b7-c17f-39dc-9d54-aad762239502 | -18.11276 | -53.56779 | 2025-11-05 05:05:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7039f9de-b7e0-3480-838d-596b031810c4 | -18.12059 | -53.56889 | 2025-11-05 05:05:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08e3b081-1595-310b-87c4-7f88f9bde3fe | -18.11599 | -53.57344 | 2025-11-05 05:05:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2bc267c-6688-3791-b343-8281f73fe9df | -18.11685 | -53.56942 | 2025-11-05 05:05:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60a7c7aa-613e-3d6e-8373-72e9287f5a2c | -18.12127 | -53.5638 | 2025-11-05 05:05:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ed527a0-546f-39c8-a3bd-242ae841ef8e | -19.34 | -45.8483 | 2025-11-05 05:05:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 431d7a73-224b-3ef9-91cb-93e9bae515b9 | -18.24364 | -55.38535 | 2025-11-05 05:05:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 04f5e804-c477-3bf3-850d-bdef717cf750 | -15.67757 | -58.38496 | 2025-11-05 05:05:00 | NOAA-21 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b95e4ff-449a-3338-a09d-c343b42585b6 | -18.51207 | -53.50954 | 2025-11-05 05:05:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa9ffca9-f9b2-32db-bd65-8a6b9ddbb3c6 | -20.56293 | -54.65674 | 2025-11-05 05:08:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c370ae48-890b-34f8-81b5-aaa2b340bcf6 | -4.4633 | -43.2152 | 2025-11-05 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |


[Clique aqui para ver as próximas entradas](README36.md)
