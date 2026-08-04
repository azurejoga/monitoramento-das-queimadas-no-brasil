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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dd0e217-5a13-3d31-8a9b-176a68e97e38 | -17.96138 | -47.13958 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9ede9b6-d080-32af-a844-87ec0a9f7dc6 | -17.9845 | -47.16644 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5bf6e5cb-e898-35c9-9ef6-cfe6b1e1957e | -20.99213 | -42.83253 | 2026-08-04 04:21:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 32a79d22-7833-3f03-807c-be90bf6ce3d0 | -20.01683 | -41.94409 | 2026-08-04 04:21:00 | NOAA-20 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c988a29e-3daf-380e-a1fe-15cb3a75165b | -21.21914 | -45.78813 | 2026-08-04 04:21:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e492796e-e54a-395d-849a-db79b3bffdea | -17.98115 | -47.16585 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ccfc6bd-7c6f-3461-b5d2-6bcdb3c699e0 | -15.05267 | -41.35083 | 2026-08-04 04:21:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b2f26bf3-d865-389f-bd2e-d063e7eebabb | -17.98785 | -47.16702 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9257342-de8e-38eb-bde6-509e0e043edb | -18.95583 | -43.17821 | 2026-08-04 04:21:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dd18aca8-c6df-36d4-83a3-684d8086a329 | -18.71521 | -47.58432 | 2026-08-04 04:21:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90f93356-c411-3233-932f-b956ca7767c5 | -14.26137 | -45.26144 | 2026-08-04 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68fd9549-68f6-334a-b4de-befb8ae180c8 | -17.97901 | -47.15792 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a91337f-51a2-32a3-8eb1-c32ef198fd39 | -21.22248 | -45.78871 | 2026-08-04 04:21:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3dcd108f-c83b-3d1f-9ee1-19bf472665f0 | -17.9851 | -47.16277 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 071ed776-3421-3666-b90b-1f9bc25c6e01 | -19.00669 | -46.24714 | 2026-08-04 04:21:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17800b2e-2e17-38ea-9ede-db028af9fa7a | -17.95928 | -47.13935 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dca9aa1c-557c-3e30-a885-0f491d17b296 | -17.9912 | -47.16759 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 110be8ad-eb40-303d-be80-4879fbacbfd2 | -20.50866 | -41.66865 | 2026-08-04 04:21:00 | NOAA-20 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f1bc2e0c-50de-339d-b882-0089db822ad4 | -17.86379 | -40.05231 | 2026-08-04 04:21:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cd0992f1-3ae2-3b87-841a-59dd5e6d3e8f | -22.10877 | -47.01282 | 2026-08-04 04:23:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2791c269-0089-3cb7-83e9-2454e6a5c2a0 | -22.57511 | -46.65875 | 2026-08-04 04:23:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cb8f46ac-6b98-3a19-bfb1-fae4ec12c1db | -22.31594 | -47.18305 | 2026-08-04 04:23:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b7f9d698-5462-3f1e-a21a-a41d32848ec1 | -22.92075 | -42.43978 | 2026-08-04 04:23:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8f329963-3f46-3dbd-bb5b-212f163dc352 | -21.51754 | -49.64075 | 2026-08-04 04:23:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8dbe1d13-1f7f-3fba-8329-c1d934029958 | -22.91686 | -42.4392 | 2026-08-04 04:23:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 541d724b-09a8-3ff7-8f2a-bc802f609b0c | -22.85727 | -49.3566 | 2026-08-04 04:23:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21486823-bd75-3c76-88d4-349f8c325dfa | -23.21963 | -46.43789 | 2026-08-04 04:23:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f4566bc6-67c1-3561-9e09-4c6379ed1c51 | -22.85384 | -49.35588 | 2026-08-04 04:23:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae172992-b636-3156-bc84-e2636e8e7ace | -22.62543 | -46.24387 | 2026-08-04 04:23:00 | NOAA-20 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 56d3b37f-890c-3bbe-875d-5eaea7d62370 | -22.5718 | -46.65814 | 2026-08-04 04:23:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a9103e28-f2b8-3e00-9c42-8fc47c0e4e8d | -11.2213 | -54.855 | 2026-08-04 04:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| f2e69bba-6076-30f9-bdf2-e44bcabb0101 | -8.3544 | -45.9897 | 2026-08-04 04:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 33465e77-0c3d-3cfd-9e03-4bb56d6b7ec9 | -8.3546 | -45.9671 | 2026-08-04 04:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 1c8aab2e-4a66-3ee7-8995-98e1c818c7e4 | -8.3544 | -45.9897 | 2026-08-04 04:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 09ffd6d0-adf9-3ff8-ad86-d7912a6d5f2c | -11.2213 | -54.855 | 2026-08-04 04:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 26bd587a-e343-3c73-8e43-c4c422529472 | -8.3544 | -45.9897 | 2026-08-04 04:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 2602ed51-53e6-38fb-98fc-2e675bb276fb | -8.3546 | -45.9671 | 2026-08-04 04:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| e675355c-3da6-3475-a7be-dbd4ff4daab4 | -11.2213 | -54.855 | 2026-08-04 04:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 640faad5-30d8-3a5a-b819-3df7b0b04db9 | -11.2213 | -54.855 | 2026-08-04 05:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 5cef0d3b-f8ca-3137-afef-5c69f52b93aa | -11.2024 | -54.8567 | 2026-08-04 05:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 659874d4-efb5-3506-b057-5ed82292027f | -11.2022 | -54.8771 | 2026-08-04 05:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 144e3252-0be6-3fe0-bcbc-d7d0fef8482b | -8.3544 | -45.9897 | 2026-08-04 05:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| c6eb8c83-be1b-374f-9489-bbf739c5f433 | -8.35921 | -48.24422 | 2026-08-04 05:04:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 70530bd9-1804-33e2-8431-8fc8718439af | -6.55076 | -55.15878 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3df9d56-f62b-35b4-8b5a-fb1ac82e2431 | -6.56627 | -55.16832 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40d149b5-8aa8-387b-8515-3e2b5e02d647 | -7.11607 | -46.72238 | 2026-08-04 05:04:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96d0db86-6e2e-35e5-b2d7-9000bd98b88f | -8.93674 | -45.20091 | 2026-08-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c98a465-f3ab-350a-a036-b192fac00234 | -2.31121 | -48.5876 | 2026-08-04 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70dc54fc-21d8-3e83-9d65-4ba494cfef98 | -6.5425 | -55.1682 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab6d580a-b942-3265-af54-63788017de06 | -4.89684 | -49.96035 | 2026-08-04 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44e25a20-f9ca-3267-8bbc-83d3a26f83f4 | -6.10239 | -55.81165 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fabcbd9b-a9ce-34a4-b399-3988c8c4ff98 | -6.57719 | -55.16348 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62ab8ec0-1cc9-36a2-ad28-a770b8dc9b64 | -6.56967 | -56.54204 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ac59cdb-f530-3331-81b8-f7d72b52a5d3 | -2.56872 | -59.87417 | 2026-08-04 05:04:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9134ed3c-fbe8-39d1-8a2b-a914aa2811fa | -1.63969 | -54.4599 | 2026-08-04 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd3295cb-7698-3d89-b870-85ca9e8a7e2c | -8.92822 | -45.2107 | 2026-08-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16d8de06-f6c7-3fff-b718-0ec4414b6712 | -4.89573 | -49.96796 | 2026-08-04 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c189fc69-d908-356a-8c0c-b0f9e9de1fae | -6.54798 | -55.15477 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a573210-ccbf-30bf-9e46-fc21a95303bb | -6.56245 | -56.52308 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5ac3c12-0ea8-3700-a5a8-04862d09bfdc | -7.61256 | -46.46565 | 2026-08-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| edf05332-ca57-38e8-866c-dc1e0fd26ad3 | -6.56071 | -55.16033 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1076fa69-6890-333e-b099-35493529bcba | -5.63365 | -45.91471 | 2026-08-04 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af403985-127d-3984-acb2-98ebbff076b1 | -5.14157 | -46.20704 | 2026-08-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 68146fd0-5710-3bc3-a252-86da5521ea24 | -6.95763 | -52.82155 | 2026-08-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 944f3447-4a1b-33a9-9586-7999199e3c75 | -1.54816 | -53.69414 | 2026-08-04 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96e8d6d6-0db3-3733-9381-2dc204db60a1 | -6.56577 | -56.52359 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6a591bf-d4b9-3026-b36d-ae454466e7c1 | -7.12595 | -47.42916 | 2026-08-04 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 393f4e61-5a87-3a8e-96e7-f7e7bbddb4c6 | -6.10292 | -55.8082 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0330fa8-a2b3-3a9a-bbab-2dc39105a522 | -7.60705 | -46.46489 | 2026-08-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4ed03902-c6e2-3257-808f-bdeeac8c0153 | -6.56191 | -56.52655 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c5b9178-20d5-3194-94c1-87c72a7ffca4 | -3.66724 | -49.46732 | 2026-08-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 40273e8e-02af-3840-8ecd-bd19c9fbb4b4 | -6.57453 | -55.15889 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5fe6910-82ec-36bd-ad63-2b3f7334d84f | -6.55245 | -55.16974 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b1a45ea-8d4b-3fca-94e7-0f6afc3953fc | -6.57612 | -55.17046 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3a1facc-53d8-32de-b801-5ecd089480a5 | -3.58207 | -50.2648 | 2026-08-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c4ef98c-5681-3755-933e-f9d2962de307 | -6.54968 | -55.16575 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3cfdbc2a-e2ad-3379-b2be-f775106277bc | -6.74732 | -60.02018 | 2026-08-04 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 983f222f-2c0b-3571-94be-235667852f1f | -8.35484 | -45.98631 | 2026-08-04 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ba340240-db85-3fbd-abd2-3643f6c6ec94 | -5.1425 | -46.20047 | 2026-08-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d761288-0ec7-34f5-aafc-02626f7b56bc | -2.69219 | -47.35766 | 2026-08-04 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6674fb0-248a-354c-bbba-8b7229bae994 | -6.55855 | -55.17426 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a263043-ecae-3b1c-8159-edc7cf03546b | -3.98206 | -48.43492 | 2026-08-04 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c1b86fdd-8609-3a91-b854-fab7ed9fcff2 | -4.64039 | -43.12914 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d86e6742-90b2-362e-b156-486d0f545ade | -6.36014 | -55.46708 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3dba36a-c085-3feb-b3d0-dbbea64a6bb3 | -3.0293 | -48.41299 | 2026-08-04 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d77e3bba-ea49-3ab7-90f2-b1f629d9f797 | -3.67089 | -49.47188 | 2026-08-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 28809270-5adb-389f-a0f0-2c5d3efbc403 | -7.61291 | -46.46415 | 2026-08-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e343bc1e-4ad8-359a-8cac-96854a2c4c3d | -6.5486 | -55.17271 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc11fb1a-5af5-3a6e-993a-7e0588d52e9f | -7.37768 | -45.05556 | 2026-08-04 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 465965c6-6294-31f0-a30b-7373b05e1068 | -6.57345 | -55.16586 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9beb5631-bc16-3f26-9705-ead0807838e9 | -6.96483 | -52.82261 | 2026-08-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf26d4e1-5849-36c2-924e-fa64b3579a74 | -3.67397 | -49.48033 | 2026-08-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 20ccbd4e-7504-3d15-a843-5e125dd3de5f | -6.53085 | -55.15567 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5f721bb-66f5-36bd-ab43-34a18058a288 | -6.56565 | -55.15038 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f48163f8-ce43-3909-92d0-d16e2dd07a69 | -4.37009 | -47.76996 | 2026-08-04 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a354884-f968-323f-8b8d-badac5e0f99b | -3.92731 | -59.40529 | 2026-08-04 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 168fc7b6-1526-3904-8136-b8d538e693c8 | -6.55859 | -56.52604 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8170b25-570f-377f-a88a-c17ab51cceca | -2.7477 | -48.76859 | 2026-08-04 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d946b8c1-0afb-378d-92c1-ec491e178ff3 | -6.54304 | -55.16472 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9896b11-df77-32cd-a63f-bc1798be988f | -3.11575 | -47.91285 | 2026-08-04 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README12.md)
