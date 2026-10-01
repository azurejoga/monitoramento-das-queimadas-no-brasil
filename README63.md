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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a45a225-cb14-3c64-93cb-f5a8dd49d03c | -12.38809 | -54.1006 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb155331-f7e0-3474-a6fe-7058a56ba9b7 | -12.77609 | -54.00629 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a05bb08-bd17-3034-ae67-3d84c81dd348 | -11.34271 | -50.96837 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 801a51bd-31b0-30fb-b66e-38023bcf8f64 | -8.32282 | -46.75738 | 2026-10-01 04:34:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5e740c6-42e9-3c86-934a-f53e60eec214 | -12.86411 | -44.33627 | 2026-10-01 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ef4b5d8-65f8-373a-a721-7bb2a67d1140 | -6.76564 | -48.67868 | 2026-10-01 04:34:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62dc5a7c-37d7-3f91-9bf1-8ad37d28e158 | -10.84513 | -48.70279 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11eb3161-6694-3749-939a-ec5ea0c6f8d0 | -10.24919 | -44.58245 | 2026-10-01 04:34:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b29f9330-a2c5-30db-bb76-ddb02f34c451 | -8.13636 | -43.43654 | 2026-10-01 04:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7e372d5-b228-3e54-b434-33538d5701af | -9.75848 | -44.81572 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24bc475c-f31e-342e-a856-610ce4d6baca | -8.49626 | -44.75593 | 2026-10-01 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b09d3719-a778-362b-8833-986088ee18b1 | -10.56434 | -50.05373 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 373ea585-98d0-3877-8dc7-c7c402fe3b10 | -11.7947 | -50.41792 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d32e1253-35b6-3d9d-b3ce-92e9420c927a | -8.035 | -45.47597 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78b59a78-64b5-306c-9400-8b19275a5f26 | -10.91244 | -43.84747 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9983e7d5-982e-3959-b2a3-dea226f63af3 | -12.35369 | -46.38115 | 2026-10-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ccb3f7d4-7c31-31b1-a881-960ae9dd4043 | -9.21191 | -45.82374 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea75e580-6ca6-3e5d-bfba-206b00a26d68 | -12.32733 | -46.3954 | 2026-10-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d51740f5-60be-3c09-ad79-357676a9c428 | -8.61042 | -49.46424 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8adda94-e11b-3b53-9d9a-ef204db4fd69 | -7.48998 | -55.00301 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f116cbcb-3f22-37b0-9f65-5b00263c5d93 | -12.18375 | -47.38468 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42eaea5a-0ed4-3e99-af91-b464f329d2ac | -6.75022 | -55.08725 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 253a29ff-2e6a-39ca-9dc2-13cba1f030c8 | -11.71605 | -43.44416 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 792a2d3c-f671-31f6-acc2-aa0af88e42b5 | -8.01607 | -42.88277 | 2026-10-01 04:34:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 68d6c404-94b6-3385-a64a-acb5d1ceee0c | -11.45993 | -43.45021 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 787833d6-0137-3fc3-a1ef-4932545c7754 | -13.53652 | -49.19063 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d919bb0c-0ddf-38dc-9b2d-9cba82e680a3 | -7.71784 | -54.79534 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2372484f-a057-3b04-8c5b-4deec53fe206 | -11.19514 | -44.85292 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9987c2f6-2adb-3760-8b2f-489ee08c8948 | -10.60432 | -53.97552 | 2026-10-01 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10c73543-0251-3d13-9311-c48225b2cb80 | -11.65494 | -47.59406 | 2026-10-01 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2a3856b-e158-3f39-b466-289211644044 | -10.81225 | -48.75653 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d9667dc-84cf-3151-814a-021f32543a6c | -11.44917 | -43.4438 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0be4ba64-eb09-35ef-9a2f-12f579b318f1 | -7.61869 | -44.54889 | 2026-10-01 04:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cd94bd8-9ac7-3d19-ab16-e695dd522516 | -10.52296 | -57.78421 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77548ed1-59de-3288-bab2-49775a8ad2ff | -10.65693 | -50.76307 | 2026-10-01 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25ec764a-0eee-35e2-ba1d-9dc150a0cd49 | -8.62007 | -45.3691 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d2723ac-248a-3c50-a48d-9ee5ca5d1795 | -8.24842 | -47.98949 | 2026-10-01 04:34:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32a3aa33-7b9e-3bfb-8642-57cab567a384 | -7.48553 | -54.99897 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e140164-afc9-3e12-8808-59e9da071980 | -9.0874 | -49.8867 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ebd7a26-5f47-3936-9f92-391cd0347d90 | -11.12545 | -44.58953 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f067ecd-a1a5-3084-b1d8-21fec5fff265 | -9.0818 | -45.00599 | 2026-10-01 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b34a715-46f5-31c8-bee3-c8ecb33ffc68 | -12.08991 | -50.69271 | 2026-10-01 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 917f7f52-273f-3a1f-95ef-10523cd7c0ac | -8.96563 | -44.18259 | 2026-10-01 04:34:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8318c8c0-07f8-39e3-83b9-79c6d82022e7 | -9.88114 | -44.96815 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e01de3fd-178c-3928-aec9-af6a3a0d6ef1 | -7.55695 | -55.03149 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc60e51-c80d-310c-93f9-b1a27b0afda1 | -11.69936 | -43.45148 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36f31df2-8481-3b7e-9db6-428ed65c6c5a | -7.19124 | -46.54449 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5f5cbb5-c0b9-39fe-b6da-ed1cf4c5b6b6 | -8.13608 | -43.48935 | 2026-10-01 04:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce2ac6ad-ec23-3754-b10c-bf2ac9e72f9f | -11.32742 | -50.97011 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9980b871-df9a-3d8d-b2fc-9372fd6adf89 | -11.46305 | -43.45551 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3cba0884-a943-326a-9caa-e886e081195e | -8.30418 | -54.71262 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad9e757b-3ff0-314e-980a-38b4e9613354 | -7.5696 | -46.62245 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73df564c-d29b-31ae-a961-23ff72ed6627 | -11.25647 | -54.07346 | 2026-10-01 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54e31aee-cb61-38f0-b7d2-e075644a6ec4 | -8.20498 | -45.49148 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a1b3883-b292-3794-8225-dc368d7f1f46 | -8.01243 | -47.4488 | 2026-10-01 04:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57db66d9-c276-34dd-ad3c-95d375959edb | -8.12679 | -43.52716 | 2026-10-01 04:34:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d3e55682-c373-366e-8604-f7a91aee59e3 | -7.71996 | -49.54348 | 2026-10-01 04:34:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29822b68-6483-3de8-ae73-865a8f01cc1d | -5.86773 | -57.7572 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 574ebc08-9161-37a1-a647-7e9e40592697 | -9.38751 | -56.97552 | 2026-10-01 04:34:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 608258bd-9921-3629-a7ca-8343dedf4e92 | -14.14242 | -46.24106 | 2026-10-01 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59856c4f-6312-30fd-a372-dc3d9bd6d2b5 | -12.77237 | -54.02683 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79dafbf1-d3b3-3cdb-92ef-2acf44241813 | -9.76545 | -44.8168 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f7a2334-bd84-38a2-a0eb-1ae2c53a41b4 | -11.37619 | -55.12999 | 2026-10-01 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96376d9b-9321-3e07-8ef3-835795816b81 | -11.96526 | -57.5944 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf0beb23-fe90-389a-93de-af53a2f7d6d6 | -10.74716 | -50.54237 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a2948ee-0396-3d8d-a234-e2a8477a7df9 | -7.49202 | -54.99152 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fae35b3f-640e-380e-ae99-ba4303b03ca6 | -12.70761 | -54.06585 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c94cb365-c7b5-3963-8577-cbd314d8211b | -8.98281 | -44.18925 | 2026-10-01 04:34:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c1a9e5d-6499-385a-bf4f-a1fdd4ddb8b3 | -9.28322 | -46.45955 | 2026-10-01 04:34:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e108cc6-7ffc-32de-bc39-46e92d399ff7 | -9.14336 | -49.96696 | 2026-10-01 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe8eb182-140a-3787-a378-f50cde499aa8 | -13.6685 | -44.31033 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc7a33ea-c27f-36da-b47d-7b67496f8599 | -10.2386 | -44.60526 | 2026-10-01 04:34:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96d51880-d7da-3da2-9576-549032ff829e | -7.71993 | -54.7555 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c398a4b-cf60-3981-a294-bb8b1c0fb202 | -9.58409 | -54.63419 | 2026-10-01 04:34:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 42fdafb0-e81f-36af-b0cd-29a805412224 | -8.33304 | -44.15941 | 2026-10-01 04:34:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fe144540-8e5c-3996-9d55-35ad2c0e9b46 | -9.83061 | -49.30441 | 2026-10-01 04:34:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff5b5413-6a48-3420-b35f-8fd8cff9edbe | -11.3456 | -43.35769 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8ebc49fe-7a00-33c1-b9e0-7de1c149e6bf | -11.45543 | -43.4544 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae6d236a-7d7b-3381-a5ec-ca49da1cd35c | -13.4261 | -43.81155 | 2026-10-01 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f746c15a-da91-3426-973c-0f8f1d90e8a0 | -11.38838 | -43.40564 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73602d32-bf7d-3e33-a39b-b8b0f66ba692 | -13.51585 | -48.02488 | 2026-10-01 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76bad14b-571d-3ee8-96a3-02d7d526bab2 | -8.77155 | -47.84178 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75160e2a-185d-3f75-9e54-e6af5ad34b4c | -10.70209 | -45.3012 | 2026-10-01 04:34:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae2d1ef0-7afa-35ec-9de7-d8202366cc6b | -7.85154 | -45.82351 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 295a92c4-703e-3751-9097-430e618bff86 | -7.6112 | -44.55163 | 2026-10-01 04:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94641d74-2665-3b53-b80e-37a4f9129609 | -7.37936 | -46.42917 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ccd11ee-d742-368c-b93d-b1d43e2d17a3 | -10.83727 | -48.70877 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf20becb-f640-3b62-ae99-c14eed2068f8 | -8.49569 | -44.75973 | 2026-10-01 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d129b23-014c-379e-864f-3794317bb8f4 | -13.8826 | -44.45875 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b29f2b39-de9e-32d9-8713-6e23e76a46da | -10.27681 | -44.63992 | 2026-10-01 04:34:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ab81eabb-4185-38de-929d-8133815eb83d | -12.18651 | -47.38874 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83c319f2-b5ba-308d-b88a-e18c866f6c97 | -8.78815 | -46.71394 | 2026-10-01 04:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 527ece6a-b79e-3fbe-b88c-99c9101a493e | -10.24795 | -59.02997 | 2026-10-01 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba188a76-0bdb-391c-ba72-133ad43ef139 | -6.3423 | -55.32311 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 124bef9a-657e-310a-a48e-f9a860643b1b | -7.5034 | -45.83394 | 2026-10-01 04:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e5da05e2-039e-3288-8f83-d490bf10abd0 | -9.1996 | -45.81429 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47e7acf9-6eca-3106-9fe2-4ebb215b3ea5 | -7.34227 | -55.58919 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da42047d-0055-3aae-a1e0-38ef3a7ebb27 | -11.41639 | -43.48258 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d38ae624-e982-31c1-9240-f08821391900 | -10.78293 | -50.52717 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 03b8d881-b14a-335b-bd17-afc4a720dae7 | -11.182 | -45.11065 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README64.md)
