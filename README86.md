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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee25e7d4-1654-3908-9e82-76592e1925d0 | -10.93779 | -63.86538 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7743bd0b-58a0-342c-a64c-07035806c1b7 | -10.93623 | -63.87375 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 410526e5-2fc1-3138-b39a-d631747a0482 | -10.92051 | -63.84553 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6324e4e9-8a6e-3b31-8f86-ec2b7fdb0337 | -10.92002 | -63.84814 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d76f003d-a71f-3c67-881a-002d9d8c5c7e | -10.88959 | -63.92599 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23572c0d-40dd-3468-aa36-d36a0770df23 | -10.88899 | -63.92916 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 910ed567-70da-3dd2-b750-139c05e9a02f | -10.86122 | -63.92022 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efe54fde-264a-36a9-b783-f7998bdf0db5 | -10.86067 | -63.92318 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ac4535a-de86-321e-9c1c-7a8b97bdc284 | -10.8593 | -63.90192 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 158a0802-8ff7-3950-a42f-375566dc0693 | -10.85891 | -63.92081 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9478d51-49bb-369b-b158-aa0bf9133b7d | -10.85877 | -63.9048 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9187db45-2e26-32b4-8667-d69299704b29 | -10.85833 | -63.92384 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5a7f7af-6300-37d3-8ae4-7315601425e9 | -10.85824 | -63.9077 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87f34a14-f534-3cfe-9e34-664d4069004d | -10.8577 | -63.91063 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61d95629-e4ae-3075-b493-0ac04bd03183 | -10.85316 | -63.9067 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f10d54e-e403-39aa-90a1-9031ede71c86 | -10.83067 | -64.20866 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5153b017-56fe-3ac4-9342-cf32139f4d41 | -10.83005 | -64.2119 | 2024-10-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcb2e23b-7e1c-3b6d-b923-a09cb027e626 | -12.47755 | -63.89719 | 2024-10-12 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 041a0567-020b-3823-bc63-8496ece49af1 | -7.34762 | -64.69035 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1dc46f4b-3cdf-387c-9115-aed235fd1b55 | -7.3099 | -64.67134 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b10dd75f-386b-3612-b2de-bd831acaf506 | -7.30918 | -64.67529 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca6f4f5b-8a86-3592-ac7d-331422112095 | -7.30348 | -64.67428 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab603b73-254b-3e3e-806e-f557faa117b9 | -7.30276 | -64.67824 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4edf1fc8-5133-3bea-b9b9-50baf2865ada | -7.29996 | -64.66138 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d116b388-5607-3c35-94a9-f9e8af3fd44f | -7.29924 | -64.66534 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1575b641-5572-32dc-8ab7-7ebedccd3517 | -7.29354 | -64.66433 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 293ebf91-7899-3b18-a90c-0d92560c52c9 | -9.39866 | -64.41732 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf34f35a-a146-39f7-b5a8-77a3ef1f4964 | -9.8925 | -65.00503 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18f552d9-ee94-38ef-b407-2c75d133e67d | -9.89189 | -64.79386 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6beb903-0538-3a31-8077-706724a370aa | -9.89179 | -65.0088 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7795572d-b84a-3d95-9c1a-f29f0a6b512e | -9.8912 | -64.79749 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd0d9413-1649-3c92-80eb-ed74a4d70140 | -9.8911 | -65.0048 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fba64a0-455b-31e5-9406-8f7163f6e061 | -9.89052 | -64.80113 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6d44011-ea70-383c-bd78-927c83da12e7 | -9.89037 | -65.00858 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ef8c796-920c-3876-b513-429731659322 | -9.88984 | -64.80476 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 79b41cca-6425-3070-963a-4e918e66107a | -9.88916 | -64.80838 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fe2f1d46-745e-3217-af73-e873c31e6b1e | -9.88848 | -64.812 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f72bfa85-0976-3a47-8082-054fbf4e2ed2 | -9.88779 | -64.81566 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c0fe0ce3-1935-3a5b-86aa-5619d64d5951 | -9.8871 | -64.81935 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 893e0005-c012-34f3-ba60-33a2141baaab | -9.88692 | -65.00401 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c57b87ff-2be9-328e-9f4b-a335e9a90978 | -9.88622 | -65.00777 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d68fc366-c2ea-302a-be5e-d71f6045747a | -9.88434 | -64.80378 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 071ae6de-83a2-359b-8cba-010665c1e942 | -9.88365 | -64.80743 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6999271d-0c36-3b61-aeb4-add26e3b7bab | -9.88296 | -64.81108 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69ad41df-05fa-3c2b-b942-28d6d8c960bd | -9.88227 | -64.81476 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 892d1745-2bb8-3f10-9e11-028d87b00dbd | -9.88158 | -64.81843 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82e7792a-a7e0-3479-a147-31ade87c0973 | -9.74885 | -64.88707 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be0724ce-de0c-33e5-aa44-0b5b05b06627 | -9.74402 | -64.88228 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9ecea1f-9347-35ab-a2fd-7d856bdea43c | -9.73849 | -64.88123 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 594dad66-ad4b-3b87-955d-37337c7e2d66 | -9.56538 | -64.62216 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83306709-001d-346b-a1cc-b234d07a9c08 | -9.53886 | -64.57818 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a977eef8-a9aa-3ec3-bc14-f1cd98b5db48 | -9.5334 | -64.57722 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d7cea00-2709-3596-b63d-96b824fe2e53 | -9.49357 | -64.67033 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38101c2b-ef15-34b4-962a-3fc76d72217e | -9.36269 | -65.74881 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cbc7fb8-d285-3864-9f26-3a6192ba65fc | -9.36188 | -65.753 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38b496a4-a6e7-3bf9-a437-276869e177fe | -9.3584 | -65.73938 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d6b56b8b-23a6-35bd-9faf-66757033e3dc | -9.3576 | -65.74355 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 150c36b2-dd0e-34f4-a81f-a692beb9eae2 | -9.35679 | -65.74773 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 02a851c7-062f-3a22-a614-2adb3ed35644 | -9.35598 | -65.75198 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 92ecdf15-aa88-3440-acea-909f679da829 | -10.06432 | -64.93602 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9545cb11-bdf0-39a4-9834-b8c386ce2dad | -10.05881 | -64.93493 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4788756a-0ee2-30da-920c-83c10c6bc232 | -11.46337 | -43.92642 | 2024-10-12 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 777e6fd3-fcbd-3a8a-9915-8e48c55510fb | -11.46281 | -43.93122 | 2024-10-12 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e33cf48c-61d0-394e-a583-63e4eba45e83 | -14.0846 | -44.61891 | 2024-10-12 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0106509d-33f7-32f0-8143-9b4f2dce7f70 | -12.32358 | -45.32624 | 2024-10-12 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d44fa165-499e-3ee7-92a4-f4223f74ea15 | -12.3231 | -45.33012 | 2024-10-12 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4033b84-16d6-3275-a589-f989b8cf15af | -12.32021 | -45.3272 | 2024-10-12 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 526e88a5-2fb8-3d35-af9e-1df1c9ca0ff2 | -12.32588 | -45.32808 | 2024-10-12 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b7b980c-ce9d-3ad3-9174-bcca44b10235 | -10.84166 | -44.43775 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ecf280c2-4b38-3051-9bfd-d6b03683e3d9 | -10.84115 | -44.44197 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ab0d0d7-28b4-3d20-abe2-264e3d6a2bf7 | -10.83663 | -44.441 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ba9a718-1bb6-35b4-a75f-b144ec050927 | -10.82692 | -44.94635 | 2024-10-12 04:59:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef45044e-d17f-36a5-884e-33f9d024b167 | -10.95864 | -44.64511 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 425ae615-35ca-373d-8d5d-a95a0f3db790 | -10.95812 | -44.64933 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4559d683-a506-3050-800c-fc472e696c8e | -10.95761 | -44.65353 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6c570e8-4659-327d-bfbe-bf35cb13f03b | -10.9571 | -44.65771 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca57a9c6-4f4d-3e63-989e-cf73f32443bf | -10.95607 | -44.66611 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf16fedd-bf53-318a-800f-1d2a43a22e16 | -10.9528 | -44.64435 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3bdf5483-611e-33b9-b6ae-6a12751e1fbf | -10.95229 | -44.64857 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b41382a-236e-332e-9381-8e3141ad1d97 | -9.19488 | -66.09396 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e737c7a8-cd76-3dc6-8e19-aaff68dbac3c | -8.70354 | -67.00034 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d3811a8-ec5b-34a9-b53e-afeb3987f801 | -8.69607 | -67.00452 | 2024-10-12 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcc92689-4861-3451-80e8-e100f9c66a1b | -10.95178 | -44.65279 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd1e6568-c48a-3aa3-859a-86503c3f24b7 | -10.95127 | -44.65698 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22149703-54ee-307d-91ac-88ef5d9350a3 | -10.94697 | -44.64361 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 13bc724b-8e10-31f3-bdb9-aa879577e05f | -10.94646 | -44.64783 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3bf6e8c-f524-3d98-8144-1a48411c884a | -10.94594 | -44.65204 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51bbf053-b580-3dbf-b6a9-a0ce22639975 | -10.94113 | -44.64285 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c94deb55-4045-3d9d-b140-a9af4d6f50a9 | -10.94062 | -44.64707 | 2024-10-12 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4d5c4ca-2c06-3897-a456-765db830616f | -11.93593 | -46.58747 | 2024-10-12 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c21bac1b-0791-300d-ae02-4e0c4c2e4150 | -11.50303 | -47.32092 | 2024-10-12 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2c51ee9-19da-3806-bc97-5c0fad4a13d4 | -11.33407 | -47.08811 | 2024-10-12 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bd755d1-5c1e-30b8-9504-64d515b189a1 | -10.4768 | -47.66216 | 2024-10-12 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 87ceff29-9281-347f-9254-62f7e877e083 | -10.47609 | -47.66749 | 2024-10-12 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18e2ac43-eff5-30ab-92ab-55da0c16546f | -10.47207 | -47.6615 | 2024-10-12 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bd9a41d7-80d4-3bba-bf9a-ae29e50e261b | -9.74496 | -48.29686 | 2024-10-12 04:59:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3f059bb-fe3e-3f69-8176-da240f556487 | -9.74424 | -48.30212 | 2024-10-12 04:59:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 764bd81f-2077-3700-9835-7548f619ce3c | -11.20919 | -47.84769 | 2024-10-12 04:59:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 917438e9-f80e-358f-b6a9-08da98ce987f | -11.20852 | -47.85271 | 2024-10-12 04:59:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 303fcba8-e827-371a-8873-1a44e8eed226 | -10.56667 | -49.94273 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README87.md)
