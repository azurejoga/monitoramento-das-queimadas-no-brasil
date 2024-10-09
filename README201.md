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

## Dados Diários - Página 201

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26b9f07f-2506-3917-9f3e-91fce983032a | -16.94409 | -57.4535 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 72709e15-ed33-3d53-8f62-50a78fa54165 | -16.94353 | -57.45713 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 292e1a19-af3b-3860-8940-06582a469edf | -16.94297 | -57.46076 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cc657eff-ec39-3e0f-95e7-67ad3ccb5e40 | -16.94242 | -57.46439 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9ada13e4-6d5e-3115-a9cd-6d4959472757 | -16.9402 | -57.45658 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 02641826-afb0-3c9b-abb8-d41236d6b4fa | -16.93909 | -57.46383 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 18974cac-b5e4-3129-95b0-d8ce1c9c5002 | -16.93632 | -57.45966 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 85c626ab-1c1d-39a2-baf8-f0b4028d5c51 | -16.93576 | -57.46328 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e946de5a-85c4-31d5-a9cc-eb50249944fe | -16.93244 | -57.46274 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8c5c0595-51eb-3927-8670-edfa8c6f8eef | -17.16206 | -57.4259 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9d21f5af-8c39-39bc-a5f4-1d391e2cf33f | -17.16094 | -57.43319 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f664cbc0-1931-32be-8a3f-dd44d7d34606 | -17.15983 | -57.44048 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| deca72a4-7974-3858-8017-220690228d76 | -17.15929 | -57.42171 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 620e355e-502f-32e1-bfdc-af494aeea068 | -17.15927 | -57.44412 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 426a730b-722f-34e6-b61b-7e2b1c6ecfd4 | -17.15873 | -57.42535 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f655896a-c87c-3730-896e-b4dcab575b97 | -17.15817 | -57.429 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 09e40f73-b37e-367d-b846-9ff7eb7ebb48 | -17.15815 | -57.4514 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6e323a25-47e9-3589-832c-198739d10890 | -17.15706 | -57.43628 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 81bca2a5-9004-30c3-9afa-805c971e5542 | -17.15596 | -57.42116 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 43932f18-4be2-301b-b8e9-2a19265e6324 | -17.1554 | -57.4248 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 269aed16-fc9f-3b00-8de1-ca6358af9200 | -17.15484 | -57.42844 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 069149e1-9818-3bb7-81eb-746828080dc8 | -17.15483 | -57.45084 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 35d45fe2-006c-37d4-879a-8cdccb13b049 | -17.15429 | -57.43209 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 4131b4a6-3c47-3bdc-be1f-56a9cce6aca9 | -17.15373 | -57.43573 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f4f754e0-27a7-3d1b-91cc-02c1a1bb04e8 | -17.15318 | -57.41697 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a18fe2ad-187e-3093-98a1-1880a501fda9 | -17.15317 | -57.43937 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7e9f58c6-2778-34cd-8e9e-ea26ebbc24c1 | -17.15207 | -57.42425 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0c2bc98b-4969-3045-8988-a79470c4bdd0 | -17.15094 | -57.45394 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 50f162e4-b46b-3b85-90db-657ee3f2962c | -17.14983 | -57.46121 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e74ef019-75ae-3225-a785-50ae02794dc2 | -17.1493 | -57.42006 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a401d1e4-c7cb-3830-97db-70c7db7c04e8 | -17.14873 | -57.44611 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 2e4664bc-f739-3295-9dd7-6627d7ea42a6 | -17.14817 | -57.44975 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a8f06663-6051-3cd3-a020-f018fe8ad639 | -17.14763 | -57.43099 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ce9aaa1e-e689-3157-82bf-96a216e74436 | -17.14761 | -57.45338 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f3831824-35b2-3716-bd3f-f95511cb4e38 | -17.14707 | -57.43463 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 44b6f3bf-3e80-3f80-a8b7-c1190d2f1802 | -17.14263 | -57.44136 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 923af2a4-92df-3aa7-b3d6-9a592b4b6917 | -17.13984 | -57.45955 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cb59be3a-d0ab-3436-a3cc-ade11197d51d | -17.13764 | -57.42934 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9985244c-66fa-3f11-a173-d949b0e5a40e | -17.13763 | -57.45173 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 21dfa681-a3ca-3927-aecd-1afe12d709c7 | -17.13487 | -57.42514 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d232c0e5-fd18-3298-9892-2d0253e55b32 | -17.13431 | -57.42879 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 411a6034-f290-34e6-b8dc-09f20f9b69be | -17.13376 | -57.43242 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f1e5203b-5951-39a2-a497-816ff7016705 | -17.1332 | -57.43607 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1a0e2c31-f034-3202-ba70-5c35e4e1bb61 | -17.73356 | -57.07659 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 13c55414-9bc4-3945-8a4f-21c64f4ee372 | -17.70835 | -57.06102 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6da192e7-2bab-334a-bcc7-7608d8eb2b09 | -17.17528 | -56.95377 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e7005097-86b2-3ca7-ac3d-6e07880b3b81 | -17.15214 | -56.82058 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a0691440-802c-3cff-8a13-5e99d4e341e0 | -17.15158 | -56.82431 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7c8fa17c-68fc-3753-8a9e-37de17fc4e29 | -17.15102 | -56.82804 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 38fdbf9b-d5a1-3660-9097-92b5487777a6 | -17.15046 | -56.83178 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3afe10b1-28f5-3a7f-a9f1-1b8963816420 | -17.14989 | -56.8355 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| da0a43f8-e030-388d-84f1-31cafec9c659 | -17.14933 | -56.83924 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 139647fd-805e-3218-be4c-f6a01b22742b | -17.14877 | -56.84296 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| c41adb05-8a85-38ee-9087-833a72f7d27a | -17.14821 | -56.84669 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 786dbbb5-79c8-34bb-a233-0e4f028ab17a | -17.14821 | -56.82376 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 41b782f0-32d4-33e7-8a03-fcb5238ef522 | -17.14765 | -56.8275 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ab4e8926-c6c5-388e-9ade-aa7bd9df17de | -17.14653 | -56.83496 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 9e3f3c77-823b-31a1-8a8a-850741314d11 | -17.14597 | -56.83869 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 2dd57d3e-4d9b-3a69-94fd-e5de69a94abd | -17.14541 | -56.84241 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 162f2d11-301a-37b4-bd8b-049813a5596a | -17.14485 | -56.84615 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9324fd62-eb4b-3a9d-b4de-2ffdf56e4777 | -17.14429 | -56.84987 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8c2d360b-b613-37a7-860a-641674e135f0 | -17.14204 | -56.84187 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a7144aeb-3c24-3e15-b297-0cebc4a21655 | -17.14148 | -56.9598 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| be66a477-6234-32d0-89e4-a3005d97fdf0 | -17.14148 | -56.8456 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2cc173df-87b6-3c3e-8e58-a994a31c59d4 | -17.14092 | -56.84932 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9b734f3a-d663-3c36-a285-8af3c018b75b | -17.14036 | -56.96721 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6c2a563d-1b7a-32ed-ba21-5ef060386430 | -17.14036 | -56.85305 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| af7f917d-083a-34f4-92e5-b69531cd28ce | -17.13811 | -56.84505 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 342d9d08-ed04-31d9-bdab-aa48a5356b74 | -17.13755 | -56.84878 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 58ecc707-f22e-345a-9e39-11d7a47d8032 | -17.13699 | -56.8525 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a7c11610-8461-3995-91a4-dcdb650a575c | -17.13475 | -56.84451 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1f451b6e-bbc4-3335-9899-f615d3451646 | -17.13419 | -56.84823 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4b08bf65-1b7e-3daf-accc-3bb8380a3c1c | -17.13363 | -56.85196 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 3356190b-7e48-3594-b54f-e3d45d442edd | -17.13082 | -56.84769 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bf3915a0-99e3-3b07-9fa2-fcb74baf78e2 | -17.13026 | -56.85141 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| a78b7d5d-7df0-348d-a040-bc4a43c16a8b | -17.12971 | -56.85513 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 881c23a3-cafe-324a-b7c8-71a4a7effb6c | -17.12746 | -56.84714 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f02f2ed4-c5b4-3442-af1f-0e6a714c2c1e | -17.1269 | -56.85087 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 24e9e950-affc-33c4-a728-5ad6e4888be5 | -17.12634 | -56.85459 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 58751ea5-5bdf-3b27-80f9-d6168738bc5c | -17.12353 | -56.85032 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0aca0001-eb2c-3362-81a7-3ebbec54e630 | -17.12297 | -56.85404 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 94d39b0a-6e24-37c3-8587-f7efa32922d9 | -17.11905 | -56.85722 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f8b833d8-01f4-3fae-8c19-7a0276c49b43 | -17.11849 | -56.86095 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 501193d9-6fb6-3086-b758-78ecf15d1b7a | -17.11569 | -56.85667 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e511df75-2a06-3f79-9fae-ea31170a385b | -17.11176 | -56.85985 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e1af5afc-9f87-3222-a04f-79884cace236 | -17.10615 | -56.85131 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fa91bbf2-cc8f-3dd0-a879-9ad994824825 | -17.10559 | -56.85503 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 49c5ae7a-8c51-3e8e-a764-59a51d935c95 | -17.10503 | -56.85876 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 65252dae-35eb-3f6c-a890-a5755b013eaa | -17.10278 | -56.85077 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a2bd62da-7e65-33f2-a341-113454b66150 | -17.10223 | -56.85449 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e2fa12ac-24a5-3571-9aeb-2bd0cceb808b | -17.10167 | -56.85822 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a82607c3-30eb-3ae8-8943-a29bdcc3323c | -17.10111 | -56.86193 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f806c55b-6a37-34d0-b703-ad2afb09d56d | -17.10056 | -56.86566 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1508b893-c410-3f0a-acb8-a8d3624adcfe | -17.09942 | -56.85022 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6c449f87-8962-3e16-89c0-ea630e6967c0 | -17.09886 | -56.85394 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7b81f65f-e577-3100-8cd3-af362fa031c2 | -17.0983 | -56.85767 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 79c513ab-b23a-3c17-9a50-0ef352365de3 | -17.09775 | -56.86139 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a5db78d6-b857-3b91-b348-b2e2337ad327 | -17.09719 | -56.86511 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b8155000-4382-336a-9b3f-130f23ee3f44 | -17.09664 | -56.86884 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 478e81ec-5420-37a4-ad33-538c2bad47a9 | -17.09494 | -56.85712 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README202.md)
