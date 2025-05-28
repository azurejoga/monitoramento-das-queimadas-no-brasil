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
| b9640f3f-5153-3e5f-bacb-3b016ff7620c | -7.6762 | -46.0995 | 2025-05-28 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 1c32c499-89e9-3ba7-b829-67ba1d1b9faa | -7.6136 | -43.4043 | 2025-05-28 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 77b5577a-201a-3b7c-92cd-2c3d447aea0e | -7.983 | -50.699 | 2025-05-28 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| fd22f6d2-a07b-3004-b2cd-687e8119c30c | -7.9827 | -50.7201 | 2025-05-28 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 8e1e3a13-4159-3a4a-b805-b129debe1ba8 | -5.7711 | -43.4985 | 2025-05-28 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| ae987b14-fa92-3932-b237-52d3c781fb27 | -5.7713 | -43.4752 | 2025-05-28 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 4e663f98-6203-3b80-8a8d-c9a59708119a | -13.0874 | -45.2791 | 2025-05-28 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 257.4 |
| 3f9a6b90-9f52-39c3-886a-7881645f88c9 | -7.964 | -50.7215 | 2025-05-28 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 2708b4d9-43b6-3a17-bff0-1cb6214005f1 | -14.681 | -45.0956 | 2025-05-28 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 1fabbc96-5551-35da-8281-071ad0e386d8 | -7.9827 | -50.7201 | 2025-05-28 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 31f187fb-ae9f-3810-a0e7-79a3377691a4 | -7.6762 | -46.0995 | 2025-05-28 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 0647e306-4de7-3bd6-92a4-93932b088767 | -7.964 | -50.7215 | 2025-05-28 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 7dc3a118-e6d7-3749-8af3-12d541af76ea | -13.7065 | -45.2454 | 2025-05-28 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| de9bfb2a-bb7e-3510-a208-1a2fb13575fb | -13.0874 | -45.2791 | 2025-05-28 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 264.2 |
| a5f2192b-11fb-3c9d-ae2d-6f6187a589ec | -5.7713 | -43.4752 | 2025-05-28 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 6d00dd8d-c6cf-355d-875a-c33c11c81e63 | -14.681 | -45.0956 | 2025-05-28 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 171.5 |
| f2d488fb-3789-3ec5-9eb9-5c14931f33df | -7.983 | -50.699 | 2025-05-28 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| dc1791df-aee0-3f2a-91c0-02d3d503a7cc | -5.7711 | -43.4985 | 2025-05-28 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 04e40cf4-35e6-32e1-93e6-87d567e96810 | -13.0681 | -45.2823 | 2025-05-28 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 4956a0e7-4ae7-32d8-9775-f6ff1ab0688c | -7.964 | -50.7215 | 2025-05-28 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 5a833288-7f79-346b-9f39-c98cd54db15f | -14.681 | -45.0956 | 2025-05-28 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 176.0 |
| a7019215-9f3d-3bc5-9d01-4c8628df6b77 | -13.7065 | -45.2454 | 2025-05-28 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 144.7 |
| de2300ea-40f4-3240-93f9-0b634bd0dc9c | -7.983 | -50.699 | 2025-05-28 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 8ea7f2e2-5491-34c9-a8d4-832c45d17096 | -12.3324 | -49.9857 | 2025-05-28 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 183.6 |
| b4fdf262-8c9f-3eec-acc3-67496138b941 | -13.0874 | -45.2791 | 2025-05-28 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 258.2 |
| dea1c852-8011-3853-88c4-6bed38fdba89 | -5.7713 | -43.4752 | 2025-05-28 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| f59efb24-c639-343d-a664-f5676b4bb933 | -7.9827 | -50.7201 | 2025-05-28 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 9988febb-cac0-39c7-89fb-6e509b22579a | -7.6762 | -46.0995 | 2025-05-28 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 9b70f0c8-d9fa-33f9-815e-c3118438feb0 | -5.7711 | -43.4985 | 2025-05-28 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 759365f1-5614-3d59-9c8e-5328046bd4f8 | -12.3519 | -49.9617 | 2025-05-28 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| e485f9ad-0b59-32d9-8a94-ac67d72e2ac8 | -7.9827 | -50.7201 | 2025-05-28 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| e31fb3c3-20bf-37d5-af3e-f6e03167f526 | -7.6762 | -46.0995 | 2025-05-28 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 0ce352b7-17bf-3260-a605-1dade662b9e8 | -12.3327 | -49.9641 | 2025-05-28 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| e0f5d610-cafb-333f-9c21-5d641b2294cb | -7.964 | -50.7215 | 2025-05-28 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d1e7b43a-e1e5-33b5-ba46-b3c5eb35e806 | -12.3133 | -49.9881 | 2025-05-28 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 230.8 |
| 9e4fada3-7c01-3f77-ae09-e79f60533779 | -5.7711 | -43.4985 | 2025-05-28 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2ebcb716-44b4-38ce-9f21-53d0acdb0f4d | -14.681 | -45.0956 | 2025-05-28 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| c4a2dbc9-869d-3591-ac7f-94d73d54ebab | -13.7065 | -45.2454 | 2025-05-28 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| beeb447d-90ab-3abe-bb6a-823dc60d9032 | -5.7713 | -43.4752 | 2025-05-28 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 1be1cb11-9493-38e3-9bf9-803888bb946d | -14.6816 | -45.0721 | 2025-05-28 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| cd5deb8d-5b08-32b3-be13-592e31edfcfe | -13.0874 | -45.2791 | 2025-05-28 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 271.0 |
| 19863d07-6445-39ae-b9f8-756858e49c15 | -7.983 | -50.699 | 2025-05-28 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| fecccde3-d7f0-3922-8446-514f43456165 | -12.3324 | -49.9857 | 2025-05-28 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 208.9 |
| cd039a92-3cba-3f1b-b5ae-86f5143e592f | -7.3248 | -43.9449 | 2025-05-28 14:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 47f62ca6-4499-3acf-97fb-f5eebe3ee9e9 | -12.3519 | -49.9617 | 2025-05-28 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| a1e3672f-1da6-3812-a67c-35b0f56fd2ea | -7.6136 | -43.4043 | 2025-05-28 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 78f6799d-b939-3158-941a-d631b2a675cf | -14.6816 | -45.0721 | 2025-05-28 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 91e7f916-3df9-3f6f-9a4f-c04aa601f260 | -7.6133 | -43.4277 | 2025-05-28 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 6174d491-ad15-3603-ada3-92507856d12e | -14.681 | -45.0956 | 2025-05-28 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 978e9f3c-34dc-345c-b52f-15bf46d15fa8 | -7.6762 | -46.0995 | 2025-05-28 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| a2a61d87-af34-3de5-bc6d-97f4594c99b5 | -5.7713 | -43.4752 | 2025-05-28 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 0834ff79-87f8-33be-9536-eb6e5fa0d9ad | -13.7065 | -45.2454 | 2025-05-28 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 149081db-8c17-3601-8f65-f5108506c347 | -7.964 | -50.7215 | 2025-05-28 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 1c8c44af-eeeb-30b7-b592-7d9f4b423036 | -13.0874 | -45.2791 | 2025-05-28 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 234.6 |
| be5c00d3-920b-3be7-9e53-ac5e8ea7900e | -7.983 | -50.699 | 2025-05-28 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| c6ab048d-a2f8-3427-87b4-510efb81758f | -7.3245 | -43.9681 | 2025-05-28 14:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 8bb9ee5b-4956-34a9-8f06-61203f91e4a6 | -7.9827 | -50.7201 | 2025-05-28 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 5c28c5cd-305b-3ce7-8c74-c4c0a1154779 | -5.7711 | -43.4985 | 2025-05-28 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 05031b81-7b4d-323c-a48b-91e85bf24020 | -7.6762 | -46.0995 | 2025-05-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 6cfa3a52-2401-3cdf-b22e-33c23e734725 | -14.6816 | -45.0721 | 2025-05-28 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 25d90412-5920-3066-8786-03bf90f69756 | -7.9827 | -50.7201 | 2025-05-28 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 089038b4-d293-324b-ad4b-dd938d477b53 | -5.7713 | -43.4752 | 2025-05-28 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 02b14c8c-6ba5-3a75-8db5-20284b7188eb | -13.7065 | -45.2454 | 2025-05-28 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 4545715a-e7bd-3982-a569-f021fe913e38 | -13.0874 | -45.2791 | 2025-05-28 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 243.6 |
| 71d2c602-1d38-3fce-af30-855969c44161 | -8.8939 | -45.094 | 2025-05-28 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6d22b7c3-9e77-3cc6-9762-3db5f26c62cf | -7.964 | -50.7215 | 2025-05-28 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4ac999c7-ba15-3a14-983a-029f6260f797 | -5.7711 | -43.4985 | 2025-05-28 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 6d8c9559-79f1-3eb9-b4b3-a9ac5dc391d8 | -5.7713 | -43.4752 | 2025-05-28 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 7270e33e-9e27-3e8a-8df4-9650f3e3ffc7 | -12.3133 | -49.9881 | 2025-05-28 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 273.9 |
| 00573337-6947-3465-9441-94bbde802380 | -12.3324 | -49.9857 | 2025-05-28 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 198.2 |
| 508fe716-876b-33f6-ad13-5a9eeb9dff61 | -14.6816 | -45.0721 | 2025-05-28 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 140f8215-d5c5-33a5-9afb-613fc4854a6a | -7.6762 | -46.0995 | 2025-05-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 9e018828-3d47-3f9b-b05a-cd39a2a9bf60 | -8.8939 | -45.094 | 2025-05-28 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 42b86aa2-f57e-399e-86c4-20e730421633 | -7.9827 | -50.7201 | 2025-05-28 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| f2292e19-4add-3cc7-872e-bd8dc704093f | -13.7065 | -45.2454 | 2025-05-28 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 2c68e79b-514d-3c29-a942-ded0f3b8258f | -12.3519 | -49.9617 | 2025-05-28 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 7f315838-5121-3ac5-b98d-6d2d727f13da | -13.0681 | -45.2823 | 2025-05-28 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 0da516c6-45ba-3b19-9925-0511145550dd | -7.6136 | -43.4043 | 2025-05-28 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 7c250def-1b97-34bd-bcbf-5884f29da316 | -13.7065 | -45.2454 | 2025-05-28 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| c27e6120-ec10-3c6e-835b-3a103bb146c0 | -13.0681 | -45.2823 | 2025-05-28 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 63c4cb11-170e-325a-ae68-b25eb3725412 | -6.3348 | -43.3832 | 2025-05-28 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 097fab1c-f408-36a1-a0c9-ffaffeb7f6ac | -12.3324 | -49.9857 | 2025-05-28 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 220.0 |
| fba7da8c-3779-36bd-a9ab-01fcd5ce92c1 | -12.3519 | -49.9617 | 2025-05-28 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 595c3bba-403c-321a-82bd-044c59fc0ef7 | -12.3327 | -49.9641 | 2025-05-28 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 7b25c439-fff6-3ef4-82ef-49d2c8c2c142 | -7.9827 | -50.7201 | 2025-05-28 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| de904d49-1773-381c-9c64-81941cbea28f | -7.6762 | -46.0995 | 2025-05-28 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| ff8137ff-a575-3a39-a920-64b54e061136 | -12.3133 | -49.9881 | 2025-05-28 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 207.6 |
| be3aadf7-b9cf-3956-8a08-f17262de7935 | -7.3245 | -43.9681 | 2025-05-28 14:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |


