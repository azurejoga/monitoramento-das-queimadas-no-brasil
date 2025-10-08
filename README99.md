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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e90d3fda-3ad1-34ff-b8a8-c6c5aa148a31 | -14.72275 | -46.07184 | 2025-10-08 11:40:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 94daf45b-a78e-3fdb-bec4-cb44c1ac98e2 | -12.57013 | -42.39233 | 2025-10-08 11:40:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 0838717a-766b-3686-b46e-a9a0f074667d | -12.70218 | -40.54512 | 2025-10-08 11:40:00 | TERRA_M-M | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 50cc885d-c057-3847-ba6d-d4ba684c3c14 | -12.4292 | -45.63127 | 2025-10-08 11:40:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 2903fb8f-861c-38e2-a5a8-92072dccfb7f | -13.74125 | -45.66416 | 2025-10-08 11:40:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 43b81099-68d1-310a-af3b-145dcec5a18b | -12.23643 | -43.77736 | 2025-10-08 11:40:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| fdd36d11-5333-3ffe-8e77-11018cc74326 | -14.70998 | -46.08493 | 2025-10-08 11:40:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 3b633fc5-8576-3ca8-87cf-ed810fc0d3de | -14.62482 | -41.08777 | 2025-10-08 11:40:00 | TERRA_M-M | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| cab60d36-b2f4-33fc-b861-e5433ca5d60a | -14.21419 | -43.45864 | 2025-10-08 11:40:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 7280496f-29dd-3f02-abb1-c84554594246 | -15.8977 | -43.26175 | 2025-10-08 11:40:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ff5c4151-4eaf-33d4-85b5-27f8c43cc698 | -13.81161 | -45.79119 | 2025-10-08 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 345839ef-b6b6-3f9d-896c-7859bbe452e7 | -15.47485 | -41.97974 | 2025-10-08 11:40:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| f8216f05-cc70-324c-96a8-33209c1cfbc5 | -15.36972 | -47.30277 | 2025-10-08 11:40:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| aa59e4f7-c217-3570-af65-65548958ceb7 | -14.21647 | -43.44456 | 2025-10-08 11:40:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| f010ce48-e10b-3b4f-836d-f02d75f82949 | -14.90788 | -46.81792 | 2025-10-08 11:40:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 32139036-9375-3d77-828e-1c83a83ebb1b | -13.29426 | -47.16478 | 2025-10-08 11:40:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| cadfcec3-2c6c-3a02-8432-8a880c0e8fd9 | -14.87006 | -40.799 | 2025-10-08 11:40:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.9 |
| 5d7390d6-a92e-3c9f-85b0-415e3b1e860f | -14.02616 | -41.41645 | 2025-10-08 11:40:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 44.7 |
| dc952f15-371a-3179-ab0f-0d026db9fef0 | -14.52188 | -42.23541 | 2025-10-08 11:40:00 | TERRA_M-M | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 99d47a0b-967e-3f33-99f5-dc655988a793 | -14.71885 | -46.09359 | 2025-10-08 11:40:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 2b0fc2a6-86ab-3e69-86d3-b59b3a314eaa | -15.24326 | -46.35752 | 2025-10-08 11:40:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 27.5 |
| d1f04cee-fb77-3940-864d-60acc56e0c7d | -14.40171 | -46.03196 | 2025-10-08 11:40:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 38.9 |
| ccbddb42-ea9a-3964-8931-e8df70cfcace | -14.02103 | -41.41994 | 2025-10-08 11:40:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| c413ae63-2400-310b-af5b-b814076c04d7 | -14.87155 | -40.7892 | 2025-10-08 11:40:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 4dfb9a3d-55b5-3730-8798-9748c4cb77b1 | -15.53522 | -41.99598 | 2025-10-08 11:40:00 | TERRA_M-M | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 24ef61f5-b409-3a79-b24d-8bca6fff9385 | -14.72312 | -46.08755 | 2025-10-08 11:40:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 1d96d93f-f2d6-3676-86b8-26d06b8bad20 | -14.39234 | -46.00787 | 2025-10-08 11:40:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| fbf8590c-9d12-3a04-949e-3de88c0246e4 | -13.73765 | -45.68503 | 2025-10-08 11:40:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| bb11a141-a552-3576-a8c3-71380fcb8374 | -15.32578 | -46.17729 | 2025-10-08 11:40:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 4a3f25dd-0fec-3c14-8024-fc6d4297a33a | -13.27733 | -48.04259 | 2025-10-08 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| b4890b98-0a7d-38a6-aabe-4d6b5d2c4116 | -14.58575 | -42.73867 | 2025-10-08 11:40:00 | TERRA_M-M | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| d2500582-dc76-30cd-b6b0-2f21e42bc63b | -14.52009 | -42.24692 | 2025-10-08 11:40:00 | TERRA_M-M | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 05ed8789-055d-3b93-9387-649e30247fe2 | -12.57845 | -42.38736 | 2025-10-08 11:40:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 95b9f5b9-87f5-310f-96fb-44f838aec7e1 | -13.71727 | -42.65941 | 2025-10-08 11:40:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 38a5031e-f035-373c-a85f-d9a952958613 | -14.57364 | -40.86451 | 2025-10-08 11:40:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 1439166c-46cb-31a5-807c-0a2a5175f0e4 | -14.38842 | -46.03009 | 2025-10-08 11:40:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| c5be2c53-6037-3342-89ff-fb1d0065b52f | -13.76602 | -45.75522 | 2025-10-08 11:40:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| ed8f65aa-ce2b-35b3-8b62-78ec349b4317 | -14.80078 | -42.81201 | 2025-10-08 11:40:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 26.5 |
| b1cd21c1-a936-3b53-a2a7-6eb821e49b32 | -13.35632 | -47.59638 | 2025-10-08 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 60401356-458b-3a27-9541-f14d3c6d48d0 | -14.71937 | -46.10943 | 2025-10-08 11:40:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 50.7 |
| d7664dc2-a56b-306b-b086-6a5feb9fd851 | -15.23816 | -46.3636 | 2025-10-08 11:40:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 25.9 |
| fda8ae66-8c04-373b-a6c3-1cf0a5afb668 | -15.46097 | -41.53457 | 2025-10-08 11:40:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| e320d601-078e-3690-a94d-705fdc262378 | -18.15682 | -41.04339 | 2025-10-08 11:42:00 | TERRA_M-M | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 5788c581-fa47-3cc5-8245-62a7694b14e6 | -21.06033 | -45.8778 | 2025-10-08 11:42:00 | TERRA_M-M | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 9daad205-5224-3da7-a616-10cc9cc0473f | -21.09363 | -45.69395 | 2025-10-08 11:42:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 267fad1b-cf43-3250-aa62-d7b4d6edd6f1 | -18.02937 | -44.95996 | 2025-10-08 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 6ab2184b-4e41-3854-8d91-bcd246851b82 | -17.98072 | -44.97741 | 2025-10-08 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 3fa5f410-90ee-3fbe-b725-55f695deeabc | -20.31071 | -46.64694 | 2025-10-08 11:42:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 34163f3e-aeaa-3edf-8abc-ca12a812885c | -18.02079 | -44.9419 | 2025-10-08 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 39.6 |
| c2456ef6-6655-393f-8a5e-5ea4a13896b7 | -21.09475 | -45.68475 | 2025-10-08 11:42:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 45bdd1cd-6ed2-396f-ada7-79563a4bfdfd | -18.55571 | -41.57821 | 2025-10-08 11:42:00 | TERRA_M-M | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c7a3177d-71d9-3ef0-a091-a707fac816a6 | -18.24551 | -45.45704 | 2025-10-08 11:42:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8a07f94e-c7dd-39f8-bfa0-d22788bd12b9 | -18.41306 | -45.21171 | 2025-10-08 11:42:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 40.6 |
| eef2e44f-22a0-3951-93c5-8c9b670e4f42 | -18.08085 | -44.45535 | 2025-10-08 11:42:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e7cc2924-870d-3ce8-9c26-5508a9184972 | -20.09385 | -41.48034 | 2025-10-08 11:42:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| df45b21d-a5ab-3298-8cf1-0004e1ed27f0 | -19.79859 | -41.96461 | 2025-10-08 11:42:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 27786c20-b6f0-33bc-ae8c-2a324bb5121d | -18.0331 | -40.1963 | 2025-10-08 11:42:00 | TERRA_M-M | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 1bf44f7b-ecab-3a65-abf5-93384618e8d7 | -21.06052 | -45.88765 | 2025-10-08 11:42:00 | TERRA_M-M | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 250cdf9a-6542-303c-b102-42b18a189b42 | -20.09528 | -41.47081 | 2025-10-08 11:42:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| cdaa1d44-3905-3555-9167-6187cab460f6 | -19.81185 | -42.18563 | 2025-10-08 11:42:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| d6acb94c-4bfd-307e-979a-bdd5d8c6adc6 | -21.09192 | -45.70065 | 2025-10-08 11:42:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 045567bb-e04d-3da4-9cf3-7d0a53bd0967 | -18.61034 | -44.45248 | 2025-10-08 11:42:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5a51949f-2072-3ab1-a593-7284c0b382d0 | -19.54061 | -41.29296 | 2025-10-08 11:42:00 | TERRA_M-M | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| f340da98-b520-3a97-bc6f-51a279c60bbd | -17.98146 | -44.96708 | 2025-10-08 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ad358005-03d5-3f83-9d05-33be61373c28 | -20.1064 | -44.34527 | 2025-10-08 11:42:00 | TERRA_M-M | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| ed9cb473-e621-3b86-a414-0d9c60fe2184 | -18.60799 | -44.46671 | 2025-10-08 11:42:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5e10868f-5a6d-3275-8267-372764771b91 | -17.42115 | -44.87025 | 2025-10-08 11:42:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| ddaeb2ab-918e-3197-9b26-cc6c75bf59cb | -18.2523 | -45.46438 | 2025-10-08 11:42:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| a6a8c99c-1e60-3d12-86a7-9519b3ce8dfe | -17.94722 | -44.41697 | 2025-10-08 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 3f447577-bdf4-35bb-ae07-cbdeaf573621 | -18.41014 | -45.22844 | 2025-10-08 11:42:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 49.7 |
| b2e8ed2d-c684-320f-af53-e536eada98d8 | -19.81928 | -42.18299 | 2025-10-08 11:42:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| ad3a520d-c875-3b0e-9e3e-547f99aabe14 | -17.45588 | -44.10354 | 2025-10-08 11:42:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 334408ef-7247-3e42-9de1-a0829055d033 | -19.79708 | -41.97442 | 2025-10-08 11:42:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 0cdbcb8b-638a-3777-b702-27c839c2327e | -17.40973 | -44.86847 | 2025-10-08 11:42:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b9f7353f-8f01-3067-a2c4-0c2b2db400b1 | -13.8117 | -45.7826 | 2025-10-08 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 64873495-2a5a-371e-b7f2-6466f81ac20f | -14.7179 | -46.0867 | 2025-10-08 11:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 131.5 |
| a4e8a8bc-c17a-3158-8375-3a2743c57bae | -13.2662 | -48.0409 | 2025-10-08 11:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 919f3154-d6e7-3af8-9390-a25056211e9a | -14.3884 | -46.0294 | 2025-10-08 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 412fdbee-f0b4-36cf-adc4-18afcce180d7 | -11.1644 | -54.8804 | 2025-10-08 11:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 423096f2-42ca-348d-a663-71d71f123286 | -11.1833 | -54.8787 | 2025-10-08 11:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 6150701a-7859-370e-964a-ae1b1e85d8ac | -10.9296 | -47.1329 | 2025-10-08 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 373.0 |
| 764b877d-ed26-3c07-b64f-ad0ec7744cd4 | -10.9106 | -47.1353 | 2025-10-08 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 504.7 |
| bbf2619a-b54a-3986-ab70-d68414e2715a | -10.9109 | -47.1129 | 2025-10-08 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| bf5ac4c7-0fd6-386c-a3b1-9fe9e70c2ef5 | -11.1642 | -54.9007 | 2025-10-08 11:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| dac37144-cd48-3c08-85f1-06ec93f266e7 | -12.5107 | -54.7345 | 2025-10-08 11:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 57b7b3e3-7ea8-34e5-b4c3-b8d576373ae6 | -10.4245 | -45.3907 | 2025-10-08 11:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 34162c37-39cb-3a48-bd5f-fe7a4f8dc876 | -13.2855 | -48.0381 | 2025-10-08 11:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e7b37809-18b1-35a9-b0ae-534b60e84779 | -14.7184 | -46.0636 | 2025-10-08 11:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ae9e07f3-d659-33d9-b575-56c900a38a75 | -10.93 | -47.1106 | 2025-10-08 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 660ee0ab-9590-31c3-bee4-bd9c2428f4e1 | -13.8343 | -51.8529 | 2025-10-08 11:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 263.0 |
| 9109f89d-e293-33d1-99aa-31157c86e6fc | -13.3774 | -47.2411 | 2025-10-08 11:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| e39e744e-333c-3f4a-8f84-dd5b2eb864da | -13.0009 | -46.7795 | 2025-10-08 11:50:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 78e1d372-fedc-3c4c-a58d-6311e818cd3d | -13.834 | -51.8742 | 2025-10-08 11:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9be5ab4a-843a-3364-90bb-996599df9711 | -13.8536 | -51.8504 | 2025-10-08 11:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 85de0cac-633a-3db4-ad07-9309a6b957c2 | -13.0935 | -48.0215 | 2025-10-08 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 2af2fe2f-63af-3255-8ef0-2d970e35f326 | -11.183 | -54.8991 | 2025-10-08 11:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| d3cc6aac-e45a-337c-b5c3-c4ceadc7bc52 | -11.1833 | -54.8787 | 2025-10-08 12:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 0f0122b2-05aa-3cec-ab80-4ec5919f1b8e | -13.3774 | -47.2411 | 2025-10-08 12:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 100.5 |
| ec096104-edbc-3afa-bf75-8ac0a9ed3c81 | -13.8536 | -51.8504 | 2025-10-08 12:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 3745b1ce-543d-3636-8700-b8a6ec5a47f9 | -11.7085 | -50.9385 | 2025-10-08 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |


[Clique aqui para ver as próximas entradas](README100.md)
