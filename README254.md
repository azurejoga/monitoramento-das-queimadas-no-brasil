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

## Dados Diários - Página 254

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| deba6685-863b-3098-81d7-eb0ce97c40f4 | -5.9833 | -40.961 | 2026-10-07 19:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 8a8e0cd2-c160-3119-ba2c-118a22b9fa60 | -3.2957 | -49.1202 | 2026-10-07 19:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 53454ee4-2fdf-339f-b34a-6e9d90a8531d | -0.5993 | -49.4293 | 2026-10-07 19:00:00 | GOES-19 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| bbbc67e6-fe67-337c-8291-23d12e75fbe4 | -1.1094 | -54.1401 | 2026-10-07 19:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| bc31c15e-03f5-3486-a38e-77886e614a5e | -3.6786 | -54.5115 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| af89d3ff-d4a5-3203-81e7-804dff1b0ac0 | -5.7374 | -45.176 | 2026-10-07 19:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 289.9 |
| 4574342b-b74a-3050-bb21-089acecba66a | -4.0947 | -52.0635 | 2026-10-07 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 42840b14-61ce-353c-9a9e-e429c073839a | -6.1937 | -42.4785 | 2026-10-07 19:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 685d29d2-9851-3b5c-ac54-2c53150d37aa | -4.2744 | -46.3846 | 2026-10-07 19:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 19984f15-002f-33ad-87d7-c590225e58d6 | -1.091 | -54.1603 | 2026-10-07 19:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| b6fc65c4-e270-391a-849b-9dc4df2860af | -3.8037 | -47.4839 | 2026-10-07 19:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 19c4aed0-087e-320a-9351-b4ba5b2fc9ff | -9.9596 | -43.5045 | 2026-10-07 19:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| b9202545-3b57-3308-945c-64dd53156056 | -12.1431 | -43.323 | 2026-10-07 19:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 1b9c51b1-ebf8-3e86-8665-118e15c4a0ef | -9.2451 | -45.6692 | 2026-10-07 19:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| bece8c86-37fa-3ac3-ad99-39163cac7041 | -3.5875 | -54.3138 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 08e0b41b-e198-397b-8828-0ecdca61a358 | -5.7659 | -42.0389 | 2026-10-07 19:00:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| d38179f8-e70d-3264-bd3e-a872dc16f611 | -6.6753 | -44.9674 | 2026-10-07 19:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 3734edf0-a421-3b14-bb50-826068e00f5f | -4.286 | -50.7707 | 2026-10-07 19:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 01267b10-ffa3-3abb-8c8d-48bd45df6970 | -1.8011 | -57.0967 | 2026-10-07 19:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 1f8a4b73-cff4-37eb-be34-84542c5caa5c | -3.1951 | -42.9538 | 2026-10-07 19:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 288.3 |
| 876e4ec8-5641-398c-a343-1cdb81ea0c0a | -5.9412 | -45.3874 | 2026-10-07 19:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 55822ae3-21ce-3e1d-a011-3f0b4e5c7160 | -3.2956 | -49.1415 | 2026-10-07 19:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| eb66dea6-4266-3d0a-a4c1-0dfede265647 | -1.8794 | -54.3912 | 2026-10-07 19:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 463f37e0-ce9c-3c78-9eb0-fa971ae4dd58 | -1.801 | -57.1161 | 2026-10-07 19:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 181.7 |
| 544b2354-f65a-3bc9-bb17-a86f13784549 | 2.1267 | -50.8371 | 2026-10-07 19:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8fe28b88-6788-3f53-8e3b-bc8977cda4ee | -11.6374 | -43.664 | 2026-10-07 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 6d235745-829c-3e9e-b7ef-54764b8bd55f | -13.3671 | -43.8742 | 2026-10-07 19:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 249.6 |
| 473527a6-2771-36d2-9418-afb34ac54cab | -5.8966 | -53.4975 | 2026-10-07 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d219d67a-f4cc-354b-a344-9b48cb659819 | -9.8061 | -64.9979 | 2026-10-07 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| fc015713-28dd-3f98-873f-3652bab8a346 | -9.0407 | -65.9215 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 168.7 |
| 2e135222-4363-32f6-8007-74f0ce997e18 | -5.4771 | -42.8427 | 2026-10-07 19:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 03e6943d-4316-3cd7-bca9-13882451d3ab | -3.8081 | -40.4608 | 2026-10-07 19:00:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 66cf72b5-e616-3344-bfbf-e27f69612990 | -3.6603 | -54.512 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 2c769a40-60b6-36b7-b446-2f04762ae917 | -9.0591 | -65.9396 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 140.7 |
| f761eac6-4aad-3311-9735-56476a6785e5 | -6.1431 | -47.9214 | 2026-10-07 19:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d3f56c85-e0a4-3f9b-a9d9-b7274ca4495e | -5.9699 | -53.5953 | 2026-10-07 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 29205a04-42ef-35dc-a2c2-0f4cdc61e9f2 | -2.6859 | -49.0325 | 2026-10-07 19:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f9f1f949-8899-3f48-8cfe-15d620bff63b | -5.0325 | -49.7687 | 2026-10-07 19:00:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 64bd03c8-2e72-3cbf-b8a4-ce7e65018a80 | -11.7335 | -43.649 | 2026-10-07 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 5c8f4694-0835-37ac-8298-6db56626828a | -6.2108 | -40.8187 | 2026-10-07 19:00:00 | GOES-19 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 2f1822ec-e475-3281-b6dc-5c741ae8fc8a | 1.7672 | -55.5463 | 2026-10-07 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 6994bff5-4768-39d4-9aab-ef038275e5d1 | -11.1122 | -47.6218 | 2026-10-07 19:00:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 530bd686-8af8-3117-b65a-b08bddec5d75 | -3.891 | -52.2147 | 2026-10-07 19:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 32e5f32a-e82a-30f0-8bb3-8084776870ef | -3.73 | -55.486 | 2026-10-07 19:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 6342e300-81f9-3374-8fb4-2dc312c5e41a | -5.2899 | -50.0937 | 2026-10-07 19:00:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1eb5b050-1738-356c-8bd6-b8bce0919d05 | -4.2112 | -44.6124 | 2026-10-07 19:00:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 066f6a38-28cc-3f4d-bffe-2b37fcb6320a | -2.7044 | -49.032 | 2026-10-07 19:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 82317f8d-c68c-3557-8ebd-d0e74cdfcff9 | -9.3395 | -65.4451 | 2026-10-07 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e06ef5e5-28d6-3542-bb75-a2170190fc79 | -5.496 | -42.8178 | 2026-10-07 19:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| ea52d8b5-2cd4-3e05-a07d-26ffb535c571 | -3.3452 | -50.4707 | 2026-10-07 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 752bf008-6763-34cf-9deb-b00060dc72f8 | -3.1787 | -50.5597 | 2026-10-07 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 3db8d07c-e6c6-3a26-b6d8-2539e6dbb413 | -9.2314 | -46.6831 | 2026-10-07 19:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 244.3 |
| caffb6f4-9c60-39f2-a2b3-1f087f56c9b8 | -11.7139 | -43.6757 | 2026-10-07 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c75ccee1-e368-3cf2-a68f-714a905c6dce | -8.6036 | -47.1478 | 2026-10-07 19:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 7e5acc36-d5f1-3436-a42b-c937053d5300 | -8.537 | -66.9764 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 44cac20d-fb1a-3b07-b5fe-04a06932ae2b | -1.4771 | -53.6134 | 2026-10-07 19:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| e2840aa8-2f0c-3980-a2f8-bc9e7c55d385 | -5.5148 | -42.8164 | 2026-10-07 19:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 6b451cea-51e5-3202-8c18-c630250cb4c6 | -3.4763 | -50.0673 | 2026-10-07 19:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 69847d72-6ee6-375b-b14c-58de5cc308e7 | -9.9585 | -43.5752 | 2026-10-07 19:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 2ada5774-893c-3a66-8e7e-195e10564bdf | -6.0447 | -53.49 | 2026-10-07 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| c3397bf2-e67d-3edd-83d3-27a506e05832 | -9.9398 | -43.5542 | 2026-10-07 19:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 2aeda7a4-949a-3858-8220-094238f95b79 | -3.1697 | -58.6437 | 2026-10-07 19:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 3f537fa0-52ae-3adf-a9ab-ed257c627b69 | -3.476 | -54.6372 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8c992714-0686-3d0f-a2cd-0d7b09f0ddc4 | -3.1697 | -58.6244 | 2026-10-07 19:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 2ba5334c-6964-3f18-b5e4-973d2fc4e765 | -6.6784 | -52.9664 | 2026-10-07 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| d0886b2b-d75d-3c49-b31f-645d00d9f4d9 | -11.7143 | -43.652 | 2026-10-07 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 58a51b58-a271-34d8-8443-2fd0841b98f0 | -9.2125 | -46.6851 | 2026-10-07 19:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 144d33e0-dafe-3957-b3dd-309247faa938 | -8.8573 | -71.4625 | 2026-10-07 19:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 94.0 |
| aaf9e6a6-8bd7-3d1d-923e-4a6bee73853e | -3.2137 | -42.953 | 2026-10-07 19:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 218.5 |
| 27a22695-0159-30a8-9bb8-08d76cf248a3 | -3.1971 | -50.5801 | 2026-10-07 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 2cd464f6-4af3-3176-b0ca-7f477ae5d162 | -11.8508 | -43.5361 | 2026-10-07 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 8635acce-3f87-36f2-832c-4968c11e5d36 | -6.3541 | -43.3349 | 2026-10-07 19:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| d37c33ed-d8ef-3d2a-bdfe-1ee1afc88368 | -5.9835 | -40.9367 | 2026-10-07 19:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 185.2 |
| 6e2b590b-0222-3881-abbe-2432f58e86df | -5.2461 | -48.3887 | 2026-10-07 19:00:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 103.1 |
| aefc728e-ce9c-30b3-a1e9-a9c7784c2e58 | -7.4697 | -42.8315 | 2026-10-07 19:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 241.7 |
| 25fb0bbf-5f96-368b-b9b6-5b49d06c36cf | -2.0447 | -54.3085 | 2026-10-07 19:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9c7ccd1d-c4ac-3f06-a3a0-89d37b6c1a4c | -2.4942 | -58.0768 | 2026-10-07 19:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 4d9d91e7-a46e-3716-b6bc-b140f8ece7ed | -8.5367 | -67.032 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 4b8bb6b1-aabc-3c72-bb4a-836947a02842 | -6.1502 | -39.4158 | 2026-10-07 19:00:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 100.4 |
| 86562ddc-6175-3d7d-a958-1f438f0a27d2 | -11.8503 | -43.5598 | 2026-10-07 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 8989fd76-252d-3881-bcc1-3c2107f9acc5 | -9.9787 | -43.502 | 2026-10-07 19:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| f8ff5a71-7a29-30b3-8d9a-08a0d56b365f | -6.4395 | -52.6727 | 2026-10-07 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 47ec4cf8-ddfe-3c66-85c4-d7928ab36ecf | -5.4835 | -44.2592 | 2026-10-07 19:00:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 0163b6e9-9d25-3054-a816-675c23ebe50b | -3.6049 | -54.5736 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 19b7b27a-079b-304f-a04d-9160b88f271e | -7.6767 | -72.3142 | 2026-10-07 19:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 128.5 |
| c588ff66-82f7-3795-a2b9-5ee0a9d05f0c | -8.9082 | -49.986 | 2026-10-07 19:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 78198790-fa3f-3e89-8f9b-e6d0384966c3 | -2.5314 | -57.8052 | 2026-10-07 19:00:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 172.0 |
| ac3757ab-8171-3de2-9e76-f012b87ba99c | -3.2398 | -53.8813 | 2026-10-07 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ec1d6240-a2ed-32a7-9f6e-6a03b3d6c73a | -3.8627 | -50.4106 | 2026-10-07 19:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 69ed1688-a38c-38d7-a202-a9249ab1703d | -7.6767 | -72.296 | 2026-10-07 19:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 375ec1ce-00d8-39b8-93b3-ffcc4c57afd0 | -8.2181 | -46.362 | 2026-10-07 19:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d0d4340b-fdc1-3ec7-998f-f6c1ab5bb362 | -6.7528 | -52.9417 | 2026-10-07 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 997f9438-6510-3424-bcf0-65036bce4131 | -5.7376 | -45.1533 | 2026-10-07 19:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1038.6 |
| b62640c5-3879-3298-b37e-692a13d13747 | -3.6931 | -40.8572 | 2026-10-07 19:00:00 | GOES-19 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 108.3 |
| d1c004c0-f1e2-3cf0-a863-170429575a5c | -3.8786 | -44.1265 | 2026-10-07 19:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 43540bef-a564-3d9b-a8ba-ac2114507b8f | -3.3133 | -53.8793 | 2026-10-07 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| d36cf007-c654-35f8-8df9-0219204decd7 | -2.9271 | -53.9295 | 2026-10-07 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| e8ab6c69-5148-39cd-8864-9780742ec1ac | -6.8955 | -43.6601 | 2026-10-07 19:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 69a39fa1-d466-3853-88af-2f1ace717887 | -7.3935 | -46.2144 | 2026-10-07 19:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 5fb8686c-8929-3727-a093-304b1817eaaf | -9.2122 | -46.7075 | 2026-10-07 19:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |


[Clique aqui para ver as próximas entradas](README255.md)
