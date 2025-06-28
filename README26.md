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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e6b6e70-dccf-34f2-931e-9424e480d64b | -9.71092 | -56.18105 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 63f82cf7-1eef-3421-9faf-48fc0adaaadb | -10.8808 | -53.77203 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cab44d67-077d-39df-b098-eaffdee9204b | -10.03154 | -54.32842 | 2025-06-28 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe59174b-1082-34df-b47f-67ad82bd2115 | -8.86711 | -50.16594 | 2025-06-28 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cd74634-3e69-3188-9d79-14ecac6e5a05 | -11.04546 | -55.37756 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7aba93ab-4a00-3c73-ab2b-afb592b99209 | -11.03868 | -55.37645 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f1379d26-767c-34f7-afa2-c754870abbf8 | -11.07738 | -48.25156 | 2025-06-28 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad0e06c8-9ce1-3a6b-b4fe-379cba1a1928 | -11.03988 | -55.3691 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 61b11b5c-2688-3aa4-bce0-078724a65687 | -13.9979 | -44.02787 | 2025-06-28 04:51:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13b459b6-76fb-340c-b464-b9df2b5e7e0c | -12.10099 | -54.58333 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49b59567-8622-3cf3-99d9-1a724fec4054 | -9.03549 | -63.98281 | 2025-06-28 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 530f4351-7c3f-3b11-ab77-8fb54d941f8b | -11.7815 | -59.31815 | 2025-06-28 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a5c6298-ee8a-3e01-a4d5-1fa4c3c793e8 | -10.83561 | -53.75755 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93a28566-cfcd-3add-bee3-53bd43a97c41 | -11.43981 | -54.46745 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c04667a3-af21-394d-94b3-e12024b76023 | -10.9504 | -49.25346 | 2025-06-28 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c23a641c-9734-3c40-b443-04d9eb590972 | -9.74179 | -48.33746 | 2025-06-28 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b87e5a28-6269-3bd2-af6e-4769e8848432 | -11.14373 | -53.93644 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c95af011-d6b4-30a4-8694-a2f4c1a2ac55 | -11.04487 | -55.38124 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 08f2a755-77b5-364a-bdab-2e9f3d8a8451 | -10.29922 | -57.1334 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b7ce68f-0dcf-358f-95ab-f76fcdb5dae6 | -15.42718 | -47.3778 | 2025-06-28 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12192d91-99bf-3303-b29e-da62877ca995 | -10.29628 | -57.1284 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8720e547-ab05-33e8-b57c-66f7dced10d5 | -11.0347 | -55.37958 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7574a4ff-eb66-3d4e-be9d-bb342c19c221 | -9.091 | -59.49332 | 2025-06-28 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bec168c-6fd3-36e6-a004-80f41fb66434 | -11.27456 | -52.74854 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15a6c87c-03cb-3f85-9730-c0b51037fe52 | -10.02934 | -54.3208 | 2025-06-28 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c9486ca-9842-3dc8-ba33-5bf5a7704fb9 | -9.71445 | -56.18165 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| de3914e3-6cf0-3644-992c-b70ade948662 | -9.5996 | -63.46825 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b7b7aa7-2f0a-3756-bc50-0070baad73ad | -10.83891 | -53.75809 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9f79e62-4298-312a-9a8b-36d6e8cb774d | -10.83946 | -53.7546 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a023adde-4610-3c5e-84f3-0fbd8e935831 | -10.60219 | -52.83952 | 2025-06-28 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37eed7bd-f55b-3cc2-aec6-a08a68c03582 | -12.10875 | -54.57735 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dac55603-69e0-3821-a23b-ca4ec6b7599d | -9.72085 | -56.18686 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e8e15c4e-da66-37f0-98d9-d0b932af05e2 | -11.88641 | -58.73895 | 2025-06-28 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95be6d0c-3d61-3470-8309-a6e5409a4f95 | -11.05657 | -56.74178 | 2025-06-28 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ca18dec-f027-3082-ac4e-c7330bfb12a6 | -12.10819 | -54.58089 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c5f3bcb-502f-3109-a451-70c5586c6809 | -14.19627 | -57.40508 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec3ff0e4-08fb-332b-bc58-c0fd8d561907 | -10.03602 | -59.35975 | 2025-06-28 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f457ea8d-f3b5-3819-9d23-59f27f53a65f | -11.80344 | -56.96032 | 2025-06-28 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe380c8c-2152-3d5c-b7c0-a8432ceed99f | -12.10374 | -54.58741 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c345cf00-83f6-32de-8fa4-5a9e0ed20269 | -19.63687 | -45.18974 | 2025-06-28 04:53:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ab914b4-71dd-3b17-adf3-d495b5593167 | -19.16751 | -49.14043 | 2025-06-28 04:53:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b4a8866-7433-3e34-808e-6ac69a41d5ee | -21.29709 | -55.93332 | 2025-06-28 04:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6099f180-00f9-339d-919d-a6fc01d37481 | -19.63119 | -45.18895 | 2025-06-28 04:53:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6668f53c-5179-3051-9073-73064563f2db | -20.30868 | -50.36838 | 2025-06-28 04:53:00 | NOAA-20 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 48f1178f-06d6-3959-b57f-a2857839ee12 | -19.02327 | -57.62323 | 2025-06-28 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| beb0f5c0-e6ec-3cb0-9c4a-b1cce9ea330d | -21.20467 | -48.51853 | 2025-06-28 04:53:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a62942fa-0ab7-370e-af77-0d0047c1bf05 | -18.42793 | -54.55785 | 2025-06-28 04:53:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9c34c5d-0816-3330-91a3-97f29266090f | -20.76311 | -46.76849 | 2025-06-28 04:53:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cf64dcab-58d8-3b13-9120-193232250e5f | -18.66004 | -55.74829 | 2025-06-28 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6d6a34ad-f7bc-3e11-bd37-149860bee69d | -20.76351 | -46.76849 | 2025-06-28 04:53:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 24127e8e-c6e5-30b3-b823-66a1eff482dd | -19.16371 | -49.13515 | 2025-06-28 04:53:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8067d1e4-4d29-31e4-9038-4be665f9b38b | -21.20527 | -48.51323 | 2025-06-28 04:53:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7770a1bf-7546-3d8f-be22-b65db5128ccb | -16.07901 | -53.74686 | 2025-06-28 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d56d64d3-2635-3f58-9b43-bf91c19b7de0 | -18.09024 | -54.27605 | 2025-06-28 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fa73ec6-f7b7-39fa-a095-87129dfa4b50 | -16.25516 | -53.67685 | 2025-06-28 04:53:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3ff0806-d038-3acb-a866-96777feea00f | -17.75171 | -52.43293 | 2025-06-28 04:53:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e97d8b9e-6c90-33da-8c72-ec412ca3678e | -16.25125 | -53.68 | 2025-06-28 04:53:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3163c594-0c8c-37eb-84a0-0893b6c9fd54 | -17.1542 | -54.00882 | 2025-06-28 04:53:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e5bbd02-e07c-3eab-8bf4-91f9dfcf7e39 | -16.25404 | -53.68427 | 2025-06-28 04:53:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e2c5882-9dee-3c20-b96a-6465f1cd8d21 | -17.13974 | -46.59966 | 2025-06-28 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd1d32d4-0369-3370-bee0-6b3cd4665a98 | -16.25852 | -53.67739 | 2025-06-28 04:53:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d188f0a-db06-3d7b-9239-7e9017a9808d | -16.2546 | -53.68055 | 2025-06-28 04:53:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 982b0a65-5f5c-3dd3-b38c-f589be91cb62 | -16.30209 | -52.9406 | 2025-06-28 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80da5647-5e83-33b7-80e5-360d8298ade8 | -17.1401 | -46.5966 | 2025-06-28 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 186e8869-565d-3b46-8d85-fa8449912b17 | -17.68815 | -54.00698 | 2025-06-28 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b10ad534-dcb8-34c5-b879-78167ea9b782 | -17.75526 | -52.43345 | 2025-06-28 04:53:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6734ab2-c475-3fdd-96f1-373dabd01209 | -16.25796 | -53.6811 | 2025-06-28 04:53:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c85e4d0-bffe-3613-baba-f6824e244a5d | -16.70371 | -49.35836 | 2025-06-28 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 41619bee-637e-3e13-a900-e85cabac2eba | -21.60784 | -57.5682 | 2025-06-28 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57d4bd61-61ed-3749-bd7c-2cb808e99404 | -21.60848 | -57.56436 | 2025-06-28 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74b7d455-2695-3027-a75f-591568f42393 | -21.61119 | -57.56885 | 2025-06-28 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9c61d55-7d92-3ea8-86ee-b7b235d91d05 | -11.0455 | -55.3773 | 2025-06-28 05:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| deae0064-c0af-3a6e-b7f1-6c90664d2ce8 | -9.7041 | -56.1843 | 2025-06-28 05:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| e86f2cff-386a-328e-9e50-c66e8626b8a0 | -11.2664 | -52.7527 | 2025-06-28 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 234f3031-4616-3abe-8304-cba1cea3f95f | -11.0455 | -55.3773 | 2025-06-28 05:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 662de983-cb1b-3b3c-b371-78a41bf5926f | -11.2664 | -52.7527 | 2025-06-28 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 8b011f34-bec1-3af9-801f-bba70cfa6484 | -6.9108 | -43.9834 | 2025-06-28 05:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 76baa4ff-00f1-3fd3-ae58-19a8b7d828e0 | -9.7041 | -56.1843 | 2025-06-28 05:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 732f9989-057d-3f09-a28f-6e2e10204b2f | -11.0455 | -55.3773 | 2025-06-28 05:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| e3cfbdbe-d773-38e4-a006-352ca6950b1e | -11.2664 | -52.7527 | 2025-06-28 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1d929c5c-0308-3a37-8a79-2f6b18e38dec | -11.0455 | -55.3773 | 2025-06-28 05:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 36ecb655-c235-3b58-a162-a058de52d6dc | -9.7041 | -56.1843 | 2025-06-28 05:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a1bfa0f8-d291-39b4-82d0-c816796c71cf | -11.2664 | -52.7527 | 2025-06-28 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 90b343d6-dada-3f81-9929-0d468a889054 | -11.0455 | -55.3773 | 2025-06-28 05:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| ad166bbf-bb4d-3302-84f0-773135f48031 | 2.75052 | -60.36603 | 2025-06-28 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdd76ea9-878b-37b6-871a-69f704525cb7 | 4.24331 | -60.63139 | 2025-06-28 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db2bd0b8-19df-348b-a82a-bd7e6b133be2 | -5.13693 | -60.36471 | 2025-06-28 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41d1db33-a692-3a2e-9bcb-4bb329a41838 | -3.87486 | -54.22995 | 2025-06-28 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72a3077b-1240-3033-bf98-328a013b0cf4 | -6.55823 | -54.98357 | 2025-06-28 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66a6c83e-827b-3c7a-87f6-08050d55707a | -3.87665 | -54.22685 | 2025-06-28 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 641c220b-4ca2-3e32-8053-9a4b6ecb6dc6 | -7.10784 | -52.58982 | 2025-06-28 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7baf6104-8d68-314a-92c8-426c758a17af | -6.5523 | -54.98357 | 2025-06-28 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4131fdc5-110f-3691-a978-7ed6e17fd9ef | -3.87546 | -54.22571 | 2025-06-28 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25ae5f3c-bd00-3c20-8dc9-6b83b45bbe05 | -6.54647 | -54.98269 | 2025-06-28 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 843f568f-ad99-3aca-86cb-4938ae77efa1 | -6.5524 | -54.98284 | 2025-06-28 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fad26f6c-0bfd-3302-adcd-894f0dc05595 | -11.04511 | -55.37005 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 223415a1-23b0-325b-af54-f4cde4ec0593 | -11.27346 | -52.75504 | 2025-06-28 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ff658341-28e0-3d73-99c6-7a843d144cbb | -9.72284 | -67.2494 | 2025-06-28 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c1be681-43a9-37af-925f-302f0fe33044 | -10.03328 | -54.33092 | 2025-06-28 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ade6399-ce4c-3f9f-b5f3-0f8ca0f09485 | -12.11175 | -54.58959 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README27.md)
