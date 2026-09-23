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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1145c3c-cc85-38c2-b706-917b33e99e21 | -8.378 | -45.6036 | 2026-09-23 11:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 230.7 |
| d40b7f2b-177e-377e-9a6f-f561a01e1aa7 | -12.4216 | -46.9551 | 2026-09-23 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| e3d17056-23cc-30df-9e1d-9a2b3f9c0f78 | -12.4212 | -46.9777 | 2026-09-23 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 1c042971-5be2-38f1-9ef6-c03ad023e6be | -12.4216 | -46.9551 | 2026-09-23 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| ca7500cc-8ecb-353a-bd5f-79583ca0b8b6 | -11.5307 | -45.3553 | 2026-09-23 11:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 253.6 |
| 95abe245-8d28-39a1-885e-9a02ad9fcad5 | -8.9205 | -45.931 | 2026-09-23 11:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| ade25b63-9756-36e4-a71e-39a7ae6ae753 | -12.4212 | -46.9777 | 2026-09-23 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 6794da9f-6676-3516-9657-64e71f8627fb | -12.402 | -46.9804 | 2026-09-23 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 0a68802d-9baa-3e68-adc1-96ad740a6610 | -11.5499 | -45.3526 | 2026-09-23 11:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 235.5 |
| 0971c737-d644-3cfa-9fbd-82156a98bbfa | -8.3591 | -45.6056 | 2026-09-23 11:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 256.9 |
| 05e5822d-bc91-3101-acb4-f87a98fc122e | -8.3783 | -45.581 | 2026-09-23 11:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 226.3 |
| 992ebd04-16c5-346a-81d5-1cf8051d732d | -8.378 | -45.6036 | 2026-09-23 11:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 275.9 |
| 14844c52-cc73-320d-af6a-6e26b7ce3cd1 | -8.378 | -45.6036 | 2026-09-23 11:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| f21b07e8-4e26-3f5a-919d-45f494299430 | -8.8105 | -44.2757 | 2026-09-23 11:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| f03d2382-e5f1-3b78-9604-e8de556851b7 | -8.9016 | -45.933 | 2026-09-23 11:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5599356b-565c-369a-97cd-ff4bb9c5845e | -8.9019 | -45.9104 | 2026-09-23 11:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.7 |
| d11e27f6-10f4-3822-8ddf-cd5b3af04631 | -11.5499 | -45.3526 | 2026-09-23 11:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 5587ee7f-e5ee-33b0-82a3-2c06cd810235 | -8.3591 | -45.6056 | 2026-09-23 11:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 9ed77b08-2ad0-3296-bd2b-9278560cb295 | -8.9205 | -45.931 | 2026-09-23 11:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 6d1b3bb3-3f53-302b-9e3b-d5f606433c65 | -8.3783 | -45.581 | 2026-09-23 11:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| cf8e16a3-e82b-3d0a-b660-c9a45fa60126 | -11.5307 | -45.3553 | 2026-09-23 11:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.6 |
| cf41718a-10ec-3b6f-80c7-8adbbe435444 | -8.7916 | -44.2778 | 2026-09-23 11:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| acb3aa51-09dc-3ba7-bf76-3255be1a9975 | -8.9205 | -45.931 | 2026-09-23 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 186.6 |
| da352ef9-c74d-3c47-8c6a-ae3953a3d15f | -8.5992 | -44.5301 | 2026-09-23 11:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 5f971396-70df-3603-a14f-2b625ca9c6bb | -6.6317 | -43.73 | 2026-09-23 11:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 27eb0719-0f7e-39ae-99f5-153b1313afc0 | -11.5307 | -45.3553 | 2026-09-23 11:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 82e7cf9e-010f-3346-9eba-02d0a4338b28 | -8.8105 | -44.2757 | 2026-09-23 11:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 490afdc9-ee5b-3a93-b7a6-1d8174f2d0b3 | -8.3591 | -45.6056 | 2026-09-23 11:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| a62694ba-2542-3118-afdd-e383f784654a | -8.3783 | -45.581 | 2026-09-23 11:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 7eed8eb7-5eba-3d06-9b58-bd4e55293379 | -9.5731 | -47.9529 | 2026-09-23 11:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 6a880050-bd0b-3a46-ac6e-5f3b2b13095c | -7.9904 | -44.9608 | 2026-09-23 11:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 9fc2ee0c-8629-314f-8316-f26183cf058d | -11.3596 | -44.1989 | 2026-09-23 11:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 58f6dac5-905e-37c9-8e91-b047187df769 | -11.5499 | -45.3526 | 2026-09-23 11:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 50603c91-e38b-3d52-ab4e-ec7eca110e87 | -6.6129 | -43.7317 | 2026-09-23 11:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 304.7 |
| fecda04b-9332-3d95-bc3d-a2b160485460 | -8.378 | -45.6036 | 2026-09-23 11:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| a2f48898-db43-368f-80e3-33d6945d9150 | -7.0349 | -44.6625 | 2026-09-23 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 3f488757-55c0-3a6d-bbe2-36b6c8675c16 | -6.6317 | -43.73 | 2026-09-23 11:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 2ab056e1-cb37-3591-b55c-f091b2277441 | -8.7912 | -44.301 | 2026-09-23 11:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 3b43e637-f51e-310e-afde-2ab37097af96 | -8.7916 | -44.2778 | 2026-09-23 11:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 264.5 |
| 50061604-1ae7-32b9-8d47-aeba4ca326da | -9.5731 | -47.9529 | 2026-09-23 11:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 156.2 |
| f3c3b688-cf9e-3277-92cc-889843e59be4 | -8.0923 | -44.3307 | 2026-09-23 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| cf002364-5e22-3483-8ffd-95a709bcb426 | -11.5307 | -45.3553 | 2026-09-23 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 308.6 |
| 0955165e-f14a-36a0-9f03-65e39cd544d0 | -8.9205 | -45.931 | 2026-09-23 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 1ee3ce76-5b00-3f87-8ecc-9d9297412eb9 | -8.8105 | -44.2757 | 2026-09-23 11:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 437.4 |
| c58de2fd-a812-3deb-a715-b807331e6579 | -7.0352 | -44.6396 | 2026-09-23 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| c2449e2d-82f9-36b5-a990-22dbccf30d90 | -11.5499 | -45.3526 | 2026-09-23 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 336.1 |
| 88160f6b-b38f-344e-8c16-c5cb1bed4986 | -9.9247 | -48.4847 | 2026-09-23 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 520c22bd-5036-3c09-bb55-dca3d973cf83 | -8.378 | -45.6036 | 2026-09-23 11:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 23d451aa-d8a8-3536-b137-ca5d3a1d148e | -9.9439 | -48.4608 | 2026-09-23 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 5bf70137-60e4-300f-8763-e38fefae40a6 | -6.6129 | -43.7317 | 2026-09-23 11:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 320.9 |
| 838eae8d-90c2-3dd9-8737-a37a6290e710 | -9.925 | -48.4628 | 2026-09-23 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 0bc716ab-2109-34d0-ae4c-ef07b66eb04a | -9.5728 | -47.9749 | 2026-09-23 11:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| db82992a-f26b-3228-8b06-3409710ea318 | -8.378 | -45.6036 | 2026-09-23 11:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 302.0 |
| 49b5b19b-bdfe-30cb-952f-c3cd2918d49a | -11.3596 | -44.1989 | 2026-09-23 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| df8c02f6-9a39-34d1-b43f-6839c9bf3efc | -9.5728 | -47.9749 | 2026-09-23 11:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 93a69b4d-3bbf-392d-a2c4-66ac5bec5fbd | -9.9439 | -48.4608 | 2026-09-23 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| e64c7e50-cc18-3f87-ac2a-57b046bdde13 | -8.3591 | -45.6056 | 2026-09-23 11:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 3ca2b167-5102-3d03-8b6f-0eb136df91b2 | -7.0352 | -44.6396 | 2026-09-23 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| d2e692e5-7804-3960-90c0-be97448f19e2 | -6.6317 | -43.73 | 2026-09-23 11:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 5566935f-c08e-3787-95d0-46460402b825 | -7.0349 | -44.6625 | 2026-09-23 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 9cecd2f2-3af8-3500-951e-4356e83c0c8e | -9.925 | -48.4628 | 2026-09-23 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 21326d6c-9b38-30b9-94af-2c80e5e40ac1 | -9.9436 | -48.4827 | 2026-09-23 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e5bcf8d6-e2e4-3167-a82f-67fc3a1c0ab9 | -8.7916 | -44.2778 | 2026-09-23 11:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| c00a41e3-1ef2-3ab4-b7f6-665d97464cb1 | -6.6129 | -43.7317 | 2026-09-23 11:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 341.4 |
| 1e0782e0-34d7-3200-a5e5-10b7e71f6eb0 | -11.1189 | -51.0454 | 2026-09-23 11:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 31ecc73f-0693-3bc6-97e9-9aba7d616066 | -11.5499 | -45.3526 | 2026-09-23 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 370.4 |
| 1517f97f-6430-32d1-9b2d-4d76b044e3c1 | -11.5307 | -45.3553 | 2026-09-23 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 265.4 |
| 6eee0eb5-99e7-3272-847c-0cc8c75e4daa | -9.5731 | -47.9529 | 2026-09-23 11:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 54a8002a-4692-30a0-b8a5-18ca0cd73458 | -8.8105 | -44.2757 | 2026-09-23 11:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 239.2 |
| c288c290-e524-332d-ab1b-cb0054972978 | -6.6331 | -59.9265 | 2026-09-23 11:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 3a70e91e-990f-3bd7-ad3e-8c65a5a7976f | -8.3783 | -45.581 | 2026-09-23 11:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 209.1 |
| 2882d3f5-a070-3fde-8588-a04c7d259708 | -8.9205 | -45.931 | 2026-09-23 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5a802657-5241-3d38-b028-d410d16e8149 | -9.9247 | -48.4847 | 2026-09-23 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| d844abd5-dfc4-3280-897a-80061a8af1a6 | -11.1189 | -51.0454 | 2026-09-23 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 94606bbd-3690-3146-aada-b06f962f6f68 | -8.9205 | -45.931 | 2026-09-23 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 559e66b9-0f0f-354a-a9af-18777a8883dc | -8.8102 | -44.2988 | 2026-09-23 12:00:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 4310d815-d3cb-3406-a463-d72c9228739b | -8.9202 | -45.9536 | 2026-09-23 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| bc27032b-7b63-3f9f-a339-9484cd1eb744 | -6.6331 | -59.9265 | 2026-09-23 12:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 4d65ff51-96eb-3376-aadc-af01d0e39337 | -9.5735 | -46.5337 | 2026-09-23 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e1d7b397-e989-3bc6-ac92-952536150381 | -8.378 | -45.6036 | 2026-09-23 12:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 492.4 |
| 167c29d6-c24e-30d8-8689-8d395aa1a956 | -6.6129 | -43.7317 | 2026-09-23 12:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 299.6 |
| e4bf1577-2ac8-33ac-addc-b39801dee49e | -8.3783 | -45.581 | 2026-09-23 12:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 394.4 |
| e3d64454-1725-30db-9c27-f67d08edef1e | -8.9013 | -45.9556 | 2026-09-23 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 6e202c94-82f6-3c80-a7a1-066ce815c3d2 | -8.7916 | -44.2778 | 2026-09-23 12:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 317ca14e-b31a-3dd1-96cb-892f60569ff0 | -8.8105 | -44.2757 | 2026-09-23 12:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 95c99b4b-9f42-351b-aac5-4ebfc05bb23d | -6.6146 | -59.9272 | 2026-09-23 12:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 844c5325-e530-3f9d-a10d-4c5f0aa33387 | -11.1 | -51.0475 | 2026-09-23 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 91b383a2-7150-3224-a787-a0772e49e6a4 | -8.3591 | -45.6056 | 2026-09-23 12:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 67488935-0e7c-378e-a317-7a7a43fb8777 | -9.925 | -48.4628 | 2026-09-23 12:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 7e7080a7-9b78-3a5e-a45a-dc8abb083c46 | -7.0352 | -44.6396 | 2026-09-23 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 7017d3ea-758f-3e40-8e5f-7c4fb843c2bf | -10.5561 | -46.7095 | 2026-09-23 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| b2739947-d3f4-3f2c-bcf5-e5c9e61a77f2 | -11.5307 | -45.3553 | 2026-09-23 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 75dfd2cd-b2c1-3076-8d13-e6690398497d | -8.0923 | -44.3307 | 2026-09-23 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 9aa3f8ab-8d67-3eaf-a4ac-016b773f6e32 | -8.9016 | -45.933 | 2026-09-23 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 0a30fea4-6bea-3fc3-95ed-f5f9f09625a3 | -9.7 | -46.65 | 2026-09-23 12:00:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 356c7a40-73df-354a-bc82-faba037d546a | -9.7 | -46.7 | 2026-09-23 12:00:00 | MSG-03 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff575162-3632-3ddc-a331-4462625d57ec | -17.46 | -40.18 | 2026-09-23 12:00:00 | MSG-03 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 148b7920-668b-30ae-991f-59409cbb1184 | -8.8 | -44.28 | 2026-09-23 12:00:00 | MSG-03 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c7267499-1fc9-30cc-8c9f-3b1cf259d5f6 | -9.73 | -46.71 | 2026-09-23 12:00:00 | MSG-03 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a44bd69-9145-3edd-9946-95a41f2c280e | -8.3783 | -45.581 | 2026-09-23 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 169.4 |


[Clique aqui para ver as próximas entradas](README131.md)
