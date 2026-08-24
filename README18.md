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
| a10de9f9-81c5-387a-b9ff-58a180f36d7f | -9.95033 | -48.33852 | 2026-08-24 04:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 355cbf3e-3dce-315b-bc7e-3fe70542f142 | -10.73673 | -47.97889 | 2026-08-24 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 030cbc96-a3db-34d9-bee5-4911d7911e6e | -7.31626 | -46.14762 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb622cd0-67ab-3478-a965-8b5637f3428b | -10.69739 | -47.75459 | 2026-08-24 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2ad3c7f-d63f-3e3c-b6db-639ed34f0aaa | -9.05568 | -50.76982 | 2026-08-24 04:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cbec5f0e-eb7d-3148-90cc-169e71191a35 | -10.79461 | -50.95208 | 2026-08-24 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e16bf917-ac1a-302b-9a66-5cebcb8a7232 | -6.94622 | -42.69588 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0dc57966-2ead-3720-86f0-d78e63ec75ff | -6.3333 | -54.75512 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bb97e55-8616-3096-b664-aebe3ba14449 | -12.13388 | -43.39734 | 2026-08-24 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79ee58bf-9671-34d0-a39c-1237f1062710 | -12.13724 | -43.39787 | 2026-08-24 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ee126b7-592d-3aaf-a914-e2ecefce36ed | -6.33953 | -54.75626 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec521bca-d4a0-396e-b8ea-4d0e0575d0fb | -7.37679 | -45.82207 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45a06b1b-f753-37f5-9564-54524256076d | -10.07052 | -46.37464 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93c9af63-1028-32d7-9fb6-cfd3a9fbe25b | -7.30584 | -42.97462 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b27e0e73-2dff-3657-b222-e509b92440ab | -8.56266 | -47.44535 | 2026-08-24 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd88fed2-cafe-3e4b-b56e-46752edfc4c2 | -7.30807 | -42.98211 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bcdd8ea2-3e9e-3c82-b42e-d702458b8858 | -6.22591 | -55.61668 | 2026-08-24 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edc6c529-d1f5-3bde-806f-d9005914f9e9 | -8.08683 | -50.05013 | 2026-08-24 04:25:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b383e68d-706a-33b9-9315-4e0b78b3deb8 | -7.16254 | -42.74034 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 76102557-4933-3607-8f18-668229881d15 | -7.36473 | -45.80814 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6761f54c-4ae3-371c-b855-9391145f6e0e | -7.18865 | -42.74807 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 353970c0-6c80-3e90-962f-331e30242a5c | -7.24901 | -49.87292 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ed9a18fd-71f5-35c7-b490-c0e59e1203f3 | -5.0656 | -49.38299 | 2026-08-24 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6238de50-f3b0-39e8-bb02-125503221b9a | -10.01345 | -46.82545 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd032233-0641-3742-93f4-45bf679ad0a8 | -7.26942 | -45.36739 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d2d2e183-ade3-3c78-9c0b-159a03c0fc52 | -11.11624 | -49.88954 | 2026-08-24 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af3a809c-1b92-3904-a359-b39aab67f328 | -10.73748 | -47.97457 | 2026-08-24 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a794936-12dc-390e-ad51-7b326e41847f | -7.77994 | -56.29029 | 2026-08-24 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 389847e7-4acc-3fa3-a316-838636c172d8 | -7.3625 | -45.79984 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c83630fa-0bf1-3342-9130-73cd7465be9f | -7.97102 | -43.9216 | 2026-08-24 04:25:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 893f62f9-0323-34de-998e-01c877b8565a | -6.18783 | -53.53296 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9718f014-bbea-3fa1-88ba-b6921e575cb8 | -7.81025 | -45.19878 | 2026-08-24 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f29acfe2-9f27-3da7-ab76-415e857973bd | -8.08145 | -47.27508 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e2c9cbe-a838-37a5-a2d6-41a738aaff82 | -8.37489 | -46.4737 | 2026-08-24 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e9516a9-f482-3790-97ca-082259b12a42 | -12.028 | -41.92831 | 2026-08-24 04:25:00 | NPP-375D | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 370eb9d1-1aaf-3a8b-89d3-0de05d3e04db | -9.05111 | -50.76894 | 2026-08-24 04:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3203093f-8366-3be5-bd2d-c9c7fc566ba8 | -6.18134 | -53.53598 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb1480c5-3356-3da6-9136-4844e31be1d7 | -7.89696 | -46.32391 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7d7385f-e8a6-3c45-9d56-69c84ee0f329 | -8.31345 | -46.89326 | 2026-08-24 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21bb5e30-6642-3a40-b7e9-02957b444b92 | -7.96758 | -45.28424 | 2026-08-24 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5725ab36-9eac-3f1f-87ef-51ac0945bc22 | -7.18253 | -42.74351 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c1aaf8f4-c729-3668-9691-599826f34f8c | -11.58539 | -46.95503 | 2026-08-24 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59c84dd7-0a44-37f5-b103-29048ff9881e | -8.10984 | -47.49512 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbe1963d-c209-3669-850b-c4db1e393e76 | -9.02992 | -50.75522 | 2026-08-24 04:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03a74139-5ddb-3952-ab7e-154c9e790ca2 | -6.34576 | -54.75736 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1618171-576d-3848-b731-468ce1647f64 | -10.46959 | -49.52131 | 2026-08-24 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9fd559c-af26-33dd-a092-d3ac36cb18cd | -8.95818 | -50.76022 | 2026-08-24 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52869a76-f5b2-3eb0-b2a9-27dbe23b0f53 | -11.09955 | -38.59651 | 2026-08-24 04:25:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 255cc02e-7d19-30e5-8007-cdb72321b7f9 | -6.1936 | -53.53408 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 915dab4d-7d69-337c-bb29-396fa10a73cf | -7.24585 | -49.86475 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1f04f94d-7308-3428-9ad1-5cd1abd47ca5 | -10.70183 | -47.75084 | 2026-08-24 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e58caf1-f13c-34ec-84b3-8589e4e00d08 | -10.6323 | -52.24741 | 2026-08-24 04:25:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3c4edb6-6087-3c61-9338-4eaa4bafdd2e | -8.09579 | -50.05114 | 2026-08-24 04:25:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3bb4b52-1a8d-3683-8dcc-e99da07800f1 | -10.29115 | -48.20375 | 2026-08-24 04:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c37e40f3-91ea-3928-b838-a3b661c51d26 | -10.55257 | -46.31841 | 2026-08-24 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53b17971-c02c-3f6f-a2ce-5e584bbb6f34 | -10.01768 | -46.82198 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c26a3d6-a2b9-3bb1-aae2-0e0f4ea34743 | -8.11125 | -47.48841 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13b48a75-a309-3fc5-9faa-fce79aa2825a | -7.25576 | -44.20152 | 2026-08-24 04:25:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d57ebaba-6219-361d-97aa-ad1838aa7bde | -11.78621 | -47.26548 | 2026-08-24 04:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e9a2f3a-336a-3ed1-b332-503657bc1e6c | -6.95343 | -42.69343 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 87cecebb-b4b1-33cd-b929-b159636a2722 | -5.00712 | -56.13691 | 2026-08-24 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc6dcd75-d530-3b91-863f-61f10ff6fc54 | -10.06768 | -46.37019 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 320cb237-770b-3669-980f-3c3b04fb73ab | -7.19366 | -42.75962 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d692317-709c-3854-ac5e-e282bc1f4487 | -10.80524 | -50.94468 | 2026-08-24 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a167677-079e-3138-a76e-be6f73f94b2f | -7.30252 | -42.97409 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1385b460-d9f1-3a19-8219-2eb2cd06dfde | -7.19311 | -42.76311 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a6f39f6-8e8e-3d16-992b-325e4afb67ac | -7.36568 | -45.82422 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 37759ba8-45d5-31ad-b73b-4ad7c5879514 | -12.40289 | -42.89849 | 2026-08-24 04:25:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1de0176d-59b4-3ab4-adab-b5f963dd5ab8 | -6.19353 | -53.53167 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c58f11a-f3b2-37b5-bf4c-9912a0fb0412 | -7.44713 | -46.91851 | 2026-08-24 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0b4bfede-2aa8-3d21-9d0d-52b5da2f5369 | -7.9718 | -45.25848 | 2026-08-24 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 39100fcd-866b-3780-8e6c-bbe4a11aed19 | -12.40628 | -42.89914 | 2026-08-24 04:25:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 06e1d9ec-8afa-3072-b260-e261e59c410d | -7.654 | -42.73851 | 2026-08-24 04:25:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c79f27e-9218-35b5-8120-70c35d66f92c | -11.65959 | -46.5346 | 2026-08-24 04:25:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52115df7-1423-373e-b208-495175c57a86 | -8.80292 | -48.31718 | 2026-08-24 04:25:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 826778dd-c65f-3d56-bc8d-5248856f16c9 | -10.7991 | -50.95292 | 2026-08-24 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abdaef84-55d5-3cbf-a0f0-31a50a605dac | -10.43126 | -50.46807 | 2026-08-24 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eda11cff-d6bc-3e74-93fc-ce4369d912a8 | -8.97932 | -46.02525 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f74b4ea-c894-3b20-8b6a-98fa9eff8855 | -7.97921 | -45.25593 | 2026-08-24 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45a500b0-eab1-3996-8759-2200bd84026a | -7.19421 | -42.75612 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2b8358a3-fc50-3b1d-b25c-e76320b9c498 | -12.215 | -43.17146 | 2026-08-24 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 96257ba5-06d3-33ba-b907-91697652be26 | -7.30307 | -42.9706 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6839f391-d65f-3633-ad64-177692090803 | -7.9712 | -45.26216 | 2026-08-24 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9e322ef4-47b2-3ccd-902e-341eec0e30b9 | -8.37555 | -46.46965 | 2026-08-24 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5da859e5-2de3-3f16-a552-1ca136689e7e | -9.71546 | -46.0298 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a77fbf33-775b-3f6b-9758-521d2aa79435 | -7.17309 | -42.73841 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cf01a469-a975-3013-acc6-2b4943e39815 | -7.27285 | -45.36796 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f6f5103-df81-3893-b51d-568911a89cf8 | -7.17097 | -42.79545 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a3feaf41-a6f7-3666-8fbb-fee4d5d2a165 | -6.80214 | -42.6693 | 2026-08-24 04:25:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 374e3498-66bc-36ac-9931-1be4acb7569f | -6.34664 | -54.75254 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7921a1fc-df33-36cc-8bdc-84a1f9e286c5 | -12.22176 | -43.17257 | 2026-08-24 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 336c2f2f-391a-32ec-9127-7800a7541af0 | -7.16199 | -42.74385 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7725ed6a-4798-3fef-b353-76548f9b5abf | -8.10072 | -47.48193 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9606e8f7-7eae-3234-b2f8-03a19c485612 | -8.33736 | -47.70483 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fa8efb0-3188-391a-9dcf-e72340428eb9 | -6.2248 | -55.62252 | 2026-08-24 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a838987f-5cfe-3e59-b417-352df3e7d014 | -8.30981 | -46.89264 | 2026-08-24 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d71e0f6-fa47-363b-b0ad-e1373986b9c4 | -9.68278 | -47.89279 | 2026-08-24 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dc6496a6-34d9-3fd5-bff9-5c23d9ee4632 | -11.65266 | -50.5482 | 2026-08-24 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99b21c88-d3b7-30c1-91d7-36192458f46a | -6.62569 | -53.34744 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f573c047-d7d6-3315-9c84-58b105d1ed17 | -5.68638 | -53.74212 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
