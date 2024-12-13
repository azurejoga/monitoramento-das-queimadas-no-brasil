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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac73f727-5eae-3759-a3e7-8bc970569eff | -15.08827 | -48.93688 | 2024-12-13 12:44:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8fc47660-3155-397b-93aa-fc14d85a6db9 | -11.89378 | -46.93019 | 2024-12-13 12:44:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 058cd957-1ad1-3304-a1d3-5d1f6b20a44f | -8.33687 | -42.46491 | 2024-12-13 12:44:00 | TERRA_M-T | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 4acee5cb-7d38-30cf-87e9-88d1ebfa725e | -17.45956 | -49.8904 | 2024-12-13 12:44:00 | TERRA_M-T | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8eb363b2-d575-39c6-b42b-ecd2d6c4f470 | -8.47414 | -47.97534 | 2024-12-13 12:44:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1858c1c7-2e6f-3d5d-a679-066824df9d1d | -8.47542 | -47.96646 | 2024-12-13 12:44:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 24e42b14-a02f-32ee-8dc1-6a4ce0b2b3d8 | -12.40956 | -43.55579 | 2024-12-13 12:44:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9890cf26-4255-3826-a451-f2d501bb8e6c | -9.60258 | -47.69935 | 2024-12-13 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 997d345c-938d-3ed5-b58e-27aecd8f3b09 | -8.37721 | -48.45872 | 2024-12-13 12:44:00 | TERRA_M-T | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 35967478-1ad7-388b-b00c-c78344bb67bd | -8.31799 | -43.50266 | 2024-12-13 12:44:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4c1ea1c0-41fe-318a-9084-3992fe2e0caa | -7.24435 | -47.81071 | 2024-12-13 12:44:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| b1755345-774b-3f91-a133-819f29a4a77a | -13.68677 | -46.51743 | 2024-12-13 12:44:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 33987b7b-4881-3271-b15f-3725ec5ceb82 | -11.0672 | -45.31846 | 2024-12-13 12:44:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a5cadad2-e75b-3641-ba0c-26bcf2df7a96 | -7.46696 | -49.0035 | 2024-12-13 12:44:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7c915535-aafb-3378-8b45-86cae9f993e7 | -12.76564 | -49.31033 | 2024-12-13 12:44:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 80e4c512-cb9e-3cdc-a9a7-2b2976966d64 | -12.07424 | -48.40934 | 2024-12-13 12:44:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 31f8015c-8ce2-3f05-b89c-2f2b9a2212a0 | -12.09873 | -43.59372 | 2024-12-13 12:44:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8c214551-b767-3d37-bfdd-e28dc3460967 | -8.46532 | -47.97409 | 2024-12-13 12:44:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fd1031d2-7f6b-3dcd-b151-fc7d3d6bb43e | -8.74798 | -46.70406 | 2024-12-13 12:44:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 033bb11a-3490-3fdb-a91f-b27449c0b4d2 | -12.48436 | -45.24874 | 2024-12-13 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d5966e51-e729-3c2d-9267-2fe4e32d602e | -8.46659 | -47.96522 | 2024-12-13 12:44:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9d808ceb-a4fb-3f5f-891e-9347925a2e70 | -10.31979 | -47.97018 | 2024-12-13 12:44:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6679a9e2-bc0c-3cdd-bb83-88ce81907f3f | -10.37007 | -47.68173 | 2024-12-13 12:44:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| dab3af8f-d4d2-3b99-bbb4-def87e4ffb07 | -10.32894 | -42.39977 | 2024-12-13 12:44:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 16d5dabe-c97d-3e50-81d7-d6eb185717c0 | -9.90965 | -42.10615 | 2024-12-13 12:44:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| ff9988b8-df88-37e4-b083-c9d2f33d3b23 | -12.07553 | -48.40029 | 2024-12-13 12:44:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 3d327c7b-6fb9-3178-8681-f99b96410c63 | -14.76459 | -52.63933 | 2024-12-13 12:44:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f0d5b82f-7fa4-335a-bea6-7e30b86da9ec | -11.48204 | -48.22592 | 2024-12-13 12:44:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ea9f34cc-9e90-3b55-baa2-aabde0ff59e9 | -11.78453 | -44.17372 | 2024-12-13 12:44:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b31e38f1-5c81-3646-88ba-69f2b530927d | -13.36138 | -43.8373 | 2024-12-13 12:44:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d9d75356-49b3-3b2e-a7e4-30717232302b | -26.94035 | -52.79762 | 2024-12-13 12:48:00 | TERRA_M-T | NOVA ITABERABA | SANTA CATARINA | Brasil | 4211454 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 8dbd58d4-0afc-3c03-bbf4-80aa23111bd9 | -3.4042 | -42.2621 | 2024-12-13 12:50:00 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 58e27d07-6996-3cc0-9858-b1d29ab20663 | -3.3531 | -41.358 | 2024-12-13 13:20:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 6f13b51d-b5b2-3126-b50a-c2934d1d3f7a | -3.2789 | -41.2411 | 2024-12-13 13:20:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 165.8 |
| ed9a75e8-0b07-3a22-9252-7dfab0d9d311 | -8.2739 | -48.0145 | 2024-12-13 13:20:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 6aedeaa9-c1d9-38b2-ba4c-6fb0f0831ac3 | -2.9747 | -42.2339 | 2024-12-13 13:30:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 50e6b3e6-79ea-389a-a625-944e89d2bcd4 | -6.2456 | -39.3314 | 2024-12-13 13:30:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 96.7 |
| ada7a078-002c-3808-b59b-b2c817a36ba9 | -8.2739 | -48.0145 | 2024-12-13 13:40:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 513c78f8-1f5f-353d-b474-4ffd7c70c599 | -2.9747 | -42.2339 | 2024-12-13 13:50:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9204d069-3624-398d-a40a-219c94f95cef | -8.2737 | -48.0364 | 2024-12-13 13:50:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| d975451e-542b-3cf8-bf6c-da2967d77dd1 | -8.2739 | -48.0145 | 2024-12-13 13:50:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 5314bc21-f0b4-3d21-8d22-1cebc5ec2d2e | -2.976 | -41.9729 | 2024-12-13 14:00:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 120.8 |
| 24fedab5-3cdd-3d28-9143-80ba2043c57c | -2.9764 | -41.8776 | 2024-12-13 14:10:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 50317c56-0ebc-3108-899a-6defa3e4cf50 | -4.1696 | -42.4346 | 2024-12-13 14:10:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| c7fb1804-c0ad-35ae-a732-0c63177c0e69 | -2.976 | -41.9729 | 2024-12-13 14:10:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 755ae32c-f07b-31d8-8406-bf2b0162e9c7 | -4.4095 | -42.8911 | 2024-12-13 14:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 4720ca0e-e734-3c95-88fa-657315188af7 | -8.2739 | -48.0145 | 2024-12-13 14:20:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 8f89743c-7a8e-3f37-bda0-7630aa87a6c9 | -8.2737 | -48.0364 | 2024-12-13 14:20:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 5b402db1-b8fa-3e51-89d2-c1adb99803f0 | -8.2551 | -48.0162 | 2024-12-13 14:20:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| b3c8032b-1221-3c37-b902-ffd9d01483ac | -3.2976 | -41.2403 | 2024-12-13 14:20:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 80.1 |
| f435af96-892f-3d56-ac84-c68085ea0d4a | -4.4095 | -42.8911 | 2024-12-13 14:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 70c5f5ad-7843-3d2c-a112-928be0d12bef | -3.3531 | -41.358 | 2024-12-13 14:30:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 198ace8f-b7aa-3941-b6c3-bffaea1278b1 | -3.4867 | -40.9166 | 2024-12-13 14:30:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 9e943426-2737-3e8e-afe7-9286521dcfa5 | -8.2737 | -48.0364 | 2024-12-13 14:30:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 1ce62ce8-7e32-3b60-9664-6eb95782a01c | -4.1696 | -42.4346 | 2024-12-13 14:30:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| cae5bbcd-f59e-3fcc-921f-d31520dfcf20 | -8.2739 | -48.0145 | 2024-12-13 14:30:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 191.8 |


