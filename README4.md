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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ab25d4b-9607-3068-85ae-a492b5dac338 | -8.93944 | -50.91667 | 2026-09-21 00:20:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ada02e6d-f7d4-3aa9-a638-4ed1dfc356c4 | -12.33113 | -50.69139 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0ec61c67-188a-3ce1-b05f-f69a3e685694 | -9.45422 | -45.44052 | 2026-09-21 00:20:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 196af16c-fc03-300e-a518-791d3b6e8e80 | -8.30792 | -46.01218 | 2026-09-21 00:20:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 9df6aa21-3137-3d57-a283-a167169916ce | -11.34231 | -51.35713 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| f158ed29-9096-3f01-ba12-c3610dc687dc | -11.34529 | -51.37746 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7e811fff-d3e1-3aa7-aef5-5357a864cebf | -16.30609 | -53.84304 | 2026-09-21 00:20:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 34ad4060-c593-39c9-bfd1-32bca2f64e1c | -15.06396 | -49.58128 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8e4ddb18-9221-356b-b429-182645a09280 | -8.17309 | -54.78146 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 530be6f9-23f6-3bb3-8d6a-5ee2cc6579a9 | -9.45215 | -45.43555 | 2026-09-21 00:20:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |
| d8aea9c7-492d-3978-bc72-169b28c2dbee | -14.06085 | -52.10775 | 2026-09-21 00:20:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b8f6067e-5696-361f-b730-d80cc6be821d | -10.38165 | -48.905 | 2026-09-21 00:20:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 8ce65f93-0360-35db-9789-1c533d214aae | -14.6179 | -52.071 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ecc0fa18-e70c-3e4f-8d54-470efc93851f | -11.68453 | -43.42301 | 2026-09-21 00:20:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| edce5c85-5ccf-3d15-8bc8-0f39e691122b | -11.11816 | -54.0166 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a4d336ae-5168-38b4-9150-c5e73aff8c3a | -11.04449 | -54.15226 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 9c88d1ca-c73f-3169-9d1e-8cb38e228705 | -11.01433 | -54.12911 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 346780e5-4368-3e6d-b7c5-d1c510dc3d61 | -8.60789 | -54.7895 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 272d170d-9891-383b-9993-e22330843a83 | -10.70427 | -50.78693 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 04666169-512d-3884-849d-83ecc47041f0 | -11.28146 | -54.12718 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| cc238a05-966b-3436-9974-30e218b697d1 | -10.85559 | -54.11821 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| acd0588c-79f6-3686-a37c-a6f7406d65fa | -10.91801 | -53.96619 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| bfae0ba3-66ed-3503-b482-ac068e87abe2 | -9.69531 | -54.32619 | 2026-09-21 00:20:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 116262eb-14f8-32e4-b58d-f33443d642c1 | -9.82885 | -48.45779 | 2026-09-21 00:20:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c79f28c6-0e07-3434-8d78-9cb04b3c4f2c | -11.10934 | -54.01786 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ac33a15d-bc6c-3e6c-9eab-16264b56e785 | -11.79609 | -51.1092 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 249fc146-3e84-39e9-bc67-15865759c811 | -11.24738 | -54.15683 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 728bc80a-18c2-3ff1-a90f-16dc5ecd2c2a | -10.75847 | -50.59979 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 867cad91-f716-3dfc-b416-a01d48b11f66 | -10.89279 | -53.97892 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6e00b643-dde2-3514-93d4-23207d7125b3 | -11.37432 | -51.44548 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c2487375-7531-3d26-be9a-4c8991a997cc | -11.11432 | -47.52243 | 2026-09-21 00:20:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9c6572a6-7ecb-3a20-b85e-7f5c1fa9c2fd | -12.53545 | -50.07942 | 2026-09-21 00:20:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 29eb0bf6-631a-3e0e-9aa5-47923a529702 | -10.46518 | -50.35521 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 7c90ffd2-9b4b-3330-9304-96dcfb33c3e9 | -10.87341 | -56.24007 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| a06cfe75-c18c-3b14-8bab-075a5033f72f | -9.67889 | -54.33759 | 2026-09-21 00:20:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 393f4718-a3e0-3372-a3a1-3f507969c21b | -6.90403 | -46.01494 | 2026-09-21 00:20:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| cbc80fbe-bffc-32fc-bc05-2757f9f5996e | -10.78056 | -50.83162 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 25770e1f-0511-30ce-998b-84b86b635c66 | -10.89739 | -54.0785 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4686b6c2-8837-3eb4-997e-d9fac270a257 | -10.76602 | -50.8 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2155cfc8-2cd5-37b1-b8b5-3894094ce7ea | -10.26726 | -49.9847 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| eced5c01-bf6e-33b3-96e5-82fba7722f67 | -12.02888 | -51.50657 | 2026-09-21 00:20:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3954f850-5258-33f2-b71a-608fa0fcbc66 | -10.87609 | -54.05421 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 813a1a35-5e99-3359-9c05-3f4d99495008 | -11.3851 | -51.45413 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ba08058e-7657-397c-841f-e93e8d180c13 | -10.48826 | -50.99565 | 2026-09-21 00:20:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 6295847e-d53d-3555-861c-e1da538728ca | -10.88156 | -56.22834 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| d03f1e03-4534-3ffb-b570-2fbcc64e578a | -11.35017 | -51.34548 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4709c596-2c56-3aaf-8eaf-c80922dcc06c | -11.04694 | -54.17022 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f35d1a37-f008-3117-a476-ed6ef5f5b6f7 | -8.78108 | -48.75159 | 2026-09-21 00:20:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 36.5 |
| e68a8ef5-6f00-3baa-a305-9a64a00f4800 | -11.94831 | -46.49884 | 2026-09-21 00:20:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| ccb7d828-2d3e-3ea7-aaf2-576f32ca9765 | -8.1807 | -54.77131 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fe05c8bd-7dd9-31ed-86ed-8cac98574134 | -10.8147 | -50.77467 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e55205ec-73c7-3aa9-8e0a-aee61e42fe07 | -9.81995 | -48.32178 | 2026-09-21 00:20:00 | TERRA_M-M | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 13796209-a36e-352a-ae77-33139c45b64a | -8.18192 | -54.78021 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 86affd9c-1a71-332c-910a-cce46523f620 | -14.18404 | -49.59386 | 2026-09-21 00:20:00 | TERRA_M-M | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1bed4cf2-d99c-3b2a-8231-c473231399df | -14.0467 | -52.0721 | 2026-09-21 00:20:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cb7799cb-7b89-3f31-8f78-ab0785b4fa4b | -10.88723 | -50.93157 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 00505c8c-e6c1-39b2-bc29-68fc7ae3446d | -14.77009 | -48.42931 | 2026-09-21 00:20:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e6350206-9cba-3377-883c-f3ad9a9a5e1f | -15.97534 | -50.11442 | 2026-09-21 00:20:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0dd25bf8-855a-37bb-8a83-9b020c3ccb19 | -12.76435 | -52.85025 | 2026-09-21 00:20:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 466a4302-bdbe-31a3-88ab-6a9c5da84615 | -14.18628 | -47.88406 | 2026-09-21 00:20:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b5ab73c6-1fda-3d65-9d5b-287390e68c9d | -7.87973 | -54.72304 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| edaaf635-50e4-32db-bdea-4921233df8e1 | -10.9092 | -53.96746 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 8bab50dd-239a-340b-8af3-b2f4c8a61bb6 | -10.71372 | -54.01687 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b389bd9c-9af4-3e21-a1a2-8851ca7b3791 | -10.70261 | -50.77583 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d0e9f728-6f6c-3207-893a-108a350bc5ab | -11.04082 | -54.12533 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9b1722ff-750d-33fc-a1b0-602175d949ae | -11.01677 | -54.14705 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| c9f3de59-fcca-31d3-814b-e1ffc427c291 | -11.33144 | -51.34837 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3497a716-dfd1-3ada-b2b7-22ecc549c42e | -8.6037 | -54.62654 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a1f00821-3912-3b9d-81d7-4588b52b49a2 | -12.82774 | -54.05197 | 2026-09-21 00:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 20d2fe8b-2b7d-3831-8c8d-80daccf1e990 | -13.90412 | -48.57972 | 2026-09-21 00:20:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 0542e51e-bbf7-3475-9fd3-d2dca3efee3f | -10.2127 | -53.91956 | 2026-09-21 00:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 376628f3-6add-307d-be29-00001cb81823 | -12.18683 | -47.06324 | 2026-09-21 00:20:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| d15220d8-b8df-36f4-858b-bc364194e5eb | -9.82629 | -48.44127 | 2026-09-21 00:20:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 926df8e0-18e0-3f9e-9919-6883f7ae7843 | -10.79521 | -50.77769 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a025f5f1-d396-3c43-9810-bb715ae38b3e | -10.46599 | -51.3427 | 2026-09-21 00:20:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1a45aa2c-4433-3ab0-8ecf-46731bfe1f25 | -13.86075 | -48.58622 | 2026-09-21 00:20:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2027cdd9-9526-384f-b545-72f8c5e3dcc1 | -11.05612 | -54.91807 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7725d83c-7b5b-35b0-8ed5-990624968d10 | -8.08273 | -55.33767 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7bdee831-51e1-3e21-b2ab-e5e5fd22ad15 | -11.80726 | -49.80245 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| eadf58f6-10d9-347f-a8b2-7d61b77e2e0c | -10.86794 | -50.93459 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 261040c4-1aea-330c-a01d-802a9dd2e9ee | -11.03688 | -54.16249 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2f23861a-29f6-3976-8ff5-85a767af8991 | -10.88735 | -54.07082 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 350676d2-c744-37d3-810d-d2648edb0291 | -9.68011 | -54.34653 | 2026-09-21 00:20:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2affcb2f-3a52-3233-91f6-914c9f7912ca | -8.62152 | -55.23531 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe6e8b43-5dac-365e-85a0-a4a608fe740c | -14.06216 | -52.11702 | 2026-09-21 00:20:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3f849a31-f073-3e7a-b39c-7db1ab3a308f | -13.86292 | -48.59972 | 2026-09-21 00:20:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e544a9e1-e8e5-3fe7-97d6-e6bf38853282 | -16.04608 | -52.52782 | 2026-09-21 00:20:00 | TERRA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 300b47d4-f288-3d01-a8d5-245691c21e62 | -14.86232 | -47.15008 | 2026-09-21 00:20:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 17372d10-67c5-3d4d-86d8-615835724c9a | -11.22751 | -54.07724 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0667217a-1c09-39c8-b615-d7f9f2f4fe56 | -11.8631 | -49.9753 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| cbcaa83d-f38a-3d49-882f-1cfe25572901 | -12.76561 | -52.85927 | 2026-09-21 00:20:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ddae6feb-1fe5-362a-97ef-e277e8c7b0b2 | -11.87216 | -49.0111 | 2026-09-21 00:20:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d1324598-a2a0-33a9-a189-ab08af0c2de6 | -10.49715 | -50.36234 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cc8f7780-8c5f-3ce1-a22f-b213468eaa6b | -12.68739 | -50.96237 | 2026-09-21 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 80c9f480-6929-352a-b228-b54c7948fb22 | -10.53898 | -54.49908 | 2026-09-21 00:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cfe452d8-8005-3c46-917c-f78a2ac949be | -10.92315 | -53.93814 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 49bf13d8-1737-3cb4-9c3b-e2cc6dc0f769 | -10.47702 | -50.36549 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 99be667c-a7f4-3ed9-8dea-dfa3bc8ec6a7 | -14.05561 | -52.07072 | 2026-09-21 00:20:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1f868ad0-9958-373e-9fae-108ac019a470 | -8.08396 | -55.34676 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1c693dff-b902-3373-a4d7-b51e2ed88b5c | -10.82609 | -50.78423 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README5.md)
