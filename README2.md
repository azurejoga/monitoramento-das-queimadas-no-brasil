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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac5ea07f-d755-3849-9fa4-d1a5434e6898 | -8.846 | -50.5016 | 2026-09-23 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5b37c847-d70f-3c2a-bf5a-279216d15c17 | -9.1024 | -61.4491 | 2026-09-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 4914c583-5d0d-33dd-9d14-2e6adf12de08 | -15.2694 | -47.6327 | 2026-09-23 00:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 06f2339f-f0b6-399e-afc5-7548c61adb3e | -6.6815 | -55.0703 | 2026-09-23 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 4a07bf4b-666c-3b36-ba26-5db39c956782 | -11.71 | -50.98 | 2026-09-23 00:00:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d2a18e6-de22-3852-a250-5d7138b39e7e | -5.76 | -45.09 | 2026-09-23 00:00:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14d6c472-51fd-3f92-ad25-4a9bcc86df30 | -14.64 | -45.66 | 2026-09-23 00:00:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c11572b7-47f6-3631-a15c-eb8d5cc1b824 | -12.82 | -50.92 | 2026-09-23 00:00:00 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 085eee01-8c01-3106-b92a-a12d3d688043 | -12.79 | -50.91 | 2026-09-23 00:00:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 336aff67-27ef-3276-9429-377185c13075 | -11.74 | -50.94 | 2026-09-23 00:00:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e4d7b51-50a5-35af-a169-0f1ce60d5e7a | -12.82 | -50.86 | 2026-09-23 00:00:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4449ab72-49c1-3c72-af76-e1a13baeadc7 | -11.89 | -45.79 | 2026-09-23 00:00:00 | MSG-03 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83dcfc51-a2a6-37d9-9d93-297f13baa2ba | -11.71 | -50.93 | 2026-09-23 00:00:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b5580659-3ecb-312e-beab-b6dece89f0fa | -6.61 | -59.97 | 2026-09-23 00:00:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86667b85-5930-3b7f-b1d5-37813585e2d0 | -9.95 | -48.47 | 2026-09-23 00:00:00 | MSG-03 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3720e4c7-a319-3953-b465-53b1c17523c4 | -3.23 | -46.93 | 2026-09-23 00:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32062202-d3a9-3766-aa5e-f9b04ec4a1d8 | -14.63 | -45.62 | 2026-09-23 00:00:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f5b7b11-b471-3000-8b9f-58d52dc94197 | -9.95562 | -53.974 | 2026-09-23 00:01:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1128090a-bfcf-34b8-b914-7b8b3af63dce | -8.83125 | -50.49075 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| e76bb345-a79e-3a11-a858-c5b565f7f14a | -10.1165 | -46.08369 | 2026-09-23 00:01:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1ffdec8d-071e-3c13-a143-543d134cd804 | -7.61555 | -50.41902 | 2026-09-23 00:01:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| c38414b2-0a9f-3786-b01c-9624b563b951 | -9.85925 | -48.30826 | 2026-09-23 00:01:00 | TERRA_M-M | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a1422749-ac58-3d17-aada-60348b7e08ea | -10.91241 | -53.94849 | 2026-09-23 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 7df3d5b9-2dce-3d97-b1cc-2ec0e879dd71 | -8.84027 | -50.48948 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1b5f441c-1aaa-3032-a12b-5cb69d753513 | -9.03679 | -45.02368 | 2026-09-23 00:01:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 61a6a156-e6b8-3629-90bb-25da0bec83f7 | -6.60878 | -43.74208 | 2026-09-23 00:01:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 0f5b9529-739e-3dde-a8ea-ccafdaa60460 | -8.38712 | -45.59178 | 2026-09-23 00:01:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d343217c-563d-3738-8425-a3e3302e4ad4 | -7.09502 | -52.74838 | 2026-09-23 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| fda2f5a5-fe57-3078-8cc1-e04f5d213c9c | -6.52731 | -43.55676 | 2026-09-23 00:01:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 4a409b1b-f248-3b25-9364-cd6968aeca06 | -8.33412 | -50.83471 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ba398f12-b427-3e38-9ea5-f957ea3ef7d1 | -6.72387 | -44.1385 | 2026-09-23 00:01:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 05eb5cc8-1f85-30f5-a2a5-e14b3085bdce | -10.38839 | -54.41098 | 2026-09-23 00:01:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 689d2699-bd2d-3c3b-a606-c1dcf91bb17c | -8.22416 | -50.76964 | 2026-09-23 00:01:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d46c4012-908a-329b-8920-1a1f51cbdf95 | -8.45681 | -48.69966 | 2026-09-23 00:01:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 320bb457-f3c3-30b2-91f8-dfcf776b7ea4 | -9.70039 | -51.98016 | 2026-09-23 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9c728acb-027c-3c37-b5ab-a13860938937 | -10.32696 | -50.52472 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6d30d140-afa0-3fe6-ab3b-a5addc1b7e62 | -10.05438 | -48.84059 | 2026-09-23 00:01:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b94484e-90d0-33e3-b795-55c3cc86d642 | -6.32671 | -43.94721 | 2026-09-23 00:01:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 0c68fad0-1eb4-35e0-8b1e-d0dfe38924d0 | -7.09647 | -52.7596 | 2026-09-23 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| d1add7f9-2bbd-3233-a59f-2a29fa9e09ca | -8.23639 | -54.67524 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 07a05a2b-186d-3266-bd81-7064edf2c4c5 | -8.25153 | -54.79234 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8aaf4ff2-5852-34ee-b0b6-3980368277be | -9.5943 | -48.45589 | 2026-09-23 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 23741b04-94a5-3d6b-a847-b94da3bb56a0 | -8.4657 | -48.68311 | 2026-09-23 00:01:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 95324fc4-e537-38a7-ad85-d6c8a2479b44 | -8.7821 | -45.84652 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3a51b866-91d4-355d-94e2-10eeecd13349 | -9.95723 | -48.47926 | 2026-09-23 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 18c375a2-77c9-302a-bfbf-fe79fa4edd31 | -10.62095 | -54.00296 | 2026-09-23 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 48c8ff7d-01c2-3fb2-a178-038c0d0c3d0a | -9.85163 | -48.31828 | 2026-09-23 00:01:00 | TERRA_M-M | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b54f7bf7-8201-3130-a22d-06f4a515a663 | -8.37685 | -45.59301 | 2026-09-23 00:01:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1c4deb48-a532-3fc2-941f-19b26cb25106 | -8.6046 | -54.63197 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8a53d1a6-437c-34e4-83a1-c525b81cb7a2 | -9.96875 | -50.2536 | 2026-09-23 00:01:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 316ffadd-36ad-3950-9271-27fa3c3d4aa2 | -8.68566 | -49.41401 | 2026-09-23 00:01:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dccd2621-6bdf-3347-b965-4780e3bb9667 | -9.86048 | -48.31706 | 2026-09-23 00:01:00 | TERRA_M-M | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 37baa31b-2f8a-3657-89f7-420887b7e7b4 | -7.43691 | -49.84724 | 2026-09-23 00:01:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a5106d8c-4795-3015-bb30-2b11912d5397 | -6.1067 | -44.15704 | 2026-09-23 00:01:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| aa0a3c21-bd3f-34e4-b400-d4631db18474 | -11.0155 | -54.14698 | 2026-09-23 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| fdef89fc-0bec-33ab-b460-d1401acf9c57 | -8.83902 | -50.48015 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 1bc2b0bc-e065-34d4-9ffd-7fe717e8d930 | -10.61101 | -53.99429 | 2026-09-23 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 6b4800f7-f816-33d4-b86c-268a3ff2fe98 | -7.42566 | -49.83072 | 2026-09-23 00:01:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 056f102b-35bb-381d-a086-8ebdc39ac2ec | -7.41912 | -49.86452 | 2026-09-23 00:01:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 1b606c76-330c-3cf0-b3d2-9d700489cbc4 | -9.63327 | -49.67433 | 2026-09-23 00:01:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9192aa00-43fc-3600-a288-2a1b8dde9029 | -6.9189 | -46.55561 | 2026-09-23 00:01:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 238.3 |
| e705f3a8-0f11-35f8-8b52-848aa9c6a111 | -8.45086 | -48.44782 | 2026-09-23 00:01:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 65244101-6cc7-3423-a02d-87ed0e600906 | -6.85988 | -48.28091 | 2026-09-23 00:01:00 | TERRA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 60190450-1fa4-3b05-90c8-221cbe88b0da | -8.46818 | -48.7009 | 2026-09-23 00:01:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9c2cae3c-5d71-3395-8643-f8196e56e9ac | -8.59596 | -54.62189 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 96eb9235-9e54-3bde-b792-ddd6ce24f02d | -10.62263 | -53.99284 | 2026-09-23 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 9f620028-8484-3f4e-b74d-ac4f52eb8d42 | -8.59277 | -54.63361 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 746296d1-e802-3c4f-901b-093a57c80e7b | -6.8993 | -46.55822 | 2026-09-23 00:01:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 20a0809e-2d0c-3b8c-8e14-2adb3c2c1f2e | -10.36196 | -50.44492 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b109506e-ef86-3ba7-8230-4cd243a41715 | -9.95599 | -48.47034 | 2026-09-23 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 76dc570c-f1a1-36f3-83d1-2ac8b07bb2fe | -8.59813 | -54.63872 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 4c1d3700-218b-3601-ac5e-3104acd37e8b | -7.63901 | -49.51801 | 2026-09-23 00:01:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7715c1aa-3e2e-397a-a0e7-04490a5c4e3f | -8.79185 | -45.6342 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b1997a6f-f593-39db-bfc9-e6c2953ac72f | -7.13935 | -43.07866 | 2026-09-23 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.8 |
| 2b1c192c-8da8-3027-8f35-0166c9175342 | -9.55969 | -47.9393 | 2026-09-23 00:01:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3552fa86-c17b-3651-b189-d192eaa2c856 | -6.62095 | -43.7401 | 2026-09-23 00:01:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 1b7242f4-f3c9-3e95-8af2-7f6d617772f6 | -9.04055 | -45.01643 | 2026-09-23 00:01:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 52e50551-5d52-31a7-850b-da48d65735e7 | -8.35988 | -45.61981 | 2026-09-23 00:01:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fb5c66af-b587-30af-937d-c1980c853cca | -8.82558 | -47.25589 | 2026-09-23 00:01:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b105e6d8-cdb8-3d2c-8a36-3497a970cc1f | -8.36249 | -48.5401 | 2026-09-23 00:01:00 | TERRA_M-M | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0c4a9c80-1c79-3e0e-8afb-12c99ae13220 | -7.39591 | -55.2204 | 2026-09-23 00:01:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6fb0c2db-1d05-3fe1-858d-fdc6030bdc07 | -6.72885 | -44.1713 | 2026-09-23 00:01:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| dc99c833-6324-31d6-8182-c1762d77577c | -8.94454 | -50.92031 | 2026-09-23 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| aeaffb99-75c8-3542-a787-f69bf1d1f3b8 | -8.2619 | -51.1953 | 2026-09-23 00:01:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b171898a-7772-373f-94cc-3d60b18883ea | -6.91731 | -46.54454 | 2026-09-23 00:01:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| de1b57b6-6c4c-30b6-8cdf-4551b9c74cec | -8.24936 | -54.77552 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f2f1dc46-c8a3-348a-91de-a42d82aecd50 | -7.98531 | -44.09665 | 2026-09-23 00:01:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 95c34d9a-1d7b-33d3-b9c9-e2a9fa237e8e | -6.72636 | -44.15493 | 2026-09-23 00:01:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 207.9 |
| d8dd56b5-aa60-3dbf-8703-2188f99ef2c2 | -6.32412 | -43.93013 | 2026-09-23 00:01:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 8d1ff79c-1a87-32a2-9d23-65f8249d455a | -6.89468 | -43.64137 | 2026-09-23 00:01:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 06db1813-d6fc-3994-bb1a-5065a7d31fdf | -9.57051 | -46.53808 | 2026-09-23 00:01:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bed36a20-9378-3855-aa6f-137416431668 | -9.95761 | -53.98984 | 2026-09-23 00:01:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| ef44fe7b-5519-3fe9-97b6-f4d4e637f567 | -9.94964 | -48.48945 | 2026-09-23 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5af8fef4-7d0a-3be3-8feb-db2ccde735fe | -7.80857 | -46.60573 | 2026-09-23 00:01:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 81c53091-6016-366a-ac22-d0a7c94f713e | -7.0324 | -44.65679 | 2026-09-23 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 94d8e39b-3fff-3fb0-9d5f-d3473b79f0d1 | -10.609 | -53.97817 | 2026-09-23 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| b8195ae0-cb7a-32b5-a557-9a604b63b6c9 | -8.15064 | -49.54434 | 2026-09-23 00:01:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b937e6b8-c244-369a-a35c-d0a8287633b0 | -7.15179 | -48.45363 | 2026-09-23 00:01:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c34663a-edc3-3dbd-84c4-f7f76d1843f3 | -6.77512 | -48.66719 | 2026-09-23 00:01:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 17f8976e-f245-3ae2-a3c3-c057d30e12c1 | -8.25739 | -54.78598 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |


[Clique aqui para ver as próximas entradas](README3.md)
