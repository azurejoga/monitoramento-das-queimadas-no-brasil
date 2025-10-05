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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41005f34-3134-3b06-8e40-4f32507c87c7 | -5.53957 | -42.67848 | 2025-10-05 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ebb8d492-fe7d-3d35-94ee-a8c0d99d6863 | -8.54965 | -46.27915 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2f153feb-4311-321b-a3b1-2a869556d169 | -6.15645 | -44.6687 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 9cedbae1-479e-36ad-9efe-5f09109b0a3d | -6.60822 | -43.72549 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20afc5e1-74d6-3b2f-afaf-d3fba98cdbcc | -7.2909 | -39.27167 | 2025-10-05 03:53:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 72a8487e-f6a9-3a38-9b7d-1a695b4121b2 | -8.56032 | -46.32915 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3db1e479-1da1-363f-bb18-479eaa875ec7 | -7.47025 | -42.63247 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 772dfe24-6c1d-3c64-b1c1-0f59cd389d16 | -6.58641 | -43.46278 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09b8be21-853d-3002-adca-0edcfa533b53 | -6.60886 | -43.72176 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5dff9f7c-0fdc-35de-9020-ce0a7a36ab05 | -7.58601 | -43.06663 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecf2d917-563e-3135-b33f-0b9de9048657 | -6.62813 | -42.42323 | 2025-10-05 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 291085fb-c350-3241-bebe-e27851a0a61c | -6.25294 | -45.34139 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e268ba4-d998-320c-94c6-1a3446165422 | -6.33414 | -43.90343 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb4535ab-a487-37e6-be63-4eaba20ad6e9 | -5.12585 | -46.23435 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d33553ab-25f7-3223-aa79-57f48a02a825 | -8.11917 | -44.10083 | 2025-10-05 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 856a2c95-3554-3c37-b453-2fc08ea96df1 | -7.78054 | -42.60978 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6fbc871f-73d5-3525-9191-12b1fd5dae6a | -7.37658 | -39.20286 | 2025-10-05 03:53:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8c85e25b-d23e-31fd-bb40-dea966e1b64b | -6.37998 | -43.8908 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82007141-0598-3b7b-beb5-60fb304abf0a | -8.50795 | -44.6643 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09286383-62e6-312d-8b91-a191d4da9065 | -5.48694 | -42.8003 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6fed2fc9-e0aa-372f-9948-a864cc873ecc | -5.28897 | -43.1105 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 829178e1-e3aa-34df-8a0d-ea8d6fe65ba7 | -7.24805 | -46.94875 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6039ef6a-b05e-3062-8383-76790ed13760 | -10.35543 | -48.16601 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1003e726-0bd7-3f59-aa4e-b4afa616b807 | -6.27705 | -46.35902 | 2025-10-05 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22fb1b8e-4af6-3604-b0d1-e1e7f51870f2 | -5.41241 | -41.34784 | 2025-10-05 03:53:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 762c7d61-679f-3fa5-b8f3-11affe716a24 | -9.98415 | -48.27372 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 914efce4-f19c-3133-a8ff-bb6d891d8a1f | -8.59731 | -46.28727 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c467145a-6d2b-3fcb-b6de-9f53341e5be3 | -7.23913 | -44.88815 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 78794f25-7031-3e26-aff5-99c173ee6abe | -8.23678 | -46.80482 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a1d9aae5-74fb-3886-bb96-2be99552822d | -6.60856 | -44.31507 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b4f52a4-19b4-3f79-a9b9-56c43a662fe8 | -6.33958 | -44.02524 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15bb5e10-6a03-32f6-9a4d-66abb4eee5e9 | -6.21741 | -44.07848 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9909948c-7e58-3389-9326-3f21079be674 | -5.85173 | -42.80875 | 2025-10-05 03:53:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ce65a4ca-c0a8-3733-b916-82a4471f18e7 | -6.02373 | -44.01937 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 38f6fc3d-331c-3421-a067-fca025f2ce04 | -5.84088 | -44.45415 | 2025-10-05 03:53:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c2cd1c8d-9ae8-3129-a41d-63419e8236ba | -7.05552 | -42.77427 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e649cebd-67eb-3e85-a73d-2ead890bcf4e | -7.87982 | -42.59819 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 86c82f73-6c00-39dc-a2b9-8c50ad82719c | -6.24964 | -45.36045 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0359d8f3-de82-37b3-bc4b-f5cd9ce23e25 | -5.41172 | -41.35204 | 2025-10-05 03:53:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d0c68339-498a-3596-9b50-fa6ee6c5773f | -6.15946 | -44.65105 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f95848ac-614f-3193-a9ec-4f48b0202d51 | -9.29679 | -46.0093 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3294a856-172c-3da2-894f-abf9ba3476b0 | -6.55993 | -44.15882 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35cc0a45-7e1f-3844-92bc-b6291404fe91 | -5.83173 | -42.46339 | 2025-10-05 03:53:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8edfea34-5e08-3ccf-a5fa-3c3833fd9aeb | -6.32577 | -43.90172 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61609997-b352-31af-82f9-d9c6dcf9253b | -6.13506 | -44.63364 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aac34cd-93ca-3f42-bf4e-9cdba6936824 | -6.10941 | -45.88301 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb29a7f6-e6d7-3788-a46d-7a5f352e2779 | -10.01153 | -48.29375 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f496f3d-a598-3653-837b-9c30819fc2e5 | -6.71806 | -42.79631 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6277701b-09d3-32b1-8ef8-61859e601f2b | -8.95674 | -44.60773 | 2025-10-05 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5a61997-1110-3be8-baf8-799377677ae8 | -6.40165 | -42.69223 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0a1c2c90-1d95-3d0c-9ae9-6b47315994bb | -10.71725 | -44.17495 | 2025-10-05 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c76ee52-5b84-3dc4-b133-8aa5ee8c6985 | -10.01233 | -48.28954 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4da256f0-02f1-3bc4-b232-987a0de07764 | -6.01835 | -45.41815 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a51c614-3c9b-33d1-940f-79c37209729d | -6.12818 | -42.86143 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 324be191-f80b-3799-960e-d1b04d06a636 | -7.58452 | -43.09995 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7ae0532f-7a16-3cb9-95cb-d15eafb7b4bb | -8.54217 | -46.32046 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c1ee97b8-eeaa-38b4-bced-95997ad5475a | -8.53458 | -46.33516 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c54fbe6-9da3-3d7a-bb8f-e194ca6e1341 | -5.87 | -42.83959 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eedabe5c-cf6f-3de1-bec5-895ee8c4417e | -6.20561 | -44.07814 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d25dcc3e-9c39-3bdb-9745-0d109cdc70a6 | -8.38107 | -45.83358 | 2025-10-05 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55bbfb66-69d2-3d4f-9c9d-414dc937a4a1 | -5.46883 | -42.78678 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ed20e0f8-add9-3d10-968b-adb64da3bdda | -5.29832 | -43.10458 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80ff5309-aefc-353e-83e0-2b5752b8f123 | -6.9938 | -44.21051 | 2025-10-05 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0e760af-8d0a-3e64-82f0-5a68e6476c08 | -5.92154 | -42.89601 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 030385e2-a492-34a9-b70f-80aa54903f1e | -5.77574 | -42.94711 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| cc8b43eb-4c57-3068-b540-1b624a0c0460 | -8.7876 | -40.56739 | 2025-10-05 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3857662d-ed4b-33f7-b886-b31f16cfad4f | -8.56765 | -47.65829 | 2025-10-05 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24815f5a-3f90-380b-ae35-339cb82e13ca | -5.85339 | -42.79866 | 2025-10-05 03:53:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 82c659ae-9747-39d5-b3fa-22bc04254ca6 | -7.04986 | -42.80849 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cce7d899-9804-345f-a728-ba9c6260dcfc | -6.65737 | -41.59462 | 2025-10-05 03:53:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1141ede1-778a-359f-b457-ebb9ecfd07e5 | -6.3627 | -43.91597 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cd24197-3c4a-34c3-afcb-795c5d3fc99f | -7.77132 | -42.61813 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2ac4977d-77c7-37a3-abbf-1021093f2df7 | -7.78291 | -42.59581 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 18722ca3-db4c-394b-946f-c098fb389344 | -8.59829 | -46.28177 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9f72cb17-98a0-34b7-9675-15be454ec024 | -8.30533 | -44.83501 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60014419-1c4a-3d07-b9ee-f600d3a89f2e | -5.85115 | -42.78761 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aa247088-9a43-366b-91da-2f7bff2b53fa | -7.5224 | -43.8553 | 2025-10-05 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62e4808a-7a26-34b9-aa8f-a073b6789934 | -8.86098 | -46.79955 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66fbf969-56fb-3e77-b4ac-db4c4b50d6be | -10.14964 | -45.43133 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8295b08-d085-3251-9240-8dbc9b75da54 | -6.24037 | -44.25412 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6942ab5e-e6c1-3c19-85c1-4f40b4df7b15 | -9.11971 | -44.39692 | 2025-10-05 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64269c04-9707-371f-b375-2d2664b3b91c | -9.06539 | -47.01521 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 861bd09b-b585-3789-9da9-294e88c20103 | -5.2301 | -42.98883 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 62169f3b-3020-37a7-be4c-20deb78002dc | -8.89925 | -46.68499 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 363f0c75-850e-309f-b5ea-7f54681be597 | -9.57305 | -46.12313 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14feb362-1174-357e-a60c-e1a16f807d46 | -6.60788 | -44.31916 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f9a8676-9770-3cff-b46b-bc01faefbde4 | -6.25675 | -45.34697 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c739c2e7-4e6b-3010-a92f-3830ccf1ccee | -5.43045 | -42.93165 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43729676-a304-33cb-8607-e3fe58ed7235 | -10.39399 | -45.40446 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e29ee7ef-c0b3-340d-ba61-7d4a3583b4cf | -6.71785 | -42.82181 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ce1e14d3-68fa-3001-8362-b34db7545699 | -10.86691 | -45.4126 | 2025-10-05 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 364238a1-923a-355b-a5a0-db6a39c73e60 | -6.91668 | -37.44476 | 2025-10-05 03:53:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a026a8ad-f27c-39f7-8969-3e75ed383a26 | -6.52149 | -42.50467 | 2025-10-05 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a08876e8-82d4-30e8-99dc-2fef524e358c | -6.15289 | -44.60948 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 943757f2-f86c-3c5d-99c6-f3c2f20d5fd4 | -8.86297 | -46.84558 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60491100-0e5c-3238-b586-bf11208a1111 | -5.77691 | -42.94017 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 16188a0c-36fe-3d21-a4e6-4647fc523a8c | -7.79718 | -44.53497 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a36f4cb2-278c-3b63-bfc1-dc4eca970824 | -9.95532 | -43.78017 | 2025-10-05 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9754c49-d345-35db-8632-b60239676e45 | -6.13877 | -44.66517 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 51ac2ec7-bd81-3c37-92ad-898716d06000 | -8.56601 | -46.3249 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README49.md)
