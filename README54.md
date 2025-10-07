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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8ba1bb7-1c45-35a9-b378-0e4d1ac342d9 | -7.01102 | -42.29243 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a806bf18-e2d6-3282-b199-04ce1cf85f54 | -8.46621 | -49.2231 | 2025-10-07 04:36:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ca5fe32-0713-3f2e-88d8-90c81abfc5ca | -9.846 | -51.37748 | 2025-10-07 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e131899d-7d2c-31d8-9981-17c5a8f509ea | -8.52855 | -46.25339 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec951fd8-787b-3948-becf-74bc8220e94a | -8.61325 | -44.92822 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b47c275f-8b10-3eea-b857-da043b169c26 | -6.98038 | -42.87393 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 41990fb9-4fce-3974-a9e1-19d1292bfc93 | -4.11197 | -50.0516 | 2025-10-07 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ae37ea8f-96a3-3a13-9026-b8f6a2610361 | -9.27918 | -48.32149 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c4f4f19-c3eb-321e-98fb-246ee2256a23 | -6.22995 | -44.21476 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8efcc263-7244-3858-94e8-a9e95a522a07 | -10.18151 | -45.53842 | 2025-10-07 04:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94fc850d-f67f-3672-885f-35dff4fe1f40 | -6.729 | -42.16671 | 2025-10-07 04:36:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ddc0c1f-4bff-3737-bb82-5fcbd430907d | -9.04007 | -50.59571 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ea3f979-4748-31be-9590-f55d9dbe8aa5 | -9.03724 | -50.59134 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c93653c4-b3da-37af-8546-e54cc3dde523 | -6.45548 | -44.58583 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9fe03e48-e063-3ecc-851c-fc3f8b140672 | -8.60811 | -44.92049 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78ace63d-1acd-3c59-8aa6-50802c7fe9ad | -6.15989 | -42.59235 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| abd7b7cf-a6dd-38e2-bca8-c2a23822638b | -3.46901 | -53.45746 | 2025-10-07 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85af3e21-2acd-3f91-a239-1a3f6adc656f | -10.03052 | -48.29377 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cad0f844-1e0f-37a2-8ee1-97ccb66759ff | -8.44169 | -47.20951 | 2025-10-07 04:36:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c85d461c-38f2-351b-aa98-96c22be4f344 | -9.69932 | -45.93086 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 596724e3-683a-3d6e-8d4e-d16dc90b9ce0 | -5.9573 | -44.33794 | 2025-10-07 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef695df8-8049-3e60-8b29-be100a1092bb | -8.58037 | -44.33773 | 2025-10-07 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95e17705-a1e6-3f6b-8d30-f24012afd841 | -7.02403 | -42.79875 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9fb8ff18-d565-324a-891b-4b15982f3535 | -8.34118 | -49.65723 | 2025-10-07 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6a25c96-2302-34d6-b533-13e894b056ec | -8.86289 | -46.78725 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9c9e0d2-a4b6-3c4b-a146-a0a63e01c6c0 | -6.62862 | -56.28067 | 2025-10-07 04:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a10d84e8-4b46-3879-93a3-c36fd2d3671e | -9.00612 | -49.20856 | 2025-10-07 04:36:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80557dc3-e829-3451-ae8d-0e89c7a90d5d | -6.56791 | -44.14552 | 2025-10-07 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b00caf47-0ecd-3caf-9908-8f3605f47788 | -8.20474 | -44.18862 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc2f23d7-286a-33ae-823f-937f4c463fa3 | -8.61758 | -44.92442 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1ff6103-d45d-38bc-a4e7-67db15672541 | -8.62116 | -54.95857 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21d60519-6668-3ba9-84e4-130884022cda | -7.75685 | -49.85521 | 2025-10-07 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee07d2a3-e65b-3cd3-8cd8-be9a742a45e4 | -7.89094 | -47.8112 | 2025-10-07 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78dbdc28-8786-3cc6-abfc-6c391bb934ca | -9.00499 | -49.21562 | 2025-10-07 04:36:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38fb0068-4281-3b5f-ba37-6e73a07f49d6 | -5.50164 | -43.07072 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 97945329-2cf7-3cae-a6d0-6602957fce04 | -10.23567 | -48.19224 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a49c9721-8fe8-3d98-a948-5ddc78cd67af | -7.46567 | -42.62875 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7b1770cb-ac9b-3d1f-a625-9a6c50fad695 | -10.38672 | -45.40474 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a2a8618-8f5e-32c7-b5be-53aabcb5f42e | -8.17002 | -43.36442 | 2025-10-07 04:36:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2b597e7c-89a0-3d06-b09b-78770441fcbd | -6.33928 | -44.02725 | 2025-10-07 04:36:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cce97e3-d454-30bd-ad1c-c6519e0474ea | -4.57307 | -55.95916 | 2025-10-07 04:36:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e253eb5-f78e-3d8d-8f44-8fdcd8d13ba2 | -9.19106 | -47.84331 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2790b160-968f-38ec-8eed-53f7608f94c1 | -4.31941 | -46.80822 | 2025-10-07 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24a00737-193c-33bc-a2bd-02f22d8be93c | -8.15116 | -49.49363 | 2025-10-07 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0db404c2-e634-3724-9971-a37ec00b2bff | -8.64366 | -44.90085 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d3a941e-8cc5-390f-8eb9-50492c2289ba | -8.34794 | -49.65833 | 2025-10-07 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2adb265b-2031-3068-8073-99dedd2a31c7 | -6.6991 | -46.02977 | 2025-10-07 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 688de704-0aba-312c-b727-f12f5f075a83 | -8.5887 | -44.33414 | 2025-10-07 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4c74fca-da58-34d1-96c1-e09b3f191064 | -9.96683 | -43.78641 | 2025-10-07 04:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| caf06149-8185-3449-9b02-35c82b08d4d0 | -5.77417 | -45.74218 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eab4a98c-b345-34a1-96d8-36b6da1767e9 | -5.25196 | -46.56446 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e69a2207-ee30-3451-b18f-94cc9565e62d | -7.52504 | -49.90461 | 2025-10-07 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 816105a1-b8a7-3ac3-97af-175dfaf0934c | -7.29344 | -41.97964 | 2025-10-07 04:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f652a3ba-dbbd-3fb9-9104-b376a1de8849 | -8.48709 | -46.30659 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f890ce77-e46a-337a-9a54-1bd75dfda666 | -5.5009 | -43.07568 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 92f6038b-11e7-3deb-a0d5-b57a587b5868 | -8.62037 | -54.96299 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aa6971f-235e-3a79-a0dd-14b87d7f2f22 | -3.46994 | -53.45506 | 2025-10-07 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64842c88-efca-3e92-854f-269e50af4622 | -5.30244 | -44.55602 | 2025-10-07 04:36:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4fb5fc1-a19f-3ce1-a9dd-b61ba9f232e5 | -8.66448 | -46.28172 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9bfc98e4-7faa-3936-a374-7e5f3800bf13 | -5.59871 | -43.11256 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 179e4788-57f9-3ed0-8c35-5a64044a809e | -9.33408 | -54.5153 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a91f258b-b83d-3f79-b0bc-fc22c9e32b50 | -5.24805 | -46.56748 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dea510b3-b5cd-37c4-88a6-2d9ebc0403e0 | -8.54468 | -46.24056 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 41bb9a23-40ba-372b-a2e0-dca1f404dc90 | -8.61883 | -54.96069 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44aeee1e-1acf-3201-be60-7aaf69993f9a | -8.91111 | -50.60326 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ba412cd-1880-36e1-807a-7cafc8d267b0 | -5.64026 | -43.60696 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 760c2ce8-5f62-30a3-a3da-9952ade29038 | -7.51764 | -49.91167 | 2025-10-07 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f889c55-1acf-3ea9-8957-e8171402f97a | -9.20054 | -47.84842 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61125ed8-a4d8-3958-8fc0-38ffda2306b2 | -5.76668 | -45.74487 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2ec36c2-d983-3bfb-8a00-16f46bc0303a | -9.66812 | -48.405 | 2025-10-07 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5772a0bd-7f75-3db2-87ca-014a771fd5c7 | -6.24938 | -43.27256 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb04633f-f8c2-3586-9814-4a8671f40f47 | -5.79454 | -45.47324 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 836b7561-a68d-383b-a3ee-cd9494acb50a | -3.67664 | -55.57655 | 2025-10-07 04:36:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90e194b0-5e15-392d-bb07-64eeabc1534a | -9.6731 | -48.395 | 2025-10-07 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f636ba26-ccda-34a0-aa89-ae15906dbc4d | -4.14049 | -47.66055 | 2025-10-07 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ec48b89-4ba8-361d-a960-63e807893bf1 | -7.71027 | -42.38773 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cc6e956-23f5-3a56-be00-83558e5cf325 | -5.51348 | -41.00484 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6624e094-fcd8-314c-a9bd-95244d8ebee8 | -10.03549 | -48.28383 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b54de449-88f8-3067-85c0-c7c14488eed5 | -9.03974 | -50.70544 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29fcd552-bd1e-3240-a037-f294980c649a | -5.14799 | -49.8471 | 2025-10-07 04:36:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b347e7c-d000-3de0-b2ad-5117491e3195 | -5.41441 | -41.07548 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a90290d-f3c1-3820-ae0a-ca1994b7b913 | -9.02658 | -50.65578 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c089f441-0a6c-37b5-a1b0-3c7f9e907d9d | -9.19161 | -47.83977 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d3314da1-c1f3-3aa9-9c2f-eea530fb0ff1 | -8.17762 | -50.29919 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74709d83-d555-39ee-9938-d1ed5f07b12c | -6.45247 | -44.58103 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 29b4014b-f164-3406-8c98-be10d58937bc | -9.02368 | -50.69472 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b087441-44be-3ce0-a5b4-da873590bc01 | -5.7556 | -43.39683 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f08c7914-1ad6-3671-8f92-aba85c81ca00 | -7.98458 | -49.95917 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e13f46a7-497b-3a6a-b8cf-61f693a1c83a | -6.17517 | -51.16002 | 2025-10-07 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f4ba40d-2592-3549-afca-48e3f2e85a9c | -6.29529 | -46.09033 | 2025-10-07 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b18dbb17-1a39-3b0f-85af-5f4e9149eb4a | -6.23908 | -43.26058 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42d2d05f-328e-3b1f-ba7f-9a094d95c295 | -5.26184 | -46.47871 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a64a7d5c-d828-3c25-827e-7004ab388e35 | -5.65098 | -43.18892 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 040e5279-9558-3fcf-8b30-ffe1a6c030b4 | -8.38038 | -41.85126 | 2025-10-07 04:36:00 | NPP-375D | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4f3d093b-fd98-35ea-b61e-1130aec90c6f | -5.88951 | -49.37072 | 2025-10-07 04:36:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4023d073-fe66-3b5f-87c8-1001e122b06a | -10.36275 | -44.98365 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bad19f98-00bd-3063-bdb8-f2cb2340c1fa | -10.61356 | -44.34461 | 2025-10-07 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebc12c0d-05ca-3efc-9f86-3eb96ea51d2f | -6.15461 | -42.58099 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9790d6e1-f079-3533-ad67-a1974c9fd940 | -8.18674 | -50.30844 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95f96714-7388-36cf-be0b-6e019483aeb6 | -7.68761 | -42.40189 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README55.md)
