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
| ebaab577-4b76-39bb-9ce6-c76189e73152 | -7.0214 | -44.55994 | 2025-06-26 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae16beec-eba9-3f6d-9d8d-b9e58469b1e9 | -8.68127 | -49.95072 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dadf0f23-87fe-3ded-ab58-2276af8df1c2 | -10.07346 | -49.65675 | 2025-06-26 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5b34417-ccaf-3148-a326-803869146634 | -12.03117 | -47.77712 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a840594-6cb7-3f4b-8039-76dc0547cb25 | -11.28036 | -52.46394 | 2025-06-26 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 161ed256-a93d-3b47-ba83-f194e7d33581 | -6.18171 | -48.08039 | 2025-06-26 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2fb26f87-8d02-3532-bcb0-55abe340f4eb | -6.29032 | -47.0169 | 2025-06-26 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94d5c729-1276-3f5d-bd01-dcf00767cae6 | -11.5678 | -52.09658 | 2025-06-26 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09303310-7f5c-3db6-9b69-361d679c94d2 | -9.87555 | -48.44748 | 2025-06-26 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00377fa0-3ff2-3033-ac5d-23c2f14e1e15 | -8.53577 | -46.32801 | 2025-06-26 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3cd4c8f-b283-3e1f-9819-b69871c02ccf | -12.51221 | -44.08844 | 2025-06-26 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba8eea1a-2332-3161-9e3f-51eb321c68e0 | -11.24075 | -49.48951 | 2025-06-26 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8def1db0-29d5-308b-8ac1-1228a51c2aa8 | -10.23475 | -47.45857 | 2025-06-26 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 048c6881-0d62-390b-97b1-6afcd7e16b89 | -11.82274 | -47.55272 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3253520-ba54-3ab3-88df-37645962697d | -9.872 | -52.43789 | 2025-06-26 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0e94edf-9c76-367c-b999-b65772e8e0a9 | -7.1122 | -47.84523 | 2025-06-26 04:40:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f47b40d6-c9e6-3a21-86ec-768a41eaf313 | -7.19867 | -43.09015 | 2025-06-26 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c79fa595-32b9-3fc6-87fd-67cb9489e14c | -12.02923 | -47.77443 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4fb84fbe-7d05-3087-9e5e-8e22cfa504aa | -10.07014 | -49.65623 | 2025-06-26 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d531f083-3e63-3f3c-9207-4969a5f12132 | -11.91046 | -54.82095 | 2025-06-26 04:40:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34891116-16f3-3ac6-8073-644896820434 | -8.85677 | -50.15604 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85d191dd-20cc-35fd-adc6-04b61af45aa4 | -9.12041 | -49.44219 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ada53f09-d87e-3db3-9ea9-819c17329237 | -10.65296 | -44.48906 | 2025-06-26 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0655691e-381c-3941-a2d5-e273138ee938 | -13.04661 | -48.82377 | 2025-06-26 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6796eb5-3d64-38d3-b42a-81b60dfbc80a | -8.32942 | -49.23532 | 2025-06-26 04:40:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e07f692a-46f6-359a-961c-8311d3489f3d | -10.29742 | -57.13622 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e88c724f-c8dd-355c-a180-98928341392d | -6.18166 | -48.05831 | 2025-06-26 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bea96d08-771e-3c91-b89b-34476f74b6b7 | -11.56903 | -54.31498 | 2025-06-26 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 202513b6-30bb-3ec7-b3be-ff9abfcdb9c1 | -12.55414 | -52.24534 | 2025-06-26 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35b3d771-2bca-32d6-aaeb-a65224a8091a | -11.58272 | -46.91332 | 2025-06-26 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b7b3703-8d0a-32ac-b5d0-f90d496e4a0f | -11.82749 | -51.25554 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 590bb0dd-3aee-3381-b7d4-03d752019e4b | -11.06542 | -55.38305 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 45b542cb-9d6d-38a0-853c-a5015f7926af | -10.65533 | -44.49163 | 2025-06-26 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a16a9f87-4a82-3fce-adcc-da8fe142cb64 | -11.81311 | -47.54277 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b4ceb8d-61e8-340a-9d5e-76a88869aa83 | -8.11949 | -55.0732 | 2025-06-26 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d184555f-0a3d-38e6-8df2-c601290315f2 | -7.31981 | -45.75179 | 2025-06-26 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba8aa777-e738-3a93-aedf-01e8ab96d9e9 | -7.09251 | -49.16327 | 2025-06-26 04:40:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9c999b8-f697-3a31-a933-f5e492aeb266 | -11.07716 | -46.63531 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa718427-b75e-3ee7-8c8c-13f82b4a8570 | -9.32655 | -47.82584 | 2025-06-26 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 307c9277-4c79-3ba0-a644-4f7d975fe854 | -9.23955 | -49.30924 | 2025-06-26 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00a40eb3-5059-3fa2-a09f-838e046e89e2 | -9.79347 | -57.42755 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 119fe4f0-55d8-35b1-b370-6788b7352f09 | -9.50246 | -56.09797 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| de19fdf8-ad15-3963-b2d1-2666211a1032 | -10.50906 | -47.20518 | 2025-06-26 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab268045-c88d-31d2-ad8a-7c27357a63bb | -6.1811 | -48.06195 | 2025-06-26 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c63b44f0-ff65-37b3-94a3-56ded2c9bec4 | -10.50823 | -53.58589 | 2025-06-26 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 244dd305-aad6-3298-ad18-c2b64e2b10c3 | -12.4952 | -45.90142 | 2025-06-26 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acb31262-3ec6-360f-9fc9-d9e58f7a5853 | -10.24813 | -44.6348 | 2025-06-26 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddb06c31-aeeb-3d92-bdf9-83fd12e07463 | -9.8855 | -48.05349 | 2025-06-26 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1de03f4c-d806-3c12-9929-5b22d0eb1095 | -7.97894 | -49.65424 | 2025-06-26 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58919864-6a9d-3eb4-965e-2648883e1db8 | -9.49923 | -56.09267 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7302aa3c-96f9-3ff9-ae36-128ab10c83a8 | -11.36455 | -48.70744 | 2025-06-26 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b0c906a6-10f1-3420-95f9-f9deab779866 | -11.81269 | -57.35069 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9803ce3c-92c8-312f-8cda-2583ef72b019 | -8.80035 | -45.00733 | 2025-06-26 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20e998bf-8477-363e-9a68-3dc36c231b75 | -11.95832 | -47.02409 | 2025-06-26 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c40c34cc-973a-3f55-b84f-c818f207091c | -11.83804 | -57.8579 | 2025-06-26 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e24594c-e806-39e2-9969-fef317f0abd8 | -11.26739 | -52.45796 | 2025-06-26 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d26a4f27-e508-36d6-a62c-2a7b18e7ee32 | -11.06989 | -55.07248 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 214033ce-c214-3346-ba3a-6267ec093461 | -8.2579 | -47.02395 | 2025-06-26 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff81661a-ae68-3398-baa9-fbbb407a9879 | -10.86201 | -54.29882 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aa23355-5ae0-3102-8b04-75c762c07c22 | -11.14039 | -53.93689 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f439b452-5519-3c6a-94ad-374745feb092 | -12.02291 | -57.08635 | 2025-06-26 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| be10b5b1-ea70-32e9-85b4-82f08dcdc770 | -10.86898 | -53.78116 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d8eb4bf-f4ea-3936-8c87-8502988b68e6 | -12.02648 | -57.09133 | 2025-06-26 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6bdd0a3-01b2-3e4a-ac80-cfa88117002b | -10.27714 | -47.60972 | 2025-06-26 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e034f39c-c496-37b5-b482-caa264f7cc82 | -7.10082 | -49.17522 | 2025-06-26 04:40:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eed746ae-86d3-3d2a-a4f3-2eb8d249e854 | -12.21663 | -51.46367 | 2025-06-26 04:40:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ea9e50f-96d8-33b7-b1ab-5ae62c62719a | -10.16508 | -53.92838 | 2025-06-26 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b56d801f-a31c-352f-816f-18d665f916ed | -7.3648 | -46.22784 | 2025-06-26 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f959b70-ca74-3e9d-99a0-bf17a7eced57 | -11.83097 | -57.76878 | 2025-06-26 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e27c0138-579c-3a96-8d65-2bc9c271018c | -9.49891 | -56.09328 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1ff8be88-be66-325c-86ca-ca8f83e1f77f | -11.8143 | -47.55998 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 58d71e7a-f81f-31dc-9d6b-8497fb77c295 | -9.7943 | -57.42283 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a6e2956-b4a8-3421-9992-f7e69834e821 | -7.31398 | -45.76505 | 2025-06-26 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9968a06d-7879-3904-93ce-16ba95ffee38 | -11.61386 | -46.5048 | 2025-06-26 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1bfe70b-8e5b-3a9b-9912-6f052277e2d4 | -9.11933 | -49.44921 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e66ac3cd-e467-3290-ba53-9b3d6a96cdbd | -11.86889 | -54.6976 | 2025-06-26 04:40:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16964ba9-ad00-32f3-9414-e9d13cdde132 | -6.1778 | -48.08345 | 2025-06-26 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 88ae1b92-f46e-385c-9cc7-2583f382cf94 | -9.24009 | -49.30571 | 2025-06-26 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a30b59c4-cfdc-3826-af6c-b600d4116505 | -12.76563 | -44.40894 | 2025-06-26 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6b33517a-65c5-3a8c-8a04-8c8369805a4b | -10.06811 | -55.55051 | 2025-06-26 04:40:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b64bf603-11d1-3d89-b96a-c68a9eefa232 | -10.29704 | -57.12975 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01da6278-3dd2-37a4-8e15-153972cd2cb3 | -9.51048 | -56.10275 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 268b4ec3-dc39-3de4-af6d-447c2a04b2d6 | -10.82136 | -53.73415 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2c853a7-eead-31f9-90a3-c977e10a9598 | -11.99315 | -57.20341 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3720279c-1072-39c3-98e6-2e27634ef769 | -10.41875 | -47.50939 | 2025-06-26 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a2213276-1ef2-39e0-b2e4-65676cb4b890 | -11.27078 | -52.45852 | 2025-06-26 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 895915a8-1434-3e7e-80ac-912441e1b8ff | -10.62368 | -48.08163 | 2025-06-26 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e9e49d9-5b14-353f-b303-13ee895347b0 | -10.50107 | -53.58471 | 2025-06-26 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a19eb32-2920-36df-a543-8f240c8dc4e0 | -11.15476 | -49.69957 | 2025-06-26 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d1d9a4e-9f98-3d25-adca-782c2e09186e | -10.50396 | -53.58946 | 2025-06-26 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cdb9515-ce6e-3de1-8760-f606e606c82e | -10.81707 | -53.73769 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a707a419-27a8-3837-b547-53e7032a4f77 | -12.80397 | -48.73291 | 2025-06-26 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1ce232e2-fd10-35bf-9d45-300d06d02e24 | -6.87517 | -47.23778 | 2025-06-26 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2aa1863c-9787-3cbc-b102-983be916eb4f | -9.48056 | -56.07377 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bfc3add-c8d8-38cf-86c3-daa69039a692 | -7.02086 | -44.56373 | 2025-06-26 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e3590df-b3fa-3afc-80a5-0bbf7f04b904 | -9.50275 | -56.09734 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6422d1af-2bb9-3e1c-bd31-65a770b2b36d | -9.33003 | -47.82636 | 2025-06-26 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d69d33b5-61eb-366a-89de-a7abdd118a9b | -13.03855 | -48.83042 | 2025-06-26 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24d04a76-4c79-3641-91af-1fa192079c02 | -9.50961 | -45.42938 | 2025-06-26 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8da00840-f9e2-38d4-8723-bb8166a400ae | -10.2982 | -57.13177 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README13.md)
