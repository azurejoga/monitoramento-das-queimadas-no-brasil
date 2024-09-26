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
| 58313418-107e-3fd5-95dc-ac5f3df81d6b | -9.1219 | -61.3143 | 2024-09-26 00:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 52b28d8e-a69c-3176-a770-79411c376185 | -9.4353 | -51.4829 | 2024-09-26 00:26:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| c286803a-56c4-3b2e-aed3-9bd43a2f51fe | -9.5827 | -50.1584 | 2024-09-26 00:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 3af3aa6c-b095-3645-8834-b60798fe8fb3 | -9.6015 | -50.1566 | 2024-09-26 00:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 166.7 |
| 70dc537e-dfa7-303a-84be-87c72f88832e | -9.6018 | -50.1352 | 2024-09-26 00:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| da518ced-7823-3641-afc9-9cafb5a8d337 | -9.6946 | -57.1989 | 2024-09-26 00:26:02 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 613958bd-cc2b-3e8a-a22d-ae89cc8cad13 | -9.806 | -53.5664 | 2024-09-26 00:26:02 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 6365c661-79dd-36c8-b705-db2684f152fe | -9.8083 | -68.8152 | 2024-09-26 00:26:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e18c9bfb-4be0-339d-b566-761935d77250 | -10.0506 | -68.5875 | 2024-09-26 00:26:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 531b9557-cd05-3358-9157-58a2faf2dc2d | -10.0692 | -68.5871 | 2024-09-26 00:26:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 49.1 |
| bcf73df9-b009-35e5-a79f-de10b5e67ab1 | -10.3713 | -58.9056 | 2024-09-26 00:26:05 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| c9cde08d-d490-30c9-a12a-fa0456181fc8 | -10.3715 | -58.886 | 2024-09-26 00:26:05 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 95962e6c-1228-3faa-914e-fc09b6dc98bb | -10.3882 | -67.8737 | 2024-09-26 00:26:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 2ce6cbab-fccc-3bbe-99df-c7639eb2ce9d | -10.9924 | -44.4383 | 2024-09-26 00:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 885fed4b-a935-3761-8032-6d3a07514556 | -10.9928 | -44.415 | 2024-09-26 00:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| fa70f85f-76af-3852-b4cd-44e2e8a77402 | -10.9264 | -54.2692 | 2024-09-26 00:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 2122b0c4-732d-3e75-a06f-e845ba69ef02 | -11.1845 | -54.7769 | 2024-09-26 00:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1597e97a-0e6c-3d95-bf0c-3f07b764fa29 | -11.1847 | -54.7565 | 2024-09-26 00:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 73495733-7720-3c03-9c7a-48ef631cca7f | -11.2034 | -54.7752 | 2024-09-26 00:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| b9aebc7d-7958-3392-afc1-2c55ffcf8945 | -11.2036 | -54.7548 | 2024-09-26 00:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| bcb06780-b3eb-37d4-9e02-dc482e54633c | -11.2599 | -65.299 | 2024-09-26 00:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 71c24aa5-efcd-38a2-8518-ff67c0e05e36 | -11.26 | -65.2801 | 2024-09-26 00:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 271b2f66-d701-3d0b-a63b-6f7fd4da2886 | -11.2786 | -65.2982 | 2024-09-26 00:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 85c980d4-80fd-326b-8432-ccfd787d458c | -11.2788 | -65.2793 | 2024-09-26 00:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d0a9fc3d-5d43-3877-9fef-80ec9b89a446 | -12.2175 | -45.5074 | 2024-09-26 00:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c067b683-d370-393c-bc38-06f083f5d14d | -12.2367 | -45.5045 | 2024-09-26 00:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| fdb5a8f3-6a8e-3715-8d62-f21f0c281ef5 | -12.2371 | -45.4815 | 2024-09-26 00:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f67caca5-79b2-3bab-b9ea-825a34a8448e | -12.5085 | -53.498 | 2024-09-26 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 43e1f616-8e2e-3dad-996b-1d4395a6cd77 | -12.5088 | -53.4772 | 2024-09-26 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a76ccb5c-a6fd-3dee-89a3-98a555759ecb | -12.5273 | -53.5168 | 2024-09-26 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 126fb088-bab1-3052-b528-b571c93dcf99 | -12.5276 | -53.496 | 2024-09-26 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 192.4 |
| 2bbe4c28-5e4b-3dda-9f58-ac73927756f1 | -12.7881 | -51.366 | 2024-09-26 00:26:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 93c2632b-571c-3213-806c-31e5510b08f5 | -12.7884 | -51.3446 | 2024-09-26 00:26:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1e77efe0-3435-377f-9f3c-bee9080bc786 | -12.8072 | -51.3637 | 2024-09-26 00:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| d0551018-d35a-396a-a94f-99c54134492a | -12.8822 | -51.461 | 2024-09-26 00:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| fe8418b0-c505-3900-9269-16210c88538e | -12.8219 | -62.7271 | 2024-09-26 00:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 38.1 |
| a726b8de-23ee-3e62-a056-48c62c160933 | -12.822 | -62.7078 | 2024-09-26 00:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 74cf1cb1-f55b-3d9b-9cf0-e278511db099 | -12.8222 | -62.6886 | 2024-09-26 00:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 9356ec81-57b1-33a1-b254-bbe5656cb006 | -12.841 | -62.7067 | 2024-09-26 00:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 117.1 |
| d9ae1e0d-fb5c-3243-a040-1bb889d5d49b | -12.8411 | -62.6874 | 2024-09-26 00:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| cb990328-fd4a-34df-8f85-3c3c6e42c037 | -13.1963 | -45.6308 | 2024-09-26 00:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 8cb2c372-1061-3088-8a23-e6626afd3074 | -13.0295 | -57.2985 | 2024-09-26 00:26:20 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 53e6359a-0ab7-331c-91d3-5d9e009d5eb8 | -13.7509 | -51.0951 | 2024-09-26 00:26:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| ecb3a52c-4392-30c1-98ad-f0548dbb89ad | -13.7513 | -51.0736 | 2024-09-26 00:26:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| b45d4238-6bc1-3dc3-bc97-ebba2f18c72a | -14.6728 | -45.4701 | 2024-09-26 00:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 680ccacc-0ea8-307e-abae-ea3537f13878 | -16.9925 | -57.9288 | 2024-09-26 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.8 |
| 646cc7eb-f855-3b18-9015-0ab215e97f34 | -16.9928 | -57.9084 | 2024-09-26 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 15949677-9cf3-308e-a0de-3572c9dd278d | -16.9729 | -57.931 | 2024-09-26 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 151.9 |
| 043bfbaa-0baf-3e2a-a1a0-5f31cb27987b | -16.9732 | -57.9106 | 2024-09-26 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| fbb24756-2ca2-34ec-9f58-5eb4d1b98c7d | -17.5737 | -40.23 | 2024-09-26 00:26:43 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 56.4 |
| 1450fe39-0fe4-3dbe-942b-15d5805c805a | -17.5744 | -40.204 | 2024-09-26 00:26:43 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 212.8 |
| 40088668-567c-399a-9479-c6bfef5de232 | -17.5947 | -40.1985 | 2024-09-26 00:26:43 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 111.9 |
| e2bbd459-d2fe-3383-834c-886f1f14601c | -19.929 | -43.7959 | 2024-09-26 00:26:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.5 |
| 4f3ce0a7-e6e5-3909-8c75-2a69b37fc498 | -19.9298 | -43.7711 | 2024-09-26 00:26:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| 3fa61608-40bd-35d1-ab5d-c0d38964efc5 | -19.9546 | -44.9598 | 2024-09-26 00:26:56 | GOES-16 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 177f81cf-d989-3d19-aa45-27246d684aaa | -20.03 | -43.1747 | 2024-09-26 00:26:56 | GOES-16 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.7 |
| da5b6bf4-8a58-3c44-a5da-0a2c4bbc39bb | -20.3999 | -41.8602 | 2024-09-26 00:26:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.8 |
| 84a22da9-2c82-3815-a88b-3fd8fc46b28f | -20.4197 | -41.8798 | 2024-09-26 00:26:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 119.8 |
| fe467860-4f66-3570-90fd-98756cd3e08e | -20.4206 | -41.8541 | 2024-09-26 00:26:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.6 |
| 48851f8e-7a6f-3c14-8a7a-8650eca3824d | -20.4404 | -41.8737 | 2024-09-26 00:26:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.1 |
| 02cc734a-09ff-3d62-a233-679101bbb615 | -20.5876 | -51.5026 | 2024-09-26 00:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 23e5eb8b-c3d0-32eb-9eaa-210b1fcbca7d | -20.5881 | -51.4802 | 2024-09-26 00:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 180.0 |
| 20479ae2-7eb2-3d6d-978b-71bdc44451bb | -20.608 | -51.4986 | 2024-09-26 00:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 166.6 |
| 975b0693-7fb7-3b83-897a-9411be044dae | -20.6086 | -51.4762 | 2024-09-26 00:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 201.6 |
| 5dd86a54-d7db-3abf-a1b8-5f7eed61ccc3 | -1.0553 | -53.3553 | 2024-09-26 00:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 2466b325-300c-31f5-9cef-a019e90274b0 | -2.6601 | -57.5507 | 2024-09-26 00:35:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 45666289-13b8-30a7-98d6-c85182b13bce | -2.6602 | -57.5313 | 2024-09-26 00:35:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| ced8875e-0659-3361-8fd8-0917aed14449 | -2.6784 | -57.5504 | 2024-09-26 00:35:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 706998a2-2793-3fef-acad-f29aa0c420fa | -2.6785 | -57.531 | 2024-09-26 00:35:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 8ad58fab-de23-3254-8577-bb380448329e | -2.6968 | -57.5307 | 2024-09-26 00:35:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 612800d4-3280-3e26-a6c7-6674e1b50529 | -3.3158 | -53.2122 | 2024-09-26 00:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 8a40019c-d56b-3681-9e11-01b41e416b94 | -3.3342 | -53.2117 | 2024-09-26 00:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| d94d57ae-e448-37a9-9172-ba852cb40870 | -3.3505 | -53.7775 | 2024-09-26 00:35:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a884d4d8-5122-3581-b517-bbfaccc0d3f8 | -3.5673 | -50.3794 | 2024-09-26 00:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| ab318583-9caa-354c-b474-cbc3948bbdfc | -3.7821 | -41.5999 | 2024-09-26 00:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 44.4 |
| c3309ebe-4734-387e-8539-2b69842439fe | -3.8008 | -41.5989 | 2024-09-26 00:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| d21648f4-235a-355a-ad5a-2ca00a07b629 | -3.801 | -41.575 | 2024-09-26 00:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 4b5310b6-c3fa-3482-b492-eede340e2aa9 | -3.9208 | -46.4459 | 2024-09-26 00:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.8 |
| a9e7f67d-8901-3c36-8748-68f442eebd94 | -4.0656 | -44.048 | 2024-09-26 00:35:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 44fb0557-abe0-3643-b3e2-c18f553d1fda | -5.212 | -47.9577 | 2024-09-26 00:35:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 7ec44ff9-6b09-3384-99f7-33b9bfb98fbe | -5.2306 | -47.9566 | 2024-09-26 00:35:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| aef03807-4d93-366d-8ef4-249eb94f497f | -5.943 | -52.1241 | 2024-09-26 00:35:40 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ee14527d-230d-3a35-81a4-2fd4b878a9cb | -6.5772 | -60.0437 | 2024-09-26 00:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 23b691f8-fa96-3de3-a078-5546c386a140 | -6.7902 | -44.7296 | 2024-09-26 00:35:44 | GOES-16 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5ec874e9-c1b8-32bd-ad32-f84e7ce855ff | -6.7839 | -59.3245 | 2024-09-26 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| eb3d9699-4df2-32db-b5b4-2ae3971fc531 | -6.784 | -59.3052 | 2024-09-26 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.2 |
| d35df026-d5b0-3ebb-a39b-eca82163e21b | -6.8023 | -59.3237 | 2024-09-26 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| afd7ea34-2f40-3b7a-a053-689c63715d9b | -6.8024 | -59.3044 | 2024-09-26 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 2131e2ec-328b-3b81-9316-efec80c125a1 | -6.8384 | -63.1457 | 2024-09-26 00:35:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| a507f719-1195-3e64-9894-6b8afecabb80 | -6.8385 | -63.1269 | 2024-09-26 00:35:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 3427d6cb-2181-333a-8e87-156723e5f082 | -6.9305 | -63.1241 | 2024-09-26 00:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 109bed7a-23eb-34d8-840e-9606a68b461a | -6.9306 | -63.1053 | 2024-09-26 00:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 81a54061-2bc9-368c-b7bc-fdc941d5f3b0 | -6.949 | -63.1048 | 2024-09-26 00:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 01b1f94b-74d7-3d59-b97f-5d0e2495bc93 | -7.0912 | -46.4412 | 2024-09-26 00:35:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| add96a61-fd59-3e16-acb7-7d2e9355d1f1 | -7.2905 | -61.106 | 2024-09-26 00:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| c0e5aab2-deb0-390e-8d8d-3245f7672725 | -7.2906 | -61.0869 | 2024-09-26 00:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 796d3659-b2cc-307e-b055-59e91e119c7c | -7.3637 | -55.5134 | 2024-09-26 00:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 3aa5346b-a98e-355d-b4aa-fab491d4601e | -7.3639 | -55.4935 | 2024-09-26 00:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b21d0c78-d3a1-3293-9b14-38ecb06a5502 | -7.3824 | -55.4924 | 2024-09-26 00:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 0836804b-4ce2-34ee-a035-d4ec22a0ca54 | -7.5705 | -55.1617 | 2024-09-26 00:35:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |


[Clique aqui para ver as próximas entradas](README8.md)
