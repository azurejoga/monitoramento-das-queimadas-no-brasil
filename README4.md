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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 092a7049-00eb-36e5-8952-b902f872668f | -15.82634 | -42.68551 | 2025-07-28 03:28:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e54db488-4abd-361d-b9c5-78381e6827b7 | -17.35582 | -42.63885 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b67ef36d-4a2a-34f1-a8a0-e82855fe7a1d | -14.97692 | -46.96562 | 2025-07-28 03:28:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcbf2645-3a1e-3dbd-a7dd-d578ddd6d009 | -14.48627 | -46.53413 | 2025-07-28 03:28:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f73ea52-e449-35ae-bb26-1b48e5552709 | -17.35511 | -42.6423 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 14a9c81d-56e8-3e69-89ac-d79ddec279b5 | -19.5061 | -48.48209 | 2025-07-28 03:28:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9aacc2d0-27c0-36e9-8293-c09150682c5b | -20.37904 | -42.15348 | 2025-07-28 03:28:00 | NPP-375D | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e068701c-dc5f-32b3-982e-be0ceef6f3c5 | -13.52787 | -46.29737 | 2025-07-28 03:28:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 194c8a56-1344-37f8-aa54-889b4c5f3453 | -17.53668 | -43.92352 | 2025-07-28 03:28:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fd2a042-434f-38f1-9997-61487185b94f | -14.48812 | -46.54764 | 2025-07-28 03:28:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10831790-8dcf-30e7-b37a-946bd19d50c3 | -17.36397 | -42.63686 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f849d18-6922-3789-8cb3-a3c010811346 | -15.83194 | -42.68637 | 2025-07-28 03:28:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4918dd44-9f3e-3444-a01b-2df57b2d181e | -17.36047 | -42.64351 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e8d7d100-0edd-363d-b60c-e97daaebddc0 | -17.35901 | -42.6506 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9e5003e-231f-34cd-945f-70a593457640 | -14.48464 | -46.54132 | 2025-07-28 03:28:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8f2216c-776e-303c-a0ee-9d6f41e3dfb3 | -15.82546 | -42.68979 | 2025-07-28 03:28:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 3be03b47-e841-39b3-82cd-04fbcb563166 | -14.48971 | -46.54041 | 2025-07-28 03:28:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3aa7e210-0e97-3f42-8466-0ee73e352be0 | -4.1601 | -46.8322 | 2025-07-28 03:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e470637a-8cdf-36d5-b522-d14af276f205 | -6.489 | -56.1941 | 2025-07-28 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| c40e72cd-9755-345e-a784-5de0dd407a17 | -4.1603 | -46.8101 | 2025-07-28 03:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 18e0fd6d-cae7-3877-9b07-e1074925d11a | -6.4889 | -56.2139 | 2025-07-28 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 8e384ec8-3fd7-3acf-a300-bafd89fa818a | -19.96626 | -48.4259 | 2025-07-28 03:30:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b859045-dbb6-3f39-93ff-bc67ae159260 | -19.97334 | -48.42775 | 2025-07-28 03:30:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7714e5aa-a2c0-349b-a76b-28da5c3464b1 | -19.96904 | -48.42627 | 2025-07-28 03:30:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 099e1822-697f-3152-9120-f7e97ad8193a | -4.1603 | -46.8101 | 2025-07-28 03:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 95.6 |
| cf6fc00b-9aa2-3fc4-baa6-35db6775193c | -6.5074 | -56.213 | 2025-07-28 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| bb42ec13-af12-34db-9dbc-75e8b3762d40 | -4.1789 | -46.8092 | 2025-07-28 03:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c2716f1a-d442-368c-956f-02ec4daab636 | -4.1601 | -46.8322 | 2025-07-28 03:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 65668658-50d4-3661-b7cb-18995785da16 | -8.10658 | -43.06325 | 2025-07-28 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e1438769-f76f-3e31-8800-3b36f6c5d672 | -6.64337 | -43.03666 | 2025-07-28 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 460e89f3-fd8a-32d5-a2d5-d04b5927d09d | -7.55687 | -43.68597 | 2025-07-28 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef07a82f-9e8f-3382-96cb-f018ebb2099f | -7.23927 | -45.38963 | 2025-07-28 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3b05a83-1479-37b7-8da4-0fd7480cd07d | -4.0464 | -42.52386 | 2025-07-28 03:47:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d437a0b9-17a7-3a95-8c47-0de7825e15fa | -7.9211 | -43.10524 | 2025-07-28 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b643fc98-b395-3e01-87ef-96eb3cd25c90 | -7.08689 | -44.8983 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df1cf116-75c3-3ce1-b408-7b99806dffe0 | -6.85172 | -43.06131 | 2025-07-28 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7575b53-d3f6-30f5-8542-78bae0fec5f5 | -7.00634 | -42.36276 | 2025-07-28 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0833ef6a-ff19-38b2-81fa-9fe8801d4620 | -2.95047 | -41.35841 | 2025-07-28 03:47:00 | NOAA-20 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bf06b95a-5e85-38aa-823c-976e01a718f2 | -7.92212 | -43.10282 | 2025-07-28 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 419e8c70-31e3-360d-b316-a4e4438ea96b | -9.59625 | -43.86357 | 2025-07-28 03:47:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 244ecec0-1664-33fa-a229-183c4b8d50ad | -6.92462 | -44.23863 | 2025-07-28 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d9aac6d5-a4f5-36c3-ba2c-5737c88aa538 | -7.9107 | -43.09284 | 2025-07-28 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f732777-3674-3edb-9de0-51d26b3e4a00 | -7.29509 | -43.4221 | 2025-07-28 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92da5d51-a609-3945-9bc2-cf4893770cf9 | -7.13986 | -48.20763 | 2025-07-28 03:47:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ac3b16f-aa51-349f-b8f9-94a0f0013649 | -7.90933 | -43.10099 | 2025-07-28 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93756664-ee5e-32d4-bbc1-9796480c6bb5 | -7.41799 | -44.7136 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 754d5249-7287-32c9-b021-e87bde035b47 | -7.24377 | -45.39339 | 2025-07-28 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 14c15346-78cc-30a5-9cbb-495cf335177b | -7.78516 | -44.60705 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c842b1e7-8ae1-3aa6-ad02-e7a19e708580 | -7.53628 | -44.43042 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ff47fb2-f211-358f-a558-1d15673549e2 | -7.0983 | -44.935 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42b6c65b-da06-3b3e-a939-ddaacd6169ca | -7.69431 | -46.0479 | 2025-07-28 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3bbeb61-7dd0-3a2f-b194-8d4813aacdde | -7.06952 | -44.91206 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db2f628f-121f-3424-87e2-bf257ab61fe0 | -3.13424 | -47.01405 | 2025-07-28 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 424fb83b-aec3-35a2-bd07-128034f5c1f2 | -7.18197 | -43.94774 | 2025-07-28 03:47:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fe10c96-69f9-3499-99b2-312342112c2f | -3.1402 | -47.01507 | 2025-07-28 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc0fb34d-589e-30dc-be0f-4516bd0e6203 | -7.91002 | -43.0969 | 2025-07-28 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fb4ce42e-48ee-37c7-8fb5-72f155658454 | -7.01169 | -42.35611 | 2025-07-28 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 479e6667-6304-3985-bf10-7aeee2e00275 | -8.03465 | -46.90606 | 2025-07-28 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c57aec4-64b3-3d7c-8302-6b7a46f4df24 | -6.63475 | -43.03514 | 2025-07-28 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 159c972f-df15-3c1a-abd6-797903c76bd7 | -7.08 | -44.92493 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| baa3e377-1c38-366b-a33f-20e3abb017bb | -7.07218 | -44.91246 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1deda3fd-a0a6-3684-9b49-eeec9ee370c5 | -7.00697 | -42.35906 | 2025-07-28 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 669f610f-eedf-3ec7-b16a-ecc19b4547a7 | -7.10997 | -44.92577 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad44d80b-4e04-35ee-926a-9b821a1819e8 | -7.2882 | -43.07367 | 2025-07-28 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c5c71979-2fd4-3044-8c95-de50367342ba | -7.10031 | -44.95211 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4403b380-de19-3a38-9a45-bc689faae163 | -7.23978 | -45.38673 | 2025-07-28 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96dc1930-a55f-3fdd-9e47-d25d12fb87c7 | -7.35269 | -44.72042 | 2025-07-28 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a040c3f4-94fe-3da5-a53e-1845f64107cb | -8.10725 | -43.05938 | 2025-07-28 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ac6540b7-8487-35f5-88d3-be0d237c98f1 | -7.02042 | -42.10859 | 2025-07-28 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 19ab284a-575b-332c-83b8-e77632f8231a | -7.37544 | -44.48127 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34b29554-ed92-35ce-b695-7b97a9bfd835 | -7.09642 | -44.94568 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2549dcdc-4923-3ed9-88ed-4d6bad4410df | -7.92143 | -43.10693 | 2025-07-28 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 325b213f-688c-3d33-9c2d-329bf15e2584 | -7.80495 | -46.57486 | 2025-07-28 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4221ca3-9abf-3981-9b9c-992d0814ca3a | -7.07801 | -44.90789 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33d83f7e-d371-3771-9c06-3a3416ed446f | -7.90354 | -42.63299 | 2025-07-28 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c8201945-0307-3e80-8a8f-49293616db04 | -7.08096 | -44.91954 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8c9d337f-5616-3df0-9556-6596a44c1148 | -7.01231 | -42.35242 | 2025-07-28 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3ddba449-0ddc-34b3-b00d-2a8877dc2410 | -7.49982 | -44.41869 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9e9fb74-5a96-3b64-9a40-3c16f2c9fed3 | -6.39488 | -43.37632 | 2025-07-28 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 250c44a9-c8b5-3d80-9e95-d2f8419c404c | -6.81771 | -44.14691 | 2025-07-28 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad1634bf-cafe-32f5-a8d7-4afab3e9a57d | -7.53218 | -44.39882 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9afc0db0-6318-3587-85ff-275c90b5f1f1 | -7.80557 | -46.57143 | 2025-07-28 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bff9f728-19d9-32d7-b7a3-28b5d99da0ca | -7.11101 | -44.91985 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c9038285-fc58-3f05-8e7f-ca956c5d3028 | -7.07743 | -44.92446 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 81d869a7-0703-3bfc-b807-0006ccdbe105 | -9.44771 | -43.19773 | 2025-07-28 03:47:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a883307a-18a0-329a-b569-7ba490cbb197 | -7.21011 | -44.16334 | 2025-07-28 03:47:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ddcb5dc-e5d9-36eb-8c61-69be47c12321 | -7.17742 | -43.94691 | 2025-07-28 03:47:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1115be55-9b24-305e-9b56-67cb5e263858 | -8.28668 | -45.00609 | 2025-07-28 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38ba572a-749a-3cf3-965c-ddf22885d8d4 | -7.4183 | -44.71119 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7dee04a-dd07-32fb-8594-37e19ad54c93 | -7.10614 | -44.91902 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bdc6fd18-4cc5-3c8c-8af7-9e7b5bf90876 | -7.21132 | -44.16272 | 2025-07-28 03:47:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2aa4a75c-6f4d-31d9-a42c-372a12bb8714 | -7.11206 | -44.9139 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 30ef377e-055b-3b15-94db-b8456e8ae7ea | -7.92182 | -43.10117 | 2025-07-28 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fb871459-4903-3279-9114-24b996ef5029 | -7.1072 | -44.91301 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d3ab7389-4aa0-3aa7-a835-692bc531d60d | -7.29604 | -43.07923 | 2025-07-28 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5e5e8fc8-339f-3e9b-af72-0ce693ae9089 | -7.38181 | -43.44296 | 2025-07-28 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7878c845-f47e-37a1-934d-0b47659dab40 | -6.38264 | -43.69154 | 2025-07-28 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a63bad50-e8d2-3a64-b9f1-76a756fef3c9 | -7.24325 | -45.39632 | 2025-07-28 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a764aa4-6a4a-36ca-90d0-92587574fc2b | -7.09553 | -44.9507 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 97fd40bd-532e-33fa-9bfd-05b577f646de | -6.85602 | -43.06208 | 2025-07-28 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README5.md)
