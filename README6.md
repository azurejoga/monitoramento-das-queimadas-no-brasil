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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6484a31-df1c-3550-9e46-ad8e5a1f0eee | -5.40819 | -46.02427 | 2025-10-30 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7a86bd71-d19e-351e-8387-d20c1cd51465 | -3.22837 | -46.86466 | 2025-10-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8c529fa2-3688-35da-a729-012dbf9b6429 | -8.33451 | -47.92727 | 2025-10-30 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d4fb64ee-66b3-3c79-a03d-8397a98366d8 | -6.58132 | -47.54037 | 2025-10-30 00:35:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0530b932-1679-3eb2-beaa-7e43defb0f96 | -6.85838 | -46.28613 | 2025-10-30 00:35:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1068fe9c-b6ec-3ac9-88ce-11e108b17aa3 | -4.48455 | -43.42317 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| cee5b1ad-20a0-37ae-97bc-c7444eb4ead3 | -6.48573 | -39.74062 | 2025-10-30 00:35:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 60ccacc6-2b86-36c8-a0d2-26b0a3c2704c | -7.30155 | -45.67862 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| aea9ad53-16c5-3a38-9591-3a11f38f1dd5 | -5.80477 | -40.84282 | 2025-10-30 00:35:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 6b6e784f-a168-3260-91e2-a32eeafe8760 | -8.70201 | -47.98411 | 2025-10-30 00:35:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 15f34de0-a993-37e5-b929-08a6afee7e05 | -3.12758 | -49.10201 | 2025-10-30 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d93255f-23c1-3e0f-a6a1-cd8620e45697 | -5.02695 | -43.6127 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 91522800-3d1c-39c4-8050-d9846bedb183 | -4.42588 | -43.37034 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 13507427-9df5-316c-bca6-90dc330f08e4 | -4.08703 | -46.9344 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f68035bb-3ff8-388b-b794-9b68379aa258 | -7.28322 | -46.0589 | 2025-10-30 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0eb354aa-305f-3599-8603-16162d4d578e | -3.84872 | -49.38039 | 2025-10-30 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62aa21fb-abea-369a-af7b-8fc1c3aca56f | -3.76567 | -50.36711 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6c90dc30-3281-372c-b983-a00bc6d76f3f | -7.86085 | -43.7902 | 2025-10-30 00:35:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| c05ed5ee-04a4-3a99-bd36-27aa47ce0ea6 | -3.66635 | -51.72276 | 2025-10-30 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 57bd386b-3acd-36b4-a22b-b5b85e630e26 | -4.15912 | -46.79396 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9017fdc9-3a4b-3803-9818-616cd25b6f1c | -2.66647 | -47.87564 | 2025-10-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ce0420be-f0cf-3ead-8f23-f66f5755fd27 | -7.32027 | -47.85817 | 2025-10-30 00:35:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1607b88b-5ace-360c-b0be-90b0274a1818 | -4.22923 | -45.5854 | 2025-10-30 00:35:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 5bf1298b-f0b4-36f1-aba9-3a1e5e6624de | -4.03155 | -47.7807 | 2025-10-30 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3ccd315b-cc69-3f33-abb6-f054c80f7e69 | -3.23016 | -46.87725 | 2025-10-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| a0ed20c2-36b4-33ff-a962-50156142493e | -6.86011 | -46.29825 | 2025-10-30 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 911d5b3d-772f-399e-9513-6ce90605cebc | -3.38281 | -48.95104 | 2025-10-30 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cb974b32-9edf-3781-90f8-5792f820a112 | -5.60841 | -47.1247 | 2025-10-30 00:35:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| c075afc1-4e92-3664-8b14-1f7a227e8a64 | -4.3657 | -55.77656 | 2025-10-30 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 731ecbc9-3765-3334-a621-150fae4ce26f | -4.2989 | -48.06353 | 2025-10-30 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b194b13c-b874-3266-8858-a5f42cc0a4ac | -9.84971 | -47.69544 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a4f01658-ecb8-3bd2-a172-e16961e82dcb | -5.9341 | -47.32489 | 2025-10-30 00:35:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d73beee5-895b-3ee5-861b-8c41a36eebce | -2.66589 | -49.95498 | 2025-10-30 00:35:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5c9d39d6-73b1-38c8-8f61-47fa32782f8e | -7.30323 | -44.98391 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 12e1d4ba-2db6-36c1-aa44-9ef4bbff8751 | -9.28947 | -48.41836 | 2025-10-30 00:35:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9941ecc8-76a6-327d-af78-907ebb032c60 | -6.23435 | -43.97119 | 2025-10-30 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 0d31a868-ade0-3c4b-9ee9-18d082a02fac | -8.70027 | -47.90702 | 2025-10-30 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 18848031-24e3-3e9c-a18e-7db406f240e2 | -3.48415 | -52.34747 | 2025-10-30 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 49db38d2-9021-3d24-8318-c29d879bf085 | -4.96257 | -48.2611 | 2025-10-30 00:35:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2e82ccb1-8d30-3f3a-a8c1-25653df42a3f | -4.43273 | -43.23239 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 42e41c67-627e-3451-8e8b-9ae2e806c9a0 | -4.85105 | -45.43566 | 2025-10-30 00:35:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| baf2c413-a74e-30d2-92a7-c5437b5b3314 | -7.93046 | -45.49804 | 2025-10-30 00:35:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d2920bef-a528-38fe-a733-a20ae7c7cea4 | -3.52929 | -47.5517 | 2025-10-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 22523df5-d348-3185-b63d-2e9f28fd50df | -5.04126 | -45.17148 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1c7c3ffc-2410-3b37-a979-53df0bff45a2 | -9.08897 | -47.78627 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| af4becf7-b314-3ede-886d-fa1d3d67021e | -5.43512 | -45.34187 | 2025-10-30 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 049b40a6-eca8-39e9-983c-31faf3c229f7 | -4.35645 | -48.19921 | 2025-10-30 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 94c7446a-d8bf-376f-9550-eae996cb7877 | -8.24225 | -46.92145 | 2025-10-30 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fcc87432-b8eb-3ce2-8b3a-baa23e5ff9e8 | -9.82748 | -49.56776 | 2025-10-30 00:35:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7a38fc75-31e2-381e-85ae-a441fd279377 | -3.83976 | -49.38168 | 2025-10-30 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| add01678-be36-3517-ad78-cdf5833df6e7 | -3.34998 | -49.50629 | 2025-10-30 00:35:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6ab79809-3a3a-3e3a-8b5c-43cd519c3ec1 | -6.01411 | -41.98936 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 7cae9904-1777-3f8f-866a-39d47ef5433e | -9.7114 | -47.7574 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b2e46166-7293-3c18-a061-5dd268c2438f | -3.23196 | -46.89 | 2025-10-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ee33cbf3-2037-3651-86dc-d40f2ed0c22b | -4.33506 | -45.75869 | 2025-10-30 00:35:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1b1adbf2-18ad-32d4-920a-5bf9c459b00b | -3.48544 | -52.35707 | 2025-10-30 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 36fdf5b9-9a51-31d0-b950-179a187900fe | -3.66511 | -51.71365 | 2025-10-30 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| f58b9f6c-c708-3fe2-9565-81045987f2f4 | -5.59141 | -51.12244 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| f5bbf371-9fd6-3108-8218-2e74d06f3880 | -4.25932 | -50.67092 | 2025-10-30 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d3fdf0cd-b62e-3839-a5e5-d3563e220974 | -9.93946 | -47.17379 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 231ee55d-cd4a-3327-8bfe-6dbc3bab15ac | -3.689 | -51.0814 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 23fc23ce-d32e-3fc1-907b-fe5589e0c848 | -4.01996 | -46.04627 | 2025-10-30 00:35:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3c1ee871-eb02-35e8-9333-e192f2f778c1 | -3.35255 | -52.80702 | 2025-10-30 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b22c1a69-1473-3020-ba77-03a5d4682f4d | -5.79927 | -40.80794 | 2025-10-30 00:35:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 35.6 |
| 1dccb19b-7dcc-3b71-b3dc-6f999e19ebe5 | -3.4321 | -46.18265 | 2025-10-30 00:35:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e10d6966-b0fe-3c61-9dab-06726fc711b5 | -4.5319 | -54.9682 | 2025-10-30 00:35:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| b4d3784a-6945-33e7-8cfa-5ecf17b3f182 | -9.05201 | -45.3546 | 2025-10-30 00:35:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| bdb97090-6b91-3447-8363-8567d19aae03 | -7.61987 | -43.57883 | 2025-10-30 00:35:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 739afd92-fb9d-38aa-a021-294269dabad2 | -7.95853 | -46.73983 | 2025-10-30 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5781f5d5-b7b6-343e-813d-cb1b2b2ef468 | -6.01303 | -47.09652 | 2025-10-30 00:35:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 800467d2-36eb-37c0-b6df-d20a07287a7b | -3.61467 | -51.07999 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a17d439d-72b8-33f0-bfec-ae850047ad47 | -6.48329 | -46.88332 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 6543169d-8f07-3661-a01b-4b00eeca9636 | -3.48655 | -49.89347 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0c7b07ab-58ac-3948-9138-355fe5addef4 | -6.99252 | -46.22893 | 2025-10-30 00:35:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 94bc31b0-644e-3778-8cdd-979f42e50fb8 | -4.8408 | -45.84211 | 2025-10-30 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 397fc9be-1164-3b44-b7c1-4b56dbf1beda | -8.47589 | -48.20763 | 2025-10-30 00:35:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9dc3c1a5-1f56-36b2-8e25-79c2b03908ab | -6.13629 | -41.59318 | 2025-10-30 00:35:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| b36d5287-1f51-3993-a001-eed398b5c2df | -3.40865 | -52.72795 | 2025-10-30 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4b94fb65-d0c9-34da-926a-c53be3dcd711 | -5.93074 | -44.73174 | 2025-10-30 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c3b4f6bd-2489-3c17-b083-1cb110dae7b0 | -2.79446 | -50.28389 | 2025-10-30 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 2b0c1e2f-0080-30d2-820f-951f4db97911 | -8.32674 | -47.93812 | 2025-10-30 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 1017e551-ba32-3874-9389-d5f610fa4ca1 | -3.21978 | -46.87875 | 2025-10-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0cfddef4-1019-3d84-a894-6f181ab220ad | -7.02226 | -46.43226 | 2025-10-30 00:35:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9dd9cff9-b3f6-3eb1-b0e4-17411874f3ba | -8.32402 | -47.9191 | 2025-10-30 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6b797296-fc4d-328a-9199-81d5dbba7d47 | -2.77316 | -45.38398 | 2025-10-30 00:35:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| cf94963c-004f-3da0-b796-fc46efda339f | -4.68911 | -46.36713 | 2025-10-30 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c1e51dc9-893a-337c-8fb9-0329abf1f526 | -9.08692 | -47.90277 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| dbb3850a-4eae-35c8-b818-8c686cb5e024 | -9.89883 | -47.90904 | 2025-10-30 00:35:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2803131a-7b98-398e-bb61-3a10c854d6b6 | -6.532 | -43.58529 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 054d0925-9f9d-37f6-bac0-a957e87193cd | -9.31708 | -43.09376 | 2025-10-30 00:35:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| f1c123f5-1a36-3488-8122-c3cf16c25b92 | -4.69015 | -45.59339 | 2025-10-30 00:35:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| be0c3e4f-6540-366c-b542-0c06283accaf | -5.23065 | -46.14482 | 2025-10-30 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 43d8e95a-14ca-3c55-b426-0cb4d2a6d6b8 | -3.60642 | -52.64212 | 2025-10-30 00:35:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2831360f-dca7-385e-9e43-d2fef9f6766d | -3.44611 | -52.81887 | 2025-10-30 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fff83af4-5d9c-3ef1-8911-2307c1b55420 | -8.43459 | -48.69716 | 2025-10-30 00:35:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fc6a7a7e-348d-3924-8520-500ef0a9d623 | -3.10851 | -51.28685 | 2025-10-30 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 10f41d99-0896-3c39-b554-0a685f7e4b32 | -5.43659 | -45.3503 | 2025-10-30 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f91917be-a82e-3d04-b73b-fffd7d2a7928 | -3.98147 | -51.06751 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3ba8eee9-6b72-350a-bf71-3ff631c4c53c | -6.85746 | -46.29229 | 2025-10-30 00:35:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| cc4e4af4-ce37-3477-b83e-57a63be1122f | -6.13451 | -41.58689 | 2025-10-30 00:35:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |


[Clique aqui para ver as próximas entradas](README7.md)
