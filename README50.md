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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72cc2d1c-cae5-35a2-b8a0-8f19ce95df08 | -12.72487 | -48.02867 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf8c86b7-9a1f-3fc5-a821-91cb2a7edb89 | -13.06121 | -50.08025 | 2025-09-17 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 334b3d59-9463-3f23-9569-e9224d887a97 | -12.3877 | -51.40606 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d37a3aca-1848-30ca-aedd-f9fdaa07516c | -13.2001 | -47.31995 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62782ef9-1379-309f-9805-a977689b38eb | -14.80851 | -48.11805 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41b8dd23-d5a6-3cbf-88e8-2f51245a274a | -14.61502 | -46.37083 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9844e8d1-ffe1-3d4a-b46d-4476b2c679c9 | -17.3141 | -46.81543 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36d106fb-ef5a-3f96-8c98-e940311f1c49 | -13.21154 | -47.31406 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d62a01c-2556-37db-a071-73f2ccc98adc | -16.61627 | -43.37059 | 2025-09-17 04:34:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8a3d59d-7a2c-3bdf-912a-a76cf8b71da9 | -14.83786 | -51.69858 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a137c3f3-1cbe-3d67-90bd-c88ece915409 | -14.90236 | -51.68966 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f49fafb-ab21-34c0-8b9f-76e51aabcc24 | -12.70579 | -47.97353 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 77022ac1-9d71-3d16-b068-7e53e8568970 | -14.47497 | -46.35691 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9173043-2a98-3f22-a531-aa8bd3ea815e | -15.42775 | -46.15718 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7b1cbcaf-3989-3262-ad86-f71ccbc7f3e2 | -12.38298 | -51.41316 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fbc97b7-64a5-30d7-bcf4-5b72408a943a | -15.99001 | -46.44946 | 2025-09-17 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7c3fe92-8b52-39d5-8226-b2557a156140 | -14.86264 | -50.05442 | 2025-09-17 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9e24e78-e664-3f0d-964f-3a7c5560a52e | -17.72101 | -43.56598 | 2025-09-17 04:34:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1a9c496-4ef3-3d20-ae62-b96ae98fc775 | -17.95858 | -45.25064 | 2025-09-17 04:34:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 829fd035-76f4-3e21-a5f5-a4bfe53fbced | -16.6956 | -54.96838 | 2025-09-17 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7eda47d8-d77a-3df7-882c-f5f81c86863d | -14.59568 | -46.37638 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1637a69f-51f0-3de0-ac83-776682e8c12f | -18.37343 | -43.32803 | 2025-09-17 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 915e8460-69b0-34b7-b3ee-97bef6220c70 | -14.55494 | -47.35924 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8fa22e0a-5105-3719-be61-45cd4a5a8152 | -14.90855 | -51.69467 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 56862756-6cf3-3d98-8521-dbca62091210 | -14.50444 | -47.36433 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5540074d-56aa-34ed-93ca-24cb387a69e7 | -15.40781 | -47.33216 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74f41b56-5662-311b-86b2-e87543fbb95a | -18.16068 | -45.22454 | 2025-09-17 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a33d3ed3-50b4-34cb-a993-634efe1ba94b | -12.71365 | -47.98967 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 404f8b89-cfca-3056-b9e1-d2aa1af08f76 | -15.41661 | -46.15549 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3061b242-2f49-36ef-bf5e-beac61266903 | -12.6935 | -45.80554 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61f8366c-48e9-3278-b2e2-1404382c4e85 | -13.22867 | -47.29372 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14a8eb22-eec1-319f-a1b3-ce8ddcb2b127 | -12.85863 | -47.12887 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 054c8ad7-ea3c-3dc2-9641-2a2c003ed727 | -13.14597 | -51.6105 | 2025-09-17 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb97f8d2-e94a-35da-a78b-9ec93dc2b101 | -16.8526 | -44.05123 | 2025-09-17 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1f2c8bd-cd96-304d-9c33-20ad79f81c4a | -11.07187 | -49.75261 | 2025-09-17 04:34:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a43310c-0553-30f9-ad9b-76d95d6ce096 | -14.6005 | -46.39489 | 2025-09-17 04:34:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c18ea3a0-4e93-34ec-813e-85753fe62c6e | -17.33189 | -46.79557 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 410fb6c2-6d7c-3424-ba4f-7f5d787d5d8f | -14.39807 | -43.53302 | 2025-09-17 04:34:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e566de27-2d39-3a48-a683-994ca3d4b6ef | -14.28714 | -47.41634 | 2025-09-17 04:34:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3edb4bee-e03b-3d2b-b1f6-1ee2b1f3699d | -12.31327 | -50.12478 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6e206b6-a356-3e35-8476-18383ee62128 | -15.39537 | -46.13077 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 284961ff-9d66-349d-bec2-d87944870a8f | -12.72766 | -48.01051 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 46e4d479-2fd0-3849-96c1-99ab808fdd73 | -13.22586 | -49.45298 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bfce0ce-eadb-3166-883d-e086ec08fc34 | -14.90704 | -51.68265 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a73ce4b-dc4e-3500-aaa0-13d0b0d5b577 | -14.90729 | -51.70228 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a9d3ad0-50d1-364d-b2e1-c3039eb05ada | -14.60377 | -49.36879 | 2025-09-17 04:34:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 079dabf8-2d8a-33ff-a2d9-e457f82c662c | -17.1963 | -45.90924 | 2025-09-17 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e64f9849-6ad6-3086-af7d-38b9bbb2742b | -12.72206 | -48.00217 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 9898b8bd-41ef-3e2b-9e4d-04e46f12d633 | -12.44465 | -44.74639 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42d64580-f896-39f3-83d5-071e369b1796 | -16.85453 | -44.05415 | 2025-09-17 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8f4ce88-4e97-30a9-839f-b6245b0c8be6 | -16.61817 | -43.37362 | 2025-09-17 04:34:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2ae5672-da69-3d95-b349-ceb9fbada5f8 | -12.84472 | -47.19754 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bed6ca5-56b7-388e-ba35-36672590bca8 | -15.41915 | -46.13725 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e25cc1d-3217-3fde-a15f-94c946805377 | -12.6994 | -47.76618 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0b79d98-ba75-312f-9d25-c4baada72ac2 | -14.91323 | -51.68766 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59ec3936-06c0-37f7-8300-08d1fa1038fe | -14.5521 | -47.35448 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 603866a4-ef9a-38b8-9422-406834739698 | -14.89831 | -51.69286 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb9f7612-924a-3d3e-8f70-5fde623049c5 | -12.69779 | -45.80174 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c282a74-2e35-38fe-b1e3-9b386ac6d238 | -15.39686 | -46.13377 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b898c416-8d4b-3657-8f52-73352a1eaafa | -12.10389 | -44.83376 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34cacd3e-41ad-3dec-931b-5769c4dd2940 | -14.8074 | -48.12548 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4380ddef-0888-3d4e-b034-717a008cdce7 | -12.3637 | -43.20443 | 2025-09-17 04:34:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91e2dada-7800-3499-b228-2c08866a630b | -15.42403 | -46.15661 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be80b275-1ace-39cc-b8ac-fdea1cc56861 | -14.60708 | -49.36934 | 2025-09-17 04:34:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa39a006-9c05-304d-8f73-07a2ca78142b | -12.0654 | -46.56591 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9da06d08-9b57-3617-870b-789673d32ba1 | -12.64445 | -44.85964 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b0d37b1-1dfa-3475-bc78-569bfa23815c | -18.61688 | -48.1963 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a760c689-4277-3159-9d33-c1a43a4364c2 | -17.32936 | -46.81349 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17bc8047-cc67-3c26-88e1-a510afdbdd0d | -14.83319 | -51.7056 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2131afe4-cd64-38e7-851d-f2842c221532 | -12.69962 | -47.96883 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 563237b0-189a-3318-b7ae-6d6be6dee682 | -14.61922 | -46.3937 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24dccdf2-6128-3342-b93f-2f7ed857063d | -12.42655 | -40.92825 | 2025-09-17 04:34:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3c2c6b87-3c09-30fb-9a64-0483f0363917 | -10.81193 | -50.66045 | 2025-09-17 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 49f96e97-53bb-3733-bdbb-d27d049d7a08 | -14.90387 | -51.70168 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fdf40bc-f9f6-3353-b634-b32228190426 | -12.29601 | -50.12558 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65c4bf57-dd55-322e-9d59-b46fdefff036 | -18.55299 | -49.24778 | 2025-09-17 04:34:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f68dda6f-dcb7-38c7-9f1b-7f8e132185aa | -14.97869 | -53.40295 | 2025-09-17 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc8a74af-8442-3c13-a3af-fcfb39383e99 | -15.41849 | -46.14193 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4af5ae56-e55a-3225-b22b-680d68039e3f | -15.43148 | -46.15762 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6a3c94d4-dd5b-3a3c-8b04-1665b593e337 | -12.97705 | -47.94539 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f06991ca-030c-3cf6-ae01-273f24481e97 | -15.71797 | -39.32067 | 2025-09-17 04:34:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 51cf8e6f-5e56-3fec-888b-112aa9aae128 | -16.61762 | -43.3782 | 2025-09-17 04:34:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8f2f0c6-36fe-3231-83df-2ff00f7cae28 | -14.20338 | -47.00638 | 2025-09-17 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6452d8af-735d-3e0a-b207-7a501c78fa5e | -18.54472 | -48.14376 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7449e095-355d-33a2-9f54-c500ec473b04 | -14.89426 | -51.69607 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d2d9deb-d705-3224-860b-549159d1de0e | -13.70609 | -50.81701 | 2025-09-17 04:34:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ab82254-c9f5-3a82-812a-a2e1e4f09f22 | -12.71926 | -47.99801 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02fb7738-1e1f-36f1-8dba-e3fbf881d337 | -11.17752 | -50.65503 | 2025-09-17 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a00fb609-ba78-3f5c-afb0-39b770e517fe | -11.59778 | -49.82077 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0dae5f1-cd00-3b44-bf3f-56a38582cf41 | -12.24646 | -46.75638 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c96ef3c-e763-3bca-b89b-1b840c22bdb0 | -14.84247 | -48.35162 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfe35630-a8ea-36e8-9481-af9e22e218ff | -15.97636 | -46.44542 | 2025-09-17 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 91d2500d-1399-39fb-b5ee-268ee77b4831 | -13.66078 | -44.39801 | 2025-09-17 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f44d552a-be9c-3aef-95b6-36c7621be223 | -12.06312 | -46.53313 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63801c05-0488-343d-9888-aaa72010a960 | -14.91665 | -51.68826 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20c77bf6-545a-3a72-a542-300cfe281e25 | -19.53118 | -50.59219 | 2025-09-17 04:36:00 | NOAA-20 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| ef9ce1cb-563b-3e33-b250-2407d7f36187 | -23.80655 | -50.97717 | 2025-09-17 04:36:00 | NOAA-20 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 50967a75-1bfc-3d78-83db-b70ac1232a02 | -22.66851 | -53.12289 | 2025-09-17 04:36:00 | NOAA-20 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 96d83a71-e1bb-3411-83a4-110e73fb5556 | -21.60278 | -50.32723 | 2025-09-17 04:36:00 | NOAA-20 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 7f635058-5bc4-3c8d-832d-1ffb7d20c53c | -21.60669 | -50.32402 | 2025-09-17 04:36:00 | NOAA-20 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README51.md)
