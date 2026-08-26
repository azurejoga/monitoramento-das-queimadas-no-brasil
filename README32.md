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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b73f6bf0-212a-3203-9476-ab4518e1f0cc | -9.38448 | -48.21476 | 2026-08-26 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a81eebd9-7aa5-37d7-a76d-5f9b35fe1d94 | -7.02223 | -59.22983 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c4c6d931-3378-3468-bd2d-7c5980d16dd3 | -7.11302 | -56.55596 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89921c0f-97a5-3fee-a7cc-6b47e7500657 | -9.41195 | -51.643 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac2f84c0-3ce1-308d-bf03-d222b81aa94d | -6.75965 | -59.4487 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ac06dea-febc-31bd-9dd2-3c335736202b | -5.98082 | -55.71453 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ffa5b8d-6d3c-37a9-a3dd-bafcea546d41 | -8.6242 | -54.742 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a52034e9-7ff9-3402-84be-d64caae10c82 | -7.50012 | -55.35681 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26e46b74-f421-3401-82e7-d829a1610f98 | -2.98552 | -49.27373 | 2026-08-26 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67485bb2-af0f-3a78-b95e-72883aef46e8 | -7.01784 | -59.22912 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f2787390-ea44-3bb9-97c7-63a858367f58 | -6.83202 | -59.9397 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68985a38-e446-3a5b-8e53-b3abc063995d | -3.12405 | -61.19225 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08e4d11a-1954-381b-8f77-7d95e95dc19e | -8.62207 | -54.71188 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12849f2d-5d8b-34b4-ad95-bd5dbf290fc6 | -3.62589 | -49.70187 | 2026-08-26 04:51:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68734e4a-0fbd-3a64-946a-f24ef09fee99 | -8.53231 | -54.83929 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cac99b2-97fa-3f0a-af62-ced5aa5689be | -5.79121 | -57.611 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72a1d869-5a79-3303-ae2c-c536a08235f3 | -10.33488 | -48.22029 | 2026-08-26 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70048bb4-f0f3-376b-abd0-f7317a7f3393 | -7.12256 | -42.78826 | 2026-08-26 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 54dac969-6360-300e-8d7d-d4310fee4cf8 | -7.52301 | -61.37904 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 63793ba0-e1fc-3727-a731-13e51f0f3415 | -6.32308 | -44.84305 | 2026-08-26 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7d566b3-a0a6-3be4-893a-f788cd892646 | -8.63655 | -54.75142 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29c5b74a-3778-3e84-8e99-37058815c787 | -6.26779 | -53.35898 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a21ea687-91fa-3640-89ce-c78abb4b529a | -7.54234 | -61.35811 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fdcf2b3-2015-382c-85f6-b27e69da1d35 | -9.4443 | -51.68213 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 890ceb03-4a1d-398e-bad5-daf079567172 | -7.03214 | -59.22558 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fec4fa9b-7560-3ccf-b0c0-e00b568bb895 | -7.27714 | -44.07917 | 2026-08-26 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc144d02-829f-35d6-9db7-76ea5bc2253b | -6.74044 | -59.64654 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ded0c56e-440f-3d02-a13d-bed9c0b5a79d | -6.62443 | -58.49175 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8ed409ee-ffaa-3bda-9444-811b4cbec8a8 | -6.14562 | -57.9412 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae117283-f3ae-352c-abab-3dc38313e708 | -8.64526 | -54.74949 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1b35ff2-2867-3671-be0e-d3ab21c5dd73 | -3.77966 | -59.27671 | 2026-08-26 04:51:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89082482-b471-3bf4-be7c-cdacdcc93b1f | -7.28667 | -43.026 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 89f5a639-2577-30cb-a8ae-12288f8ebb46 | -8.02284 | -51.79458 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f734fc5-a2be-348c-90a8-4f420da6d8ed | -8.54511 | -54.78149 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10f57abc-9986-3af0-832a-2cd4e912a269 | -6.77353 | -59.43685 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| edf2a1a3-799a-3f3e-80c0-d259d5600397 | -6.12277 | -57.82634 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dc458055-3e3a-3e53-b2ba-ca6b45fc6176 | -6.72904 | -59.14473 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ea86ce0-3e9f-3549-aeb9-b3a02967c4a5 | -8.08731 | -45.90528 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2e6c687d-2bbe-3481-80b0-e8106b8084f7 | -5.98441 | -55.71512 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74e0bbbe-96a3-3c0a-ad3a-e5a995af7907 | -7.75564 | -44.7529 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33db1695-7179-3597-a243-9b29609d5e3a | -6.77604 | -59.43314 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 96d6d137-0928-338e-8055-d4b9b8129fda | -6.076 | -55.54784 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 296fa6b5-22a6-356f-ba72-43a88510646c | -8.61928 | -54.70771 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 998448a6-e0ce-36df-b22e-2948ee6b34fa | -8.02011 | -51.81259 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3de83edc-c89b-33a5-bd70-72556a5d872f | -3.54088 | -48.17975 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8301afad-33b7-3127-aa21-3938331964b2 | -6.61956 | -58.49496 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57430b2f-1040-3450-840b-ae366276fa43 | -6.15061 | -59.92337 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bbed1feb-e593-31e3-be64-d6a0a97be31c | -6.95198 | -59.08796 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b32f5836-7f7c-3acb-a26b-6cf70909879f | -7.52595 | -61.39155 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 59bd4b70-7aa0-32ea-8c02-183ee51d8a2d | -8.01419 | -51.81493 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ef4349c-a510-3d6f-9f84-d19d4d212f89 | -8.01794 | -51.82698 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 282e914b-c2c9-37bd-88f1-317c3697fa53 | -7.55752 | -61.41846 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cda9847-2d41-39c5-b7cb-c933f4e89105 | -8.54173 | -54.78094 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 882837c0-8761-3aca-a8df-29a1174c680c | -8.27218 | -55.53764 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dcf3f75-a05d-3534-bc33-db92c7ecdb32 | -8.64584 | -54.74586 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67e125e9-bc31-3ebd-8cdd-f0e61b6db604 | -6.62309 | -58.49955 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 227ca4fa-7b78-39f0-887b-09100db7adaa | -9.03758 | -50.78979 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c6a17f0b-d7f0-3e40-bc64-e1aedd5e8d77 | -9.41473 | -51.62455 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba2f527e-03e9-3282-af8b-b6baae9d07f9 | -7.06722 | -59.23148 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9ad631bd-781f-34db-97da-fa3e4ff3fb95 | -10.58426 | -46.31115 | 2026-08-26 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb6614cc-bc41-3da6-b6f4-5a5c2644094d | -6.98569 | -59.25903 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e1be7c4-4232-33a2-8273-5d1e8c5fe290 | -8.57354 | -54.84213 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5db19ae-15b2-36b1-ab6b-561e2e6acf8f | -6.72967 | -59.14322 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9301da44-7071-3030-868c-3fca68868435 | -9.04049 | -50.79437 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 52afd2f3-73e2-3a45-a0d9-28ed2f876e45 | -6.99159 | -59.27775 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97869d47-692f-3b02-a7a1-d162b3e8aeb3 | -7.39379 | -55.16632 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a7bfdc9-eac7-3cb1-826a-03d57b69a8ad | -7.30599 | -42.96781 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2a09d042-a952-352f-ad5a-5e16a68bf533 | -8.17517 | -54.95928 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c748f5d9-7d2b-3bfa-b0e2-af996c75ed88 | -3.13055 | -61.18633 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb3f539a-2fcf-3f9f-9c21-e2818f5b1dff | -7.51373 | -61.37745 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| dce75585-7b3c-3814-a6ec-7782ebf84865 | -8.13339 | -47.50675 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b27a88b0-93e2-3d56-9930-13c97cc189b7 | -3.13647 | -61.18385 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d11aab1f-ae49-3e9d-af8d-a8962d5867dd | -7.02081 | -59.23835 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 151c84a4-6ec5-3f28-ba56-8a29ea521b95 | -8.52632 | -55.31086 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af47ff76-f0ae-3c68-b16d-32f3e3435d77 | -7.37689 | -55.18299 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a560e91-158a-35e7-86ab-f9f77766c973 | -6.65255 | -58.50428 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 09b24d0f-49ce-38e6-91c9-3e76fbf5e6b4 | -6.65125 | -58.512 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a0b0a927-6121-3a5a-b7c8-3249fdb8ac46 | -10.37973 | -45.06597 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 907d6dff-e598-35d0-b8f1-94f477a67911 | -6.30124 | -53.57898 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61e8f617-4c32-3b26-85dd-0e8f4de2c05b | -7.52179 | -61.39089 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0875e188-487d-3b43-85b0-01f6af194466 | -9.03707 | -50.78678 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0164c762-98b8-32f1-be2f-805588d812af | -7.30852 | -42.99143 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 081f6310-437f-3538-ab94-de8df9e129c7 | -6.27775 | -53.36053 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbd94f84-4d64-3909-8f15-1ecff8c8d61e | -8.01084 | -51.81439 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a9c79a9-7fd7-3b9d-87ca-9edda38c9b0d | -6.77903 | -59.44278 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b0845ad5-0e7a-38f0-bf61-2cc22a20f3fa | -9.02654 | -50.78533 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ba86cc0-731f-3dac-ae25-d81bd3ce289d | -2.83153 | -48.65362 | 2026-08-26 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 339f5eb4-adf1-3f25-b873-7e1b25723e02 | -6.13714 | -57.86546 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c24a32a4-bf4e-3774-8935-6050308b6bcd | -6.51286 | -55.22622 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92d1318b-8ecf-3de0-99ab-d769dde14424 | -5.97657 | -55.71812 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73a04e3b-1751-3c3c-b4df-fb780fbcb179 | -7.38258 | -55.15355 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 983753ce-e4fc-3d34-9292-363bc2ec6a09 | -8.10456 | -47.46083 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b445b72f-4c18-304f-8da3-6689af0a0781 | -8.62438 | -54.69737 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66d78592-fc20-3fb1-86ee-02294a8d88b2 | -5.86552 | -50.14235 | 2026-08-26 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27a45fc3-1a33-34ca-b5bd-02aa1eb20c5c | -3.6605 | -48.96119 | 2026-08-26 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c138acc-84e9-3728-8de0-8f853c8cfb78 | -7.5233 | -61.38213 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 27e62d2a-4049-378f-832e-261781a2179b | -2.79924 | -49.58468 | 2026-08-26 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c6ee195c-c769-38c2-b234-83aeb875e0f5 | -5.9573 | -53.58181 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f14d3400-da5c-3299-8fba-7862e756ae09 | -6.27388 | -53.3635 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3879f90-5537-3fa4-85bc-8c752de41f1a | -8.53463 | -55.34711 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README33.md)
