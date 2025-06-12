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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e20b6753-d8b4-30b5-8bb2-1c6bfb336404 | -10.28303 | -48.20923 | 2025-06-12 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f212cb11-0c92-31fe-90e7-715285dae362 | -11.5711 | -47.43792 | 2025-06-12 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e39adbec-fa5b-309e-9d2d-1186d852b401 | -9.60529 | -49.02267 | 2025-06-12 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d8b73df-d4fc-3e44-ae35-00cb973076c0 | -12.05437 | -48.08012 | 2025-06-12 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b1edabe-b046-3e6a-bda4-2837952a88e9 | -10.70765 | -49.52313 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7236ca4-aa8c-3c45-bc33-8aff6b29af82 | -11.56993 | -51.31261 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8c0f65a-162c-33d6-ba78-6ec5bcbf59b0 | -8.07241 | -34.97716 | 2025-06-12 04:02:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c0e90fb0-ac64-3461-a507-e6130780ee64 | -11.27795 | -44.6419 | 2025-06-12 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c27c4bba-6d6c-3a56-89a7-5bf35cea6a3d | -10.65323 | -49.42397 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 896d12db-24ff-3258-8192-69bd31a77ee1 | -7.23736 | -43.10432 | 2025-06-12 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b92d5d82-3123-388c-8850-2fc673775075 | -6.16184 | -47.27018 | 2025-06-12 04:02:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ac511a8-0e6a-36f2-8213-7a35148c18ca | -10.07125 | -52.74601 | 2025-06-12 04:02:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dccc812-c368-31ea-b838-e0979eb0ec58 | -10.88771 | -54.75687 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| afb49090-4a5b-301b-9a27-1362910ee5ed | -11.77668 | -47.31683 | 2025-06-12 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a4deabc-e22e-3823-a558-99bcfbd487b7 | -10.88912 | -54.75335 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d21327b6-9b49-3f1a-bc9d-df5c319d809b | -6.94778 | -44.56691 | 2025-06-12 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 09bcb3e3-cd1b-3496-acbf-bd572b202e53 | -8.66066 | -47.13222 | 2025-06-12 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2aac6b91-891e-304c-bf52-465a9bf4e034 | -9.9883 | -47.84749 | 2025-06-12 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86ab39e2-0da7-3687-8500-223bc40c7c20 | -11.5797 | -47.43962 | 2025-06-12 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f32426f4-df5a-386b-aee5-c8258f79ef39 | -10.1379 | -47.43898 | 2025-06-12 04:02:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c73fc380-1aca-34f5-b113-047ea4761947 | -13.34437 | -40.30828 | 2025-06-12 04:02:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0088f021-017f-3494-8f8c-39910c18dadb | -8.31272 | -47.91706 | 2025-06-12 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 671112c2-a68b-32ba-9d59-3d859d17e076 | -12.23446 | -44.16646 | 2025-06-12 04:02:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6a7e70fe-aa4b-329a-b4fb-42f9a79de69b | -10.66029 | -49.35866 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| edb57852-139b-3227-80e6-1671cb950cca | -10.69976 | -49.50932 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 011db411-3495-30a6-8933-4cf7f21b0e96 | -7.23671 | -43.10835 | 2025-06-12 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 46c819c7-8346-34a3-b69e-ed7490505272 | -6.60664 | -44.25992 | 2025-06-12 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afdf4eb3-33e9-32a4-bcd2-fc217c9f9f72 | -12.76866 | -44.40464 | 2025-06-12 04:02:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a61226dc-ad50-37c0-b322-b72bba0909d1 | -9.41472 | -48.43125 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec92c25a-6a93-39b1-bf1e-d2a8dccbe9c0 | -5.91472 | -43.45995 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 01909b8a-c9d5-3545-81fd-21b7e09ca104 | -12.38078 | -45.77226 | 2025-06-12 04:02:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0e6da74-25af-3af5-8e60-771d4de59304 | -9.41504 | -48.42794 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4714c5b-7254-3720-8364-a028ea41c12c | -11.56377 | -47.45383 | 2025-06-12 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d52b8bc-70cb-3499-810e-a6a6ba628c39 | -10.9978 | -50.76191 | 2025-06-12 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd7ca2ab-fb75-39bc-bd41-483a8c07ff20 | -11.57141 | -51.30511 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 633b3eac-cd65-3b51-ac01-c86ec42c529f | -9.41026 | -48.42704 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a7e9acd-1429-3db3-9eab-064eadb1c7f2 | -11.61102 | -46.99343 | 2025-06-12 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 046c83fa-e0c7-3e6a-977d-3e5bb79320dc | -14.42494 | -47.89894 | 2025-06-12 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3c846b1-a181-3437-9407-5ea674722d43 | -15.71965 | -43.49242 | 2025-06-12 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20c289fb-609d-39d6-9aa2-b881c0cdaf6b | -14.175 | -45.48764 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba6bd0ea-9494-3be7-af62-c351a8bd507b | -20.37759 | -45.60299 | 2025-06-12 04:04:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3725b76b-37dd-31f8-b95c-43af3e0c1d80 | -15.72814 | -43.29785 | 2025-06-12 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c34c8e2f-b4f0-3514-b271-ec6e6b52b69c | -14.03584 | -55.13391 | 2025-06-12 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6848961d-b990-3fd2-a6c3-fe3ad73e41d4 | -11.77023 | -54.37173 | 2025-06-12 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e1d8ff11-65d0-3610-8d66-61664bc86cdf | -19.5789 | -49.10281 | 2025-06-12 04:04:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58b3ac6d-abbc-30ea-85ca-b844f8860e06 | -14.18235 | -45.48895 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c34894c-0cc4-3ef5-87c4-ad5b44029bcb | -15.37828 | -47.88164 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96d96459-62d3-304a-97ed-1f7cab1ed28b | -14.17421 | -45.49212 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2967553-f743-32cb-8921-815ee8c76a5a | -14.84667 | -48.31428 | 2025-06-12 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01daa2df-57ea-36ee-8b2e-322a5323bb55 | -12.20777 | -49.62565 | 2025-06-12 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca78a8c0-3278-3608-ab88-7708dc240b3e | -11.37452 | -55.11007 | 2025-06-12 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e04f112b-0c6c-3b34-8dfa-7e04141b717e | -15.37413 | -47.88076 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35c91aa1-e714-3e89-9246-fbbd29f86917 | -14.65576 | -48.06888 | 2025-06-12 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40a5f622-6a5a-3d02-aac7-dcd111abd483 | -19.57736 | -49.11087 | 2025-06-12 04:04:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1af8ab23-9868-3758-a7b8-9896f4c5cffb | -20.44909 | -46.40481 | 2025-06-12 04:04:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c884c46-0379-3ec6-bb45-693c619d70f2 | -15.723 | -43.493 | 2025-06-12 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 684ce0cb-15d3-3556-9bc9-7897078de3a3 | -12.20718 | -49.63498 | 2025-06-12 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16339208-7672-3d69-9fe1-760d6ce56181 | -14.17132 | -45.487 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87e41a4a-57f8-3c1e-b643-0e437b567e88 | -14.1897 | -45.49025 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c21d4213-7556-3ba8-b306-0cdf714d2518 | -14.42577 | -47.89444 | 2025-06-12 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0587edb7-a10e-32f6-a237-00a461099d38 | -19.51268 | -44.27578 | 2025-06-12 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55ed2cc3-ca51-3535-a292-aa6f6bcc612e | -15.36903 | -48.07819 | 2025-06-12 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9099431d-d93f-37f5-94ec-d7e8c2fa828c | -15.37974 | -47.88126 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d0d2ed14-1f1f-3aa2-90be-554a07184a21 | -19.49861 | -45.28791 | 2025-06-12 04:04:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a9921bd-577e-3fc9-9ed1-38095c8169fb | -14.03425 | -55.12204 | 2025-06-12 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bb685a9c-2bee-3b21-a5d6-b9bab20b983f | -13.6576 | -53.94587 | 2025-06-12 04:04:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 97a7b933-8d42-3106-a151-8b1d4c449ca3 | -19.96893 | -44.21531 | 2025-06-12 04:04:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0eee0aff-b495-3146-9b81-572c3dc0f54f | -15.3756 | -47.88037 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab9ab669-7cdd-33e3-bb46-1a47d85b4851 | -12.43342 | -54.87282 | 2025-06-12 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0531de5b-e72b-3c95-9b58-662b093d8846 | -14.17867 | -45.48829 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3eb668c8-895f-300d-8f82-002054ff1a2e | -14.03162 | -55.13395 | 2025-06-12 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8550eae1-4885-3c81-9394-ff5e6a2daf45 | -14.1868 | -45.48514 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ede6c6bd-4566-3c34-90fa-4fcbfdd73b1c | -14.03043 | -55.12642 | 2025-06-12 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c86bdcf3-c34f-3e54-ac40-7b8c64d369ec | -14.18157 | -45.49342 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1109a050-c495-33b6-922e-4d56461a1859 | -20.45057 | -46.40158 | 2025-06-12 04:04:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 222dd424-b802-37a2-84a3-ba0c087d4767 | -13.89382 | -54.65757 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7b697f06-6a98-3bc8-8531-8a8c2c0cc2f2 | -20.44624 | -46.40014 | 2025-06-12 04:04:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ad404b4-a3e7-3669-a9ab-4cb7c5d0b811 | -15.72025 | -43.48874 | 2025-06-12 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8da511e5-7a0b-3186-b915-90c89aafa1ac | -17.28934 | -42.66358 | 2025-06-12 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 89820165-dabc-3a97-ad1f-d0cbaba8845f | -15.37486 | -47.87674 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0a21052-0724-32d8-8a71-fe60bbb78186 | -20.44979 | -46.40078 | 2025-06-12 04:04:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99d02684-4c20-392c-9825-dfb1fe75b035 | -13.88967 | -54.64493 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 943825dd-dbf2-328f-ae7d-e0dc9f2433d9 | -14.03711 | -55.12795 | 2025-06-12 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c99ccf8f-0e3b-3264-a892-a88c6200f912 | -17.28548 | -42.66661 | 2025-06-12 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 39deef23-d43e-30fd-b264-54557ca84f0d | -11.86944 | -52.2565 | 2025-06-12 04:04:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8d8caaa-8edd-377d-a714-15961571c322 | -20.44701 | -46.40093 | 2025-06-12 04:04:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9416516b-1819-39be-9a29-73b807e293e1 | -14.18602 | -45.4896 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9ce4c8f-e7ae-30e8-96e5-0ec547d89496 | -14.17244 | -45.48452 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05f1d1b5-c05d-305d-871d-84f94efaf212 | -14.0317 | -55.12048 | 2025-06-12 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 73b3de7c-2c31-3d4d-8185-a25809f13888 | -19.97921 | -44.85712 | 2025-06-12 04:04:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2ce0d9a-7975-37d4-8db0-eaa57a8bd864 | -12.1405 | -54.66184 | 2025-06-12 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1207a72-7f3a-3082-8651-b9a190e6c223 | -15.17615 | -43.06588 | 2025-06-12 04:04:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7fddc1f3-a524-33d5-ae3d-f337bef2b5a0 | -13.52857 | -47.86166 | 2025-06-12 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29f04e7c-26a9-3b2f-b8e7-cf411baf4bae | -18.86396 | -49.11457 | 2025-06-12 04:04:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 995d7450-dcf5-301c-ad14-077831fd7206 | -11.37315 | -55.1168 | 2025-06-12 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 209f5d20-139e-3d0a-8ff5-151f72692097 | -11.37926 | -55.11152 | 2025-06-12 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e177cdf3-3612-3f9d-b23f-08f83581ea68 | -17.28878 | -42.66717 | 2025-06-12 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1f23ec59-6aab-3804-baa1-1e2196c78301 | -13.88842 | -54.65078 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7603f230-7fee-320e-827b-c67aa587256d | -14.17054 | -45.49147 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bfb02e7-f333-316b-a51f-a8e31b721ed7 | -18.37952 | -44.5124 | 2025-06-12 04:04:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README9.md)
