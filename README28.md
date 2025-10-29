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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f09e4b48-3f81-39af-8f09-760f38ceda95 | -3.24157 | -48.77605 | 2025-10-29 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 584d1ca7-fbe6-3ed3-9065-9445645c9fff | -4.89014 | -40.4444 | 2025-10-29 04:21:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 17653696-ec2d-3866-b285-d3ad7b634e6e | -2.42651 | -49.30292 | 2025-10-29 04:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5972f5ef-488c-357b-a8d3-bf2924b88f4e | -4.40513 | -43.12191 | 2025-10-29 04:21:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c559d8b5-6f64-35c2-9f36-f372e80cb8a2 | -4.5146 | -43.06929 | 2025-10-29 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9efd737b-5858-3ebe-aca9-bd816730c8be | -3.3286 | -54.08665 | 2025-10-29 04:21:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de9479e4-4e02-37ca-88fc-901dc32ae9bc | -4.8559 | -45.77512 | 2025-10-29 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1867886-b0d3-3da0-8192-c403d03dda94 | -2.63729 | -47.9537 | 2025-10-29 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9160626-e71d-3ade-933d-07531adb2c2e | -4.2163 | -50.07917 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ee7676d-74d9-356d-bc0b-1793cca98a03 | -3.71277 | -41.56426 | 2025-10-29 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 927bacd5-d0c1-3074-92d9-6ca0af7f4744 | -4.14427 | -43.35948 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 268f6065-84a0-31dd-be9b-9821a8753496 | -4.40569 | -43.11836 | 2025-10-29 04:21:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e195022-c6ba-33c2-9d99-da654d348112 | -3.03916 | -50.26751 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31a7573a-b046-3863-9acb-bec705df7dd4 | -4.66757 | -46.40107 | 2025-10-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21c27090-d16a-3ed4-bdeb-538a5e812317 | -3.35059 | -52.806 | 2025-10-29 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| cdb48517-eccc-3e4f-b8a3-e5c217e14c08 | -0.4252 | -52.04155 | 2025-10-29 04:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0cf431ab-3ecd-3c82-9a93-2265391f3549 | -4.08613 | -46.93769 | 2025-10-29 04:21:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5eaeaa7-f720-3db3-8c3c-80b3454ce310 | -3.14532 | -49.21445 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 653b5e4e-0884-3f64-83c1-4bd80304b55d | -4.86267 | -45.77617 | 2025-10-29 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ee34dcf-36a8-3204-a21e-b16a972dae6f | -2.41756 | -49.30536 | 2025-10-29 04:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5bc795f6-5736-3711-afc8-eed716cb21c2 | -3.23681 | -50.65109 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8431f4b-7e0b-3035-abab-61572a6fdc58 | -2.48306 | -48.36665 | 2025-10-29 04:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7518edbf-5075-3624-b104-07ad6ad4494a | -4.35935 | -47.23592 | 2025-10-29 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec5f1d50-6133-3a85-a3ce-316cd7faad87 | -4.25099 | -48.57219 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74bf8705-4013-34fe-8705-af75b0183b34 | -5.53399 | -41.7122 | 2025-10-29 04:21:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e0c327f-c493-366b-85f6-80e1ccc0d29b | -4.69397 | -45.99877 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0879b5cb-2969-366a-9c89-f761b5571786 | -4.0293 | -50.45161 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4085ee0e-ace4-36a1-a498-5104b0a70ea1 | -3.59346 | -43.60909 | 2025-10-29 04:21:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 915f51fc-acbf-3dce-a87a-931e3e8bb052 | -4.79501 | -43.42807 | 2025-10-29 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 266a15a2-38e0-36de-a973-464b7081ce76 | -2.96285 | -48.59533 | 2025-10-29 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 705e92cb-0340-32b0-abcc-7468af2bff53 | -2.76394 | -45.40018 | 2025-10-29 04:21:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f1b0a8e4-394a-3c00-ab86-2902b2224e0d | -1.49199 | -47.80716 | 2025-10-29 04:21:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf72fa73-28fb-39b8-b8ed-85d60f5a4c84 | -4.65669 | -46.57809 | 2025-10-29 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e3621fa-1511-34ef-a0d7-8878597ac312 | -4.67671 | -43.23959 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 044c47ce-41b2-3d1d-a464-3a4946f76f77 | -4.1482 | -50.68647 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07540dd1-3f31-36d7-b4dd-8cd7440d554a | -2.807 | -48.66633 | 2025-10-29 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db8af044-9b95-3cc5-97bd-6cefafa2adf5 | -3.16048 | -49.25065 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c68e5b6-473b-3c3b-9ec9-e6acdc9e1802 | -4.21366 | -50.09525 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a33a3d5-a793-3db4-9921-580f039d34fd | -3.88133 | -44.72145 | 2025-10-29 04:21:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| da518874-4da7-3492-bccd-d308583c4600 | -4.14761 | -43.36 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33d0873c-7ef6-35c0-9db2-005a10f7252d | -3.58401 | -41.04515 | 2025-10-29 04:21:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ababee48-9beb-3949-934b-6e305b3307ea | -4.70423 | -46.10947 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33c6d031-3881-3143-9704-d05539322ea0 | -2.76452 | -45.39657 | 2025-10-29 04:21:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3f617a1f-7ce2-348a-a6f5-13e939506166 | -4.01622 | -48.98948 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a915026-0f7d-3367-90f4-94a2c9f2069c | -4.80018 | -42.96669 | 2025-10-29 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af245854-eb22-3d29-a916-331ba13a7ec2 | -1.49125 | -47.8119 | 2025-10-29 04:21:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a9b3d73e-8091-3742-8ba3-3e50bb8ce8bb | -4.85929 | -45.77565 | 2025-10-29 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 705da605-cbd7-391f-8b7a-335998990f18 | -2.6358 | -47.96302 | 2025-10-29 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 231183be-52b6-30ad-9a82-62b8fbb2663a | -5.53461 | -41.70818 | 2025-10-29 04:21:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 17363cbb-5b62-3e26-958b-c44fd170c1df | -4.80609 | -46.60909 | 2025-10-29 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cef981b-f5e7-36c4-9be2-2b62d8903073 | -2.77354 | -45.4054 | 2025-10-29 04:21:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36e6c63e-15cc-3b97-9fdc-8c914e25213a | -4.7303 | -44.44729 | 2025-10-29 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e44eb3ad-5d25-3aad-bd82-942dd9f04e88 | -3.80149 | -43.32081 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 775b7930-7722-37b4-972f-6bffc923ee0b | -3.11497 | -51.21192 | 2025-10-29 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48156b2c-dc93-35cf-bfac-a44e85175f40 | -3.15637 | -49.24997 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d54bbc1-a065-3e55-a362-9c0b2f349c9d | -4.48289 | -43.43713 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 339cd012-05d8-34a3-b255-80315a062aad | -3.99818 | -43.65829 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cef809d-b139-393a-ab5c-f30eac8ac498 | -2.41817 | -49.30157 | 2025-10-29 04:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f40224fc-7cbd-342f-83f1-f10e6e24668a | -3.66978 | -44.19882 | 2025-10-29 04:21:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ab83d0a-38cf-3dad-868e-694ac3dd1f15 | -4.49889 | -46.4565 | 2025-10-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfc7af70-1dad-3879-b79f-7f80ba838f16 | -4.4064 | -43.12177 | 2025-10-29 04:21:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f004178d-63c3-3e62-96b6-4e43c17a1b82 | -3.42895 | -50.1151 | 2025-10-29 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c36ab26-c63e-35a9-9909-0798f8c2af84 | -4.08113 | -42.91865 | 2025-10-29 04:21:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f8c3dee-c76c-3762-8da5-550f52a27c1d | -4.2247 | -48.56276 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2168190-9528-3003-8b8a-867c1bea8f99 | -4.08903 | -46.94228 | 2025-10-29 04:21:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56f280d7-853d-3640-baeb-14a89734cf21 | -4.69085 | -41.85481 | 2025-10-29 04:21:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e8a1332c-af85-31b3-9817-c8eae8634cd9 | -4.21268 | -50.07452 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0aaed7c4-1642-36a5-bb2d-15569c29afd2 | -3.32168 | -52.6278 | 2025-10-29 04:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ad66b10-429c-3056-94d9-4126771f4b37 | -3.59708 | -47.51688 | 2025-10-29 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ceaee83c-93b8-3bdd-8f48-e481da47c3ac | -3.35531 | -52.80993 | 2025-10-29 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aeeb3d17-f263-3634-ae28-026c959e450c | -4.08677 | -46.9337 | 2025-10-29 04:21:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3c5da6e0-a27d-35dd-8a8e-9cd199c4ff4b | -3.73727 | -51.34665 | 2025-10-29 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db8a0639-fcc2-3066-a96a-1af9dbaf2303 | -2.2028 | -51.3695 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd7e6c7c-820d-3060-aa3b-7689301bcc3b | -3.03845 | -50.27174 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 757afaf4-0133-3369-b910-87f825956ce1 | -3.66314 | -44.19778 | 2025-10-29 04:21:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99970a04-5b8d-3216-a838-3fa69ac24e75 | -5.56133 | -42.17126 | 2025-10-29 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6fa6f778-3bdc-3817-a67d-a8addb739bc1 | -3.89356 | -40.80249 | 2025-10-29 04:21:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9a1966b6-b19f-3044-a388-4e249b2cb362 | -5.09624 | -42.47561 | 2025-10-29 04:21:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 19ad4e45-3340-3208-a5cf-c0a5bb98148d | -4.85987 | -45.77205 | 2025-10-29 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0679d231-38fa-3ac8-9fbb-defcbcf8c6e8 | -4.61407 | -46.59876 | 2025-10-29 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e02820c9-1619-3318-8f39-aec07636ff66 | -4.2107 | -50.08655 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 3cd7487d-cc01-3bf1-bce1-3f72ebfbeac5 | -3.60207 | -48.98944 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d247bcc-334e-33d5-9cf6-d089b4db60d0 | -5.90176 | -37.82205 | 2025-10-29 04:21:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 75645547-b33e-34c0-a86e-1028c8fc3d29 | -4.20841 | -50.07381 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fb4f3b4-f1ee-3159-a1db-3b1748297e53 | -4.66351 | -46.40427 | 2025-10-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c69ee60-9d08-3ccd-a10c-af1554370684 | -4.65742 | -42.51584 | 2025-10-29 04:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 00e54c03-7060-3dd0-809d-ddc1ba1a7a6b | -3.59391 | -50.39423 | 2025-10-29 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3f70224-6c90-3608-8527-f762b0a5892c | -4.69339 | -46.00238 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8f88bad-8205-399e-b2d3-642383aadc84 | -3.72567 | -41.57423 | 2025-10-29 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 49f98e15-493e-392a-b894-be03d79006a1 | -4.20576 | -50.08987 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 754a913d-2b78-3eb8-97c1-98efe26bd945 | -4.00935 | -43.28822 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a176407-6ecf-36b4-9fec-88822a0fa2bc | -4.0099 | -43.28471 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 700fc156-c807-3dc3-9f0e-7c9fd15d1242 | -2.22221 | -48.3746 | 2025-10-29 04:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b5896b6-d781-3e1b-a937-30f1bdc7ef63 | -5.08853 | -44.81261 | 2025-10-29 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3725bebf-b478-385e-8e2d-4e4302f26746 | -4.40695 | -43.11822 | 2025-10-29 04:21:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7b6328f-71e2-3089-8462-24249fee6852 | -5.02757 | -44.81013 | 2025-10-29 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b816b353-711e-36ef-800b-6514124c17c3 | -4.48865 | -45.20451 | 2025-10-29 04:21:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b6d28e1-9442-34a5-8926-993a51bdcf32 | -3.37646 | -49.96538 | 2025-10-29 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 943f49e1-f845-37ae-8653-c4ff1961771d | -3.70563 | -47.65223 | 2025-10-29 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe83be44-164c-34a3-b463-d5a7ce04ac68 | -5.63925 | -41.09414 | 2025-10-29 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
