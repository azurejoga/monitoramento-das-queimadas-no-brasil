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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fac547b4-e747-3f8d-8e57-db3d992f1437 | -9.76367 | -43.44595 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 557b3da2-e14f-3e87-a7f9-46d123623a98 | -9.71201 | -43.42669 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 82df204c-ea19-39d0-a30f-2aaaf28fb428 | -5.84543 | -45.16799 | 2026-09-08 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 363b9919-6674-3ab9-bacb-11ce973b574c | -3.24131 | -47.24866 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| a8e7ab61-1fbd-3765-af91-707d6900596b | -9.74184 | -43.49713 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8270867-d045-3f7c-9165-6c7da6d11206 | -4.72136 | -40.37149 | 2026-09-08 04:08:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a82438b-8618-32d6-8afa-07d27004c836 | -2.86781 | -41.74477 | 2026-09-08 04:08:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7231e05b-5eec-3bca-bddb-21a07eb7773e | -6.61271 | -44.71941 | 2026-09-08 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1546d7af-82ae-3fd6-bc5e-d3788384c3c7 | -4.36428 | -47.78046 | 2026-09-08 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 59b313da-c288-3bf8-9a17-edefa1ffca33 | -6.62051 | -44.71652 | 2026-09-08 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d43cdd67-5ed7-329d-a719-d083ce3223f1 | -9.74801 | -43.47988 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8e652e5-5244-39c7-a019-444c766447ce | -9.71187 | -43.47039 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 55634184-45fb-3d7d-a4bd-ee36e15935cd | -9.73623 | -43.51084 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9edf560e-2735-30d1-a17e-c5b25c7a19ad | -9.74127 | -43.50069 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 193465e1-daf9-3fe3-98f8-9a428cf0fa2d | -9.73159 | -43.38974 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| cbbfef60-7047-3287-ba58-56986fe5fea3 | -4.7401 | -42.57645 | 2026-09-08 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| be2ad958-ec3e-3c27-8cba-c9ff7eb4d1ec | -3.2457 | -47.24934 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6936ee5-37e5-35af-a0ae-2b8ac7de9eae | -9.74234 | -43.51547 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 34860408-5f1c-35cb-a59b-9e9e43503d09 | -6.38327 | -43.74598 | 2026-09-08 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61954e7c-ad80-353e-adca-dc02302cc9a4 | -9.72323 | -43.39928 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 452bc8f6-0036-31f6-bd78-a02856af295b | -2.75423 | -49.48003 | 2026-09-08 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2330edf5-b0ed-3cc5-83fe-566036cac538 | -5.49531 | -43.67759 | 2026-09-08 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a1fa513-4d92-313d-b447-9e65c9a2bcca | -3.54547 | -48.17639 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 28e52464-2798-3664-867a-510bfbd5fe9b | -9.76588 | -43.45359 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 723bdf25-c8b0-39d8-94f1-0b13d1876aec | -3.44971 | -47.27261 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6eb7d728-120b-34ec-a899-4d35d9e2242f | -9.76023 | -43.48913 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d9bccad-460b-372c-ab77-9c9921995318 | -4.98149 | -50.63597 | 2026-09-08 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7d290dc-c86b-312e-b8a8-601bb8aaed01 | -9.76306 | -43.47135 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 688ab11d-0f0e-380a-9c1a-03a39cbdafc9 | -3.9747 | -41.51798 | 2026-09-08 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5068af37-777b-3c5d-9417-99514ea7efc4 | -6.69498 | -47.41682 | 2026-09-08 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20cc5aa7-3386-3cca-b4ba-915165802926 | -3.54852 | -48.18691 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| daa86a43-8d8c-3435-b0ad-94156758c365 | -7.9325 | -49.73923 | 2026-09-08 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0870d48b-6b85-315a-993e-e5decf77aea5 | -9.73793 | -43.50016 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6ac99f57-8940-3fe5-be8f-3fe5fc9483a0 | -2.87029 | -50.44516 | 2026-09-08 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0467dce2-f17a-3ed8-b1f3-431429fc710c | -9.71258 | -43.42314 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fe236589-c313-3518-b058-2d0721dc4718 | -3.42131 | -43.16499 | 2026-09-08 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3c3907b-3d17-3796-96d0-395e5c38b689 | -9.71876 | -43.40588 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 6ca2852f-aab5-3f39-b367-0ef48d5886e4 | -3.54387 | -48.18618 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| de7b571d-6239-3734-b260-e2ea20be12cc | -4.03762 | -50.88377 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86c0db11-b5af-3cdb-80cf-ede4acf06cc7 | -9.76357 | -43.48967 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a677098-082d-3ea5-b6b2-ad31f8e6d90b | -6.18412 | -43.84645 | 2026-09-08 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e7bf95b-23eb-3c5f-b578-2f39a4f9c6b1 | -7.54143 | -45.0093 | 2026-09-08 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 687cae48-e4fe-3202-a579-c0420c6a81ec | -4.27678 | -48.66071 | 2026-09-08 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 833203da-58c8-3885-8916-530574b9c23e | -3.7114 | -51.14015 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f203ef3-f765-36b3-9ad3-370f7c7ebf9d | -2.03208 | -48.57739 | 2026-09-08 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82e0cc42-d970-334f-9de1-8c5b1f62bcb8 | -9.72714 | -43.39624 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 163d1964-c8d3-394b-9aa4-0726672581a5 | -9.72436 | -43.3922 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a3a59c13-cca4-3793-87d2-e69d16d2e9ec | -7.13939 | -42.24814 | 2026-09-08 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| da551769-b1e0-3d6c-b391-b94102ab74b4 | -3.33241 | -44.58898 | 2026-09-08 04:08:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dab745fc-2000-3d70-837c-5d2cb7d80af7 | -9.72082 | -43.45724 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5629d1ff-fb7a-3e67-b358-c3fa766b610b | -9.70698 | -43.43678 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| abf259e4-b768-3da4-8ac8-c761989c7dc0 | -9.76034 | -43.44541 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a9e55b78-364f-343d-9b66-8341c7862ff1 | -1.98338 | -48.38184 | 2026-09-08 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11dd9fb6-4139-3f1c-8327-bec03a96dd0e | -3.55399 | -48.18269 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7c3ea5a0-5f1c-39e3-93fa-1c3cc2b796e1 | -9.70805 | -43.45148 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4db84ae-2117-30c5-be4c-de9ed1270ab2 | -5.62234 | -44.24685 | 2026-09-08 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 299265e2-456c-3376-941f-620e6cd7b76c | -10.08335 | -36.1669 | 2026-09-08 04:08:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 17e7022f-86e6-3db7-b09d-ed1ff773d6eb | -4.72857 | -48.84458 | 2026-09-08 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10b56e73-bc4d-3da4-9f4e-b6799899b421 | -9.71244 | -43.46683 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a5245a55-d962-3114-82eb-cc20b3f60588 | -6.01523 | -45.81322 | 2026-09-08 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f231c0a1-bb3c-3fe5-a2c7-b987cc465d29 | -9.76419 | -43.46425 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2b73e7c8-85ae-3abb-b77c-5dc66f391212 | -9.72351 | -43.48324 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2d05444d-478e-3d71-a9e2-7e72c8842844 | -9.72088 | -43.43539 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb76c90a-5cdd-3eea-85d8-94919fe3c03b | -7.69756 | -44.31079 | 2026-09-08 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8e61c6b-b29d-3608-bb32-6b56a5955475 | -9.72521 | -43.47256 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fab9cf8a-d438-3986-b070-86760f9450d5 | -9.7238 | -43.39574 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 1db9ed32-5d78-35f6-bc0c-bd5459e148d1 | -9.739 | -43.51494 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0622d6b-8b27-3ade-b8f1-0ceebe98d296 | -6.29449 | -47.34312 | 2026-09-08 04:08:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cd8ae41-44d7-3344-8a3a-2ab8010072c3 | -4.04504 | -50.87371 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c023e04d-a2d2-32d6-b8e4-ff957ea9ff6e | -4.11103 | -49.06217 | 2026-09-08 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e77ce499-4ddf-3ef0-af70-d28cc0089671 | -7.09443 | -41.68811 | 2026-09-08 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 30344467-12cc-3a18-b97f-7de1ca09114f | -4.49972 | -42.5532 | 2026-09-08 04:08:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49f8a816-95b1-3bbc-b101-4127aed5eb18 | -8.53664 | -39.47918 | 2026-09-08 04:08:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bb057de4-d066-366d-8458-045e196b892e | -9.7277 | -43.39272 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 195a3770-6bdf-34cb-930c-0f301965cf7c | -9.37989 | -48.54553 | 2026-09-08 04:08:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c953227-344d-3c1a-8c0f-45abbc31e61d | -5.59322 | -45.37765 | 2026-09-08 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8507c30c-551a-384f-8f03-d2fc1b2a2f4a | -7.61059 | -47.29284 | 2026-09-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa9e87da-23cc-3ca3-b146-cc8509240ad5 | -9.74354 | -43.48646 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5d48c183-2087-39ae-abd5-c8f9c17be8bd | -7.54503 | -45.00981 | 2026-09-08 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 015b9068-8714-3973-ac5c-25275eaee50b | -4.72941 | -48.83954 | 2026-09-08 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb333cb4-77a3-3dee-a982-cc8a8bc1ad03 | -9.70862 | -43.44793 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3786e4d-7ce3-3302-b4ed-e9252d49c81e | -4.15118 | -38.48134 | 2026-09-08 04:08:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7adc2bf6-276e-3a9c-b4c9-a6577279447b | -2.87577 | -50.44608 | 2026-09-08 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fdf9258-2ecb-32e8-93c3-e2d97b367c7a | -9.76363 | -43.4678 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29d249bf-c0da-3377-ac78-9eb76cda3983 | -9.72025 | -43.4608 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15950a2b-cb33-3291-a146-6d7477a850ae | -2.97985 | -49.26682 | 2026-09-08 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91d38db8-58d9-3dda-a04a-2c00950312dc | -9.72294 | -43.48679 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8d557377-36e7-3200-badc-4d04c6875291 | -9.72855 | -43.4731 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a32e3364-a178-3ad3-9f63-d6c4331396ff | -4.87751 | -43.38901 | 2026-09-08 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fef2ada8-0f88-368f-b923-90e7bf7f8e6c | -5.49186 | -43.67706 | 2026-09-08 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b1ed5b9-0d5d-3c4b-a63e-9182ee3f24a4 | -3.32502 | -44.58782 | 2026-09-08 04:08:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54adeeaf-7150-3d09-8d65-b3c2c37bf90b | -9.71428 | -43.41247 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 5da7fd0a-a4d9-3c71-b477-e443f621d577 | -7.37299 | -47.01296 | 2026-09-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 884b9981-a210-3822-b354-973565111ed0 | -4.34745 | -47.58174 | 2026-09-08 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c23959fc-16ca-3282-be00-dbfdbe1933a6 | -7.37516 | -47.76175 | 2026-09-08 04:08:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 64174368-8df7-3417-90a2-41b4888f6a0f | -9.31773 | -40.2033 | 2026-09-08 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 3550a4e4-9719-384e-accf-614355fdafc2 | -4.94404 | -45.66747 | 2026-09-08 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25644fcd-b655-38e9-95f4-c3ac496f7735 | -5.75605 | -49.11209 | 2026-09-08 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7d46c87-91ab-35aa-a5b5-49c85b2df563 | -6.38268 | -43.74975 | 2026-09-08 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99cef03f-2c2e-3981-9f66-245de7700edc | -9.71762 | -43.413 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |


[Clique aqui para ver as próximas entradas](README11.md)
