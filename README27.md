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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c943e168-c088-31d1-9919-b82c76f7e0c0 | -11.52292 | -39.09182 | 2026-09-19 04:02:00 | NOAA-21 | BARROCAS | BAHIA | Brasil | 2903276 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 121deac7-bfc5-349a-84d7-906da2c49d4f | -7.85926 | -45.17773 | 2026-09-19 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6aca5be9-827a-3f3f-9ae6-dcd331515f97 | -10.20865 | -46.58676 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bbaaf68-16fe-34c1-9868-4892ca470d16 | -8.37815 | -47.2042 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73690487-bfb8-3e88-8477-b6145454b0b7 | -6.02448 | -51.76901 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ab7e717e-6876-31ca-9d79-ddd7ce842d44 | -5.61771 | -45.24828 | 2026-09-19 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e9a14834-85f0-3ed7-acec-6adf39b651fb | -9.74671 | -46.08033 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88625eaf-23c8-3475-8709-3b65a7af2353 | -8.72364 | -44.87635 | 2026-09-19 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e23c681-3013-390b-9432-33d4888bde7b | -7.6038 | -45.42374 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3764b7e7-231f-34aa-a01d-863bed7915fc | -8.44376 | -45.69985 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea220e52-92d7-31e6-90e2-9f909848816e | -7.61065 | -45.43201 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57de2b4a-5400-3e6a-be24-cfbb3e02edfb | -9.80615 | -46.41063 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 66c4906b-77cf-3eb3-bb88-ef4527da0a08 | -11.22333 | -42.83226 | 2026-09-19 04:02:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 158ade11-75a6-3efb-b4ca-73a486f472d2 | -9.96058 | -46.6153 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb2a09c7-349a-37ca-82e7-44cfc5e819f5 | -3.36366 | -50.46132 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ded20bd-78cd-3f25-b6af-2f906019d1e6 | -8.37391 | -47.25427 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e008020-58c5-3817-b2c1-4a093e08d339 | -9.81229 | -46.39995 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92c91553-5fff-3bad-9da7-66bdb473a726 | -9.80197 | -48.32514 | 2026-09-19 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 657a730c-6cae-35c9-88f6-040c4596d233 | -6.77861 | -42.97412 | 2026-09-19 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 41df29f1-be65-3c56-a7a0-7ea2bed2f1a8 | -10.53444 | -46.74693 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6d527082-db9d-3b87-9456-ef899d937c65 | -7.7847 | -44.88139 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29405722-81b2-3b3b-a39e-e7afd011dd56 | -7.41051 | -49.84989 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8290436-d258-3bee-ad7f-e5c554242fbe | -9.94496 | -46.53178 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46b4edf7-8463-3723-b065-7bccbb334896 | -10.54073 | -46.60223 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57849d82-e941-300c-864d-a3572386a297 | -8.76718 | -48.66846 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2a43f5ce-ba5e-3893-8729-4098cf0743d7 | -5.33187 | -48.99188 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 196b5052-388e-3169-9d71-3ea9fe6a92aa | -6.94651 | -43.10286 | 2026-09-19 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaf24fdd-4b21-3981-9afe-4347e6e5d7e3 | -9.02896 | -48.7274 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0083962-bc94-3ab3-9ac3-b5fac5071ce9 | -7.76189 | -46.73946 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ad38a7d-0771-3e65-be28-ca2b9cc4c1eb | -6.94773 | -42.5515 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 10fe274e-5af9-351f-aa09-3b3e628e9d5e | -5.64884 | -51.70247 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2956323-05fe-3b58-8623-81581685db62 | -8.61251 | -54.61639 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c425449-98e8-314a-a29a-8a3ef868292b | -10.12758 | -45.56472 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d369f0e4-2ec5-3643-bb17-dc3917988aa8 | -10.13539 | -45.56594 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 571f7b3f-d19b-3654-b1a2-c5a471c1af8d | -7.64337 | -46.10474 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6735bdb5-45bd-3e4a-9372-95ccc4add1e7 | -10.48308 | -46.30168 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57bc3494-4485-3f78-a431-9a4a84f9b35d | -11.15927 | -42.79118 | 2026-09-19 04:02:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7aac3312-301d-34de-a06b-3ef5771a2a2d | -9.03388 | -48.72814 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1603d899-3aaf-34f6-a1eb-3605fa84f307 | -2.82546 | -50.4811 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9728fa7-46e7-3166-9191-6d78b0adf3e6 | -10.60905 | -46.10155 | 2026-09-19 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afdccef7-9689-30c2-a8db-55fdcd369a89 | -9.61173 | -45.37362 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3714ecb9-ad4a-333e-84e6-295208d6cd58 | -9.20709 | -46.76924 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34b7ac95-dd8e-3b75-9449-2a8ccc83eae4 | -6.95426 | -43.10001 | 2026-09-19 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cbceb64-f138-3b0b-89d2-d0e5f70a8ede | -9.67764 | -48.33158 | 2026-09-19 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ceffc0b0-ce58-36c8-9d20-e9eb7362cd27 | -9.84138 | -48.37582 | 2026-09-19 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f9877526-3f40-39e9-839d-e2441d267e03 | -7.64203 | -46.11266 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eaa181a4-7e80-3826-9e7b-bba529e533b4 | -6.00906 | -51.79722 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68d23a8a-b132-33cf-b596-f1cbf0b27fd5 | -4.59348 | -42.96323 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96533f4a-023e-3048-ad9e-6bee59b81417 | -8.49311 | -44.55848 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0af6c0dc-430b-3f35-8aa6-e0928188ca27 | -2.82019 | -50.47539 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 791d9448-5525-38e3-bbf0-0e0509b9d5d6 | -5.87983 | -44.97493 | 2026-09-19 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cec405f-774d-3a0c-ac47-c4d8c4ee0697 | -8.61393 | -54.60933 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 000e034b-373b-3f64-b3ac-68523e7890ee | -5.56078 | -48.45129 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c17c0b3-f9c2-3de6-902a-0838c1239e6e | -8.7775 | -46.91549 | 2026-09-19 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9202151-9570-358e-9d49-fb29726daa7b | -8.47727 | -44.53368 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b7d1032-5f75-3ae7-a834-ea8d077e3fcd | -7.67305 | -46.13379 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f142b285-f7cc-31c2-b61b-f64b17a5a1c9 | -9.70094 | -48.32757 | 2026-09-19 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 616f7cc9-b7fa-331e-bae1-d7ec41c80f5c | -9.19651 | -45.77567 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6dde608a-355e-3006-9895-b0bd9aab38e8 | -3.37721 | -50.4543 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f641c43a-bcca-3892-8a51-d151e2e8d66f | -10.52324 | -46.71309 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56269e0e-265e-3648-bf5f-436a81b5d7e7 | -10.20799 | -46.59064 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7785625-86f7-3ffe-a818-89646727d448 | -9.88386 | -46.55417 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d772550-84d2-3073-af3e-5f6cbdf435f9 | -2.81956 | -50.47289 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8f0dc961-59c1-3c06-8244-6510e11aeee9 | -7.77751 | -44.893 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7626c0a1-3e05-3593-a6f8-0f357b0cab10 | -5.14397 | -45.77499 | 2026-09-19 04:02:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5a920366-5275-375d-9106-ea808050032d | -9.7179 | -47.1327 | 2026-09-19 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 974584f2-3bc4-3877-8ebd-7d295fa40719 | -5.25884 | -50.97329 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 102845b1-13f5-37d7-a71e-fc350202e23c | -9.35296 | -50.11313 | 2026-09-19 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e181cb08-b222-3501-881b-f0967f80cb59 | -9.70218 | -48.33031 | 2026-09-19 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0edf4ba-b473-34f0-8e54-62c3b005083a | -2.82627 | -50.47638 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b809f88-9ba0-308c-b8e7-2e2f249d494d | -5.16792 | -45.42039 | 2026-09-19 04:02:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 483abc26-3f6a-3bcd-b952-da89b7eb93b6 | -6.99645 | -42.17979 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4550c8cb-b930-3ec7-8d0c-a807d9957e12 | -6.29817 | -41.80055 | 2026-09-19 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| da458549-5ced-3766-9fd7-1c7a5e870733 | -7.83567 | -44.90969 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0210b88b-31f8-3e9b-971a-f2c398545a06 | -10.59016 | -46.60023 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e5322d1-96e7-374b-85c4-2611bd8b253c | -9.803 | -46.09444 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4e9e125-cab4-37ab-9eee-a180f020b704 | -7.5822 | -43.45042 | 2026-09-19 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97112ee7-03ca-3826-bed3-88a622a197e0 | -6.27164 | -41.662 | 2026-09-19 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0869997d-2f5d-3f8e-af29-5b0fb56a9dcf | -3.55724 | -50.29379 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 202171f2-1e8b-3379-a61b-4def2df58c77 | -3.33164 | -50.11772 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdea9e67-484e-3e69-aab3-40eaebdae4e3 | -8.77674 | -46.91985 | 2026-09-19 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2f9353d5-f0ab-3497-a2ad-c17827150fb5 | -9.89358 | -46.54748 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0915b988-47de-398f-a7af-562841907c00 | -9.80431 | -48.32935 | 2026-09-19 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c732abc8-3e84-372b-8aca-d11f32b7b756 | -6.26373 | -41.66814 | 2026-09-19 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9133f425-b834-3786-99a1-d6c9edf7826b | -8.35996 | -47.24006 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efa430a9-e9fc-3633-93c4-004d74111dce | -10.39843 | -48.3247 | 2026-09-19 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be948fa3-0521-382e-88a2-f187f21a273e | -9.04567 | -48.71863 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f65f95c-04e3-328e-8dcd-6f7321089835 | -3.55795 | -50.28962 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee9ce6e4-fbcd-379d-81a1-a24010677677 | -9.56887 | -45.48423 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c683224-b7cf-3f23-b7ef-7c12baf90450 | -9.55811 | -46.58184 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97de86c5-43c7-34dc-aed2-500bde5bf54b | -4.36257 | -47.78492 | 2026-09-19 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2d9eea41-abc9-301e-8d5b-1607b40ae3ed | -7.19265 | -50.82539 | 2026-09-19 04:02:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22dbd7c3-1149-3f2b-b3cb-963b79ba9a71 | -9.03288 | -48.73375 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2e7436c4-0680-31c3-b2b4-aaddfe038e3d | -10.40395 | -48.32067 | 2026-09-19 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 10165681-5d60-3bb1-8409-80f77589e588 | -7.85847 | -44.86824 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5e79f689-80ab-3b0e-9507-e2d44f467675 | -10.50399 | -46.71719 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbcab087-642c-350d-b976-5c49acfe5379 | -10.61185 | -46.10931 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3948f93a-7822-31cb-88fb-465d72e28256 | -4.87471 | -40.81648 | 2026-09-19 04:02:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ea8d06ad-e580-30cd-979e-2e811d7c5b6a | -10.47821 | -46.30483 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9013b417-df04-3ded-b6b8-83659877fa18 | -3.35688 | -50.4648 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README28.md)
