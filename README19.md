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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd965e0a-c035-3580-85b0-0e3ba81824dc | -3.1099 | -54.2263 | 2024-10-16 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 199.3 |
| 6b8ba009-0e94-308e-bd0c-20e160c36d36 | -3.11 | -54.2063 | 2024-10-16 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| d554209f-8752-3126-85b8-6b2ec81e75e5 | -3.1282 | -54.2459 | 2024-10-16 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 38c1db70-da52-362b-9209-869660218a89 | -3.1283 | -54.2259 | 2024-10-16 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 183.2 |
| ad7801ab-778a-3462-b1b2-d97c2815e35b | -3.2862 | -47.133 | 2024-10-16 01:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e0104955-27c3-3dbc-9dc2-fafd600bc8a8 | -3.2863 | -47.1111 | 2024-10-16 01:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5137c744-75a3-3b5e-b311-a5bf7a586172 | -3.288 | -50.9321 | 2024-10-16 01:35:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 6868c6cd-a11b-388b-bdf9-82fefff83e6b | -3.4104 | -44.5599 | 2024-10-16 01:35:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 128.6 |
| e73c5642-930e-388d-a311-81718c9d9677 | -12.5093 | -63.018101 | 2024-10-16 01:35:27 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b339395a-2262-3d32-b143-e6cd18dddef3 | -12.5112 | -63.027 | 2024-10-16 01:35:27 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cd3cc785-eece-3fb1-83b5-1fee8256c1bd | -12.7896 | -62.938999 | 2024-10-16 01:35:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5dc53f4c-b32e-3053-b218-dc2444461bc9 | -12.7877 | -62.930099 | 2024-10-16 01:35:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0367d3a9-530c-3a3b-91ce-7918bcc554e9 | -12.7602 | -62.9454 | 2024-10-16 01:35:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b16e50f6-cfff-3dc5-9b24-e59551870575 | -12.7583 | -62.936501 | 2024-10-16 01:35:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0d4a16b7-b337-3bee-84f8-ef468a36ad6d | -12.7719 | -62.952202 | 2024-10-16 01:35:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 25541d26-b5cc-3362-bcd1-984ffcb61a44 | -12.77 | -62.943298 | 2024-10-16 01:35:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c413dc47-d7c4-3bdb-89ee-a1d15ab52a0b | -12.7681 | -62.934399 | 2024-10-16 01:35:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 798caa73-9dda-30bf-9b29-e618cda19929 | -12.7817 | -62.9501 | 2024-10-16 01:35:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 068b93c3-193f-31a2-977b-16239688e751 | -12.7798 | -62.9412 | 2024-10-16 01:35:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cc6b80d4-ed4e-30b6-97ca-bebf312c4ce2 | -12.7779 | -62.932301 | 2024-10-16 01:35:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f56591be-2d75-31e1-a4e3-2e2a3cf0e0e4 | -12.5015 | -63.029099 | 2024-10-16 01:35:34 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab78ddfd-2695-30d0-b758-5b4661c93321 | -12.4996 | -63.020199 | 2024-10-16 01:35:34 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f157a27c-ee9e-344e-ab78-01d7ed02580e | -12.4764 | -64.026199 | 2024-10-16 01:35:38 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a39773cb-7fca-3bfc-b19f-7414404ed9a4 | -11.9383 | -64.873199 | 2024-10-16 01:35:42 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1f1a4332-9e47-3768-be2c-477269b97e32 | -11.7627 | -64.083 | 2024-10-16 01:35:42 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 31ca1092-da47-37b5-a102-acf295be58ec | -11.9285 | -64.875198 | 2024-10-16 01:35:42 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 039763fb-daa8-3acf-8802-5206ef804194 | -11.8866 | -64.919098 | 2024-10-16 01:35:43 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab293ef9-56bd-32e6-8331-90b0203dcafd | -11.8889 | -64.930397 | 2024-10-16 01:35:43 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bf880221-6e34-3551-a518-358d7fb1cf86 | -11.7392 | -64.798798 | 2024-10-16 01:35:45 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b503e257-fa61-3ecd-88ac-7488ddad8683 | -11.7414 | -64.809898 | 2024-10-16 01:35:45 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc3cf51-d1ed-3a98-af67-337afd63f836 | -11.7142 | -65.218697 | 2024-10-16 01:35:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b2b43a9d-b4fd-317c-9c1b-8d86e3a7be8b | -11.6996 | -65.197304 | 2024-10-16 01:35:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fb52ccc4-ac9e-3863-bb6b-142ece19f395 | -11.702 | -65.209 | 2024-10-16 01:35:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0d7a28a9-821a-3842-a665-aa6305c4ca47 | -11.7044 | -65.220703 | 2024-10-16 01:35:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3bbf940-26a2-3d53-b196-6f6d126fe43e | -11.7068 | -65.232399 | 2024-10-16 01:35:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eeee931c-6bb3-339c-af95-ee04a991eda7 | -11.6898 | -65.199402 | 2024-10-16 01:35:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 60f4ce64-e9a7-3cc4-8d86-1fe594e2e1e4 | -11.6922 | -65.211098 | 2024-10-16 01:35:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a8f8d238-4821-3930-88d3-c158d75a6923 | -11.6947 | -65.222801 | 2024-10-16 01:35:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fcff5622-8dea-3ba4-86e7-c9f00473f472 | -11.6971 | -65.234497 | 2024-10-16 01:35:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6711d983-eace-3b98-b19e-93c6b8318f1e | -11.6874 | -65.236504 | 2024-10-16 01:35:55 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b800c54-f31a-37d6-8b47-539531940b6a | -11.685 | -65.2248 | 2024-10-16 01:35:55 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3aed9a24-a66f-3350-8b30-a1661b25442e | -11.6825 | -65.213097 | 2024-10-16 01:35:55 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 42d565d8-2f91-3d1a-94e5-02b1be1edf59 | -11.6801 | -65.201401 | 2024-10-16 01:35:55 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6b65a970-25b0-3804-8515-189b53e8ab09 | -9.1709 | -46.9792 | 2024-10-16 01:35:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 158128bc-9741-3d39-9be0-376d3b763d88 | -10.8224 | -49.2343 | 2024-10-16 01:36:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 06f57022-438a-3d9f-a6d2-dad3f1fc66de | -10.8413 | -49.2322 | 2024-10-16 01:36:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| e48d7050-f406-3909-9080-2ce127ab52a5 | -11.6915 | -65.2432 | 2024-10-16 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| a8966973-caaa-38c7-99d2-7ff2b2564ba9 | -11.6917 | -65.2243 | 2024-10-16 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ea0f1c23-4d0e-3736-ab33-512a3daca426 | -11.6918 | -65.2054 | 2024-10-16 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| fdfd4286-4f4c-3aaa-9057-d5889a9de66e | -11.7103 | -65.2424 | 2024-10-16 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 15b1e0b5-7a50-318b-b6cd-1af58d9406d4 | -11.7104 | -65.2235 | 2024-10-16 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 886b0a45-bb05-3a41-ac45-2121dd0b7bd5 | -11.7106 | -65.2046 | 2024-10-16 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 88b2c43b-b502-3eb5-8ba7-481400871c88 | -12.0427 | -46.7161 | 2024-10-16 01:36:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c892cea5-d731-35cd-97aa-3ad0c485c269 | -12.0431 | -46.6935 | 2024-10-16 01:36:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7b1dbb49-075b-3c38-a8d0-357e19775352 | -12.0619 | -46.7134 | 2024-10-16 01:36:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 3fed1b8f-3958-3b25-a4f8-adc7d2419edd | -12.0623 | -46.6908 | 2024-10-16 01:36:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3d605166-24d2-3aa9-b22c-aea10eaf7b0f | -12.4925 | -47.2818 | 2024-10-16 01:36:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| bec24474-ad88-39e9-8429-0a9b4d6f7b40 | -12.3793 | -63.7294 | 2024-10-16 01:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 877fa172-eba3-3c63-a900-2f877aac83ce | -12.3795 | -63.7103 | 2024-10-16 01:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| c71d8d35-f338-38ad-9b87-4d09769e0499 | -12.3983 | -63.7093 | 2024-10-16 01:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 23a4aed2-3242-36fa-810e-ed731e133e32 | -12.4958 | -63.3024 | 2024-10-16 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e0ced1df-cbb5-309d-a0f9-7d60d9cf6935 | -12.4979 | -63.034 | 2024-10-16 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8ef0ab65-2432-378b-967e-b323c0ecd5d4 | -12.4981 | -63.0148 | 2024-10-16 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 62b700a9-4efc-32d7-be20-8fee0d66379b | -12.5147 | -63.3014 | 2024-10-16 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b82db895-a396-3789-9b99-163bbb34f756 | -12.5168 | -63.0329 | 2024-10-16 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 9313baf1-cc11-385d-bacd-3470309fc396 | -12.517 | -63.0137 | 2024-10-16 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 8b90c96b-436e-3ad0-b1f3-6c7b0bc87e2a | -10.6249 | -67.841202 | 2024-10-16 01:36:21 | METOP-C | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 179f3fdb-1915-3615-8a3a-9be351e76cb5 | -10.6215 | -67.824303 | 2024-10-16 01:36:21 | METOP-C | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 2e3f6fe8-3e74-3db1-b549-a4d569d809ae | -9.1672 | -65.3862 | 2024-10-16 01:36:29 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| deddd761-0e74-3737-8492-a9a65592f4ed | -9.1696 | -65.397102 | 2024-10-16 01:36:29 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 181d2a6f-63bc-3ce7-a242-ac429e178099 | -9.1598 | -65.3992 | 2024-10-16 01:36:29 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06ee0a3f-0964-3f16-85c5-d194b7b49d8c | -8.58 | -63.245201 | 2024-10-16 01:36:39 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 861ba7f8-eb94-3f39-8705-a9bcf0ade2f2 | -17.2439 | -42.6575 | 2024-10-16 01:36:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 4625f5b2-e3e6-3421-8de5-3d682711859d | -17.2639 | -42.6527 | 2024-10-16 01:36:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 4629ed58-8612-37a5-b604-995bcb040cf9 | -17.3041 | -42.643 | 2024-10-16 01:36:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| dfc11a82-ce87-346a-9e92-8658d313add4 | -17.0204 | -57.3948 | 2024-10-16 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 971f94db-af20-39ab-ba81-938c1eb4ea3e | -17.1754 | -57.4995 | 2024-10-16 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| fcbc6611-2658-34ba-a34a-9828bfbca724 | -17.1951 | -57.4972 | 2024-10-16 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 215f565a-2288-3a2b-8fa7-5928f7839fb5 | -17.1954 | -57.4767 | 2024-10-16 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| cd332d44-eed8-301a-b2fd-8967e641539e | -17.2081 | -56.6946 | 2024-10-16 01:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| a31af35a-11d9-3b1c-a5db-a343469365da | -17.2177 | -57.3102 | 2024-10-16 01:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| f6245516-fa62-3ae5-acd0-1f5f89a3f04a | -17.8249 | -57.4425 | 2024-10-16 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| fcb5fa71-4c2e-3e81-86a7-cac722c0110f | -17.9633 | -57.4255 | 2024-10-16 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| d2052686-7326-3f98-866f-67cbad1fab0e | -18.2544 | -56.5821 | 2024-10-16 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 7d266fa4-a88a-3e25-aca9-b9b09269f0d2 | -18.2739 | -56.6003 | 2024-10-16 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 6b2a691a-be0b-36c2-b042-b64db753f24b | -18.2742 | -56.5795 | 2024-10-16 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 165.3 |
| 0484f4f2-9e20-384d-ab84-e77ebecbf999 | -18.2746 | -56.5587 | 2024-10-16 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.8 |
| df976327-3c8b-38eb-ad8b-35723ddc9ca0 | -18.2941 | -56.5769 | 2024-10-16 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 44237460-8f72-3a10-a73d-a1f7284eac75 | -3.2228 | -48.931499 | 2024-10-16 01:37:03 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb0d717d-2758-327b-9c29-e365ae80869f | -3.1151 | -53.7276 | 2024-10-16 01:37:24 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbb5d702-d5bd-3130-a7ed-48592c4f3051 | -3.1189 | -53.7435 | 2024-10-16 01:37:24 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24f3eb79-401f-358c-a214-7cc005c5a258 | -3.1312 | -54.2248 | 2024-10-16 01:37:26 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 656bf30a-6007-356c-9c03-f86341a0b43e | -3.118 | -54.212299 | 2024-10-16 01:37:26 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c73d84f8-9cba-303c-b7e7-2c6282db62ba | -3.1215 | -54.227001 | 2024-10-16 01:37:26 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75d53895-5495-3b05-9703-eed4826d0c34 | -3.125 | -54.241699 | 2024-10-16 01:37:26 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d88e0fe-8f51-3bad-b1bf-2219a05ab284 | -3.1082 | -54.2146 | 2024-10-16 01:37:26 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b46bf332-7ca5-3d0e-9e0d-e12efcb9b9d4 | -3.1118 | -54.229301 | 2024-10-16 01:37:26 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f20eec2-48fb-3507-be6f-715da5e8f424 | -3.1153 | -54.243999 | 2024-10-16 01:37:26 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec74d240-0976-3dd6-919f-a5941d2af2a5 | -2.0566 | -56.639301 | 2024-10-16 01:37:52 | METOP-C | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 620707d4-f76d-3675-922c-15cd04ac5c5e | -1.7836 | -55.999802 | 2024-10-16 01:37:54 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README20.md)
