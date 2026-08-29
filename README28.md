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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2d1c960-bb46-310c-a01c-4b737fbe09aa | -5.28709 | -50.93788 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffbfc696-9cca-3875-b282-914fd1b9c3b0 | -7.2927 | -49.96067 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d48a052-faad-3630-b90b-e6bcc9633a20 | -7.2853 | -49.95539 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b5ecc6f-40b0-339d-823f-96757ec07fa0 | -8.59799 | -54.7782 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17010d11-927d-3533-bda5-264d6e02eeb7 | -6.78556 | -55.66849 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 77ac2baa-6753-3402-8640-8ccd556268f8 | -7.34594 | -55.17258 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 470347d9-9a1b-367e-a473-a51c63b20020 | -7.12669 | -42.77048 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 37ec6cc8-ce71-3414-b6d9-4ec804e66db4 | -6.95151 | -58.95598 | 2026-08-29 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57e51897-cb16-3af2-829b-4fc2aa063c54 | -6.62056 | -43.73979 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 264de03b-f05e-39ae-969e-f3ba9e1862fd | -6.71322 | -44.42027 | 2026-08-29 04:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50c3aade-8032-331b-b3fa-f8919386b9bf | -10.07018 | -48.69407 | 2026-08-29 04:32:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a72c0756-8d40-331f-a04d-9ba695514cc8 | -8.60243 | -54.77939 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bda656c6-3dd0-3979-bf2d-530fe4f0736a | -5.87401 | -57.77262 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22dc5546-8e71-3c02-aea2-92f9947f2f85 | -11.36005 | -45.15538 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 037488a3-a543-39bc-9c06-21861014d969 | -4.28847 | -48.18886 | 2026-08-29 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 84c3070d-b9d2-3b5c-9741-61511a6dd27c | -6.76027 | -46.13732 | 2026-08-29 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 290014b0-3cee-352d-b885-d74711187864 | -10.45307 | -45.14125 | 2026-08-29 04:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1136f14-e543-3386-9030-e595e2529e57 | -8.16376 | -46.16908 | 2026-08-29 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 872b9073-7436-305a-ab90-a3727fd6085e | -5.34078 | -45.15907 | 2026-08-29 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cc7dce6b-18be-3d8b-991b-680dd697a96e | -7.51868 | -55.30593 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 49ffadc8-1116-3650-9ae4-7a45c64d7270 | -11.36339 | -45.15591 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7a771a3-6b12-30f1-a56e-b69bef1eba36 | -7.11799 | -42.78083 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 874f95c0-cd7c-350d-9cdf-b84cdbf6b5e8 | -7.19803 | -42.73358 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f5771eef-bdec-3fab-9b78-d56f9fd278ea | -7.50725 | -55.30373 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 0780f32a-6ef0-392a-8f76-e84a21bce42d | -8.94996 | -50.80895 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7dabb2a-ed08-36da-a838-5bb4eb93674d | -7.53659 | -44.45669 | 2026-08-29 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40d75322-d9a8-392e-b5b6-457e72a2aef5 | -7.50025 | -55.27721 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 297aae2a-b411-38ad-96be-ba4776b3cb6e | -6.17597 | -45.92355 | 2026-08-29 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b92b7915-a169-36a9-bec6-a8693fb1cc73 | -7.34745 | -55.17078 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed2106f4-5c7e-364c-b130-a72155aaa52a | -6.78635 | -55.66416 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d0f63359-8c9a-31d0-a8e5-79009c63018c | -5.33801 | -45.15506 | 2026-08-29 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e64f646f-e408-32bb-80fd-84af6a7fda78 | -9.43292 | -51.68521 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c25d502-3223-3797-8764-a9a8a082b98b | -11.23986 | -45.0773 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89508ca3-5ff4-3697-a118-ef99df9d3e80 | -8.67703 | -49.54642 | 2026-08-29 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc2126f4-f1e1-3721-a92c-c938eafb4dea | -7.11747 | -43.16751 | 2026-08-29 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cde535e6-b943-3348-8063-dd847272f706 | -11.36949 | -45.13874 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e88f3b6-0e81-3f28-a06b-6b43902c5cb2 | -8.52906 | -55.35852 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2fc02214-fba4-3a04-bbf6-9035ef59b046 | -8.58806 | -54.76575 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81c41414-011e-34bf-8e10-4017ebcc142f | -7.28933 | -49.95605 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1483a06-cfbb-3b56-ab4c-97a8807b8f5e | -11.25155 | -45.06822 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9254fb55-c2d2-34d0-8919-66815b786075 | -7.05459 | -42.18523 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2576a271-5b16-3d6c-bb3d-315771f6be33 | -5.89014 | -57.76162 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 786346d5-71b5-3845-89c2-3f32d4d387bd | -8.81866 | -49.62782 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a38cee4-690a-3052-b9ec-870498fbc73e | -9.20543 | -51.54621 | 2026-08-29 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 840c24f1-acaa-36ec-b150-5c85068835ac | -8.60472 | -54.77225 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 329e0001-5d04-3edf-bbad-db4a740792f9 | -7.10492 | -42.18895 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 556d1f53-2279-3d87-844b-a79dfc107d3e | -5.98134 | -57.69136 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 32aa26c7-a455-3ee9-8d37-f0fc81b09da7 | -4.9716 | -49.61848 | 2026-08-29 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa6382a8-8652-370d-b9d1-1448be3b4b2d | -8.97864 | -50.79075 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db8fc934-823e-31f5-8aee-81f6f6d850ae | -9.26711 | -45.64447 | 2026-08-29 04:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f96d5509-c6fa-397c-b9ed-b0d6f12b7c40 | -8.59699 | -54.77842 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35a53295-0f1d-3b35-9589-70d324911ddd | -4.45297 | -46.82423 | 2026-08-29 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eb109fee-1e59-35cb-b713-b348850de935 | -11.21808 | -45.05224 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e55ee52-e9a6-3179-b8f4-bc29119572ee | -9.20378 | -51.55544 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ee45564-5116-3a5f-b4b9-2feceb5e2da4 | -10.05854 | -48.67513 | 2026-08-29 04:32:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adb7358e-4b6d-367d-b1b0-00ea6f0fb6e2 | -11.25044 | -45.07536 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2151d7a7-3987-3cab-a214-66fbc13c7f00 | -8.11645 | -46.78244 | 2026-08-29 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 137b66af-1255-3c39-8dc8-cf1f92e10858 | -6.62111 | -43.73624 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ab061d9-153a-37d9-bfe7-5f860dc9145f | -7.29488 | -49.97248 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cb171b8-fb8c-37b7-a222-8df4d897ee6b | -9.60936 | -55.12304 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b2579b3-8008-3810-8fa0-6efdbdaf0b10 | -8.16262 | -46.17619 | 2026-08-29 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 435b8000-947b-3ac2-a640-6e8dbed945fb | -7.07926 | -42.80208 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 82c84fbb-018f-3ed9-a31b-028827322412 | -7.2828 | -49.97047 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3dc7c98-a78f-38ff-b807-4d1b1ea5e774 | -5.83344 | -49.19317 | 2026-08-29 04:32:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 438075eb-dcc2-3168-9d46-fbc86f9594bc | -5.98922 | -57.68668 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 41aa727d-2de7-36d3-bd76-11c8aa461713 | -10.06076 | -48.68399 | 2026-08-29 04:32:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b78c8eab-8ee2-335c-bdb7-814b2bfbf338 | -6.155 | -57.78827 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ec30b074-0745-3aab-a419-1c7169745d13 | -8.59325 | -54.79911 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4932d30f-1446-3699-8cd2-ebb9bade8a1e | -7.34092 | -55.16778 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9d2c6915-0445-3229-87ee-e0e40ab6edc3 | -10.06658 | -48.69346 | 2026-08-29 04:32:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ba58783-aaa6-35d5-b70b-a166b562c526 | -6.78235 | -55.68617 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be5c9a7a-02f7-3c6a-a21c-25cd42746cee | -3.15827 | -54.62962 | 2026-08-29 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b627fd8-96de-30b4-8ead-0b2d27e8e8d2 | -5.88888 | -57.76854 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 863b97d9-efe1-3b0f-9f36-1591a3009ef6 | -6.16861 | -57.79078 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8481d1c7-bc99-3ff1-adae-a63d9a6d58de | -9.26823 | -45.63747 | 2026-08-29 04:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca2b1a5a-af41-3fd5-850c-942042e9d724 | -11.24396 | -45.3144 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39c9d572-6d86-3aa7-9469-b7952150ac92 | -6.40963 | -51.68036 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38ad8228-2772-3b45-b1cd-b1f224d8bd93 | -10.85962 | -44.80532 | 2026-08-29 04:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a30a78e3-6d3c-3bd3-b2e9-de128fd2b2b4 | -8.5941 | -54.79879 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 733b3d22-785a-35d1-a5f5-7e92b17b7ecd | -7.5194 | -55.30198 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8d4e922c-adb4-3594-b13a-392546774a4f | -5.60823 | -44.00319 | 2026-08-29 04:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8fa1314c-50b4-3dec-aa98-6862a4206b1b | -7.21246 | -42.75549 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2024224-fc37-322b-a732-178f366d84e0 | -6.34238 | -44.09019 | 2026-08-29 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 115a537e-4d5e-36d1-aeb9-bb22b8d6c328 | -8.59255 | -54.77722 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6369d5e-e67e-3787-ade0-1279707301af | -6.62336 | -43.74386 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3e2b241e-108e-3074-90d5-79eeeadc70b4 | -3.18482 | -48.01988 | 2026-08-29 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd3f6e45-5ae7-3977-aa1d-124ba0e52329 | -6.5818 | -55.44384 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c01600ff-51bd-37b1-bcb9-ee700f786f58 | -6.75928 | -55.67811 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84a85657-8f3f-37f0-bc04-606f50ddce87 | -11.37673 | -45.13623 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f2a40d5-2d71-3cbb-8892-986ec2281a5a | -9.4224 | -51.59295 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09a9264b-718b-39c2-ac1f-0330e80fdc6d | -6.6228 | -43.74741 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cd3b320e-1488-30f3-97fd-6adbfd7d4e1e | -4.37114 | -47.77517 | 2026-08-29 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1c715cbb-d3ed-3299-8417-2c8f10c730e5 | -6.41123 | -51.67108 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0332bfa2-7087-3397-a485-410cd0de73cf | -7.51226 | -55.30875 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c83c2870-d6b4-3c56-9848-8cb5f9b81c28 | -6.62672 | -43.74438 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6b6c98bc-71b5-3a6d-a794-af862a9a2464 | -6.76608 | -55.6745 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01a4e80f-4c0e-30a7-8318-31b19138a454 | -7.28342 | -49.96676 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0791365e-e197-3446-a940-7ea1b7ef7bac | -6.77207 | -55.67527 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60568c12-9a5a-3228-9637-a36c47b343dd | -6.93497 | -58.95272 | 2026-08-29 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b0d900c-7685-3429-81de-9e28ad314892 | -6.84261 | -42.86695 | 2026-08-29 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README29.md)
