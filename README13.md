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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3525463d-6919-320c-b586-456680c8de1f | -7.44996 | -45.19826 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 142896e7-7568-3dcf-b47d-f57df1298400 | -7.21176 | -44.63601 | 2025-11-19 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e34c30d-d59a-3221-924f-d9ebec34e49c | -8.99546 | -40.43259 | 2025-11-19 04:29:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7f5bfe4d-a82e-36df-bb98-31a2c33b4a3a | -8.80971 | -37.33707 | 2025-11-19 04:29:00 | NPP-375D | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29755ccf-d23c-3691-a165-24f79e755c8b | -7.84559 | -42.83989 | 2025-11-19 04:29:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b06396c2-1b5d-3ec8-b773-c7e4c85de34f | -3.7367 | -45.60449 | 2025-11-19 04:29:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4870d2a-ddbd-3d7f-8904-4732ece914bc | -6.11986 | -42.95777 | 2025-11-19 04:29:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a9287bdc-0d05-3aeb-a905-45327aeabbc2 | -4.58208 | -44.06697 | 2025-11-19 04:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4c6bf2e-35f5-3ac1-92ce-a2b4b0472593 | -3.68315 | -50.16689 | 2025-11-19 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f62d3a03-9cef-3ca4-b145-97a3ef3cee85 | -7.43881 | -45.19638 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6ba2ed6-56e3-3bce-9ee1-148ec5e189f0 | -9.11355 | -44.67697 | 2025-11-19 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 893ebf2e-e330-3053-95e4-a6118f62118a | -4.04197 | -46.00991 | 2025-11-19 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab6a9094-88d2-30b5-8b35-d9c8f8662a91 | -5.62805 | -45.17492 | 2025-11-19 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e0b7d27f-59d4-3dbe-ba22-82754398b4f1 | -9.2788 | -48.55288 | 2025-11-19 04:29:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72132490-014b-32b6-b324-f77e25aefdd3 | -8.75488 | -44.17038 | 2025-11-19 04:29:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbe7842b-0bef-3cce-bf86-bd3ce1081813 | -4.69093 | -45.88605 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81378192-b3bf-3e83-9899-1560f98290b1 | -7.42967 | -48.93681 | 2025-11-19 04:29:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cba89ee7-9e5e-345f-ba55-0ba628d9e033 | -5.42821 | -43.9886 | 2025-11-19 04:29:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f61e0757-6689-3e85-b6c6-e924cd90b5b3 | -6.64728 | -39.24608 | 2025-11-19 04:29:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a787b5f9-c2db-3a54-a042-4ad881ad92af | -3.84976 | -43.94877 | 2025-11-19 04:29:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ad49d4a-7a1d-30c0-977b-b7a44b2ce1ac | -5.33626 | -50.89317 | 2025-11-19 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 984e8c05-313c-3236-bd93-0d0bcb05c462 | -2.28636 | -53.64826 | 2025-11-19 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d5f5c60-21f2-3b5e-98de-92c3e00a489e | -5.62033 | -37.80537 | 2025-11-19 04:29:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c02ba8a7-abee-3730-b1c1-68bae4772775 | -5.09105 | -37.86884 | 2025-11-19 04:29:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c877c403-b80c-36ea-bb88-c1154bbe1569 | -5.11933 | -46.08819 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2a98fd1-2d76-3b6e-8ee5-f4594ce53146 | -4.4912 | -45.86531 | 2025-11-19 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 156fcd6b-abb6-33ac-ad06-9cfdf93c2248 | -8.87797 | -47.33232 | 2025-11-19 04:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cac1375-fba6-3e9b-877a-09d0eb138df3 | -2.87944 | -52.61731 | 2025-11-19 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d63feb49-5cda-3aab-956c-6bda9ec95b9e | -10.12032 | -36.39314 | 2025-11-19 04:29:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 460c4dbb-83cb-3abe-af52-454e866bb581 | -8.87465 | -47.33179 | 2025-11-19 04:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a93700a8-6aa8-3642-ad3e-0dadd094e636 | -8.39313 | -44.0622 | 2025-11-19 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a68a7b5-54f8-373c-acf3-c6e5246bd706 | -4.9937 | -44.75807 | 2025-11-19 04:29:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b390194-0214-31a1-bc3f-3b90bbe82b23 | -8.38607 | -44.06111 | 2025-11-19 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea37d53d-ee16-37c0-ab0a-28797c026389 | -8.87853 | -47.32882 | 2025-11-19 04:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94aa1938-b37e-3e10-a5ae-453fdcaec697 | -4.48435 | -44.33531 | 2025-11-19 04:29:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 620b0245-119a-3cbf-aa8b-d1365ecce7ac | -4.78712 | -40.24815 | 2025-11-19 04:29:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d7ac860b-4b3e-382b-bfad-1ced33eeb732 | -4.76133 | -45.75882 | 2025-11-19 04:29:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3188f3f5-6b07-3d3f-ac87-fac1ecb980ca | -7.44376 | -45.19365 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7c9d2e8-3fba-38c6-8966-ffda6329c6de | -5.71623 | -49.01899 | 2025-11-19 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 888fbb74-7605-3795-ac86-68bc837acfe7 | -3.02143 | -49.43462 | 2025-11-19 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 255a44a5-45e2-3e99-824b-b214cb8a0380 | -4.75801 | -45.7583 | 2025-11-19 04:29:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db742355-d301-3b22-99ff-ac4f42fafe27 | -6.55455 | -44.46569 | 2025-11-19 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 969d6e15-8bd4-3579-be8a-c220bff9eb25 | -7.43825 | -45.19996 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 173ce004-f35a-3265-a06d-a1c825d2f997 | -3.67923 | -50.16626 | 2025-11-19 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae7cd9e5-15b5-3118-8730-6d8931d267f6 | -6.20169 | -39.39509 | 2025-11-19 04:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c1ef85dc-ee70-3719-8e63-9966fb467b40 | -4.99034 | -44.75755 | 2025-11-19 04:29:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f45a2aef-2767-308a-b6f4-21a9d3645d78 | -5.22873 | -49.57566 | 2025-11-19 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb237f6f-6b79-3de8-b268-d487a26a06e7 | -2.28125 | -53.64763 | 2025-11-19 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb5a3ff3-f303-3ba3-91a7-cdbed136f122 | -8.20233 | -43.02781 | 2025-11-19 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8723fadd-1eef-312e-93f0-f8fce1aac8c9 | -6.72069 | -42.12484 | 2025-11-19 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1a5d2e27-be76-3e1b-93db-5228e0c449f1 | -8.30725 | -44.05787 | 2025-11-19 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6117726-0782-3882-8d0b-6dc560a74143 | -6.89301 | -40.09184 | 2025-11-19 04:29:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 32e69244-c4e6-3d69-b3d9-597f7d603157 | -8.87577 | -47.32478 | 2025-11-19 04:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0371443-709f-3e9a-9a61-e7c683471a49 | -2.91054 | -49.08948 | 2025-11-19 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb284634-7e35-3542-9363-d1788301bd08 | -7.62985 | -42.57869 | 2025-11-19 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e2a94465-cc85-32d8-895e-d7c794044ccb | -4.88395 | -45.86311 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e45013ae-2cb8-3120-90ee-bb82ee3b9d7a | -8.21729 | -50.48148 | 2025-11-19 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 908af12f-e0cc-3cb1-8090-f2813516f16b | -9.66454 | -43.89185 | 2025-11-19 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2766198e-a826-39dc-b7d3-b3c98ecbc27b | -3.67843 | -50.17117 | 2025-11-19 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25d5ef7b-eb43-3ae0-8556-9b4bfd97b2d1 | -5.11988 | -46.08474 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c86e1b0a-8333-3c42-a392-36e344542305 | -5.05031 | -45.13169 | 2025-11-19 04:29:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 800f1823-31d3-366f-93d3-476fd1d0079b | -6.20493 | -39.40487 | 2025-11-19 04:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d1adff33-5c6e-3d24-b587-e3255f71bb6b | -6.55112 | -44.46516 | 2025-11-19 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82b11001-b227-39e9-93d0-fe25592731c5 | -6.89236 | -40.09624 | 2025-11-19 04:29:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d14e1909-058a-36a3-85f4-fed7bbe73b8c | -6.86205 | -44.84547 | 2025-11-19 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a753d795-448e-35f1-a3ad-134df65076de | -8.29944 | -42.25291 | 2025-11-19 04:29:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db1ab118-d3de-3df6-83ad-dfa226e58983 | -8.8813 | -47.33286 | 2025-11-19 04:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36163475-a306-3863-ae21-0725dd7bf5b7 | -5.2881 | -45.83115 | 2025-11-19 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3428a7b5-7681-3204-be2f-0bd0dc97b457 | -8.6037 | -47.92693 | 2025-11-19 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db7ae32b-c86b-3ee2-9431-2932960d1fce | -4.42274 | -45.91116 | 2025-11-19 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 96624b60-5e8c-3fd9-a0be-276c920ee718 | -8.38253 | -44.06057 | 2025-11-19 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74af18d2-bcf7-3bc9-9bfc-a432139e36c7 | -3.23694 | -48.52027 | 2025-11-19 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f53f79be-eeb9-3ef4-82bc-7a15dcdbe145 | -8.13586 | -47.59605 | 2025-11-19 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b052e45f-1365-3e7c-8f55-6ef8cfab2bfb | -3.01386 | -49.43342 | 2025-11-19 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0afdad14-6952-34e9-bf2c-acb3f0f1bed1 | -5.45887 | -50.74579 | 2025-11-19 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d9e19b9-5870-3157-bc86-be3432dbf0e1 | -5.68371 | -38.59637 | 2025-11-19 04:29:00 | NPP-375D | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 221ff7c6-e107-35aa-a769-e36375645b87 | -4.755 | -45.90649 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c1959f3-b07b-3188-a6ca-0eb3e3251094 | -4.10962 | -49.09954 | 2025-11-19 04:29:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93cdf730-441d-37e2-ad6e-25e36c04b808 | -6.21694 | -39.60732 | 2025-11-19 04:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b2d8b9c-527c-3029-9e6f-5e552abf29df | -5.62076 | -37.80242 | 2025-11-19 04:29:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5d2d1127-535b-3a2e-bf92-12d7d902b108 | -7.34163 | -40.02524 | 2025-11-19 04:29:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1f421866-deca-377b-879a-e32b37944052 | -8.28682 | -43.9525 | 2025-11-19 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a33189d-1863-35c0-b718-3315511be861 | -6.71996 | -42.12959 | 2025-11-19 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f5510394-bf24-3486-92b9-07dc8efff81b | -10.00647 | -39.192 | 2025-11-19 04:29:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7060341c-b98a-39f0-9d2d-44949456c53f | -3.40746 | -46.9078 | 2025-11-19 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96f5b990-2117-379b-9e1a-c061a0b104a9 | -3.34885 | -48.37207 | 2025-11-19 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 983db6d2-32c8-3f9e-adca-0b5eca4f8658 | -3.08403 | -48.15168 | 2025-11-19 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 79d9caca-986f-356d-bb72-8d9dae9596e5 | -7.14623 | -44.92295 | 2025-11-19 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c45594b-ddf0-3e4e-8460-7d2e75fd585e | -6.99188 | -44.63687 | 2025-11-19 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31227c25-71a5-3d35-8b5b-68855657383f | -5.12896 | -44.05079 | 2025-11-19 04:29:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f563e32-454a-3965-b47d-09041205cec3 | -6.65193 | -39.24674 | 2025-11-19 04:29:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 91c57256-2a60-31bb-9832-636d695cf565 | -7.44659 | -45.19774 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 770455d1-f6ef-3ef3-b228-c4662b7552c6 | -4.15233 | -46.78814 | 2025-11-19 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09840ea6-b828-39ee-9216-cec47261b542 | -7.43377 | -42.75835 | 2025-11-19 04:29:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a4ab6afd-d1d2-35f2-b882-8d417aff84e4 | -8.12248 | -47.59389 | 2025-11-19 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51cb3094-608b-357b-9b55-94e66e3edb32 | -5.21235 | -45.0202 | 2025-11-19 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 05dda0f5-414b-3a21-bfbf-16d255d99180 | -8.21834 | -50.47952 | 2025-11-19 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2578cb68-7567-3164-b8bc-4b17d7f998c9 | -3.34821 | -48.37607 | 2025-11-19 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d5551ade-832a-378c-8062-f7d2484c7454 | -3.3708 | -49.25736 | 2025-11-19 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c978d479-4d12-3ba9-a698-cc67f75e3b5c | -7.45278 | -45.20234 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
