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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85125351-e1ed-30f0-870e-cfbe76121c79 | -2.17439 | -48.01861 | 2025-12-31 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7628fcad-c04f-3e87-89f6-11f6946d44f3 | -4.79574 | -40.78941 | 2025-12-31 04:44:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 518ebe44-db8b-3090-b9ff-fbe4831772c8 | -6.29368 | -46.99836 | 2025-12-31 04:44:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d4d759c-62f8-356e-9d13-34db22648560 | -3.34234 | -42.14819 | 2025-12-31 04:44:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fb2e59d0-44cf-3d3e-a48e-a5934ed63c86 | -4.32507 | -43.7857 | 2025-12-31 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cad9b9ee-8e3e-3d24-8963-dcfd62e9458d | -4.79618 | -40.78642 | 2025-12-31 04:44:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 289a0f34-7dad-33c8-aa23-5fc0d310272e | -5.88412 | -46.50285 | 2025-12-31 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfbea2c5-1b5a-3ddb-a528-4dfcd8514c53 | -5.70778 | -44.20509 | 2025-12-31 04:44:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4853fd49-b658-3670-a9d6-484a7b35943e | -4.98876 | -47.93231 | 2025-12-31 04:44:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e7e7aee-4d4b-3b86-8f13-693bcbb5016a | -4.86561 | -50.82541 | 2025-12-31 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10f58b7f-6f42-3089-ba91-68ed7f9e7aa9 | -5.78808 | -47.92801 | 2025-12-31 04:44:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 548a23d5-ee79-30df-9d35-fcee036a5d03 | -2.17384 | -48.02208 | 2025-12-31 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36f1ef61-b293-30db-b7b9-e7d480a42055 | -3.87298 | -40.44905 | 2025-12-31 04:44:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9a9e2df9-7f6d-3b93-9aab-3c7bee8d3c81 | -6.22452 | -43.69193 | 2025-12-31 04:44:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ceeb937-4375-3162-914e-e0e76fd1a5fa | -3.34689 | -42.14886 | 2025-12-31 04:44:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4241d0b8-6189-3a90-856a-1cb0b69954f7 | -3.55693 | -41.96671 | 2025-12-31 04:44:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9d02487-3ffb-3174-ac64-39fb8abe941f | -6.55756 | -43.60317 | 2025-12-31 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fed4c02-15e1-3974-bd4a-3e5da102bc49 | -4.07081 | -42.88297 | 2025-12-31 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 532868db-459b-3ffa-b1fb-3c427ecfef2f | -5.04936 | -47.18673 | 2025-12-31 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29ae5d12-c85d-336a-b882-aad45b44337a | -5.42726 | -44.86662 | 2025-12-31 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e42a41d-a839-31db-bd08-b5fd7f9d8a55 | -7.14499 | -45.25591 | 2025-12-31 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 169c61c1-e46c-3b4f-ad90-d993ae175d2d | -4.0887 | -47.16534 | 2025-12-31 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b577184-c82e-3a17-9626-f5a4bfe64fc3 | -5.28724 | -45.82744 | 2025-12-31 04:44:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4fd9d34-218a-3fcb-94b3-e191fad5c027 | -7.25323 | -45.48774 | 2025-12-31 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 110b3cc9-14a6-3887-857c-68f32ac79e5a | -6.55626 | -43.60346 | 2025-12-31 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f275feeb-5181-31a0-aeea-c0e24b959499 | -5.72427 | -45.04199 | 2025-12-31 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 83a0bcc2-ea8e-3587-93c9-97d05a4acd07 | -3.19926 | -45.55421 | 2025-12-31 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ca55936-af89-3e16-b87a-e19d58578d92 | -5.6205 | -37.33232 | 2025-12-31 04:44:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 40d13fd8-dd51-35c1-a584-356b4bc43326 | -2.44727 | -47.79287 | 2025-12-31 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdf340bb-c288-3240-8857-480eb8645cd6 | -6.18122 | -43.41789 | 2025-12-31 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92017a15-7d37-3f10-94fb-7d31c0279a25 | -4.30744 | -43.79064 | 2025-12-31 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb63b2a9-d876-3293-abcd-753b9235f984 | -4.63174 | -47.93914 | 2025-12-31 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fea2360-4d9e-34f4-9e0e-947dab29bb6f | -3.53576 | -43.66986 | 2025-12-31 04:44:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b782fdf-e1a4-3de7-9e63-76ed41f6b7b6 | -3.87815 | -40.44981 | 2025-12-31 04:44:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5453e88a-7c69-3ab8-9ca8-4e7c39ceaa8e | -5.98765 | -44.57319 | 2025-12-31 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17afb502-367d-3a60-9b28-1fb2b76b2e32 | -9.7123 | -48.90285 | 2025-12-31 04:44:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a235f12-1837-3272-ae9d-4b82aa59b396 | -4.07017 | -42.8872 | 2025-12-31 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39bccee9-440e-3cf1-b22e-401181cb60fe | -4.26394 | -48.83941 | 2025-12-31 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ac4c8ac-fcdf-3cb4-964c-06d06c0000a9 | -5.98363 | -44.57261 | 2025-12-31 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0dc412b-dd18-32be-810f-aa8d40ca1d18 | -4.32151 | -43.78129 | 2025-12-31 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf783328-b384-31f3-b183-fba278a085b8 | -5.05906 | -47.18464 | 2025-12-31 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 535e9133-39c6-3157-bc59-6c92c9d6ec66 | -4.31738 | -43.78064 | 2025-12-31 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba022dd2-d18b-3cce-9017-7033e8e4361b | -7.25416 | -45.49081 | 2025-12-31 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a8b19c0-9c61-3a9b-8019-f463fe5b45ba | -5.65108 | -50.16803 | 2025-12-31 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5bb8478c-ceea-36d4-8b55-f7563f99700c | -4.79106 | -40.78572 | 2025-12-31 04:44:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 511a93d3-13a9-36c1-a1c6-5223249171f8 | -4.62782 | -47.9422 | 2025-12-31 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 504fb720-8ae4-3ee5-970f-c059ad5356b6 | -5.98095 | -44.59018 | 2025-12-31 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 452412d5-ddc6-3bad-bde3-f0351ec923c5 | -4.6075 | -45.67424 | 2025-12-31 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50437c66-fd2c-374a-8dcb-e9ebc24421c5 | -3.44028 | -41.67911 | 2025-12-31 04:44:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2fd87e38-633a-36c4-9944-f8cc0c2a3f6e | -5.53094 | -46.45255 | 2025-12-31 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfeb6f16-e52d-32f8-abec-65ff541bab47 | -5.725 | -45.0371 | 2025-12-31 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 83af5a62-72a8-3034-b1ec-ef3fa789fc70 | -4.31269 | -43.78381 | 2025-12-31 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61555153-3c4d-3a6a-ac54-02ff806603a5 | -5.47618 | -44.70052 | 2025-12-31 04:44:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fe1a6e6-15e2-3cf7-9d70-288b34ac3f50 | -6.59433 | -50.06409 | 2025-12-31 04:44:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0e030f9-baae-39f9-92b3-a595bfcb6851 | -3.5339 | -43.66867 | 2025-12-31 04:44:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d65f2bd-ee8e-3947-a80d-e8775f413206 | -6.96238 | -46.21717 | 2025-12-31 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f29c181d-a6fd-3bc5-88a1-2a48b9136f24 | -5.98167 | -44.58983 | 2025-12-31 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79d7e00c-033a-3170-8d46-b464b90a88e8 | -5.53032 | -46.45662 | 2025-12-31 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d720f3d-ebfc-3b74-a01b-f862188fb636 | -6.22757 | -43.69106 | 2025-12-31 04:44:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44ff27f2-473f-3cf1-81fc-1c674f0460ad | -2.63055 | -47.29473 | 2025-12-31 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc5cedf8-5b4e-353e-890a-7673dc652c23 | -5.28658 | -45.83185 | 2025-12-31 04:44:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a0399b1-a715-332a-a8f8-de243d2d4c02 | -6.12868 | -49.32832 | 2025-12-31 04:44:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1ccfc2d-c5d6-38fc-8a72-c078bc7f23b6 | -5.45219 | -49.26732 | 2025-12-31 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ead270f2-defe-35a3-a1d9-cef3cba7a4a3 | -11.16015 | -43.32024 | 2025-12-31 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b8f95907-ff4d-3fe2-9d8b-7ee17d596e41 | -15.51888 | -43.54985 | 2025-12-31 04:46:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 795284fa-6122-3984-aa50-f94b1bb86f3b | -14.72441 | -53.97065 | 2025-12-31 04:46:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16c510d4-3b6e-3e28-a879-c89b499fc9b1 | -11.15139 | -43.31385 | 2025-12-31 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1fe3b2bc-2d82-32eb-a918-fbc408d15cf1 | -17.37786 | -42.62329 | 2025-12-31 04:46:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c70ff482-919d-317d-99b0-b60c17cbbf44 | -16.48042 | -50.9109 | 2025-12-31 04:46:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35e347a4-67f2-3515-bb06-e9f3b454f00c | -16.4313 | -42.20986 | 2025-12-31 04:46:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1086d1ed-0acd-3fa5-b5b1-6b257a03c820 | -16.00425 | -46.95613 | 2025-12-31 04:46:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fdf4043-465d-34d9-9332-309da79f056a | -14.50119 | -52.55948 | 2025-12-31 04:46:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0079788-d0ed-32af-bb9d-bd240a1cc383 | -9.92172 | -57.23131 | 2025-12-31 04:46:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adfae93d-95c1-3529-96d6-d89d49eec9db | -16.56185 | -51.30913 | 2025-12-31 04:46:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 756f9d64-d0cd-335f-9487-6b70f5d761cb | -14.72374 | -53.97465 | 2025-12-31 04:46:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6054ee84-eae1-3b19-9549-93c6e7af15c0 | -14.72092 | -53.97001 | 2025-12-31 04:46:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ab5326d-130c-3ee3-9ab8-ade699be5ac0 | -16.43675 | -42.21069 | 2025-12-31 04:46:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6734180b-1ee9-3abd-aba2-6478e3c8dadd | -16.06923 | -57.08485 | 2025-12-31 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2b87ea4e-cd5d-3b1f-ace5-eb44020d70b5 | -17.37748 | -42.62679 | 2025-12-31 04:46:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8a987f4-108b-39e8-a7a5-6bd833cc05ac | -11.15611 | -43.31451 | 2025-12-31 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 92bcf5b2-280c-3032-930e-691d0d36f81e | -11.15544 | -43.31956 | 2025-12-31 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a217465a-e516-3a26-bb8a-8d6db69424a5 | -17.3771 | -42.63028 | 2025-12-31 04:46:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d79aeffd-4eea-3e00-9f4a-8e8d6f0cdced | -11.05672 | -51.73811 | 2025-12-31 04:46:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7e7280cf-746a-3906-8e8c-ef6805257d79 | -16.31505 | -57.567 | 2025-12-31 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 59486767-da47-341b-b30b-21233d6857e8 | -16.30747 | -57.56137 | 2025-12-31 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 48fe75ec-5d8d-3d64-865b-bd990e842057 | -19.32848 | -54.02437 | 2025-12-31 04:48:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ed6acbe-1291-3776-bc49-d698830161de | -16.31162 | -57.56218 | 2025-12-31 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 77ab9c5f-2891-3fbb-9f37-1e9f84fbcfa4 | -16.59885 | -58.21159 | 2025-12-31 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5042aec3-49c8-3148-bad3-c36280526527 | -18.19645 | -54.49513 | 2025-12-31 04:48:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25a659d8-6a3c-3b82-90d4-6ae2116a4ba0 | -16.30673 | -57.56541 | 2025-12-31 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ec66b29d-6a30-3887-8960-e3adc8b9c6ac | -20.32838 | -55.92373 | 2025-12-31 04:48:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 656288d4-9c7f-39a5-ac25-8e7e59651bfc | -20.32762 | -55.92804 | 2025-12-31 04:48:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 52e839f4-d07b-3ecc-8b1c-a2bab8c28e14 | -19.32447 | -54.02756 | 2025-12-31 04:48:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 086f1638-f6f3-3709-b249-e424a712e1d2 | -20.32123 | -55.92231 | 2025-12-31 04:48:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9dfd76f8-eac8-3a97-ae2c-334c2e282af4 | -19.49457 | -53.95181 | 2025-12-31 04:48:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19c97fdd-d3d6-32fc-b8e8-827a7d0d0c73 | -16.59455 | -58.21071 | 2025-12-31 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 518c5e59-5d61-3095-9d5b-15dff2662071 | -20.32481 | -55.92302 | 2025-12-31 04:48:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 76eac5e1-90a8-3751-be1f-9fa173b17c9a | -19.32786 | -54.02816 | 2025-12-31 04:48:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b52a4164-8c3f-3d86-a655-5cdfcd1d5f74 | -33.7149 | -53.374 | 2025-12-31 04:53:00 | NPP-375D | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 5ad985f7-e1cf-3ed3-8006-a294bd733f41 | -33.722 | -53.37535 | 2025-12-31 04:53:00 | NPP-375D | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |


[Clique aqui para ver as próximas entradas](README8.md)
