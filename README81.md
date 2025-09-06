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
| 65ed3242-d2b8-3e87-8744-8cde8cd82391 | -6.84432 | -52.80828 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae3cf2a3-17df-3d37-89cb-77fee2bd2e30 | -9.46902 | -60.51446 | 2025-09-06 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bedc43f6-07e5-3111-8fcc-aafefa636033 | -9.23161 | -57.08305 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f418ddd-0126-3268-902a-bd433c8dbe96 | -7.79805 | -52.12949 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b4e0e29-0323-39d4-8f34-e5f873dd6406 | -5.06382 | -56.07447 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37587823-0918-3e20-bbe1-8b91a05815cf | -9.46611 | -60.51001 | 2025-09-06 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6523d567-4a28-3deb-9a69-73a4cdc35c78 | -5.50744 | -60.12696 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccd73e38-d40a-34d7-aa84-85040749bda5 | -5.48524 | -60.13494 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d92dac2b-47bd-3b2a-bc4d-f98e79678f91 | -8.42138 | -62.29187 | 2025-09-06 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b03b99cb-a78c-3975-9b19-2c6b9269d0b0 | -9.23107 | -57.08694 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb2d2464-8320-37fa-b520-b9d62d87a93e | -6.1737 | -53.50208 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e551408-4d2a-3c16-9d52-bd65f374c42d | -5.07295 | -56.07176 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42dbcbb9-1ae7-3be9-805a-d77abde0e032 | -6.19336 | -53.24525 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a214654-52bf-36da-ba7b-333ceff6ee58 | -7.38801 | -59.66338 | 2025-09-06 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2fe8115-e87e-35e1-8a35-35aae1378ca1 | -5.00806 | -56.03761 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7fa4f12-ab14-3dc6-a895-7fc827c9bb74 | -7.73389 | -50.31786 | 2025-09-06 05:29:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c60447f6-0759-3629-8409-148e542a0a72 | -9.2398 | -56.89885 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc157111-69bf-32b9-9289-f356f74092dd | -8.77478 | -49.63686 | 2025-09-06 05:29:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9e5d54c0-68fc-3712-847d-e67199ef9ef7 | -6.26627 | -53.45454 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 473e1a5f-70b1-33d4-88ef-53405db56f39 | -5.98276 | -53.59478 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66ffa6f2-3b66-332b-ab54-18c1b011de4a | -6.69445 | -63.1295 | 2025-09-06 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8b922e6-e723-3557-a9ac-173e52fc871e | -5.76955 | -56.51013 | 2025-09-06 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66466dbc-aa97-389a-b203-572158497ad9 | -4.89922 | -55.99138 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05b5614b-362e-3326-80e5-d1eb90c967f9 | -6.44393 | -62.86126 | 2025-09-06 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f66bc55-52b3-386c-858e-5771a80b89b5 | -6.26802 | -53.44185 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b21ccb2-66fb-3530-a270-c0832e2159a6 | -6.56356 | -49.84865 | 2025-09-06 05:29:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d00ee43-849a-31f2-9a35-913685c1e56f | -5.90591 | -57.72437 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e022fc2-080f-3c49-adc1-11026f8dc41d | -6.84635 | -52.84132 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b321aef-8923-35ae-a909-bc5440e70a92 | -6.81636 | -52.80832 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 92f6671d-8834-3c73-9812-b06370a37f71 | -8.47867 | -62.64568 | 2025-09-06 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17e5fc9c-c6d3-3be1-8686-b98e1e4ea46e | -6.45965 | -55.88727 | 2025-09-06 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9c98d4f-129f-321e-8fa0-9a96c6ee0f8a | -5.06868 | -56.0711 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76a8e6ed-c018-3243-afd4-8894e54cd98c | -6.68826 | -59.42788 | 2025-09-06 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da232834-f178-3b35-8d6f-b994347d7a88 | -9.24349 | -56.90387 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6aa9fb1-b149-32fa-989a-5ba018877d3b | -5.13085 | -60.36677 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3279c6d-cdcb-3007-8e38-df38979d9726 | -7.79226 | -52.12989 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71b99d7e-cb3a-3d49-9bd9-fcbc27c8e1cb | -5.94814 | -53.80027 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f1c6816-efa3-3606-902b-a215ef6cae5c | -5.48922 | -60.13177 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47a88ff3-8c3a-37bf-aea6-5b5eb64c3a9a | -6.26978 | -53.42904 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67119866-4659-3edb-b432-b1761d87d051 | -9.70584 | -49.48523 | 2025-09-06 05:29:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7649d8ea-9b6c-3240-a57d-39085bdfb7d7 | -8.8833 | -62.38247 | 2025-09-06 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 628fa6c6-64f9-3bc4-b305-a8856883b7ac | -5.97719 | -53.59702 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebe4f4aa-81c2-3c5e-840c-8e757d207275 | -6.19292 | -53.24844 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0913324-7718-3bc0-b57c-7ac9e20c0142 | -6.86942 | -58.93666 | 2025-09-06 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4484bb25-1cd8-349a-b6d1-842d57bfcc40 | -6.34288 | -60.03186 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e05b8d0-2002-3c7f-a948-914d01f27df2 | -6.32248 | -58.17668 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7594c87d-a0db-3b59-add2-0d7f7e744335 | -9.07187 | -62.35124 | 2025-09-06 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cd1138c-d382-327a-95cb-19ec56b69d5b | -14.18 | -53.0564 | 2025-09-06 05:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 046d288b-01ac-328b-9999-19bccec8853e | -15.63569 | -52.89999 | 2025-09-06 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f27470cf-53e2-32af-98a8-3f46308b9e57 | -9.99502 | -60.01363 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea9fab7d-c5bc-38c7-b180-f0709a61b528 | -14.1771 | -53.06804 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| adf17b92-f870-3b83-9603-81d7ec2c4653 | -12.9822 | -54.82364 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b26b0d8-3321-35c4-91a2-a1e296c46445 | -17.60766 | -50.55953 | 2025-09-06 05:31:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6fcb09b-ace0-3d9c-af6b-1d65fba8ac85 | -15.21886 | -52.35357 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0a8f9965-c835-317a-8a36-4336827143c0 | -7.69092 | -50.27134 | 2025-09-06 05:31:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 644a82ac-ef51-3cad-a3d5-93001fc0746a | -10.60015 | -44.31692 | 2025-09-06 05:31:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 1eeb7039-39c9-3bd4-9076-f094252e5902 | -12.95555 | -54.78072 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c315dcfe-7526-3764-a35e-601ccbfa60a2 | -14.18758 | -53.02905 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 31683808-0872-32c8-9856-0bdc27726d61 | -14.34551 | -60.32485 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94cff997-7f65-392c-a897-cb49c5539bbf | -10.59842 | -44.32757 | 2025-09-06 05:31:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 6a265d73-a694-3e62-917a-8282356f91df | -11.64834 | -54.54432 | 2025-09-06 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55d42ad9-5bc8-3b25-ba7a-03365f1c3bb6 | -12.95594 | -54.77741 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cc17ece-cde2-3080-b918-a85fa6fea7cc | -5.98474 | -44.72481 | 2025-09-06 05:31:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 9d1d9484-cfb2-3c87-9eb5-b0fda7638490 | -14.33749 | -60.32792 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 682410aa-ee28-33a0-8b30-dddc66f51f8d | -10.88449 | -55.72674 | 2025-09-06 05:31:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c3a9738-b485-3d9a-b2e1-63aec6b42aec | -12.488 | -53.85456 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be578923-1ff9-3c40-a9a2-416b6e79ffae | -10.41917 | -60.74399 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 347544ff-d643-390c-ae4a-66993f8c8fcb | -12.38742 | -62.20535 | 2025-09-06 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc5050e8-1864-3985-832f-c57acd02b6c1 | -12.49284 | -53.86086 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e746821b-90f5-377a-8248-51fb328b718a | -13.92925 | -53.99388 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d66d0607-2449-3a00-adac-237fc06e2f9e | -12.99422 | -54.81221 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8386b676-86e1-33da-9eab-5f24c237db20 | -10.42556 | -60.74893 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 402a0545-3e0d-3604-b4af-2afcb2faedbe | -13.00253 | -54.83838 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d72a7535-8e27-3288-be5d-17c70dd846a6 | -15.1761 | -52.40002 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65d51873-6c83-38b9-bada-8e9e1a4be90a | -8.08632 | -45.31401 | 2025-09-06 05:31:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| aee8fe81-4232-360f-ab4e-c43d7a859f78 | -10.60626 | -44.33979 | 2025-09-06 05:31:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e4b0c62b-25f0-32f2-aa2b-f0642658cfe5 | -15.71857 | -53.56564 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34ae9755-d83e-3c00-ab7f-a74845a67502 | -11.47853 | -55.54788 | 2025-09-06 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 93825ba7-a577-32ef-9308-d37fcfbb13eb | -10.44786 | -59.55133 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6b6f8cf-b468-32a5-bf5f-34db2f99b359 | -10.60798 | -44.32911 | 2025-09-06 05:31:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 270.4 |
| 8548231f-0950-38d8-803a-0cb357af8bad | -12.98258 | -54.82048 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32d492a8-5d3f-3a85-96fd-b9d2d3f95ed4 | -13.00327 | -54.83202 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9353ae4-de43-3f3c-b2c3-98e8240f1e29 | -15.20579 | -52.35688 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5f27a17-f539-33ff-8acb-0eee5c5f3f9a | -7.04967 | -44.34868 | 2025-09-06 05:31:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| afbd0e2c-9e07-31fe-96c5-773a40987442 | -12.49859 | -53.85988 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf3f006d-25a3-3670-a0a5-00c46d03b390 | -11.20801 | -55.02874 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eb7718d-4517-3e92-aafd-5183d6c75b1b | -12.96562 | -54.78535 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7713997f-cf64-3205-ac10-62c49d112d51 | -12.99986 | -54.80955 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 890632b8-2454-3f3a-8323-df9e4d7b3073 | -11.18035 | -55.0456 | 2025-09-06 05:31:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e6c0161-1654-3e6d-bb84-33bce0f0699a | -10.57539 | -61.2486 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6aede174-78af-3b03-a9eb-9233ec41711a | -15.5798 | -52.89542 | 2025-09-06 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 948da5ff-a57c-3470-9bd3-ad21c7ab4fe0 | -11.21807 | -55.03003 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e52e80e9-fe39-3656-ab5e-6d89144881ba | -12.35333 | -63.64418 | 2025-09-06 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66c28d89-bf5a-3ad5-8cda-8c57e3716302 | -12.4988 | -53.85798 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8244d660-0611-3b8b-9789-3cc5dfc397a2 | -15.57417 | -52.8902 | 2025-09-06 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eff4119d-5780-3243-949e-398f874f50ef | -12.99543 | -54.80243 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36687aec-305f-39f3-88d1-b52f69ab4bd7 | -13.92967 | -53.9903 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f482b477-dfae-3b86-abac-e6d49cd4c49d | -9.93466 | -60.10152 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e3334cb-0794-3461-bfbc-2820206ab9b8 | -15.1776 | -52.40666 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d43618a6-c9c7-3544-a7f9-a0d0a65de4de | -13.01777 | -54.84399 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README82.md)
