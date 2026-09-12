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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 014875fd-e3ad-3060-b9f7-cae4e8ca416f | -6.76208 | -58.62008 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6821c58a-d302-395f-9640-4271985ff8d9 | -6.23666 | -51.69693 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c360ca47-a855-3471-8041-4765850b373f | -6.11315 | -55.63493 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9ac127e-0fd2-39e0-9f53-e2aa95dddc85 | -8.09363 | -54.83776 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3808a38-a205-3aa6-8b6d-c93cc2913b76 | -6.23713 | -51.69366 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7351c8bf-fb29-3a8a-b8b6-d4f97263699d | -6.20864 | -55.26898 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 463436dd-fe92-3bd1-8b63-18cff1948ef8 | -6.00779 | -57.67448 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4851b94-6eeb-3ec8-940b-9eb63333ee7e | -6.07575 | -53.49274 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b7c573f-0da6-322f-93b9-0d0c7a3bb6ec | -5.98082 | -57.77886 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ebf54e-11c2-3435-8307-ab906dd48839 | -6.10244 | -55.65128 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f78c56b1-fb0c-3067-8690-c416f0dff0fa | -6.84371 | -55.81067 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0df5ebd0-4fcd-3245-937e-bb675e65511a | -12.13677 | -48.97632 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7f93a0d9-98d4-31dc-9682-9e977a13b303 | -6.09613 | -59.90173 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b8b0e82-78d0-31f8-82ad-1a1199937eae | -6.21278 | -55.2696 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f717f7f9-0f7a-395c-8d49-61202b9fa2a0 | -6.19852 | -57.72578 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e01a9b98-5d1b-379b-823c-01b2d9cc1bdd | -6.29087 | -56.01948 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd46a1ca-d549-33b2-b3b4-15aba3de90fc | -6.60423 | -58.84676 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58965d28-3a26-379b-92e8-9c9c8e17f994 | -6.23619 | -51.70024 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26016b9f-198d-3210-8207-ef0f835ba4d9 | -6.20533 | -57.77692 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4258de2d-f34a-32ec-a7c1-702f65e373b2 | -6.28499 | -59.93093 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 356bab76-411f-3680-b328-846dcb2c47c0 | -6.8811 | -55.64426 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aa07b63-c3f5-3d00-8d6c-7027f54aebb9 | -6.10943 | -59.90383 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dfa091f-cbae-3574-9f0a-e698671aea75 | -6.18654 | -57.73237 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d407cf68-2568-3473-87a3-1b4987f9f58f | -12.13101 | -48.96593 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df5827ed-c818-3da6-91a2-e3260b73830a | -6.40177 | -54.97833 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 394ca1ee-fa98-323b-a163-6b9fff411395 | -6.24634 | -51.70487 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eeab8d6-e205-3b76-a412-c642aad443cc | -6.11512 | -55.64925 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51e7845e-5ff5-30c2-ad18-f1a9c029c80e | -6.2056 | -55.26076 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 497f9a57-ea97-30a7-a2c4-00bbffc30e1e | -9.98723 | -59.86483 | 2026-09-12 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f70fd65-9d8b-31e1-943e-0d32f46b9bc0 | -6.1747 | -57.71386 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d36b747-5b89-3204-810c-f8afe2cfcafa | -6.81105 | -59.43233 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 517ea92f-fdbe-323a-80a6-73eb2b84d85f | -6.11615 | -55.64241 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfacbf76-568a-30b2-ac7c-e8d3008a0176 | -6.12968 | -57.6832 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0caf031b-e786-3669-8857-be889a9c0f0e | -8.61013 | -70.97151 | 2026-09-12 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ed5270b-1fda-3fa6-a51f-725cb5409b74 | -6.43065 | -56.10489 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25f52686-5901-36b8-9ba4-49f65bd91a91 | -6.18359 | -57.72771 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c773605c-71be-3b25-b699-969057765449 | -6.28692 | -56.01893 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69919175-95e1-34ca-be32-82d4111d0182 | -6.503 | -58.38527 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7c99c18-8259-33e1-bdc7-0ed0c258bb63 | -8.75895 | -70.8135 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5c68d2e-5977-3ab5-83be-ea4d5578e3c3 | -6.81961 | -58.99318 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec61bd20-1132-31ab-a09b-d625de59ef2b | -9.74134 | -64.95652 | 2026-09-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccc4463a-c1bd-30a7-a320-05838e020f2b | -8.84408 | -71.36821 | 2026-09-12 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b42f5d41-8ebb-336f-a87a-4628b9c3c152 | -10.51163 | -57.44872 | 2026-09-12 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6067a411-0ea8-31db-a6da-f3c4f581b009 | -6.24291 | -51.69107 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a24aa1d8-bff2-3243-942d-0e3782e35234 | -9.70783 | -54.35089 | 2026-09-12 05:29:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dccaa90a-fca1-3e28-92f4-0e20fd3784e2 | -6.87865 | -55.63277 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 194f723d-03a2-3d55-9faf-3cb57fdb4dfc | -11.08416 | -50.8371 | 2026-09-12 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f49ff83-0bc9-3e5a-b979-4cf30037dd4a | -10.54799 | -51.33837 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 91d06539-b65c-3237-a8ef-33dc79cfa32f | -8.07298 | -54.85655 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04ac7ebb-0eff-35ef-8bec-e7c9e52d6777 | -6.88356 | -55.65565 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a289df9-5e3a-34cc-a32b-6a46ee552ccc | -9.17315 | -68.21847 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 50f48428-b94a-34d3-8f31-a9c32e2e8524 | -6.09946 | -59.90226 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0764d075-9ed2-3c0e-a78e-2f94ec5a4ce4 | -9.31015 | -68.77824 | 2026-09-12 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85c1cd2f-9cb6-3099-92f9-073f4c87f4ca | -6.79422 | -58.79501 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e535fc5b-9421-3f5b-92cf-f4197c270ff4 | -8.60747 | -69.6603 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a979dc49-c09d-3c66-a687-05b45aed6727 | -11.24846 | -54.13676 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 344bb5a3-a8a4-3daa-800b-058183880541 | -10.56242 | -51.36295 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e53356c7-4e13-3063-8daa-104d826a09d6 | -6.10545 | -55.65865 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b4926a9-449c-3551-8a61-03205ce2e2bd | -6.11155 | -57.63391 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2637a883-1130-3f6f-9ff9-10848ddee633 | -6.1811 | -57.74412 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a55a74ab-df5d-3068-949a-bdbea76df19a | -9.18675 | -68.22076 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30e89eaf-bf54-3ef1-9aac-ad1a030242b1 | -6.11969 | -55.64632 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6038e8d-a1fb-3ae6-8052-d28180de600f | -6.61735 | -58.8526 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5e9ca06e-50a4-3558-bbed-6e1114a9b7df | -6.23321 | -51.6832 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 336db42a-aad5-33b2-8cb1-023a18452864 | -6.88274 | -55.63334 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4422ff5-f44c-355e-818f-e4f8d3906c85 | -8.50167 | -50.15089 | 2026-09-12 05:29:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfd9604a-6eb4-3c34-86e2-95f64880c7b3 | -11.42849 | -51.4303 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5f8cd31-0fbb-3b9a-9539-3ac254173e06 | -6.84934 | -55.80057 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35487b22-3435-3154-adbb-5003973b1e05 | -10.51479 | -57.45402 | 2026-09-12 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 451179b4-54d3-3492-b4ce-8b6521587f1e | -6.20891 | -57.77743 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2af65dff-a64a-3900-a4ea-fddf1963f9f9 | -6.10511 | -55.63355 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eba5dc84-c8ef-32cc-915a-f13ee2a226a4 | -6.28633 | -56.02763 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6785c1a-fb00-3120-a84f-28eeb042a8ed | -9.14311 | -68.20371 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9876f43-e92d-361f-a645-5b28215df01b | -6.1 | -55.64007 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61e69661-4221-3427-a18b-3b3bf50840bc | -6.60766 | -58.84731 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8c977d0-986b-3869-b211-b01ff3b7be99 | -6.10701 | -55.64835 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a45f3fa-3de9-3e3a-ad08-a1aca812d95a | -10.68443 | -54.16499 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d35e1fd-15ac-3fcd-a19a-b3e1fb5d687b | -10.23829 | -56.25957 | 2026-09-12 05:29:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 117977ca-488c-3954-a39b-6551f5fd3051 | -6.8162 | -58.99266 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31fc24c6-1f96-3712-a098-0f0f335a5899 | -11.2395 | -54.13029 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02e63878-caca-3876-b68b-1d51c75d1299 | -11.23881 | -54.13552 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5f67322-2378-3998-95fb-1da945d27435 | -6.84598 | -55.25029 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33256132-7597-3af1-9521-c679e2f19d7a | -6.10858 | -55.63787 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70dbde35-ed7b-303d-9467-bb09b2e4e48c | -9.30546 | -68.7774 | 2026-09-12 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5f00798-d009-3469-8044-f342640a6200 | -6.37937 | -58.28902 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28007e14-a17a-3b86-9a37-f4206679e4c2 | -6.88844 | -55.64769 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc6b8a10-bd8b-3448-90b2-147433f4c542 | -9.63806 | -49.68066 | 2026-09-12 05:29:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8779e165-e35c-3c91-923a-644d57b96112 | -8.50772 | -50.15171 | 2026-09-12 05:29:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 258904ec-1695-3211-90a7-959de39ffde3 | -10.5388 | -51.36477 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4febae3-cccd-33d9-8162-eb075dd984fb | -8.5711 | -54.56453 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dfb11e6-4c14-36c6-8e6d-29f3105df1b5 | -6.87921 | -55.62907 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa17b98f-555c-3b92-9431-1ae9c63b261d | -6.33497 | -55.85596 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f7be127-bcd5-3a7f-b27b-e99c019302b1 | -8.85038 | -71.3655 | 2026-09-12 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 363349cb-c6db-3f0b-b058-e3645001d89a | -6.81562 | -58.99635 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f77bac9-a579-3032-a6a3-f8847569456b | -6.88164 | -55.64065 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00cf8660-c6d1-35cb-8f19-8ee9662ab021 | -6.07974 | -53.49805 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d8d69e0-ba0e-3723-b81b-e7f7f57540b5 | -6.60993 | -58.85526 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 679ef83a-df5f-3491-a605-ed08ebafb610 | -6.10295 | -55.64788 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3729a092-cf09-37a9-86df-dbfc5b3e98ca | -6.76949 | -59.43323 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21416795-88a5-3fe4-a8fd-7bd3dc324915 | -8.09427 | -54.83345 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README53.md)
