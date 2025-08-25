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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cea7798b-c54d-3b95-8edd-bb87fe85cb69 | -15.14175 | -59.59548 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5ea48ed2-30b1-3b61-9bed-2f8671e06bb7 | -14.76247 | -55.93674 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67153f90-9c55-39b1-9223-2004f02edc92 | -20.34918 | -46.72518 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70c9672f-4b83-3c20-88f4-8c5ae3a7f98e | -21.63238 | -44.01768 | 2025-08-25 04:44:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 456d9250-9ead-3ab7-9c7a-f26cdbd33df5 | -19.93719 | -47.4896 | 2025-08-25 04:44:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a261a74-67c0-31d5-ab5f-17853ac979d9 | -20.71624 | -49.46627 | 2025-08-25 04:44:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4375fba9-8d78-3a10-8d4f-e1e00741e293 | -14.44053 | -56.47443 | 2025-08-25 04:44:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1864319-aafd-30f2-92da-d1c5f2b3351f | -12.59484 | -60.36118 | 2025-08-25 04:44:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93f2a401-f1ec-32b4-9362-67324767b611 | -19.94651 | -47.48021 | 2025-08-25 04:44:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3a264cd-6f0a-3d86-97bc-28371df9eb88 | -14.38886 | -51.95407 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f877100-c6af-3ada-8fd5-b4665a587ced | -20.54718 | -41.68738 | 2025-08-25 04:44:00 | NPP-375D | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d0e74206-c7ca-36a5-9368-29397526cf87 | -20.61712 | -45.02792 | 2025-08-25 04:44:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| ae57c476-f37a-360a-96a7-b951cc133b53 | -15.0659 | -48.66216 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb35dd27-9714-32dc-a609-7e00b8b21970 | -22.01468 | -44.28575 | 2025-08-25 04:44:00 | NPP-375D | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bfb7b300-bb47-376e-9dba-3ef07bb295ab | -21.12255 | -48.91855 | 2025-08-25 04:44:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d6eb8845-bfb2-3dc4-a262-e0effbd9f00d | -14.71586 | -55.93177 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a2942ce-f60d-3ba6-9253-7c7c3c70124c | -15.03867 | -48.50942 | 2025-08-25 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d239471-23b7-3703-ad77-4ff1b6a7d7ee | -20.90482 | -44.08245 | 2025-08-25 04:44:00 | NPP-375D | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d7379b3c-3f82-38ad-9d58-c74075bfdcec | -19.39133 | -43.74198 | 2025-08-25 04:44:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c1424c04-5f0b-34a6-9efb-168fae55dcf7 | -20.36338 | -46.71384 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fe6712a-dfe1-38fc-8841-b03dc6b63f7d | -20.391 | -46.73265 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 15e331de-4f0d-3399-b68b-3ab96929e52c | -19.73124 | -46.46669 | 2025-08-25 04:44:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2254c587-4cc4-31e8-8316-f4b8c792ef96 | -19.91289 | -44.63063 | 2025-08-25 04:44:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2910ab35-d94b-324e-9b84-d2a964367b89 | -14.67217 | -54.89227 | 2025-08-25 04:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3605a5b8-cc66-3274-a0fb-d19a7b8bcdfd | -20.37537 | -46.75548 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f57323cb-0789-3a8f-9acc-e7699f4cccfa | -21.48622 | -47.55178 | 2025-08-25 04:44:00 | NPP-375D | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b169d7d4-a236-37d7-8f5a-9c6902bab140 | -14.71194 | -55.93102 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac741f4d-33f5-3aaf-ba67-2f5c115737af | -20.36285 | -46.71813 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86f97e2a-9970-3168-afaf-61b92a3fb636 | -20.38057 | -46.74792 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76c0350d-ad0d-377d-8558-e565367f338c | -20.35757 | -46.72646 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f4f003b-8c62-35ec-97fc-4b41e1a494a0 | -20.29324 | -47.18169 | 2025-08-25 04:44:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db230df7-ac3e-39b5-ab73-70b531a133fc | -14.10349 | -53.99148 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ecd1dd2c-cc47-34f3-91a6-d8be01113275 | -14.10279 | -53.9956 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 187d118c-8c85-3210-be47-88ca80f88f7c | -17.59919 | -46.0977 | 2025-08-25 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49ad0815-a5b9-3716-bc75-3bbb06cc8b2f | -15.10408 | -48.6974 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c82bb78e-c823-3ea0-b80c-f7c6b0652b13 | -14.30467 | -60.37569 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c6810f3-156b-3b01-92b0-8110495d75b7 | -17.6034 | -46.09826 | 2025-08-25 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6eb31ff1-cfe8-393f-a853-8bee01de3251 | -20.38723 | -46.72855 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31a0a51d-1168-3c6d-9e83-e8a691380be9 | -19.91765 | -44.63151 | 2025-08-25 04:44:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 124ff104-13f3-3011-b0a5-484a9448ebd7 | -14.7604 | -55.92569 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8844bb24-69ec-38c7-90c7-1f4ecfe2eda3 | -22.17941 | -46.63116 | 2025-08-25 04:44:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99469f98-1e91-3525-ba55-5757f7cefc36 | -14.33972 | -51.96048 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c355965b-14f8-362c-b464-08c66a8e56f1 | -15.20336 | -48.27986 | 2025-08-25 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24afb036-0402-30d2-818f-a8e7db158366 | -14.27616 | -51.96137 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cad5c0c2-253b-3541-9ea3-b1c37acf0b8a | -20.73309 | -49.42624 | 2025-08-25 04:44:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e01a5839-2049-3321-87d0-b53c285acdb5 | -14.29606 | -60.37203 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf4d177a-ed0d-393e-95e6-3d798879a65d | -18.38504 | -46.83675 | 2025-08-25 04:44:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adf59ed1-fdbb-35ae-b32d-c3b4e12bff60 | -15.07346 | -48.70937 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b196853e-d7b6-3f3a-8d1d-ac4be07af65e | -14.91625 | -45.54656 | 2025-08-25 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d72951d-bac5-3bc3-8fd8-d4860c10cad1 | -15.64473 | -52.7247 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 405a6bcb-ba04-38b9-a870-c0d95b2f7285 | -20.37111 | -46.7554 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0307598e-477f-3d1f-80c4-2a8ec9028e51 | -15.06993 | -48.70885 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e73a336e-9866-3afd-af68-d0fc0a206f70 | -14.71544 | -55.92796 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f308fb3-c816-3104-87f7-4cc9791bede0 | -14.64169 | -56.58478 | 2025-08-25 04:44:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5354c6b-43e7-35e8-aa5d-08071aa1b868 | -15.13551 | -48.15348 | 2025-08-25 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 733ed441-5798-3140-81f9-576a2e0bc46a | -16.48426 | -46.75881 | 2025-08-25 04:44:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b2f2af8-6fd4-3088-8902-1cccaab454af | -21.41493 | -47.59487 | 2025-08-25 04:44:00 | NPP-375D | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f349e8fe-e896-36e9-8da3-6c2416956948 | -14.42564 | -56.4637 | 2025-08-25 04:44:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c246c25-9dd6-3362-8e08-1c011e829f1f | -18.38859 | -46.84122 | 2025-08-25 04:44:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14f16e89-7853-3939-b620-9d68391a0f2a | -14.71452 | -55.93303 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9d739a7-542a-3154-9ca5-4e21b8187b57 | -20.29685 | -47.18605 | 2025-08-25 04:44:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 768b6b47-8c87-3041-8375-983fcd03a3b4 | -14.26371 | -48.04258 | 2025-08-25 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fea3255d-7689-3129-907f-9dc62f253df1 | -14.73989 | -55.92713 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7d1ca1d-5650-3c22-919f-afc12c0b2da7 | -15.13974 | -48.14973 | 2025-08-25 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cabc26d3-2db9-3dc0-9f3b-cd618cae83ee | -15.63642 | -52.71194 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e10e337d-f1e5-3171-9bce-47cb8a6be41b | -14.43308 | -56.46905 | 2025-08-25 04:44:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33233598-68e3-3664-b3e6-cadd86c82ff0 | -20.382 | -46.73632 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 445be031-c95b-37c6-a32c-3129a3ecd8f5 | -15.03513 | -48.50877 | 2025-08-25 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2829685e-b30c-3b32-a4c4-bb68cc04aff0 | -20.27219 | -46.65316 | 2025-08-25 04:44:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21975f0c-ec9d-3803-b51c-1b348c39bd52 | -15.06344 | -48.47818 | 2025-08-25 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0baff868-20ff-33ca-b6b3-e84e79dd28b6 | -15.64136 | -52.72412 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43b19af9-7f60-379d-982f-75fa8977961e | -15.17632 | -48.20362 | 2025-08-25 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7745a6b-b563-33fb-b149-b65468832933 | -20.29278 | -47.18537 | 2025-08-25 04:44:00 | NPP-375D | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccd140d4-d356-3189-ae89-62bb3dd08dd1 | -14.64647 | -56.58174 | 2025-08-25 04:44:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39426cda-6eb4-32ce-a680-8d4a12a6f853 | -18.76877 | -48.02929 | 2025-08-25 04:44:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bfa678cd-1913-3fab-9109-85073b346e76 | -15.1375 | -48.63923 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c93550a-20e3-36c1-abe3-9de5c84e54c4 | -12.59414 | -60.36489 | 2025-08-25 04:44:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da13154a-7a76-3f3d-8d4a-0f83f216f940 | -14.22695 | -58.62589 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7381472-4fd1-34e1-9b2f-913b2a2f2cf9 | -18.76495 | -48.02882 | 2025-08-25 04:44:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3a0e0460-d8e0-3f03-833b-37a7c0895ef1 | -20.45344 | -47.41199 | 2025-08-25 04:44:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1652435-ba79-3fc1-9e4d-dd5131e48e08 | -21.2847 | -43.78653 | 2025-08-25 04:44:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f94a3c9b-0979-3326-a138-3fd4ef6d5708 | -12.59526 | -60.3621 | 2025-08-25 04:44:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc160b01-d29d-3663-a973-ea7ac5cd3ad7 | -20.37157 | -46.75165 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a2e5b32-9214-376e-95d8-50707b3839b0 | -18.23158 | -49.25995 | 2025-08-25 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1243b86f-912e-3049-95ac-7f3878018307 | -20.92833 | -46.84715 | 2025-08-25 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ab3d2ea-540f-3589-9633-ad98b87dd516 | -15.19317 | -48.22168 | 2025-08-25 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fca82d1-0e44-3d63-a41c-8b26d1aef1e4 | -14.38944 | -51.95046 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f16ed79-4e44-32ff-9de1-84df7cb6c8e2 | -20.37584 | -46.75166 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c8acef6-ead5-32d1-b87a-321c7d6b9d5b | -14.43714 | -56.46992 | 2025-08-25 04:44:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e669f771-cfd1-3ed9-a763-1a2303bff76b | -19.3694 | -44.21704 | 2025-08-25 04:44:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55f4a59d-b6ca-340a-8bf1-d5ecaa141e08 | -18.34145 | -46.01862 | 2025-08-25 04:44:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e954656-c9bf-35a3-b5de-7fa49625e858 | -20.39149 | -46.72872 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8da5478-a177-3f0d-b5d0-0d4235b184c9 | -15.07063 | -48.65449 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c5e03d5b-535c-31ec-963f-75e719b3ce6a | -15.08227 | -48.72306 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba0fafcf-335e-33f4-ae64-79890b57556a | -15.12597 | -48.64698 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33470b60-dd2a-3fed-ac6e-b4fc30ae45a1 | -14.72327 | -55.92944 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21342be6-06a0-3579-ab80-2b320d86a8b0 | -15.03687 | -48.52166 | 2025-08-25 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d70c5fc6-e9a5-352b-82a1-d0b68dba8304 | -16.4197 | -49.94055 | 2025-08-25 04:44:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 446d8cbc-5057-3989-a10d-b8727dbbe0bc | -14.92722 | -45.53014 | 2025-08-25 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 925c7b15-cf0b-3bb9-a95c-fc9a98b678b1 | -22.01401 | -44.2919 | 2025-08-25 04:44:00 | NPP-375D | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README56.md)
