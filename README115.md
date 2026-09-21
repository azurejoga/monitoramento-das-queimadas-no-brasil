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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3de79293-b48d-3376-ac0a-30768efd7a96 | -4.1025 | -52.13465 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 46e2984b-a9dc-3e12-88e9-1edc3683f2aa | -6.73223 | -55.07574 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c53ad24f-e62d-3d01-9ff4-9a97362657cb | -11.11451 | -54.01253 | 2026-09-21 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 0bbd6c15-cb50-3025-8a06-87a70d1f40cf | -5.76111 | -57.587 | 2026-09-21 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 386915b1-6df2-3171-a28b-395f1ed5d3ab | -12.40821 | -58.2039 | 2026-09-21 12:44:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 73379101-5503-3286-90c7-35be1f1a7841 | -7.32099 | -54.9155 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8092c292-586c-3c6e-9287-9edab5ffa9ac | -12.1754 | -57.50734 | 2026-09-21 12:44:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 63565c61-4074-343e-b7d7-e8088fe7ec1a | -3.82381 | -59.3274 | 2026-09-21 12:44:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b602237d-6773-3977-85d6-8ad34da73754 | -3.11122 | -60.71987 | 2026-09-21 12:44:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 42fd198f-629c-3c8e-9cc2-75ae90db1fdb | -6.46739 | -59.98439 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 999dadea-ea36-342c-be23-adc3ad7559c2 | -6.20392 | -57.78945 | 2026-09-21 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b1ecbbda-02c0-351b-903a-d1f605d24599 | -5.20215 | -56.11672 | 2026-09-21 12:44:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 174018d8-ffd9-3ceb-ada9-6a204eb0910f | -6.45285 | -59.97643 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 458cc1a0-029c-3084-ac88-fe09931cb252 | -8.1813 | -54.75166 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1d29b3a7-1987-3fd8-907f-7d27121cc451 | -3.16978 | -58.58714 | 2026-09-21 12:44:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ec798095-2146-3c32-af72-3d7936837771 | -9.24434 | -57.14675 | 2026-09-21 12:44:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 33649042-c576-3ed6-9c2e-922a81fc8323 | -3.39256 | -59.52324 | 2026-09-21 12:44:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f5d6795d-2aac-3cd6-bcee-9fdbe0122b4b | -7.57348 | -57.68242 | 2026-09-21 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| b06a31cf-43fc-3326-abd9-cda338ca82aa | -4.46055 | -55.68735 | 2026-09-21 12:44:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 8047bd40-6045-31ab-a9bd-a278eacee8fb | -5.92837 | -59.95601 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 328.6 |
| 1854f800-cb09-32fa-a553-5e501657421a | -5.93636 | -59.96723 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 814c5d71-15db-3e34-a7bf-59a9ec4a80f3 | -5.97782 | -57.77588 | 2026-09-21 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 98d360bc-0ab6-3e50-b2c9-d5737c20f966 | -8.60655 | -54.61371 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 40a5c215-1924-312c-bf20-88f405bfeb07 | -7.32332 | -54.9461 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| e6dcec75-e690-3222-a50e-54478d0043c0 | -7.25543 | -55.60423 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| a14cf9dd-8ecf-3f7a-bcf8-ee2a6f3754f1 | -11.0491 | -54.16914 | 2026-09-21 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5e7a2c90-435a-3a9d-b95b-dc831c82985d | -8.18443 | -54.72576 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 13226423-24df-3636-9255-8ee4dc47a1d3 | -8.79812 | -60.79435 | 2026-09-21 12:44:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1a2c11aa-e9f5-3328-83c7-30f7ec656ee0 | -2.9987 | -60.79824 | 2026-09-21 12:44:00 | TERRA_M-T | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 6cf5f312-8195-33d3-a3c9-aefd9bb6bab7 | -9.76111 | -60.76479 | 2026-09-21 12:44:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 28f99792-4ad8-3b22-923e-550156078326 | -6.75681 | -59.11647 | 2026-09-21 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 303df4a7-d236-3917-9a6b-5407edbc29d3 | -2.87892 | -57.81005 | 2026-09-21 12:44:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| fb16b622-24c6-38aa-a8b4-c05285c62071 | -6.19304 | -57.78809 | 2026-09-21 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| dd9f01e9-e28b-375b-b5c8-fcda5d050240 | -7.58468 | -57.68387 | 2026-09-21 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| db6175ff-6d2e-3446-abf1-b2ae076c6e66 | -4.34893 | -55.64664 | 2026-09-21 12:44:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 8575bc53-4303-3eea-9c3b-19fb237c43d3 | -10.21105 | -60.70178 | 2026-09-21 12:44:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d123986c-8dee-3be4-81b2-f0899ac47033 | -3.44334 | -58.23296 | 2026-09-21 12:44:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 1fa8fe6c-ac23-3506-9967-4e4d95443ee8 | -5.93773 | -59.95727 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 9356807b-0078-3ce5-bce8-54e23c4429de | -7.33236 | -55.21095 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| b08aa461-e14b-317b-8b65-eff86dff8edc | -5.00903 | -56.0977 | 2026-09-21 12:44:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 341405b1-78b3-3add-a415-b36ad0156375 | -3.65168 | -58.86035 | 2026-09-21 12:44:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| dc1e046c-8d2d-3502-b229-9cb6b1e1d9cc | -3.2903 | -57.85869 | 2026-09-21 12:44:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 664deaa4-c5f8-35f6-9de4-a9b9c4f6cf1a | -4.0109 | -53.5029 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 7d99d886-16bc-3ced-9a23-b7554968c0c6 | -6.30814 | -60.0117 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| ab8c0277-11e6-3f8c-8dc4-cc4ebd0d396b | -7.33389 | -55.5998 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| c68e5f2a-7c9e-330a-8325-61f650994543 | -5.92974 | -59.94603 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 7b5aa7a7-7a3f-3d7b-80ce-862fdbf80b94 | -7.57544 | -57.66763 | 2026-09-21 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| eef50d12-9a0d-3b18-8972-3e42d747d56e | -3.75623 | -59.42545 | 2026-09-21 12:44:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 28efeb1e-3700-3250-b44b-24c0110b9d1d | -7.31781 | -54.93993 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c89b65a0-95cc-318c-8763-50f8dd9b1a2e | -7.33467 | -55.61483 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| af26e3b1-4cc5-38d1-8ace-39efe496e6ea | -7.31876 | -55.20872 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 024059bf-cda5-3fe0-befd-97ad2fc0f629 | -5.8482 | -53.508 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 93304d4b-dec5-3708-bbae-d4ec43fb823e | -7.24539 | -55.59727 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 391fa480-8f78-3be3-8e5b-5d04b1289b55 | -10.22353 | -59.40194 | 2026-09-21 12:44:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 3a55225c-923c-3eba-8016-3878e673071a | -3.75765 | -59.41542 | 2026-09-21 12:44:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ad575eb2-ff44-3d80-ac5c-894af797a348 | -9.48543 | -65.49711 | 2026-09-21 12:44:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 40dd5ff4-d054-3311-83a8-e523cda0265e | -11.99055 | -58.07167 | 2026-09-21 12:44:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 8c73e31e-f173-3c62-858a-4026c6757050 | -3.24487 | -60.88659 | 2026-09-21 12:44:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ebb2731-a2d5-3fc5-9b3c-d356ad3a96fa | -6.46224 | -59.97769 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| b03f5c04-c742-38d4-9a1d-6da59ef0d86f | -6.35808 | -58.28622 | 2026-09-21 12:44:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| bce3a7ee-0a49-33a9-9fbb-b0a87a4a18e9 | -2.86862 | -57.80867 | 2026-09-21 12:44:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 8f021bfb-9c0e-3718-bb44-ff7884fae616 | -4.34648 | -55.66482 | 2026-09-21 12:44:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e2b39303-4a56-3e33-828c-3f18caebb819 | -6.73811 | -59.41485 | 2026-09-21 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| eed0d8f9-877b-3088-bb06-2a4d7d8b380c | -4.46454 | -55.6746 | 2026-09-21 12:44:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| cb188680-8228-306e-b67f-c324882c88d8 | -6.74638 | -59.42707 | 2026-09-21 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 80b6cb9a-12c8-3c08-9ffe-b31b3d3ad78b | -4.29698 | -56.26076 | 2026-09-21 12:44:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f29f23dd-ea79-39e8-abca-3d2bc9e1b9d2 | -12.48152 | -57.58734 | 2026-09-21 12:44:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 28462923-93e5-35ec-a6d7-6fb2bbdc395c | -6.46877 | -59.97424 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5e8d0aa8-2927-3019-9e25-e7eb094a4cf9 | -11.05263 | -54.13691 | 2026-09-21 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 075b312b-51c5-32b4-a806-1eeeead7ce6c | -12.46899 | -58.55256 | 2026-09-21 12:44:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8cc772a2-d1d8-3586-b65e-7b136c466cab | -3.39115 | -59.53307 | 2026-09-21 12:44:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4f9c14a5-df3a-3e6b-b0eb-40cbcfafbd69 | -12.00222 | -58.07309 | 2026-09-21 12:44:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 2b7dfc2e-a9b8-389c-8ca7-4b889915315b | -6.9233 | -62.90586 | 2026-09-21 12:44:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 060a5c47-6692-396b-94de-bcbff2b7d7a4 | -3.39856 | -59.52999 | 2026-09-21 12:44:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 63acd2f7-fee4-3708-9bf2-5e7d1e872032 | -8.17816 | -54.77754 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 165978ef-f61a-3081-a74e-8fd88f86653d | -6.3816 | -60.00788 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b2230d6d-dd3a-3939-be46-8cb03b918780 | -6.75318 | -59.06935 | 2026-09-21 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0212746c-ec52-3464-956a-b51d78e2f586 | -10.58999 | -53.98383 | 2026-09-21 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| af78a19a-d4b5-3cb6-8040-d13d8acb1230 | -5.42273 | -60.21526 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d1ce70bb-8ef4-37c1-8e3a-bf600e960bbc | -5.77208 | -57.58841 | 2026-09-21 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| c8f46a67-4fbe-3199-ac24-b8d0b3903139 | -6.69631 | -60.00698 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cc342a1e-f5b1-3891-b1b8-d66f050b9c4a | -6.16004 | -57.94994 | 2026-09-21 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e04b061d-5b4f-3541-9fb7-dcef4b78794e | -9.54698 | -63.77922 | 2026-09-21 12:44:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a9e2d722-ff6a-3d54-a8a0-560558cffc5a | -6.38025 | -60.01775 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5ea99619-bdb5-33a5-8ca5-e60e28568d8a | -4.09177 | -52.13999 | 2026-09-21 12:44:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 11b31e99-eadc-3568-93a9-632cab19c2ec | -6.73664 | -59.42575 | 2026-09-21 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 0d3da6ce-294d-31a8-a716-105b4940dd24 | -6.72229 | -55.09185 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 6bfeaae8-26ab-3afd-a671-f9533cd57333 | -5.01136 | -56.08014 | 2026-09-21 12:44:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 243d8210-534f-3acb-a9c2-d77316224c3b | -4.09627 | -52.1039 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 905e0555-16de-3c01-8315-ad12527fdfc6 | -6.79525 | -59.13912 | 2026-09-21 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 61ed0e44-30a4-3943-8a06-bb649c862b13 | -5.84431 | -53.53782 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c52f8ad2-2069-32e8-bd8c-ff4c74a74482 | -6.65632 | -58.43433 | 2026-09-21 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5d7b851f-efa1-391a-99bb-74abe69f9c7e | -5.20452 | -56.09892 | 2026-09-21 12:44:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 9f97e144-7f9c-344b-8809-c43edf90724c | -7.25814 | -55.5826 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 04025e1f-41ab-3732-a224-5d225ee563ec | -9.03861 | -61.65101 | 2026-09-21 12:44:00 | TERRA_M-T | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ce926b18-06fb-37f1-819e-d9323a47a4ba | -2.79562 | -59.88973 | 2026-09-21 12:44:00 | TERRA_M-T | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 775919b5-3e89-335d-aa95-105b91ba29b0 | -3.66124 | -54.2724 | 2026-09-21 12:44:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 731462f2-8a21-3391-a759-08f12fc81f72 | -3.17958 | -58.58848 | 2026-09-21 12:44:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a74c5462-c3e5-3f3a-81da-36b8d7a241df | -7.59788 | -57.67052 | 2026-09-21 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 1bfb40c2-cad2-3a1b-9ff3-b01bae480864 | -3.54451 | -58.68489 | 2026-09-21 12:44:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |


[Clique aqui para ver as próximas entradas](README116.md)
