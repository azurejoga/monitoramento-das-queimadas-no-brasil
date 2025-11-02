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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d2e1ffd-a4f6-3941-820c-81a3072e4121 | -10.97418 | -54.24622 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ab050cc-e50b-30b9-861f-dfd12bce6e16 | -13.77967 | -48.87235 | 2025-11-02 04:50:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 196b25f9-cb33-3d40-9643-be088b6f3169 | -11.57174 | -47.07916 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07f06643-56c0-3a91-b53a-d165b8cd3f34 | -7.56269 | -56.15263 | 2025-11-02 04:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71f868b9-7b88-3bc9-802a-5bf9ec110361 | -11.73564 | -59.31111 | 2025-11-02 04:50:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d2afd860-d449-3bfb-b3be-f2549a406db4 | -13.31357 | -43.46263 | 2025-11-02 04:50:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 14abb934-20c5-360b-ba28-073ae45b4c55 | -14.20588 | -47.8048 | 2025-11-02 04:50:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2fc425d8-5d09-3c4d-9570-768703e46ee3 | -9.95608 | -44.51126 | 2025-11-02 04:50:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfb15b4d-a373-3bb7-bd48-3bce87f7735d | -10.99326 | -53.99989 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58a2df77-f191-3510-9429-61d6ae81392c | -11.73645 | -59.30885 | 2025-11-02 04:50:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b738289a-0e26-38de-827b-30a879a4099b | -11.57225 | -47.0755 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11da9507-8349-3f9d-b015-fa2767f97719 | -9.96153 | -44.50673 | 2025-11-02 04:50:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28aaabdf-3b1b-3953-9107-27fd0e65e88c | -14.01915 | -43.47887 | 2025-11-02 04:50:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bc7e40b1-dcc7-3e6e-9992-4f5d00621b97 | -11.35815 | -55.13487 | 2025-11-02 04:50:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f0f4419-7b38-3c90-8ce1-db60127bd3ee | -12.23221 | -54.39395 | 2025-11-02 04:50:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb1d0d7b-968d-3223-9901-5dc7bece28d7 | -12.88863 | -54.75476 | 2025-11-02 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df0fb25d-fb46-39dd-8bab-13f329763947 | -12.87121 | -50.86695 | 2025-11-02 04:50:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f8ac629-2915-3d85-b661-64ec59335412 | -14.02453 | -43.47955 | 2025-11-02 04:50:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 313df22a-dcae-3291-9316-30415af77ce2 | -12.17206 | -53.6259 | 2025-11-02 04:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9710c2d5-c670-356e-b20c-cc949dafcbf7 | -7.59586 | -55.69376 | 2025-11-02 04:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0727f172-ea27-3aa7-8f7d-29e93b19b72c | -13.78343 | -48.87298 | 2025-11-02 04:50:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d26ece73-9311-3140-8ad9-6dbd15debb28 | -14.29987 | -43.83233 | 2025-11-02 04:50:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27d78213-8927-3f85-993a-ca501e7ed905 | -10.73638 | -46.25325 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| edb53ec9-269b-34af-acd5-b390bd99c9d0 | -10.74432 | -46.25846 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bda62c93-e4a5-3fad-94a4-a530eb5ba94e | -8.1572 | -44.48315 | 2025-11-02 04:50:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b2bd69d-66b8-327f-b1c1-a1a34c69d79f | -12.85172 | -43.77024 | 2025-11-02 04:50:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a41df2b2-0899-344e-82de-2b22174451d9 | -10.62476 | -52.18964 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae62a4b0-90df-3dc2-bc28-267aebdea741 | -14.65336 | -46.60971 | 2025-11-02 04:50:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01ba3dac-fefb-35fc-8ceb-dee39edbab51 | -10.73487 | -46.23272 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 247bee9e-1c02-3a24-9ddb-fa9069cf9af4 | -8.85574 | -49.87949 | 2025-11-02 04:50:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f4c8593-1ca7-3322-977d-4e53f1bdbd86 | -13.61267 | -48.26425 | 2025-11-02 04:50:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d56e727d-d5ce-3804-beed-eaa9778c377e | -14.2054 | -47.80827 | 2025-11-02 04:50:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fe85141-d45f-32ce-b586-113ee7a5fcab | -14.59794 | -46.65556 | 2025-11-02 04:50:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d4c823e-5228-3781-ab38-bf70bdea347e | -10.61867 | -52.18505 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64d83ade-5cbc-3177-a37e-854d05c522e4 | -7.60121 | -55.69181 | 2025-11-02 04:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06806380-62bd-3d17-9fa7-d97ca15ba9b4 | -11.7356 | -59.31358 | 2025-11-02 04:50:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 698ab230-0a16-3015-bdd4-796a1d565f56 | -12.46421 | -54.32307 | 2025-11-02 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ef0434c-3b9c-30eb-95a8-25f6a085c3c9 | -11.273 | -45.49501 | 2025-11-02 04:50:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83a62a68-3ca6-3de3-b2c4-93a992606f8b | -12.8718 | -50.88617 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 560f6e88-0421-36cb-b840-25cac1458889 | -11.56767 | -47.07859 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97f76ff6-cef7-3db2-80df-3a65a7ef62a0 | -11.12291 | -54.6381 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b09175c3-a265-361d-a137-9aaeff83cce0 | -13.77592 | -48.87173 | 2025-11-02 04:50:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62140de0-cedb-31fa-bfaf-7b3e18576c9b | -13.77217 | -48.87111 | 2025-11-02 04:50:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f69c373b-93b5-3fd0-9454-8e13c81dae59 | -13.31931 | -43.45994 | 2025-11-02 04:50:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a8e0435-d537-3ab0-936b-8e6330e4d49c | -9.13729 | -51.3019 | 2025-11-02 04:50:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b32e763e-39ee-34c7-90b9-efd07353b52c | -10.73377 | -46.24069 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d74f41b-ecc8-324b-b1f4-10657a44692b | -10.63252 | -52.1837 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07ce465f-979c-37d4-b045-0d00a9c0987c | -13.14448 | -48.4459 | 2025-11-02 04:50:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c94b1ce2-ee43-334f-97de-1a4b03ea19af | -8.60283 | -54.65684 | 2025-11-02 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 319c27c5-f555-3984-bdd8-1b3c70cb3dde | -14.65773 | -46.61044 | 2025-11-02 04:50:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92278950-806a-3e3f-a166-9e82961390d0 | -12.23321 | -60.32451 | 2025-11-02 04:50:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e2d86e9-25a2-3cf4-9ecf-a8b966fb7238 | -13.77264 | -48.86836 | 2025-11-02 04:50:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6392f8e6-7ebf-318a-9092-b059caa0c3c8 | -13.77905 | -48.87681 | 2025-11-02 04:50:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c22df5e-744d-324e-909e-a7c80823505f | -11.1194 | -54.63748 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4acdba60-b385-3409-a9bd-1eaaef66ed78 | -13.7227 | -43.63777 | 2025-11-02 04:50:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d78f15c-6d35-34a6-8bd6-7f9b3beedfdb | -11.2013 | -53.83852 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bd0f98a-6c67-390f-a98f-925b0d98797b | -13.31397 | -43.45924 | 2025-11-02 04:50:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3df3dedb-9592-35cb-8ca2-8dd5d9b71ad1 | -10.73103 | -46.2606 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbd24a60-612a-3084-93d6-01d3c036cbe6 | -13.72676 | -51.45734 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 421ea717-582c-3a18-907b-ed7f53093aa5 | -14.20992 | -47.80531 | 2025-11-02 04:50:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c9b2815-01eb-339b-ad5e-a3c844e43697 | -10.62864 | -52.18667 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f9f3321-c59c-3c18-a0c0-23b520e66751 | -13.76433 | -46.89015 | 2025-11-02 04:50:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a835ea6-23d7-32fe-a8b5-8e81970554bc | -12.46483 | -54.31929 | 2025-11-02 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8e6c3f6-044c-31ed-a6bd-1bd9262580a4 | -11.20434 | -53.82002 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6aa46ae-22b1-3c55-9e9a-b9b4e0025a06 | -12.18523 | -47.06804 | 2025-11-02 04:50:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2229d920-3680-3d61-9f69-5f7ada2a3e86 | -12.87749 | -50.8947 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| efa65f50-a8b5-337f-9e1e-cbf2366b5f17 | -11.73017 | -59.31501 | 2025-11-02 04:50:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eece2f64-638b-36d5-80d6-b77e5625fea2 | -13.02374 | -44.10365 | 2025-11-02 04:50:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2ceb380-4019-3664-b8ab-074dbca7a30f | -9.13674 | -51.3054 | 2025-11-02 04:50:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 515fd89d-32a2-3e65-b5b5-7c6cd6035414 | -10.73432 | -46.23671 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcc97f43-3845-3398-8a6c-1c0586e77aeb | -12.87521 | -50.8867 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93cd9ff1-411d-35e1-bff5-8c26b2382d1e | -10.50737 | -51.87943 | 2025-11-02 04:50:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63df0ab2-79e7-3b22-a711-ecc258ae7488 | -11.60064 | -48.64297 | 2025-11-02 04:50:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28288ace-1826-35b6-a8ce-3047eb9cddcd | -11.57632 | -47.0761 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d6e9bf6-b142-3806-8990-d1076b77047b | -6.54302 | -55.04721 | 2025-11-02 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcdafda4-69fa-33d6-bcd6-5b5546d79e55 | -10.73542 | -46.22872 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eddc5994-3812-3b94-9c3a-440284b79e43 | -7.53072 | -47.29274 | 2025-11-02 04:50:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 282ca071-cafe-35f8-9a7b-8e784ad2c018 | -9.14007 | -51.30593 | 2025-11-02 04:50:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc479c72-f9b7-3845-995b-1d8a80eaf899 | -11.1661 | -53.88215 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d786eac-26c0-3d3f-bafc-89ee8d6a0791 | -11.72728 | -59.30722 | 2025-11-02 04:50:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c03aa27-d958-390a-beab-2ec27d8dbb62 | -11.27752 | -45.4956 | 2025-11-02 04:50:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc7fd3bd-1e15-3303-a56e-e04c0ec8d67a | -9.3083 | -41.06978 | 2025-11-02 04:50:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f83d9ee9-2fba-31ed-ad4c-9b00cf1bbe25 | -9.95769 | -44.50785 | 2025-11-02 04:50:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1decf32e-9dda-3f02-abea-cbbfa8d031e4 | -11.97864 | -58.06438 | 2025-11-02 04:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9d96af0a-eaee-3e98-bfb0-e1105c387e46 | -14.45527 | -51.52873 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 77ac57dd-fa1d-3612-9e66-fef45c8e9061 | -15.32747 | -43.89149 | 2025-11-02 04:53:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9af2015-cd2d-3b51-b326-a90ccd92bff6 | -15.62281 | -58.22538 | 2025-11-02 04:53:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7b92c2ad-2f64-3077-8b5c-1e503f9892ae | -12.37865 | -63.88393 | 2025-11-02 04:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55fbebab-e9bd-37fc-94df-119f9e954033 | -14.45066 | -51.53264 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 34f13814-19f9-3b86-a0d7-7dead4a72105 | -13.49426 | -61.44683 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3629e61-3ee8-3959-bb12-d85a3f74671b | -13.49999 | -56.56803 | 2025-11-02 04:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e46612ed-26b0-350d-8c23-841fa8450575 | -15.24644 | -51.75502 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f40f66f-86a4-3d8c-a5d3-617db25ff767 | -13.49094 | -61.45196 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efdda852-2938-3a9c-bed7-3ad4e4f5c43d | -18.52535 | -45.3515 | 2025-11-02 04:53:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b02bda48-625f-3d3a-9876-13f94785a06d | -15.97425 | -48.07026 | 2025-11-02 04:53:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d273f7fc-8230-3592-9227-34f0213cff94 | -18.49741 | -46.95968 | 2025-11-02 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6134359-6ac4-3443-bc36-dc57815c32a9 | -18.49347 | -46.95434 | 2025-11-02 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a67c4a4-7399-3cad-8123-f599dd98361f | -14.45471 | -51.53243 | 2025-11-02 04:53:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8aad90e0-c128-3b6b-b18a-8e22947445d7 | -18.5193 | -53.49532 | 2025-11-02 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93f64073-08bb-3127-8b87-fc5ac0c4da61 | -13.49365 | -61.44991 | 2025-11-02 04:53:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README22.md)
