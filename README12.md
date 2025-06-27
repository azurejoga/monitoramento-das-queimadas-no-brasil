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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 605c0bd4-6014-3445-86ab-37b7c68e1ea4 | -12.15091 | -44.80087 | 2025-06-27 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 183aa1f7-eb28-3019-bc43-73b602d51ab4 | -12.03133 | -47.77343 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2a6e82c3-1b8f-3566-9f12-0c9852b9c171 | -9.51242 | -45.42223 | 2025-06-27 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 31f4f459-85bc-3cac-b74f-f634f66235c2 | -11.57864 | -52.10645 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ddcdc905-6d06-3f21-9f66-16a871f19c13 | -13.93957 | -54.50062 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dd5c30d2-de69-3c40-a3a9-3dfc3ecc714e | -12.61133 | -57.8802 | 2025-06-27 04:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45d34600-197c-359d-a1b1-e496b0ded33a | -12.5857 | -57.378 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddd42bd7-1102-3359-a504-084d610521be | -11.06033 | -55.38157 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e3522b34-8cc6-394f-bd2f-39a1fc3b5425 | -10.45807 | -49.57676 | 2025-06-27 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af434340-3493-3d10-9196-124a3f1438a0 | -8.62418 | -51.57543 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e3aadd53-fd77-3ac5-bbfc-4cc6228dee54 | -16.62342 | -47.02248 | 2025-06-27 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9736c3d8-0a65-30d8-9a87-6e85a0937fe8 | -11.80853 | -57.35507 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8c064ce-aa58-36fe-b430-2dfbc7d17fbe | -10.70774 | -59.12404 | 2025-06-27 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de5d58fe-584a-3a4f-b643-8b67894801ac | -8.61918 | -51.5713 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e7b74b77-4bbb-3481-b8b1-7e5f39e2629a | -8.61983 | -51.5747 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e8cb0e0-d20e-3af4-89f8-73d63fbfde43 | -11.43613 | -54.47202 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1871f77c-6d94-35ba-85de-0b70757d8d54 | -10.30293 | -57.13052 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c16ded78-92b4-30de-a94e-5bc5e1162682 | -11.80941 | -57.35067 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74ea4c5a-2309-3de5-a3ac-44bc0d7c9769 | -12.0037 | -47.16432 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff598be4-33c1-3be9-b48e-bb981df56df3 | -10.66615 | -44.46446 | 2025-06-27 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7e24bcf-bb39-3e85-9e10-f90e9845d39e | -9.8759 | -48.05186 | 2025-06-27 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a2594c1-41f5-3975-8333-7118e8f2371a | -10.82712 | -54.04989 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d71f09dd-0593-360c-8057-7c2874761416 | -17.04423 | -43.77808 | 2025-06-27 04:21:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68c536fe-c1a3-3c4f-9bd4-3c7fee18a666 | -11.84159 | -43.79959 | 2025-06-27 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4863b8a6-e204-39ab-b5b0-30f98d6d3ad1 | -9.74519 | -48.04304 | 2025-06-27 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7123eceb-02e1-3287-a6d8-bca5fad24d0a | -13.94647 | -54.49051 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c68c26c4-6ce1-3d27-bec8-45f93ea35903 | -11.44116 | -54.47294 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03c51777-b60b-302f-a530-7345ddd67542 | -9.74868 | -48.0436 | 2025-06-27 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6a1bac1-e680-3fd0-9863-cac4546301a3 | -10.29653 | -57.12684 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d4b0551-d80b-3086-acb6-60eab60ac308 | -12.00313 | -47.16789 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d0bcdba-6982-3578-b3ae-1e1911c1f11d | -9.11905 | -49.44626 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 030236c9-e6da-3e52-8c36-c7b8f86c1d2e | -11.67109 | -46.73279 | 2025-06-27 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15a82c42-32f3-373d-ade1-ea64378577ae | -10.83344 | -53.75404 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73187a54-fda0-3dc7-963d-fb194ce1ba39 | -10.87275 | -53.77637 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0980a75-0c71-34ef-85ff-6bcc31605825 | -11.13732 | -53.91729 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f77648d-c8cc-3f77-8622-78dd5a735e07 | -13.59044 | -45.25534 | 2025-06-27 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05d7e9e2-b0fb-3502-bf8a-15f3203141ef | -12.15099 | -44.8231 | 2025-06-27 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6628833a-efa1-32a1-ae7a-ef6d94a4857f | -12.02456 | -47.7723 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7e101e97-8730-33b7-802a-671c4473dfa9 | -9.78493 | -48.57445 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdd1ffba-506b-3df3-bea9-2186bbad940b | -10.70648 | -59.13016 | 2025-06-27 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| deca9110-127c-3225-b8f8-a9cac2ae9754 | -11.57134 | -52.11286 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 16210a50-1f78-397b-8c5c-7244e612ff89 | -9.75565 | -48.04472 | 2025-06-27 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0c82050-9541-3d6e-bf1c-d126fab30de1 | -12.43358 | -43.722 | 2025-06-27 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4b8a249-7403-39d5-bf4c-96849d08dbf3 | -9.35951 | -58.84974 | 2025-06-27 04:21:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6c44a3e-f821-3f76-a5bb-f0849d70427f | -9.2808 | -46.50294 | 2025-06-27 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a25124c-84d2-3c31-aa21-a7068263c137 | -8.61706 | -51.58379 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a75c644c-c52c-3ca3-b188-414861bc0922 | -10.52527 | -53.62947 | 2025-06-27 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e969d70-91eb-36ac-b796-c693d23de3e9 | -9.3446 | -58.85357 | 2025-06-27 04:21:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bed0ea85-0792-3252-8246-7b3ec05ce564 | -11.56934 | -52.10909 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 97d98d6d-d0a3-35fe-a15e-c18a7e9e4f1a | -14.4459 | -48.86819 | 2025-06-27 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ef4d7f9-f9da-3721-bc94-96461769cf87 | -10.71463 | -59.12488 | 2025-06-27 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 60413b33-ae56-3e1c-9909-de46e445b17b | -11.17987 | -55.92612 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2642e17-6859-3303-b69a-58fcfba31eef | -10.83099 | -54.05656 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4cbd1c13-75c4-3c5e-9720-cfb1dff35111 | -11.77606 | -45.21181 | 2025-06-27 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 561f871b-2cb4-37b0-9d05-8bc2b5e85039 | -14.44311 | -48.8637 | 2025-06-27 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ce67e78b-9536-3804-b317-3e9596a7b636 | -10.3017 | -57.13269 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 879044aa-c526-360f-9401-0fac24ef06bf | -9.07524 | -49.42694 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 54cae2e4-dbf1-34c5-969d-7fc7c3473809 | -11.82115 | -47.53436 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df71326f-50a8-3326-9619-f4306c1f32fd | -8.61847 | -51.57552 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 85f83d05-1505-326d-9138-8a24b4482a15 | -14.01521 | -54.49087 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea54efaf-5430-3915-8510-147da93f0a78 | -10.2594 | -44.63906 | 2025-06-27 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e3a8cacd-b12e-35c1-98a8-ca28b3bd2f5c | -10.41891 | -47.50866 | 2025-06-27 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad319e40-9372-3ece-9a30-cfde9072dbee | -9.51317 | -56.10653 | 2025-06-27 04:21:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2a9a764-c152-36fc-85d6-2ae3082693b7 | -8.33556 | -55.09423 | 2025-06-27 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffe9d780-421c-3575-8db4-d4f6aaf067a7 | -9.79128 | -48.56393 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 363b86b6-95d9-3340-9a9f-d4cabc71c4a2 | -11.92042 | -54.81307 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38fc9dc4-5c49-3fa7-b3af-f5a3d01d9462 | -10.29686 | -57.12933 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5c5db78-101c-3bc4-b4ef-8ec5252e0644 | -12.80576 | -48.73512 | 2025-06-27 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1ce968e-ef99-39a7-adc3-9400bdcc01e5 | -13.93583 | -54.49404 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a23603f3-ced3-30c1-b447-fa56c5a73b5c | -10.82293 | -49.1029 | 2025-06-27 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33c87cd3-589c-3a1c-a75e-cea5dba43e89 | -10.82572 | -53.74137 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c641e9a-de50-3132-933c-579cafdc9de2 | -13.64918 | -46.81242 | 2025-06-27 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47eeab4f-54b1-3853-afa4-430709e87493 | -11.7722 | -45.21482 | 2025-06-27 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a40e2548-df54-39d0-a64e-0696f3fd966f | -17.04485 | -45.88783 | 2025-06-27 04:21:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9283d1c3-82fd-3f97-8cbe-52fb5e8f0819 | -14.40236 | -47.89341 | 2025-06-27 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a55822a-2f3c-3681-b7cc-79c5460b13fa | -11.95499 | -47.02369 | 2025-06-27 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c121333f-887b-3012-aad3-bbeb387c1473 | -9.06995 | -49.43549 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb0bf728-f0c9-3bc8-b080-b08540d62a44 | -14.23959 | -45.50233 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5c7a927-ea71-399a-84f1-2781af33b95c | -10.29779 | -57.1247 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f053d9f3-4d41-3712-b9a5-cc0d5e667407 | -12.00761 | -47.16128 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7ec7f1a-6ada-38a1-a35e-b0af99f2ce83 | -11.18682 | -55.9198 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3fba858-09a8-3711-86bd-cc2abbc03378 | -14.29393 | -41.60419 | 2025-06-27 04:21:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57c2f064-d2b4-34b3-9d76-bbc96f4391d2 | -9.11606 | -49.44103 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c75c17ba-cc98-35f0-ad2d-45d4bf5dc5bb | -13.29423 | -57.08548 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2dfdd93-18fa-3660-b017-a12d7a128ba7 | -14.53789 | -53.83263 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38e2e0c2-4b30-3707-be84-427db346a639 | -9.11685 | -49.43642 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9c7640f8-fcc0-3983-bb1e-4f98aced6f11 | -11.78083 | -55.03578 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7ac108c-f7c8-3187-871a-1e2014b0e499 | -14.53637 | -53.83967 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05e3ac45-fe73-38bb-a22e-f9feab36d544 | -10.6628 | -44.46394 | 2025-06-27 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c529932b-4c8b-386e-9482-9ca3f33c5b41 | -10.52624 | -53.6241 | 2025-06-27 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 47851e5a-3e84-3321-9532-372a78be3b24 | -13.58029 | -45.26091 | 2025-06-27 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3644c83-9b1a-350d-83e2-05856ddde62e | -12.28316 | -48.80301 | 2025-06-27 04:21:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c94f3d87-4bd0-321f-b902-20d09a3220fe | -12.03339 | -48.75021 | 2025-06-27 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab645545-5de7-356b-afb0-296a348b265c | -14.23571 | -45.50541 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdd98dce-665a-3c03-a062-0bb9d64e7472 | -16.4287 | -44.52329 | 2025-06-27 04:21:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f69a693-9bc7-3274-82cb-68d58d92457c | -14.53696 | -53.83746 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94fc10be-80be-3054-83bc-2306efe0f942 | -10.62584 | -46.69258 | 2025-06-27 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96e6ddd6-96d1-30da-b590-299162a5aa69 | -13.15922 | -45.23185 | 2025-06-27 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb57d7cc-2099-3b85-913f-4f05cbaf40c8 | -11.67497 | -46.72979 | 2025-06-27 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7b62078-dab0-38ec-86db-071dcc789198 | -8.61341 | -51.57895 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README13.md)
