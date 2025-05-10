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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f42076b-4e08-307c-97dc-cbdfbc9a646e | -20.76515 | -46.77037 | 2025-05-10 04:23:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3822459-d18d-33e1-bd9f-cd56fc142c82 | -19.87486 | -46.61356 | 2025-05-10 04:23:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0238093b-ac13-36ab-bdf8-b2e79612b70d | -21.20061 | -41.30325 | 2025-05-10 04:23:00 | NOAA-21 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 93e0d338-ba00-3ada-bd0e-2ea04ce76922 | -23.4048 | -46.5563 | 2025-05-10 04:23:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a036e00e-fb53-30d2-870d-750272ea02ba | -19.55246 | -45.29058 | 2025-05-10 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 239d5a3a-7282-303b-b4c6-e928b34cf507 | -18.9571 | -52.24947 | 2025-05-10 04:23:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d78eb59b-6b98-300f-97e2-b4731874fc32 | -21.20009 | -41.30793 | 2025-05-10 04:23:00 | NOAA-21 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9bd3ba7c-d048-3ece-8171-6f5c5c74c51f | -20.51336 | -47.35828 | 2025-05-10 04:23:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1359f51-3e8b-3fe8-9709-88e6a72800f6 | -19.13415 | -48.02523 | 2025-05-10 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cda451b7-51ee-31f5-bf63-2dc911b6e5e7 | -13.9902 | -56.8058 | 2025-05-10 04:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| eb517a18-ce15-31d3-a938-c4203af518d7 | 0.71493 | -51.3721 | 2025-05-10 04:44:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3806f6c8-aada-3a72-9ac9-4bcef7b33164 | -7.29798 | -55.31225 | 2025-05-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e700daeb-38c3-3444-a5d9-b7c3c12823de | -9.84331 | -44.68681 | 2025-05-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7eb01544-ffc1-3e3d-bb7e-c77027bdd2b1 | -7.05554 | -44.35378 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5220e7f1-9306-31aa-8992-089bf1c0c59a | -7.07508 | -44.38032 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2abaf72-1ed4-3557-aad5-e3c91a6614e1 | -7.08956 | -44.37727 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ce0c747-5062-3ccc-92c1-2a13396b0508 | -9.84863 | -44.68267 | 2025-05-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de69d53a-da1d-3c80-bda1-e34171f53c20 | -10.49191 | -42.40864 | 2025-05-10 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f6b67fa6-1c71-3f7d-8c71-881cd657445a | -7.08037 | -44.37614 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5b70cba-33fc-3841-bec0-fc561366b817 | -7.07417 | -44.38191 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc6ac841-6b36-35e2-8c66-493a26a186a0 | -7.07351 | -44.38668 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 018040e6-1ffd-346c-9ea2-327707bbd965 | -7.08402 | -44.37831 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6c420c7-cfaf-3c29-a696-adf9fce0323c | -7.08497 | -44.37669 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65c99a20-dd52-3d9f-bf38-a7b13ec63175 | -10.49237 | -42.40505 | 2025-05-10 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dc2928f7-a542-35b8-9417-aa28ac52a614 | -10.49834 | -42.40218 | 2025-05-10 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0f1a0674-abc3-38e8-bde6-2e89f6cdb88c | -7.07369 | -44.38977 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7672edb-ad1b-3923-9bbf-64d3d8b8f170 | -8.1531 | -46.72527 | 2025-05-10 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efa22212-8275-355e-a58d-3c3cf3e2368f | -5.10265 | -44.79913 | 2025-05-10 04:46:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52d7ea0f-2575-3be7-98c0-bc83e2cc6cbc | -9.84397 | -44.68191 | 2025-05-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 045720d1-5ab1-3ae3-ae72-37ff0b60c18b | -7.30178 | -55.31288 | 2025-05-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84cb02c0-e2d2-35ba-bf67-12a6a901a62f | -7.07438 | -44.38508 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad7467f1-ffcd-3297-85bb-15b6ada664a4 | -7.29721 | -55.31689 | 2025-05-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 74cb7032-3ad8-3a45-ac27-b23fab6b8301 | -10.49283 | -42.40143 | 2025-05-10 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d499bee-37a9-320d-b0ec-03f17a6963a4 | -7.08469 | -44.3735 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ac5aa34-cbe5-3b85-92b0-f2a4f115bc5d | -8.46867 | -49.61864 | 2025-05-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0535f553-c4c6-38d6-9c9a-1231b686b777 | -7.08862 | -44.37889 | 2025-05-10 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1067d07c-d010-3669-86e6-f7fac6dd2708 | -12.17374 | -54.24116 | 2025-05-10 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efb6dc6e-57a4-3b65-ad5b-5491dc372f42 | -12.72624 | -54.97451 | 2025-05-10 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d497387c-776c-3599-9a57-63a5af09388f | -13.62298 | -54.8818 | 2025-05-10 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cde04da6-5953-352e-a191-6fad6d9825dc | -11.15087 | -48.67667 | 2025-05-10 04:49:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89934399-b3db-30d4-a65c-d770a168defa | -11.37869 | -55.12314 | 2025-05-10 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 579f557d-a969-3a1f-b027-070efd81d0a8 | -16.1123 | -47.55816 | 2025-05-10 04:49:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fce3937b-51ca-3f32-8300-ea16283d1646 | -10.99244 | -44.44286 | 2025-05-10 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 907aa67d-5711-3b93-b95c-a1533d7fc265 | -12.6288 | -54.06676 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51731366-06e9-3cbc-82b4-701c22ce3360 | -12.64717 | -54.06244 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9e9e89e-6907-34bc-88ed-5d15b68b1da6 | -11.37303 | -55.12347 | 2025-05-10 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 214ba540-ee49-329c-8e3c-e2cff7e1baec | -13.97495 | -56.81004 | 2025-05-10 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 37c105d4-e990-3e5d-9b08-ef4fb70e76e0 | -10.6422 | -44.4841 | 2025-05-10 04:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ad0a2de-fb4b-3b46-9c3d-ca0e19b27d20 | -14.64566 | -45.13992 | 2025-05-10 04:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41eaebe9-5a6a-34ee-bef4-a448d013b412 | -15.30667 | -53.31494 | 2025-05-10 04:49:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04a5fadf-0892-3c1b-aac7-c767684a9a07 | -13.3761 | -54.25948 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24e034b1-a7d4-3703-873e-6d8d5b945217 | -11.37582 | -55.11839 | 2025-05-10 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a9c5edc-9f13-3d1f-b659-1e80fee00312 | -12.62894 | -54.06701 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54cd8f27-1cc6-3bb7-8875-afd640c40566 | -12.68733 | -58.1496 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e72005fe-8aaf-38bd-8184-66b6ce71c075 | -13.9833 | -56.80679 | 2025-05-10 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 80de002f-ae19-322f-b45f-26d77bc596ea | -10.64291 | -44.4788 | 2025-05-10 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a2642e3-0958-39fc-b98c-7e18ddeb0e32 | -13.37486 | -54.26696 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9df69bd9-73a8-313f-b491-118e26771909 | -13.37548 | -54.26322 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81baf28f-1ac0-36aa-b6d5-cb4c3a7fa988 | -10.99173 | -44.44818 | 2025-05-10 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd6b58db-ead6-39c2-bd71-df4745ed807e | -11.06748 | -46.12395 | 2025-05-10 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7a0a0a6-2b20-3680-a858-dbd162785be0 | -13.04136 | -53.72385 | 2025-05-10 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3de300af-0660-347c-a19a-3883bb97f908 | -13.09056 | -52.29348 | 2025-05-10 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 91986d41-2dcf-34fd-8e43-861f79fe79de | -14.64703 | -45.12904 | 2025-05-10 04:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9dab1c1-39f3-3017-a61c-8577ba771cea | -13.09112 | -52.28993 | 2025-05-10 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a8a66b6c-d82b-398d-b8d1-2f7c80b91a41 | -12.68655 | -58.12953 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 961a5b49-64a3-33f4-9fde-d4cc9c3b8c53 | -12.17436 | -54.2374 | 2025-05-10 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80e16335-50ac-3985-894a-3088f431462d | -11.91423 | -54.40129 | 2025-05-10 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4238e73-edb7-3ba6-bbde-d32b08fdc32b | -11.77888 | -48.7 | 2025-05-10 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31de0a92-84ad-3f72-8f5b-a39c441fdf1f | -12.69176 | -58.14944 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f947250a-8ac5-3ee2-8534-64f7a10c93e9 | -13.24788 | -50.13068 | 2025-05-10 04:49:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| cdf69c35-acc1-31e6-a21b-068c204292ac | -10.98347 | -44.43632 | 2025-05-10 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19f01bb5-245b-3abc-a738-10f8ee9b4c5d | -12.36726 | -63.92433 | 2025-05-10 04:49:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 669297cb-7bb6-3852-a034-5ea5dde30b43 | -11.40548 | -52.9533 | 2025-05-10 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 887e37ff-1b1b-3aad-8500-43f17515b288 | -12.63976 | -54.065 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f7d26ca-67b1-3e76-9a83-b507bf8e8262 | -11.40605 | -52.94973 | 2025-05-10 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80b00006-f211-3cdd-98fc-7862aa28cd35 | -12.63915 | -54.06872 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fb3924d-8d82-3050-b3eb-18d1d1a163ae | -10.97309 | -44.44038 | 2025-05-10 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ecb80ce-2372-3423-8abb-f42e82b1abd4 | -12.68759 | -58.14869 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0c95e5c-4080-3de7-b05f-fff7a8d6babf | -13.97872 | -56.81078 | 2025-05-10 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 85c33db0-ae49-3a12-b664-98f51b0e0ca3 | -11.62354 | -54.93715 | 2025-05-10 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acf582ae-452f-39f0-9c84-cba0174e6c2e | -13.98248 | -56.81153 | 2025-05-10 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| bf80f955-4fde-338c-929a-b66273c1d4db | -13.97577 | -56.80532 | 2025-05-10 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e50f7015-af24-3a25-a7b5-842625521886 | -15.07987 | -48.94506 | 2025-05-10 04:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1841b262-a5d6-34d3-98fd-2749e5acff13 | -12.63234 | -54.06758 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a811cc86-e548-378c-9bb5-916b8e254f2b | -11.14719 | -48.6761 | 2025-05-10 04:49:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 569060b7-68b2-3b17-a194-ef56264ba87f | -12.32994 | -55.16533 | 2025-05-10 04:49:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4016a99f-dbb0-3e3b-a752-1dbc27e82e80 | -11.97356 | -63.53109 | 2025-05-10 04:49:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dea797ba-642e-347d-825e-d1120270af38 | -13.04077 | -53.72749 | 2025-05-10 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c99a1e7-bc3e-3ec6-8f48-d450c4d2eec7 | -16.10808 | -47.55762 | 2025-05-10 04:49:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3653d566-f9b9-3e7e-b15f-3740e6675784 | -12.64255 | -54.0693 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e32e1cb1-922d-3a35-82fd-3b485a7e5284 | -11.66248 | -58.26687 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc25e8a2-ddf9-362a-b585-01bcfc18553c | -11.77518 | -48.69943 | 2025-05-10 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 136fb113-ca19-32e0-b584-ccc3240c70d4 | -12.69151 | -58.15037 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c8e1586-a95d-31d6-8faa-9567017c7a47 | -10.9876 | -44.44225 | 2025-05-10 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c502df3a-a090-3068-9b18-dd57cf770af6 | -12.68687 | -58.15258 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47fc663b-2264-3bb3-b91a-0f03d5658216 | -13.2514 | -50.13122 | 2025-05-10 04:49:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 01b41329-9c08-3aff-b459-c02144ee44f5 | -10.97379 | -44.43505 | 2025-05-10 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41d7593b-98b4-31be-a514-ebc9ea5615bd | -10.6707 | -44.38055 | 2025-05-10 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 813d12e7-0496-308b-b4ee-7c4f1c72c428 | -12.17498 | -54.23365 | 2025-05-10 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c675a2d0-fc7f-3544-96a4-966f8b8b91a7 | -12.69005 | -58.13412 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README6.md)
