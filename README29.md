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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 725c791a-6058-3b38-b38a-810f2d4a9a21 | -6.27445 | -53.38144 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 03732256-0fad-3ea2-a638-321e3be9fff1 | -6.14971 | -57.94183 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73334b82-d9b9-3334-8e2d-ba72c33eaa44 | -7.37973 | -55.18735 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e3f4bec-cd78-37a3-9e18-d1f9e139972d | -3.53575 | -48.1882 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| acaade05-618c-35f7-936b-2d232e3a4d0d | -6.0987 | -49.48026 | 2026-08-26 04:51:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e368038-35ac-3ed8-a145-ce0fc0040c5f | -8.08063 | -47.50817 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1543bcee-fba2-39bc-a849-3ae935e7f3e9 | -6.27168 | -53.37743 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cb660ba-3ab4-37af-a2b4-cacb758ace73 | -6.28384 | -53.36506 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7864f579-16d1-37b3-b314-930358ba312b | -7.4496 | -43.1064 | 2026-08-26 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| acf8bca0-f198-3fe6-9ef9-cf3fdcd2e597 | -6.69496 | -58.71378 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 408f2f77-a347-3272-ab02-14d7a036b110 | -6.25841 | -53.37536 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 06cbd1ec-9453-3657-bee3-14f6519e869a | -6.68668 | -58.71714 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67359933-5e61-3011-b902-e33fe5e55b9e | -6.86225 | -56.57231 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d6929f1-8374-35e8-9f9e-650d657ead23 | -6.41138 | -60.0596 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b760763-6393-3091-b641-403b4aed8598 | -2.79208 | -50.51908 | 2026-08-26 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ffc9512-97e6-376d-abaf-225afaee0ecf | -4.80483 | -43.17299 | 2026-08-26 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 312f76f5-3ace-34cd-b74f-fa61c7224c11 | -7.46598 | -45.38203 | 2026-08-26 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 616f5c2d-0719-36e7-997b-c2348d234009 | -6.18891 | -53.49318 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2931fc5c-1381-3c17-9fd0-38560f29e4c8 | -7.44911 | -43.11018 | 2026-08-26 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ed672368-15d3-3cda-9bae-20aacdfd0a3f | -8.14933 | -54.98982 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f8df723-d58a-3df3-924e-025b02cc7bea | -6.33223 | -54.73764 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ada5058-d110-3b4e-bf92-5151b986b6ac | -7.51323 | -61.38037 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f511a6bc-83e5-31e8-905e-6b56a7bc5cd2 | -8.75864 | -44.25121 | 2026-08-26 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3d3cbf4-acdc-322e-830b-9ba6506ad49e | -6.26227 | -53.37239 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9da03d30-69cf-3143-927b-15fbb5677d29 | -7.76143 | -44.74797 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3f4fb54-8bc6-3778-a251-00f31161c0c8 | -3.09764 | -61.19808 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31b2327c-72d2-362e-af4a-3e28047d2614 | -7.54287 | -61.35514 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b50d64f4-c148-3b98-835e-ad61fe9a77e2 | -6.50873 | -55.22955 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4de8905-9815-3b8f-bed8-7bf439799a04 | -8.13758 | -47.50734 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9f0fb6b7-b258-35ec-957f-3c8e5d9f8473 | -9.44599 | -51.67101 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3407292-da94-3ada-8813-54a73cb486f6 | -8.53524 | -55.34333 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9d8aa72-37a5-3f51-9575-2cacf342ef6e | -9.03295 | -50.79036 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 585c556a-8ca0-36e4-bde7-36ec78100213 | -7.37628 | -55.18676 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe9142cc-844e-3617-b311-f48ca9d37984 | -6.71611 | -56.34455 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2798fd4c-19a4-33cc-a1f4-2a2473d527f6 | -6.81153 | -58.61753 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f8741ee-ce85-31f3-98c8-aa09e925cb37 | -9.04108 | -50.79031 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a9555ea9-2d15-31f1-8e4d-a547f2fc2729 | -8.55201 | -55.3229 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8624ea4-8434-3677-b4e0-da4e4b213b1a | -6.8122 | -58.61361 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bab58ace-1672-3870-95c5-dc2d3d2720ed | -9.44136 | -51.58693 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6eb76c6-9eb2-36dc-bc1e-8c93c563d870 | -6.27111 | -53.3595 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66fa5bbd-6da6-3827-a74f-316784fdf258 | -8.6186 | -54.73366 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35d56ef1-aa4a-370a-9cfe-11dcdbba0175 | -7.02806 | -59.2219 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 022046cd-fcec-3752-ba1d-198afcbe51e1 | -6.1193 | -57.82217 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 910efe00-ac45-3558-b008-a4ca53d12fdc | -5.49289 | -49.09946 | 2026-08-26 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4910127b-e06d-3505-a87e-0692a190ebf3 | -8.71169 | -49.60804 | 2026-08-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d7a6763-0cef-3298-b653-133e5dc55fd4 | -6.25177 | -53.37432 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 031ad941-d25f-35b6-841f-95e0d46db0c8 | -7.27267 | -45.3663 | 2026-08-26 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84831591-510f-3a83-9392-a81de17f3150 | -6.62242 | -58.50347 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e3b8569-88cb-3642-a4b8-1af0e838dc3b | -6.50937 | -55.22565 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dba0e1d3-c5c7-3e16-a47f-9b2ba1a7ea6b | -6.27059 | -53.3844 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 830b33e8-bd7d-30b4-985b-45104b358336 | -6.93388 | -58.9491 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30613329-6674-38a2-bb53-8e17d4030c9d | -8.56806 | -54.81132 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e4d22c3-a999-331e-be57-73f4ab6006b7 | -6.6907 | -58.71308 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7aaaefba-8dee-32f7-abc1-b3dc0ea768de | -6.31288 | -53.57002 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9b043c8-a96a-3534-863f-4bf789232fc1 | -5.9235 | -43.63953 | 2026-08-26 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 046954f0-530e-3693-b60c-22229450b0ee | -8.60732 | -54.73929 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11fd08dd-a54a-39d0-aa99-6fb2b8a2a742 | -6.27498 | -53.35653 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f746f5c-e410-3f12-8e6b-1fffcdf845dd | -7.49193 | -55.36329 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7daec1ed-4f4e-30aa-8a40-a6b9dc14972b | -8.17557 | -54.95972 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3afa7956-fbb3-3299-979d-d7af174bd0cc | -6.62663 | -58.50414 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 86a27835-689e-3d35-a2a6-13c39049378f | -6.26891 | -53.37344 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0adf7797-ae53-36b2-872f-a7408b0160bc | -8.17176 | -54.95872 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 15a21e4d-578f-3ea6-b753-1608a5718fa2 | -6.65384 | -58.49662 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7bed0502-0dad-3a38-ac41-e9c584bf868e | -6.64281 | -58.51072 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7d60d5fe-2972-3411-9c8d-60cf043d3580 | -6.44472 | -54.97505 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54159bcd-b877-3d0a-9cea-99e9fe8a0856 | -7.95836 | -52.43964 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf4aecd3-67ed-3154-9fe3-c78a32448768 | -7.76455 | -44.76292 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05c0c3ac-26bc-3f30-ad92-63b908268972 | -3.20302 | -61.1465 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d370d4b-234e-3f87-9ffc-978b4a7ef284 | -9.41536 | -51.64349 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bdf0b41-8fbd-312a-b3b1-80fbb91e5cfe | -5.4927 | -49.10069 | 2026-08-26 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2207ec2-d717-3017-bce7-a8d48bc08551 | -8.00749 | -51.81384 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7e7cd59-1e66-38a4-b1ac-90abcbf2b035 | -7.02551 | -59.23773 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a129958c-317c-3148-80b4-3ed1ca299623 | -6.00387 | -44.74696 | 2026-08-26 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a44f699-7344-3678-8a25-39855847721d | -6.25342 | -53.36388 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a7de0ff-5ce0-31b9-a80c-67d1d18ff4e1 | -6.55787 | -56.55521 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3dc4e0f-790f-334a-b937-bf2bd085a0e2 | -8.12933 | -47.47449 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d3e1597-ea57-35df-9c94-5dc4988074ba | -8.01458 | -51.82647 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2fb5e0a-af74-3657-8280-759c262169f9 | -8.55581 | -55.28081 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06d7ce7a-0eec-3a90-83d9-eb89950e3aa4 | -7.48486 | -55.27536 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4065e0d5-c840-315b-b151-0b1ed84735c6 | -7.29356 | -44.08084 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc22cccc-c16d-3f4b-b29a-26dc5cc7a1ec | -6.6293 | -58.48849 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a898b29f-0f50-34bc-9f51-4d1a356cba89 | -6.14682 | -59.91759 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b6f3c86-e5a3-3b56-bd65-f7a48e212366 | -5.5131 | -44.11652 | 2026-08-26 04:51:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3beb44a-f3bd-355e-a6e3-13405bd0b091 | -3.12463 | -61.18886 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34bd3175-85e5-32ef-86b6-5d2ca137e3e8 | -6.71362 | -59.12904 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44c80190-4dc8-3e0c-b9e9-5fd4409354da | -9.59648 | -45.99616 | 2026-08-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d147dddb-a8ff-38c9-ab16-5c3ce18db97e | -9.62246 | -48.29594 | 2026-08-26 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47307a62-f4e2-3259-aaf2-1197a29b8ae1 | -7.52834 | -61.38298 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0c067574-8639-3074-a893-bc05481a6967 | -8.62198 | -54.73419 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c9cc785-192d-3024-8dc0-b34ecf887554 | -8.62305 | -54.74926 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2587cd81-3999-3600-8d57-6fe38ee37a1d | -8.09985 | -47.56419 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1f01299-321b-3179-bbe3-fc4209b13c08 | -6.27997 | -53.36803 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38aa819a-611d-38ea-9b17-8027122daed9 | -6.55849 | -55.09892 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c4f5554-505f-3d58-accb-0162137a4b6b | -5.07499 | -44.86027 | 2026-08-26 04:51:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdbed87c-89c1-3735-9c0b-b13d1c2eda2e | -7.0643 | -59.22224 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| e66a2fb7-4db5-3d25-8813-0e06ea04ab7f | -6.80086 | -59.59962 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8f867702-59e0-3695-8fc0-8f1e7ccb298c | -8.11236 | -47.46613 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fee27d77-4bad-3933-9066-65854f1f64a1 | -9.4409 | -51.68163 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8bce980e-1318-34c0-945c-8e51e0c0891e | -8.64388 | -54.74885 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 411f61fa-2f6e-3928-bac5-2667136a9758 | -7.77852 | -61.56982 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README30.md)
