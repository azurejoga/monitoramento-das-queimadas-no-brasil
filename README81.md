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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7a51c4f-b90a-363f-b7e9-ec6ff5ff775c | -3.44953 | -58.21583 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d285af01-adc0-300c-a761-25e8e03fe8d8 | -3.02617 | -51.33899 | 2026-09-18 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbed2d10-3554-3559-ae7a-90b6dfbfb1d9 | -6.16094 | -55.70116 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93f87a00-c41c-32fa-bede-e318a64badf1 | -5.73779 | -52.24846 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1029092-b692-3800-9081-d47daa135bb6 | -3.56862 | -43.47119 | 2026-09-18 05:16:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 548700e2-0537-3af7-ad53-c078b784fd6c | -3.26672 | -54.26746 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a95e39f-f2d1-3c44-aad3-d0055f499383 | -14.22052 | -48.51006 | 2026-09-18 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d5182af-62e3-39b0-88df-0b5b8671aa67 | -9.70978 | -47.09965 | 2026-09-18 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58df76ec-4a06-3618-af1d-e2aa968503bf | -11.51987 | -46.86338 | 2026-09-18 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5c2a44a-8841-3526-a67e-031132c55d10 | -9.39222 | -46.84705 | 2026-09-18 05:18:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da278c26-354d-398e-bb9f-bcd51515b1b2 | -10.54523 | -44.85271 | 2026-09-18 05:18:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26e6bd00-99fa-36ab-8f72-4445632f8ba2 | -9.59572 | -45.85961 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 13a7bc47-3167-3830-89c7-55a1e1c9335d | -14.22645 | -48.51056 | 2026-09-18 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e5f6575-ff64-39b2-bda8-4478939262dd | -10.1107 | -45.65173 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7f93f5bc-22d5-3e30-a7e2-32191a4181b5 | -14.13578 | -48.72892 | 2026-09-18 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dde387ea-e717-3fde-9a40-99e44246de48 | -6.92521 | -63.02525 | 2026-09-18 05:18:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b852839-1b2d-3650-b12b-783c99414be9 | -10.11623 | -46.3031 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76b58876-c9a5-32df-9d7e-2884c41de7e8 | -13.00232 | -46.93943 | 2026-09-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2703e497-f6cf-335a-b46d-016a70e3affb | -8.77409 | -46.90385 | 2026-09-18 05:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97482f8b-d5c6-33b6-b055-b4b3f0c492a1 | -9.91535 | -46.54162 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04417049-6160-3f5b-ae91-011b7489be4b | -10.65536 | -50.25204 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 58409d69-1e9c-3b75-8bb7-74dd11bf5ce9 | -9.76636 | -46.08245 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efcadf57-ceaf-3216-823a-17cc260afb9f | -11.1324 | -47.70822 | 2026-09-18 05:18:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4976dfd2-7719-3458-8b32-5f8a05a0e66f | -11.00042 | -57.0605 | 2026-09-18 05:18:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47058303-00d6-3ffe-9c86-ddc302b6371b | -11.06136 | -48.30025 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bcf28e5f-75b6-337d-adef-fed0a5aa2292 | -9.38819 | -55.97378 | 2026-09-18 05:18:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebb8a518-64a9-3101-a531-9459a20e95bb | -11.63875 | -51.58366 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 531d41d4-5324-3d31-94a3-38462dfb9324 | -6.92931 | -63.02596 | 2026-09-18 05:18:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 396a6a73-9cf3-3afd-a271-4e4e78e717fb | -9.77907 | -45.04215 | 2026-09-18 05:18:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3134daf6-1ead-3c23-b747-b9a99548d327 | -10.88831 | -53.99884 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 897061aa-224f-35ee-9641-b004411c894c | -11.87454 | -47.58816 | 2026-09-18 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fda7dd17-b547-3d7f-b8d0-4df0a44e42aa | -10.61331 | -46.56412 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4736b32b-7e37-36e5-91b4-4d2a1add7df2 | -11.55754 | -46.89707 | 2026-09-18 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a654cb33-6485-3833-bf0f-a7a5a3137bae | -12.5522 | -50.7141 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6b4d23c-8e40-3870-935d-2dbc139a0370 | -12.53781 | -47.08247 | 2026-09-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a17c6104-47fa-32de-8b74-90f4776c253f | -8.90526 | -45.01443 | 2026-09-18 05:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5bb3cda9-26d5-3d04-8f68-aefa7f1686b7 | -8.86623 | -62.39877 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f094834-4e61-39d9-ae7b-30c355fc72d2 | -9.945 | -46.6137 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3e6bf490-7d04-385c-b946-ba02466961dc | -10.65614 | -50.24619 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 391df3e2-b1b8-3dcd-85c2-d32f5d30a983 | -7.87525 | -54.72337 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32e07b3b-4d30-311f-9e46-acc1cd5d435a | -8.93251 | -51.46238 | 2026-09-18 05:18:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5e3dc4a-6b88-379b-b683-737c072c906a | -12.40126 | -50.69876 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04c164e5-842b-33bb-9855-0c7d51ccb65e | -9.60114 | -55.10172 | 2026-09-18 05:18:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be0846d1-9c49-3a5b-be01-d93e85025837 | -12.55978 | -50.73111 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3cf9aca0-6db7-316f-b4ce-18165d0bb7f8 | -12.17755 | -46.98904 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42190e0b-66b2-34d5-aa01-1d4cba1707e3 | -12.78025 | -47.56706 | 2026-09-18 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54840088-897d-323d-a1de-370e970271ff | -13.74478 | -48.80127 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c7fd86e-15e3-3556-bad8-afddde73138f | -11.06588 | -48.30301 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74b53fac-cc4b-301d-9e9e-da1d6d644a25 | -10.51835 | -46.71971 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bdbc4bf-f787-38ca-af7c-05a8789059a1 | -7.94682 | -54.89431 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ead2036-266f-351f-b0f5-ff8666f65ea7 | -8.90443 | -45.021 | 2026-09-18 05:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4702c55f-4e9f-3d47-bc98-e2a0daa3b059 | -11.98645 | -52.467 | 2026-09-18 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07c65405-1d18-3704-95c3-877374cfbfdb | -9.91575 | -48.38542 | 2026-09-18 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad3863d9-d574-3f69-9d2e-9d58fb8166d5 | -9.5722 | -46.56747 | 2026-09-18 05:18:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65657103-3a8b-3b81-9c5d-09a6e64c02fe | -10.81053 | -50.20002 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db1f5d74-8a76-32e8-a0aa-7cbb6dfc1280 | -11.5268 | -46.85921 | 2026-09-18 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 689746ad-7cdd-3d57-b343-4552cb87a060 | -9.8369 | -48.34756 | 2026-09-18 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c411d702-5831-3ec9-b22b-4b48e8902663 | -9.71774 | -54.81765 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0a6996ea-797c-371b-b9da-5288089f9efb | -13.68545 | -48.59629 | 2026-09-18 05:18:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ff935bf-4d03-3073-9662-a21310bc67da | -9.71341 | -54.8215 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 025cf0d2-3bdb-3da1-af8b-c699c5df1afa | -8.86125 | -62.39563 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4285697b-29cd-3783-8467-690790f7d7c9 | -8.91297 | -45.00857 | 2026-09-18 05:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51c88fc0-b8d4-36f3-9378-951273a01e6e | -10.51506 | -46.72198 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22a8db72-faa3-33cf-b56e-08f9be245afb | -10.95125 | -54.0906 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e66d3e3b-c50c-332d-b4f3-216936b1cc5e | -12.16545 | -46.98267 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 969fc053-2292-394d-b11e-467bc73e4b4d | -11.06899 | -48.28555 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05b7c389-4468-324b-b189-49705ac3f5f5 | -9.92544 | -46.51159 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf4fdfff-6408-36bb-a52a-88377bb627fe | -11.07304 | -48.30035 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fe9c47c-e8a1-3692-b80e-ca89281f134e | -10.50055 | -46.28411 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5432213a-0a77-3a23-8bf8-dc4e763a2334 | -9.93975 | -45.34199 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1898513-7205-381c-8b33-25283b91640e | -7.49924 | -55.01049 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c5b65557-9c5e-3697-9d02-db2292defe36 | -11.98704 | -52.46268 | 2026-09-18 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5361a695-17a7-3242-8b19-dae1e5bae685 | -10.51708 | -46.72974 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47030b22-fe63-38fa-846d-befa53fdf467 | -8.16027 | -54.81821 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 702eefca-6c06-3511-af79-9cf3d1f88770 | -13.75046 | -48.80277 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90fd6ec7-6491-3472-bca2-0a5910c63663 | -12.17688 | -46.99463 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a00251e0-eaa2-3028-a3bf-6b5d85a31f04 | -8.95053 | -51.46492 | 2026-09-18 05:18:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88888aa8-8ab4-30a7-a0a6-81e431572a78 | -11.13186 | -47.71275 | 2026-09-18 05:18:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5daeb5c1-f668-31eb-92ae-9d4b6add726d | -10.64609 | -50.24483 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 766c9926-7159-32e1-ae73-a236a66d60e5 | -8.91348 | -45.00886 | 2026-09-18 05:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33b98384-4c07-38dc-9477-a8600c6f122c | -11.20175 | -55.031 | 2026-09-18 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a6a2ef2-2397-3036-a95a-cb35f4859e4f | -10.66602 | -50.48711 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7b88e9e-8672-3cab-aee9-dd3313f67f53 | -9.70176 | -54.82408 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e3303ea7-2ceb-337e-b998-2a249aab7038 | -12.29233 | -50.75277 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddde7694-a55d-3db6-a4e4-3b3254f67739 | -12.25916 | -47.13837 | 2026-09-18 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0be2d96f-6c01-3d46-9354-5868c969141b | -12.30448 | -50.73692 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18fa86f3-09c8-3a4d-af53-b714d299b3cc | -12.55933 | -50.73866 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1056edec-4961-365b-8742-733b2b59bfb8 | -11.87565 | -47.57904 | 2026-09-18 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81931f34-8616-3136-bccf-3f6292c27950 | -12.51712 | -47.09517 | 2026-09-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2183e92-8b9e-3a7a-9d4b-ea317ab9a34d | -10.61895 | -46.06623 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9e9a69f-ab6d-323a-a970-b2f95785f271 | -9.71278 | -54.82574 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ef7b40fb-1a27-3eb2-96ea-e27d651aa30e | -9.91665 | -46.5309 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4d3163a-4b58-31f1-a4da-239e5ea01697 | -7.75147 | -54.75273 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4293ad7e-c08e-3ae4-81b4-766ede10ef0f | -9.57846 | -46.5685 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b12509bc-f7a2-32a7-96f1-81741e31f34e | -10.80937 | -50.20074 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8772002a-91ed-3e71-b0f0-608671c7fc39 | -10.84541 | -54.10431 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50941ebf-2b9b-3316-bd5b-f3f6318b3b84 | -8.48547 | -57.6264 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b72c1d3c-3cfb-3a39-9ba4-c661a6c83d13 | -10.64222 | -50.2354 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a6bdd4c4-7801-3726-bee5-cb37a3e94645 | -8.89953 | -62.40222 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd935492-2011-329d-9711-7dc4a06a7474 | -8.90173 | -62.41245 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README82.md)
