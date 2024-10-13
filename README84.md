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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca7ecd92-8208-3242-a226-87a939f5ba34 | -11.2022 | -47.84899 | 2024-10-13 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56896102-e2ae-38d1-bc78-fdef87270abd | -13.02914 | -48.64527 | 2024-10-13 05:04:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5afbf4ff-5ab6-31d0-938d-0697615b2f75 | -13.02877 | -48.64834 | 2024-10-13 05:04:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c3b4e22-07a6-3e97-b45e-d95da4075bac | -13.02635 | -48.64807 | 2024-10-13 05:04:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 969938da-ef0b-387b-8fc0-761c5551fb3a | -13.02595 | -48.65111 | 2024-10-13 05:04:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d5d5ded-1c81-3406-9e39-a034a1a1fc7e | -12.83647 | -48.56488 | 2024-10-13 05:04:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a530290c-023b-3d02-a905-c50f972197de | -12.83608 | -48.56804 | 2024-10-13 05:04:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29337535-3091-3a3c-bcc1-34fb679d4221 | -7.63028 | -49.41601 | 2024-10-13 05:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 265a49e9-a46b-36dd-900d-4cb631e9e11a | -7.62965 | -49.42046 | 2024-10-13 05:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4897bd6-21dc-3d4f-9f2b-d14ed13933ec | -7.09084 | -49.8772 | 2024-10-13 05:04:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eedf57f3-676c-3473-b344-f08e9080c857 | -7.08654 | -49.87658 | 2024-10-13 05:04:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57fa7743-d500-3d33-bb14-6e47f06cbc4e | -7.00991 | -49.31587 | 2024-10-13 05:04:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27bfff24-14b6-3878-8c6c-b4f4ba329380 | -9.44649 | -48.88758 | 2024-10-13 05:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20c56760-410c-31c6-8533-3decdb0ef411 | -9.30059 | -49.63702 | 2024-10-13 05:04:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5867f21c-3ada-36ea-9156-34917e4aaa7e | -9.18159 | -49.65962 | 2024-10-13 05:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad1880c5-2451-35b1-9762-557846163849 | -8.78293 | -49.92791 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3efb83b-2d60-3f05-b42e-daae591588b7 | -8.78244 | -49.92685 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10ceec8c-3b32-3b64-be4e-90f26d28ca62 | -8.75392 | -49.78329 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1e7b591-7f24-313e-ab63-b0161da18565 | -8.68895 | -49.92737 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee7f99c7-3a3d-338f-a435-21036a172f4d | -8.68854 | -49.92908 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5e57682-da51-3c11-b784-8f6a71d16c89 | -8.68075 | -49.92188 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18d5d581-9021-3a08-887c-e11040338269 | -8.68038 | -49.92363 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c58bd228-8a28-3eda-9c66-ed31b6060ffd | -8.65663 | -49.93322 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 852bfaff-67fc-39be-a098-8f3688d41db8 | -8.52887 | -48.77543 | 2024-10-13 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19d00ca3-1389-387b-9070-92346089f794 | -7.97374 | -49.46005 | 2024-10-13 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d7a042e9-7793-3e9f-bfa0-8e161c3fa6b5 | -7.96927 | -49.45937 | 2024-10-13 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53f487ee-d263-367e-893e-138f8a6ec0b0 | -10.5294 | -49.9487 | 2024-10-13 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 646eaecb-f07c-3119-9322-e6072d6aadaf | -10.52879 | -49.95324 | 2024-10-13 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33752945-7166-3de9-87fa-9aca220d9985 | -10.52819 | -49.95776 | 2024-10-13 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1be3b622-7a85-399b-b342-61a6be384871 | -10.52369 | -49.95712 | 2024-10-13 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 014a52f6-cdc2-3db7-a456-ea7bee5cdb05 | -10.51919 | -49.9565 | 2024-10-13 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2c7263df-accb-3d28-a5f6-25433b49273c | -10.51859 | -49.96099 | 2024-10-13 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 33aee2e8-0739-3bb3-96d4-5530336183fe | -10.51469 | -49.95585 | 2024-10-13 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 438d3ff1-a5cf-3715-bbe6-f823b8280372 | -10.51409 | -49.96036 | 2024-10-13 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93897f43-d841-34d5-a76d-e99cac5b2138 | -10.48668 | -49.9499 | 2024-10-13 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0259ec4c-4b18-3282-a043-c6dca2342b0c | -10.48605 | -49.95442 | 2024-10-13 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9700babd-1a50-3184-a5a6-58e46b9374a1 | -9.94352 | -50.05798 | 2024-10-13 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd82c9b4-9ce9-36f8-965a-d7a29d9ef646 | -9.62302 | -48.98272 | 2024-10-13 05:04:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0ff3f54-c907-3dd9-bfec-94feefafb8b7 | -9.62234 | -48.98768 | 2024-10-13 05:04:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b464284-62fd-3536-8093-36fbcc8638ad | -9.54659 | -50.21825 | 2024-10-13 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d26e1cb-bb8d-3481-bd2b-68fb73b8c633 | -12.02307 | -50.92613 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7fcbbbb-1dee-36e9-baff-d7d11db892fd | -12.01822 | -50.92964 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 696834d0-5f97-3445-8a5b-bd290022fcab | -12.00851 | -50.93663 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1350a6e0-e53e-36f1-ba81-75060c21e651 | -12.00421 | -50.93603 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b7e97ff-1d1a-3df9-8e30-3099effe0a0f | -11.99991 | -50.93542 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecf021a1-406a-3a4e-8716-79960bbd48f1 | -11.93908 | -50.08997 | 2024-10-13 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4280de4-215e-300c-bd41-db89fa0637a1 | -13.20402 | -49.82243 | 2024-10-13 05:04:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4fbe5cf-8e23-3e9f-9dd3-9b47c2c96f62 | -6.6388 | -49.86662 | 2024-10-13 05:04:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fc60d69-f37b-395e-a9d4-0e21fb3f2bf4 | -7.6787 | -50.2478 | 2024-10-13 05:04:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f09af88b-c12c-38b3-9a03-2b3a205cd252 | -6.92249 | -49.9492 | 2024-10-13 05:04:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50e183b8-1f3e-3b35-ab33-43489705c699 | -8.10425 | -51.09812 | 2024-10-13 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c06add9d-eaaa-34a5-919c-35ad00c2a3d5 | -8.10375 | -51.10167 | 2024-10-13 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e53d5672-f2b3-33b0-a2ac-10c22f172b9b | -8.10278 | -51.10843 | 2024-10-13 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e746ca6-5dce-3a08-ac07-b2c549e07f7e | -8.09876 | -51.10785 | 2024-10-13 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbb8c02d-05cb-3550-b5b7-090247071fde | -10.82251 | -51.1353 | 2024-10-13 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b73f2e7c-e6cb-38e2-a70c-67c9488e5dc6 | -10.82198 | -51.13915 | 2024-10-13 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbafc7c3-9bc0-37f1-ae40-fb4385a8634c | -10.82145 | -51.14297 | 2024-10-13 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ddd00d6-5705-3176-a1a8-5cc15fe5283f | -10.81728 | -51.14237 | 2024-10-13 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a89b22f-3757-3a3e-a70e-c198e180df57 | -10.81364 | -51.13793 | 2024-10-13 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b03b3b6b-a09a-3fb9-b928-8a2395d79fec | -10.81311 | -51.14177 | 2024-10-13 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af8f633c-c375-37a7-9471-84747479ab9f | -10.78551 | -51.12601 | 2024-10-13 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 555434be-1f61-32f8-b3a5-1693f0cd080d | -10.66782 | -51.5334 | 2024-10-13 05:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f76fdba-feef-3fee-be3e-8e4f15be3103 | -10.60122 | -51.77321 | 2024-10-13 05:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27a6dfe8-3c03-33f0-bb4a-ef3c4ed44387 | -10.59723 | -51.77261 | 2024-10-13 05:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11fbe755-1ea2-3d6c-bf6a-fafabaaa7c14 | -10.59253 | -51.77709 | 2024-10-13 05:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b773fc31-ec13-37b0-9753-864fd3ed2d2c | -10.58455 | -51.77594 | 2024-10-13 05:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c9f8e14-261f-39ae-8bbe-ce001f9538d9 | -10.06613 | -51.40436 | 2024-10-13 05:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0376ba2f-9201-3f19-ab91-0cfd994e227c | -10.06156 | -51.40734 | 2024-10-13 05:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c50d5301-df88-3110-90c3-836c65192ae4 | -10.05751 | -51.40676 | 2024-10-13 05:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 317b0300-21c5-39cd-b1d5-3e61b32d67b9 | -9.45516 | -51.79371 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3abcfaf9-792d-3af9-99f3-49b5d25c0f62 | -11.26826 | -51.43017 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82e93b2c-5bfc-31a5-9a71-05713792a5c5 | -11.26775 | -51.43389 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfc2fec3-819b-3d13-98e6-493979cc6680 | -11.266 | -50.90685 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dc920ac-ca36-3daa-b52f-9edc5f33d843 | -11.26545 | -50.91085 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af36080f-76d9-34e7-b9b8-da02be9d597a | -11.26491 | -50.91485 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c00420b0-a5f9-3f6d-b1c3-8ce03eff9012 | -11.26163 | -50.93886 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe4085b7-50d7-3d0f-ba31-d1278a1f57b4 | -11.26119 | -50.91024 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 361a3669-454c-3df2-a44b-68a7b01fe217 | -11.26065 | -50.91424 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd4e6903-6959-3ac3-9bb1-52d2d22767d8 | -11.25738 | -50.93826 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e018046-2dd1-3d4c-954d-02caffa7fad0 | -11.25693 | -50.90964 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bf4a9db-32df-3b49-a6dc-d99ff411553f | -11.25684 | -50.94226 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7407980c-3d54-30a3-93c9-4fa3a687d273 | -11.25509 | -50.79389 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8306b5b1-dffd-38be-b955-090065c34c03 | -11.25454 | -50.79799 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80dffa3a-6043-3c96-be70-444c8fb031a1 | -11.24801 | -51.07009 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91eb1599-1481-3401-9381-0a2595f7d1cf | -11.21728 | -51.29348 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d9163cb-d588-39c1-afd4-e9cd63005aab | -11.17979 | -50.94507 | 2024-10-13 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5157b915-02fd-38e5-b469-c591de5f437e | -6.40554 | -52.71984 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7ea0b42-05ff-36b7-9ff0-6fa6973a4ac3 | -6.40257 | -52.71521 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 790b55eb-710f-3cc5-9eb4-9ce5e31dc3f3 | -6.39602 | -52.71008 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55a9a212-6d87-36d2-b202-a247515e59fd | -6.3954 | -52.71415 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e317226-019c-31c9-9e8e-e25c68ea1b3d | -6.39243 | -52.70955 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55cfec8c-36d8-3b8b-a8ca-da40f3ba97cf | -6.39181 | -52.71362 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5aef1b3-1bd1-3198-ad7c-e1824331ab5a | -6.72895 | -52.03516 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3b9658c-dcde-3eb1-aa49-a982c962bb49 | -6.72589 | -52.03016 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40fec3b6-15bc-321d-91b8-32b7c5886aea | -6.55198 | -52.5384 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5092b6bf-6b58-3b8e-b7e6-8d0ce81ba385 | -9.10437 | -53.31694 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dedf8f52-2c38-3931-a1ee-65a35294ca10 | -9.1014 | -53.31228 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd4bd2d4-e72b-3a55-a34e-f613af9d0999 | -9.10078 | -53.31641 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1271bce-e6cf-373d-8f53-a11804c58b6e | -9.05853 | -53.24402 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b3bf275-1ce8-3116-bc08-6b5060ae2f2b | -9.05493 | -53.2435 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README85.md)
