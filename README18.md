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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 702fee5f-53f4-3e98-8968-5f9a1a06b2b3 | -2.6074 | -49.22228 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cd97843a-bc16-3609-bcd8-52349764c096 | -3.40505 | -50.27353 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2e2475b-03e3-3205-b4a8-d97a6a2bbe92 | -3.14956 | -50.60467 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa9c7356-a7c1-30f8-a1b6-93c1bb158a8d | -2.63817 | -49.20798 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 302862df-c991-3181-b83a-c40efc4274f0 | -3.20609 | -44.28573 | 2025-11-09 04:16:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95927c3f-3a28-3849-a879-f2476bddd810 | -4.58315 | -45.62211 | 2025-11-09 04:16:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4dfd26a9-255b-3c72-a70f-15d55c3f42c9 | -5.13662 | -45.7171 | 2025-11-09 04:16:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33b28b36-4734-328d-b0b7-bdcf40f288fb | -3.75483 | -52.10205 | 2025-11-09 04:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fa99e4d-746a-35aa-9727-d36043089d73 | -4.75435 | -47.52563 | 2025-11-09 04:16:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 654b3a10-a2dc-3cd3-b9f8-916f24ddafdc | -4.68399 | -46.40295 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 279a602b-ab3b-390e-a0fd-aa342186020e | -4.14167 | -47.66007 | 2025-11-09 04:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ae513bd-d977-36e2-9fa7-e38ee6c528e2 | -5.38117 | -44.73021 | 2025-11-09 04:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9662715a-1970-3256-b4e3-4f4bd660a7f1 | -3.32039 | -49.12985 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e5dc510-b0c3-3a52-b32e-a21e7b8e0406 | -3.31753 | -50.10735 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a82e0c11-7554-317b-a445-824f0c5de688 | -3.07943 | -52.92057 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3813adb-a02d-3225-ae1e-a2e4061b9cb2 | -5.80915 | -41.34159 | 2025-11-09 04:16:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1f8f00dc-3f1e-3c69-8928-d8b8615897f8 | -3.89705 | -47.18284 | 2025-11-09 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b3efdf3e-faee-3573-ad34-b14ec74fc21a | -3.08918 | -50.32255 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4251d5ba-f7c4-37cb-92f3-cb0217303bb7 | -2.79957 | -48.93852 | 2025-11-09 04:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d1c9beb-0687-30dc-9520-700fc6a5a181 | -4.39817 | -49.6669 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ef81733d-afd7-3b35-b3b9-a094bbe6b4b2 | -4.7969 | -46.01357 | 2025-11-09 04:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caf49cc3-cf1c-3597-9fdb-bc9bca4c12e4 | -3.47651 | -48.97525 | 2025-11-09 04:16:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3cade13-8b4c-3633-9aa8-08c10b6f7ecc | -2.79391 | -49.65833 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfea560d-e23d-3d75-afd6-d0bd6829b717 | -4.14734 | -46.25752 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc48c0ef-5bd7-38f7-9c6c-c9330d6d26c9 | -3.47247 | -39.57327 | 2025-11-09 04:16:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 1a83a787-b29f-3a5a-a80d-1d4a62544d88 | -4.68027 | -46.40234 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe379d3e-b43f-3987-ad69-0e1e9022ded9 | -4.40278 | -44.08006 | 2025-11-09 04:16:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb55c152-b7e6-3407-86bc-51c0924589ca | -4.39659 | -45.16156 | 2025-11-09 04:16:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f5fd115-7b80-354f-b443-6e0bf3388fe1 | -3.30492 | -50.22752 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f87e79c2-a337-3d20-9305-55bd5aff2add | -3.83417 | -51.12976 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1341a06b-ab9d-3ecf-afcd-0e3796836dac | -3.34807 | -50.17944 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6ad38b8-fa62-33e7-9fdd-1d4d3741e744 | -6.02893 | -46.56126 | 2025-11-09 04:18:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 131bf61b-38cc-3dc7-a38c-77d9743729da | -6.72294 | -38.54264 | 2025-11-09 04:18:00 | NPP-375D | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5bdad3a9-13dd-3d6a-8ade-e0040cd151a0 | -7.41208 | -40.07395 | 2025-11-09 04:18:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7e8e3e8e-7c42-3628-95a3-f81110524702 | -10.33504 | -49.63762 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 61ea0065-667c-31cb-a48a-9877146886a2 | -7.49879 | -46.61065 | 2025-11-09 04:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| decd0efe-4d29-3b87-92e9-cad47501af4f | -6.08223 | -42.69717 | 2025-11-09 04:18:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d31bf4d4-4735-3cc2-873b-e198043f3b4a | -8.82222 | -40.6176 | 2025-11-09 04:18:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 267314c1-836b-3730-9f97-c7610f8eb31d | -7.40208 | -40.06546 | 2025-11-09 04:18:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d8686c9d-5b79-3ae1-a717-c64bb8a665b2 | -5.39833 | -47.25957 | 2025-11-09 04:18:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba54b329-97de-3f3b-98dc-09a3b0119e25 | -7.49949 | -46.6064 | 2025-11-09 04:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 576bf333-d946-33a7-b0ff-2a5008247f2a | -5.0995 | -56.16238 | 2025-11-09 04:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91c10d8e-b74b-3e3a-944c-fb4e8b6e0f1c | -6.86001 | -40.15475 | 2025-11-09 04:18:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b0a6f405-1fc2-33d6-84d8-90a991c51163 | -5.09259 | -56.16103 | 2025-11-09 04:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baff46c9-0ef7-33b8-b65a-b0d19158c6eb | -10.06131 | -38.55511 | 2025-11-09 04:18:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b9d2a861-c812-3d9c-8f7b-41719c2e39ae | -5.50426 | -47.20039 | 2025-11-09 04:18:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 523c6474-27cd-39c4-ba30-a3661c403249 | -6.88276 | -49.24762 | 2025-11-09 04:18:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77efbc51-b056-3783-95b6-a300796b0e62 | -6.68744 | -46.66813 | 2025-11-09 04:18:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5505bd2-db5b-3b71-9d2c-7a6ae7fc4116 | -7.40843 | -40.0734 | 2025-11-09 04:18:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 229ae0c2-a8a6-3a41-8f34-3d86c237c2a3 | -7.55799 | -45.85504 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 535ac4a9-b2af-35c6-8b6d-a935c6404fb6 | -6.26925 | -42.24011 | 2025-11-09 04:18:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 183b2aba-78f8-3e74-85f4-efccbc5680ec | -5.39878 | -47.26176 | 2025-11-09 04:18:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a14cf5e0-3940-3b91-9066-1944372d47d8 | -5.84823 | -46.4486 | 2025-11-09 04:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc04122a-eabb-3b14-873c-105e26f2abb4 | -6.68977 | -46.66724 | 2025-11-09 04:18:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| defef6ee-d94c-3a35-b00e-3b9c8093de2c | -10.33639 | -49.62996 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8cf85c60-de3c-36ce-acdd-ef320b69e0f6 | -9.87531 | -40.5718 | 2025-11-09 04:18:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0866130d-e26f-38b0-a6e2-a634fe94ad1a | -10.06543 | -38.55585 | 2025-11-09 04:18:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea6d7d0f-fa3a-3336-a986-3b5570242a55 | -6.9949 | -42.78748 | 2025-11-09 04:18:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d368d4d0-0f65-3417-8018-34576533a4f8 | -10.33222 | -49.62921 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| cf96ccab-12f4-38c3-811e-bfad10e93af4 | -12.11036 | -43.64234 | 2025-11-09 04:18:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e91948c2-064e-3692-8e73-bdc22f29c339 | -8.36156 | -49.94384 | 2025-11-09 04:18:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce89be41-1a3f-3383-9005-d7653e8fa273 | -8.20046 | -45.70255 | 2025-11-09 04:18:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e910b78-7cf1-33ba-9812-1ec8ba88a26d | -7.13915 | -46.413 | 2025-11-09 04:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2569d5b6-a692-35a0-b244-1c349f335e88 | -10.33989 | -49.63454 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| bfd44e36-a6ca-31ef-813a-f76f23f51952 | -7.40906 | -40.06916 | 2025-11-09 04:18:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bab4a538-1ea3-3bf5-8598-1e5a960014cc | -6.43 | -44.68117 | 2025-11-09 04:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1b71a6a-52c2-3f12-be89-f2aa6915b898 | -7.40572 | -40.06601 | 2025-11-09 04:18:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 03e5bdd3-57a0-3e72-9d68-8cbfc6cafafd | -6.01971 | -43.7763 | 2025-11-09 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2d3a994-987a-39cc-9974-e1a84546c7de | -6.64128 | -43.54973 | 2025-11-09 04:18:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efb771b7-322c-3e84-b9fa-75948dfd492a | -7.54396 | -45.85278 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2aee526-755c-39fe-a47f-df2d4c025492 | -10.33572 | -49.63378 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e404310b-33d9-3ff8-ade8-80a59a41c802 | -6.85378 | -44.84954 | 2025-11-09 04:18:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fed74cc-55df-391c-8f9a-35bf6679991c | -8.70871 | -41.1253 | 2025-11-09 04:18:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 660ef4a8-ec9b-35e4-b61a-d94c0bba1e34 | -5.57612 | -47.13075 | 2025-11-09 04:18:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03390639-534b-30fc-977b-a9784c107b12 | -7.9517 | -46.84901 | 2025-11-09 04:18:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5126fc53-548a-3df4-85f4-f81b83d859a9 | -6.68814 | -46.66381 | 2025-11-09 04:18:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2798824-e091-335d-aafb-5424bf42a131 | -7.94804 | -46.84838 | 2025-11-09 04:18:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc13c8af-7ea0-3e35-8f5c-315349310149 | -7.27577 | -41.03199 | 2025-11-09 04:18:00 | NPP-375D | BELÉM DO PIAUÍ | PIAUÍ | Brasil | 2201572 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a55ffd54-95c5-3b43-8ac2-e59535da1132 | -6.12751 | -52.64131 | 2025-11-09 04:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c57690dd-67bb-39aa-b80c-f192cc402c3a | -6.46173 | -44.6786 | 2025-11-09 04:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e11340f-fb6e-303f-9d11-b80d5776330f | -6.99823 | -42.788 | 2025-11-09 04:18:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 490690cd-1759-3256-95c2-d90c8767b4a0 | -8.92647 | -40.27213 | 2025-11-09 04:18:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb09bfc3-f5d6-3cbb-906e-4cd020f8b398 | -7.27505 | -38.72343 | 2025-11-09 04:18:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| abff5895-aec3-384f-97ea-35387c237279 | -9.8782 | -44.5798 | 2025-11-09 04:18:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 241f99aa-1b44-337d-9f4f-4017cfb3be1f | -7.54747 | -45.85335 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5aa5d05-623a-3a6d-b52e-ec83265b6cd0 | -5.86067 | -44.70378 | 2025-11-09 04:18:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48e0785c-e84d-3dfc-9c01-e746378e94f6 | -6.34314 | -46.76554 | 2025-11-09 04:18:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d152f88-cba3-34f9-a6c2-11e60988a7c0 | -10.07198 | -45.60736 | 2025-11-09 04:18:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f6cc1b0-0c33-3976-86bf-a8becff6dc5a | -7.27229 | -41.03143 | 2025-11-09 04:18:00 | NPP-375D | BELÉM DO PIAUÍ | PIAUÍ | Brasil | 2201572 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c4e12d7f-5035-3e31-af6e-e8b2f04ba7bb | -7.14275 | -46.41371 | 2025-11-09 04:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfc22e36-da1b-3991-8427-48d9d59dfbea | -6.88707 | -49.24839 | 2025-11-09 04:18:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea43c641-1f17-3fbc-bb7a-41da0dea4349 | -8.12547 | -47.85368 | 2025-11-09 04:18:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81ebf187-923c-3f56-8100-a09381883aed | -5.22772 | -49.57901 | 2025-11-09 04:18:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fa6f695-7e49-3cec-bd12-5e02f4b87b2a | -5.73639 | -46.45608 | 2025-11-09 04:18:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03118141-207d-3bd6-acc6-7d1875d9735d | -7.27373 | -38.72485 | 2025-11-09 04:18:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| af320371-56b3-398d-b9b7-d111960cd048 | -7.17673 | -44.95017 | 2025-11-09 04:18:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 45c90f93-c847-35a9-8488-d9759358b798 | -10.34474 | -49.6315 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 74a8931d-f917-37c5-9554-dba26ad54a8b | -5.40346 | -47.25761 | 2025-11-09 04:18:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfc9f3f3-6139-3f00-bd3a-79b65e035fd9 | -6.98733 | -39.06911 | 2025-11-09 04:18:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cfc05d5a-5495-342a-95a1-558e7905cf63 | -6.39821 | -44.4906 | 2025-11-09 04:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README19.md)
