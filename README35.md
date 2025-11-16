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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bec2c63f-7a57-38b7-8081-58fc24217d65 | -12.40393 | -47.55447 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af4c399f-9e8e-3a8f-bb07-9a4e991996ab | -9.70939 | -48.90018 | 2025-11-16 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49556127-267c-3e9d-81f7-4f3e849ae58f | -11.5722 | -42.4271 | 2025-11-16 04:08:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fb4f8806-4431-358d-a559-5257d7099105 | -10.00006 | -44.78106 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4237d477-5377-3b4e-a650-537a6d152b0c | -12.05936 | -48.21735 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0f7ae24d-ddf3-3fc9-842d-45a5116c9d97 | -9.74568 | -43.95211 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f14ac3aa-914f-3ba5-b30a-334c79042326 | -8.06059 | -45.66142 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bc2e681-fa9b-36ca-901b-7bb57cdacacd | -9.15901 | -48.05481 | 2025-11-16 04:08:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e41a7a7-8c43-39a2-89e5-77fba0e5fe2d | -6.54142 | -42.20455 | 2025-11-16 04:08:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 49785680-30ff-3d18-b88d-c1fcd1a07b29 | -7.24496 | -42.56843 | 2025-11-16 04:08:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4cbe115f-ac3a-3e55-be53-d5028a278048 | -10.06567 | -45.51938 | 2025-11-16 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdd22093-652d-3fe9-bb31-ccfa0eeafd8d | -6.07512 | -41.5451 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a2c3a94-01ee-3aa0-b987-c2b71976e298 | -6.31926 | -41.82769 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 27f9be6c-ba14-348e-ac3e-c81155020b56 | -6.69995 | -44.14627 | 2025-11-16 04:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a2708da-162e-3232-899c-edece009e50a | -12.39888 | -48.09279 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 422bc40a-5271-347b-b798-dedf0b8a146c | -9.82695 | -47.08285 | 2025-11-16 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edd9644b-2cd6-36ef-9628-6e726bb78178 | -10.18295 | -44.50261 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3542e833-c92d-3cfb-b035-a0cce0df8465 | -11.84376 | -47.60309 | 2025-11-16 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08dcfd12-9035-3462-aca2-e34dddad41ae | -10.39232 | -49.04994 | 2025-11-16 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8f1accf-6cfe-34a7-8154-adcf7e50bb25 | -9.99787 | -44.77265 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16037871-71ba-38ad-80cb-40193d96ad6b | -6.13031 | -48.05177 | 2025-11-16 04:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ad819a0-7465-30e9-9149-d1d2d47bfd71 | -7.46268 | -42.54547 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 17e41a1c-4d77-3916-abdb-e19213cb13e2 | -10.12031 | -43.89704 | 2025-11-16 04:08:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f723cc63-4faa-3605-9d35-deb8dee1fb61 | -9.66366 | -43.90068 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 98b67458-27a4-3b16-aaa0-a325ba9191ad | -8.46046 | -45.13908 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37333370-0b37-34f5-8270-26448257c6b0 | -11.1053 | -44.80555 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc53e7d7-348b-3474-8a96-39ecdc659165 | -6.96024 | -39.55634 | 2025-11-16 04:08:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4954ae90-8257-3dac-bf36-ca265897b6c1 | -10.53875 | -47.92107 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37fa3604-f9c3-395b-b164-f2f87d8d8fdc | -11.82744 | -45.52776 | 2025-11-16 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1df56d3-c2ee-3d73-b98e-1ae79f27f346 | -12.38615 | -48.09414 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07d403a8-1c95-3522-9b49-51ec1c7a84a9 | -5.96282 | -43.74643 | 2025-11-16 04:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b19a2ed3-e21a-324a-9312-bda62d1bdb3f | -11.41221 | -43.32944 | 2025-11-16 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ec64768-57f2-3021-9fd1-b386c10aa8d2 | -6.81028 | -48.79189 | 2025-11-16 04:08:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 495ad4ae-4ad0-35f1-83ae-a83353599546 | -8.55411 | -47.78885 | 2025-11-16 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eadb7bb5-0c6d-34f8-b4a8-779222940d11 | -10.16577 | -44.49971 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 810d84d3-357d-39cc-a824-e58113fc5d12 | -5.70073 | -42.8679 | 2025-11-16 04:08:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 373660ee-25ff-3803-b9a8-68b02eccdb98 | -9.73713 | -43.96202 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 423f0092-9be0-3e1c-ad6f-47c2c8685001 | -9.84579 | -44.1811 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aa365d6-710c-3be9-9207-eaa64f520052 | -11.98205 | -44.97691 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70c32d57-45c9-326f-af75-dc289e73490f | -6.6761 | -42.04111 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 716c9386-d3d0-32f7-880a-18ff74b46d87 | -7.282 | -46.71405 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c1cd5f2-62d0-3c57-ab3e-43e0a0727319 | -5.29598 | -48.61629 | 2025-11-16 04:08:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 681f6650-19e1-3d08-8ec6-4a8321d76760 | -8.05973 | -43.10099 | 2025-11-16 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 6ed50a4e-88ca-355e-8eed-15d2c5473174 | -6.29128 | -41.72467 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.1 |
| df05c413-8b02-319a-ba71-ececf6e39174 | -6.25448 | -41.42183 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a8713fb2-b400-38dd-84ef-3cc47bfa2c84 | -6.31588 | -43.81253 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a57430ac-ac87-3591-b956-223f7ce190c4 | -11.15998 | -49.44176 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0439f06a-3308-33a5-8329-bd16df417a8f | -6.78048 | -43.54581 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4eff3c14-1eb3-3dfd-8daa-3cf2330a346a | -12.39733 | -47.56888 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1909006-6c0e-35ad-8487-0fc0faea3122 | -6.92894 | -39.6254 | 2025-11-16 04:08:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59397259-441c-3179-a9a9-18bb2e886c8e | -6.60141 | -44.2596 | 2025-11-16 04:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e147a55c-a04b-3167-82a2-de1b27601d02 | -12.68917 | -46.79552 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 110bbd50-7de7-3b7f-b33e-014d01da9ab3 | -4.49786 | -50.79471 | 2025-11-16 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69cbd659-9bb3-37d1-9577-58d108f6a338 | -9.0591 | -44.79137 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfc8db28-578c-3eff-89b3-7c273d774259 | -12.19585 | -49.61648 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d78fc8b1-d986-3e95-8ff8-4179ce970720 | -6.06536 | -41.64953 | 2025-11-16 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f910e0f2-39bd-33ab-b1bb-e1e7566a9e30 | -9.74552 | -43.95958 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 539cec2c-d229-3828-a623-9e40b8eed6e5 | -7.40738 | -40.06509 | 2025-11-16 04:08:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 61444044-df95-3a70-a24e-1cabca38483f | -9.72757 | -43.95662 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ee415028-04c0-3fae-b7b7-4a80fc614c4e | -6.86126 | -38.60788 | 2025-11-16 04:08:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c079cf1-d8e0-3d4f-b60e-640f36b60caf | -10.32304 | -44.26637 | 2025-11-16 04:08:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f4b19b0-cdae-3d8c-905a-578bb917c878 | -10.70769 | -44.05695 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09815612-5f89-352d-8420-8dbc187b701a | -7.21622 | -47.98389 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9069ee7-2e23-39cc-b41e-762800641f91 | -11.66443 | -48.46474 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 315e4fbe-967f-3d08-938c-0fe6e1b29c2b | -10.54976 | -48.00393 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b4e0f80-44b3-33da-82c5-937cd178081a | -10.84309 | -44.09332 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bb6226f-8849-38e1-9785-cc4b0d263495 | -11.70725 | -48.39969 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 732b82c6-5d05-3dfa-873c-b99d2bc9cd7c | -6.3165 | -41.82371 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3c44a758-9618-36a4-92d7-83cf81e1cb70 | -11.05816 | -45.15785 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 410c568a-3a8e-34ac-8478-5df0237c0475 | -6.37459 | -42.29242 | 2025-11-16 04:08:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a95b5551-109a-363a-9f7c-a4470fcf9f0a | -7.71707 | -47.30151 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ac2adf5-6d66-3594-88a3-00bed7636f9e | -5.74903 | -43.02057 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7516b5d2-8616-3c24-b7c8-b325a0458f53 | -11.91867 | -46.18894 | 2025-11-16 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffac73ac-52a9-3a2a-8171-3564e8528d9f | -6.95727 | -39.55612 | 2025-11-16 04:08:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52a39c57-b179-3b1d-a9de-abfa925f66c2 | -5.53761 | -49.60007 | 2025-11-16 04:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 247f7531-ea29-309b-907c-fdf08a3285f7 | -10.93855 | -44.02637 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20c0442c-8cfd-3801-948f-8d23893df60f | -7.21099 | -47.98468 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f73bd99-b8a3-3aa3-8b3b-40356ca6f861 | -10.39397 | -49.04823 | 2025-11-16 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6f6199b-4579-3717-9727-18cb14d2c40b | -7.27073 | -48.03246 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be602c07-120a-3a1e-8230-7602993ac29e | -6.71537 | -42.13626 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b00760e-0afc-3651-a508-bc845af7477f | -10.4329 | -44.41131 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2ca96c6-075f-3b3c-91c3-206f6285a26e | -11.84625 | -47.60535 | 2025-11-16 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b936e78-34b9-3982-a76d-ee8554c1f289 | -7.132 | -42.69822 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fded5a76-b1eb-3966-8a1f-1a90e5e8b0bb | -6.07358 | -41.619 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7a28a001-6792-329c-be41-a90a0c478ca7 | -6.86246 | -38.35677 | 2025-11-16 04:08:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d9410be-61f2-311a-bd23-40db4e17e911 | -10.84369 | -44.0897 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94f4db61-af2e-3283-af73-7d64496d6647 | -11.16454 | -47.45221 | 2025-11-16 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcefa76e-eaa1-38b1-9d3b-c83cc950d13f | -9.66306 | -43.90435 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c500ee99-8252-3f07-91a7-324152622b4f | -7.38881 | -45.51631 | 2025-11-16 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23168539-ad84-3f9e-aa42-eca445ea437e | -6.85841 | -42.83899 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3f311ce7-924f-325e-a50a-291f95691d4e | -11.6442 | -48.60385 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b49a5577-e105-3fc2-80c8-7654a9284e23 | -6.08079 | -41.65907 | 2025-11-16 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 24bbf1e0-9a77-3dc4-936b-5c394906f6cb | -7.01227 | -45.1626 | 2025-11-16 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c3a9278-11e6-32fa-aaa4-42a6e3f8c2df | -7.05406 | -39.63259 | 2025-11-16 04:08:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c144283b-4833-371d-bbb5-21e53efa3867 | -8.0625 | -43.10509 | 2025-11-16 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 2a2304e6-0e42-3777-bce3-678cc01cf0b4 | -5.99677 | -41.91152 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3125a1af-2f91-309b-ae43-582a3b126249 | -9.06262 | -44.79197 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41c653ea-63dc-3fab-badf-5a28d4bf4a4c | -7.07792 | -41.58371 | 2025-11-16 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 664d96dc-1e9e-38f4-a287-912865fe3f69 | -12.06409 | -48.21437 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7baac8d9-efed-3c92-8998-aaf47379bd26 | -6.08403 | -41.61711 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README36.md)
