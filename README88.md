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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cd0a7f9-5e00-3763-9c41-de633f5434aa | -2.38626 | -51.283 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aaeb2ca8-8e83-39d1-b8c6-228ad9480d3b | -2.38569 | -51.28671 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 647cbffe-8275-3bf3-8c7b-9ff9a698cf97 | 0.06876 | -51.60535 | 2024-09-26 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b99491f-7bde-35c6-a96d-764a8bc8a7b7 | -1.11159 | -52.17427 | 2024-09-26 04:55:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ece3bc9-1732-3f9f-8f36-76d5092641fe | -1.88597 | -54.8969 | 2024-09-26 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7131eb98-f7d0-3f9e-b2c2-8e71e0dd1a0f | -1.88339 | -54.71453 | 2024-09-26 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 54bb9938-89f3-307a-baa5-5f03a8f581f8 | -1.88257 | -54.89638 | 2024-09-26 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ab626d28-5759-348a-9141-b5da5c618956 | -1.88002 | -54.714 | 2024-09-26 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6cecf772-a38e-3d6d-8eb1-d6ca773a1005 | -1.34155 | -54.65483 | 2024-09-26 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6daa9d1a-7dc9-3596-8811-c440a2b92361 | -1.34097 | -54.65848 | 2024-09-26 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 05dae00a-adcb-357d-9576-bde67b57819c | -1.3404 | -54.66212 | 2024-09-26 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 591d877c-aea5-37e6-b4cc-975168f55ed4 | -1.25017 | -54.19535 | 2024-09-26 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11f278d6-32e9-332e-8495-c2eb933f60a6 | -1.22632 | -54.22077 | 2024-09-26 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 453f944a-6900-375b-a388-364eadb8d834 | -0.94652 | -53.72553 | 2024-09-26 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb7553be-3fcf-3c7f-b70d-48ba7d51df0d | -0.94598 | -53.72897 | 2024-09-26 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78961737-a148-3bb8-9099-2361a00a4b66 | -0.9432 | -53.72503 | 2024-09-26 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fe4912e-d889-3d85-8c82-fb49ff555996 | -1.05188 | -53.36093 | 2024-09-26 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10f14001-7c84-3684-89c8-83351640cdfb | -1.04889 | -53.35336 | 2024-09-26 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 697c68ba-e2f0-3977-913f-2035ff94cf92 | -1.04835 | -53.35678 | 2024-09-26 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9278ad4d-cad5-358c-85af-a80519721c6c | -1.04781 | -53.36022 | 2024-09-26 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 22a994e0-ed4f-359a-93fc-588e02edbb98 | -1.04727 | -53.36366 | 2024-09-26 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 872c894a-0e01-3c0b-9cf8-0c60c1fde2af | -1.04559 | -53.35284 | 2024-09-26 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2fba71a4-9b23-3009-b829-5d4ec850ac9e | -1.04505 | -53.35628 | 2024-09-26 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2df28c21-581d-3922-b5b7-4d4d608ccad6 | -1.50292 | -55.10177 | 2024-09-26 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e4a07a1-6ba6-36d2-8a93-23564792d9d8 | -1.4695 | -55.49615 | 2024-09-26 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81f3290e-b743-3ec7-9076-443932ff07e4 | -1.41531 | -55.43272 | 2024-09-26 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 512cf910-ae99-3bf8-a828-3966d21eb1f8 | -5.95516 | -43.27925 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 097328d1-975e-3b8f-8796-ba2de642aa7c | -6.32979 | -42.50982 | 2024-09-26 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9bb41394-633e-3559-bff4-50d3f28bfc32 | -6.3236 | -42.50837 | 2024-09-26 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3d08f442-17be-3ee9-81b1-ed01b8339634 | -6.31742 | -42.50687 | 2024-09-26 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b4027306-ee43-3e5d-bd56-662cf143e053 | -6.31674 | -42.51182 | 2024-09-26 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 85c3bae2-e35a-3c0a-87cf-dd302cc78911 | -6.31539 | -42.50589 | 2024-09-26 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ce78ac59-af72-3b34-ac26-17cf5fdefe42 | -6.31475 | -42.51085 | 2024-09-26 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0ba413bd-a303-35ae-92a6-10d3e7e3ef68 | -6.31053 | -42.51057 | 2024-09-26 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7b601b99-d07c-37da-9445-bba64d85d457 | -7.59461 | -42.2901 | 2024-09-26 04:57:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 093fe738-32db-3c1b-8675-e5e570fc4d22 | -7.59391 | -42.29546 | 2024-09-26 04:57:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a3a0f537-5c4a-39eb-8ac5-bc032195b207 | -7.58738 | -42.29517 | 2024-09-26 04:57:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5e904743-4e29-37e9-a786-19f7874b9e04 | -6.54701 | -43.02654 | 2024-09-26 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 69aa6bb6-2490-3f69-8658-28f906ff7481 | -6.54636 | -43.0313 | 2024-09-26 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7f478dd1-354d-3b2a-9d88-a508960f452e | -6.54571 | -43.03609 | 2024-09-26 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d22c8e1-ccfd-30b7-a212-1fa947e5f121 | -6.54028 | -43.03046 | 2024-09-26 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f495c7e-c703-3804-8da8-6f2767983a14 | -6.53965 | -43.03511 | 2024-09-26 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8a43b67-d8aa-3851-8b21-b713246182f3 | -8.06728 | -42.88519 | 2024-09-26 04:57:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ade4c0f1-28b4-3d07-9807-12bda30c7e8f | -8.06662 | -42.89021 | 2024-09-26 04:57:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b05ce177-411b-3df3-96f5-a2369e09b86b | -4.66748 | -43.75827 | 2024-09-26 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b951e5a-94fa-3b3c-8cb8-c734d69ec3c2 | -4.66695 | -43.76215 | 2024-09-26 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7449b66-6cce-35ed-82e6-f22e12a90522 | -4.6639 | -43.76035 | 2024-09-26 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b058520-0da4-3c63-9988-de8a1d5c2197 | -4.65995 | -43.74787 | 2024-09-26 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1d5abac-7204-322e-afb0-95f2f92aef82 | -4.65771 | -43.76323 | 2024-09-26 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93352eaf-250c-3cd9-804d-9241b4c0daa1 | -4.65727 | -43.74871 | 2024-09-26 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b72d58c9-d18c-34c5-ab10-9355fec50b57 | -4.65431 | -43.74696 | 2024-09-26 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 244756e7-4dc9-3e89-80a4-c39e5d8ff158 | -4.05767 | -44.04868 | 2024-09-26 04:57:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c300fc52-d0fd-3a36-a840-34e3a0acc7cc | -4.05715 | -44.05221 | 2024-09-26 04:57:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 43563437-221f-3288-a941-11955593ff3f | -5.8956 | -43.88264 | 2024-09-26 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f39cd459-479b-381a-82cf-780f3b09b373 | -5.89502 | -43.88681 | 2024-09-26 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48082c40-ebe7-383f-ae9a-b9a582066036 | -5.88991 | -43.88171 | 2024-09-26 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c345998-140c-38ed-b54c-3118dda58caa | -5.63314 | -43.63594 | 2024-09-26 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd7d6d97-a1c4-3c37-875e-332037fac726 | -5.62793 | -43.63111 | 2024-09-26 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 404aabe4-ee60-3d85-a07f-952db95e2974 | -5.62736 | -43.63515 | 2024-09-26 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 35caa88f-78f8-38ce-9174-bf72ec020342 | -5.96771 | -44.57951 | 2024-09-26 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f92a8e96-6fc4-3c12-9d80-cdc05421cb55 | -5.96227 | -44.57858 | 2024-09-26 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a8484a2-ed4b-3835-9c88-2da24de5d6ae | -5.79735 | -44.1478 | 2024-09-26 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb635233-1371-3e67-8126-0c45a3476288 | -5.721 | -44.81531 | 2024-09-26 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3c25d4c-4750-3677-8cbd-33896fd6fd0a | -5.71518 | -44.81794 | 2024-09-26 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94e5e184-8ecd-3c62-85d9-2f0cf1883dbe | -7.84276 | -44.91458 | 2024-09-26 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3d6906d-ddb7-3dab-adcd-bcdea2557267 | -7.68218 | -44.63896 | 2024-09-26 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0e490c1f-2346-3162-be4f-7dc4f1204196 | -7.68165 | -44.64299 | 2024-09-26 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 42058efb-40d5-3f85-ac5a-c9fb894bfd98 | -7.68113 | -44.64695 | 2024-09-26 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3075adfe-6af0-38cb-ae2a-551a1c4d927d | -7.20912 | -44.09196 | 2024-09-26 04:57:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff6c2448-06ce-32a5-b277-00c1f683444d | -7.20861 | -44.09582 | 2024-09-26 04:57:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b128f45-0a06-3910-9804-461c819c000c | -7.20341 | -44.09098 | 2024-09-26 04:57:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 821baabb-4ffb-3aae-b874-b29f30be4637 | -7.20292 | -44.09473 | 2024-09-26 04:57:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fbe7ba9c-4cfe-3661-885a-7d131e589a6d | -7.20126 | -44.09327 | 2024-09-26 04:57:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a11315a8-cff8-3c65-b11f-0d4f7d010286 | -7.07529 | -44.16407 | 2024-09-26 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e43e62fb-8306-3d49-aedf-40f4133ad259 | -7.07336 | -44.16214 | 2024-09-26 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75de5709-cab3-3446-825e-15913679e1fe | -7.06962 | -44.16304 | 2024-09-26 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b8205a0-525e-37f9-9bd3-3aae9ff867e2 | -7.06717 | -44.16494 | 2024-09-26 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46938f3a-84b5-3868-b4a8-44c6296925d2 | -7.31916 | -44.74687 | 2024-09-26 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b91a7840-aec1-3daf-8dfe-06848efb4e85 | -7.22281 | -44.79329 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4eb0ba3-712b-3d95-aaf2-5b71370010fd | -7.21782 | -44.78889 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70ff5552-c338-333b-bae7-9e42f2d6824a | -7.21735 | -44.79241 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b102a58-2a57-35cf-8c5e-2b1ca7a1f297 | -7.12735 | -44.83271 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4cefff41-f7d5-3940-a6d0-1c246ec87c3f | -6.78677 | -44.72959 | 2024-09-26 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b65ff03-dcfb-3a05-a176-7ad35bf49c96 | -6.78644 | -44.72385 | 2024-09-26 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 850ef66d-937e-3be0-9b95-a630e5442c26 | -6.78633 | -44.73289 | 2024-09-26 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89a575d8-c4b4-390a-a2e1-c55d2ed45f41 | -6.78596 | -44.72722 | 2024-09-26 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38ad9186-0f00-393c-b36b-99b0a7cfa618 | -6.78549 | -44.73055 | 2024-09-26 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89d4e900-4960-33f8-8f4a-892e86486c20 | -6.78087 | -44.73213 | 2024-09-26 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4033d9c7-0a8c-3f4f-9b57-4b599fa15123 | -6.78003 | -44.72979 | 2024-09-26 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c60efb4-b2ed-357d-b1ea-faa7eb1fca9a | -6.77956 | -44.73312 | 2024-09-26 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b8255ea-e548-347a-8fc3-697f00410cec | -6.57862 | -44.93069 | 2024-09-26 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8eeb4f84-b22a-3555-9fbe-5ff289348e63 | -8.68638 | -44.74726 | 2024-09-26 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29afd1e1-1b07-396d-b122-baa82e956c69 | -8.6808 | -44.74634 | 2024-09-26 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2612052d-07f2-3e07-bf17-fc9b7e90d8cc | -8.55717 | -44.06623 | 2024-09-26 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f376845c-5d15-3bc4-880c-a260bdc5b9cc | -8.55127 | -44.0658 | 2024-09-26 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa0af950-7a20-36be-9e3c-48a042211fba | -8.23424 | -44.8468 | 2024-09-26 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdd3c1ba-c40c-3487-b301-d2158d786219 | -8.23374 | -44.85054 | 2024-09-26 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fb7e42d-530a-3c39-90a5-89ae885b6307 | -8.23323 | -44.85429 | 2024-09-26 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee76b958-8091-3607-8514-392d1020224d | -10.6357 | -45.85334 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24499666-24f4-377d-83f2-9b700ee9f464 | -10.63525 | -45.85691 | 2024-09-26 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README89.md)
