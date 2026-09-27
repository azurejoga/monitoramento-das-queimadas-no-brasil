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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d66ab0f-561e-3a4d-a685-c41a9c633acf | -11.94076 | -50.62172 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 41e6489d-5a94-39eb-b0b4-f83dc5e06826 | -12.99246 | -42.2242 | 2026-09-27 11:45:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 46.9 |
| 2f58122e-a993-31b2-801e-be163461c465 | -11.92619 | -50.48785 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 77a0894a-095a-367e-aa54-1d472e24a9dc | -9.84449 | -44.94611 | 2026-09-27 11:45:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 593c82ee-aea5-3f22-a5ad-8f8c412d258c | -5.74013 | -45.05856 | 2026-09-27 11:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0bbf0a4f-fe28-3be0-800b-31c199d1e76d | -11.96417 | -50.53137 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| aaca8001-44d2-39f0-9006-01186e10b7d9 | -5.26886 | -48.37257 | 2026-09-27 11:45:00 | TERRA_M-M | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 21fbd62d-809c-33d5-b193-fcb59a0c6e2e | -6.8518 | -43.5017 | 2026-09-27 11:45:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 22ddd55a-f7e8-3cc4-a1f1-77a9922a1b5b | -13.91939 | -42.08911 | 2026-09-27 11:45:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 35.1 |
| 80e8fead-513b-39d5-87be-28da177400c4 | -7.99377 | -45.02135 | 2026-09-27 11:45:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 463585fb-5578-3e0c-b5f8-33a254913dcd | -6.83977 | -43.51274 | 2026-09-27 11:45:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 44ca2cc9-d8d5-3271-92f0-46494e14df94 | -14.64069 | -45.10048 | 2026-09-27 11:45:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2ac356f2-c6e7-32cc-8b1b-4529c5b59e3a | -12.24594 | -50.39147 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6fd82f58-2179-3500-bbc4-011947d2f88b | -7.37449 | -42.09589 | 2026-09-27 11:45:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 33.0 |
| aa4ec43d-7edf-3944-95b4-005ff06e8b62 | -12.28583 | -50.36287 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0af529db-91bd-38f2-8745-f9dba5bbc14d | -8.35056 | -45.43099 | 2026-09-27 11:45:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3c36127e-1f93-3f3c-b068-a7f0a4c3cbeb | -8.34607 | -44.15607 | 2026-09-27 11:45:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 9a090752-bc85-35c0-8407-77731b604a37 | -14.12832 | -46.32812 | 2026-09-27 11:45:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 1e16a722-64a8-350f-9d65-6517dd067f55 | -11.05282 | -51.31362 | 2026-09-27 11:45:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 35e817d8-af1e-3939-8c83-62b776404b50 | -13.88466 | -49.03359 | 2026-09-27 11:45:00 | TERRA_M-M | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| c739995b-1054-361d-ac23-55b7bb3a4aed | -12.28433 | -50.37278 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| aa35cf76-a5f5-3f98-943d-fc698faad8d1 | -8.36467 | -44.17055 | 2026-09-27 11:45:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 241.8 |
| be5e4779-98a7-3e02-b8c0-81e19c8df0c4 | -12.02202 | -50.59224 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 87308c7e-b4d1-3f0f-9709-79b6b394dd07 | -6.84147 | -43.50028 | 2026-09-27 11:45:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 8af8f3e8-249e-3c37-a99b-246d511496bc | -14.12021 | -46.31629 | 2026-09-27 11:45:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9f532852-5168-3509-822f-3d89e2541e22 | -12.23668 | -50.39006 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 759f181d-5d3b-3cf8-b4b2-94e0a13b992e | -12.99463 | -42.20538 | 2026-09-27 11:45:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 9f997c31-fd51-3ead-aaf1-cd0076ad9988 | -8.36938 | -44.13506 | 2026-09-27 11:45:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 498e5657-30ee-3ac7-a7c1-7be3bb3e7263 | -11.76628 | -51.00178 | 2026-09-27 11:45:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c75e4bd0-5961-3125-b16e-0d280416e241 | -8.08182 | -44.83616 | 2026-09-27 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f1f81021-a35a-394a-b25f-0673757f2fda | -6.84164 | -43.5756 | 2026-09-27 11:45:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 238b879c-b41a-38be-b360-26c7eac60f83 | -8.35459 | -44.16922 | 2026-09-27 11:45:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 2895057d-710f-35b5-8f3c-654f639b9173 | -8.23385 | -45.42353 | 2026-09-27 11:45:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0ac96925-a161-3a72-a394-f10e9ea86afe | -13.65817 | -41.53112 | 2026-09-27 11:45:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 42.3 |
| 449431f1-9896-3473-91ce-a3e6d851efd4 | -14.12695 | -46.33862 | 2026-09-27 11:45:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 2ef74710-fe24-37fd-8bd3-2b9317ba2029 | -8.35615 | -44.15741 | 2026-09-27 11:45:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 153.7 |
| ced24937-b36a-3f7a-be04-cbb01e2dee13 | -7.27225 | -43.3176 | 2026-09-27 11:45:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 578478a6-665b-3599-aabc-31815e23be58 | -11.93552 | -50.48927 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c09b0d5b-5465-3f6d-894b-c3c2ebb6ffdb | -15.74812 | -47.03017 | 2026-09-27 11:45:00 | TERRA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9b5d74c1-65ed-30c6-aef4-950a19bd0210 | -8.37095 | -44.12321 | 2026-09-27 11:45:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 63f4f36f-e75c-3427-b6bb-4e3406b68a39 | -14.52976 | -48.32534 | 2026-09-27 11:45:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bd7fca7f-2a76-3c06-9a14-8e25af54e175 | -12.13484 | -50.32744 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 51a58e54-77ff-32ae-9a79-9d0dc8310f4c | -13.91708 | -42.10975 | 2026-09-27 11:45:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 29.4 |
| dba8cee6-6980-329c-8a00-25906d268dd1 | -13.91819 | -42.10415 | 2026-09-27 11:45:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 7d6f1aa3-31ba-3e76-9846-1f0f162e7398 | -9.15397 | -45.61633 | 2026-09-27 11:45:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1ad9971f-29ac-3fcf-b458-1d4896be5263 | -12.99126 | -42.21842 | 2026-09-27 11:45:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 60.1 |
| e9fc163a-495c-3246-aaa7-495b1c96fba2 | -12.26711 | -50.29939 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d2995f02-648c-3e49-aab7-2e877d3ca805 | -5.73703 | -48.32792 | 2026-09-27 11:45:00 | TERRA_M-M | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 4ae53bea-b747-3dc5-897d-eed59fc1a357 | -8.10175 | -43.99562 | 2026-09-27 11:45:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2c49cf45-e5cd-3ea1-8265-14c16d13cc2e | -11.93451 | -50.62466 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f546105c-b3ff-3bf0-a1ea-0499e07b22fe | -14.80662 | -45.95881 | 2026-09-27 11:45:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| bd771c91-92fd-336f-a647-97ae10e40b58 | -10.02021 | -50.14138 | 2026-09-27 11:45:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 078c6a04-edfd-3b99-a142-9503fcab80ec | -8.34921 | -45.44098 | 2026-09-27 11:45:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2c8631d6-4ae6-3027-b4a6-ef6022a00dd1 | -12.11158 | -50.29357 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 25735a34-cca8-3fab-a830-0bfb4efc5d3c | -13.64463 | -41.53001 | 2026-09-27 11:45:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 70.4 |
| ff7f5cc8-ff52-362b-a4c7-7b577431cbf9 | -8.27957 | -45.41527 | 2026-09-27 11:45:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 20ad5b7d-1f59-33dd-b332-847e79defecf | -7.29508 | -43.30745 | 2026-09-27 11:45:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 56dcbad6-cb0e-3ca8-8124-b124a5f257a6 | -9.31532 | -47.63173 | 2026-09-27 11:45:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7a9aa1fb-6963-3f6d-85d5-5b1a7981fd1a | -6.87043 | -45.54852 | 2026-09-27 11:45:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1d7afba0-3a45-37cb-a5b7-f332b225b42f | -13.88927 | -49.12666 | 2026-09-27 11:45:00 | TERRA_M-M | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9d170d7a-05f8-3a6c-8b0e-b568e7b10ad3 | -11.96571 | -50.52123 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 8ec7861b-7363-3f4d-8488-0a5207b539d1 | -14.79685 | -45.95747 | 2026-09-27 11:45:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 56cc817c-a352-3099-a67c-924b54c55ecd | -14.11746 | -46.33744 | 2026-09-27 11:45:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3a3b44c2-663f-3151-b1fc-0304ce1fa5a5 | -11.87644 | -50.501 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| c31cd153-cf49-32d6-8a13-af9617744645 | -12.42867 | -44.14938 | 2026-09-27 11:45:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 991bdc59-24a9-38d5-af7d-cadfceabd271 | -11.99146 | -50.2896 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 83cbe49f-100b-3744-b505-ea4aced4fc4f | -6.94347 | -41.60608 | 2026-09-27 11:45:00 | TERRA_M-M | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 6d44c1b7-b340-3f7c-a010-89f47f864714 | -11.77266 | -51.02487 | 2026-09-27 11:45:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| ca63abef-fd1c-3dac-8004-4f6f00b034b0 | -10.01084 | -50.13999 | 2026-09-27 11:45:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 77c3ce89-6d2d-344a-8d6c-80215ba7dedb | -11.87489 | -50.51114 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| cc21a52c-0805-31e9-bafb-75ff4ec751d5 | -6.8501 | -43.5141 | 2026-09-27 11:45:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 32c4e2d3-db73-3885-b76e-19f714de530b | -8.35771 | -44.14557 | 2026-09-27 11:45:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 4a380217-19d0-3c07-86fc-1d7896f0ad14 | -15.63691 | -43.25319 | 2026-09-27 11:45:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 15.4 |
| e3914b42-0810-3fe3-8ed0-9f9fb3492bf6 | -7.37238 | -42.11197 | 2026-09-27 11:45:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 147.5 |
| 56195d4a-3a0c-3f3b-9e7e-327c9ba31568 | -11.05106 | -51.32511 | 2026-09-27 11:45:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 203f9e59-6041-3dda-93a8-06be7f84d5c6 | -7.3703 | -42.12784 | 2026-09-27 11:45:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 142.8 |
| be4d4d5c-c5f7-3931-b6f4-eb4b5001a8c7 | -8.24916 | -49.96211 | 2026-09-27 11:45:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 81f045fa-eef5-354e-aaa2-404bf6f62c93 | -11.93604 | -50.61439 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bb0cc245-963c-3258-ba59-73f84daac890 | -12.1256 | -50.32604 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 3e5a68cc-dd02-3e5c-b82e-8da13661a9f9 | -15.47648 | -46.15397 | 2026-09-27 11:45:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a3530eec-e7ad-3d95-8755-85da3c3fb11c | -8.24323 | -45.42434 | 2026-09-27 11:45:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fe91dc8c-ed93-31f4-84ef-99ae5b05a92c | -12.13336 | -50.33735 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1fb73a40-f928-3236-bd45-82f8ffc3eb02 | -14.12157 | -46.30576 | 2026-09-27 11:45:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 57ffe710-1853-3b92-847e-7c0fdf7429e7 | -12.24447 | -50.40143 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d485bce2-e7a6-3419-b835-c79167049b9e | -11.93703 | -50.47916 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c37f1c9c-8384-3154-bfcd-e4b5e906c2c4 | -11.89666 | -50.49371 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 67210e47-fad1-3a77-aae6-2561dfe47f69 | -8.35304 | -44.181 | 2026-09-27 11:45:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| db0009af-f739-3161-8f36-73123b2f7fb0 | -12.22288 | -50.715 | 2026-09-27 11:45:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 966ff0a3-e85e-3332-80f1-256b54375aa3 | -14.11883 | -46.32688 | 2026-09-27 11:45:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 8734478f-48fa-33ec-a111-07a1ee8f366f | -8.36781 | -44.1469 | 2026-09-27 11:45:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| eb5b47d9-12ba-3bf7-82a2-4ed9eeca22b2 | -7.9952 | -45.01089 | 2026-09-27 11:45:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d5b584c5-965a-36f9-a26b-ab6d352c73de | -8.36624 | -44.15873 | 2026-09-27 11:45:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1167.6 |
| 5258f643-37ea-3888-bc25-68eece8e47cc | -12.22445 | -50.7047 | 2026-09-27 11:45:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 37.8 |
| ff7b17c2-616e-3d64-88cd-be1088d73243 | -14.50195 | -48.33062 | 2026-09-27 11:45:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 18c4bfd2-c70a-3a4c-a1fc-0a523c90278a | -16.04226 | -44.92306 | 2026-09-27 11:45:00 | TERRA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 13852353-f7a1-38e5-8f9a-87a4a44396b0 | -11.9277 | -50.47774 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 61e7fe3e-55f9-353c-b083-77b079d6c2f3 | -14.53104 | -48.31621 | 2026-09-27 11:45:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3e6f0cbd-7d27-3f17-aa5a-4bc8e0976d77 | -12.0205 | -50.60246 | 2026-09-27 11:45:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 373a4542-1c87-3f3c-8f1f-06b2c7155b86 | -14.64412 | -45.09504 | 2026-09-27 11:45:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8cc12ea9-f54e-39b8-8357-d7ec72366a9f | -6.84333 | -43.56331 | 2026-09-27 11:45:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |


[Clique aqui para ver as próximas entradas](README54.md)
