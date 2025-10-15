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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fe6c055-d064-3ed5-838d-8e160d0f1c0e | -4.28212 | -48.58902 | 2025-10-15 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3458bdb3-c7ce-3709-8585-9853122e56e5 | -6.23354 | -44.17215 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1a813125-99c5-3173-8e48-ece015ab5877 | -5.23272 | -43.6638 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd9e7b09-c377-30d5-b7ac-fdd53edb7276 | -7.48932 | -42.13747 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e3d39b06-6e01-3f50-8485-92cdebcd9113 | -6.21586 | -42.49708 | 2025-10-15 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7a22a267-562a-3b94-8ba3-a4d339f08d6b | -5.42967 | -44.23106 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 181db05f-79cc-3e5e-a04e-bf8abc726d2b | -6.8933 | -43.97244 | 2025-10-15 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a45d3069-9fd0-3b37-b5ec-a6bbc1832ac4 | -5.84404 | -43.96077 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5bcf6a6-6296-3e74-a5dd-9995376701d9 | -5.14948 | -45.7705 | 2025-10-15 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff62b387-b5af-3f59-9fa1-19e21cd27213 | -5.47355 | -44.64712 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f265684f-2443-3df8-8d11-95680f7c49cd | -8.21657 | -44.03621 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a266d871-4fe3-3dd9-88b5-4bd3dc2def65 | -6.91247 | -38.26455 | 2025-10-15 04:06:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9085a3c2-c5d7-33aa-bdae-62dea9ed17ad | -5.32046 | -42.92395 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 457cbf2b-2259-330f-84d4-fefab16bad12 | -4.11727 | -50.71876 | 2025-10-15 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c193764d-10a6-32aa-9c60-1076c44498ec | -7.57112 | -43.84021 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6cb641bd-e4b8-38e8-858a-2a59717f8861 | -6.14733 | -41.73114 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ec42cf57-b4b8-34f8-9554-ed43b1c19c3d | -5.26796 | -43.22605 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 886173a4-369c-3b99-95d8-751e394e3acb | -5.82169 | -46.53643 | 2025-10-15 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 629f5e9c-aaab-336f-a2a3-c052604f1c7e | -7.92931 | -44.13385 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cb6d5d68-f690-313f-9394-797dabe316e0 | -5.58669 | -42.83807 | 2025-10-15 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3b576041-e8ac-3968-b139-850652a333ac | -2.95219 | -49.33947 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d606c2a-39c7-3c18-b0de-f1230e17b46b | -5.41985 | -40.98203 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3bd2590e-3154-3aa4-8fbb-f6589807265e | -7.75247 | -42.44897 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0c638d66-bd14-3e6d-935e-bd0bcf86d7d5 | -2.92532 | -48.3078 | 2025-10-15 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 56ce61fd-b937-35b9-823f-e5fc81296762 | -6.89745 | -43.96912 | 2025-10-15 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adc4e56f-ea15-3474-89fd-5daa0be08c76 | -4.80093 | -45.71968 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8889bec-cc27-3030-a876-774ab8ddcbeb | -5.15083 | -45.76973 | 2025-10-15 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5399685-56eb-3d31-b3eb-b521642feac2 | -5.87652 | -43.87199 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5ed4285-744e-3282-bb30-09877a4e6c62 | -6.45239 | -44.57701 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a9e9d9e3-3c37-3cd2-be26-840006432587 | -4.2561 | -45.58549 | 2025-10-15 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2cb3f407-bec1-3398-b9ce-acbb275d091d | -7.9328 | -44.13442 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfb443c7-361d-3e09-a324-1c9e94c4f5f2 | -5.88852 | -43.75281 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 14dff9c0-48fd-38b3-abc3-b33448f3d18a | -4.54514 | -45.41589 | 2025-10-15 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7708537-f787-35b2-8b2d-67c944b2769d | -5.18572 | -42.91051 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7e552fb-113f-3210-bc25-45aa9f3c9646 | -4.6429 | -42.81798 | 2025-10-15 04:06:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 202450e3-12bf-3d88-b611-3da9ebf0dbac | -6.19458 | -43.28994 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d55fe5f0-579a-339a-9a59-f2fb56d37a66 | -4.52442 | -48.05318 | 2025-10-15 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ee59c615-4bf9-3040-9fb6-dd6cd5e49160 | -8.21436 | -44.02796 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce858f55-68c5-3835-bb4d-37e7c785eb87 | -6.58926 | -41.51372 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c3d5c1f8-9338-320e-883c-209a58c3178c | -7.50271 | -46.64264 | 2025-10-15 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0efc1de4-a1ff-3387-9761-7762c65970e0 | -7.16945 | -42.20481 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 00824f63-01c1-3f8c-a834-1a9a18a7e006 | -7.94263 | -44.14004 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffbc22c9-8c3d-3e75-9016-b6f5bb727c9a | -2.95167 | -49.34257 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1498f7e-4e55-39e8-aabf-6ae3c5dfe326 | -5.91426 | -42.82898 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ce184520-f843-309a-a069-4d7ebfefcd27 | -5.39987 | -46.41339 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9726753-8b09-3331-a11d-f6f29e0c9f3a | -10.16745 | -36.17464 | 2025-10-15 04:06:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f3ad098b-ca5a-3f43-ab38-00163b920986 | -5.87011 | -43.86687 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53c8a586-cf01-3b2d-97d3-33963880ec9b | -5.19059 | -43.81182 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ad96bc2-14ed-3bf7-be10-0e1497302b70 | -5.40753 | -40.88829 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9f3c025d-a936-3849-ad96-6f350d179968 | -5.38615 | -43.23273 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 128fb740-6800-31d8-857c-7af51ed791df | -6.03047 | -44.31041 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49514582-28b9-3a3d-a6a7-2b03a3713d9e | -5.91939 | -42.81868 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 48704ea0-049f-3906-b194-ff2ffc9dcd1a | -3.22152 | -48.93064 | 2025-10-15 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7295485-9e83-310a-9eac-5081f2afa676 | -5.85551 | -42.82693 | 2025-10-15 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f022f5c5-bc20-3f28-a46b-fa10a6e496d4 | -4.54825 | -45.42144 | 2025-10-15 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aef5ae28-c406-3c0e-88b8-d710247dfd0a | -7.54083 | -42.68673 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6503ebc3-abb6-3562-aca3-a3055b9f90ad | -5.60751 | -41.19213 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 39c71531-41b1-35ab-b722-1a6bad0c9cbf | -5.79371 | -43.89122 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4fb45fd9-4e99-3909-93f4-4f80e1fb27ff | -4.95188 | -41.70474 | 2025-10-15 04:06:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bf06476b-ae25-3b0d-a26e-76f5c30443b7 | -6.4594 | -41.84097 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9ed4ae00-fe3e-322c-afd9-498adc290781 | -6.05725 | -41.89105 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0da91e66-d57d-3d0e-9e88-9a31b0a9434d | -6.99023 | -38.4444 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eb96c936-7c29-3c16-b8df-4ad57cc680fe | -3.46475 | -48.98331 | 2025-10-15 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23185bb0-de28-3ab7-b137-bd61db7bfe3e | -5.07014 | -41.19504 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 523f1666-fb69-3498-9bf6-6a92222a528c | -5.58802 | -44.74946 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d1f0bb1-3918-3e32-b0d1-7e9445577a40 | -5.86371 | -43.86172 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97a19af4-c5c0-39a7-916e-b4fcd8c98d5e | -3.07477 | -49.50699 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64ba1892-c200-309a-b791-06d6234ca19b | -5.28276 | -43.24405 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1c3afd2-159c-35a1-9d75-0eedc2bfedb0 | -5.13429 | -46.10512 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| beca3335-c30f-36aa-9af5-f02b4027b8eb | -6.21921 | -42.49758 | 2025-10-15 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d7cf6f14-41ef-32b6-848d-8067fb082d41 | -9.17151 | -40.31003 | 2025-10-15 04:06:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c8ec78d6-8da1-3c9d-a300-0b429a95df1f | -5.38899 | -44.04086 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5011ec2-ab34-33ec-a19d-ad69cfa71a2a | -7.43831 | -46.75356 | 2025-10-15 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0920557f-23c6-3176-8b95-a02ff9dd28ea | -7.02416 | -42.73187 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3ffc975a-91e7-3576-89ee-df1e3533b304 | -5.39989 | -40.8908 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ae2bf08d-8660-3d75-9078-dae3ab595e18 | -3.78332 | -49.42974 | 2025-10-15 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 041af26e-215f-350a-99cf-1b835f27215c | -7.36508 | -43.64027 | 2025-10-15 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d1ba460b-9687-3924-a667-7547c5c8a490 | -5.13834 | -46.10571 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9275dde-d990-31a1-9795-810ecbb0ca1f | -5.05726 | -44.44407 | 2025-10-15 04:06:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a43975f8-4b98-331b-9100-5ec81dc348cd | -6.1523 | -41.7426 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| acd59403-1acc-3047-a018-18a13a47740e | -8.97186 | -39.92353 | 2025-10-15 04:06:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 390b67a4-d8df-3b66-8357-eb265835e952 | -6.58302 | -42.96537 | 2025-10-15 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 137e3701-bb90-3e30-863c-a194a99b51bf | -5.25313 | -43.47105 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a490ce4b-f89a-3d7b-98bb-8537357d5d7b | -10.15945 | -36.16935 | 2025-10-15 04:06:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 50441073-eb3c-3a52-85ea-3fafbe23346f | -5.40418 | -44.22053 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 973d1342-2aea-3cc9-a47e-207aab6a4d5e | -5.79356 | -43.89183 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c0db862a-8143-33b1-a13a-a6bb10b5d9a9 | -5.61558 | -42.72281 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 78e3a517-1b43-3fbe-9874-0cdba13d49ec | -7.03308 | -42.74066 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ba5c41b4-9623-3e7a-b50e-a125e582912f | -5.97892 | -42.86583 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 02650579-82a9-3e44-9b21-e3081322e750 | -4.77294 | -45.74134 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| edf54848-4c4d-3b4a-9f1f-aae676e78b55 | -5.00719 | -44.49958 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71d129a6-d267-3955-a40f-3648804a0b7c | -6.58989 | -43.92034 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ceb0bb06-ceeb-387e-8f58-d07065d626b6 | -3.57014 | -49.44586 | 2025-10-15 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12cf3c6b-e45f-36ab-b1d9-2e50ebbd50e0 | -5.83389 | -42.33073 | 2025-10-15 04:06:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 23c44cc0-14fd-318e-b336-8f4db767900f | -5.41499 | -44.22231 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ac34320-b5f3-3c2c-9dee-893fa577cafb | -5.38454 | -43.22083 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b52b654-4995-3c31-869e-01e2822bcfe2 | -4.91176 | -46.70885 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 817b8f86-199f-397f-b7c5-8421b1ab514d | -6.26118 | -44.34145 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58351bfe-a1d6-3757-876b-3f42406f51d1 | -7.03644 | -42.7412 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7b2c6aa5-f423-3161-ad92-3fbc88e3fd6d | -5.18455 | -42.91791 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README32.md)
