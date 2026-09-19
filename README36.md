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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94d5784a-c169-3b2e-b590-a6cd8ad98a53 | -13.73535 | -48.79137 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aaed41ee-6ed5-31d2-98c5-ef40e50b895a | -13.74262 | -48.78473 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23c460b2-4358-31a8-9663-5eaf067a7beb | -11.96947 | -45.78117 | 2026-09-19 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11bf97ea-f7a6-3cdf-b71b-52eb67d86dcf | -11.33684 | -47.3544 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f915789c-f734-3d92-aeb0-693f793fd65a | -10.83664 | -50.90027 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2bdb03a-d3e4-33b3-a41f-1f4e968ed1e9 | -14.15822 | -45.17221 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 901a6d12-697a-3dac-96e5-7d0cd1bb48a9 | -14.79971 | -48.54932 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90922fac-32f3-3ea6-b9a8-694fd562d982 | -11.00297 | -48.32677 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4895e96-299c-3b79-95f3-9736789f5f89 | -10.88332 | -54.07239 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba25c779-375d-3c19-9eeb-c3cb69c94813 | -10.92581 | -53.96534 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cbaa9a1-bfbf-3076-aa15-b806e2212bd0 | -10.36375 | -48.89625 | 2026-09-19 04:04:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b97ed0a-6530-31e6-8d32-22124e76fe7f | -12.86213 | -46.33907 | 2026-09-19 04:04:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a159b3b3-ed04-38ac-803e-8aa7ecce3313 | -11.08219 | -48.27877 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3b7599dc-493a-3f09-88f2-d227b405ce41 | -11.32931 | -47.67714 | 2026-09-19 04:04:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97fb5a9f-fa74-3c40-9c84-26da003f3e4c | -14.12972 | -45.55399 | 2026-09-19 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e3e103a-fc2b-36d6-a00a-44062077430e | -10.86279 | -54.10508 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce9c5879-45c2-3f65-8498-6fc24cac3dae | -11.04857 | -48.30766 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3bd0ff31-900a-3ae9-9ab1-d0abe1cf22f0 | -10.9235 | -53.9767 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 326ebc80-fe03-3a21-9028-75e30406c06a | -13.0122 | -46.94909 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cea35568-028d-3d00-983b-2b0d25f58da6 | -11.30338 | -46.78125 | 2026-09-19 04:04:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26734bde-0d5b-3ceb-a5bf-4cb90e25e0c1 | -14.67962 | -46.65675 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e1c3ac9-8bb5-3e5e-9be8-ef17a13379bd | -13.72952 | -48.80437 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a311bda4-f1c7-3d62-aa9a-efd581564a97 | -14.68377 | -46.67839 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f938cb6b-4863-3eb9-9ef2-a75a22b9df0f | -14.9292 | -49.92987 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd21a7b6-cf09-33f9-8831-763fb21d47a0 | -13.6285 | -48.30415 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 63863a51-0d1d-33ae-b9c6-773252e03a61 | -11.49779 | -47.72426 | 2026-09-19 04:04:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1df1b40e-e690-3006-a0d0-df56ed35c84f | -14.94257 | -49.93775 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fdc4d2d9-d939-337e-98fa-b22a06bf77ea | -13.00688 | -46.97884 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 1eabc500-83f0-34e4-b7a9-c4b18c68b5a2 | -17.24058 | -46.72149 | 2026-09-19 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2355ce23-3464-3a74-93db-bc2186cffa9e | -12.98858 | -46.94056 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f806c93-8c4a-388e-be41-0f5997c07e7f | -12.13491 | -47.00487 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 30bc5636-2992-30e0-aee2-c43d41459a88 | -11.81097 | -46.8455 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cca2395a-3eca-365a-977c-5c2340d23e7f | -10.87667 | -54.07116 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3fe00323-2657-35ca-9d5f-dc49d9bf4b8b | -12.54732 | -47.08761 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f17a8df1-f05a-3daa-97c3-030b4071e547 | -12.15744 | -46.97397 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 469740be-fd81-31f0-91a5-2731d5d3383a | -14.68766 | -46.67911 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11ffa1ec-f0d3-3e76-9f5b-d3b252c14878 | -14.69127 | -46.65889 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a1154784-8be1-3c4c-914b-baddb0fc90f5 | -12.55216 | -47.08441 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b481764-f051-3754-9b0c-24287d254570 | -13.74542 | -48.78743 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 485dd851-ce7e-3e09-a274-ac9c2d8b6ccb | -11.91315 | -50.12267 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 32cae7c9-f8d0-3368-8908-7277589d0c65 | -13.63925 | -46.93041 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f206e6fa-f52a-33b4-8b67-f4026bb386af | -10.02365 | -51.89645 | 2026-09-19 04:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9779fb1c-1f56-35dd-b9f9-6c2c6e8cc747 | -10.92465 | -53.97104 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1e352b5-06ce-3fac-b859-40e004b0466b | -12.14303 | -46.98319 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c9c99520-914b-336c-948e-f7cb6df96261 | -14.66293 | -46.65664 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a0e42bed-8c0b-311d-b77c-78fda5253413 | -13.60096 | -46.93597 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29a84f49-6866-35dc-952a-79738886753f | -14.16761 | -47.03117 | 2026-09-19 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84c1bcdc-6eef-3af2-ada8-b95a72b1210e | -12.13058 | -46.98132 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5216b282-ba40-33b6-9935-83f1faaf608b | -12.33509 | -50.72823 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 363dc622-8b65-320d-8a2a-2a5db8bf8851 | -12.99738 | -46.98497 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6b8670c9-c257-3caa-aa2c-670a20ff3682 | -11.30761 | -46.75728 | 2026-09-19 04:04:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a00cca5-41ba-3dc0-88f4-9290b8ce61e6 | -11.51748 | -46.87446 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68382412-d368-3b06-b591-3cac8baeb43b | -11.46618 | -45.713 | 2026-09-19 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d935b83-2d54-36a6-be98-95e97f6322d3 | -11.67333 | -54.44893 | 2026-09-19 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb291d08-d3a6-3c3c-9945-14c9bc01fbce | -14.15076 | -45.21524 | 2026-09-19 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c52b8d89-c474-3c29-b666-12bc9bf488fc | -14.16109 | -45.16913 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edb83cc0-7d41-3b35-bff8-0cede07d08c6 | -12.13342 | -47.01318 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 18073951-fc57-3f89-96f0-f067ed8559a7 | -10.89096 | -54.04865 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4e10d6a0-4538-3715-94f6-0fa73fd31d20 | -11.94204 | -50.13784 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f148b51-6369-3a63-b8cb-317b34bf59a5 | -12.41481 | -45.05469 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48c87e09-d47a-3018-ba49-0bff3cd4074a | -13.00969 | -46.96313 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 904cad71-8ae6-3c7e-a753-3311cf6c5572 | -11.0584 | -49.74498 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9593912-d4a0-3ac5-8c54-7345c6982795 | -12.7029 | -45.94985 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7caff074-0dd7-3857-bafa-5129689d22cc | -10.92532 | -48.41452 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e18b5cbe-6e82-3421-ab52-34e8685c457b | -11.30867 | -47.26494 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdc27f18-5e79-33bd-a483-f70298a0b83b | -11.82126 | -46.85925 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe444d9c-a07a-39d8-a0a5-d018cd1097d6 | -10.88645 | -54.07145 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 117d5138-c4a8-377b-a7a5-da7b26ec3c41 | -12.12721 | -47.00018 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc4b71e5-a2af-3dde-8c4c-48fd17f680be | -14.9524 | -49.93726 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 341ba572-7003-323d-8c23-3f1e24d5c396 | -11.04313 | -48.31153 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b3c60026-1cb2-310c-8c59-495cb93cf7cd | -14.13872 | -45.16969 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f41ead1-d543-3ab4-a5a6-38bd1ab85390 | -10.86154 | -54.11112 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0aa9634f-42ee-33d9-ad23-ce32753b4b4c | -14.68857 | -46.67406 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b26f014d-fb3a-34e6-8a1f-745c8946f1bb | -12.98793 | -46.94417 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 579fbc7a-a581-3c51-9f60-6cf16f7379f1 | -13.73968 | -48.80027 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbef268c-5d54-39cd-b630-c2b70f8f2c01 | -11.50216 | -47.7251 | 2026-09-19 04:04:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65833dab-4de6-390a-801a-fdb57f60d58c | -10.02783 | -51.90648 | 2026-09-19 04:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e2c8098-42f5-3902-9335-cca99b80c1cc | -14.66317 | -46.65896 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a7fe7add-9a76-38ac-b1f3-08bf7984ec0b | -13.88219 | -48.6075 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10d4ace3-0e52-3950-a3ae-011e4aa71b15 | -15.58007 | -56.53424 | 2026-09-19 04:04:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 855d09a4-7a6e-30b3-85e6-886722b2b241 | -11.00389 | -48.31842 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3d9b0dc0-4314-3a7c-a128-22d93bf86641 | -11.86072 | -47.59375 | 2026-09-19 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42be0408-137a-3ac1-a695-70970e62e229 | -10.93563 | -47.85506 | 2026-09-19 04:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5f02f305-755f-3000-b70a-666b6ac97269 | -11.08301 | -48.27417 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5cacde45-9771-371c-9235-55934ab34068 | -11.98085 | -44.93195 | 2026-09-19 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0529d0af-09a7-3a52-938e-40c40d97ef37 | -11.05783 | -49.74797 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05178bc7-1836-3854-9e8a-342fd7e393e7 | -11.11939 | -45.28859 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a115387a-073f-3c1d-ae72-432554a134cf | -11.30408 | -46.77728 | 2026-09-19 04:04:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9e3a31e6-691e-322b-894b-94d60c6e2fdb | -12.74021 | -47.0205 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b3d878b5-b70f-38f0-abab-4879fb7e7f79 | -12.69272 | -45.96307 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80dd2b88-74a6-32b4-b02e-44a571b3d411 | -11.33616 | -47.35825 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90f12022-3eab-3b30-b914-7ddf78ee57c3 | -12.58109 | -47.0894 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2afcd0f9-c4a7-3e1e-96bf-10a81f766688 | -11.12101 | -45.27917 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37dc5dc0-2aae-3b39-88a2-2b2a638eec1c | -14.93028 | -49.92418 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ce49d7e1-15dd-31b9-9298-1947c8a4cd54 | -12.1418 | -46.99013 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d7ae58f8-69db-317a-b53d-a3998847a62b | -12.98124 | -46.98127 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ae3eb85-0496-382d-93aa-2961b6b37abd | -14.69037 | -46.66394 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d19214a4-fffd-3fe0-a621-3416a8a28349 | -14.93065 | -49.92186 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a4304d3d-94c6-3003-9818-0d10cf44aaef | -12.41406 | -45.05919 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b89900d-d8b1-39d5-80dd-8c29ee1f5c36 | -13.59111 | -46.94476 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README37.md)
