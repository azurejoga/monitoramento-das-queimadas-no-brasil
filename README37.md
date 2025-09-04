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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26619798-dbc5-31cb-8d91-0879b41b35f5 | -13.45701 | -46.9385 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47a6f385-313f-3b69-a8f5-5155f35c71fd | -7.69507 | -48.73729 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 11c06dc6-e499-30a1-9314-1ccd85dbc600 | -10.1546 | -46.27068 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2aa7578-bc47-32c1-8967-3c25673f19ad | -10.4806 | -53.62603 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e43b8ee-4538-3108-86ab-f4fb272bcdf7 | -12.63736 | -57.00856 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0ebee8a-616e-3925-aaeb-2cc0c163e72e | -9.76954 | -49.44586 | 2025-09-04 04:27:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ae47ff5-dfd7-361d-b9f0-909c699e1593 | -11.23313 | -44.96371 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c3947e8-0bd2-3674-91d6-cea327fca659 | -11.62061 | -52.18845 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e24fa4fc-aba8-35ad-b1b9-a0d0a8c474ab | -7.85927 | -46.73177 | 2025-09-04 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86edd62e-6d81-3a56-a1c9-8c08687c90b1 | -12.48758 | -48.06355 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc53b46c-3123-35c1-9dc6-dbfedab19d45 | -12.48482 | -48.08113 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1514dfbf-3193-3f6f-813d-1dcffb92ab85 | -8.90046 | -45.84962 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd6ca7a1-36d8-31cd-8721-f075eda02183 | -9.97734 | -51.63358 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 114dfae1-1337-3c47-ae9e-1223436c97bc | -11.61672 | -52.18779 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1a102a1-e578-3b49-817b-e849bcb10480 | -7.69873 | -48.78048 | 2025-09-04 04:27:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfc28d2b-a829-3c65-befc-bf8dfb7fb1e1 | -12.49297 | -53.84836 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dec586ca-9f0d-39f8-8b11-34eb63c99a0d | -14.53704 | -48.07343 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8cd97277-4391-3878-9cac-fc90b9808e4c | -9.07069 | -46.98838 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4eec75d-66a1-324a-991c-f0bc5210e8f5 | -10.88238 | -55.73613 | 2025-09-04 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a97f9f7-f59a-3480-a5fe-fd36a3458b89 | -11.88185 | -50.6045 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29a3d330-1748-3469-a423-211c4b38df52 | -14.8199 | -48.331 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48fd1770-ed6d-324e-917c-4b0626437217 | -6.74309 | -58.7196 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3a9b5563-f0ba-34ec-b323-8ad0211afd69 | -8.38053 | -48.31932 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9f3c51c-0a01-3f77-9a5f-5435acc07a37 | -10.87713 | -44.03768 | 2025-09-04 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be4cc5b0-40a7-3662-b3bc-686f0b645d04 | -13.31076 | -51.76466 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6514a01e-2abb-367a-97db-d7acf3b8fe46 | -11.05427 | -45.40757 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 627a36e1-4934-333e-bff5-60b6b6b9fc0b | -9.50137 | -43.16553 | 2025-09-04 04:27:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7c027a22-843a-3f91-8dee-c008f2402046 | -10.53136 | -46.76022 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 828e54d3-d814-3d03-bb69-7b1c8c412fff | -12.81205 | -47.6656 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d006e02-ce65-3181-8fa7-2050ba53dc21 | -10.99159 | -49.75021 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a81cf45b-6db2-3fa7-862a-6b85b4434295 | -8.90721 | -45.87252 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a2ed017-4da3-3ae1-b3d1-f4d1bc95d89d | -13.31214 | -51.76595 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc541d6b-43e1-3c42-ae71-007b5f12a6c8 | -15.04081 | -50.07404 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd83eb81-1154-3725-80dc-986bcf42290a | -15.05937 | -50.04578 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d8bccb6-5c24-3227-a53b-7a6b610e3596 | -12.97332 | -54.76087 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b51e560b-aaab-3d7b-beed-3d419ea1ec54 | -11.61974 | -52.19342 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4508e2aa-1ab9-3bf7-862d-f367f34b463e | -7.71442 | -50.29144 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07e1f81c-e8d6-3970-a62b-74fa04762de6 | -9.33027 | -55.21494 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 086277d8-d2f8-30b6-be03-ced905891952 | -7.69285 | -48.72919 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 50cfede2-5039-3ac0-a96c-9ac8f73b7e74 | -12.23429 | -50.14482 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f3cf896-13a2-3f02-9c83-6835d681191d | -11.67609 | -57.35065 | 2025-09-04 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| bb98e452-367c-309f-a051-54aa694c5186 | -12.23776 | -50.14541 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94fb494e-6167-34ee-8700-2a2b68231421 | -9.33516 | -55.21594 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 65f67bfc-9475-3358-9eb3-0c521e42d76c | -9.45074 | -46.75677 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d45ae92-afe3-3874-adcb-990cc7cdf343 | -8.36299 | -48.34254 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae6113d5-6334-3747-b674-9a2aafb88458 | -8.44125 | -47.33648 | 2025-09-04 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 686b4ef5-9a00-3b28-a501-0d34753953b0 | -8.06708 | -52.34965 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35c6a1cf-6f13-3cca-9821-8818e54b566e | -7.71076 | -50.29076 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1db6f9a1-3b6a-32dd-98fb-61da71b68dea | -14.81834 | -48.23256 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1730a40-46da-3150-928f-7f61feb887f1 | -11.44228 | -46.91512 | 2025-09-04 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b33ddc32-30d6-31e9-8a37-4b67d3c1ea5e | -10.14068 | -46.25026 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89752361-1f3f-327b-a134-a68a19091750 | -12.233 | -50.15263 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88d83339-ea3e-3223-821b-e6a9d93031cd | -12.48648 | -48.07058 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e6edb4b-e646-337d-8a79-65db6f4e117c | -11.86417 | -51.50153 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac8978ab-4c72-3dc3-a6cd-346d5d0bb021 | -11.61354 | -46.64132 | 2025-09-04 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49d79b65-85d3-3bb7-ad70-d59d1e1eb83b | -13.44646 | -46.94038 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 499f2bcf-48d0-3b18-940a-bf08f7a52450 | -10.95939 | -44.21877 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3800136a-cdee-30d6-92ce-a234e5f10852 | -11.86405 | -51.52458 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 145800ca-1a2a-3d32-acb8-4b02405c3a40 | -14.77509 | -48.13819 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6516ca80-4ed0-3310-bc96-0e27021259af | -12.18465 | -53.88622 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebfb751f-73cd-359d-bd7b-2889e20e7fe8 | -9.62191 | -47.03392 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72e687c5-e9d5-377d-9bde-cc96eded6639 | -7.69164 | -48.73677 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9a52b8cd-8216-3c8b-8786-c8ab52fbb0a3 | -7.97817 | -46.36006 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cc0e613-0e9c-3966-9de1-58cbbd391f67 | -11.05771 | -45.40807 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d951cb3-3c65-380d-a6be-35526b204637 | -12.15829 | -43.70646 | 2025-09-04 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4d55dd6-b883-3341-97ce-2c02fbb5fc6f | -8.37105 | -52.53164 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3a6b9aa-9805-3cb5-9577-a23f133b7ca2 | -8.85546 | -52.01604 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9df886a0-27b6-33b0-9524-31f655501dca | -8.03992 | -45.38407 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9bc458e0-1acc-30bb-8893-beff6de2cd5a | -8.88519 | -45.7706 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 463f0c6b-64df-3d29-a666-4387c435a52c | -13.735 | -46.92268 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9932bbbb-8286-328c-903b-40192cb86553 | -11.05542 | -45.39996 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f00b1409-16c3-34cd-91a4-0edbce43f4bc | -8.45582 | -45.04356 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1593b69d-3818-3887-9a0e-e8ee92462320 | -8.49992 | -44.63411 | 2025-09-04 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c64315e-2407-3e69-aac8-6a89b3884612 | -15.02552 | -50.04034 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 154f1ef9-f5d2-30d8-9560-adfdd08e2b21 | -9.06354 | -46.9908 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4de314a2-5f29-3d28-9a27-e686d21b4688 | -15.03827 | -48.10858 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbb2a513-488b-386a-a6e1-5ce9a79fb045 | -14.82111 | -48.21481 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc407b68-b7f3-3aba-b44e-8d2d7d7702e0 | -15.00802 | -50.07584 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44212527-ad99-3669-a271-ff8758fcde2b | -10.96676 | -49.75003 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7caac646-c302-3466-8cbb-b40a69cec920 | -14.56127 | -48.04835 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55ca4b45-4e52-31b0-8330-7ba59cfa93c8 | -11.95633 | -45.77048 | 2025-09-04 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fc0b659-fc61-33fb-a7ca-227a5eadf306 | -7.36547 | -49.38998 | 2025-09-04 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10fd3eb8-6941-3544-a7cb-755177175215 | -12.48207 | -48.07706 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 706b697c-281e-39d8-8013-4c0ae40c205f | -12.91038 | -57.00209 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 272fa4f4-1f14-3f19-9ce1-2fd099e10492 | -14.29106 | -53.09307 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 633abde5-cb8a-32d7-ac89-3a582d4ca89d | -12.90003 | -56.939 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59c18488-1de2-3a51-b259-b406ff524e02 | -11.6413 | -52.20752 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18f9d69d-8ce2-39e9-bbfb-27fc92c5938c | -11.64603 | -52.20329 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1be55853-06d8-35c0-a29b-b6f5c6dae7c4 | -15.004 | -50.0364 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 179283c2-8c08-37d2-a6f6-5cd3a07ea469 | -14.57197 | -48.06878 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e857f14-44cc-32bf-a210-ca6d661e6fbe | -9.4376 | -48.09396 | 2025-09-04 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6175788a-4ca6-3b7f-b974-cd95a3151925 | -14.8145 | -48.21372 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f5101cbf-620a-33e4-81b4-6c4d15aae001 | -9.72576 | -48.31537 | 2025-09-04 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c86fd33e-cc50-3867-b73c-d2ba1a6b5bae | -12.24058 | -50.1499 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b31c94e-1b13-3ff2-8b25-22906ec7f0d6 | -14.81107 | -48.34411 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b3fb45d-b5e3-3692-a0af-4bc5e0411252 | -12.9143 | -57.00962 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20aeeef4-9b53-3fac-98bd-ff7f01262134 | -14.78094 | -48.16816 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f50fb0c-8c66-3f48-9b3c-b900c8d28136 | -15.03883 | -48.10502 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3e307e2-ad09-37b6-a56b-2eb83752ffdc | -15.04206 | -50.06648 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9f4e9eb-424a-36fc-90b0-c4e5d921cd75 | -8.72797 | -47.0048 | 2025-09-04 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README38.md)
