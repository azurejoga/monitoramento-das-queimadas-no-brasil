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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb98411c-ebc2-353a-8c55-38d108edee80 | -5.39119 | -45.91298 | 2025-10-17 04:49:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c793ba9-cd82-37f8-9d0b-17c28fa2513f | -7.02905 | -41.82085 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7cadd528-f9cf-3335-9f1b-ecefcad17c53 | -5.14552 | -46.05636 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1afd64d7-5034-3dfb-b079-b392a81fda89 | -2.74017 | -48.30846 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19895da2-c490-3e69-8179-c1c19345c33b | -5.2377 | -49.22657 | 2025-10-17 04:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c791686-9681-33b3-a984-ce835643ce87 | -3.59186 | -42.83791 | 2025-10-17 04:49:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed7f46f9-12bf-3e74-a34d-8297d07b37b6 | -6.20915 | -41.76307 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f1d35e05-cb54-3810-b791-2be21534b771 | -7.17756 | -42.35939 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 97988358-cb73-3027-ae36-1f99263ca78e | -4.404 | -50.49496 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a753bd1-eba6-3a84-a406-56ad0e0a7131 | -5.86116 | -47.5801 | 2025-10-17 04:49:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a51e1203-ff34-35cc-a348-5a2876df9833 | -7.46004 | -42.15873 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d50535d-1b71-3090-af2e-ea86b3703827 | -6.20906 | -41.74987 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1c303b95-c584-3587-a1e5-b4cb30d1cd6d | -4.41188 | -43.39303 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| cd92a492-6bfa-3fe2-b284-2830363191b1 | -7.47031 | -42.16376 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4d2ca893-ed00-317a-8ab3-006b61ea6600 | -3.24557 | -45.97111 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| d49345cf-e06b-3f74-86b7-3f0d336dee69 | -6.53082 | -55.0516 | 2025-10-17 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 301b508e-9591-357b-b41c-842d2a3889bb | -7.35806 | -44.06117 | 2025-10-17 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 631628bf-652e-35ca-9cae-f056233ea806 | -4.95362 | -49.5743 | 2025-10-17 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b771067-fa7c-30a1-84b8-349b33310f1a | -8.10191 | -44.98297 | 2025-10-17 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2446d42e-aaf9-3be8-a020-6a8df9d92f2d | -3.62613 | -42.77279 | 2025-10-17 04:49:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a53f9779-4df3-364a-8c75-e2904657a24f | -6.70442 | -44.3924 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed2cd855-2f31-3498-9a0e-54fc3b5dff43 | -5.35983 | -47.30078 | 2025-10-17 04:49:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cebe1ed-b6a8-3c52-a5df-f0fe4c2f8248 | -4.54365 | -59.92684 | 2025-10-17 04:49:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 333eb67f-16a1-32c1-b80a-6bb2365c13fb | -4.412 | -48.949 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddd18c42-7e30-3185-af5d-4cfe24d0448e | -6.07497 | -49.40581 | 2025-10-17 04:49:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf44a220-a617-365d-910e-e937ed91f282 | -4.22078 | -48.36365 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f4e76a3-c27d-30f6-87a0-d2f306ce2b17 | -6.8338 | -42.4178 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 601d907e-d9e0-3684-abfb-0e1ef29339c2 | -7.67814 | -44.6257 | 2025-10-17 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 383e400a-b687-3a06-bb7b-57c89b7a339d | -5.90839 | -44.74693 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 44ec18e4-e43d-3123-ae0f-9e1199ab24ed | -5.87772 | -44.83632 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07814571-0200-35b6-a497-a6f23162b71a | -3.82015 | -52.34236 | 2025-10-17 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce78fc9a-a804-3ebd-881a-87584ef9c01c | -6.37682 | -41.47542 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c1a15432-3f9f-391e-8492-97a31ccadaf5 | -1.18313 | -55.66714 | 2025-10-17 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 188d8f61-0071-3459-9722-b1ed661a0f50 | -5.89022 | -44.74855 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8091bfb8-714b-383b-b104-f89de49f0fbf | -7.041 | -42.73236 | 2025-10-17 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a82e62e6-dc67-3523-bb35-7dae0f10a1d5 | -4.41043 | -43.4029 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dd5ea621-8961-3922-ba09-5093c0a6536a | -7.16445 | -44.99736 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66b6a368-b74d-3856-b544-f1d4cfa25673 | -4.01492 | -48.96742 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79c8496d-42b4-3c11-a674-543624f89ce1 | -7.11682 | -44.73964 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f1be8fa-e6f5-375e-9ac2-a5cedb9e54a5 | -5.84567 | -43.88317 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae07535d-d3a9-3a48-9414-26892f1c2667 | -6.7457 | -44.36786 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8345d2da-26fd-3e31-a0a4-61215b5725e2 | -7.84263 | -45.45583 | 2025-10-17 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3f91698-96b7-32aa-bd31-600fe786cd5d | -2.86688 | -50.73876 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5515fd42-49d1-32a1-832a-89b059e4d688 | -3.87622 | -51.94734 | 2025-10-17 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2df8c466-99ec-3283-8c70-bf91354e68a4 | -6.20216 | -41.75938 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a301267f-3941-359e-8fe5-d4210f2dde56 | -5.09095 | -45.43157 | 2025-10-17 04:49:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 994f7f85-694e-34a5-b543-fb1d9330e957 | -5.17713 | -42.929 | 2025-10-17 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ab887c7-48e4-3498-bc71-8d17f7ad36ab | -7.32526 | -44.15683 | 2025-10-17 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f68ddbb1-b4e3-3e4d-8050-d1c336afc03a | -5.87977 | -44.76184 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75ddaef3-f918-3cae-a6d5-2636cf476973 | -4.93695 | -48.55441 | 2025-10-17 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d972296-a03c-3d9d-abf9-93e2ed7bd92b | -5.41443 | -44.2481 | 2025-10-17 04:49:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0c6c123-f9b4-3f35-baed-2528c7ae9151 | -6.39857 | -46.87915 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 124ed24c-6bf9-34e1-95d0-1dc4dee938b2 | -3.82366 | -52.07999 | 2025-10-17 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bad7bab-3269-3995-bbe0-9c28fd964772 | -3.52439 | -50.30732 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af4a5e7d-826f-38f0-94c0-3dd5928f7e0a | -5.86827 | -41.23529 | 2025-10-17 04:49:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 648780be-1fac-3933-aca6-15ca5fd3d416 | -8.25444 | -43.33996 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3b0a3ee-cb8a-34a9-8b01-d7430491e73f | -7.17539 | -46.93842 | 2025-10-17 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7ee701f-c3e9-3bc0-9897-e6fe97d82edd | -6.99531 | -39.2282 | 2025-10-17 04:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f7317cd3-f9a5-37a8-9db0-4d93b398c3f4 | -6.32425 | -40.94414 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1224e80d-b0bf-37e6-aa58-f916d02bbc85 | -3.23855 | -45.96501 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d4ac67a5-1170-378b-991b-f05897ce4af5 | -8.24059 | -44.01648 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1a622b8-870d-3819-85da-87cde791620d | -6.22397 | -47.03703 | 2025-10-17 04:49:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 486d28f9-a600-33b9-be76-16ab8a846b08 | -6.21329 | -47.88289 | 2025-10-17 04:49:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9380890-5975-3a8f-a249-79f94b0ff195 | -8.30503 | -43.41724 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ba35303d-5749-3db2-b64a-41ebb55f21e6 | -5.88542 | -44.75401 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b49b22a6-9721-39f9-9b97-c0f05f84b7b2 | -3.24167 | -45.97052 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 64571b27-6e3d-32d6-9a78-61d023fc1c8a | -2.29614 | -47.99295 | 2025-10-17 04:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac7e9baa-ede9-34c3-8cbc-62c9f0ebaa35 | -6.35249 | -45.48426 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2024fff5-8ccc-35ca-93d7-d53f62f16ec1 | -6.70196 | -44.37756 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2645a08f-c39a-378d-9801-07b27ca9d925 | -8.24943 | -44.02289 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12955fca-c31e-3a81-a3e1-2d06d17a54b0 | -6.76352 | -42.38409 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 70594bc9-09bb-32c9-aee6-73d772f5b358 | -7.8997 | -44.98197 | 2025-10-17 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b38701c4-be6b-333d-a8f9-06beee9d63a2 | -6.69539 | -40.86757 | 2025-10-17 04:49:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d97b318d-927f-3fe2-9fb7-163dc165e8dd | -2.87962 | -50.723 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67b5f573-c23c-3bf8-8ef3-2e8edb72b412 | -7.40858 | -44.75405 | 2025-10-17 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| beee1eb5-4ba1-3d9c-bb72-9ff165a542ca | -5.81042 | -42.33523 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 62c09d28-0c24-3d75-81e4-96a7cf2617d1 | -3.50369 | -52.48878 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 56659104-5f37-3dbd-907c-3db1200a6e7e | -5.39401 | -50.48362 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5ed2995-d542-3f5b-b4a5-b0f33f80be6d | -8.20332 | -43.96887 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e13a832-e9ea-3918-8bc8-9b4105e657d5 | -5.16622 | -45.21466 | 2025-10-17 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3ac8b5a-f354-3474-878c-940a387b0779 | -4.66586 | -49.73652 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ca678e1-1aec-321b-806c-ec501347a445 | -6.28804 | -45.51004 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9b741cc-40c7-302b-bdd2-8e0af0f59eb9 | -6.74942 | -42.3705 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c6e8a27e-978a-31d1-ad0f-22afcc05cc50 | -3.49812 | -51.60241 | 2025-10-17 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4305ca5c-cb3a-36d4-8e7d-d989e074fc1e | -5.85742 | -42.33948 | 2025-10-17 04:49:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ff5c0bba-21d3-33ec-9924-7978c9152945 | -4.3305 | -47.88982 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0888bc5-fb90-3f92-af97-bc3284f6e14b | -7.04433 | -46.37798 | 2025-10-17 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b86ae798-c0d7-347a-a2ff-e8242a4640fc | -4.40643 | -43.39732 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d49c4112-15bb-332b-ae83-86453b442034 | -3.24179 | -45.97258 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e789d860-4ffd-3eb3-81f4-d382f2214cf7 | -7.66729 | -45.63734 | 2025-10-17 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf74e9b6-c529-3432-aac9-c6581ce76a5e | -6.6933 | -44.27759 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 981563ac-3337-3fba-bb4b-b4a6f0a22f2e | -4.74233 | -44.94272 | 2025-10-17 04:49:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2d09fbec-2db7-39d2-8f24-3d7af0393caf | -1.49169 | -47.81079 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 635736f1-7d39-312c-af9b-0a7ace3e9807 | -5.71617 | -44.50948 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4c38ecf-7f61-386b-a555-9c4a90678b84 | -5.19771 | -47.4856 | 2025-10-17 04:49:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f0b6e11-5d41-3fc7-b332-f0a16763a719 | -2.5955 | -51.34468 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f844827-8be3-318f-9ffd-f06be6d3a060 | -5.09149 | -45.42793 | 2025-10-17 04:49:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7943a654-dff4-3fb9-98fc-ed1183f68b39 | -7.45468 | -42.15788 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 512f7acc-734c-31bf-a7f5-262fe9ef6d4b | -7.90094 | -44.98354 | 2025-10-17 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2aa3a6cf-48ac-3fe4-a002-36c7fb53be1f | -7.18327 | -41.68243 | 2025-10-17 04:49:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README76.md)
