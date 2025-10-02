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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 576fc169-4f1e-3bc8-a509-47795cfad8b5 | -14.9924 | -46.9091 | 2025-10-02 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c1557ae1-49d9-38a2-b3d7-e9f3a266b308 | -6.6955 | -48.7062 | 2025-10-02 01:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 85.6 |
| dcc5ba40-b7e2-396b-ae44-7a27807796c3 | -22.5728 | -46.7997 | 2025-10-02 01:00:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| 2dfff8b5-d896-3ec6-88a8-57e7160a102c | -16.0426 | -50.8522 | 2025-10-02 01:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 7f334520-4c16-35df-a821-dcf38580473b | -14.4255 | -46.115 | 2025-10-02 01:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 958da0fd-f5b7-3c50-aafb-ccc030ec3151 | -14.407 | -46.0722 | 2025-10-02 01:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 05f72563-6c83-3809-b340-95e6e1e8f3c6 | -13.0119 | -45.1988 | 2025-10-02 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 053deb16-ea44-3fed-b1ed-729f52ef4011 | -14.426 | -46.0919 | 2025-10-02 01:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 695de100-1d86-39dd-b67a-faeb5f641802 | -12.4207 | -54.3536 | 2025-10-02 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| f529e558-fd29-36a7-bdce-b93c7ef8ca48 | -13.4055 | -47.7974 | 2025-10-02 01:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 1f895b6e-a33b-34b3-9dd5-d031956b4b40 | -10.6622 | -48.5123 | 2025-10-02 01:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a7b6e8fa-1e14-3f74-8458-26986dcf2e9a | -14.4065 | -46.0953 | 2025-10-02 01:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 790bca94-f5a7-3728-a5b3-92d75a25d47a | -6.7213 | -44.1387 | 2025-10-02 01:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e81fcf44-93f8-39b3-9870-717af57c7577 | -4.3713 | -43.0105 | 2025-10-02 01:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e9322d98-6296-3ab9-9100-8939876b6f3d | -7.7941 | -42.5369 | 2025-10-02 01:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 8efde4d6-a9be-33f0-8120-024c09dc5db2 | -13.8637 | -51.2517 | 2025-10-02 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 8c71c8ec-2fd4-3fb8-858a-f3c1e3bcf5ee | -13.4059 | -47.775 | 2025-10-02 01:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 65b58c90-4798-31e0-a9a8-b64eabdb035d | -22.5518 | -46.8053 | 2025-10-02 01:00:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 3ed70255-e7bb-3964-b97b-3f2d6db17850 | -13.1546 | -47.8345 | 2025-10-02 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f79af80f-4887-398b-9e7b-5a96c9265631 | -7.7752 | -42.539 | 2025-10-02 01:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 179.6 |
| ce18a88e-3436-3f9e-a920-20fdc5bfbdc3 | -10.6432 | -48.5145 | 2025-10-02 01:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6ecf68b4-fc55-3cbb-b7fe-0d24cb6e1492 | -7.7755 | -42.5152 | 2025-10-02 01:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 133.2 |
| d0a8d986-257d-3b94-a130-f765fdf435d0 | -13.0114 | -45.222 | 2025-10-02 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| eeb136d8-4058-3330-b575-1fec51e43da6 | -6.2411 | -45.3198 | 2025-10-02 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 3d5b5569-d935-3be5-85f2-27584b854c1f | -5.9856 | -44.6118 | 2025-10-02 01:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 90212876-eba3-3684-8666-4768de0124c5 | -10.8237 | -46.6088 | 2025-10-02 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 3981b8df-8573-3643-8148-d87e49106b35 | -13.1542 | -47.8568 | 2025-10-02 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1c561d1d-4019-3c11-b7f9-a45cc9561b49 | -7.7755 | -42.5152 | 2025-10-02 01:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| e119060b-3bf1-3d37-80fd-fd6756e691a4 | -6.2408 | -45.3424 | 2025-10-02 01:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 74710094-9ecc-3f2f-b4ff-a7e8b7cd4f8a | -5.9856 | -44.6118 | 2025-10-02 01:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 56f56680-676f-33ac-a2ab-52a661973ef1 | -15.2542 | -49.3104 | 2025-10-02 01:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 42.9 |
| e1f783b3-ac70-3507-ad83-5a8c83e74514 | -15.2547 | -49.2883 | 2025-10-02 01:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| cc00f6ee-bd36-3453-81b8-8fca20fffeb2 | -14.426 | -46.0919 | 2025-10-02 01:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8ff08a51-cb0f-3072-b385-ef3836a85268 | -14.9924 | -46.9091 | 2025-10-02 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 69d0b87f-7da8-3d27-88e3-e3d65e42f3ef | -13.1743 | -47.8093 | 2025-10-02 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a23ccbe0-5286-3dce-b008-7eb6444abba9 | -7.7944 | -42.5132 | 2025-10-02 01:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 035ecba9-6689-3568-815e-5b023f34997a | -14.4255 | -46.115 | 2025-10-02 01:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| def01a77-7619-3195-afec-24c795c4b83a | -6.6955 | -48.7062 | 2025-10-02 01:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 92.7 |
| be857008-e07c-3133-bb89-c484c77901e6 | -5.986 | -44.5661 | 2025-10-02 01:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| c6f09223-64d0-3518-bef7-8f1878f6f087 | -7.7752 | -42.539 | 2025-10-02 01:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 159.6 |
| e8b8467e-701d-3f56-aba1-5c05b19dc715 | -5.9858 | -44.589 | 2025-10-02 01:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 4c1e422a-ad4d-3c4f-acab-574bd2466964 | -14.4065 | -46.0953 | 2025-10-02 01:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 662891f3-9b3e-30bf-aaa4-0081cab9fedd | -14.3704 | -45.9634 | 2025-10-02 01:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 9c6ce54d-b977-3a56-a3c1-95dadfbd2426 | -14.3119 | -45.9736 | 2025-10-02 01:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 31aafa31-4e6c-34ab-861a-b05387bf800a | -10.8237 | -46.6088 | 2025-10-02 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 7ac5b72e-488d-32b4-b2b9-3932fa47c48f | -12.7002 | -48.5637 | 2025-10-02 01:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 39571e39-b6a7-3349-8fa7-fba946411e35 | -9.9361 | -43.7891 | 2025-10-02 01:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| f043a93f-2e52-39a3-b12f-18ef56e9ab84 | -13.1546 | -47.8345 | 2025-10-02 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| b75ebd16-7f81-3ec2-a0c3-60eac2407bca | -13.1739 | -47.8317 | 2025-10-02 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f8471264-e4c0-38f9-8f9a-53ff59a67d28 | -6.7213 | -44.1387 | 2025-10-02 01:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| baadb3d6-03ed-3c96-8943-649ffda03ca1 | -7.7941 | -42.5369 | 2025-10-02 01:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| af673b63-a071-38c6-9053-b28c32b6407d | -6.2411 | -45.3198 | 2025-10-02 01:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b6afab07-514a-339f-9af3-cefa46beeaa1 | -14.407 | -46.0722 | 2025-10-02 01:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 3ea5e081-29a7-3d80-b377-772adc147579 | -22.5735 | -46.7755 | 2025-10-02 01:10:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.2 |
| 61350616-6218-3650-b51d-50caae09d877 | -12.2777 | -45.3603 | 2025-10-02 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 618c451d-f3ab-3199-b6d0-e84a8dc70032 | -5.9858 | -44.589 | 2025-10-02 01:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 2ff5cb07-411d-31f8-888c-1c26b1713099 | -13.1542 | -47.8568 | 2025-10-02 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 810e1ffc-ec87-33b4-a5fc-bf961a9b976f | -14.4065 | -46.0953 | 2025-10-02 01:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| be3f23b7-8755-3fe5-a982-6fddd6a4cb2c | -10.6802 | -48.5758 | 2025-10-02 01:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 3b4c84b9-51a6-34c3-98bf-e8b8a46ee8b4 | -12.4737 | -47.2621 | 2025-10-02 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 47ed1b93-d07e-3900-b5a1-98bb51a97df5 | -13.0114 | -45.222 | 2025-10-02 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 81a8b6ea-e7df-382c-8ad4-69f6de7f41d3 | -13.1743 | -47.8093 | 2025-10-02 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 6dfa3879-6d20-3cbf-85d3-e6a64e5fea57 | -6.2411 | -45.3198 | 2025-10-02 01:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| d2337e4a-e61f-36cd-822b-d8e152ed5d4b | -9.957 | -43.6693 | 2025-10-02 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 25430845-920e-3892-8743-27553230aabe | -7.7752 | -42.539 | 2025-10-02 01:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 223.4 |
| a96f64bc-ea13-3b09-9315-5846b3f71bf3 | -7.7755 | -42.5152 | 2025-10-02 01:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| ed1d35f7-a19c-3a09-b682-fd0c43a636d4 | -14.4255 | -46.115 | 2025-10-02 01:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 9224af7d-b002-3e52-aa53-58deec18cb2d | -14.407 | -46.0722 | 2025-10-02 01:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 145cbf5a-2ba9-306d-88e2-f01042f2d5a3 | -14.426 | -46.0919 | 2025-10-02 01:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5d67c671-479f-3d03-92ac-50fd383e9100 | -13.155 | -47.8121 | 2025-10-02 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2444829a-1ea8-3246-a11e-b761adcc6c51 | -13.1739 | -47.8317 | 2025-10-02 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 564abd87-7e6e-3bf3-93f6-eb715da9793c | -6.6955 | -48.7062 | 2025-10-02 01:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 72.0 |
| eceac8f7-6a90-393e-8db8-8d15ebd5ddec | -14.9728 | -46.9125 | 2025-10-02 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7d9abb58-8557-3501-9fb8-af5a22f5b552 | -15.2738 | -49.3073 | 2025-10-02 01:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7812fdb6-856c-38e2-8b02-9a7a956fd0d6 | -13.1546 | -47.8345 | 2025-10-02 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 50c69aca-c038-3367-a859-d3bb96cf7756 | -13.0119 | -45.1988 | 2025-10-02 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 1ad43ee0-f34e-3594-b675-984df32a681f | -6.7213 | -44.1387 | 2025-10-02 01:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 7c49a2c0-ebba-311d-a5ca-d97dae7f4bc9 | -7.7941 | -42.5369 | 2025-10-02 01:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 0a181f5a-3d24-38ff-ad73-7a5764f060ca | -14.9924 | -46.9091 | 2025-10-02 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 21a70380-6b57-36b0-af95-f86ae7eed2d8 | -12.4207 | -54.3536 | 2025-10-02 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 827ba385-bb4f-3c6f-a820-944cc12f19df | -13.8637 | -51.2517 | 2025-10-02 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 9825a323-ab96-3b0c-ad3c-23e5c9dd8ea4 | -7.7563 | -42.541 | 2025-10-02 01:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 105.7 |
| c0db34c0-67c0-32c8-a616-2726362d67d4 | -7.7755 | -42.5152 | 2025-10-02 01:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| 1fcb52e5-6db4-34b6-b212-436bcc697967 | -6.2408 | -45.3424 | 2025-10-02 01:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 7b7ecda5-3ff4-36b4-80a5-92d925934481 | -14.426 | -46.0919 | 2025-10-02 01:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 104.4 |
| cfe1bfd7-d9fb-3249-add8-5ab993a596bc | -15.2542 | -49.3104 | 2025-10-02 01:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 4684c0bd-b9fd-30ef-b2c3-40cdb647c743 | -14.9728 | -46.9125 | 2025-10-02 01:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 11097a5c-322c-385b-a2b1-6cc4ab3f90d0 | -11.8755 | -51.2173 | 2025-10-02 01:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 9bbd3429-a745-3355-9b58-fba40b187475 | -13.8637 | -51.2517 | 2025-10-02 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| ea51d4fd-c27a-3778-954f-4226871ede43 | -14.407 | -46.0722 | 2025-10-02 01:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 08a20873-bd48-37e9-992b-28f718fac275 | -13.1739 | -47.8317 | 2025-10-02 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 0f834a60-639c-303b-b36f-2c693b987e0f | -13.3085 | -47.8341 | 2025-10-02 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 819a0e58-19bc-3cc6-9cbf-2bd87f683fb5 | -7.7752 | -42.539 | 2025-10-02 01:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 223.9 |
| 95068790-fb67-372e-822e-29b90dd3a71b | -11.8752 | -51.2386 | 2025-10-02 01:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| fac222d5-4bb2-3ec7-be49-be6bf4ba6ccb | -13.155 | -47.8121 | 2025-10-02 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 3b700820-a784-3a3d-8fdd-42f432b5e933 | -13.1546 | -47.8345 | 2025-10-02 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 7edcc315-7b1a-3b76-935d-3b23db31902c | -13.1743 | -47.8093 | 2025-10-02 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 465c9d86-958b-322e-9575-fdd7cb19bea5 | -7.7563 | -42.541 | 2025-10-02 01:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 194a1d61-34fc-34f2-ba89-4652cbee1812 | -6.7213 | -44.1387 | 2025-10-02 01:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 96a35352-cf07-33a4-9f7d-d2ca71703941 | -5.9856 | -44.6118 | 2025-10-02 01:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |


[Clique aqui para ver as próximas entradas](README13.md)
