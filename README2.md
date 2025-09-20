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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59148390-b6e1-3d1a-a4e0-10d70012394e | -4.3681 | -46.2688 | 2025-09-20 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 6bb56137-95d8-3109-8ff2-d79a75f32ad8 | -4.368 | -46.291 | 2025-09-20 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 6efc151e-c234-3bfa-93b2-c6b5a6542c4a | -4.3494 | -46.292 | 2025-09-20 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 3e1aeefc-f9ae-3362-bfe2-d33564eeb4c0 | -14.30136 | -47.11801 | 2025-09-20 00:30:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 427a825e-26e6-3908-bab0-da2e2831a007 | -15.67667 | -42.47634 | 2025-09-20 00:30:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 4fd75844-2d26-3bd8-86a0-7aa37f62e24d | -14.30011 | -47.10897 | 2025-09-20 00:30:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 184357ef-c032-3d94-a6b4-8fc1f2f29b01 | -14.43928 | -46.51381 | 2025-09-20 00:30:00 | TERRA_M-M | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 7bc1bc47-258b-3084-9a36-7fae95aa8b25 | -14.19328 | -46.41095 | 2025-09-20 00:30:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 76cec4b8-36b2-351d-a97c-7e9d3458fa14 | -15.68239 | -42.48302 | 2025-09-20 00:30:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 877ab2f6-cc71-34b4-9775-71165937fecc | -16.32661 | -43.96908 | 2025-09-20 00:30:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| dd903fae-2645-35cb-b00b-2a31e570fd63 | -15.67881 | -42.49011 | 2025-09-20 00:30:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8f31c64b-6106-34b0-9df4-a0277a420396 | -15.93362 | -42.18824 | 2025-09-20 00:30:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| 8b333eea-6cd2-31f7-bf03-a0bde31cbb1e | -15.55011 | -42.67299 | 2025-09-20 00:30:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 44e0548b-1c43-3a8b-a8fb-04b839e770d4 | -13.96752 | -45.04686 | 2025-09-20 00:30:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| dc9d04d1-f270-3d0f-ba4f-52acb7ab1d03 | -14.14231 | -43.97189 | 2025-09-20 00:30:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 76017a65-4079-3151-a992-18421b89ed31 | -16.31875 | -43.05692 | 2025-09-20 00:30:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 2f87f1b4-63e0-3d7f-adaa-799d09909d45 | -16.32491 | -43.95789 | 2025-09-20 00:30:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 89e8c1ec-616b-3198-86cb-19f501530da2 | -16.32072 | -43.06924 | 2025-09-20 00:30:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 44.3 |
| f946780b-579a-3a25-8c9a-7025679cfb91 | -13.07722 | -42.14823 | 2025-09-20 00:30:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 26.6 |
| e2e4a9ae-a1a6-3d1d-b1ba-91cc6deec77e | -16.31903 | -43.05053 | 2025-09-20 00:30:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| c6ed8496-8642-329f-987f-eb09cd9cb54a | -16.3108 | -43.06469 | 2025-09-20 00:30:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c16aec68-0b96-31a8-91e4-852b39390a9b | -13.07483 | -42.1334 | 2025-09-20 00:30:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| f6cc4c48-4b85-3847-a321-20cb20fc80d6 | -16.3127 | -43.07703 | 2025-09-20 00:30:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5247c5c2-62fa-385c-a9e8-83c51a9ea481 | -16.21829 | -46.6483 | 2025-09-20 00:30:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 356a5491-a891-3dd9-9cfe-ecf5ede18b5e | -14.43797 | -46.5046 | 2025-09-20 00:30:00 | TERRA_M-M | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68d0e94d-1385-3345-a2c7-ff378c8ce505 | -15.68012 | -42.46906 | 2025-09-20 00:30:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 235071cd-8436-3d51-924d-ac3353c8377e | -16.32091 | -43.06282 | 2025-09-20 00:30:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 392c3934-0550-326e-a40f-6d63a0c33cf5 | -7.32317 | -44.56899 | 2025-09-20 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 20b081ab-0476-3fe2-8c50-20d4cea2b280 | -12.42454 | -45.02513 | 2025-09-20 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 16f2f507-c275-3ae8-a501-432e41e9a980 | -7.25302 | -46.37815 | 2025-09-20 00:33:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 58656c80-83e5-3c5a-a2a0-be49303269f5 | -5.8019 | -43.64384 | 2025-09-20 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1732e5df-18db-3e0e-ba79-4ce0e4f812aa | -5.88715 | -46.00055 | 2025-09-20 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 112a784d-2ba0-3144-a75f-296c685b52bc | -11.50856 | -43.62873 | 2025-09-20 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8bfd19ed-5234-3dca-82dc-1651ea11eefe | -7.37673 | -47.04564 | 2025-09-20 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| db2d7fc9-6755-3f57-b6ef-f912518e341c | -5.82583 | -46.27962 | 2025-09-20 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1cd9c036-7d92-3955-b9c4-141917280cf5 | -4.91588 | -38.68804 | 2025-09-20 00:33:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 41.0 |
| eb402f76-4138-3ab3-80e4-da3b6c58e6c1 | -9.52216 | -43.064 | 2025-09-20 00:33:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 2a9239ea-d422-343f-92e5-e1c0564d2235 | -6.96378 | -42.43736 | 2025-09-20 00:33:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 21e2cfb9-bcf5-39e8-8fa2-7cc45a778c9d | -6.81021 | -47.86498 | 2025-09-20 00:33:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d4aa8d97-741e-36eb-813b-0c171742b2e7 | -12.7256 | -47.78249 | 2025-09-20 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 93632863-6fd1-3bc8-8273-860bef2506de | -9.22623 | -43.30923 | 2025-09-20 00:33:00 | TERRA_M-M | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 03546576-5da3-3c2c-9e88-bc0a8b26bc96 | -7.25588 | -45.48855 | 2025-09-20 00:33:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| d6e13f83-cd33-3c5f-a91f-faa50b8bf47b | -12.35741 | -47.05678 | 2025-09-20 00:33:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8e19eab0-ebc1-3617-bacc-a3fdce1a2a3a | -6.18095 | -45.42202 | 2025-09-20 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e10f366d-260e-35a2-af17-9e64362c14ef | -9.13592 | -40.106 | 2025-09-20 00:33:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| bedbe190-088c-38b6-bb03-0212c8e5b683 | -6.19187 | -41.22643 | 2025-09-20 00:33:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 6e7fd30e-5f74-3d03-ab97-ef88b267b178 | -5.79024 | -43.6456 | 2025-09-20 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 09c75872-4e1a-3b39-8385-5eac9ebbbe23 | -6.9031 | -44.76964 | 2025-09-20 00:33:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 21ab6c95-5685-3b4e-a339-d43431c3d828 | -9.2285 | -43.32415 | 2025-09-20 00:33:00 | TERRA_M-M | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 12d091ed-825f-3cc5-aa4f-01d219a345fa | -5.10649 | -43.20189 | 2025-09-20 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| f023d42b-140c-3c2e-8e25-28a09f87c76a | -6.80895 | -47.85602 | 2025-09-20 00:33:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c19a75bc-9204-34f4-911b-c3eefc8cbb52 | -12.7358 | -47.72587 | 2025-09-20 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| de5dd539-fb9b-3abb-a650-30b11be58843 | -5.10907 | -43.21972 | 2025-09-20 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| a6bb0378-261c-3bac-98fa-010011ebbfd8 | -12.15542 | -44.94522 | 2025-09-20 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 72a63eec-f917-3f50-a46c-e7fe406642a6 | -11.20176 | -47.36259 | 2025-09-20 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 234a4758-cab6-30aa-a925-9b950d80d3e3 | -7.08584 | -47.33556 | 2025-09-20 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c17290e8-0c3c-3686-9066-e95c01746887 | -11.46884 | -43.58131 | 2025-09-20 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5de41698-81fc-3be9-b1cf-43d7c5542bbd | -6.64229 | -49.78494 | 2025-09-20 00:33:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9c9f692b-a656-33c5-bc7d-9b6ff8466ddb | -5.10023 | -43.21463 | 2025-09-20 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| cf76c724-80c8-367a-b699-9553c4ca714d | -12.09295 | -44.85529 | 2025-09-20 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 960bfb1a-580a-383a-9357-b554bc5a72dd | -6.61091 | -43.59608 | 2025-09-20 00:33:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 990d676e-f676-3c05-b158-c5721fe53f36 | -5.92805 | -45.07978 | 2025-09-20 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 2ceeadbf-58c3-3cc7-ac50-d543fe2b1b55 | -7.97038 | -55.29603 | 2025-09-20 00:33:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a91d3388-4933-34b8-b331-b18d07297557 | -12.39586 | -43.8168 | 2025-09-20 00:33:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 572add91-d130-34e7-8c49-a7d9727036b3 | -12.80399 | -44.13483 | 2025-09-20 00:33:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| c102315b-1430-3896-a2a8-152ba8d25412 | -8.71653 | -47.06269 | 2025-09-20 00:33:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 26a6bebb-227a-37d9-b60b-10e99a53536c | -8.14641 | -43.6286 | 2025-09-20 00:33:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7bb378b6-f617-3277-9e4d-967f0b7defa9 | -6.91541 | -44.78043 | 2025-09-20 00:33:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3e0aa2a1-082d-3dda-8e0f-12ac7f6b3291 | -11.66589 | -44.88618 | 2025-09-20 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 72ed0822-de67-339e-8a86-e8677e79f102 | -11.46679 | -43.56789 | 2025-09-20 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 516d6a73-b34a-3d59-a598-cd442ce305f9 | -5.69143 | -46.35436 | 2025-09-20 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3a37badf-e32f-3e32-90bb-f4d98e07ca0d | -6.72882 | -44.15332 | 2025-09-20 00:33:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| f03b9214-aef2-34e0-a90a-d09f8e9b61a9 | -7.92309 | -43.90529 | 2025-09-20 00:33:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 751bf2eb-321e-3a44-b53c-c8afb88bd08c | -7.20607 | -44.43734 | 2025-09-20 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fda6d5fa-2411-362c-a5e6-356d3acd97dc | -12.4331 | -46.67174 | 2025-09-20 00:33:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c5da172c-a386-34ab-9168-4930ad2605d6 | -7.33171 | -44.55416 | 2025-09-20 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 6f349fb3-e021-3dff-b7be-52fc89ae8273 | -10.24037 | -47.99793 | 2025-09-20 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3108ef43-91d8-3c5f-9243-0cf650bec03d | -8.96945 | -47.68628 | 2025-09-20 00:33:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a9e779b7-af58-33e7-a62c-239f97edc851 | -10.23896 | -48.05257 | 2025-09-20 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 870d50a1-9603-3709-9c99-6e0ce6410b9d | -6.1827 | -45.43388 | 2025-09-20 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 77830658-5ead-381f-b8b3-cfc528e017bb | -5.79763 | -43.63883 | 2025-09-20 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 96c7d0ba-0b5d-3bdc-857c-8d0875f27000 | -12.7245 | -47.70917 | 2025-09-20 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d7e47ff1-e808-3f09-9859-42d30285cbfc | -6.40257 | -44.28572 | 2025-09-20 00:33:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 58d7f575-463e-32a2-86e5-6fea67098c50 | -11.67102 | -41.74382 | 2025-09-20 00:33:00 | TERRA_M-M | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| bf162c69-f8c3-3521-adb5-33691ae4a66b | -5.57823 | -43.45462 | 2025-09-20 00:33:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8a30200b-cf89-312c-b069-d25aa174dd1d | -9.05955 | -47.01306 | 2025-09-20 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cba3040d-769a-31dd-9fc2-6b753cc46b5b | -14.5901 | -56.91779 | 2025-09-20 00:33:00 | TERRA_M-M | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 37349cd1-903d-3033-abe5-efb1dab8bfa1 | -9.21188 | -43.13835 | 2025-09-20 00:33:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| cc1ee5d2-fc69-36c9-8bc9-c839f992b752 | -12.62374 | -47.71148 | 2025-09-20 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 883cf84b-a564-3a5e-9f0b-aade9b0898bb | -12.08011 | -44.83549 | 2025-09-20 00:33:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| d82219bf-2f6c-3907-9a12-1fa3ecca3781 | -7.60348 | -45.48172 | 2025-09-20 00:33:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 88862be6-737f-340c-b0d1-9b0ef9925655 | -12.14421 | -44.93554 | 2025-09-20 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 69ea204d-7a73-37d8-ae8e-ff471f35c71a | -12.42362 | -46.67945 | 2025-09-20 00:33:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 10c6eb33-32ee-3d1c-8cf3-fead5eba367f | -12.07848 | -44.82474 | 2025-09-20 00:33:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 38.9 |
| af00a330-54e1-3f05-b663-a81785c2db06 | -12.50177 | -46.70803 | 2025-09-20 00:33:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ae0512a7-851a-3bfa-8c77-9223947b5b87 | -13.32554 | -48.7443 | 2025-09-20 00:33:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0dce6931-3527-3f09-93c5-60679e93efcc | -5.53694 | -43.8814 | 2025-09-20 00:33:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 7fb77829-71fd-3f25-a450-157875efc64e | -6.26583 | -43.91039 | 2025-09-20 00:33:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8789b086-11c9-3f22-8d2e-0200cfe79c6e | -5.63224 | -45.94403 | 2025-09-20 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| cab5be5d-4252-3368-8b39-df473455901c | -5.92624 | -45.0671 | 2025-09-20 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |


[Clique aqui para ver as próximas entradas](README3.md)
