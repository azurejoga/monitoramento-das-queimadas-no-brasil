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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d990fc1d-1d24-3a8c-9858-7a96b429808d | -2.41827 | -50.28278 | 2024-10-19 04:49:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e22f3151-b990-3ed2-baca-d83320fea6f0 | -2.41771 | -50.28635 | 2024-10-19 04:49:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4fbd4c1-1602-3887-a0d0-aa53d32266ca | -2.40935 | -50.40533 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ba61ca1-5f37-3e42-9a6e-db26641f4f74 | -3.46026 | -49.24871 | 2024-10-19 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27043d3b-5bb6-361c-bdb9-489ddb6b3b14 | -3.45674 | -49.24817 | 2024-10-19 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cee31e9-09b5-3f16-9d61-4a701369efc9 | -3.45489 | -50.17401 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc9fa4d0-115e-3f4a-a8a9-66c720849e59 | -3.45148 | -50.17348 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4751f8c4-8eba-33cb-b666-6edf207ae847 | -3.4441 | -50.1761 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8099f61-0bf3-3b06-90a7-48a0a8aed060 | -3.44126 | -50.17189 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f680f9fc-3d13-35d9-b69c-9fa67b4113a8 | -3.4407 | -50.17557 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1324d367-a24b-3bd3-a517-7d688db0f464 | -3.43848 | -50.21256 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2bdd7e13-2455-333b-b038-f5d77404d999 | -3.43564 | -50.20839 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92a50334-9609-3b6b-9078-d845f7356b08 | -3.43508 | -50.21204 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d4821d83-9e0e-3925-90a0-d1427a13ccee | -3.43451 | -50.21567 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4b47f250-fa0e-3edc-a5f7-129fcee9544e | -3.43396 | -50.2193 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 396af2b2-0f0f-33a3-aa17-621861abe8a6 | -3.43223 | -50.20788 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5362683-c3cc-3aa4-8632-9ee69fab0809 | -3.43167 | -50.21153 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 7e4da1ac-cdbf-3388-903c-a05634146868 | -3.43111 | -50.21516 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 53d66ac0-20df-37c4-9bdf-b86b18fcf1f3 | -3.43055 | -50.21877 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dabb99bd-da23-3bde-8974-a09571b1a518 | -3.42999 | -50.2224 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41710fa8-cc65-30fa-a087-46910ff047a1 | -3.42871 | -50.20789 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbd4df9a-2b3d-32d5-89bb-26115abd40cc | -3.42827 | -50.21101 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 6bde4526-8296-3037-b57c-7efb552cbeb0 | -3.42814 | -50.21152 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8938496d-4cb0-3151-adc6-91eef27e929c | -3.42771 | -50.21464 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| b9459534-398a-3677-90d0-9aa2b6b460c2 | -3.42757 | -50.21515 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 7952d610-b271-389c-9f4e-5532edb2a7d3 | -3.42715 | -50.21826 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6ed6e14-7b5c-39e4-b1dc-e07c5369e40e | -3.427 | -50.21877 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be20c2b4-705a-3817-8085-f1c7b053e450 | -3.42659 | -50.22189 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88005155-acda-30d7-9e30-3e194550ec74 | -3.42643 | -50.22239 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a49c67c9-91a8-3a75-a94e-2271cd97d96f | -3.42531 | -50.20735 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ed1be3a-1176-3c00-81c5-e640c9160b71 | -3.42474 | -50.21098 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8a186429-72f8-3833-bc6c-e561cebe949f | -3.42417 | -50.21461 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 875336db-50c9-3403-b953-658ad26382ef | -3.4236 | -50.21825 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53492add-065d-37a9-b6c0-9d18a4d40db2 | -3.42303 | -50.22188 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cab740ec-3139-3508-ab63-1bb7b08f74fc | -3.42077 | -50.21408 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89dd1d7c-19cd-3e75-8b3b-75f65565fdc2 | -3.4202 | -50.21772 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a62eb9e-35da-3da7-a05f-1f9cb3211129 | -3.34721 | -49.14302 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1f642b7-6d04-3cb8-9ade-61eb1efc712f | -3.34659 | -49.14704 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7c474c8-3fce-3e98-ac06-08912c28c1a3 | -3.27967 | -50.17777 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5da7b516-27e1-30cb-9d5d-53fb2f3bdab4 | -3.27627 | -50.17724 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15aea9bc-c59f-3303-8a1a-4cdd26f95da4 | -3.27286 | -50.13198 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d646f5b-24bb-38c4-83dd-a8668e1b830b | -3.26572 | -49.08702 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5d7da53a-7b0f-3677-b2e2-7de33c2e0fd6 | -3.10231 | -50.19527 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32b0ba0b-e3fe-3a7e-921c-3a96c2ccc77c | -3.09892 | -50.19474 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4edd6eff-7c79-3013-b75a-fab59984c0ef | -2.96772 | -49.28833 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e8b6b8b-2179-30c7-873f-f993ed359d00 | -2.90383 | -49.37366 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad457d17-d70b-39dd-8b6f-ed7d58eef6de | -2.87431 | -49.47076 | 2024-10-19 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b87eadf7-64b9-33ab-8183-6448dcf11a94 | -2.84628 | -49.53636 | 2024-10-19 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 943a8447-09e4-382d-ae33-5719485b0d1f | -2.84281 | -49.53584 | 2024-10-19 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3f59022-060d-325d-b6c9-1652fb614466 | -2.83931 | -49.86759 | 2024-10-19 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e9327cb-d394-3f34-b1b2-ed657d84ffc8 | -2.80488 | -49.41323 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70816d65-2f97-3119-82c5-819f7b06b8a4 | -2.7896 | -49.25045 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11d5ac00-10e9-34ba-bd24-29666cd0ba7e | -2.7844 | -49.23777 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fc8b35f-38ff-3f5b-8479-a505bf97c1e0 | -2.77754 | -49.32756 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df59c5c1-32eb-3b7e-b5bd-21d66a87eb47 | -2.76845 | -49.4085 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fe37924-0c07-345e-96ae-e3d75afb58e6 | -2.76458 | -49.36478 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e0d7c1d0-8ff1-37cc-888b-45ff4d97f949 | -2.7125 | -49.16813 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d1d7c4c-116b-382e-8206-17ffcfee881c | -2.7096 | -49.16368 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7cdae92-eae0-30f0-991f-6079cc245d23 | -2.6325 | -49.07983 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbaafc62-ee26-3273-bf1c-9c7c166c1d72 | -2.56764 | -48.93761 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 084ff858-a045-35d2-aca5-639f2b62ef7e | -2.5609 | -49.12181 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 931d561d-cab4-37c8-b60a-4f18574d2381 | -2.54517 | -49.85366 | 2024-10-19 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62836353-5859-36ca-a943-c3b41563c929 | -2.5309 | -49.76469 | 2024-10-19 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0fc83e0-0d4b-3978-8850-d55c3522b225 | -2.45068 | -49.62743 | 2024-10-19 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d5035a4-4ebc-3d70-86dd-3726ab6fb83e | -3.472 | -50.35495 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 515a73fb-125a-33de-8105-81af5b3df911 | -3.47144 | -50.35855 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4516fbc2-1323-3c6a-b6bc-35d27e87a86a | -3.46805 | -50.35803 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 128cc36d-0706-3cc6-8977-48e4f8ede3ac | -3.46651 | -50.61076 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c21af50-1491-33cd-aad8-b74f17495083 | -3.46314 | -50.61024 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53978b86-7731-3b28-a2f5-1a8f72ec590d | -3.46034 | -50.60616 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 960f01cc-ede6-3637-9ab0-fe55d236df9f | -3.45978 | -50.60973 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63cce6db-61cf-334a-946a-1bf802e1c5f1 | -3.45922 | -50.61329 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 563be088-fb2c-3d24-abce-db4761a0ede9 | -3.45641 | -50.60921 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a56f1db7-096d-3cfc-8e83-80187ae39005 | -3.45585 | -50.61277 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d18af2f3-d954-3c1e-b86c-621414eb8310 | -3.4556 | -50.32656 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a77aa1f7-b70f-3786-96f3-561c58f55e32 | -3.45504 | -50.33017 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 512e6b41-6b25-38e5-86ac-1e7e27796a9f | -3.45221 | -50.32603 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cb40c88-2c83-37d6-9466-a8404e459935 | -3.45165 | -50.32964 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 874b644c-9341-3604-82ca-4930f9a2413a | -3.4313 | -50.32648 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f568ed61-0f94-3ce0-8458-43c40d244a58 | -3.41898 | -50.38363 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e838f864-58b4-3656-9864-7697eb7befe3 | -3.41549 | -50.62837 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b4d1e6f-088f-36db-8a94-f5010a68aacf | -3.41493 | -50.63193 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03549188-04d8-3652-88da-1cde96cbc8d9 | -3.40652 | -50.32685 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6611e358-f4dc-3b01-bc22-233060b692b8 | -3.38957 | -50.34637 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8de69008-5604-3f3e-be69-c06161264a66 | -3.38675 | -50.34224 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50a84b83-77d3-3d26-be3c-eb7c11f6acd3 | -3.38618 | -50.34585 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8ec3c35-4e49-3c92-bca7-4dcb84614764 | -3.38562 | -50.34945 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7544bba8-848f-3f68-9522-55c3968751a9 | -3.38279 | -50.34532 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05dae03f-c98e-302e-8cbd-56fcebda5385 | -3.38223 | -50.34891 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2fc5d5da-0d57-3bca-9074-1987c882420d | -3.37941 | -50.34479 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3309ad4b-e8ec-38c7-88c2-e6e07076149e | -3.36527 | -50.30197 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f18b7937-b910-3077-9cf7-be7a6d0ad637 | -3.36244 | -50.29784 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30309a36-b601-3355-90f5-c67ae36bca6e | -3.36188 | -50.30145 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0597c840-9319-3e76-bcc0-03b8ea4baf20 | -3.35849 | -50.30091 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a25398fe-57aa-3752-a312-1109b982e37b | -3.35792 | -50.30452 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fc52607-1e9d-3981-864b-d22b69605c92 | -3.22892 | -50.36974 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f92d0b1-b5ae-3c3c-ad4c-d85d397eaaf4 | -3.22327 | -50.36152 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70485a49-9621-3fb5-826b-d9730d109ef8 | -3.22045 | -50.35741 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ec4f47e-990f-30e0-aca2-a7f265b8a036 | -3.19236 | -50.31236 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c286ac7-81c9-3c88-bd5d-b9eda1acd12d | -3.19179 | -50.31596 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README30.md)
