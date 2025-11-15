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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74951974-cbf2-39a1-9e4e-9e9ecd5d4db2 | -5.42602 | -42.58468 | 2025-11-15 04:25:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 03a4baef-214c-3830-9cfa-9bf5358f0e0e | -7.87504 | -48.41363 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b40ef672-3ba6-3e0f-95f1-65194faa33a2 | -7.87965 | -48.40683 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 698f153c-858c-38c7-99fa-993b744708f5 | -6.24216 | -46.39322 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 480ccc84-b997-3595-966c-fb7c4ee6442b | -5.52063 | -41.77569 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 811561b8-e735-332a-b3f2-6dccac295172 | -4.6852 | -45.85746 | 2025-11-15 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 639795ce-0592-3dfd-a689-3fe5ed0e9109 | -9.8507 | -44.16444 | 2025-11-15 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b1adab0-21ca-3cc1-a421-6a59aa6d3ae3 | -5.63039 | -43.92485 | 2025-11-15 04:25:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3daae32d-b0d8-3934-b1e1-917a1d5b74c4 | -7.46643 | -45.93076 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8355d1c2-8bed-3cc5-a5c1-1d9de9eb255c | -3.58588 | -53.48931 | 2025-11-15 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f37ccbd6-f032-3d5f-820f-3f426ccee3de | -3.90994 | -50.03787 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e03e2cc-d6d8-3fdc-9f38-1b22c50c582d | -2.36684 | -49.09599 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00af79cc-ed00-3254-b78e-be4aab352ce0 | -9.93988 | -44.92966 | 2025-11-15 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df0d1d7e-baaa-3668-b36d-c6902af3c93d | -6.2962 | -41.82526 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 77c1406c-dc37-3483-936a-c0d12511d3a7 | -3.5999 | -54.68015 | 2025-11-15 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bf759ab-6626-3762-be51-2d2d5dad5627 | -7.52757 | -47.19934 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d8ad91d-676c-35f1-9654-9638518342a2 | -5.72797 | -46.54847 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8fb5b95-00d2-3c92-99a6-e270ff529abf | -8.86038 | -40.38655 | 2025-11-15 04:25:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bad6c8f5-c1e9-3df3-b506-426028733a6e | -4.15118 | -42.77652 | 2025-11-15 04:25:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3b6db59-3557-3a3a-ae20-ac96a9102348 | -7.53032 | -47.20336 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3b17f4a-32c0-30f8-9138-bdf1b126adce | -7.06187 | -43.58187 | 2025-11-15 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fec8b436-ad04-3247-8c88-170a2fb00f8b | -6.10665 | -44.21816 | 2025-11-15 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 020f2110-1f6c-3a30-877f-ad10d4f763fe | -5.16818 | -49.88044 | 2025-11-15 04:25:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88da04d9-419d-3cf5-8898-6064973076ae | -5.37237 | -46.77672 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a42b4d7-6923-3848-a1e6-2870edb71e99 | -2.73797 | -45.30037 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d1e2a93-1484-3970-8d0e-0140260420cf | -2.7882 | -52.974 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05d188c2-eddf-3563-9a94-4e8b78114e5d | -3.17246 | -48.6102 | 2025-11-15 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c644ffb4-d4bf-3ce0-97a1-f7dbb17f88bc | -2.74235 | -45.29402 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aa725e1-fa2f-3374-bceb-8783c2685b82 | -4.07649 | -47.95064 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4193d02b-b89f-3a78-890e-e75a6f6845b2 | -7.26251 | -48.03043 | 2025-11-15 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| abd6b713-f51f-3026-9b98-308eba9a106e | -7.72582 | -45.81443 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46febeec-1d7f-36e7-a928-ad8c9ee138c8 | -6.00104 | -45.39774 | 2025-11-15 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04443f0d-09a7-30c6-b227-a831faf5344a | -9.94011 | -45.09229 | 2025-11-15 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe81a58a-2d1a-3b6b-a18c-86be94a04ed8 | -8.99599 | -44.17968 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f42a7624-7ea7-355b-9abc-0c4bf6f07cb4 | -4.65491 | -46.8418 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dcf3598-93da-3bee-b6c1-2ff2a0495063 | -8.32574 | -45.40721 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50d24891-d870-336a-b30c-663465bd72c9 | -4.70294 | -40.12532 | 2025-11-15 04:25:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6836d433-c3b3-34b2-80ba-50f54d411b5a | -6.58059 | -47.53483 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 617e59dd-02dc-3edf-9d5b-dcfad9ef1724 | -2.5106 | -47.81276 | 2025-11-15 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9f7a1bc-201e-3f4f-b0ab-bce989767c7f | -4.94359 | -44.75447 | 2025-11-15 04:25:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b87448cc-b216-3523-985c-90e74d7ce0f7 | -4.61909 | -42.80822 | 2025-11-15 04:25:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32e010fd-aa4b-3d59-a78b-ffeb2f061a5e | -4.77503 | -46.45058 | 2025-11-15 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e7b7356-6c81-3737-90ff-79dc1b810162 | -4.27047 | -46.84595 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66225fe1-7615-390c-9983-f43e8f2c0a2f | -6.29936 | -41.83072 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3d6d2102-ec3b-30ff-b064-2e3f542f26ad | -8.00833 | -41.18438 | 2025-11-15 04:25:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9684624e-d2aa-3f1b-b470-05904085d827 | -2.95436 | -41.97537 | 2025-11-15 04:25:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 714d7f0b-0149-305e-a88c-fa14bf4847b8 | -6.66499 | -43.76838 | 2025-11-15 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 517261cd-659c-36bf-95ce-8329948dab87 | -6.14784 | -48.04837 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5795cdb9-2031-3702-afd2-73baf16236b4 | -4.10888 | -48.01395 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e8a30d9-cac4-39b6-a333-3ca0d3180835 | -6.88201 | -41.59658 | 2025-11-15 04:25:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 46c7e8c2-bf53-32b5-9195-3383a97aaeb2 | -8.75773 | -45.66045 | 2025-11-15 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37a9f846-50de-34ce-980c-7293596091f6 | -9.10498 | -46.55054 | 2025-11-15 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8995d4e7-7ea4-37eb-9df1-f7e24ab36ac5 | -6.30324 | -41.83128 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4d794569-1a9d-36a3-8460-adf8565faae3 | -5.70538 | -42.86639 | 2025-11-15 04:25:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8b4fefcd-468a-379c-87df-11f7e746dbb8 | -1.62236 | -54.71355 | 2025-11-15 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90bb9d40-669b-365a-bf9b-711aa1eb4b98 | -3.22935 | -51.52449 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6594857f-e314-36ec-b9f2-5d9b7e4cc152 | -9.85602 | -44.17776 | 2025-11-15 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f821b0df-51e8-338c-82be-5884746ab515 | -7.3607 | -47.28709 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87614275-87aa-33df-a632-1ff51ceb357c | -6.56651 | -47.10963 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb9ee94a-31c7-3331-bcab-fa3217d1aad3 | -5.31469 | -47.29006 | 2025-11-15 04:25:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41cfb5b8-720d-3524-a5b0-7aef2164f463 | -7.52481 | -47.19532 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f5bca88-079d-32b8-b688-749589d6c1dc | -7.71106 | -49.38485 | 2025-11-15 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1bb8d43-8abb-3803-81d4-bbb162b04b6a | -3.31589 | -45.68696 | 2025-11-15 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dadaf25e-a035-3491-b12a-6061b77df2ae | -2.98056 | -49.11996 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b0201e7-7ca5-3533-83ad-452682cb4fb1 | -9.85306 | -44.17315 | 2025-11-15 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85f4dcbb-ee98-3e8b-841f-55b82053e329 | -5.67252 | -42.75938 | 2025-11-15 04:25:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef449c49-a0b4-3466-b4aa-653b31ad49d7 | -3.39772 | -52.45013 | 2025-11-15 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 555e41da-a9e0-3228-a145-d9e046986757 | -6.65234 | -44.26916 | 2025-11-15 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71ee2e02-0566-31c4-84c6-f5f66d64334d | -4.86814 | -40.97738 | 2025-11-15 04:25:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 193e77fc-093d-3b9c-987c-1479b14373f3 | -7.69568 | -47.19021 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 051a3a8b-6d21-3d13-815f-c8ffc87ad115 | -7.14489 | -41.24379 | 2025-11-15 04:25:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8fda482c-8715-3702-b003-5b2c4ee24954 | -2.69031 | -49.85558 | 2025-11-15 04:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c67d09d8-214a-327d-be01-765b00884ad8 | -6.65856 | -44.29708 | 2025-11-15 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09eb9302-84f5-3ad6-a450-62204ff33a29 | -7.45579 | -46.88087 | 2025-11-15 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74faa117-b2cc-364f-b4a2-f802699b14cb | -4.983 | -47.23754 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b4dbb44-12c3-3b94-9aa4-75cccc160802 | -6.16265 | -48.04315 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 13c0a537-6ca0-3822-be96-b361fa6cb4ca | -9.11956 | -43.95424 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d77461f7-340d-3f86-af51-e4cafd1b883f | -7.26309 | -48.02681 | 2025-11-15 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fe53def-bdb3-3423-ab2e-b59a46e835e0 | -5.74507 | -42.72569 | 2025-11-15 04:25:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e83226c0-b602-3ea0-8f9c-b180824348d1 | -9.2629 | -45.19629 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9789173c-16df-3ba6-94fc-a7fd2bc1f059 | -6.15924 | -48.0426 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4ff467a5-4bb6-340f-a037-a4d93a428c8c | -5.48092 | -40.97136 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 247ac276-4d64-3fa3-a290-c0eb704f34f6 | -7.42946 | -45.2282 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a16dcd22-0445-34c9-bea9-998f1fea86e7 | -5.16977 | -44.85127 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb403a59-9774-3a3e-908c-53da393dc6c3 | -4.42408 | -47.60011 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63f42330-8b5c-361d-b8e1-b4461999f0c5 | -4.8654 | -47.38048 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 855ecff1-0c84-337a-95d4-073e28384e64 | -4.27437 | -46.84297 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 684f9ed8-e821-31b2-83b0-12360efc5fc6 | -3.71142 | -52.09487 | 2025-11-15 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dc381c4-bb08-3127-a36a-34abaeb9d44d | -9.09516 | -47.79035 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fda43041-a4df-3ce9-994b-bb535376f7fe | -4.10768 | -50.05955 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7c1c499f-5b6d-312b-9860-020f8c12c711 | -4.32712 | -47.57066 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4b17cf7-ebf5-3a46-be7d-d18331cb3c1a | -3.85817 | -45.11254 | 2025-11-15 04:25:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48767908-1ee7-3e68-974c-6c71f8f77c73 | -7.69181 | -47.19317 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3e242ae-cb73-3721-ae59-9ad0572d3f5e | -4.94252 | -46.80866 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 323a2daf-b300-3fed-b9f5-68cfbbef1d08 | -4.82203 | -47.09225 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fcd3aa32-aacb-3a42-a14d-04e15dd56d83 | -4.60688 | -43.36282 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8088e122-911d-367b-8f53-21b168f67176 | -5.88945 | -42.27367 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f264226b-7f34-3cf7-a2fa-43c977adbd8a | -4.89518 | -44.05626 | 2025-11-15 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f43019ee-0f2f-3b38-819e-441dc6f95a70 | -4.8129 | -41.61234 | 2025-11-15 04:25:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c163b0d5-0e3c-34e0-b93c-07f189ecba46 | -5.99717 | -45.40072 | 2025-11-15 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README35.md)
