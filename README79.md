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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc59b26b-ba04-34c4-b2c3-74eb84aad388 | -10.76666 | -60.78926 | 2025-08-27 05:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88444dbd-878f-33f0-a474-47227fe3ece2 | -9.06833 | -66.06107 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2cb49c18-6ee7-36ba-8246-53737d9c0d9d | -10.2911 | -64.50503 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49ec3c26-010e-3960-b12c-5a28b89803bd | -11.69933 | -60.1701 | 2025-08-27 05:46:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd899931-1019-3f5b-9411-d3be86e468dc | -14.30057 | -60.35851 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8644b9da-b5de-30b9-ba75-f834fe697a4c | -8.94696 | -65.94858 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5eecb12-4d3e-3f63-a7e5-a2b42321c96b | -10.94139 | -63.63467 | 2025-08-27 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7152e676-207e-3774-9932-8a2ad43f1bbf | -10.93787 | -63.63407 | 2025-08-27 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 172b671b-793c-3fe5-8ee3-b453d85b33b1 | -15.61806 | -52.72512 | 2025-08-27 05:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3f61462-28f1-331c-beb8-28d84cde9d0f | -10.10125 | -62.89774 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08148c9c-ebc8-38de-81fc-855ced087dab | -9.28711 | -63.72316 | 2025-08-27 05:46:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68efb9fe-7ab7-3dd3-ba2e-4cfa8b435018 | -10.27862 | -64.49555 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5e7e93c-eb97-38f4-9740-a5ada92395ee | -8.95028 | -65.94911 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c86daa9f-6f82-36bf-b9d3-0387332de070 | -10.09216 | -62.90919 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3ad109ef-91ae-3378-ae27-579a7e720101 | -8.9331 | -65.94994 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a973ae6d-e1ef-3526-b9b7-a3020aac3fc4 | -8.98455 | -65.43559 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdea8adf-1706-3483-8dc7-a8eb05fe13cc | -9.32921 | -63.20424 | 2025-08-27 05:46:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35aeae62-3848-3e85-a204-ea66128b4c53 | -9.01383 | -65.69792 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87adbbe1-6902-3ac7-8446-eedf810b7f80 | -10.2741 | -64.50237 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c66f9497-b4b6-3a78-b9aa-5cf5c577358f | -9.64461 | -64.99371 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9558a1a-d26b-3d0a-b6e7-49e347f55d6f | -8.96247 | -65.95823 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85777b53-74c5-3a82-96ed-902df9c56977 | -10.27013 | -64.50551 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77fddf17-faf6-3380-adf1-25e64608bf02 | -8.95693 | -65.95017 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d6ebcae4-01cd-3bea-8289-c0bccc1df2ff | -9.08533 | -65.71641 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d419ed3-bda7-3834-b2e0-f56748fccb0f | -8.95693 | -65.97167 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| cea42558-3171-3f5f-a15c-675700d321db | -9.00171 | -65.41322 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c877f1ff-1fdd-352b-afb6-6c5454101db2 | -8.94973 | -65.95261 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0bf51588-f77d-3f1c-a351-91ad6dff8d2e | -10.77079 | -60.78989 | 2025-08-27 05:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 124eede7-1133-37b0-ac96-0613576e2db8 | -8.92299 | -65.9342 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06e59c92-c6e7-3f84-9fce-19044df18f17 | -10.10363 | -62.90664 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc9b3b29-307a-327a-a6cd-7e6c72ce5606 | -9.02103 | -65.69549 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b36ded22-0b4a-3835-a2dc-de0cd0a4d079 | -8.91467 | -65.92213 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91d550e1-168e-3dce-979c-c11dc58eea66 | -8.96414 | -65.96924 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56d17b5d-deb1-364d-97f9-d0223ebedc30 | -8.91744 | -65.92616 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbac9b04-21a2-307d-a1d2-1e18f7fd076b | -9.80115 | -64.26857 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02dd466e-a2c1-3350-ac2e-dde16fcc34b0 | -10.40818 | -64.40176 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ae50acd-c6ec-3624-bd4d-0f6129e8213d | -9.01002 | -65.40376 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00288beb-d7ed-3d59-aa45-a242dda8ce20 | -11.34444 | -63.26924 | 2025-08-27 05:46:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15fc9a96-0c14-30da-9f15-89dba80bf435 | -8.99616 | -65.40515 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41acd6c3-59bb-3c22-a432-f0646e2fe0ae | -9.02048 | -65.69899 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5697cf7-02cc-3bfa-a4b4-61718d485a18 | -8.92021 | -65.93018 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b8cadc0-926b-356c-8f39-7d32baca05c4 | -10.51945 | -57.98214 | 2025-08-27 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e1c5fb0-15b3-38a3-baf7-5b9aa11cbf71 | -10.04028 | -67.53319 | 2025-08-27 05:46:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d733941c-7f43-3d48-b10e-93f235f371cd | -9.08146 | -65.71936 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fb439e3-6da8-3257-9bc4-58b0eb60b882 | -10.09276 | -62.90509 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8237c2c7-df92-36cb-876e-59a75ae6d0a2 | -9.07442 | -66.06564 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb4bd36d-96e6-3339-93bb-2260f1568388 | -11.31869 | -55.21799 | 2025-08-27 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 822628c1-bf00-3caa-9090-92027db63575 | -8.99781 | -65.39465 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7afe358-8f2c-3686-8adb-c92c9b2a893e | -9.80456 | -64.24635 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58614cfd-276f-3e5a-bb63-73977e3d8d35 | -8.93185 | -65.9213 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91e090cf-3f4d-3690-9a99-d0041be97e76 | -9.84566 | -65.00298 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b57591cf-2d5c-36e6-8b4c-fa161c7b1165 | -9.03989 | -65.72715 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8716fc40-b2bf-337d-b4f3-1308d347670d | -9.80229 | -64.26116 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2bd2bef-e199-3327-9ce6-2e15d3a40a7c | -8.95361 | -65.97114 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4333ff21-1c1c-338c-9590-0f443fddd813 | -9.67093 | -67.50768 | 2025-08-27 05:46:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0d80b88-4649-3c90-94b9-7e486471ec2d | -8.96137 | -65.96522 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 764dac44-71ae-332a-ab61-a6d8b524e194 | -9.28629 | -64.55656 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4475a54d-1036-3602-8143-d2221277c9ea | -8.93199 | -65.93543 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0905b28d-d9c6-3719-89ff-e0ff95f7a740 | -14.30878 | -60.36562 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 471563a7-7ecd-34f6-81d3-bbed3ddcf548 | -8.94141 | -65.94052 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e12ebbf-6013-3314-9283-0be5223f7081 | -10.29279 | -64.49396 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02744ebb-542f-31f8-be8a-a6ddf180eec1 | -8.51395 | -69.79392 | 2025-08-27 05:46:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fb6d4ff-40fb-30ba-ae67-d2a3dca6d6ce | -10.2809 | -64.50344 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a19ce2be-6a6d-304b-a899-25c2633ab335 | -8.99671 | -65.40165 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4ff7826-be9c-3b72-9684-4e772b4c4933 | -8.95471 | -65.94266 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f85a768-fb79-3a48-bbca-b45d854e9f66 | -8.96136 | -65.94372 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 51051276-c419-399a-bf93-20dec3366bb6 | -8.94418 | -65.94456 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c782add-47ed-3ddd-afad-256d45f08b2f | -9.80854 | -64.24317 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0353314f-d9f2-38d8-90e5-43e779d68ae7 | -8.96358 | -65.97273 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8dda5b6-6dff-3fa8-918d-675e3ab334a9 | -8.9597 | -65.97569 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ff1f149-0255-3457-86ac-9eb25cf47596 | -8.95083 | -65.94562 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49848daa-c83a-3fff-b794-514fdf3c2821 | -8.93088 | -65.94242 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| af66faef-991d-32e6-853e-c9458562516e | -9.79375 | -64.24846 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a0f0c01-1ab2-3be5-b255-058ea8874c22 | -9.04654 | -65.72821 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2aae6d9-b33a-3606-bd10-b168148f9cf8 | -8.93698 | -65.94698 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2a028f7d-6a2c-3b64-a525-edd29c0c44a2 | -8.94363 | -65.94804 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24fb78f7-db46-3fcf-beb7-d49799258893 | -11.31319 | -55.21248 | 2025-08-27 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3b2f964-8fbb-38d9-8383-8aafaf2dcbea | -14.77277 | -59.72587 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f7d6490-707f-3e00-9e3a-c611b3482dff | -8.92464 | -65.92372 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0aba681f-ee98-3a53-90ea-5d21a83bb12a | -10.03292 | -59.35676 | 2025-08-27 05:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f441d349-f9aa-3b98-893b-9f54cd29464a | -14.76955 | -59.72187 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71100c1e-df65-31f9-9002-ec8fbbe770b5 | -9.79773 | -64.24529 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ccde912-b4d6-3bc9-b833-9d22e8536c08 | -8.95139 | -65.94212 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3d2944c-e3d0-3b5b-a9f3-489ad41b65ec | -9.27953 | -64.55552 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c95b96d-d6cf-3c70-964a-b40ca960cca6 | -10.09762 | -62.89729 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7894e701-1461-3dcb-80b6-e2a5e22ef2fe | -10.27522 | -64.49501 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 27e308f2-38ac-3a44-8b24-39c76e217dd8 | -8.93975 | -65.95101 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc9ac373-d151-30de-8ffd-ea0ceb60f50b | -11.1935 | -62.64648 | 2025-08-27 05:46:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 235daed5-7262-3b81-a08a-369ecc2ef95c | -9.8114 | -64.29287 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd70484e-0ec2-3612-9f18-cd7524794137 | -8.93365 | -65.94645 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| f3086fd2-5735-39fd-a1fc-45894411bb28 | -8.99839 | -65.41268 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6041453-4e8a-3ad1-9cba-d0721a20209c | -10.41379 | -57.70808 | 2025-08-27 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db9a0462-bb2b-342d-8b42-b89978c85f21 | -10.27466 | -64.4987 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7c9ba7d5-f349-36a5-af03-20aaa828784e | -9.79716 | -64.24899 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0edac376-c631-3345-a2c2-6605301b1f63 | -9.79146 | -64.24052 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 407c9587-5dac-3308-8f0d-5364f39adcd2 | -9.7909 | -64.24423 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ce303c9-2111-3ac0-8b2b-c3baab86baa2 | -9.11747 | -67.70764 | 2025-08-27 05:46:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d6815a9-8df8-3a09-b53e-0ebce7341ac5 | -10.04088 | -67.52953 | 2025-08-27 05:46:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d02996fa-154c-3434-9982-d225a3d712da | -9.29582 | -64.53956 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34f2ac11-3708-3600-8893-121c64330470 | -9.02605 | -65.72852 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README80.md)
