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
| dbd4968c-6352-3285-ad7a-0975393b7a61 | -3.0504 | -50.3542 | 2024-11-12 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f6e562f1-7b14-3494-ae8a-409a115090d1 | -2.1271 | -50.7121 | 2024-11-12 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e1c46a99-c8bb-3cd4-ad00-8a96f69fa613 | -3.0689 | -50.3326 | 2024-11-12 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d6c739ca-d3ff-35c3-81eb-538b3865db00 | -2.1272 | -50.6703 | 2024-11-12 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1ff79d3c-8553-3a1f-9bda-3631ba971f5f | -2.1455 | -50.6908 | 2024-11-12 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| f8360095-6c08-300b-94ba-9c66b22f03ac | -2.1271 | -50.6912 | 2024-11-12 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 89797b24-2332-3c09-9a02-52f08250933a | -3.0504 | -50.3332 | 2024-11-12 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| d939e779-a341-3e6a-89b6-35fcf4046c54 | -3.0689 | -50.3326 | 2024-11-12 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 1db3892b-b54f-3776-96b0-1d14232ef1c3 | -2.1455 | -50.6908 | 2024-11-12 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 8f91a63e-3f6f-3455-87f6-0505eacdc917 | -2.1271 | -50.6912 | 2024-11-12 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 184.1 |
| 05b19b2a-5793-3478-8be7-c1085318aeaf | -2.1272 | -50.6703 | 2024-11-12 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 2eefb3a9-97c8-3a79-8622-a624834c2811 | -2.1087 | -50.6916 | 2024-11-12 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 597761a3-5905-3b7e-94e3-e8c82ec9d781 | -2.1271 | -50.7121 | 2024-11-12 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 02876f10-96c8-3891-82c9-d5a83d28b102 | -3.0504 | -50.3332 | 2024-11-12 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| eee3cab0-c567-32f1-8b0a-528d8295f52b | -2.7588 | -49.3285 | 2024-11-12 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0d90d6e3-fd09-376f-a00a-c8de77b32ce7 | -3.0505 | -50.3122 | 2024-11-12 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| bbe46ea3-c156-346d-bf59-2bb977d2b765 | -2.7922 | -50.2986 | 2024-11-12 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6fee4370-0a2a-322e-8eba-614d0d3fa3c2 | -3.0504 | -50.3542 | 2024-11-12 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 47f3f2c1-af61-351b-ad6b-4aff01a9fb56 | -2.7587 | -49.3497 | 2024-11-12 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 912d747b-fc4b-3743-ac32-240872370ff7 | -2.1455 | -50.6908 | 2024-11-12 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 69227879-2881-3f3a-afd5-25488d5a415a | -2.1271 | -50.6912 | 2024-11-12 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 174.1 |
| f22600b4-af7c-38f9-9bec-2db9d48f16f2 | -3.9669 | -48.1716 | 2024-11-12 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b3599d1f-2bb6-34f9-8479-032770747106 | -2.1087 | -50.6916 | 2024-11-12 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 965e121d-61d9-39b3-958f-4e09cc81dbd4 | -3.9668 | -48.1932 | 2024-11-12 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| fb692ea9-8b90-3396-abf5-3f63cbd84dab | -3.9483 | -48.1724 | 2024-11-12 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 02e890f5-348a-378a-b405-70eca0a05752 | -2.1271 | -50.7121 | 2024-11-12 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| d8732e70-7d7a-3cc0-a5d2-024ef1e96f9c | -2.1272 | -50.6703 | 2024-11-12 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 21e6ecdb-7b77-319c-9f7a-f27ee67794df | -2.1271 | -50.6912 | 2024-11-12 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c0d4c0ea-bb27-337e-bb11-5db0ef4096fc | -3.9483 | -48.1724 | 2024-11-12 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 592adbf6-8698-33e9-bbc6-5e25d308b028 | -3.9482 | -48.194 | 2024-11-12 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8fe6c459-4ac6-3188-833b-7d9f55b50510 | -2.13341 | -50.68724 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0fc9a7f-2a9a-38d8-bb5f-6a3d2745bd9d | -1.56012 | -56.03843 | 2024-11-12 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ac7afec-738e-3d0d-8070-26fb21bb41b7 | -2.11355 | -50.68942 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3f73e644-6073-3d1e-ba6d-606c70dd67af | -2.12785 | -50.69165 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| b36aa7b9-d275-31cb-80b0-6a32b2c26cf7 | -2.31589 | -50.68174 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b1d9150d-6fed-3870-b4f3-3b3c48e6bfa1 | 1.05748 | -60.5927 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4394ca16-9fd0-3b3e-96fb-01f473243b28 | -2.76214 | -49.32689 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b421b8c7-eb2b-3ce9-a9b5-439921c55ba6 | -2.75967 | -49.3432 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eec4d2c5-615b-3292-be49-0428db518aee | -1.34413 | -56.05134 | 2024-11-12 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e8e5378-6cbb-3793-8194-c555b1e92d79 | -2.11832 | -50.69019 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 91a4c4d0-b5fd-3089-81eb-8ec3d6ca1245 | -2.1207 | -50.67462 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b00bfb1b-d614-3deb-a6af-9dd6c01b8929 | -2.76733 | -49.32208 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c0a6276-d638-3978-b850-ea0073c1260a | -2.76496 | -49.34397 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30a2d128-f7e6-30b6-8514-5f66819b55e4 | 0.62475 | -60.08755 | 2024-11-12 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f6536d6-a115-3ad2-8b27-32da1cd2e6b1 | -2.76312 | -49.32046 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0556d4e-10c4-3547-9175-66eb4c41c0ec | -2.31668 | -50.67659 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e55e69de-11c7-33b1-8046-a26ddb4365d7 | 1.06172 | -60.59628 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d62c4276-dbab-3c68-b724-44d89c8943cd | -2.12968 | -50.68246 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 141f156e-e794-3286-86d6-58dfabbbad0c | -2.13294 | -50.69351 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e19b40b-2854-36ea-9589-acf506700798 | -2.32146 | -50.67735 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3546c9a-cd4d-3b24-9d83-41879c627ffc | 1.08756 | -60.59661 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1764cde-9293-31c1-a1ae-9ec117228f97 | 0.62125 | -60.08809 | 2024-11-12 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b23e643-1d19-3a43-b982-458d99363477 | 1.06108 | -60.59216 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e78c508b-d7fe-321b-a65d-e051bf223def | -2.32068 | -50.68246 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 469ac1ed-36d0-3247-8aa0-c0feacd42bc4 | -2.12706 | -50.69677 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 97a36a70-4b0d-31d2-a1bb-edc7aaf549a4 | -2.76891 | -49.31792 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1ae2f76-d808-34df-9816-a2a63f6f2f27 | -1.47815 | -54.3271 | 2024-11-12 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 262a99d0-63fa-3824-a65c-a16e3bd7a361 | -2.12387 | -50.68579 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f808439-0a56-3eb5-af5e-daca5d97ba51 | -2.13261 | -50.69238 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7374ba20-7bea-3112-a8c0-45c278c488a8 | -2.76545 | -49.3407 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67acde17-1869-3311-ab64-d9ad45b33728 | 1.52709 | -60.67519 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8223346c-f1ef-3f3d-8b64-da220003db6a | -2.12229 | -50.69606 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| e4e42da7-91a5-3eb4-b554-bbc72dd20895 | -2.76263 | -49.32368 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61af296e-8d28-35f8-8511-612904215aeb | 1.06299 | -60.60455 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 133dfac4-f288-3b23-9573-7848331ddd6d | 0.19114 | -60.6133 | 2024-11-12 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8630588c-b96c-3e9d-bc44-cfd04bde80d7 | -2.11911 | -50.68502 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9c0b998-f0ae-33b7-a97d-b6e27db21b9d | 1.52644 | -60.67097 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a155b81-a0cf-302e-9845-2a9a33690873 | -1.32532 | -52.48751 | 2024-11-12 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d60a6c4-0d43-3324-84d9-c5c57b809385 | -2.12151 | -50.70112 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 51c4fcd0-c9ec-3f52-98ad-c5c2c1017778 | -2.76017 | -49.33992 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad042919-0ce5-383a-908c-f2e1b3902d4a | -2.12743 | -50.69789 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6274383f-c7f9-341e-836b-bd7d349d3904 | 1.05516 | -60.60152 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f01d31a-b792-3ed7-a37b-c970f335a386 | -2.12818 | -50.69275 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| a47de503-a83d-366f-8045-156ced7b138f | 1.05389 | -60.59326 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e866cad3-01ac-31d2-a191-6aac7547c6a7 | -1.30083 | -54.66881 | 2024-11-12 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 101ef970-3c1a-3a38-a7d3-090df5cc5391 | 1.06003 | -60.60925 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c36feee6-f95a-3635-a204-5381074b89ff | -2.76156 | -49.32458 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7741f6c0-bdd4-3d8e-99ee-140bd03a8aae | -2.75783 | -49.31963 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23912768-fd3d-30c6-9794-d9c706b0a226 | -2.13445 | -50.68321 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 563eded3-344d-3ddf-abc2-58230fd82f41 | -2.12893 | -50.68758 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 7e24396e-42f9-360c-9bf4-bb55829f1c28 | -2.70793 | -49.18001 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5237cbc-2bd1-3080-90d8-d3f93e480e1e | -2.11753 | -50.69531 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 25bfc29a-1256-3221-99a3-0f308ccdecf5 | 1.05092 | -60.59794 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8ff913c-e33b-340f-997e-66fbed3ea37d | -2.1342 | -50.68213 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20389f9a-fda0-3d2b-84b0-ba19f17714ef | -1.28489 | -52.47361 | 2024-11-12 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d7ab741-5b5d-32fc-bf28-cee587a8881f | -1.3051 | -54.6653 | 2024-11-12 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d49fe79e-bf58-3ce8-aba1-dc04a8fe3813 | -2.1337 | -50.68834 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b25309c6-59f8-307d-8b44-0a4a85df7abf | -2.70744 | -49.18335 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcd59cde-7bf8-3b9e-9890-d1d1c4ab79b3 | -2.76203 | -49.32136 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 921f0365-b9c0-3bb6-a9dc-1e9dd1eff5d6 | 0.96877 | -59.74193 | 2024-11-12 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d711871b-b118-348d-af5a-d2676f1d34da | -2.76842 | -49.32117 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f85aea0-6c80-33a6-94bc-9f1ad34f0184 | -2.12943 | -50.68139 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f45f8103-dd6f-367e-bc4a-f5fb7cac4769 | -1.55669 | -56.03791 | 2024-11-12 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 403d37cc-155e-3634-babe-f2d256aeea9b | -2.12416 | -50.68689 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 58921418-5d9b-3004-b381-ac730f35b3c0 | 1.05812 | -60.59683 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc470f90-c371-391a-92ca-e532a0baf2c7 | -1.30446 | -54.66941 | 2024-11-12 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 511c314c-e9a5-317d-ad3a-d4021ab06281 | -2.11435 | -50.68423 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f18aebd0-b1e9-3111-9b24-0c10783cd442 | 1.05939 | -60.6051 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec177eda-6d01-36a8-9232-9518e4126508 | -2.75922 | -49.34091 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9b1ae1e-e8a0-3c63-82ea-e02c1b603f0f | -2.7678 | -49.31885 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README19.md)
