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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae22fe8d-4fc9-3a2f-a345-433c5b938550 | -6.05564 | -59.91946 | 2026-10-01 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10253c41-283e-3cad-a43d-7ab34c86d6e7 | -10.24945 | -59.02828 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab53e206-c32b-3720-8074-159d299bf2b1 | -6.92394 | -59.28675 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8166a24-e6a9-3c71-b49c-0e6fcf16f160 | -9.96577 | -59.25901 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c73cb58a-56d3-3d20-9a20-60fbd7a2ea28 | -5.29906 | -55.87339 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66e70ca9-e75f-3c5b-83ad-8b333722592d | -5.98097 | -55.37717 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ab5f9fc-e86e-33fd-8de4-09410eb6ddf3 | -9.17131 | -59.00817 | 2026-10-01 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a5c6c94-2f18-3ac5-98a1-690a6bdc33b7 | -8.16488 | -54.8005 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ff3e65d-ffab-3a77-9cdb-e4e457d5edec | -6.76826 | -48.68019 | 2026-10-01 05:18:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 145ab83f-4d8c-3fa9-80b1-66a054dd2c0b | -6.35007 | -55.33943 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3d1f782-2d59-3518-9fc0-5f653aff6cd3 | -6.66871 | -58.8717 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| f9d55696-0d32-3fbe-bc3d-43c844bd912d | -8.79901 | -48.00138 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70e87b72-e53b-3a67-bbbd-10ca6e03ede0 | -7.78649 | -49.87147 | 2026-10-01 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 88d90951-8e16-34f6-a3a2-0e0114cfc441 | -9.0838 | -49.88411 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 752b4706-f883-3ffc-a800-36874641eb54 | -11.32472 | -50.96965 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 25ff91c8-0947-39cf-9d25-147d58ae891c | -5.80744 | -57.73219 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d198be1e-a09f-3ed8-8187-db3d7594fb6d | -10.77616 | -54.7558 | 2026-10-01 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e001b2b-fc73-354c-a00b-725bf458aace | -10.54926 | -50.01104 | 2026-10-01 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0551af3e-52e2-3c2e-b37b-2dcc72a9596b | -10.41035 | -53.77851 | 2026-10-01 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f0e9a1e-28bf-3fd4-8703-c514b75f397d | -5.86399 | -53.4898 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f029113d-d8d9-340b-ae4a-0bf997eb7d51 | -11.2864 | -50.97131 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 3e3149a5-27ba-3c44-9138-68a7665da0f5 | -6.22863 | -56.04517 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69368b49-a16f-3a3c-9cfa-004160d42a5f | -9.70347 | -58.12645 | 2026-10-01 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e0cb7f7-b950-33a6-acc7-1e27af6b0453 | -10.53773 | -57.77613 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dae18b3-5398-3a0b-a2d2-fbb61a8f4ca2 | -5.30265 | -55.87389 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98e87d6d-bc52-3f78-a3d0-9fca53bee4c9 | -11.37673 | -55.12417 | 2026-10-01 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8a91c7b-7fcb-33c6-8daf-fe2c2466b7bb | -12.19279 | -47.38985 | 2026-10-01 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fa83c48-1ea3-38d3-a650-11a70b8a7b7b | -8.85039 | -50.50712 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a37b51d1-fcfb-324f-9214-698fe5f7e0d4 | -6.16184 | -57.70527 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3649cd4-2999-3df8-8b67-d27a327a6827 | -6.10661 | -55.68966 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd6fbcb6-bb24-3f38-9f2a-28c48eaebb12 | -11.16323 | -54.11762 | 2026-10-01 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9a3c641-98ff-3f09-8800-afb2afd3f599 | -7.34784 | -55.59161 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9543a6dd-5462-3f90-8ff6-1030ad28fc67 | -6.36814 | -55.14244 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69e75135-3af1-362b-95e8-0905047a3db6 | -6.08746 | -57.68319 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0386177-6c4d-352e-b7f6-b7f300cab3ef | -6.49078 | -58.52833 | 2026-10-01 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4f623a4-34cd-3a52-8cc0-f3f7eca71acd | -11.7362 | -50.40621 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8914c229-f451-3aae-b89b-cef9b0cceab5 | -8.00022 | -61.36827 | 2026-10-01 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 022bef89-ca33-32d9-914f-c2f385549ca3 | -6.11503 | -55.7084 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ac9c2d2-3cb0-33b7-8b00-afb4cf648015 | -8.51406 | -62.67696 | 2026-10-01 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 62bb72d6-3260-3324-adfc-86eb568318a6 | -9.00381 | -65.7114 | 2026-10-01 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6c03d93-e5b6-36fd-9c22-389940a37fba | -5.86703 | -53.49799 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61078bc9-df22-3de2-a3a1-da16afe1b86d | -6.12923 | -53.27702 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3adead89-067e-360d-bfc5-a10fa504cb4d | -6.36506 | -55.13726 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8300947c-c2fd-332d-ad4b-cf3f52829c32 | -8.19587 | -61.37636 | 2026-10-01 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36d1bdad-1fa8-3ecb-a61f-f0c2869b391e | -8.24489 | -54.65979 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5cfcf8a-462c-387c-8571-f66262981e99 | -9.35139 | -57.16779 | 2026-10-01 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f09a1606-2b09-396a-8605-13dba1eb665e | -11.74226 | -50.40315 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f562e0e2-cf9f-3c14-a60d-4d165bb012b5 | -6.01057 | -49.56065 | 2026-10-01 05:18:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 134e72d9-9321-3274-b5c3-5e55489a5c2c | -10.85503 | -48.69255 | 2026-10-01 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ac21eef-5aa8-3410-b194-523a067f0f38 | -6.54523 | -55.28065 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 491ae15b-afc9-3c22-935c-d21b5789dd32 | -6.75206 | -55.08587 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 149ab5a3-13e2-3419-9903-9fcf021f5dec | -9.34787 | -57.16729 | 2026-10-01 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9159e750-ad69-34f8-b39d-604db68feda8 | -5.77026 | -56.5179 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f493c20-7e72-32dd-a13b-87657b57e968 | -9.06982 | -49.86911 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a7f7e3a-a072-355f-8e28-53016297f22e | -8.31784 | -54.76402 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4d861cb-7797-3109-a98c-f8011961065d | -6.14566 | -53.31177 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f72f6ac-8369-3dac-8425-2d9517ca720e | -11.38169 | -55.12392 | 2026-10-01 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 55fda560-89c0-38b3-8245-841eb95af61c | -8.18294 | -54.78745 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdb29a23-8102-3559-96a8-08a6ae0c5c88 | -10.75758 | -51.66633 | 2026-10-01 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 626dd6b2-62d9-36a8-bfa3-d380c3557df3 | -11.41458 | -51.01758 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a49a64bd-1afc-321b-87ca-d59fb2832f69 | -10.07014 | -63.08173 | 2026-10-01 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9a99b9e-df89-39bd-b490-fcdd8c7d7ee0 | -11.32966 | -50.97378 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed02a5e6-7f1a-32b3-ab7f-7f245b4585f0 | -7.8548 | -45.82027 | 2026-10-01 05:18:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0190bc8e-9dcb-3096-814d-ac86665a7422 | -6.8921 | -52.4995 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c92e8f16-1938-37b3-9e39-26e57bba1090 | -10.78367 | -50.52581 | 2026-10-01 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d44e21c3-fc44-34fd-b602-3ca6f38bee2e | -7.85005 | -45.81912 | 2026-10-01 05:18:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 81685806-ddc9-3637-b8ba-04605afcae09 | -10.66053 | -50.76041 | 2026-10-01 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bd44b01-49a8-3ca0-962b-fe3b6e84a3b1 | -12.18817 | -48.42972 | 2026-10-01 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0c038a9a-946d-30c1-819c-3e3f36f0990e | -10.52677 | -57.77839 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 440186cc-dd51-30f2-b25b-e07491bc3d9c | -7.72825 | -54.79594 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d17d0d0c-e29f-3d27-97c1-ba76850eabea | -11.79602 | -50.51346 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3dc3f8f-44d4-3075-874a-e7afaa73652e | -6.92502 | -59.27985 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c55e90c-053b-3f22-ac1c-50980455249f | -6.34464 | -55.32483 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a26163f-8f2f-37c0-bb8e-e47225f14f8e | -8.2671 | -54.75935 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dad85ce-563a-322d-ab16-05de7ccca943 | -8.22819 | -54.74831 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb738864-e5be-3896-a1a1-978e68776c47 | -10.46486 | -51.76389 | 2026-10-01 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51d9dbe8-c19d-35bd-897e-0a2955597732 | -6.73066 | -59.43689 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 512bad6e-840c-3c63-984e-c304608bcd9a | -9.74243 | -65.04581 | 2026-10-01 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0dd89315-b78f-392e-997c-55d07cde2ff1 | -6.07105 | -57.61074 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b85500b8-d526-380d-a843-a40edd5a051c | -5.97357 | -55.37598 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3081911c-ccd1-3869-a8ba-cf5b0888c9b6 | -8.29111 | -46.74645 | 2026-10-01 05:18:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91bdc2a9-15c4-3f22-a4b3-3f3135381b0e | -8.84939 | -49.70516 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 187b604e-d7f5-3642-803b-055c151f1f43 | -10.84026 | -48.71167 | 2026-10-01 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1668e450-7ab4-36d5-bad6-b7fdf8d1b0f4 | -10.56505 | -57.77524 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d63f520-3313-3335-a900-f196511557e0 | -5.86452 | -53.48627 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2c2b100-d3a6-3871-8fe2-eed18de252ea | -6.70385 | -55.04774 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 33b152a1-c076-3947-b63c-e2f5e6950683 | -11.28515 | -50.98157 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3926697-77e1-3420-a974-2b8f6910f5d6 | -9.62409 | -64.17973 | 2026-10-01 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c21f787-7134-304c-9926-2acf828aafcd | -6.13581 | -53.28973 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9da24471-cb2e-3633-bd4b-24d85bf7e201 | -10.75871 | -51.66685 | 2026-10-01 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45757edb-dd14-32aa-b4ea-955d7588122e | -8.27106 | -54.75995 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 170fa6db-d67c-3517-b775-44e260ddd5b3 | -10.54973 | -50.00715 | 2026-10-01 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2607999-c60e-31cc-93a2-885212253bdd | -6.11138 | -55.70786 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6232ea86-624e-37e3-9966-ff0aea8fa4ad | -9.06882 | -49.87664 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 146a3325-1759-3fcb-960d-39af942d541b | -6.70314 | -55.05246 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a40c8ad7-3e4d-3c02-bbfe-1967d6b57b1a | -7.49947 | -54.99697 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d80f863-2fcf-3e41-9cb5-1e321c104051 | -10.84232 | -48.69423 | 2026-10-01 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c1a00fa-a15c-3183-bef1-bd470f814b1d | -7.73144 | -54.80153 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8e5aab9f-7c25-335b-bb65-458c7dd1a29f | -6.05951 | -59.91649 | 2026-10-01 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6480990a-53bd-3bd9-8141-c13497b14eea | -10.82439 | -57.21087 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README81.md)
