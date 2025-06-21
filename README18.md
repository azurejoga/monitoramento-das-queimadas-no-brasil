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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c23126ff-665a-3979-8854-57b1a4ef751f | -4.54875 | -48.02206 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45518426-3949-3d1e-96c4-da00b8f8dd27 | -3.62841 | -47.52551 | 2025-06-21 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a20131b2-744d-3e21-99c1-09ee2f4f3819 | -4.87491 | -48.91048 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd4ae1aa-2665-32a9-8b8f-9d537007e37d | -3.96788 | -48.13368 | 2025-06-21 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 01f76456-9a77-37dc-9ad2-49c2478bc8b9 | -4.525 | -48.00582 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27b9dbb6-a039-36f9-82f4-1a425ccb669c | -4.53597 | -48.02005 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07e0e85a-8d47-38d1-8448-e8b6fb6e46be | -3.62781 | -47.52952 | 2025-06-21 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16efc6d3-84c9-3e5a-b59e-4598e776f0d5 | -4.38163 | -48.07048 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acab1b67-f095-33ff-8509-50e1281ec1d5 | -3.69571 | -53.75721 | 2025-06-21 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 13233e51-db10-335f-8331-a7d79e02affe | -3.69903 | -53.75773 | 2025-06-21 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 111a32fc-0664-3590-b816-d9eb03a58f11 | -5.75212 | -43.05141 | 2025-06-21 04:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d2148f7-0654-3b52-af49-01a068b46c23 | -4.37681 | -48.07375 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e55639fc-5eca-31ca-8e16-a4ee30c7ef6e | -4.38126 | -48.07973 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 343d6302-6833-3128-b6f7-15e55e4f8190 | -4.54508 | -48.01749 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34257b13-c1fa-3fc0-9bd1-45a58c16f42e | -4.54141 | -48.01283 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aec8b2b7-33d6-30f3-9314-0abb454d152d | -4.53174 | -48.01921 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b42cb40-d127-3e29-85cc-839dc6409c08 | -3.0456 | -49.43007 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 50e02df7-337d-312d-82c2-f573c51590b7 | -4.54935 | -48.01812 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da7e5687-8cc7-3415-9e0d-6b90eece03eb | -4.37992 | -48.08215 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2647d14e-638f-35eb-86fc-6404d2c3d416 | -5.07545 | -43.72806 | 2025-06-21 04:57:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ffdd4a7-6907-33a8-b37e-7394b94ee0a1 | -3.62901 | -47.52148 | 2025-06-21 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3741ca23-c3d2-310f-a00d-bd280acabedc | -4.53656 | -48.01609 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e06816bf-ecdc-3ca5-a6d4-738edffe2008 | -4.54261 | -48.00481 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d84be5f-05a5-3210-b4ab-14111645c682 | -4.27875 | -48.18697 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1eded8ea-9c4d-3fe7-9e5b-bce66c2853af | -4.37882 | -48.06741 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b35c5ec2-1c6a-39f8-b433-0b2227ca5d4e | -4.53775 | -48.00809 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fd11ac8-f226-37b4-abba-1f5defed227f | -4.54686 | -48.00554 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2febf8ca-25f9-370a-ae4e-79d092b5b569 | -4.54449 | -48.02145 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 747308b6-bee7-36c5-9a05-af5eb748ca51 | -4.55053 | -48.01021 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bda50bb8-da97-3ef2-9615-f00f2fa2490f | -4.53232 | -48.01528 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2a5cfd52-2516-3547-88a7-c14566db0d33 | -3.04179 | -49.42949 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6530efe-93c8-37c3-a2af-e991582415d4 | -4.54567 | -48.01353 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b9eb6b3-25ab-3082-8ebc-c775418b9901 | -3.04347 | -49.44392 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7b6f0131-f4b8-3eb6-a434-673cd3cd982a | -4.53351 | -48.00729 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 439a3851-1d65-3921-b2c9-6e7ae390d1d6 | -4.54082 | -48.01682 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa496fd6-4b0b-3167-a9f9-ccf15da0b992 | -5.77911 | -45.90592 | 2025-06-21 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a775d5c-4287-3c85-85db-cd5485bfc861 | -4.52926 | -48.00649 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83f6a3ad-558d-382f-99a4-ea7417b24486 | -5.7741 | -45.90509 | 2025-06-21 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39325a71-1a42-3568-b854-5c192c3692c0 | -3.03798 | -49.42889 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28ec480f-9987-318a-ae15-059c703033e7 | -5.77768 | -45.90643 | 2025-06-21 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60bffd80-293e-335e-b798-d0b52ab976eb | -4.38048 | -48.0783 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22a22343-5e38-3281-b3e9-a84b85d45992 | -4.38306 | -48.06804 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9c0dabc-8192-3cad-a1fc-e04cf506ebd9 | -5.7515 | -43.05594 | 2025-06-21 04:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a052200-538a-3a2c-923e-52a9cfc40ef6 | -3.04418 | -49.43932 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6ae7719d-59a8-3aae-8d18-299a7a2d5621 | -3.7269 | -53.98503 | 2025-06-21 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e234335-2d02-3bb3-92cc-94a1e6f1f2ac | -4.55113 | -48.00623 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4b154a5-e7c3-394e-a95c-6e80cd79d499 | -5.07488 | -43.73207 | 2025-06-21 04:57:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 34fb791e-fdaf-3e50-b0ab-72ea1c13f204 | -4.53716 | -48.01211 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea6bb5ae-f41c-3b21-a8bd-bdc5f1331aed | -3.62962 | -47.51737 | 2025-06-21 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01f1f815-b0fd-3bb6-9591-70cb0be2b2ed | -3.9637 | -48.13298 | 2025-06-21 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6a055d13-2535-342b-99a7-f1c4a789975b | -4.53291 | -48.01131 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1af69478-5f02-3d06-bed4-d47676d70142 | -3.62527 | -47.51669 | 2025-06-21 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| feeece24-57d3-3874-8aa8-6a42f7d3920a | -4.5341 | -48.0033 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32b3389e-1fb5-30fa-a202-810338c46fd8 | -5.75162 | -43.05453 | 2025-06-21 04:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 792e35d4-cbd1-3f3b-b1ad-20377060d682 | -3.72635 | -53.98849 | 2025-06-21 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a217ef8-64c3-3645-9d0d-cd7d139b0a42 | -3.03346 | -49.43295 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc248861-a057-3646-96ce-7c7849fbfc41 | -3.42334 | -47.60677 | 2025-06-21 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf20d0cd-2514-33c3-a68f-584a2c4b2885 | -3.03727 | -49.43354 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04904898-e1c8-3275-b838-9d61e48cf9fb | -3.42272 | -47.61083 | 2025-06-21 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc2bd4d4-a6c6-3c8d-992a-5ecb7ec5de75 | -3.04251 | -49.42484 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e920a8a-89e6-3eff-9ccd-67167969ea8b | -3.96845 | -48.12988 | 2025-06-21 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ce1e8df3-c3d9-3688-952c-6256cfb1999e | -4.37702 | -48.0791 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 319c86c5-0240-3eab-8b9f-374c86e54ffe | -3.03966 | -49.44336 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9fad50fe-77c3-3d45-85ce-c1147dff43ec | -3.04108 | -49.43412 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8ba1ba92-9abd-3a76-828f-83df0e15acb9 | -4.37643 | -48.08292 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a60d90de-0d2a-3a9c-980a-f29d3eabfd36 | -3.62466 | -47.52082 | 2025-06-21 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3c1b5c4-52e3-3fc4-bd19-cad52c63378d | -4.37739 | -48.06985 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cfabf2e-f6bb-34bc-a350-7e5d16a5f350 | -3.1179 | -48.96046 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98afeecc-73f1-3bc3-bc2c-43e2a1273a3c | -4.54023 | -48.02079 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 487d721f-d2a4-3687-a84e-18ace3574008 | -4.87895 | -48.91108 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c93948c4-5e7f-3564-88fa-857e95843d1f | -4.54994 | -48.01418 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7d65c6d-747c-346e-b58d-5c3f7fc9e935 | -4.54627 | -48.00954 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a2c0706-837b-341c-b1b6-41a964a7aa4d | -4.54201 | -48.00882 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7c18c15-06db-31db-8c05-5b2107e7e20a | -4.52867 | -48.01051 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76ded9d1-9348-3015-98a2-f35c77c3d497 | -8.98581 | -49.86844 | 2025-06-21 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b9d50716-840c-3115-b6d5-49c356bc35e9 | -9.25737 | -57.52379 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 78cbf6c2-7dfe-3222-871a-3762c8b83bbf | -9.39545 | -63.26712 | 2025-06-21 04:59:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1617cfe1-12b4-34ed-b2bd-0db3b252918e | -5.30351 | -55.97404 | 2025-06-21 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0c6b32b-8a23-38d7-8bd2-889998980ade | -9.0269 | -61.22134 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a53ba77c-57ee-3211-a962-bd0df0cd051b | -9.47538 | -57.83997 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ee28a374-b13f-33f1-b681-d150589625ea | -11.06893 | -49.62177 | 2025-06-21 04:59:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 133ef367-b947-3f61-a18c-615fc1ddab82 | -9.46975 | -57.85165 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6555ee2-3f32-3189-92dd-0e71dae0bb8d | -9.0158 | -61.23272 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9236f37b-61b7-3885-ab7b-55cc340a4149 | -10.86039 | -53.7698 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f28e7c2-9382-3fbe-bb6f-d372cd0a8646 | -7.21394 | -43.06721 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bd66dcf5-3c0c-3661-bddb-c6e02a103bc3 | -10.50818 | -47.57759 | 2025-06-21 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10051259-5995-35d9-9ccb-1f314a5854bc | -11.11713 | -53.98175 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2fa00dd-6d26-3ab3-b8c9-46b686c07a74 | -11.17841 | -46.65682 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f694727-d051-3fc3-ad4a-5276e9ee5493 | -7.27217 | -45.36087 | 2025-06-21 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 770f8fd8-949d-3da8-bfa9-0cc45722f4ee | -8.38047 | -46.97894 | 2025-06-21 04:59:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 592fe041-83fb-3aed-b009-bd62ee594196 | -10.51299 | -47.57824 | 2025-06-21 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a25c448a-332d-3a59-be22-925fe9f08a6d | -10.29481 | -57.14027 | 2025-06-21 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd3ee207-17ec-3a38-8541-6667bfb822cb | -9.2596 | -57.53231 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9f2ba03-7c81-3d38-80f0-725d556685bf | -10.85866 | -53.75829 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e37675fb-609e-3468-a5fe-38f2ab9a32bf | -8.13321 | -46.82565 | 2025-06-21 04:59:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a3c7b8a-f9ed-34d8-9993-b3df684baaaf | -9.4611 | -57.83749 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18810748-bb3c-34e7-9b0e-9cc71ca760e8 | -8.37562 | -46.97818 | 2025-06-21 04:59:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3db72be9-7364-3200-bc54-5ba6fe305798 | -10.14668 | -48.99151 | 2025-06-21 04:59:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 827b1c8b-7767-3be2-b11b-ab27398ab140 | -9.47181 | -57.83932 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae4cf5ad-ecf8-3c27-8e27-4304971245ba | -10.14571 | -48.98874 | 2025-06-21 04:59:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README19.md)
