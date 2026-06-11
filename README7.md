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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e7e05c2-886f-3a6a-a3ba-25765260d304 | -9.6244 | -49.02361 | 2026-06-11 04:29:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84d597d8-3b28-3143-b9b4-b1f847077083 | -9.3146 | -48.96518 | 2026-06-11 04:29:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c7b78f9-f35c-3033-b1a9-10db615d2847 | -9.03762 | -46.30618 | 2026-06-11 04:29:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65249cba-2299-3ef0-b0e4-0171bd8afb43 | -10.38225 | -46.63063 | 2026-06-11 04:29:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03439dd0-e8a7-3a38-8608-0d4a20777b52 | -9.32128 | -45.48331 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a76898f2-21fd-3600-9b16-fb241144994c | -9.10984 | -50.91368 | 2026-06-11 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 222b0d9a-655a-34e5-b101-aa4b39caee47 | -9.80433 | -46.70021 | 2026-06-11 04:29:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52a21f65-a10e-3d0c-a6db-4a4492bd092a | -9.10607 | -50.91306 | 2026-06-11 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4af33df7-ab2e-38cd-b9a9-208724492872 | -9.3241 | -45.48747 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 53036b34-aa0a-37b7-9163-f7832cc40fa2 | -8.51379 | -47.02097 | 2026-06-11 04:29:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7539783e-aefb-3ffb-bdc1-fecfa2fd55b8 | -7.59711 | -46.45872 | 2026-06-11 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2532e0a3-5b3f-3246-af4c-9a89eafd5745 | -9.3089 | -45.47396 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b57dd628-29b2-31e0-8cfc-aa2c33fd9941 | -9.3027 | -45.46928 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e40d87e-4a15-3c9f-aad9-324271da7f66 | -7.34969 | -49.84848 | 2026-06-11 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f9edb7d-4026-3d71-8bcc-cfa334b3b8b2 | -9.31172 | -45.47812 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e654c03f-f08f-375b-b7bf-0e3732fb737c | -9.22029 | -48.57314 | 2026-06-11 04:29:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b02bb42-0b92-3006-90cc-e0d735e425be | -9.31398 | -48.96897 | 2026-06-11 04:29:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b5b5307-acf3-3f18-b44f-be24bfbf3337 | -7.99688 | -43.87265 | 2026-06-11 04:29:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8b446193-2cc8-39a3-9e12-e347af1e916b | -10.28445 | -47.61539 | 2026-06-11 04:29:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 841b11c7-5016-3d78-bed2-5dd96c4c7b22 | -9.21009 | -47.9176 | 2026-06-11 04:29:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cc340a5-b112-38f6-91e3-6d133af8cea1 | -9.31847 | -45.47916 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e5267119-e14f-340a-aa8d-71faea49196d | -8.98833 | -48.0859 | 2026-06-11 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71b62357-015b-38fe-9410-5ddba36c7238 | -7.3458 | -47.01577 | 2026-06-11 04:29:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72b32f57-ddcc-3959-b981-2ec04a9fefae | -8.10752 | -49.64388 | 2026-06-11 04:29:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bd94c27-e1da-3ca6-8d77-7fd314de6ebb | -9.21065 | -47.91405 | 2026-06-11 04:29:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5054e874-8a7e-36d9-812d-1cb7958e69ff | -9.22088 | -48.56948 | 2026-06-11 04:29:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eee95692-3342-309a-97bc-4a866a2ca924 | -9.74586 | -47.88104 | 2026-06-11 04:29:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f51613bd-3924-37bb-b222-e3a2fa75593d | -9.13801 | -47.9823 | 2026-06-11 04:29:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2b25cfb-0365-3b57-9a0e-84dc7ef7c9fb | -9.11024 | -47.96323 | 2026-06-11 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b165e9dc-6783-38f3-8561-7c294a5ab4b8 | -7.72071 | -44.16404 | 2026-06-11 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4345a945-a6a7-3265-8870-9249ee69edc3 | -9.69969 | -49.22632 | 2026-06-11 04:29:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32b59f77-6a6c-36ec-ace7-526bd9a69d3e | -10.38998 | -46.62468 | 2026-06-11 04:29:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef5ff621-9cc8-3c6b-be38-0de5d4544907 | -7.87586 | -47.1007 | 2026-06-11 04:29:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 785caf3a-ec3a-3746-823c-e8b74c126da3 | -9.10905 | -50.91833 | 2026-06-11 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 188b5a33-6003-3d09-81b2-218f21613591 | -8.32649 | -46.80973 | 2026-06-11 04:29:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a038b2e1-2a1c-3b73-8688-9c9803dae26e | -8.32594 | -46.8132 | 2026-06-11 04:29:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99d81496-c103-3e56-8fe5-b99a8c53dcfd | -10.28776 | -47.61592 | 2026-06-11 04:29:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d9817230-01d1-3e75-8389-48300200e65d | -7.92665 | -48.2666 | 2026-06-11 04:29:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37226274-1525-3197-9aa7-ab137a692c13 | -9.21572 | -48.57993 | 2026-06-11 04:29:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6a63cec1-33d2-3d3d-bf88-1224ee18e1dc | -7.34241 | -49.8473 | 2026-06-11 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2b2372a5-564c-3ba4-8250-2ec3a95f6585 | -9.62783 | -49.02418 | 2026-06-11 04:29:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db9e6fab-3348-3dc7-ae46-23c78f59badc | -10.38004 | -46.62307 | 2026-06-11 04:29:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65912bf9-a302-38b7-a3ce-787a8e6f2d5d | -9.31509 | -45.47863 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4e4e1f39-d000-387a-9884-0c5ad7dbf4f6 | -9.74919 | -47.88158 | 2026-06-11 04:29:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbb7799a-c03d-3106-9259-9b89793a1993 | -9.31227 | -45.47448 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 76abc389-f2dc-3a2a-b003-097b6ef870e4 | -7.87918 | -47.10122 | 2026-06-11 04:29:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cc71e5c-e36b-3d39-b62b-2f3bd224f05f | -9.32803 | -45.48436 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b72a814-9340-3854-97be-4aabe8d2cf40 | -9.31117 | -48.9646 | 2026-06-11 04:29:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e86435f6-2757-3a53-9cb8-4aa7707357b2 | -8.98775 | -48.08947 | 2026-06-11 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c7f770b-bac7-3333-aa77-ba34c6681fbd | -9.13859 | -47.97874 | 2026-06-11 04:29:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e25647a-f081-3878-83c2-59d758eba32a | -10.93091 | -44.66685 | 2026-06-11 04:29:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24990ff4-693b-3b74-be38-cb09a4ee0a53 | -9.33141 | -45.48488 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb439099-fdef-33b2-9eff-ac043a084269 | -9.3224 | -45.47604 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f3141312-0087-3fb0-bc63-e67ff6a8d1dd | -9.32184 | -45.47968 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e6c75ef5-d8eb-3eee-acb0-7d250dce3625 | -9.31791 | -45.48279 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2181665e-ea7a-38e0-be0e-db447d94728e | -9.08989 | -47.81777 | 2026-06-11 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63ff000d-5c8b-3289-bab8-b30d295bcacc | -7.24373 | -49.53949 | 2026-06-11 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1474a0b6-a924-395c-96c1-4fb90e594537 | -7.60042 | -46.45924 | 2026-06-11 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21716125-ae56-3975-903e-e2cdf0020bc6 | -7.99371 | -46.05517 | 2026-06-11 04:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40f770f5-2b4f-3587-9ea9-3f132ad08690 | -10.28501 | -47.61188 | 2026-06-11 04:29:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8f0cdf8-5a48-3339-898d-e2117b8a7a0e | -9.11081 | -47.95968 | 2026-06-11 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ffb6557-af0b-3aa6-b7c4-0dfd0ee6d17c | -9.32522 | -45.4802 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ab8e326f-403a-312c-8eea-58b5da50d4a4 | -7.34605 | -49.8479 | 2026-06-11 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1584d403-f941-3cf6-97f2-17edc8b1a792 | -7.59656 | -46.46218 | 2026-06-11 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0f7ceb8-e9a8-34e5-9a1b-1c6f3227580c | -7.92606 | -48.27026 | 2026-06-11 04:29:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03dc3d98-3bb4-3d8d-b798-6cec5eb4b4ae | -8.32031 | -43.81478 | 2026-06-11 04:29:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a3bb44cb-ed1f-3f5b-a138-8fa159ae181d | -8.31892 | -48.00753 | 2026-06-11 04:29:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0ec2019f-33ff-3a72-ac1d-660390b34d4a | -8.51434 | -47.0175 | 2026-06-11 04:29:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9458c6ea-13fd-35d5-9b73-563076c3eb44 | -7.47607 | -49.60559 | 2026-06-11 04:29:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea192124-83ee-3d1e-a370-3eb28168d161 | -9.30946 | -45.47032 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f67199a-2a74-33c8-9dcf-966a953c4df5 | -7.35039 | -49.84423 | 2026-06-11 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2e6646b-65f9-33c9-8205-b333bee075ed | -8.31675 | -43.81424 | 2026-06-11 04:29:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dabc73d4-074a-3d37-9a9d-6f29a5cdee59 | -9.34013 | -50.8833 | 2026-06-11 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 031ca6aa-cd65-3a80-b2f4-d8caeadfc19e | -7.72131 | -44.16016 | 2026-06-11 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d1722bc-8c00-3bd7-9450-fdffccfdde40 | -9.12367 | -48.52017 | 2026-06-11 04:29:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0865572-f3cf-385e-a80f-29c59a26ef7b | -7.62549 | -50.039 | 2026-06-11 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2e57792-1254-33b6-8d95-0accbeafc7c8 | -10.28832 | -47.61242 | 2026-06-11 04:29:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf25b8b1-3ea4-3004-a8d0-0ccfa4d62168 | -7.7248 | -44.16068 | 2026-06-11 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d51ad11a-4083-3995-b0c2-02d00cbd1c08 | -10.93443 | -44.66738 | 2026-06-11 04:29:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e717f4a2-76fb-3f5e-a68b-8c135b4ad466 | -9.14135 | -47.98285 | 2026-06-11 04:29:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d76168f7-e589-3502-9964-664e78b9aefc | -9.21233 | -48.57938 | 2026-06-11 04:29:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 56e77049-e8ea-353d-8646-c1c60edafb54 | -9.2197 | -48.57681 | 2026-06-11 04:29:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7036564-b3f7-323e-8142-04a5441d4b3d | -9.3234 | -45.4787 | 2026-06-11 04:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| ee476455-19b1-3ceb-b166-2ba085a308f1 | -11.97886 | -47.38397 | 2026-06-11 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3ac2096-7c29-384f-987c-38a6c5c51a72 | -13.53222 | -47.80732 | 2026-06-11 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6d5eb79-e132-3d22-b897-fe1eb7c10b7d | -14.6477 | -48.01242 | 2026-06-11 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3af3599c-db35-323f-9443-d0db2233362c | -12.85918 | -44.36656 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0370d875-792f-383e-a714-fc860ce2a5e5 | -12.15007 | -48.44301 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd914ec1-5706-3e4c-b737-f142aa505e9a | -12.04763 | -45.29541 | 2026-06-11 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bc38ef7-6ed9-350e-a712-0c19ea09bf6b | -17.69902 | -45.51969 | 2026-06-11 04:32:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3465848-28f3-39da-a22f-2013a1d1b7e4 | -10.42917 | -49.44273 | 2026-06-11 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8644aaa9-3928-322a-bf13-a2e7a70c1d79 | -13.5427 | -47.80542 | 2026-06-11 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a4fc359-e779-3c0d-b12c-e2caec803be3 | -12.02867 | -47.79953 | 2026-06-11 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b33c5dd7-abc0-3452-b1f3-10e3dbada8d3 | -14.9987 | -39.71207 | 2026-06-11 04:32:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20cdceeb-d210-339c-a2a3-df776b4de303 | -12.85126 | -44.3698 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85d6b337-915c-3499-9cdb-ce158d353c0e | -13.54545 | -47.8095 | 2026-06-11 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9f55d02-2bc3-3f8f-aaf5-afa539fd72ab | -11.87078 | -47.09959 | 2026-06-11 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e8e35b5-2cd0-3109-8625-131c3e51c709 | -10.90348 | -49.35574 | 2026-06-11 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a57aab3-8afe-31a1-a90c-1cdf562b7377 | -12.14893 | -48.45013 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a832cd2-1ab8-308a-a705-2194bb7214bc | -11.87354 | -47.10365 | 2026-06-11 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README8.md)
