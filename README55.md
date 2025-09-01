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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99cd0e41-da57-329a-8610-1a1a2ccac860 | -7.06767 | -44.34843 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bf45eca1-0d93-316d-91f2-40f9585dfd72 | -9.66432 | -47.80792 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a040365-8c53-306e-bd3e-4367842191c5 | -8.84573 | -47.50583 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bae13f47-3bd4-39f8-8f9a-1a54da23f857 | -7.10878 | -44.77272 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f640152-405d-3802-9e11-c3a82aa8294d | -6.19152 | -43.34005 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac6b202b-40ed-38d8-bed8-9972c0bf213b | -6.30545 | -44.76669 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba27a0c1-f23b-376f-89a8-f6283e577d90 | -6.7491 | -43.78918 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bee79f28-e3a0-335e-aa7f-d5893f7cc851 | -7.45938 | -44.82616 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8ba147e-ffa2-3057-8c4f-b913e52c91ee | -5.35017 | -45.77938 | 2025-09-01 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75ebe966-12ed-3c08-945e-e1f1f2354517 | -6.94196 | -42.01374 | 2025-09-01 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d50324ab-37a2-3fba-9c84-99410cbbe7f0 | -5.96276 | -42.96281 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03754751-6d20-3776-9893-fddd827bb8ad | -8.92027 | -45.8697 | 2025-09-01 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92888a35-8450-33de-ba25-cea338d85bd9 | -6.28267 | -43.56629 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b10f7bc3-f92d-3ce4-a47e-127814732dec | -9.41166 | -48.18882 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67f0da4a-8553-36bd-80e7-5f0ea8e7d5cb | -9.66373 | -48.0748 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1ad1410-0ffb-3651-bbdf-4966be735b28 | -5.9902 | -46.48642 | 2025-09-01 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb1f0862-5cd7-33b3-a7f7-b013b43e0c16 | -8.84797 | -47.51341 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dafad021-3e22-312a-9e2f-8917b37be878 | -6.64625 | -43.95811 | 2025-09-01 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0965095-2385-3438-b218-367119f2b268 | -6.83028 | -43.32752 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 607761f9-f043-385e-b2e3-8f827b44cdc0 | -9.14139 | -47.9421 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d08d87e1-c6f2-3157-81c9-572a30eba2d5 | -9.59224 | -48.27147 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0326e467-0957-3d33-8c4a-3b43c1f7b2d2 | -6.46314 | -42.43656 | 2025-09-01 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c27f2167-3439-3c4d-8b3c-4180cc3b7c8a | -6.8333 | -52.82156 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c83862d6-e3cc-3aa1-b3ca-931917476369 | -6.23568 | -43.3921 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92f87fb7-85ed-3be1-a084-2d9271896374 | -10.04235 | -48.0842 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ecc76001-22a8-39ba-8e8c-a5bcc0a20abb | -7.09068 | -44.34713 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| c71397a7-7930-3a7e-97b7-30f1f08a8d8d | -6.27147 | -43.53496 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30e4e51e-ed79-3f66-994c-b288eeb00620 | -6.36753 | -44.45943 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97d16c75-7cde-3843-bdbe-634ad7f2bc8c | -4.24972 | -48.54757 | 2025-09-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4de5f1a1-dad3-3253-8cfb-be55763cb6ab | -9.15634 | -45.21748 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fb1c5f7-e91c-3a04-9b28-55697ff01ea0 | -6.34623 | -53.43068 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5015fb86-0682-3f13-a2dc-3c5d9aa45928 | -7.98771 | -44.06002 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52a2e446-1ec6-332d-a637-26a5aad83c0b | -6.17485 | -43.31609 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e8e6b85-4c01-3aa2-a983-3dda224f5077 | -6.95708 | -44.33781 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 696eaf4d-0a54-3039-8750-edbc141aaa2e | -11.05757 | -44.64483 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92b06323-d30e-3c5f-a249-13b4505dc6ce | -5.43451 | -49.99415 | 2025-09-01 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6cda99a1-ed32-3f21-8f4d-126840b3ee2c | -4.92768 | -43.18368 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36f462a5-fb2f-32c1-8adf-ea7d61347669 | -6.54639 | -44.58607 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e620612d-98ce-3648-84de-56036dc7aaed | -8.82208 | -47.83386 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92292192-8414-3510-8657-96ffbddccbfa | -5.61878 | -45.14153 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f0f280b-a60c-31a1-bf9d-7d94f36c869f | -5.79445 | -45.41361 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 287fe923-0e66-3ba7-9c8f-d55c258b2611 | -6.5363 | -42.95908 | 2025-09-01 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40ebfef5-ed10-3583-82a8-882f80700322 | -8.82312 | -47.80531 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f804c85e-f1fa-3c01-9021-08bbf80aafff | -10.60745 | -44.32709 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 6bd141a6-9155-3e9f-98c7-3bd20b81c5fc | -5.114 | -43.22616 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5859c15-8eb4-30f8-b2b2-d2c27e605003 | -6.18986 | -43.34879 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00538e25-cc91-3864-9602-de7b0d2c9418 | -6.26343 | -42.61364 | 2025-09-01 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7717fd01-742f-3a70-bfcd-93c9778bf081 | -9.14802 | -47.94316 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58c0b247-1d30-3062-8960-b0823ca1545c | -6.37764 | -43.54745 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5e506b0-c0e7-3ca9-aed0-7a2ed1532d3d | -6.87387 | -44.32317 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b6ba22e-af48-3307-b5c1-ff607416f07f | -11.08773 | -44.61226 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c7c8f12-2570-37bc-b1a6-a280955d423b | -7.95348 | -46.3587 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd56cdb7-f95c-3539-886c-1aec7963c9af | -6.87283 | -45.14283 | 2025-09-01 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c39bc1a9-4a00-38c6-892f-3594dceb78df | -9.66377 | -47.81145 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e7af572-3ae1-3010-b92e-7db39eafaa8e | -7.85311 | -45.23442 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc2eaca6-0bcb-36b3-9033-914fa310c4e8 | -6.57196 | -43.69852 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d43c7dd1-4a88-35a0-9e67-b7f300222096 | -5.96225 | -42.96625 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 966daed7-1195-3aa1-af8d-ac618de34090 | -10.0418 | -48.08775 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1215bbf1-b41d-3765-a6e0-72f3789db01b | -6.1477 | -43.33745 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78813080-4f85-3063-990f-98a0f2c32565 | -6.81348 | -52.81805 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aacc2334-a2ea-3dae-a5a1-009166e9e8c3 | -11.08558 | -44.61441 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eac90955-3fae-35eb-bfa4-c8d4626866f8 | -9.51439 | -48.89515 | 2025-09-01 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ff69692-27f2-3295-95c7-7f4cc93593f8 | -6.51162 | -43.56046 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1034a8f1-a954-3521-8b3e-b028c084e494 | -7.54969 | -46.11441 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be699aa4-bcd6-35e9-b1f6-29afd38cc261 | -9.64001 | -47.81502 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9a0b405-cb9f-3248-aef7-2e84ec6fac65 | -6.29641 | -43.55311 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 679750fa-fcae-3918-958d-128c71da3f92 | -10.05012 | -48.09993 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 09872d10-d6db-3d62-b461-91f0f0af53ca | -7.84892 | -46.95069 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bd4b40f-7897-35b2-98a8-ae6bd08887cc | -6.33644 | -53.4297 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6697784-9178-3e5c-8841-c385a7520bd5 | -7.76463 | -50.3091 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb3a6b00-fbe3-354d-a052-30054241e2d3 | -8.09061 | -49.9415 | 2025-09-01 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 225a240b-b9e7-3b1a-9d62-363a138f4fbb | -3.00684 | -47.83839 | 2025-09-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3652d935-83e1-36bb-a912-aac7472c6ab9 | -6.461 | -43.95703 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43bb9590-af8c-37a6-932b-46937530d250 | -6.75816 | -43.78094 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 17a6dc29-ca2f-33bc-8f96-c48b342f0001 | -3.63263 | -49.20623 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 04663306-843b-3cd6-9524-adf53fa994b7 | -6.30496 | -43.6284 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9671709b-f97d-3d1b-a54c-c6884afc6872 | -8.84682 | -47.49875 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa6cac63-c3ec-3f5a-b9d2-e1a517a35efe | -6.0944 | -43.18447 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4e122b15-e0c0-3b5b-b13d-35d1e904cb55 | -9.23314 | -47.08197 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5fd9e9b5-26bf-3e65-ab47-63c8a297d943 | -6.1741 | -43.32109 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5288db4-641c-3ee2-a1c7-148f631795f6 | -6.14842 | -43.33261 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 706bdbc0-2b03-3390-8dac-67296261d114 | -6.83816 | -43.32872 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 9429689e-505e-33bb-bac2-5eb7fcc4b318 | -9.02343 | -50.11771 | 2025-09-01 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 842a4de8-4727-31e8-83f4-601a4fbd2a82 | -6.15771 | -43.32389 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a894da5-6d5d-3054-ac34-2c888136635f | -6.17685 | -44.11862 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e20b1b4-f28a-33a7-9bd9-c3556d850400 | -7.73144 | -50.25735 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08834b06-524b-3ce6-a4ae-ff5e01acb458 | -3.48342 | -51.19132 | 2025-09-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58498604-d294-3c46-80b5-fdcec164d094 | -9.69166 | -48.28763 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d0404d7-262e-329f-b7d6-2a49604caa6d | -5.49325 | -51.15648 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39b7643b-6aee-301a-8329-3ed7361cd687 | -8.01205 | -44.05407 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf07df7a-840b-30f3-b88f-90e65192b54b | -6.57058 | -43.70807 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a2b286f-2846-3ff9-81d8-fb5944ed35e9 | -6.2768 | -44.49141 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ae9dcaf-d7b9-361f-981b-cb256aae4cf2 | -6.45043 | -43.9502 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f956def4-689c-3315-a582-487650464882 | -7.74955 | -50.27168 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3418168-6b13-3113-a353-bcb1c123215c | -4.12303 | -47.65286 | 2025-09-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7741b990-550c-3b22-9ed6-5f61380e15c1 | -6.2641 | -43.54581 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5a265b3-b700-33fc-81af-edbdf853f905 | -6.14525 | -43.32715 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1c63ac2-bf95-331d-ab75-9249586dc6ba | -6.35379 | -43.92333 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d3a3fd4-5a1a-3b55-a044-401b079e440a | -6.31335 | -43.62474 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd931f21-a252-3f39-824a-46dae2b51fce | -3.2169 | -46.82991 | 2025-09-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README56.md)
