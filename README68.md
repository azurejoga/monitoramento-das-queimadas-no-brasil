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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec0cf7a1-dd43-397d-aac2-073e4a09eecb | -6.09883 | -44.77576 | 2025-09-09 05:48:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 52098bb6-0008-3ed2-83eb-d15cb22f2a66 | -7.56819 | -44.65672 | 2025-09-09 05:48:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d812a5b5-f491-35a7-a22a-18445d763a43 | -7.43209 | -45.20658 | 2025-09-09 05:48:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3641c747-5124-38d1-9cc0-e0a1f5ccb586 | -6.39228 | -44.43084 | 2025-09-09 05:48:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2778467a-56a6-3775-8fb9-ec55e77b79d2 | -5.81299 | -43.97364 | 2025-09-09 05:48:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9724a7c8-024f-36d4-b2b1-de6337f4da41 | -6.86352 | -45.59718 | 2025-09-09 05:48:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3e4759f8-20d0-3c0d-a7f6-1f42003588d9 | -8.03151 | -44.02259 | 2025-09-09 05:48:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f921ba6d-4681-3e4b-baef-668bf3ba8f0f | -8.04749 | -48.64157 | 2025-09-09 05:48:00 | AQUA_M-M | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 123a069d-a0b8-3ac2-aa96-7dfb8c294927 | -7.24946 | -44.81806 | 2025-09-09 05:48:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9b8f5f7a-9fe1-3c6d-9dc9-2582b9dfe389 | -6.4305 | -44.05116 | 2025-09-09 05:48:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 7832cddd-79e7-322e-affa-d9fb0d031efa | -5.26332 | -44.44416 | 2025-09-09 05:48:00 | AQUA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0ff2d7b8-1332-3326-ab41-21469ad3befd | -5.57014 | -45.04273 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 32897473-549a-3b5e-aa76-675d625e0f77 | -8.03531 | -45.50107 | 2025-09-09 05:48:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2f137f43-76a2-36a9-a48d-d64352fdf742 | -5.67463 | -45.45648 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 32a4e5c2-9da0-3217-a788-c00272a20e6a | -5.21736 | -43.6951 | 2025-09-09 05:48:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7d120d9f-a1a0-31ed-8e45-b7de0d90f8df | -5.69534 | -45.98497 | 2025-09-09 05:48:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| aac13871-c742-3487-adef-aa2272724395 | -6.34041 | -43.78279 | 2025-09-09 05:48:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 340cee3e-42dd-3ab6-b1b3-51ac4e338bd2 | -6.86983 | -47.90102 | 2025-09-09 05:48:00 | AQUA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a60ac17a-ccde-3c53-a333-e65d8e33b4ae | -5.55166 | -45.16538 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1c044bb0-dcb4-3ec3-ab37-56d118a404a4 | -5.67633 | -43.89521 | 2025-09-09 05:48:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2a2b0364-377c-3e69-b8d4-dfdc110d5d9f | -7.55935 | -44.65543 | 2025-09-09 05:48:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 56be7e28-b273-3eb9-9dc3-091caea1f36d | -5.81188 | -45.65192 | 2025-09-09 05:48:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 94ec2939-1385-396b-ade5-9f3acc859191 | -5.21601 | -43.70419 | 2025-09-09 05:48:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c500031e-cc2c-3ef4-a706-2206178e4074 | -7.07098 | -45.20911 | 2025-09-09 05:48:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1cc1ecf0-84c1-3160-9035-1262583ca6d2 | -5.45199 | -43.42147 | 2025-09-09 05:48:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| c3726884-2ae1-3ff1-afca-3450eccaa039 | -6.40111 | -44.43219 | 2025-09-09 05:48:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4556eb05-3ba4-3de0-bd43-9d6c219597f8 | -7.65676 | -50.29068 | 2025-09-09 05:48:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 88fe6050-40c0-3cf8-bfe5-5623326111f9 | -4.73406 | -44.45514 | 2025-09-09 05:48:00 | AQUA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fa63d34b-db62-35ba-bc5f-9b51766aa56b | -5.35624 | -44.79621 | 2025-09-09 05:48:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e5e35e18-3f0f-3608-ae79-a56220b0db93 | -2.62757 | -46.83216 | 2025-09-09 05:48:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| aeb8d960-c56e-3cca-8ac3-995610a1ac6f | -7.78912 | -46.08421 | 2025-09-09 05:48:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7853c5ef-86f0-393d-acf8-9d3ad9d64e81 | -8.37277 | -45.02189 | 2025-09-09 05:48:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 0554fff9-4fff-3719-b837-174cb705750d | -5.81955 | -44.11246 | 2025-09-09 05:48:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| fcf71afd-1442-3323-8268-04619b145735 | -5.54902 | -45.18291 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 2bedf885-4fec-3efe-a244-bc40b5d1dd7e | -5.53711 | -42.65222 | 2025-09-09 05:48:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5f65a1d5-7227-3e1d-a1c1-24c5b8290151 | -5.75895 | -45.26897 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| da990d75-fab9-3faa-af20-29f43e12a8bb | -7.65653 | -50.28534 | 2025-09-09 05:48:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 3698f1c7-4245-31c0-b4da-a1c507176d13 | -5.76028 | -45.26019 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ae968b11-48fe-3764-9957-4174410ff438 | -5.45966 | -43.43203 | 2025-09-09 05:48:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 5fe3b1ca-9148-3e93-8643-3bb777c4ee4a | -5.22008 | -43.67683 | 2025-09-09 05:48:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 38366c10-affa-35e5-b813-2ac68dd866c7 | -8.00022 | -46.33613 | 2025-09-09 05:48:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6eb90ba0-9f8c-3a7f-b07a-da5d1464f129 | -7.87381 | -46.24984 | 2025-09-09 05:48:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 695354ff-dfd8-3e0a-8a4b-30a7c2d94345 | -7.99884 | -46.34514 | 2025-09-09 05:48:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e4c6797a-7c2f-31c9-b037-3591de799b58 | -5.21872 | -43.68594 | 2025-09-09 05:48:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 1a78ea0d-f5f6-355c-b148-b1d6cf43eccb | -5.45338 | -43.41212 | 2025-09-09 05:48:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 621feaf6-8b8e-39a0-b54d-51584e726eaf | -5.30822 | -44.50463 | 2025-09-09 05:48:00 | AQUA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 333623e9-4f94-37df-9a20-54ec9ddb0398 | -5.2263 | -43.69642 | 2025-09-09 05:48:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 94a94a52-de33-3bee-903b-ce5def7cd2a0 | -2.62601 | -46.84255 | 2025-09-09 05:48:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 437e1953-915b-3f7e-bd41-e23dd23fccf9 | -6.29901 | -43.81432 | 2025-09-09 05:48:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3ee2ae8d-d318-3ea6-ac3f-4922f290a844 | -4.73538 | -44.44638 | 2025-09-09 05:48:00 | AQUA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 45a28eb3-9e3c-316b-9210-192bee45bacf | -5.55491 | -43.78735 | 2025-09-09 05:48:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cd56c95e-542f-3b03-8fc5-c384d4860e3d | -5.80364 | -44.83887 | 2025-09-09 05:48:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1d524c9f-6d6b-36f5-a82c-75911ec48f60 | -5.75045 | -45.25196 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| fd3627f3-f5ad-3d7f-9434-74dd762b5b59 | -7.78029 | -46.08292 | 2025-09-09 05:48:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cd9cdd40-3e5f-3305-aee7-1174a28ab72f | -5.58326 | -42.89956 | 2025-09-09 05:48:00 | AQUA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5ebbda09-63fb-3488-84d9-8a5c79e0c90f | -5.45827 | -43.44136 | 2025-09-09 05:48:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 1165275b-b28f-392e-b833-cfbf1fd041a4 | -7.08108 | -45.20163 | 2025-09-09 05:48:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3982b7ba-4ce8-3e2b-821b-4c09e7fb7f23 | -7.0723 | -45.20033 | 2025-09-09 05:48:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 41a8966b-237a-3884-a5d6-35d1be0121d4 | -8.04923 | -48.63059 | 2025-09-09 05:48:00 | AQUA_M-M | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a91bb764-769f-3d58-a2fe-f9d72ce2e67a | -5.45011 | -42.80753 | 2025-09-09 05:48:00 | AQUA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e61ac57b-2865-3138-a596-1445f1573f28 | -5.83112 | -44.09576 | 2025-09-09 05:48:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fac66324-c913-325f-a795-f1f955d89dc7 | -5.74913 | -45.26073 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| bb3a878f-a895-3151-b17a-9933b49a8f14 | -6.42916 | -44.06026 | 2025-09-09 05:48:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e54b710c-5ae8-375f-a071-ef586e40c3e4 | -5.58024 | -45.03527 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d362a03f-ccf8-349b-87f7-433995e996be | -8.11835 | -44.86612 | 2025-09-09 05:48:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 137622ef-74c9-3247-847c-23d6e3f585a3 | -5.68782 | -45.97464 | 2025-09-09 05:48:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 82d3f360-356f-3c9b-bd16-0154259ab94f | -5.8182 | -44.12144 | 2025-09-09 05:48:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 82f76ae4-ce5c-3a48-a573-67ed6cc3b08e | -5.58156 | -45.02651 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cbea16b4-5f0c-37a2-bf19-339ebdf2ea64 | -8.05909 | -48.63217 | 2025-09-09 05:48:00 | AQUA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 13.9 |
| eba0215e-3628-32ba-93ca-b5cb116cd645 | -7.86495 | -46.2485 | 2025-09-09 05:48:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7d98a54b-7630-3865-90ba-bc277c7b6e9d | -5.69671 | -45.97597 | 2025-09-09 05:48:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 81daf5dc-9b29-39fb-a731-d93a08830152 | -5.1638 | -42.93744 | 2025-09-09 05:48:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 73256d21-b89c-36e1-a6f5-a22a04265abc | -5.51541 | -42.66972 | 2025-09-09 05:48:00 | AQUA_M-M | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 867ea0cc-2424-3dd7-8628-e733d48e5c1d | -7.33562 | -49.55962 | 2025-09-09 05:48:00 | AQUA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 575a4e1d-be42-37b6-afca-b34441afe633 | -5.57892 | -45.04402 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| d5709a77-495b-3d22-ab05-bc5bf929c863 | -5.01545 | -48.46769 | 2025-09-09 05:48:00 | AQUA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e1fcdc85-c0ca-32af-82ed-9122993d95f1 | -7.0824 | -45.19284 | 2025-09-09 05:48:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c639e0dc-707a-3cfa-bc74-7c623a169134 | -12.1988 | -53.9024 | 2025-09-09 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 2802ea73-c788-3dbb-b9fa-4d5e4ff0ab14 | -21.4762 | -48.8406 | 2025-09-09 05:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 909f89fb-6da4-3698-97ea-3153bd4e4edc | -18.8375 | -49.6777 | 2025-09-09 05:50:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.0 |
| f1e5747d-4f76-37a0-a46b-13a469c60feb | -21.4755 | -48.8639 | 2025-09-09 05:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 2be966cc-db48-3f6e-b3aa-bd60a733318c | -12.1991 | -53.8817 | 2025-09-09 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 9b7c2a8a-4ef1-3415-80ae-da9bd13f5586 | -11.9735 | -51.0148 | 2025-09-09 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 3d776f15-9859-35c3-9f0a-56e1dd8635a8 | -14.3615 | -47.3333 | 2025-09-09 05:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ef83cb8e-21ef-3fb1-bef3-6ac00f3eb231 | -14.362 | -47.3107 | 2025-09-09 05:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 428371cb-0bc9-3f7a-b4bd-65348c167f87 | -13.9375 | -48.2299 | 2025-09-09 05:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 7e66e229-311d-3cfd-9c4d-167595cc931d | -13.937 | -48.2522 | 2025-09-09 05:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ee3f37a2-bab1-3801-a57b-ae00159af5d1 | -21.4548 | -48.8687 | 2025-09-09 05:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 19835a75-b373-3d1a-a5b3-d1df73fa2e88 | -22.3463 | -50.9117 | 2025-09-09 05:50:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 67412222-97e8-36c9-8288-9eee66e2d675 | -18.8168 | -49.7042 | 2025-09-09 05:50:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 803f2f6a-1857-3108-8100-9bf4efbad4a9 | -21.4555 | -48.8455 | 2025-09-09 05:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 21d27734-3166-382e-9df2-d8db5ce3ae05 | -18.8174 | -49.6816 | 2025-09-09 05:50:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 3dff2338-8976-30da-a9c9-e7893745405a | -18.8369 | -49.7003 | 2025-09-09 05:50:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| d3c6681c-65d3-32ce-add7-8ed27d1fbae1 | -11.18828 | -48.38663 | 2025-09-09 05:50:00 | AQUA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3768566a-a857-3b6e-b5c8-358c880a2a76 | -10.00404 | -51.6773 | 2025-09-09 05:50:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a15a187e-fd38-308b-8dc1-1deafa84f18b | -11.45193 | -49.2653 | 2025-09-09 05:50:00 | AQUA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 55021e1e-6ab2-3fe3-8ce5-580fef5b125a | -11.83639 | -46.76103 | 2025-09-09 05:50:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c53f1d23-4535-3b9a-88fd-bed67e1a3310 | -11.84382 | -46.77138 | 2025-09-09 05:50:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 816f775f-6a6d-3af2-9820-3ab2e43216d5 | -10.33806 | -47.72579 | 2025-09-09 05:50:00 | AQUA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ad21b173-768a-3d93-8e57-ea0a576d5a28 | -8.40838 | -49.08781 | 2025-09-09 05:50:00 | AQUA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README69.md)
