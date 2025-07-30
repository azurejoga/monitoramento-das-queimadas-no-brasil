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
| 13a3c814-caf1-310e-9503-865510da7b0f | -11.3438 | -51.2523 | 2025-07-30 00:48:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5609f0f4-5787-3777-9002-718b95c79345 | -9.1779 | -48.8484 | 2025-07-30 00:48:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 072ce8a3-402e-37dc-8ab7-88647e73da27 | -6.4032 | -53.369099 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66e3037f-e17f-3aa0-a9bb-2f957d4a058b | -3.8359 | -48.958302 | 2025-07-30 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7361f99-46de-3b74-88aa-07da7e8f973f | -2.9163 | -48.243301 | 2025-07-30 00:48:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bfbbef0-8fa5-34c0-a469-02077699159b | -6.3998 | -53.353901 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc8bfc00-056f-3a87-8e16-4421ab5546de | -12.5826 | -49.7925 | 2025-07-30 00:48:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 265eb7a4-b6e9-3951-92f8-cc8b9c79e5de | -9.2365 | -50.042301 | 2025-07-30 00:48:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e965b283-daad-30c2-87fb-2a5253889aca | -9.6334 | -48.542702 | 2025-07-30 00:48:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9611f3c2-f9a3-30aa-9b6c-83e00e63d062 | -10.0897 | -46.970699 | 2025-07-30 00:48:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7cf0ebd-b28a-32c0-b302-4a1362688032 | -7.1507 | -44.045898 | 2025-07-30 00:48:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3c142258-49b8-3311-992f-6a6987901694 | -4.6584 | -43.1124 | 2025-07-30 00:48:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 744f5b05-1dec-3bf5-b715-17728becfc46 | -11.4653 | -45.129299 | 2025-07-30 00:48:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05bfad14-3d35-3371-8256-6dbc2e8d54b6 | -12.478 | -47.279598 | 2025-07-30 00:48:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4e1fa20-eb2b-3651-ba12-44672ab84cc9 | -17.045601 | -43.777599 | 2025-07-30 00:48:00 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e71332f4-b5c9-345b-87f5-e95b45cc441e | -6.5352 | -56.190102 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 002207ea-0ed0-393c-9ad0-cc1730253180 | -11.4628 | -45.119099 | 2025-07-30 00:48:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd1343dd-9a95-3e18-9138-7958d2a32cb8 | -9.745 | -48.5784 | 2025-07-30 00:48:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b30a1ba-1e3f-3f72-995c-5fb8166b18e5 | -4.8995 | -44.955399 | 2025-07-30 00:48:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9c58b85-773f-31c7-9637-0f8bdc1c7f7d | -6.3832 | -53.325699 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9fbb391-341f-3299-98cf-14b76a3bf5ae | -11.5561 | -44.237598 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c6e256ac-00ff-3b19-93b5-bb86704470a3 | -11.3199 | -48.914299 | 2025-07-30 00:48:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 796b9d08-b4a2-3c5c-b58f-b66567ada7bf | -12.5841 | -49.7995 | 2025-07-30 00:48:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63ab5ae8-c50a-3561-97e8-817ef332c1ef | -4.653 | -43.132301 | 2025-07-30 00:48:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd27c2c5-2010-3763-aae7-d81da689469b | -12.4762 | -47.2719 | 2025-07-30 00:48:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1e87787-d4ba-3995-841e-4d6306bcf8a6 | -13.0851 | -47.312 | 2025-07-30 00:48:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 668690ae-411c-3326-8435-d68a5aa99061 | -13.0869 | -47.319599 | 2025-07-30 00:48:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f16fa19-1c5e-37f8-a2e9-3bb98c8a0250 | -10.5226 | -42.5508 | 2025-07-30 00:48:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| df443806-6ef4-3b82-9505-e0b07da18111 | -11.5423 | -44.2654 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d7d829f-b3f6-36e8-9900-2c9285dd3b67 | -8.513 | -43.301498 | 2025-07-30 00:48:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a307b16c-17aa-30a8-9a47-b3a12fa02410 | -8.333 | -54.755699 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 187d35fa-67cd-339e-bc2f-5a6025e25d1d | -11.9865 | -46.688499 | 2025-07-30 00:48:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1af350cd-e3b6-33ad-a276-0cdf42bd5a87 | -9.4301 | -40.3517 | 2025-07-30 00:48:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 411ef048-e1b6-3118-960a-18b48bb36ebb | -6.4211 | -53.357201 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38b96338-2132-35b5-a6b5-a8b9323c16ed | -11.4701 | -45.106602 | 2025-07-30 00:48:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 121240cf-6c0b-3016-a46b-a61bc68a1d58 | -2.9244 | -48.676498 | 2025-07-30 00:48:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8047fab1-4941-3d62-b672-3779efc46f2f | -12.7101 | -47.784401 | 2025-07-30 00:48:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ccdab597-6393-37b9-9c4a-fb4c5539ea92 | -9.0417 | -45.067001 | 2025-07-30 00:48:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b02552c5-38fe-3f6d-b60f-8de96894ff2d | -6.5254 | -56.1922 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eab62a5-a371-3a7b-88d9-39944df014cf | -3.1816 | -48.806499 | 2025-07-30 00:48:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c431f6a-7263-38cc-a89e-8f447f7bea2f | -10.602 | -45.235401 | 2025-07-30 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e8272220-dfa0-3e70-823a-49f9b08696c2 | -11.4603 | -45.109001 | 2025-07-30 00:48:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 73a153ec-79b2-3f75-97f6-640e2b3fec5e | -6.5156 | -56.194302 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| feb097cc-d459-37af-b3e1-7c5cf1de280c | -7.7347 | -51.0993 | 2025-07-30 00:48:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98521a09-de08-3408-aeca-3cf1021bf31f | -6.5548 | -56.185902 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04a4acb3-04b5-3226-b7e7-a526857c9d24 | -10.6142 | -45.243301 | 2025-07-30 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6f3bd25f-5fbc-3dda-b319-1ae82150dafc | -9.0514 | -45.064602 | 2025-07-30 00:48:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a60a951e-05bf-3671-87f6-8e1480cff13d | -6.4984 | -56.209301 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41a27dad-ccf4-3a26-9a42-3c7ba74b5183 | -10.6117 | -45.233002 | 2025-07-30 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1dc3b9d5-543d-3dd8-862e-01d5f5ed978e | -6.5277 | -56.202999 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8fe48e5-606a-345c-9e99-873b3b73d39b | -8.0162 | -47.680801 | 2025-07-30 00:48:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a9cbd67-316d-3c74-abae-811520d1fbc3 | -11.5366 | -44.2425 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83f5c05b-4470-3879-8a01-046dc8f9ac71 | -9.0444 | -45.077999 | 2025-07-30 00:48:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fefdef4e-5396-3695-bc6d-1352c25b1ede | -9.4242 | -40.329102 | 2025-07-30 00:48:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b66c2acc-1180-3355-b8cf-03ed4dc052af | -6.3779 | -47.258598 | 2025-07-30 00:48:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d17f4bca-cce2-39e3-9cee-d1bf0dba8065 | -6.3917 | -53.363602 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c64d9a3-f7e8-3dfc-8411-eb5e3e89ba3e | -3.8806 | -41.0284 | 2025-07-30 00:48:00 | METOP-C | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c68f5579-a537-30e2-891c-56e492b7fd58 | -18.572599 | -44.4198 | 2025-07-30 00:48:00 | METOP-C | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d0efd35-4aad-3b99-9110-02d2daf573cd | -10.624 | -45.240898 | 2025-07-30 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 624f8c3b-b055-38c1-bf92-159a4c82fca2 | -11.3328 | -48.926102 | 2025-07-30 00:48:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 148a053b-1cee-3931-933b-2b1e69226138 | -11.3422 | -51.245098 | 2025-07-30 00:48:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 01ceda3d-1fec-38b7-ac61-a955fe65ee86 | -6.0245 | -47.554199 | 2025-07-30 00:48:00 | METOP-C | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d5e5b9c-788a-3a2a-8fed-f6dd6613b7a4 | -8.026 | -47.678501 | 2025-07-30 00:48:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98e6aea7-d4a7-3f28-b0f3-8f0fe51f108a | -2.9225 | -48.668301 | 2025-07-30 00:48:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e1946d1-1215-3cda-9ba7-d6ec08aede1f | -10.6167 | -45.253502 | 2025-07-30 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 68bdef6c-6d79-3f9a-9d97-fcf6aee91db4 | -10.7091 | -48.862301 | 2025-07-30 00:48:00 | METOP-C | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d9cc381-ab69-3afa-95a8-3aa17c2e893e | -10.0877 | -46.962299 | 2025-07-30 00:48:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d89c49b9-2f90-3c9c-98f6-3a89b1b85693 | -6.5133 | -56.183601 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c118ab62-7d5e-335c-bfda-b1129c28110b | -2.9045 | -48.2369 | 2025-07-30 00:48:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad005940-e6cb-355d-b5fb-d6bd4d780e35 | -7.9332 | -44.083302 | 2025-07-30 00:48:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c55ec84b-3537-3212-9774-7bb55a63712f | -12.812 | -45.433601 | 2025-07-30 00:48:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 515e15dc-bb2a-3ca6-8cf0-070f4dc6a320 | -8.3408 | -54.744301 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff2a3a0-53b1-37ff-9677-cc29753bef1f | -2.9183 | -48.2519 | 2025-07-30 00:48:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bcc7d14-f27f-3b29-abf1-4a271bf87ae1 | -7.8622 | -46.727699 | 2025-07-30 00:48:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 391e702b-4180-3097-83ca-81a42fce6162 | -9.2677 | -50.2239 | 2025-07-30 00:48:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a550b74d-c94f-3683-8445-2ff6e1f547ba | -8.331 | -54.746399 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b387b51e-031c-3ccf-8e9f-000b86067a63 | -11.5297 | -44.256401 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad5c9abd-b7eb-3736-9e78-c3d839a5339a | -6.2497 | -46.113899 | 2025-07-30 00:48:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d41b42f-0110-3043-a792-d0c891e8d66d | -17.4881 | -46.736801 | 2025-07-30 00:48:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 34b3312a-96ae-30e4-8684-26a5becf5e2b | -6.413 | -53.366901 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb945c8-ec44-3457-8181-b691c1fb0ef4 | -2.9085 | -48.2542 | 2025-07-30 00:48:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3b90359-6cbc-340a-9467-d49c7bbbce4f | -8.51712 | -43.32245 | 2025-07-30 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 21d7b866-bb37-3c4f-9b23-a9a005044c7c | -6.52124 | -56.19796 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ca592cf2-8a7d-32a2-a432-caf9452cf7a6 | -9.15591 | -49.85454 | 2025-07-30 00:48:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 275aaa33-44ce-353d-8221-d4c973119eec | -8.02064 | -47.69461 | 2025-07-30 00:48:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 21e1c654-a30d-3175-8dc5-76391ef80426 | -5.25037 | -45.21407 | 2025-07-30 00:48:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| cdaa0e55-51eb-32be-97f4-80476a0ed27f | -10.27987 | -46.92709 | 2025-07-30 00:48:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1a76e512-b32a-3373-a1d9-fb98dcd72667 | -9.14565 | -49.84671 | 2025-07-30 00:48:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| aa3d3125-b1b8-3ad0-b68c-dbb29bdaeaa2 | -9.2378 | -50.04688 | 2025-07-30 00:48:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2ad3046e-2d31-3734-985b-75ba4e43cd4e | -5.25156 | -45.22053 | 2025-07-30 00:48:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| aef321e9-c92a-352f-aba0-490f869779c7 | -11.47 | -45.12644 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 6f063ac7-f09e-3bfd-9898-7436f2394103 | -9.14695 | -49.85585 | 2025-07-30 00:48:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a945a72e-a877-3611-95b5-258ea010cdde | -4.6493 | -43.11963 | 2025-07-30 00:48:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| f53bcb02-a46e-3427-bed8-60b1101b681c | -7.93481 | -44.08797 | 2025-07-30 00:48:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| f74e6b42-03c0-3851-ae1a-ac5b4d0f8829 | -8.63234 | -45.88556 | 2025-07-30 00:48:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6600cd97-1dcc-3993-b8e5-fe9b2854cfb9 | -11.34806 | -51.25663 | 2025-07-30 00:48:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 65e53df4-1c20-376a-a307-658de77963dd | -6.25333 | -46.12453 | 2025-07-30 00:48:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ec1e6d46-3231-3b5d-b225-7a08e472c712 | -7.85335 | -46.73365 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 23bfc2fc-2534-3866-bdbd-1937c22fb06b | -7.86297 | -47.87334 | 2025-07-30 00:48:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5fbd0d80-df14-3b87-b34b-c1809893d913 | -8.68176 | -51.21589 | 2025-07-30 00:48:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |


[Clique aqui para ver as próximas entradas](README7.md)
