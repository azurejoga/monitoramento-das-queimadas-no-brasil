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
| 2cb8b6e1-d524-3068-8aaa-18ba00afedb3 | -8.06887 | -52.37785 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdb13997-6680-333f-bbb8-34b88b7622b7 | -5.10729 | -56.14672 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d57504b0-4a85-3054-9fe0-953eb628fbd7 | -6.07154 | -43.30242 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d48bf8bc-d818-3f59-a52d-364d4fa08f02 | -7.20145 | -46.19286 | 2025-09-06 04:38:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94ca0bc1-8530-3ac2-b1be-a0dbd5bf5c0e | -6.0004 | -46.68412 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a2f0941-da52-31ef-aad1-63427e79a927 | -5.86608 | -46.02988 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9a1c91f-1477-321b-b85d-ea875cf83dd8 | -6.31919 | -58.18079 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b20c7a2-83fd-389e-adbd-d83eced0fbd1 | -2.65379 | -48.79885 | 2025-09-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71248789-78c8-3229-897a-46effb452227 | -6.55008 | -42.94289 | 2025-09-06 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc6872f3-cdfa-36e2-99eb-e5a8e3bca7eb | -6.39209 | -43.81615 | 2025-09-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4ab0894-da66-39cc-8f62-60e9ea275b64 | -8.02907 | -44.77692 | 2025-09-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c077d9f3-8541-3ddf-9ed9-18dfa0b6efbf | -6.50727 | -42.4192 | 2025-09-06 04:38:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c51263a8-9f76-35d7-91ef-ad87384fb891 | -6.20266 | -43.5778 | 2025-09-06 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d417535-4962-35be-b2db-15f86ca24333 | -5.92926 | -43.01985 | 2025-09-06 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6ffe3d56-5e04-30cd-a782-7a05a243010a | -5.95816 | -44.74173 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7603503-6bd1-3751-8910-0eb47191c74b | -2.56162 | -47.70188 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12f86410-a94b-3710-8304-c1ab00c4cb70 | -15.57619 | -52.88415 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4a8b5c1-6bcd-38ff-a2ee-3951dfbe4aff | -9.70422 | -49.48604 | 2025-09-06 04:40:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 406d49fc-de84-30bf-9f22-1d8bc46a7fac | -12.98819 | -54.79045 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93a8f74f-7914-38b7-ad01-9481deb6c923 | -9.79186 | -48.33853 | 2025-09-06 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a94a0d1c-7ab4-3b39-9aca-e52fb9d0cb33 | -12.95608 | -54.7986 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c406bea-f964-35b0-b3a9-be56e112f5a3 | -13.04495 | -56.86443 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66eca37e-9b81-33c6-99a9-b4ec1f184433 | -13.35702 | -46.83712 | 2025-09-06 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6080e933-fd8e-3505-b90f-cd69302347f1 | -15.84816 | -52.27993 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f86f28d7-4a9b-31aa-b0f1-768b44bb9722 | -12.6875 | -44.96974 | 2025-09-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbd23c98-3d1e-353c-bad7-9e88195498c9 | -14.80515 | -48.12329 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 474ec968-cae2-3266-8f4a-fb99cca44c53 | -12.97015 | -54.80587 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 703191b7-5f43-38d2-8325-9aa2313ec872 | -12.96496 | -54.78374 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 418ceb7b-2f6a-31d2-a6a9-d9da657db25a | -12.95661 | -54.81041 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6a5a176-27f1-3cce-82da-82d2015130da | -11.09471 | -52.00331 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aea02cd8-6c1d-327a-ab3d-c0da03479506 | -12.94979 | -46.56395 | 2025-09-06 04:40:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d02c01e-a6e4-3b40-ba34-df662bfc2799 | -17.86897 | -44.32121 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7439c36c-7c14-3432-8473-270cd831dc92 | -10.23748 | -50.5469 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 585d0f09-ee88-35c9-85b8-6737d36fd091 | -14.58197 | -48.01087 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35b8cb32-75e1-3646-a620-d7116ca19eff | -15.87033 | -48.9707 | 2025-09-06 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19026135-6005-398d-98c7-bef1cff49922 | -14.57012 | -48.09198 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd74164b-b7ea-39e3-af21-c29365854990 | -10.16255 | -46.2404 | 2025-09-06 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0266444e-1092-333a-bde2-3a6a95f1cf2c | -12.6322 | -56.98325 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e138ec71-67a5-3e28-b32b-065c1abda988 | -9.48868 | -54.42514 | 2025-09-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 057d8c08-46fd-318c-89a1-34f3effad863 | -10.44374 | -53.61243 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 702ad342-6e8d-3f06-835f-b2c6cb6c82ec | -9.68566 | -51.10973 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbadabdc-c3d4-344e-a452-9b02e9ea3954 | -11.54525 | -47.31606 | 2025-09-06 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ccc9684-1d0f-3a82-bde6-45710d1ab77f | -13.88526 | -48.03202 | 2025-09-06 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8673b02-381e-3b52-a482-2ff1941ddc4d | -15.72419 | -53.57766 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb763efd-c5e8-315d-925f-dc2ddb1816e3 | -10.96918 | -46.82155 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b2b30fc-8145-3fab-ae5c-758a0112d54f | -10.15566 | -46.2345 | 2025-09-06 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48737f6e-2133-3d76-9905-88a855e07801 | -16.6411 | -51.86462 | 2025-09-06 04:40:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ff525e3-e4ea-370e-a6a1-4336c989eb74 | -9.55849 | -53.58827 | 2025-09-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 117643cb-3c6a-394e-ab27-1dafc4226ac3 | -15.57806 | -52.91473 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 073ecad7-dd42-35bf-ae9f-a7a22885ae06 | -12.53776 | -49.10622 | 2025-09-06 04:40:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 642afec0-e1a8-3332-95bc-eff5e6b33d03 | -11.17327 | -50.01494 | 2025-09-06 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f79fc8fa-2e21-3775-b40d-93fc85362e13 | -11.75475 | -47.74601 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 475260e6-4cf1-30cc-a143-eb3f16d3f269 | -15.58416 | -52.91967 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 289bab8e-de7b-3c69-b7a2-303f994793b9 | -14.57662 | -49.1278 | 2025-09-06 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa6524de-fb59-337d-bda6-933debd0d77a | -12.96111 | -54.80649 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4cc2e4cf-e91a-3830-83c1-66c7348a697d | -10.08884 | -48.08837 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 632e47b2-8725-3cdc-9d11-a127d8adc100 | -13.56304 | -48.11628 | 2025-09-06 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbc72a0f-c10f-3b5f-b425-51e8217c18a7 | -10.22314 | -50.53025 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08653ab8-1230-3abd-bfae-9f40f2db023f | -9.97441 | -51.66327 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b2034983-8818-3e3b-b528-0ae2490f8010 | -10.47341 | -53.63478 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5f90f7d-a6bc-36e0-b4ba-ab21739a0398 | -11.59877 | -52.18389 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4aa7ac0b-23db-3e87-bb72-79758705fc25 | -11.62163 | -52.2142 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a435499b-11f8-38d3-9e3e-50c54f142634 | -12.9744 | -54.82552 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23f23bd7-5041-3690-bba7-d4fab26cdfd2 | -12.2734 | -53.90572 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ef265fa-0564-3039-874b-fe0139048008 | -14.79542 | -48.11359 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f36a66d-feb6-374a-863c-4becbe9a4403 | -12.51145 | -53.85063 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef0c3718-215d-3754-a225-43c28b8c5926 | -12.96644 | -54.80517 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42515f45-b6e3-3783-96a1-a042eeba5786 | -17.75858 | -42.51498 | 2025-09-06 04:40:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5b02af16-63ef-39cd-b187-aeffd2460c3f | -13.01755 | -54.84257 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60426192-1517-3f84-b9a1-451a262f4852 | -11.62222 | -52.21051 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 35943735-ebf2-381e-9345-cdf278b41db5 | -9.74471 | -51.0612 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42ba0144-c9f6-3a1c-be04-30986fb641c6 | -16.84636 | -52.11275 | 2025-09-06 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc1ea9b7-1ac3-3d26-afb6-01f673eaa2ae | -10.23362 | -50.54987 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 882cb447-ddd3-3294-b71f-6cb2f36b9983 | -12.95688 | -54.79403 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48cf829e-7de1-32b4-9c1a-758d1fd4d8c1 | -12.49577 | -53.85643 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc1bbe29-9f9c-3810-9047-e8cceff34fc8 | -15.22398 | -52.35587 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6410dab0-7f21-3853-9965-3c7d7e97c677 | -13.25591 | -51.81217 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7d512d1-15d1-3028-b296-48a1efd3beca | -11.68614 | -52.1869 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84a83589-73c1-3451-b241-7435714f17c9 | -13.92661 | -53.99934 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e20df442-e6fe-30b7-9052-29d2ff7b46dd | -13.00149 | -54.8022 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa861cc4-1115-3d80-a201-dc465af472a6 | -10.54945 | -47.00618 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d6767b37-bbec-36a8-9255-681db61aef7f | -11.19166 | -55.01037 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e4186c4-b02d-3403-aea2-001b90cbd186 | -16.31918 | -52.94361 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d06374ac-fef1-3a09-9d8d-a1c37d9c915b | -9.68906 | -51.08852 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68187775-2864-387f-bdf0-4e202ba14765 | -14.33765 | -60.32912 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e1ad783-6549-3681-a709-dd5f030a8eec | -12.95577 | -54.82217 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6cbf7c8-8d99-3040-b31e-7c2951fd1a80 | -14.57552 | -48.00814 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8610f384-1f02-3bbf-9e18-eb1b3f876e28 | -11.32477 | -55.22284 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7bf5234-832c-3066-8992-6fcd387f8289 | -12.29666 | -49.9936 | 2025-09-06 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7f9d849-b0ab-3a0d-a8cb-4d742fb9954b | -13.00493 | -48.05577 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d291878-639a-311c-9d38-440cd44649fb | -12.98547 | -54.76207 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0b14f38-949b-3909-8233-0cde32ddad54 | -11.63953 | -52.23232 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48ef8035-01c7-3766-8500-5a1d99e8bc5a | -14.58274 | -48.00966 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 386ead81-f308-337b-ba06-dbe983b2f108 | -14.96529 | -47.5879 | 2025-09-06 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| dd8181c8-956d-305e-b691-951bd884b6e9 | -13.005 | -54.82624 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 05438f95-6c26-3da8-afd4-5d7362d03098 | -9.4572 | -60.52029 | 2025-09-06 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 115330c2-f496-3c40-a439-ecc3f9118df4 | -10.067 | -48.06885 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53c76d4e-5be4-3e54-b577-bc1a6267d224 | -9.4294 | -62.36634 | 2025-09-06 04:40:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e4fa50a-5d19-3083-8f1d-485fa84d528f | -12.47792 | -53.85337 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d8ee73f-7705-3102-924f-e3309ea66a19 | -12.92032 | -48.01938 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README64.md)
