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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3afd0f4a-7225-36a0-b743-5e2fb5f29e12 | -11.07598 | -54.02698 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98231ff6-afde-3389-81a0-4f766484bc08 | -13.08609 | -47.47208 | 2026-09-20 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 549ef446-e632-3caa-a135-1fcecd135056 | -11.44647 | -45.3325 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42f1d708-f718-3817-8799-a15370180d98 | -11.95033 | -50.09493 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fabe6a1-5562-3e35-af7a-4531514f2b5b | -7.62388 | -45.42531 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0b09569-b293-314b-adea-03e99afa351c | -13.3217 | -51.29604 | 2026-09-20 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb8788c4-7227-35c1-8d40-c21e421927f4 | -8.165 | -54.74572 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00dd2e01-0e88-3a7f-ab24-26df3862cb32 | -10.36935 | -50.45054 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3cc0c77-1e24-3ce5-afe7-5317399abdc0 | -12.15954 | -47.02669 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8070f90-a067-35d4-822c-c6655b78ed57 | -8.17293 | -54.77771 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 944ed412-4188-3a25-b597-38625d29fffb | -12.28811 | -47.12939 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 601c6fa2-9690-3cc6-b551-23d3e2368114 | -13.94847 | -47.85201 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3413a056-1dc8-3154-8bb1-153a25376a67 | -6.66909 | -50.89621 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 943ba5fa-6e77-3e61-9134-390712e785bb | -9.47178 | -54.45071 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e11a503-d875-309c-ab72-89ebfe082423 | -11.94405 | -55.92289 | 2026-09-20 04:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 134281c6-78b7-390d-8668-80f57ed0db42 | -12.13405 | -47.03067 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 700ad2d3-2969-3c71-bc52-10f2770f622a | -8.32745 | -50.94595 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b849a6e-4a3b-38f0-bd0a-a43fb5ed6405 | -10.30488 | -50.24292 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b5892f03-f15c-3b3b-951e-fe801f535ac8 | -10.4134 | -48.93454 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9c647fa-0eac-331e-9cf8-0679f94975b0 | -11.85545 | -46.86274 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad7c3101-5369-31b7-a7a2-3e97e4c3b7bf | -7.75803 | -44.88368 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d57e9ad-4ceb-3f2f-a26d-1c71723166f1 | -7.08736 | -44.72186 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 610c9a3b-5236-3b44-82f4-2bc8319e6b39 | -7.43259 | -44.73825 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da5a8ec0-c2fc-38eb-85cf-58d653d4bf1b | -11.47556 | -47.75628 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69d76fcb-666d-357c-adbf-2e094d2c637c | -5.97786 | -57.78077 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9366cb70-70b2-3af1-97dd-3131dec31f5f | -9.18819 | -60.76711 | 2026-09-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f59d707f-fd6c-3efc-a3c5-48fb402ca25f | -9.16652 | -51.5103 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39e88085-7d61-354e-beb0-3e62d06593d8 | -6.80148 | -47.82591 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0635cf5-311c-3c99-bf0c-d2f13cbe64c0 | -11.85493 | -47.6754 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5df67bf0-d595-3e49-8c60-127db7a6e45c | -8.28069 | -50.83806 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| accd0df8-5ed7-36be-b7e9-c872fedd6419 | -5.84518 | -53.54977 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d17db1cc-3190-307e-b0b5-bea7cb3725d3 | -8.86986 | -45.9557 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfe6dd6d-c0c1-346b-a66b-c347611456a6 | -11.04694 | -54.15693 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6817ee1d-ee38-3e09-a24e-7321a65bc9b3 | -9.2363 | -46.18624 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56d81862-abda-3fba-90bc-4001be6e7ffc | -8.93372 | -44.39211 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d514c852-9d2f-368a-b746-84f63e8c1927 | -7.17199 | -47.456 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1195528-0aae-30c8-9b16-b53a450b7a47 | -11.01609 | -54.13618 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cd60941-fe79-318f-a4fa-10435c18b122 | -10.31774 | -49.13023 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b572714-10da-3574-b2db-90309e62a3fa | -11.04043 | -54.16264 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e820f936-1557-3420-be43-ffaeeebb1367 | -8.61734 | -55.23142 | 2026-09-20 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90847d29-00fe-320d-91f7-14662521aa1a | -8.84511 | -44.92391 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93c7a3e1-7e82-3866-9cbb-334fe7bb3750 | -11.38177 | -51.42009 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6708b5a8-6a68-3692-bd3f-b3ddcdf0b7ec | -11.01058 | -46.52248 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f29501f-ae6e-3afe-b2af-9fdfd777fd1c | -8.65406 | -45.43818 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8167997a-3fda-3f40-883b-279b2a3b0bdd | -11.66708 | -43.41853 | 2026-09-20 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6647b0a-9118-318a-bb48-3bd10daa0209 | -6.65355 | -47.47097 | 2026-09-20 04:40:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3940bd81-957f-3985-a3cb-f5672a894d30 | -11.87418 | -49.9983 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3e231dd-f7c3-3ab7-81cd-c1f3c3dbc18e | -5.99891 | -53.69134 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94e27303-cc74-3817-9a77-1c90e463f1fe | -11.48962 | -47.75471 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 590f49fe-1fe4-3194-a352-25e4fa27fa96 | -12.23257 | -50.15955 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ceda19d0-1c68-3335-ad66-6570930eebc3 | -11.31053 | -51.72086 | 2026-09-20 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9758762b-69e9-3259-bae5-edde995315db | -9.71939 | -47.22108 | 2026-09-20 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae6c86df-e629-398d-9785-6e74058805a5 | -9.12483 | -45.72829 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5833ca00-13a8-3ef6-8632-aced7b0bb433 | -7.68479 | -44.66665 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 33ada2e3-8411-30ad-97c7-a0c11f94cdf3 | -11.23491 | -48.37456 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 482fa38b-c4f8-3e40-b389-39889fe34b8a | -9.0489 | -48.71417 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d77ede77-ec86-34da-8407-4d5efc3fcacf | -11.76541 | -47.43704 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d79498db-4a16-3e87-97b1-2fb584bfd8f6 | -9.26279 | -48.2414 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bf8117d-31b1-3a22-8228-84ba805895c6 | -10.76091 | -51.66777 | 2026-09-20 04:40:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cf25eb0-74ba-3022-8bc5-416ebba99606 | -9.5805 | -55.10165 | 2026-09-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a221e618-960a-379f-b424-d276e1f9b5b9 | -11.87077 | -47.66276 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62ed075c-bef5-32f0-bff7-94bb08160fe1 | -10.04342 | -48.50243 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71e6bce7-a281-33d6-a4c7-641cd07d617f | -7.52777 | -45.44086 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fdb580c1-3e47-3790-86ab-6a6f1b1c9669 | -9.72873 | -48.14996 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1761051-99b1-3408-8d13-6e7cecaccc5a | -11.046 | -54.17834 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4740d02a-21be-33d9-b442-44bad9b6a8cb | -10.39457 | -48.90257 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d58dbab-e496-3186-bd7b-4910ad09e457 | -10.48132 | -46.29199 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c34790f-a7d8-3542-816f-efd46708053a | -13.73003 | -48.78227 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0133745-ced4-381a-82a5-45b7170a10a8 | -8.01803 | -43.33313 | 2026-09-20 04:40:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b307e00d-ce50-3b1f-a241-e756eb6d1a88 | -9.12126 | -45.72775 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 202e5a95-6c55-36aa-9aae-c1f2c3974eea | -13.94787 | -47.83248 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ed103be-170e-365a-bee2-076049fed349 | -12.52991 | -50.04126 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 225a6b3e-8075-3a0f-b635-683c9d6cef29 | -8.25196 | -50.8176 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 035ed311-319e-308d-bb04-1aa261ab19ed | -7.56122 | -45.41283 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d62ba55-81c7-3207-aeed-314bb8da804a | -12.77293 | -52.86053 | 2026-09-20 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7d07a89-2281-3d91-bb01-1cf2205534ae | -8.30187 | -50.81774 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8fb9eaa-e34d-3f24-a399-cd148e1b10b9 | -9.72486 | -48.15295 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5854f7ed-2d45-32c3-b7d8-b12255531aaf | -11.94803 | -50.10916 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 521daced-4b5f-3268-9b6a-ec49fa3193bb | -10.9257 | -53.96039 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0ff5c3f1-7b14-346b-9fa0-cdc647476010 | -8.87045 | -45.95177 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c64aafa-a510-308d-8789-6b8d5c045c93 | -5.20091 | -56.0479 | 2026-09-20 04:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e63d930-add8-375f-b244-2936c5be21a4 | -14.11278 | -45.60827 | 2026-09-20 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3805b962-84f2-3012-8130-22150b27b5e1 | -8.92099 | -49.99498 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca37fd1a-be1c-3381-9f73-c5ed994dcd45 | -5.72976 | -53.45677 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d51f5a7b-bc63-335d-a2e1-a3c5be7eafd9 | -9.26483 | -46.21067 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c004b8bc-aaa4-3c98-af99-3bdde06cc362 | -11.87603 | -49.00501 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e6b5eeb-000f-3e73-aaa3-25dec2f9af49 | -11.04557 | -48.30061 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12487d4e-99b8-342f-a697-7b4ba677a151 | -10.47697 | -51.26325 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cc002981-03e6-3e20-bedf-bed3e5e81000 | -6.78711 | -47.80943 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cd7cb2f-5ba7-3488-8a1f-d8142c0b728f | -8.42993 | -46.86015 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7d33f9d-e5f0-3277-ab54-480cc57b2132 | -5.89768 | -52.09736 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4486be70-c1f7-38a5-8cdf-bc00992088d4 | -8.45524 | -48.45188 | 2026-09-20 04:40:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94806144-3a79-3836-a531-c13d7b3963ef | -13.39166 | -49.45037 | 2026-09-20 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9ff932d-3ed4-3248-946f-d374786169ec | -9.83878 | -46.40997 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ee97b26a-fc3a-3325-ae55-981203036263 | -7.43429 | -44.75185 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 64b8b2a5-f20c-3b7e-a7f4-1df3314eec19 | -11.38057 | -51.38427 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99714ea1-f4a0-3d92-98fa-c42a5e699034 | -10.56839 | -50.88159 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f78fc1f3-3d0b-340a-a4ee-ca72ad85abcd | -8.48219 | -46.86401 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fcb4223-beee-386d-b3f5-6d7f70cb140e | -8.61407 | -54.60909 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79cdad45-821e-3f98-9f91-635a9408428a | -5.83877 | -53.53696 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README74.md)
