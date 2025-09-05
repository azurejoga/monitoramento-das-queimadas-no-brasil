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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaa2c94b-3b8a-31bf-93eb-5a00ead384ac | -6.26828 | -53.44389 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4989dd9a-42e7-3c39-8357-adbb5517929f | -9.82235 | -46.6559 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6da9827c-d817-3ba9-9021-70bebc9c25ec | -10.48157 | -53.6272 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1bac280-d647-3918-aa00-741e1e7997d8 | -12.91406 | -57.00861 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34a3b5a7-3770-303e-a572-7ba5979051b8 | -6.27935 | -53.43845 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9df956a0-2d6c-3572-a187-fe0f4d911d62 | -10.96206 | -45.96337 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae20f207-5342-363c-a188-d85a395de8b5 | -12.50348 | -53.83923 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9933b165-a59b-309b-a6e7-bb25392a0faa | -8.52325 | -51.31069 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e532ff89-e667-3676-9ea9-ee5079d41d15 | -7.77301 | -50.95966 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a65f93c3-91df-3944-8ac4-437867337c63 | -12.99823 | -54.82173 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e0e57b24-91b0-383d-9146-192330d4e173 | -11.39347 | -43.5989 | 2025-09-05 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8221dc0a-eec3-346f-a5ab-a795dc310c4a | -11.72444 | -47.75432 | 2025-09-05 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5735ccc3-69a5-32e8-84ba-dff69173ec0d | -7.95988 | -44.94806 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceab0a63-c861-3fa6-bb44-f8c8cbc3280e | -8.75449 | -46.10808 | 2025-09-05 04:57:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| feab0262-b8d4-3e83-8503-73221929727e | -7.23545 | -56.85244 | 2025-09-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8348e2c1-89eb-3acc-a948-90d4d3d2f960 | -11.74504 | -47.74643 | 2025-09-05 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd73f272-4dc5-3e34-9c42-db079821411f | -11.10239 | -52.02081 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6343388d-4d1a-3917-ba5c-ea2f351b19f8 | -13.00047 | -54.82944 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 040b7cd2-aea3-3c7d-af14-df58c8fc8665 | -6.47194 | -53.39995 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96ac0f92-2132-3bc4-ae2c-7b6293b12be8 | -10.03764 | -48.13241 | 2025-09-05 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2825def6-82bc-3ff8-8fba-42c09e9f7b27 | -10.06126 | -58.39652 | 2025-09-05 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d60eb96-f110-33a4-b2d5-4d47b1c2b090 | -14.27628 | -45.22353 | 2025-09-05 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 418dc12c-fd0f-3483-80af-650eb9dab091 | -7.68377 | -50.25724 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f6545ed9-955e-3df3-9055-ec79ab8d78a7 | -7.00137 | -55.10713 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b60284bb-0acb-3194-bd2d-c6f38277e0da | -7.6804 | -50.26432 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b79f4454-22cb-36f0-9cda-752f74cfd936 | -12.97428 | -54.79951 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddd3e3ef-6d5b-3e75-8a8e-96362dd97f58 | -12.96407 | -54.78342 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c080d637-b64c-3ebd-ae89-a95897b2788f | -11.97034 | -46.77923 | 2025-09-05 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ea1c526-a29f-328b-a233-033e595e8a9a | -9.48578 | -54.42892 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a61dbf1-90da-3641-8141-01c86f72e8ac | -9.51334 | -57.78912 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f91fe275-1ed7-3be2-b9c1-b3812dbc4a2d | -12.31773 | -47.04491 | 2025-09-05 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69b76f20-d0a9-3da2-8e59-2aea1a001292 | -12.64311 | -56.99747 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 525847c2-3c83-30c5-9cd8-84b9dc67562e | -13.7452 | -46.92585 | 2025-09-05 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc3b4dd0-b8c5-39de-abf6-c2c33fb1487c | -9.71921 | -51.07966 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 56105d2c-fa6a-3188-8272-38d637d55d53 | -13.10051 | -57.11482 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c755c3aa-1a9d-3e1c-bdd3-04a594952ea5 | -12.90457 | -57.00327 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8516ac93-97e8-315c-995c-0a37fdf1b731 | -12.97035 | -54.78048 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bec04060-eb32-32aa-8e88-05bf6a39555c | -12.83192 | -44.45095 | 2025-09-05 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7382f81-92fe-30d9-a2be-9f58d006cc33 | -7.9544 | -44.94705 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87d1ed94-1594-3c58-8c31-b64aaf647472 | -11.58015 | -52.17619 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8aede6a4-09a4-3932-b594-4d2b58637cd3 | -8.01026 | -45.44487 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd630ad3-2fb3-3bc2-a14c-e74a24d697b6 | -8.78201 | -49.62694 | 2025-09-05 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82ba46a1-e0a5-3a45-aaf0-da93addac801 | -5.85371 | -57.77356 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0ac81c60-5905-3cba-9645-0b1958e74f5f | -8.00021 | -44.77579 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9297608a-1dd6-36ef-9340-89a70c56fa4f | -11.5491 | -47.32133 | 2025-09-05 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa31a799-dd15-3722-8dff-86caf20d32e4 | -6.32923 | -58.17716 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6456d548-3924-36b4-9fa7-5d9985a41fb1 | -8.03857 | -45.39756 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 091f2bec-bf8f-3267-8d39-ae6ee88e5068 | -6.87089 | -52.78354 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2d96bf6-a2a1-3b38-99dc-a8e370514b1f | -7.38496 | -56.6908 | 2025-09-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa0e6eeb-d3a5-3602-8d4c-f4f112193365 | -6.87552 | -52.78429 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09225167-0282-3c09-96cc-1ddc400fbe54 | -12.98374 | -54.80471 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 368a25f7-d35b-3b14-ad83-3794c7377e22 | -10.98784 | -45.93177 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 449194d6-6be8-3406-a9d1-011dc8a076fa | -5.85209 | -57.77036 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1a5fd113-b7b7-395b-99e7-9de3070de239 | -10.85972 | -56.36908 | 2025-09-05 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6a31e62-b2d7-30f7-837d-9f183de49b9f | -12.99266 | -54.81349 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8c8ae306-3ebb-397c-b5a7-37103261f8b9 | -9.9654 | -51.65716 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db5da39f-169f-30cc-8430-8b171442536d | -10.96384 | -45.97087 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a49b07d3-e931-339e-87e9-591b5bb5be2f | -9.69891 | -48.9875 | 2025-09-05 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59a2e5ea-9738-3243-8431-56d47e6056b5 | -11.82689 | -51.43414 | 2025-09-05 04:57:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b11a8e5f-f623-35b3-82b5-14fc63b84636 | -12.9419 | -48.05575 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6823263-41a9-313a-8f07-9d07cb3f3ff7 | -12.96519 | -54.77623 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4df4d6b7-231a-3655-989d-dcd3b582708c | -11.19426 | -55.01004 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bda1bd16-cde7-3802-95e8-a71d68453137 | -12.97263 | -54.81027 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d930bd0d-1f64-3442-9c6d-49f09ad61fdc | -11.62044 | -52.20396 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 45306175-3e59-3a3a-8b8d-dd3ec3fa9a34 | -12.91465 | -57.00496 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47601352-b767-35a3-a227-633970e99d54 | -11.10112 | -52.02935 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa33930f-0999-3f78-9a0c-9c2ef5c6a9f3 | -11.19691 | -55.01399 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72e5de61-2d21-3d02-b74d-832ff7e7daa6 | -12.51371 | -53.84081 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c381f6ef-b4e6-3065-878f-982838c8a82b | -12.98281 | -48.0789 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fae648e-92c9-3921-aef1-9969dfdd646c | -8.89175 | -45.88105 | 2025-09-05 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aea9852-7ce9-319d-846b-cc7a0a3b47d6 | -11.65097 | -54.51743 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7816b0ff-140f-3417-92b2-0600e09e4162 | -6.32244 | -58.17128 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f94dd9a2-b0a0-3d50-8b2c-329fa47503b3 | -12.96925 | -54.78768 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70635387-283c-3301-882e-08f962728a2a | -10.48216 | -53.64602 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f31cf15-c869-387f-9b32-053b42a4064d | -10.48705 | -46.75747 | 2025-09-05 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea13cd37-17fe-3581-8917-c78a25cd05f7 | -12.91626 | -48.0278 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5bfcf562-7f12-3621-9a8d-da128fea7eba | -12.48304 | -53.83601 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1e21f7a-89d7-31d2-838d-c47814e08989 | -12.85515 | -48.00918 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ff12fb9-612a-3852-b7f0-8a83b136841a | -12.99321 | -54.8099 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2e4c6067-1830-30a8-b68e-04ad38d5452c | -6.93057 | -51.19736 | 2025-09-05 04:57:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e81464d6-7d01-3204-8cf0-6859a1c7af50 | -6.15782 | -53.41243 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8018a5f-0096-3e30-acfd-5074bd3ca0f0 | -7.6842 | -50.26516 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c118fe65-bd69-3215-9e1b-6ee89f56c544 | -5.9105 | -57.72915 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9b6de64-2fb4-3a86-bcea-9139c2911163 | -11.58614 | -52.18578 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3da59989-7d55-3f1a-b160-d191c8cf3d12 | -11.83203 | -51.42536 | 2025-09-05 04:57:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9da7c2cc-73c0-31f0-8bb7-fc3bd2ce3cfc | -11.20244 | -55.02208 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ab03387-be21-3ea7-9840-fc3392dd7e14 | -11.77472 | -60.89093 | 2025-09-05 04:57:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f1346a1-37db-32e2-87ad-3e4ab1f9256e | -7.68578 | -50.25472 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d703adef-c6c2-32ff-94b8-d50acbc5dca1 | -11.02236 | -45.0707 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 250109c5-8464-3891-bdaf-f0b38239d5cb | -9.44403 | -46.81598 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73d7dae1-6352-3846-84be-56bab546f93e | -8.48209 | -45.07608 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa0134d3-37ed-3d4e-8c70-e7e73874095f | -5.86109 | -57.77495 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28754e38-5ebf-37f0-acf1-3aa64c35d465 | -8.18336 | -47.42278 | 2025-09-05 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab8f8ce4-ffef-3fa2-8680-613f1ec41830 | -11.64931 | -54.52815 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fffdc360-32da-3ead-9ce7-31c21841c255 | -8.03634 | -52.35243 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4253b3b-ce85-38c2-8129-a3e2b1abb414 | -12.90848 | -56.93664 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2643e84f-f68c-3edb-9f45-4cb38b6107f1 | -8.06289 | -52.34095 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f42c0591-b8e2-3b75-934b-7b19afff27a1 | -11.64021 | -52.227 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 618a1b5e-fa36-3a42-b2d3-77eb16fe1ecc | -7.77479 | -50.97297 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62091802-6b19-3f1c-a017-afa3be2664d1 | -7.59303 | -46.21105 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README50.md)
