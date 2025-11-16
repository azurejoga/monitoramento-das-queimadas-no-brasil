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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d95f953-d0d8-32eb-ae5a-8695469a974f | -7.05211 | -42.25102 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 4e3dbdb3-f984-3015-bfb7-b14b1fb4da80 | -4.33534 | -50.55415 | 2025-11-16 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 1c54efa6-f495-34ba-b91a-cd0a47f41ed5 | -6.32104 | -43.81051 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c7371074-e5d6-3a21-98cb-836d595176df | -5.07929 | -44.7458 | 2025-11-16 00:13:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dbdaaaf4-51f4-33c3-ab44-cebd54a2d107 | -7.0502 | -43.95066 | 2025-11-16 00:13:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a553f85d-3388-36b2-bc76-ef438ddc7277 | -7.00816 | -45.15952 | 2025-11-16 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8636e626-96e8-3623-a938-9a6b4d4fd665 | -7.79357 | -46.53259 | 2025-11-16 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d1804384-e56c-3bc9-914f-4bedde8886ff | -9.72379 | -43.96059 | 2025-11-16 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 2b86e0fd-a059-3a9e-bba8-47ffe7368aa0 | -4.84135 | -47.55688 | 2025-11-16 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 1e37853b-a158-3347-af14-b909bb9183a6 | -9.75045 | -43.95666 | 2025-11-16 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc6d0bd0-db97-36d6-a012-8f6ae9e5d6e0 | -4.58569 | -45.17148 | 2025-11-16 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b2182b26-888b-3f43-9dce-658a0cb11ee4 | -8.31992 | -45.40074 | 2025-11-16 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 67cfe81d-aec9-3804-91d4-c25fc0d83b1a | -3.75469 | -43.97049 | 2025-11-16 00:13:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e2e19da4-ab1f-3af8-8d14-32a50d148981 | -4.42672 | -45.5488 | 2025-11-16 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 30.0 |
| df564d81-59bc-3500-8702-ca5e7bd397e3 | -10.06695 | -45.51698 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 071c298d-0f48-3e75-8c84-ceca22329e6b | -4.50537 | -50.11157 | 2025-11-16 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 4e08ef1a-3889-37f7-8db1-455952a03003 | -8.95717 | -47.52165 | 2025-11-16 00:13:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 72a1a4a5-a274-3ce5-b0be-c5382b531d66 | -4.40022 | -45.82813 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 7667b09f-96cc-30aa-9698-c9348889c6e3 | -9.65976 | -43.9026 | 2025-11-16 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 5dade577-a4b9-3ac6-8ad2-bb24782366d9 | -4.39205 | -49.66714 | 2025-11-16 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 30c20183-578e-3a95-8384-9863cd661c31 | -8.33759 | -41.25295 | 2025-11-16 00:13:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 30.5 |
| 4fcb993c-7c88-35ea-aac4-465f4f1b080a | -7.49665 | -42.56558 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1926e2ed-8b21-3fac-9026-beba2ee6376a | -9.62181 | -46.7316 | 2025-11-16 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 696b02a5-f05b-3ab9-ba9e-899e6ac9f792 | -9.34577 | -46.58561 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e0b1c61c-8225-3acb-8cef-467df27059e4 | -7.38725 | -45.51211 | 2025-11-16 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dc60a91b-d4f6-3761-a959-b3559b0f54d3 | -4.84413 | -45.43251 | 2025-11-16 00:13:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a6d4b8c6-06bb-3b0e-becc-24721fdbf3e9 | -7.05047 | -42.23991 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 378aa4e5-b26a-3ff4-9666-d07dfd2a50ce | -6.68244 | -40.79615 | 2025-11-16 00:13:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d7d3a3c7-00ee-3a38-92bd-0bf6f1365d6a | -3.99975 | -45.79227 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f697ccb9-9248-3696-91e3-365fa0a2a7cc | -5.98885 | -41.908 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 540085e7-7b24-3286-8ed2-e620c77a252a | -8.10387 | -46.03891 | 2025-11-16 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fc30ba8f-62d2-3852-88f0-3c57691aa411 | -5.74726 | -49.46504 | 2025-11-16 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| f4821a86-1134-303a-9ad9-4e0cae7d9dab | -10.00451 | -44.78381 | 2025-11-16 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 3414669b-43c0-33ff-89a4-60429ee76720 | -9.5744 | -44.61247 | 2025-11-16 00:13:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a0c3b8c0-11e5-31cd-87fa-e1dd701262ce | -9.8447 | -44.16631 | 2025-11-16 00:13:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c58e047a-7ab8-37ba-989a-c7a4d6f856b5 | -5.24727 | -43.9035 | 2025-11-16 00:13:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 63940e7c-8b75-3116-ae29-7685385335bb | -5.27528 | -49.32029 | 2025-11-16 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| f27c8a4b-9b45-3837-8548-3e1df0df84b7 | -6.74925 | -48.19535 | 2025-11-16 00:13:00 | TERRA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 77965b92-37c3-30c6-8c16-d57f375202f7 | -5.62878 | -43.93044 | 2025-11-16 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c67d6da7-a70e-373f-ba8f-641f9d51d609 | -3.83893 | -40.77758 | 2025-11-16 00:13:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 18.5 |
| d670a244-fc2a-3f34-a029-9f69a0cab106 | -3.55411 | -44.97451 | 2025-11-16 00:13:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 98fe9534-adb6-376e-a59d-1e4ffd50c4ea | -3.86197 | -40.77436 | 2025-11-16 00:13:00 | TERRA_M-M | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| fd4919fb-a239-3c2d-8f2f-fab6ae8dabfa | -9.05623 | -44.79613 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2e1f7a49-6a85-3bc1-845b-3aeeae86677c | -5.68449 | -45.98578 | 2025-11-16 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6a49e964-12b0-3ad7-afe1-ba3132ceb1be | -6.37123 | -39.63029 | 2025-11-16 00:13:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 5f23996c-16b5-3c29-b0b6-bc914574d553 | -4.96217 | -44.04003 | 2025-11-16 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 42c57eaf-79bc-31b1-9962-6c6dfbe2f7b0 | -6.14815 | -48.04834 | 2025-11-16 00:13:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 03c415e9-c391-324d-8c36-3bd55c11a123 | -4.58661 | -44.3189 | 2025-11-16 00:13:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 579aade7-cb00-3374-8d7e-63211e576929 | -4.5786 | -44.32635 | 2025-11-16 00:13:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9dbc3dae-4f8c-3581-95a4-4aca225c27a4 | -6.00854 | -41.91137 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 08010b3a-b2db-313c-a133-a9f2b7a9f3dc | -7.38848 | -45.52102 | 2025-11-16 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 48c297b2-e19e-3130-bfb7-29559040ca99 | -7.72261 | -47.30098 | 2025-11-16 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0c33e615-96cb-36a0-861b-e961617c249d | -4.308 | -50.87424 | 2025-11-16 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 40c897db-6835-3d02-bfe5-2e8e788fe895 | -6.69545 | -40.80842 | 2025-11-16 00:13:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 1ecd33a8-979c-35a0-b007-0810aae8b149 | -3.66164 | -44.81781 | 2025-11-16 00:13:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 457afa55-86be-35c0-9162-09786ca50fc1 | -6.6845 | -40.80994 | 2025-11-16 00:13:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ca81e24e-03d6-3888-a6cc-bcf5c4031953 | -4.65518 | -44.47855 | 2025-11-16 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ca877069-af44-3688-9f59-ffa7ef4c8292 | -9.52726 | -40.33958 | 2025-11-16 00:13:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 2c62f794-fdd7-3de8-9960-728668f121fe | -7.29561 | -45.10926 | 2025-11-16 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e7969732-f7a2-339a-be7d-e1f3ad4e9f41 | -5.03825 | -49.06113 | 2025-11-16 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 13e4d870-5297-3e54-b1a1-7a6775672451 | -7.64184 | -38.91459 | 2025-11-16 00:13:00 | TERRA_M-M | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 39.4 |
| 93b0ac38-e075-3f33-ab7f-a5cca8243f24 | -9.97064 | -44.27871 | 2025-11-16 00:13:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e84b13bd-021a-3a32-9c1c-2ff98a503512 | -4.05207 | -42.09914 | 2025-11-16 00:13:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 45247791-b6e0-34bc-a979-6477b360c3cc | -5.21164 | -47.57162 | 2025-11-16 00:13:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fdbd8b40-e057-3439-a5b4-6bf0f2ce3a2d | -3.99881 | -44.26461 | 2025-11-16 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0eee8907-5075-32a4-a713-20e64fb2a7de | -3.86427 | -44.02729 | 2025-11-16 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| cddab4db-3e51-3644-9ab5-2bd0848d8a0e | -9.10569 | -40.451 | 2025-11-16 00:13:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 3ed3e23f-289b-3459-9abe-605d7c3446f8 | -4.6814 | -46.72932 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| af19d08b-768f-3929-921b-54518287049d | -8.55528 | -47.78938 | 2025-11-16 00:13:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c28c9da0-25a6-3ad6-a552-185f66afe33a | -9.12777 | -45.17048 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ca37b4d3-659a-33dc-859f-4dad98b97ac5 | -3.94546 | -47.2044 | 2025-11-16 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 738355c0-2b99-33d9-bb04-0d30d6b4524d | -5.28412 | -44.29928 | 2025-11-16 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 630bc802-71cd-36cd-afe8-0c74b77917db | -4.9635 | -44.0495 | 2025-11-16 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| c91e4a55-fd2b-37bd-8a39-a0a95f1cad01 | -9.72504 | -48.89417 | 2025-11-16 00:13:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6a0ebc8a-1a0d-3d1c-bfeb-73d608b0ed21 | -5.3599 | -44.90699 | 2025-11-16 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9189b55e-b4a2-3be9-88f7-8b1e46ea2a67 | -5.75627 | -45.10711 | 2025-11-16 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 65a48ba9-73d6-3ef8-b997-e8722809a990 | -4.73666 | -46.39421 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c3dbe149-e500-3537-b68f-1891ca4504e6 | -9.85622 | -44.71705 | 2025-11-16 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 4e6c65df-f2ef-33d5-82e3-32bd7d07dda1 | -10.01213 | -44.77361 | 2025-11-16 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 37f5f816-1d2b-392f-9baa-480566e93ffb | -6.08769 | -41.60789 | 2025-11-16 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 4725610c-fc8c-3a3f-9bd6-382eacee3cb2 | -4.69898 | -46.31763 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 153.4 |
| c8e34018-b0b0-34d2-b717-baa83d6c4b09 | -6.51316 | -47.62769 | 2025-11-16 00:13:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fdcabc11-28d7-33a2-801a-cba05f531a28 | -4.4112 | -43.40082 | 2025-11-16 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 47a897fb-a16a-3a95-8c54-a15406d230e6 | -4.72531 | -46.37754 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b4f61bcb-a119-3b93-b7a8-86a538da65f2 | -4.73421 | -46.37634 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 103.9 |
| e84f0858-ef46-3986-9f62-537e56cd78cc | -9.73394 | -43.96829 | 2025-11-16 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 90b73f25-64cc-3155-87f3-05810b9577e8 | -7.22261 | -47.98283 | 2025-11-16 00:13:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 5e49b890-61e7-33b0-8950-b37ec3c625f8 | -4.42794 | -45.55761 | 2025-11-16 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 6f1da3fd-7d26-32b9-81f6-4571af08d89b | -4.09848 | -43.34891 | 2025-11-16 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a9187ce5-a8a0-3398-8600-4f2357628654 | -5.46811 | -40.99372 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 4195f976-6c07-3542-829b-9b557608cc0d | -4.41264 | -43.41098 | 2025-11-16 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| db8a02ed-68cc-3ff5-b947-456ee638a571 | -7.12587 | -46.15872 | 2025-11-16 00:13:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9392de31-5526-35fe-9630-bae0f136bbd2 | -4.68986 | -46.52579 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 00bb5624-867d-368f-8fb5-61a5a7e4b9fc | -6.70432 | -40.79293 | 2025-11-16 00:13:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| c6807c02-ccc7-3c9f-8ea8-976fb1d49880 | -7.09052 | -42.74203 | 2025-11-16 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 9a285553-3415-3a99-a70f-6177c3cfa27c | -4.64873 | -44.62854 | 2025-11-16 00:13:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ac1cfc3e-239e-35c1-95bf-699c816e9fe5 | -5.18586 | -49.33886 | 2025-11-16 00:13:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 24586df9-6805-3241-b965-98b6c629e793 | -10.53934 | -47.99594 | 2025-11-16 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b9b1c248-3c2d-3c0e-a0f2-b12b3bfcb9d2 | -8.06457 | -43.11094 | 2025-11-16 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 445170fd-fe6b-30a2-a423-c7b1cc670f4f | -9.10778 | -40.46459 | 2025-11-16 00:13:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 55.2 |


[Clique aqui para ver as próximas entradas](README6.md)
