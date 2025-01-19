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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0b36c11-d2d0-3944-a16b-b9963630f1ca | 3.75185 | -59.69856 | 2025-01-19 06:03:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e8105dd-e2b0-33a2-8e8a-485dd9b79f94 | 4.50345 | -60.69458 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4d70db5-d13c-3ff3-bb3b-c0fbc281b8f7 | 3.41891 | -60.39674 | 2025-01-19 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cc1ac14-38c7-3c04-9163-a21f9963ec6a | 3.33536 | -59.83563 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bdec502-5d6d-3f56-8f16-489a0fc46af1 | 4.53119 | -60.70134 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87049e00-f766-37bf-b690-b13e964b6517 | 3.41539 | -60.39799 | 2025-01-19 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3ec3f43-4b80-3c51-9dd1-3881d4be05c2 | 3.12318 | -60.7539 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 86d17055-6325-34de-a2c6-54048c012793 | 1.12226 | -59.40666 | 2025-01-19 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baf3dbad-3d8e-38fc-bd83-55bf55530ee0 | 1.12492 | -59.40878 | 2025-01-19 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d085c0b6-5951-358a-8171-bcba3a6a26b9 | 3.11898 | -60.76127 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daf4d315-8f68-3430-9319-1efcbe423045 | 3.11424 | -60.76535 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e209f82b-5db1-3616-9bac-163a8f2576e3 | 3.12156 | -60.74417 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34c43c60-2d32-3afd-ad36-23dfe37eb62f | 3.12264 | -60.75066 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d95d8b04-8acc-38fb-a208-0134c3b1889e | 3.11844 | -60.75802 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c777a2b5-1ee8-3c03-85cd-50b1d90fd1bf | 1.12296 | -59.41109 | 2025-01-19 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06759b4a-e6d5-3739-bb59-e34956e18b88 | 3.1152 | -60.73855 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03d44e87-1dfd-3d9d-a90e-2aa489062b36 | 3.1179 | -60.75477 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94396c7f-8457-3e9f-9645-2ab2d8adf6f7 | 1.12364 | -59.41539 | 2025-01-19 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2791a43b-17f8-36d6-9c07-a67712b1be31 | 3.12103 | -60.74093 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bba88c98-09d0-3d11-9036-e7de8cd584aa | 3.11628 | -60.74502 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81ad4ccb-de2f-3580-8779-9d0e32962b25 | 3.11478 | -60.76857 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 928e1aab-5694-3635-bb9c-5fde8342c3b7 | 3.11736 | -60.75152 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adb6d3ff-01c6-38e3-afa8-27bb5b25d729 | 3.12049 | -60.73768 | 2025-01-19 06:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd8b6b4a-9a4c-31ca-acac-39cae1fec86c | 1.12564 | -59.41314 | 2025-01-19 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9da2df67-627a-32ae-800a-2c798975b623 | -7.97213 | -72.5387 | 2025-01-19 06:07:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 55b4f618-1b3a-3dab-8fb0-0a98fb8a17fe | 1.3586 | -60.027 | 2025-01-19 06:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.2 |
| cce8d7ae-fc66-353d-94fe-4efd1629c890 | 1.3403 | -60.0271 | 2025-01-19 06:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| abfc749f-d68f-36a3-8849-f8ff4ca21a02 | 1.3586 | -60.027 | 2025-01-19 06:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 53e53d89-bb17-3abe-a016-a6c91ba96557 | 1.3586 | -60.027 | 2025-01-19 06:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 56d2f762-44ed-3690-85d5-d8b07aa09033 | 3.28025 | -59.93661 | 2025-01-19 06:35:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4c272de1-bfce-35c7-be91-08f8fd9ee384 | 4.52076 | -60.68674 | 2025-01-19 06:35:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1036ade6-8707-3130-915b-1fe6357f7193 | 3.2726 | -59.94729 | 2025-01-19 06:35:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b9606116-e468-313f-b7b8-583622fa60a6 | 4.50314 | -60.68927 | 2025-01-19 06:35:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 35ab87ef-24a2-3fc1-bb59-e84de8093d36 | 4.50447 | -60.69812 | 2025-01-19 06:35:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 19.6 |
| a5c17ecd-4ee0-311f-96a4-4c67a5240677 | 3.26354 | -59.94862 | 2025-01-19 06:35:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eb125996-c128-3122-a92b-04ea0cd25ff5 | 3.27118 | -59.93795 | 2025-01-19 06:35:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bea101fc-c110-305e-b356-75d42cadb11b | 1.35461 | -60.03071 | 2025-01-19 06:37:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| d12b5da8-f3c2-3a60-b933-0dc677e273a8 | 3.11602 | -60.74125 | 2025-01-19 06:37:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3241a90c-8e20-3f64-b629-5e81d23e3171 | 1.12435 | -59.40508 | 2025-01-19 06:37:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 131759b6-e2ec-3061-bb8f-a477707c1823 | 3.1187 | -60.75902 | 2025-01-19 06:37:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 697cf061-c0a4-3842-b049-65cf2da9667d | 1.35316 | -60.02109 | 2025-01-19 06:37:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 062e8a6b-0e67-3c2d-a215-d362616ff28c | 3.11736 | -60.75014 | 2025-01-19 06:37:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 2e0daf9e-9c4b-3101-8309-e98c0ec48254 | 1.3586 | -60.027 | 2025-01-19 06:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 1d4c3075-1f08-31e9-926f-cc85afbe53fc | 1.3586 | -60.027 | 2025-01-19 06:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 08c90a35-cd78-30fe-a1eb-dba59f80772b | 1.3586 | -60.027 | 2025-01-19 07:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 0153475b-06c6-3742-a545-e3774404a789 | 1.3586 | -60.027 | 2025-01-19 07:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 6a52aa8d-1db0-3a68-b141-2a9843d5e0d6 | 1.3586 | -60.027 | 2025-01-19 07:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 83a0e944-d6d9-3a7c-8873-6952a34f4b5e | 1.3586 | -60.027 | 2025-01-19 07:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 255dfc3f-28f6-3a1f-bd37-7fa7d48870e8 | 1.3586 | -60.027 | 2025-01-19 07:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b2cca550-7841-35dd-bfd8-7a50ed09e05b | 1.3586 | -60.027 | 2025-01-19 07:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2025f4ed-ede3-397e-b66e-d88ce79b29b3 | 1.3586 | -60.027 | 2025-01-19 08:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a62d1633-5f84-3edf-bfc9-071f23daac19 | -15.39 | -43.78 | 2025-01-19 12:00:00 | MSG-03 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 783415bf-91dd-3001-babe-069a207020ed | -15.83 | -43.46 | 2025-01-19 12:00:00 | MSG-03 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 60dbceec-6b55-3264-9ea2-fc915732b186 | -15.73 | -45.95 | 2025-01-19 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4489457c-ee2b-353d-af45-6ab6e49f1e05 | 4.4993 | -60.6987 | 2025-01-19 12:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f8341812-1822-3f5f-a3b6-7223d44b795a | 3.2759 | -59.9447 | 2025-01-19 12:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 35a2f7c4-8348-33c8-82c0-c121acbd1f1a | -21.30964 | -47.73334 | 2025-01-19 12:44:00 | TERRA_M-T | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9778d038-8000-317b-9e0d-5fce4915c246 | -17.6566 | -49.93801 | 2025-01-19 12:44:00 | TERRA_M-T | VICENTINÓPOLIS | GOIÁS | Brasil | 5222054 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 32009217-5a07-3c84-8717-12f0bebc5920 | -21.53158 | -48.5722 | 2025-01-19 12:44:00 | TERRA_M-T | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 2f10f63d-a4f2-3bef-84ff-aac3ac4a80db | -16.35896 | -47.25287 | 2025-01-19 12:44:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8bcb54b4-b430-31ce-8a67-bfdae542a930 | -20.46175 | -48.17263 | 2025-01-19 12:44:00 | TERRA_M-T | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6f3ed569-7cde-3163-a291-dc5d84368865 | -19.31544 | -48.50256 | 2025-01-19 12:44:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7803da26-4f15-37e6-a041-89b2fc8bf5cc | -19.24611 | -48.5148 | 2025-01-19 12:44:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b3db0210-fa1f-302d-8ca8-a54d5eade480 | -21.03656 | -47.96693 | 2025-01-19 12:44:00 | TERRA_M-T | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 655016fa-221f-32ff-9f4f-aa19c3d85d63 | -17.87547 | -50.40756 | 2025-01-19 12:44:00 | TERRA_M-T | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1a5d433c-ed35-3b89-8cda-28addf8e6362 | -21.24226 | -45.76654 | 2025-01-19 12:44:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 2e5f5727-9436-3393-aec2-0f0e24903186 | -20.69672 | -46.55951 | 2025-01-19 12:44:00 | TERRA_M-T | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 73919a41-f19d-3248-aafa-c4b8e3224d57 | -19.99347 | -49.19033 | 2025-01-19 12:44:00 | TERRA_M-T | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e0facd2e-35af-3892-923b-bae815b90c0d | -17.63192 | -50.30477 | 2025-01-19 12:44:00 | TERRA_M-T | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3bc3ab39-fd59-3d69-a615-41f62c9c0027 | -20.89547 | -45.26494 | 2025-01-19 12:44:00 | TERRA_M-T | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 953a79a1-7448-33f2-b429-87f182ebc362 | -20.70451 | -49.15272 | 2025-01-19 12:44:00 | TERRA_M-T | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0d693b5c-adf9-374d-add3-ca9837c21838 | -21.39623 | -45.52331 | 2025-01-19 12:44:00 | TERRA_M-T | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| ce6b0594-afc2-3634-9787-63cd096d407a | -21.24414 | -45.74932 | 2025-01-19 12:44:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 52e3f83c-86ff-37bf-b274-dad498053125 | -28.93825 | -51.54873 | 2025-01-19 12:46:00 | TERRA_M-T | VERANÓPOLIS | RIO GRANDE DO SUL | Brasil | 4322806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 68e2b739-c8fc-3648-b4cb-a41235b84f81 | -22.50767 | -50.10708 | 2025-01-19 12:46:00 | TERRA_M-T | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1719bab9-319e-3dab-a45f-fc859a24b218 | -23.29169 | -47.53354 | 2025-01-19 12:46:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 150dd304-6541-37e9-9de5-7cd8cf421efb | -21.56056 | -49.69918 | 2025-01-19 12:46:00 | TERRA_M-T | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 8eddc6b9-47df-35e1-b2a7-09e377ac42fe | -24.01952 | -47.33171 | 2025-01-19 12:46:00 | TERRA_M-T | MIRACATU | SÃO PAULO | Brasil | 3529906 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 0612162e-d7be-3b97-b42b-8dd41691257d | 2.9089 | -60.5976 | 2025-01-19 13:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 05d64b85-fc3f-3e36-a4c3-e6a30bdaf714 | 2.9089 | -60.5976 | 2025-01-19 13:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 101.3 |
| e1f15b13-fbbb-343f-932e-9cfe9cf10253 | 2.9089 | -60.5786 | 2025-01-19 13:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 72b1bf7a-1bd0-3bc7-bd9c-e2f9d64567bd | 3.2576 | -59.945 | 2025-01-19 13:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 583fe672-d6b6-3d91-9c96-ece8321c54ff | 3.2759 | -59.9447 | 2025-01-19 13:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 23f5db35-8c69-3c37-862f-8d879d604945 | 3.2759 | -59.9447 | 2025-01-19 13:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 145161f0-6b50-3973-9ff1-9c60275d7882 | 2.9089 | -60.5786 | 2025-01-19 13:40:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| bfb9944f-b7a6-3d93-ade2-52f4e680f478 | 1.3586 | -60.027 | 2025-01-19 13:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.4 |
| f6ea0487-db32-3fd2-bd6d-5cc37dec5895 | 2.9089 | -60.5976 | 2025-01-19 13:40:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 702ea3fa-f28b-3e19-980a-c09417b4fbd5 | 1.3586 | -60.027 | 2025-01-19 13:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 0e78eee4-0f1a-34fd-af46-5a60cf9eb286 | 2.9089 | -60.5786 | 2025-01-19 13:50:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 9272f4a9-4511-3dfc-9aa3-626fc5b35268 | 3.8756 | -61.2431 | 2025-01-19 13:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 87.3 |
| cdc080a2-a273-341b-8dd1-0114b4bd1d20 | 2.9089 | -60.5976 | 2025-01-19 13:50:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 15923508-4a92-36bb-80aa-0d01887d6ed4 | 2.9089 | -60.5976 | 2025-01-19 14:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 91ebd7b5-742a-3c6b-bb65-09828225ea37 | 2.9089 | -60.5976 | 2025-01-19 14:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 381eade1-a5b6-374a-9f1f-90297256d6bd | 1.3586 | -60.027 | 2025-01-19 14:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 804f74d5-27da-3f2d-9cee-93394387394c | 3.1276 | -60.7647 | 2025-01-19 14:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 8d38213a-a519-3eba-ba24-d104cb4c1c6d | 2.9089 | -60.5976 | 2025-01-19 14:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 91bd7f1d-1cf7-3921-ada5-83967d6bbe67 | 3.8756 | -61.2431 | 2025-01-19 14:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 9f8f6bfd-2d3e-3833-9038-ade5aa01dda7 | 1.3586 | -60.027 | 2025-01-19 14:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 9c1062c9-ab2d-344d-aa17-3531bb864c8b | 2.9089 | -60.5976 | 2025-01-19 14:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 19097e19-0143-30c0-9197-a85cd6f44687 | 3.1094 | -60.765 | 2025-01-19 14:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 87.7 |


[Clique aqui para ver as próximas entradas](README6.md)
