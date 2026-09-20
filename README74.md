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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d7726e7-87dc-35de-8fac-c60e93b52ea7 | -7.42995 | -44.75561 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b3a4ead-e9d3-33b1-898d-a8de5d06919c | -8.84575 | -44.91948 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 085f0553-5242-3ada-b660-4e88cf70676b | -13.02159 | -46.91397 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e82ba198-d957-35f0-84a6-e4abd9a99e7d | -8.16936 | -54.74649 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 353e2d7a-0e3d-3bd6-9b3d-217398802e2d | -6.3544 | -58.30832 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7652d944-5927-3325-bcf5-aeed7dc48fd5 | -8.65613 | -45.43993 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cf3fb55-5522-3ec0-b7fc-96d16def3dfb | -7.38171 | -44.72554 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d52921d-8fb7-39d8-b420-09df9d24c0f5 | -10.4734 | -46.2966 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 798e376a-3560-30e4-a7e0-0691f06a8776 | -13.39163 | -49.47215 | 2026-09-20 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe932566-a9b5-3458-b890-d427d35a5fad | -11.01791 | -48.32922 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b57f30f-e080-3728-ae7e-494c43e5df24 | -6.64621 | -47.73349 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c347f3fc-835b-3bb8-9e6a-72b0be5df356 | -5.75293 | -57.58159 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 995b0309-0a20-3ac7-8aeb-83278aa086b6 | -9.83814 | -46.43795 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c97acb18-6a34-3654-9807-8bfb49e57606 | -6.39578 | -55.25091 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 24a061d3-1926-3573-bf78-2d283295c5be | -9.83934 | -46.40622 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a31ee8df-cfd1-39eb-8b0a-2a7c930954fd | -12.13463 | -47.02679 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ccd48172-93de-38fa-831d-4c035af34ccc | -11.87729 | -50.04251 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bafc5bbf-451f-3cd4-9e66-2ba61396ea9d | -8.38446 | -46.51921 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c41bbbf1-3d63-32b8-9426-8518ee8a184f | -13.6124 | -46.92358 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e4731ef-405e-32aa-9c79-ea7b7ff6f9db | -10.30765 | -50.24709 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 552c6630-9fc0-3d2f-a846-c21220e49970 | -5.83612 | -53.52163 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15e9d8c9-1b37-3309-bff3-185f40b37dfb | -11.37677 | -51.40736 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 702979a8-1012-3c8c-a976-3b22cfe5bfb9 | -11.48907 | -47.75835 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5adb2569-1463-36a3-989f-0467e866e39d | -9.83296 | -46.44874 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 26ba36cf-09d1-3e13-a512-0857f5f54189 | -9.01761 | -44.92529 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d048401b-1921-3a92-aef5-ccb78bd96f28 | -9.90075 | -45.10326 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7116eb41-c6b0-3506-9c04-9072f5104148 | -8.14196 | -46.80146 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38976ff7-9a46-3d8e-aa5f-9cfb10a22c09 | -6.73147 | -55.07391 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00eb02b7-2dd6-3564-97ec-4933b7ede3bf | -8.7006 | -49.95963 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6068aaf2-168e-3e93-b6b2-b830e11ce201 | -12.73166 | -46.08592 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c70c85c-bb12-3e0c-b4cf-ab18ce6be259 | -12.53531 | -50.07127 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14f0a2e4-4a50-3c9e-95fa-6df1a133f76d | -11.86398 | -47.66169 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5069496-7b51-3348-b2df-52090d326eb8 | -9.90512 | -45.09933 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7426de01-091b-36a9-a8fe-3d4ac94ae4af | -11.73962 | -54.56399 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1feab34-ec03-3d53-8c5e-212e5d7c5293 | -10.32084 | -50.20852 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79fc8a5c-01b5-36e2-ac58-27a997a3c4bb | -11.48175 | -47.76096 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5d5bf3d-2186-3134-8539-2ef787010ab0 | -9.23215 | -46.23746 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61180981-f7ac-3ff7-8f99-edb916b61bf9 | -8.753 | -48.65277 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d77a87e2-516c-3032-a567-17f0d9a85bc8 | -10.13331 | -45.55688 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bd478701-08a5-3e72-8b17-28123de505fa | -8.66918 | -45.33032 | 2026-09-20 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa8137ff-9d92-3523-96bd-50c63fffbd89 | -8.36062 | -47.21657 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 926f11a0-5b68-377c-88a5-0abe28286d2f | -9.05166 | -48.76101 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88756d8b-7495-3725-aca3-2ab6e8945c63 | -7.04311 | -45.23119 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31ac8a80-015c-30a7-93d9-cd05741f62a5 | -7.02701 | -47.49445 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b28dbc1-5bb5-3e30-ad95-80bcacd3dde3 | -13.72784 | -48.79646 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 448aa209-0818-39f5-a16a-a3ad570d9488 | -8.36109 | -42.24238 | 2026-09-20 04:40:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cb6796cb-6c6c-35ac-b7d2-b71c61bbe24f | -7.53707 | -45.87902 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15b29808-99e9-3d21-bea5-6ca7e0cf8f74 | -12.8988 | -50.98973 | 2026-09-20 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcbd01de-e8cd-3eec-9e4f-385ce469444f | -11.45542 | -45.70213 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11c0eaf6-72a9-3eee-a660-5a83c38194be | -10.30883 | -50.23986 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36261127-4396-33d5-9b82-183126805d16 | -10.93194 | -48.31166 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51033afc-c5b4-35a5-87f1-9ef1b54ffe95 | -10.86242 | -56.17936 | 2026-09-20 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b9719abf-7ec6-3d48-bb7e-af7760543a0d | -7.06209 | -47.52868 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd9cbaf9-6d4c-3f15-a145-697f503d1772 | -10.88455 | -53.9851 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49596162-ec55-3433-8586-99698ea437fa | -11.12427 | -54.02177 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1c52902c-78d3-36d0-9fde-bc6e5ce2fcd2 | -9.57058 | -45.4741 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4edacb21-9bd7-396b-bc11-a32b2aecd671 | -10.77885 | -46.33123 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c4d28d2-6162-320f-a7b6-4c2206230ac9 | -13.03575 | -46.91561 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c1f9c95-90b3-3f70-814c-210493ebb2e5 | -9.78888 | -48.32852 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77ab051c-47fd-387c-a479-5a5e1269c5cb | -11.71432 | -54.56725 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e1255e4-3fc2-3969-a185-f3e4ea9cdffe | -13.21899 | -51.74414 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97032cdb-d255-3290-8479-e34f7942ade3 | -8.02881 | -49.54561 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3963da4-aeed-335b-b231-c7ac3778c7f8 | -9.09693 | -51.47121 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfc2a905-9e27-313d-a916-1723f748fc35 | -11.23713 | -48.38218 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 883cef7f-d7ea-3ad6-bf88-dfc823405513 | -7.37135 | -44.87043 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cb4b52f-10a0-322d-904c-0694f56c8e1a | -5.84218 | -53.51087 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c2979aa-1743-3223-ae69-9625195261fe | -10.08209 | -45.84898 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba7e4694-b955-333c-9621-cd0ca1637ab6 | -9.2404 | -46.1828 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 891ce9bd-866e-3b5d-b34f-81e6ffb59e16 | -10.09752 | -48.43927 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b44871bc-b8c8-391e-a703-77c7d03b1a97 | -7.59976 | -46.72977 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f3201b6-4d60-3ae1-a129-8cdb4d01d5b9 | -9.89483 | -46.53355 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a6fc58d-0be8-3835-b33e-031bbaa42517 | -9.77372 | -45.06505 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 991d8922-1000-3dea-a197-9ccea4a8c080 | -11.01458 | -48.3287 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca8ea5a7-37f6-3aa5-aafd-18703fb9e391 | -5.8819 | -52.05133 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35976276-93bc-3b6a-98bb-1fc5513aa9e6 | -5.8428 | -53.50709 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4ad0475-1a3d-30ba-b91d-02eae178ff98 | -12.87814 | -51.0014 | 2026-09-20 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18ca4af3-4add-3c1a-92fa-90376c7c4140 | -11.8555 | -47.6717 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1c55f853-0f29-3a34-abc2-73c8e779dddc | -7.1625 | -47.42939 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f53236fd-dcb4-33b3-ab4d-a42b51bfe5db | -11.2238 | -48.35827 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 222abb65-3d94-35c9-ad18-50d8e401bb5e | -6.66253 | -50.93644 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48f82366-08a2-3800-89f3-f2ad79c8fcdc | -10.20347 | -46.57422 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3f94643-005d-37bb-bc42-80157422218e | -12.69252 | -45.94107 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09013ee4-6565-3d43-ba86-9f2c792eb859 | -9.93509 | -60.73061 | 2026-09-20 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7f2a1df-9b2c-32b1-8a3e-ffb258b6593c | -10.30146 | -45.42845 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0abd11f5-4470-32d1-b54c-6698cc0af62e | -9.70426 | -54.83422 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d00d81cf-e322-3b43-8265-bb4d2fab1c15 | -7.41103 | -49.84438 | 2026-09-20 04:40:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 870bda2b-b762-30b7-a13d-696a4ccc7ce0 | -8.17882 | -54.74382 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 945f222e-fb85-3c27-a086-b8aa04d52805 | -5.85029 | -53.57028 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22455931-85fc-3460-8d5d-99e002bdf22c | -9.97263 | -46.57213 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12b10653-4c30-3829-80de-54b474674964 | -10.41174 | -48.94503 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fd19b4d-5e74-3629-84ef-c5b20d7d434d | -12.99637 | -46.91406 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6d1358e-54e5-39b1-aa61-6d9f62b5983b | -6.46605 | -48.44257 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81c9f472-34e5-3c5c-a475-dacaa8a35a91 | -5.87292 | -52.0351 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20c69420-cf43-3972-8fef-772f2e5a7327 | -5.83967 | -53.52618 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bea5d8c-b5ca-3081-892d-714fe0ca3b6a | -13.95988 | -47.84602 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf384e59-4e26-36f9-bc90-20cbd284466f | -11.04612 | -48.29704 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8d09a9f-c745-3c1c-b111-62ab2e1da215 | -8.34785 | -50.8528 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b34453a6-7624-36cf-b88e-87f07beaf1af | -10.26686 | -48.11592 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02422f2d-1eeb-32f7-81ba-665545967720 | -11.01364 | -54.15032 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 264cff07-65a9-30da-851f-e79d04888383 | -9.22923 | -46.23309 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README75.md)
