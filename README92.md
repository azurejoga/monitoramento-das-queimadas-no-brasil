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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60d860cc-529e-3ee9-8803-cf118b7877dd | -11.18456 | -54.89836 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2b0ac63-c7dc-311d-a61b-42daba9368ea | -10.13174 | -59.42618 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7dd6526-9a69-3590-9bf8-669b0921b96c | -11.14091 | -54.88189 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f83b630-d04d-3f59-931d-a093dd84470a | -11.73915 | -50.95547 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2cd1fefa-cd08-3db1-b455-e32015bc61a2 | -8.02746 | -55.12922 | 2025-10-08 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc0f6bcb-c2b7-3c50-9aae-2607821cdbdf | -11.17876 | -54.86635 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09da48b3-88e9-3b59-84c9-81e04aaa5bcd | -8.15382 | -54.84498 | 2025-10-08 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be0a22a6-90b4-392c-80a8-e3aa9742da13 | -11.17379 | -54.90278 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dea2d485-03b1-3258-916e-d04e29a42ce4 | -11.75532 | -50.92725 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5871cce2-46f3-35b0-acd2-836cca05b010 | -11.18564 | -54.88967 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| df6c9086-cd1a-39c4-8325-839596ac047e | -11.14052 | -54.88488 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6eea1b51-2fab-3478-9367-5088bcd7163d | -11.14593 | -54.88264 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4374dfa-5fbf-3031-968e-681278bc95c8 | -11.16136 | -54.88193 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a41ce78c-83dd-3bab-aca9-66e2ac5c053b | -11.16175 | -54.87897 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 482035b4-842b-3ebf-958c-15b7fcd1f114 | -11.13513 | -54.88708 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0866026b-cf4e-3e95-aa24-029c079cef98 | -11.74347 | -50.91425 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| c572d7ee-8bc3-3682-a401-464e553ccbfa | -11.73859 | -50.95928 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5fb0130a-7612-3248-9559-9711f6f6718a | -9.25905 | -56.28745 | 2025-10-08 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cf84eae-11bc-366d-beac-6604ef5a0716 | -7.00353 | -59.28328 | 2025-10-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03e0f4ee-6ba4-38e0-8600-d8950886c20a | -6.9915 | -62.89968 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c263f531-496b-3a84-973b-8e77b7a2c6ac | -6.62719 | -62.87716 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47dd8939-adc8-3743-9880-4b8b3f515cba | -7.59811 | -64.50542 | 2025-10-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b49d66f-ae2d-33ea-bb3d-62750eaea992 | -9.32777 | -60.59982 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 500c088c-3d8f-32ce-be09-e644785002b2 | -10.35404 | -50.24989 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 25fc2abc-66d7-36a8-9fe6-1ba68da86dc4 | -11.16599 | -54.88562 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5847c524-527b-3e08-95f6-0e38ba07eabe | -9.62123 | -54.32359 | 2025-10-08 05:29:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5d3a2d7-dc1d-34ad-adc1-939d9467e331 | -11.75481 | -50.93467 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 8fb10fff-2baa-3a1b-830d-ccaca4bb83f8 | -11.18061 | -54.88904 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7d5cdfcf-4aef-3f36-bcaa-728b27d125c0 | -11.16792 | -54.87086 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7ddccfe-12a5-33cd-9382-bdf4fa3d2797 | -10.34345 | -50.25065 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ccfdee1-03b3-3eaf-aeb1-cea2952c57b4 | -9.86795 | -60.32166 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b45365f-c977-3e45-b454-dc4918ee657b | -9.79101 | -59.96455 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fc5c859-e3a1-3315-902b-52a122758eda | -11.1282 | -59.07983 | 2025-10-08 05:29:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bd6dea2-f2c1-3e49-821f-8e1afad95e18 | -9.35302 | -60.52528 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc7d57d3-358a-3b5f-882d-3c6b06defad5 | -6.95326 | -63.09702 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36c3cb59-f0ff-3773-b24c-0c1f70c2d701 | -11.16914 | -54.90062 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c032659-8172-3af0-96b7-285db2a68180 | -11.15405 | -54.85949 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96bce970-dbd7-346a-a118-4f8b377215e2 | -9.7904 | -59.96864 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 341574c0-1da8-3596-a39d-eb2c6057bea1 | -11.6792 | -50.95906 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| deb7066d-3450-37c5-ba4f-6dc5550cad5b | -11.12419 | -54.04836 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd2b88cb-a3be-336c-ba0a-85c6ee941afa | -10.35085 | -50.24557 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4d101c1d-ea31-3b9b-be5b-bb5c87b75efd | -10.37981 | -50.23114 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8149044-ce7a-3e7c-b6b3-674895809475 | -11.73715 | -50.91525 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 415983a3-694a-398e-a3ee-64cec93de47f | -11.18108 | -54.88758 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b3ef4343-d9a6-33cc-a99a-57314a0efe96 | -11.1359 | -54.88109 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cff3a426-c4eb-3a04-babf-a8d22876668b | -11.7494 | -50.92075 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b9ab5663-0919-3183-ac62-608ae176e447 | -11.7392 | -50.95367 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 61307af3-9adf-3fa5-970c-f759a4120d48 | -9.45107 | -56.65655 | 2025-10-08 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a42851fb-a24f-3393-9583-134b3fcae03e | -10.91236 | -51.01687 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c991c7e-6e38-36c6-96bc-ce80192d3d01 | -6.80492 | -63.04502 | 2025-10-08 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e21303b-24b5-3b0f-a7d0-12df258e63fb | -11.16524 | -54.89136 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed17af1f-1799-3518-97ff-e3b7e02780a4 | -11.16871 | -54.86488 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e262182-7961-30ce-9dea-4e36c0d9cd05 | -11.17026 | -54.89207 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d79cd1a-d3a8-3026-a46c-7f21c9fe30ce | -11.7398 | -50.94986 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fa61811e-bc08-32dd-9bae-d2498fa2aff5 | -10.97352 | -59.02482 | 2025-10-08 05:29:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21594990-6d57-31c2-bb6e-c7be94e29a64 | -11.75546 | -50.92903 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 17cc3dae-9dee-3b83-bb47-2b9ca0e8cf23 | -6.95271 | -63.10051 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eaec3c0c-eb3b-3962-9bb0-3e1235486c2a | -9.63832 | -55.13504 | 2025-10-08 05:29:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 409e6ba0-b5a5-344a-9756-5cc42d44de40 | -10.33998 | -50.25407 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 95726dd1-8dca-32af-8f36-11213a5c9111 | -11.16213 | -54.87601 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f66c91f-b151-3f17-8be9-4490652f95ae | -11.17567 | -54.88984 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| fef37072-54f5-3f56-b1b9-0543c26b861d | -11.75612 | -50.9234 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2f1a8296-9fff-32e1-a86b-bfc465615ab3 | -11.74304 | -50.92173 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 25181666-965b-39bf-9397-ec72544d5f29 | -11.38103 | -54.34694 | 2025-10-08 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acf8f435-d7da-36bc-85a3-a6560a5746a4 | -11.7584 | -50.89902 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 64343ea7-d149-340f-b6c2-8b7dd7fba980 | -11.12016 | -54.03742 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fc2851c4-46b6-3334-9c64-53726b0a8689 | -12.39942 | -51.13043 | 2025-10-08 05:29:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec79d28e-c124-38c8-871e-096fd75a32e0 | -11.71639 | -50.98093 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 56e92a4d-323a-3195-8b3a-71d26dad7c29 | -11.17758 | -54.87528 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f929166-f7b8-3098-b557-4fdc074f23fc | -9.45163 | -56.65237 | 2025-10-08 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2572ab92-c296-3f11-b0dc-d4a75b724e91 | -11.15635 | -54.88115 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80ccd165-2537-3d8a-b953-10f34e5fd3bd | -11.18184 | -54.88177 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 990bc06f-68ce-33e5-81d2-cd2ef3b1a1cd | -11.38143 | -54.34367 | 2025-10-08 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0176f23-0c75-32dd-9987-c007391ab2dd | -11.69939 | -50.95601 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c6254341-c8dc-32fa-88a9-b2ea34873f62 | -6.59754 | -59.11683 | 2025-10-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a08f6769-7da2-360e-b29f-da8c2b38d14a | -11.1763 | -54.88261 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 64742eb9-899d-343e-b8a3-e3f34edbe9cc | -11.17273 | -54.87008 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eeb3f0ef-edb3-3d6d-ba80-3b02b874bdbf | -10.23117 | -52.70056 | 2025-10-08 05:29:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8cff9b51-168e-3635-939b-b6613f926dac | -9.63933 | -55.13452 | 2025-10-08 05:29:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60a2d98a-ab04-3811-aa0b-bbf4d3474f5d | -11.16408 | -54.8611 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2713bd39-a93f-3b33-8292-bfb849e67474 | -11.33618 | -56.20603 | 2025-10-08 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0affb591-bf8f-3e24-9db7-172d1d4dbc96 | -11.1799 | -54.89478 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bc9964c0-af7f-384e-bd8a-c4e7a523cbd5 | -11.11847 | -54.05092 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c07eadf3-266d-35ae-8a1f-c4ac9a890ece | -9.66556 | -58.86372 | 2025-10-08 05:29:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba0b4b73-a7fb-3351-8c71-99b96a41a987 | -6.62665 | -62.88063 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5472271-3249-3983-89bd-9a3965f83dea | -11.73981 | -50.94804 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2f98d702-9670-3c01-9985-d14dcf7e0312 | -15.22716 | -56.76211 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c4234e1-1ca1-3a9c-93eb-947469525dc5 | -17.93309 | -57.52132 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6832e2ab-d7ef-39be-88d1-57145c287c8b | -15.17717 | -56.82028 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f056ff1a-96d3-3ac1-a38c-862b4ea26756 | -12.42178 | -63.99077 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e91f4b1-1f4b-36be-8ed7-dd83473f9b03 | -17.82591 | -57.6371 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| e3228a15-9974-3044-81e2-9908f7ba0852 | -18.02117 | -57.52378 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9838aa79-2d8c-37bb-a0e0-5a96d03c6a5a | -15.21764 | -56.78344 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d7a87d6-0c1b-3dc9-b0e0-5ef4ca77ddf3 | -17.93348 | -57.51096 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d73a92d8-0ce4-31f0-bf97-76ef9f1ea216 | -15.2106 | -56.78041 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cc06cda-a1e5-3979-8e14-d5f8a4c3c6cc | -17.86721 | -57.64157 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6e69ab38-4497-3675-90e5-58a69b54b00a | -12.63737 | -50.55885 | 2025-10-08 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b5a23ef-89c2-310a-b993-0d4507b2a02c | -12.89921 | -54.74358 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb650419-5492-3058-9047-003ce008da07 | -17.30111 | -58.06735 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8dc6063f-ed04-333d-b44e-1f8156a83bca | -17.27794 | -58.10965 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README93.md)
