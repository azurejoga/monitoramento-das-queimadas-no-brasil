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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a137b191-3eda-3b1d-bfc2-d67af2299afc | -5.74382 | -40.76858 | 2025-10-12 04:14:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54096bc4-c4ae-33b4-aecf-a2b34be274bb | -4.30937 | -48.10795 | 2025-10-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53913066-58dc-3b24-a126-ef75c0403cc7 | -5.31157 | -42.87167 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 48ff1542-a883-3129-b343-1d485002e2d0 | -8.70465 | -47.05972 | 2025-10-12 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 362fd4d5-5110-31d8-8d41-e2bf4615698d | -7.44341 | -47.8598 | 2025-10-12 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6f14d84-0bf5-3527-a1ed-a6110ac36c31 | -5.74038 | -40.76805 | 2025-10-12 04:14:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 278505b8-578b-3a73-a483-34ff89e198fc | -7.15633 | -42.19168 | 2025-10-12 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e9a74f8e-4bdb-3430-b6a5-739ba9b9a907 | -7.51425 | -44.63999 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6776bd66-5418-3e90-a716-014e0e191a0e | -7.50046 | -42.75787 | 2025-10-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 507d5a57-e71a-324b-bb15-61fd41b0ca6c | -6.2717 | -42.97789 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7afcb9a5-5a2f-338e-90e3-810d6c4085e4 | -7.26068 | -39.00305 | 2025-10-12 04:14:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 03d1cd0d-d97d-3fc9-9c17-154994fe775f | -7.2651 | -44.1509 | 2025-10-12 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b569606-163d-33da-b67f-2d58bb35db0f | -6.71053 | -42.89243 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f5bae135-3334-38ea-ba4a-f046930fc199 | -7.7422 | -42.40533 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0330f7f3-1237-32d0-9209-7f1da0768378 | -7.40266 | -42.97343 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a839c0e1-7a84-3599-942d-2f8f273c8c90 | -5.74617 | -41.32415 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb9e3457-1b0e-3286-9554-14abe4481137 | -7.99283 | -39.69316 | 2025-10-12 04:14:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 499b88b6-5e2e-3be1-a50b-d931c35589f5 | -5.33903 | -43.43395 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8be66c50-bdf4-3211-aec7-60f35db99f16 | -7.49607 | -42.7643 | 2025-10-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f995f95d-e9f9-3f83-afdd-6d1956811016 | -8.7066 | -46.83846 | 2025-10-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d69794a7-2bcb-3a24-b1b4-368d92f47402 | -7.79581 | -42.4316 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f4934d43-4028-3f28-a301-44e93c8db6e4 | -7.50933 | -44.60624 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e234eb0-5427-3092-813c-3dd1ccf2cdbc | -6.25039 | -41.56002 | 2025-10-12 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9aa0b6a4-efe2-3dae-9149-9188957aa7e9 | -8.95339 | -48.66697 | 2025-10-12 04:14:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16e9e9ad-cf82-39ed-a943-4236beb88327 | -5.36476 | -46.29089 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d7d869ec-7771-3567-a877-363055f429ac | -9.40078 | -45.76282 | 2025-10-12 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a0f3380-676c-3c3b-97ad-a73eb7468edc | -5.32544 | -42.87453 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 26868b04-20d5-337c-96c8-d16818aee424 | -6.164 | -44.67194 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f83901b-1f7b-369e-95d6-6e89ef42cfdd | -7.85345 | -44.5194 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1ea5770-a25b-33f4-bde4-6a4c5f46935e | -6.83297 | -42.78416 | 2025-10-12 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f7d49c7f-e417-3556-bd69-124e4d31c32a | -4.67973 | -43.25507 | 2025-10-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a535b19b-6809-3e0b-a932-33c973118490 | -7.80795 | -42.41908 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e42fc4a-bc27-3ea0-96c9-234f005b639b | -7.35308 | -43.85418 | 2025-10-12 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb6a0e4e-e2d5-3abf-b2bf-c25759d01f28 | -5.34233 | -43.43446 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00735884-e131-3322-a846-89788482429c | -6.76602 | -42.82335 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 270f9638-517b-3265-b0d2-3fb2c8153987 | -7.3327 | -44.04689 | 2025-10-12 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41d68da8-f913-3985-bb0d-d8f9d07c8d1d | -7.87093 | -44.8768 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b93320a-e1cf-328d-a650-6db8b739fa51 | -5.64635 | -42.77671 | 2025-10-12 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ffb6d05a-add7-3f09-8849-34e9808859b2 | -5.97223 | -44.37944 | 2025-10-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 793e35af-ef08-369b-a61d-8ade34be1b1c | -7.80525 | -42.43668 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5a1a178b-21fe-381f-9ed9-ae34814f31e6 | -4.94352 | -44.76598 | 2025-10-12 04:14:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 613f8b99-e142-3ec9-9a94-73bedc8fa40d | -5.60771 | -42.56984 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 341bcc58-ec5e-33d6-bfdb-d7cd6586db68 | -6.16582 | -41.73041 | 2025-10-12 04:14:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa8d0a76-3d27-3b23-80e5-56c9a82c75b4 | -7.81128 | -42.41959 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7d4098e9-af34-3019-bcda-7d13d5b37209 | -7.24564 | -43.49698 | 2025-10-12 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f84e5b3d-2210-3e1e-a243-0fb35176e0fa | -5.60388 | -42.57277 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff0184e0-af82-3c2f-8a01-bc02463fa5ce | -5.82499 | -46.16213 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf1967c6-7f9c-3b53-9781-1315d2763a6e | -8.25555 | -43.80723 | 2025-10-12 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2af5fac5-8af6-3dce-b466-0506e95a360b | -5.2656 | -43.10044 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3329a965-c56e-3fc3-9e26-a2350e90273f | -5.47497 | -43.39514 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 329808b3-81b2-37cd-9d97-9868c7860bb8 | -7.50756 | -44.63885 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdec2719-5432-3a32-955d-638d11e84a92 | -7.13734 | -43.25653 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a77b4ca1-1543-381a-abdf-e79472d053d0 | -7.51993 | -44.60427 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbfa352d-452e-3260-bccb-0d56bbd5e025 | -6.6312 | -39.94362 | 2025-10-12 04:14:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 92e6b3e3-ef04-397f-9c03-612f920ed68c | -7.51367 | -44.64363 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae5eb945-9514-3241-b42d-7e94be64a0e3 | -5.75255 | -44.28949 | 2025-10-12 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d457206f-d44f-3788-a7f5-2bca7bc96296 | -5.43337 | -41.36918 | 2025-10-12 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ef05c3da-3cec-33d7-b1b5-ee900b1a5ff1 | -6.84374 | -47.34545 | 2025-10-12 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e41f884-8598-3ea4-8390-54e8755d9104 | -7.26831 | -42.95883 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f7681d54-d373-3d2e-8535-b0928196c1ba | -6.24156 | -42.99788 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 944cd3d8-c063-3fb8-aaaa-44873900b1f6 | -4.61746 | -45.77725 | 2025-10-12 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34077405-a6d7-3915-b7d2-0d564120c3f6 | -5.58662 | -42.98574 | 2025-10-12 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0d8cc544-48ea-33f0-8755-f2ded6802af0 | -8.82662 | -46.05388 | 2025-10-12 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4de17768-e8ad-3cf3-acf8-260c0b31782d | -4.81988 | -43.14277 | 2025-10-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2258c200-02c7-39b0-82a4-4bf471f3cb59 | -5.59469 | -45.83765 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa3ac79f-b1dc-31ae-b87a-4c0fffd4e7f1 | -5.25547 | -43.20812 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb01e6c0-3e02-3ed2-8710-9b7c8a4536e4 | -7.49222 | -42.76727 | 2025-10-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 561796ea-300b-3d7c-b182-886ac4b8199b | -7.43067 | -42.96719 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 65f82cdd-cdab-3b1c-a7e8-9cfb2c9e55b9 | -4.54223 | -49.68873 | 2025-10-12 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f13c978d-f2f4-30e4-9ac0-cb31fad4cef5 | -5.82001 | -44.03224 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78148ae5-80f3-3413-aa76-b891551d7cc0 | -7.80741 | -42.4226 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2339332b-4b5b-35e7-9e4c-6695e6d00634 | -7.33326 | -44.0434 | 2025-10-12 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98eb0331-656a-399f-abc0-036b00c73cec | -7.73377 | -46.65862 | 2025-10-12 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b3d5964-8852-315f-887c-7e0f2884daed | -8.21434 | -43.33269 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 802298a9-7139-31fb-9dbc-7171c105891a | -6.61301 | -42.49371 | 2025-10-12 04:14:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13bc5d96-79f6-3217-97a9-46f35f0e6a78 | -5.73549 | -51.10954 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba21bc6c-0f46-33d0-9b9f-d214c2951aa8 | -6.04202 | -42.46872 | 2025-10-12 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 303e3089-d5df-34d7-8d55-2467e7605462 | -11.67612 | -43.77721 | 2025-10-12 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 662518b0-23d2-3534-9643-baa5f68fa2dd | -10.06825 | -45.04155 | 2025-10-12 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6f182f8-77d7-3524-9baa-7cb5e36b8819 | -7.88788 | -44.51768 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6a2b595-32fd-3ad8-a3d3-8f57544376e6 | -7.36322 | -44.7963 | 2025-10-12 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 143bd6a9-5522-3cf9-a96c-42b0094062ac | -6.80605 | -47.05323 | 2025-10-12 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bfacde7-ecdf-367c-bae0-6dfd30237e05 | -5.34682 | -43.43156 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e2f071b-ef17-3c8f-9aaf-9fce14b4b0a6 | -6.29671 | -43.77456 | 2025-10-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bca746b-179a-3149-b8ed-d181220c71a0 | -6.17286 | -42.54561 | 2025-10-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ab311fdb-59b8-356a-ac41-f6f219d9493f | -6.16956 | -42.54509 | 2025-10-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1acaa517-1f5f-3f84-a9ca-d49f83b926fa | -6.36689 | -39.10443 | 2025-10-12 04:14:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 179cb113-d507-3d11-bee1-8cbd23a678ba | -7.74481 | -44.21721 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07bb263b-2c16-3186-a37b-7c9356f7da90 | -6.22274 | -42.48605 | 2025-10-12 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 071d31d1-aeae-3ff0-8f35-ea7a5e525c31 | -6.45447 | -41.80368 | 2025-10-12 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2c74c80f-9de7-3c75-9c7f-23e04e56b357 | -5.91526 | -44.92934 | 2025-10-12 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 025ca97c-1689-387d-a710-7f73ae5f1d9f | -7.83993 | -44.79861 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c1be3b3-1ff5-300e-a4d5-177b929e2067 | -4.57571 | -45.69486 | 2025-10-12 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdb45312-9fec-3d07-ac9b-46ba1d17a568 | -10.17868 | -44.53834 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad7f2efa-f67b-3e32-841c-6879b9289568 | -8.29571 | -40.83822 | 2025-10-12 04:14:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a12bf545-b9ba-346d-be05-36d1b970598c | -8.21159 | -43.32872 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ac04ee73-41ce-3c29-a375-0ef4e24796b8 | -5.86238 | -42.26628 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f5c8b9d-76bb-3e95-8f5e-c77851e65cd8 | -5.93706 | -43.93882 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 346cbc84-f7d6-3425-838f-8b5eb7157f43 | -5.59772 | -41.10082 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ec95f73-14dd-39a3-9e36-391805486b28 | -4.82809 | -43.50249 | 2025-10-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
