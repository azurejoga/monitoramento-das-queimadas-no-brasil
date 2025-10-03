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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 823505dc-1fd7-3161-9c52-25f277df9625 | -10.97046 | -51.07597 | 2025-10-03 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4c146f77-5785-38fd-b182-06a7b7b8a17c | -9.28228 | -60.53564 | 2025-10-03 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 900b4852-aac8-3426-bbae-4e817847184c | -10.59626 | -48.7095 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1efae959-d960-328d-86a6-01241141aba0 | -10.66304 | -48.48309 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3094107d-3f2b-3a3b-bf89-ec714ccdfb53 | -10.00253 | -50.21963 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bf0ab78b-87dd-3b52-a4f7-e97add667f9c | -10.00669 | -50.2486 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cfeb69a-1958-3c2d-82f5-496f30a0f79b | -12.75306 | -50.5573 | 2025-10-03 05:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f5049da-bf16-3194-b33e-bab3574877e4 | -10.00508 | -50.21069 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6404fa3-dda9-3a06-9905-dcbd4daf4265 | -2.24725 | -47.8788 | 2025-10-03 05:23:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9267a7ec-0080-352d-bf27-7b4d0fc6aaff | -11.91442 | -54.83352 | 2025-10-03 05:23:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92b4117d-ba01-3b8d-98b5-e764a459277a | -1.91902 | -56.6401 | 2025-10-03 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cbed5cd-0d1f-35fb-b9e6-0b97e2465de1 | -3.04899 | -51.10229 | 2025-10-03 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfefb430-8e17-360c-be4c-428b532ff91b | -13.34192 | -48.126 | 2025-10-03 05:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| edd09ed9-c613-30d7-ab69-7e8e66079628 | -9.99295 | -50.24655 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b04805e-5c89-3947-b613-50c28f9cbe90 | -1.07649 | -53.679 | 2025-10-03 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0bc3eb20-9de1-3182-9a01-58497686f09d | -10.59902 | -48.71419 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41cbfe6d-9706-36b9-9a76-7947c43aaf58 | -10.01555 | -50.22628 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef5022a2-1084-3517-a2ba-8f9804d7e65e | -12.72104 | -48.583 | 2025-10-03 05:23:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d59ebb44-c8ae-3856-87c9-88c93f78be5e | -12.9311 | -48.44458 | 2025-10-03 05:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb8bcca7-e806-3f91-950d-b6334e10300e | -1.08555 | -53.67619 | 2025-10-03 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1f92a978-4f00-3083-ab4e-9a61f5ee9109 | -5.48601 | -52.13578 | 2025-10-03 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8caf91dd-623b-3cf6-b0d5-0c545927d10c | -9.98682 | -57.82204 | 2025-10-03 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c8c5544-2907-3160-8cbd-4a4e405e1d4c | -9.99789 | -50.21914 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 07d3f101-810d-38e0-b3a5-60ab86d770bb | -2.93293 | -54.17861 | 2025-10-03 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f258947d-0b3b-3065-89ee-a9f9ea788f4d | -9.87851 | -47.80845 | 2025-10-03 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 67261049-f3f7-3b94-b09e-19a34922f261 | -9.45654 | -56.65173 | 2025-10-03 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4cc80b7-a408-3355-9b0d-3715cfc4cdc2 | -10.58895 | -48.71394 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 51cefc07-9777-3a07-95ec-5d24fde6f627 | -13.33546 | -48.11837 | 2025-10-03 05:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 956edeed-281d-3d95-8865-6c19da24d991 | -10.0086 | -50.22044 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6d3c1350-ff14-3c71-9041-49f3d3859a3f | -11.12429 | -47.8648 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6a209667-8b83-3ecb-b8d3-0f8972a7a78d | -10.01059 | -50.21617 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 380a1b43-773d-3a08-b4d8-62585dfc4aca | -7.25631 | -48.481 | 2025-10-03 05:23:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 580d8690-2c38-3b30-99c1-0b24477027d9 | -11.10307 | -47.82212 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cfdac423-d3b7-3764-b1cf-116a0d1423ef | -13.33475 | -48.12537 | 2025-10-03 05:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 667218ae-8374-34c8-8941-113828170650 | -10.00063 | -50.24777 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aab36985-6b28-332d-86ba-b24bd0ca3376 | -10.00919 | -50.21581 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fa43f9da-f729-33c0-82b0-13a658699b65 | -9.45588 | -56.6551 | 2025-10-03 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e27bc47-0a7f-31b2-9f48-4aaded7375dd | -10.593 | -48.7076 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2829d043-3ddb-33d9-b2b4-c1b8d6683a7f | -12.9399 | -48.43858 | 2025-10-03 05:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb186b80-8772-32af-ab89-133882b9aed6 | -9.63766 | -63.20047 | 2025-10-03 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdd6a623-1c77-3a28-a61e-481293ec220d | -11.09888 | -47.83367 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9646dba8-88f6-3a58-a414-d8c377c74446 | -5.83971 | -53.67474 | 2025-10-03 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d294607e-6984-319e-be18-a5448eae5428 | -11.11884 | -47.87301 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9f50a741-31b9-31a1-8e0d-a63d26c62854 | -2.8725 | -54.85356 | 2025-10-03 05:23:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 794c62dc-f4f4-306b-8be9-4e5387eff307 | -7.26282 | -48.48094 | 2025-10-03 05:23:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c31f98d-2bdf-38e4-953d-843610282633 | -10.48116 | -55.62765 | 2025-10-03 05:23:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9a915eb-5d38-3e9e-8e98-078a3192a46d | -10.89515 | -56.19423 | 2025-10-03 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 964e1836-640f-3c64-87f3-d1fec56dc3b2 | -11.08358 | -54.78339 | 2025-10-03 05:23:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4323210a-1e8b-3ff4-9452-3467ec59cae2 | -3.31035 | -53.85506 | 2025-10-03 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4e82f38-232d-31d5-a9d3-fed66bdeb73c | -12.71484 | -48.57592 | 2025-10-03 05:23:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0225b201-4328-37db-89d8-f1d6e560bb2b | -10.00683 | -50.23434 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 4dc13c4d-5cb3-3845-80d5-506744139177 | -3.56039 | -51.12833 | 2025-10-03 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2fab689-c3bc-3c2c-8a39-1b295045166a | -7.93954 | -61.50693 | 2025-10-03 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9924a2e6-e61f-31b9-923f-0f0e3db8a56e | -10.28755 | -50.30497 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59476f4c-2fca-37b8-ad18-79bfc3a5a4f5 | -3.93362 | -47.56889 | 2025-10-03 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a2a1a6cd-6ffa-3b79-9757-c2d84d6a2be7 | -11.11957 | -47.86672 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f145be6a-4813-3ca2-be48-aa4e225e0c16 | -10.89977 | -56.19127 | 2025-10-03 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71cbfe8e-14a0-314b-99ff-29dfc9e74bd1 | -11.10392 | -47.81465 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0c88e6b-7c54-3c78-8f88-2c15c34806e0 | -3.89738 | -54.12576 | 2025-10-03 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ad99664-22f8-3713-9355-93b554340299 | -10.6118 | -48.72115 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93758c71-014d-3834-8890-bd48f18eb91d | -4.56016 | -55.95933 | 2025-10-03 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4999bdd1-61f1-3672-ba70-d13418923084 | -11.62339 | -47.99511 | 2025-10-03 05:23:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9819c9a-8a28-314c-889e-1a977abfd648 | -12.71513 | -48.5729 | 2025-10-03 05:23:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d1ddd2b3-4409-3741-9dc4-277ced12087e | -10.21802 | -53.87136 | 2025-10-03 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c894a580-9217-3242-bdba-3b2a3ac11d95 | -10.58293 | -48.70698 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 780fec3a-17bb-37e1-b3d4-8f361a942fdb | -5.0004 | -56.0667 | 2025-10-03 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24b48aaa-f994-3931-835b-5bdcd8b1b190 | -3.09268 | -47.0184 | 2025-10-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| ffe75ae8-8403-30ab-8ab4-6631e29a437d | -5.61629 | -51.93378 | 2025-10-03 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a4cd2ec-96b1-3254-b300-175122379c7c | -12.93401 | -48.42745 | 2025-10-03 05:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a8ebad7f-4502-3796-b866-22de6f83d2d0 | -10.97478 | -51.08932 | 2025-10-03 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b2748790-a6c3-3ca1-a85f-79063f48c47f | -10.70422 | -59.1916 | 2025-10-03 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6028dc24-ae03-3c2f-a6dc-f70595bb063d | -10.00452 | -50.21534 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 614ccc5b-50ef-3a16-b18a-68b9d5994b9e | -1.14815 | -54.18819 | 2025-10-03 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8a8b387-20ec-3733-a10a-9656bdce4ae6 | -10.00389 | -50.25741 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da7936e8-e9cf-3b70-b705-7a26f377e5fb | -10.00507 | -50.24818 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b7316425-167b-3ec0-a9cb-80d5396e4121 | -11.07842 | -54.78735 | 2025-10-03 05:23:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71b930d0-d98d-34a6-9eb8-24af766322b4 | -11.53737 | -49.82071 | 2025-10-03 05:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c05dc500-9a5f-3357-977a-2f3c7c3db12a | -10.70711 | -59.19595 | 2025-10-03 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d76c39bf-1a3c-3a12-92f2-4c24142fc298 | -10.00725 | -50.24397 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| dc04cb69-6ca8-36db-bdcb-4b7332fd6a31 | -3.90983 | -54.56026 | 2025-10-03 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d4978b4-6df1-3847-a5dd-2d3ae6ae90f6 | 0.78917 | -51.96753 | 2025-10-03 05:23:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25196507-e474-354d-bbf2-d9eb0a90614c | -10.59563 | -48.71511 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8960913-63d6-3770-bd5d-98b0ebd47295 | -3.49654 | -50.27063 | 2025-10-03 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41e78f23-8843-31dc-b8be-de11335538f6 | -11.06984 | -47.79718 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcff2886-4164-3212-bf8e-8e89e4b497f9 | -10.00517 | -48.27236 | 2025-10-03 05:23:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 801d297f-ed02-3f64-92ab-2ee54038246e | -5.49143 | -52.13367 | 2025-10-03 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61157151-2b5d-31fd-b599-5857adcf437a | -11.0802 | -47.70391 | 2025-10-03 05:23:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f0a212be-54b6-31c8-83e3-fa38b0eae971 | -9.99734 | -50.22378 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 70de359f-0371-30a6-906a-92d39fc7f00b | -10.07211 | -48.18664 | 2025-10-03 05:23:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 447aac09-0ae9-3b47-bb96-58d9f2e81cef | -10.41243 | -54.4113 | 2025-10-03 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62a01046-fe3d-3a8b-8534-a402d37e00ec | -11.29379 | -47.83929 | 2025-10-03 05:23:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 102baba3-368e-3845-87c1-39f00f3169a4 | -10.59982 | -48.70748 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3bb2c124-645f-3430-af3e-eabb94d7e44f | -2.05238 | -56.43297 | 2025-10-03 05:23:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fe8723e-5bd5-3dbb-a6d8-05a2acbbc521 | -10.00008 | -50.2524 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9dc39504-56be-3244-82bf-c3979cd57ecc | -11.0875 | -47.87305 | 2025-10-03 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c222dc3e-6291-371c-9bcc-e30c032fd6f8 | -9.91246 | -50.4985 | 2025-10-03 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e57025c-85ac-3630-8b1e-d9ff64ce72fd | -11.62051 | -47.9962 | 2025-10-03 05:23:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ba2778e5-4d77-351c-8921-272eaf80e63c | -9.91471 | -58.56418 | 2025-10-03 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5eb9a7f-1b07-34f7-85d0-36e72624715a | -11.30796 | -47.84164 | 2025-10-03 05:23:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| de90b15d-c687-3853-b3ae-1cc2d0558347 | -10.00624 | -50.23896 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |


[Clique aqui para ver as próximas entradas](README136.md)
