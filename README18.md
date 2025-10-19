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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b0caa54-9a6e-32b4-a1be-c6ff00f5643e | -7.1944 | -42.195 | 2025-10-19 03:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 1d26fb0f-5a79-3a3e-94f2-9fc77ffc49d6 | -7.1944 | -42.195 | 2025-10-19 04:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 783371ad-4417-37fb-b8ae-e2baba2143ec | -10.8891 | -46.0814 | 2025-10-19 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 438beaa6-1db3-3e2a-82b1-2f48d7e268c7 | -16.7435 | -42.7761 | 2025-10-19 04:00:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 7a6434dd-c31d-3333-8d50-e29fc37c432b | -16.7628 | -42.7961 | 2025-10-19 04:00:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 155.9 |
| af52a82b-af9e-3425-94f2-75c213598c67 | -8.6032 | -40.1834 | 2025-10-19 04:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 90.4 |
| a46c3c68-3699-385b-8ecc-d61d04f9e184 | -16.7834 | -42.7668 | 2025-10-19 04:00:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 133.7 |
| b8eb015a-669d-3808-8ee0-d7ccc6f3664c | -16.7635 | -42.7714 | 2025-10-19 04:00:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 361.2 |
| 23f70bc1-0e67-3250-bc2f-4f2869de8d17 | -10.8891 | -46.0814 | 2025-10-19 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 7dcf79cf-212f-3f87-a7cd-e7f6e3f49b69 | -16.7635 | -42.7714 | 2025-10-19 04:10:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 183.6 |
| de59e520-0d0b-3426-8858-b5e62905fd11 | -16.7435 | -42.7761 | 2025-10-19 04:10:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 248ab0fb-b637-3f7a-8e48-65ff151abc82 | -8.6032 | -40.1834 | 2025-10-19 04:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 0f98b971-775a-3be5-b856-34a7598df4e5 | -16.7628 | -42.7961 | 2025-10-19 04:10:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 558b2e02-7dfa-39b4-830e-70a1f76334dc | -5.71209 | -46.50826 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c87ae72c-d79d-3dd0-92d4-28cc1fbaab00 | -8.04587 | -41.10683 | 2025-10-19 04:10:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b9fa5482-e542-3d22-9fea-07b7a5629b98 | -3.51405 | -49.93908 | 2025-10-19 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01daf1fe-71d4-37ff-9b98-54ee8af9544b | -4.15213 | -47.67305 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b19996ba-e575-3ddc-8913-e3157345e5d5 | -2.24959 | -51.91932 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b1b661f-fe65-3dee-b1fc-432595121ac5 | -5.47929 | -43.12673 | 2025-10-19 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71978ea5-5bc7-37c4-82a6-a7465a5e11f0 | -6.34355 | -40.98817 | 2025-10-19 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2dc9c4a2-1e40-3b60-a53f-bd3a872186dd | -5.75953 | -44.00496 | 2025-10-19 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 403c5902-d180-3b16-a31d-0b3a283f73dd | -6.74164 | -44.29003 | 2025-10-19 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1401f5f2-4b98-3258-b6e3-95c783e3a2b2 | -2.44461 | -49.37221 | 2025-10-19 04:10:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ab0b1d1-2e37-30ce-a48d-dee26d14b700 | -7.19213 | -42.21668 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 42903c63-1c30-32e1-92ab-64a139c746a9 | -5.99225 | -44.15071 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e707862-f9f5-39ed-a752-72fbb327cdeb | -4.24651 | -44.67491 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0478eb72-3aff-3b6d-9f37-02f8921e3360 | -5.21612 | -43.37258 | 2025-10-19 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 375eb4e4-5831-3aed-bef4-f06d40ab63a5 | -6.09962 | -44.02057 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 620f3468-ffd2-34a6-a133-80a6ffecccc9 | -5.76017 | -44.00101 | 2025-10-19 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e30c299-275c-3f75-b60d-7c80832a41b3 | -5.99701 | -44.05391 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b71065e1-8313-3574-b018-6d78a56ff0fb | -6.02358 | -41.92391 | 2025-10-19 04:10:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9cdf8101-0e48-3130-90a0-53cc68b045a3 | -2.7018 | -49.86985 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f34e6ce0-39e0-354e-b025-4af80442344b | -7.19979 | -42.2039 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bae80e6c-224f-3ab6-9267-fb6e0aee4524 | -5.5421 | -41.31106 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6bc0b66c-f770-3b46-a562-ad45f89d252e | -4.7423 | -48.63754 | 2025-10-19 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56dcaab9-bf28-3963-b3e4-1cc5b8546964 | -6.96022 | -39.6396 | 2025-10-19 04:10:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e125fb3-0d69-3198-8b21-05b881b7b535 | -4.12013 | -42.19114 | 2025-10-19 04:10:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 80e9971f-7cc3-359e-9685-d70145a91d96 | -3.0416 | -40.11167 | 2025-10-19 04:10:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8702f5a9-f3cd-39f2-874d-b47bfd1f0bc3 | -6.01196 | -43.98378 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 781cffaa-c014-31fb-87ca-754517bf8970 | -5.6723 | -47.99426 | 2025-10-19 04:10:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2157a9f1-c9fc-3aa2-88a9-5db1bbb2c68b | -5.89822 | -47.23691 | 2025-10-19 04:10:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 465c04fb-5f8e-33a4-97bc-ffe1c1a18b2e | -5.08674 | -47.9416 | 2025-10-19 04:10:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be5b632c-b4e5-3552-bab8-bdf4d1a6c24a | -5.43925 | -45.36749 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f7fecfe-cfa5-3f82-9b82-95b58c1b8af9 | -5.64317 | -44.80832 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3936243f-6a36-362d-aa98-653dcbdb540a | -7.84214 | -40.25878 | 2025-10-19 04:10:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 587162c0-9e9a-3b09-8164-dfa25a891edf | -7.19656 | -42.18876 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| c709313b-fe72-3b2c-aee6-673fa1a7c4a9 | -6.74227 | -44.28613 | 2025-10-19 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e76bce3-8c28-3eaa-a8e5-1050103bd75e | -5.99641 | -42.79796 | 2025-10-19 04:10:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 16e2e332-301e-3bec-9494-b6d0d91ce60b | -4.99855 | -44.46005 | 2025-10-19 04:10:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ece648d-542f-3cc0-a85e-aa3fe2d64f68 | -3.51935 | -49.94007 | 2025-10-19 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d94d3a86-b55b-3be3-b8d6-574ebab16951 | -5.21341 | -43.74537 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 144c8c28-4f4f-3a18-9ff9-45bbdd5dbad4 | -6.72791 | -46.0299 | 2025-10-19 04:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0046a2c8-8b08-3076-9017-28edc8ad36bb | -2.25113 | -51.90986 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f5be23d-decb-3970-a994-3f5aa2581d25 | -2.68335 | -49.55093 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42448ed3-4457-397c-b41e-88ea2f2bf30b | -5.22061 | -43.74548 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 429a4adb-cfac-32dc-8c22-6ee7cf0b2fb2 | -4.26938 | -44.46505 | 2025-10-19 04:10:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 32700fa0-285c-336d-ac99-ebbe6fb6aced | -5.36199 | -47.21552 | 2025-10-19 04:10:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e1450c72-6e2c-3fbf-b137-8a80aa589997 | -5.5949 | -42.70882 | 2025-10-19 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 27b35f7a-33ca-3a02-85e0-22d151f637ab | -4.97325 | -44.61289 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e849c859-1801-31f7-a3ca-222f85c68fca | -3.12113 | -49.10504 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a37eba09-aabe-3cc4-bf13-fd54f6ec4106 | -3.12151 | -49.21646 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ecf8b1e-1364-37df-9b5a-be77e08a08d4 | -4.74264 | -48.63521 | 2025-10-19 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ff894b3-56bd-31d7-bbd8-5411f807a45a | -6.70619 | -46.62937 | 2025-10-19 04:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67a513c9-4f19-3173-8e2a-eb6f3cf344e6 | -5.63582 | -44.80717 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ada668c-c182-3670-9a49-a66294dab48c | -5.58089 | -41.32426 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 14361f8a-9248-3f69-8413-02f068788506 | -4.13012 | -46.22587 | 2025-10-19 04:10:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0b3f24e-f5b8-3b8d-9595-c31e9e0f6f8a | -5.64177 | -44.81691 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccdff533-58e6-3adf-9857-b6f6b9e6c175 | -7.48817 | -45.09498 | 2025-10-19 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1da70cec-b795-30fc-89c3-84bbe9e4ad2a | -7.19423 | -42.21732 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 50f454f7-c47a-31e4-aff7-fd545be3c451 | -6.41607 | -43.91814 | 2025-10-19 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f48c79dd-4966-33d3-9f6e-60aa9b7daf64 | -2.45133 | -49.3637 | 2025-10-19 04:10:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b73ebf8c-f13e-3599-babc-9165b9cc0005 | -5.30886 | -44.84338 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f1b23fe-d001-312e-992e-67da05bc2751 | -5.77789 | -42.72329 | 2025-10-19 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a8e77044-be33-3c81-822c-364c89ffa763 | -5.98744 | -42.78904 | 2025-10-19 04:10:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a5a0c047-16b6-3974-be5d-86857d6b6d9c | -4.14536 | -47.6584 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e7c6f52-5263-3d1b-b95d-0baf86f94648 | -7.05006 | -41.82646 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e88e2344-5204-3e4a-9997-a8bed9a4606d | -3.08599 | -49.22342 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 92f576b5-41cf-3172-8006-ac9c3e9ea558 | -5.40374 | -44.05991 | 2025-10-19 04:10:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e5039f2-bf75-36b6-8020-a90b07556eb7 | -7.2838 | -45.40619 | 2025-10-19 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ba62592-3b71-3ff9-9917-bde8146c8762 | -7.36823 | -41.95578 | 2025-10-19 04:10:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8c05f71c-a364-3bf8-addb-4961ff201664 | -4.28658 | -45.48417 | 2025-10-19 04:10:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a26a037f-2a08-39f0-a778-cfc9336808fe | -4.97303 | -44.84404 | 2025-10-19 04:10:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f6d48d2-f9e6-30e9-974b-c709d8138abb | -6.00193 | -44.18093 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be4fbfab-b6a4-3a24-97f6-b202b8c447d3 | -5.48379 | -48.65008 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcc08fb1-898a-34eb-a83a-a9227ef3419d | -4.15917 | -51.09541 | 2025-10-19 04:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17a7e721-8dcb-3e1e-a771-64ce32ae5f1a | -6.59287 | -45.88094 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 893008bd-4c0d-3eb3-a66a-cbd032743e48 | -3.85023 | -41.78011 | 2025-10-19 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a58e2e86-bfcf-3c79-a458-b0ffccfe6553 | -5.64071 | -46.58472 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2bd0082-8515-37f2-bf89-d243789859ea | -7.18224 | -39.67031 | 2025-10-19 04:10:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 988958ab-27bd-37a7-8852-a1e1d9e1e055 | -4.58615 | -46.30402 | 2025-10-19 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7cd98511-05e4-3a6a-a94c-b7cfed22c104 | -5.94749 | -42.23045 | 2025-10-19 04:10:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 31f018a7-7a6b-3458-a6af-9ba17cac9329 | -5.72213 | -49.09448 | 2025-10-19 04:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6143abf3-4cac-32e8-8cca-cb82bbe77211 | -2.25646 | -51.91028 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 85c13017-be98-360d-b667-939bba35a9fe | -6.14095 | -41.80328 | 2025-10-19 04:10:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b77b94c1-0d4e-3875-874f-c91ae25f8b10 | -2.59485 | -49.50151 | 2025-10-19 04:10:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17bc2ce8-00e1-3e4d-b9b9-7e0e8d89eb4c | -4.52198 | -48.84031 | 2025-10-19 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8777dbea-f914-356a-8552-ea560eb58c0e | -3.12998 | -50.2164 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1aba6ca6-41fb-3e72-89ed-c569203c7dac | -4.23694 | -44.68687 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5ca38af-e65f-3fde-9337-79a4d12936b6 | -5.30464 | -45.00962 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d5f43bb-a8d7-3799-bf08-2a82f52feacc | -4.29102 | -45.48269 | 2025-10-19 04:10:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README19.md)
