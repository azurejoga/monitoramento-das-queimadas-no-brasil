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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bd4753b-1a3c-36a0-8723-d290254ab15d | -10.16009 | -44.54792 | 2025-10-12 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f024d979-7eb6-3fd4-989f-3bd0734d4cc3 | -9.23769 | -47.0492 | 2025-10-12 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5fcc98a6-04a9-35a2-83ae-2a0bb7eb8561 | -9.24158 | -60.50124 | 2025-10-12 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ab3bbae-2554-3f7a-948f-98199621bae2 | -10.56838 | -59.48643 | 2025-10-12 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dda5e790-48fb-3eeb-a17d-9166d03b1173 | -10.55952 | -57.52286 | 2025-10-12 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96c7aa72-e7c2-3b6b-904a-7627724f5b5e | -8.50762 | -45.95215 | 2025-10-12 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3697f021-a0b6-3480-82b3-aeabeb03f85c | -11.85335 | -56.86621 | 2025-10-12 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a865e3c7-91b3-323e-894a-e1bc163591e0 | -13.35782 | -61.34181 | 2025-10-12 05:04:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8d314af-b90c-397d-88b0-eb1d2fa474bb | -8.83516 | -46.04182 | 2025-10-12 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b99d30f2-f149-3d66-89cb-9c66330899fc | -9.42228 | -61.88487 | 2025-10-12 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0fbf89e-3615-38f8-88f6-6f8a8d2ab2b7 | -8.47731 | -46.21609 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7214815-cc8d-32a5-b320-4637311dac47 | -10.72829 | -69.45403 | 2025-10-12 05:04:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89ede8e0-370d-3a00-ba9f-956c48d368f9 | -10.86684 | -61.9815 | 2025-10-12 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24017e35-a8c7-352a-b9ba-ca108a499ed8 | -8.47426 | -46.23834 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d31c4ab-6158-307e-9faa-17caf5d6b0fa | -12.215 | -64.37058 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ea953c4b-53bc-370f-aeb6-b634cee5ed6a | -8.70259 | -47.0578 | 2025-10-12 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbaa1b06-1e04-3813-a29e-8dcd699c5229 | -14.91831 | -46.77651 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aeb3d986-4cd1-3a65-826e-3e35dfce1a65 | -14.9476 | -46.72676 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a10d3d2f-55dd-3341-9d40-01726df43987 | -11.07357 | -57.87872 | 2025-10-12 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39e749da-4fca-34a9-8942-9aeeab281205 | -14.95924 | -46.72931 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 714bf8e0-c832-3fc6-91fa-406d97e41093 | -14.94083 | -46.73412 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9b475279-0ff4-3f60-9a80-e6768000de9c | -12.29626 | -64.03054 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c29ee896-1bb6-3b87-b92d-ad0c563484cf | -12.3988 | -63.70735 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dafac44f-6a33-3dec-bf74-a2673117e1d0 | -8.47411 | -46.22803 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b87f3054-0c14-331c-9031-40fadf51d678 | -8.47602 | -46.21329 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 746ad063-45cb-33b3-8fbe-23fdc71a62bf | -14.92746 | -46.74729 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4c3502ca-c74b-3b66-9c90-f88bf40ac237 | -13.57081 | -46.34827 | 2025-10-12 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36e8ea02-1eda-36d9-9599-ac68d7be173b | -14.9598 | -46.72436 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 25c645c1-27b3-3066-84ca-414bfc57a166 | -14.9404 | -46.73801 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d374ec09-11f7-322b-8570-5c76fb33517d | -14.02816 | -48.15574 | 2025-10-12 05:04:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdbb83ae-6467-3e3f-adfe-d921c436f767 | -11.25013 | -61.17292 | 2025-10-12 05:04:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 75fd1401-b145-367b-91f2-af58fcf12808 | -10.67856 | -62.26079 | 2025-10-12 05:04:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d49d25f0-a664-369d-95e2-5d704e3b0ee5 | -10.78571 | -43.95498 | 2025-10-12 05:04:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5aa42117-413c-3297-b90a-5b8a772defef | -10.17369 | -44.54248 | 2025-10-12 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38823d7d-29c9-37e1-b5b9-81452a7a5a8d | -13.01473 | -61.43537 | 2025-10-12 05:04:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5e38df5-7ac5-336d-be58-6147f5cb6397 | -12.39077 | -63.87671 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ee49f75-7e40-3091-b2e6-e95e3f83cc09 | -10.67926 | -62.25689 | 2025-10-12 05:04:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5391cac-434d-3e96-bb65-3d95945ea0ce | -13.57343 | -46.34635 | 2025-10-12 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9995d7ac-abfd-3479-af19-052e48e643a9 | -12.12822 | -62.04159 | 2025-10-12 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eeda4c71-5b86-3fb8-b41d-0c1643d2d62f | -10.67749 | -62.26095 | 2025-10-12 05:04:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4034abd-eeb4-3440-b87e-b3413251028e | -11.93484 | -58.4547 | 2025-10-12 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e641ee8-a047-3e5f-b5d9-ecc6542d9f35 | -10.15572 | -44.54912 | 2025-10-12 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7e1341fe-dd40-38ba-8383-2d6af1b44322 | -10.78085 | -43.95781 | 2025-10-12 05:04:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9e5c1e7f-27f9-3ed5-bf52-0d667f99a3cf | -9.07732 | -48.03301 | 2025-10-12 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98aa0fc4-24f3-3b65-b347-55cfb3ad8b23 | -12.36389 | -56.85878 | 2025-10-12 05:04:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7ff85c5-56ce-3334-bc4b-09994f1ee4eb | -14.96929 | -46.74612 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c4203a3d-99dd-3d5c-be4a-005b7d54ae68 | -9.23812 | -47.04589 | 2025-10-12 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32ddecbd-85a3-3d99-86ef-1c109b4a5a6a | -12.59259 | -62.01822 | 2025-10-12 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00f06a39-cb5f-3e39-8793-12dda182bb11 | -14.94574 | -46.74355 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f5de83b-edf9-31dd-8a32-19f99151547a | -8.47824 | -46.24 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d81c78c-3b69-344e-8c30-43bba9085762 | -11.85004 | -56.86567 | 2025-10-12 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d0800ed-eaef-340c-93bf-39e7ff629042 | -8.47872 | -46.23627 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 723c9dec-0461-3527-b862-bd21d5148825 | -14.95347 | -46.72763 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fbd4d912-429d-3eaf-99f9-253cc8d30e21 | -10.63464 | -69.35397 | 2025-10-12 05:04:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4efdf632-9be8-3e44-a59e-282d973acf80 | -10.15515 | -44.55395 | 2025-10-12 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 072c4480-3733-38d7-b8b3-d2bbfe05b8d8 | -12.12742 | -62.04174 | 2025-10-12 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67b5bec5-de6c-3147-97fa-aa0e3d6f53de | -14.96982 | -46.74133 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f274a3b-a75f-3b71-b04f-81cfeffa3863 | -12.59445 | -62.95101 | 2025-10-12 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69078633-7c69-32a4-a119-5b5cd181b854 | -14.94127 | -46.73007 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b0d9c57-aedf-39be-bb91-8d4b8f3b27f5 | -10.15305 | -44.55261 | 2025-10-12 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3459c419-192b-39b7-a9fc-ffcf4b36be18 | -9.07824 | -48.02838 | 2025-10-12 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e961f9d-4ebf-3bec-8fab-d38abe4e7abc | -10.56906 | -59.48233 | 2025-10-12 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b53a37cd-2911-3e4b-a989-bacb42e16a02 | -8.47647 | -46.20975 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cff81272-41a4-3e2f-b990-24fef848fa08 | -10.78153 | -43.95226 | 2025-10-12 05:04:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27d93ed5-5e7a-3592-9503-b6cb047c492c | -14.93971 | -45.58657 | 2025-10-12 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d15f6235-c730-39cc-849a-e4aac98b0991 | -14.93997 | -46.74183 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 06b8ca39-b7c8-3159-860a-a19ec624bc98 | -9.07812 | -48.02728 | 2025-10-12 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77493a52-1522-3742-8f08-8bd40fa88c83 | -14.03386 | -48.15307 | 2025-10-12 05:04:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5024042e-ed64-34fb-9309-ff893546aa35 | -8.47314 | -46.23548 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50001008-d0a4-36ef-b6c3-04d70ac641cf | -14.02098 | -43.48621 | 2025-10-12 05:04:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6d1aca95-48ad-3324-bb50-fafcd63cc300 | -12.58383 | -62.9615 | 2025-10-12 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b62d1e38-3fa8-3d06-bf74-2145b088e780 | -10.564 | -57.5163 | 2025-10-12 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57c05a19-0436-352b-ad90-a2111af3c382 | -13.46786 | -60.97606 | 2025-10-12 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1b9ea61-cc1b-3ac2-8248-84b071e2f2cb | -14.02806 | -43.48696 | 2025-10-12 05:04:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06bb5927-d5c9-337f-a1ee-665ca212aedc | -10.97792 | -61.60751 | 2025-10-12 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd002bd9-c980-3928-a226-112fffb36a9a | -14.96035 | -46.71938 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| dad04be9-ac42-32bd-91fe-1c6a5653fb85 | -12.20753 | -64.35858 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a97fac0a-1fb9-3954-ad1b-6cc7049f0b96 | -11.49707 | -43.49367 | 2025-10-12 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d028f11-b834-3ecf-84f4-87c3fb8419d2 | -14.02028 | -43.49315 | 2025-10-12 05:04:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 559de8a8-fc9a-3815-bc11-958d23aa6962 | -12.24056 | -45.34407 | 2025-10-12 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebaeada5-fb30-3607-aabf-58c2a6362d64 | -8.47458 | -46.2244 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c73670ce-8ab1-3541-b4f6-0c3dbfd88998 | -8.70214 | -47.06118 | 2025-10-12 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 346831a1-6701-323a-90bf-b492c64fbb04 | -11.85665 | -56.86675 | 2025-10-12 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2d49da1-3236-3161-a423-9f33aedb6457 | -8.47781 | -46.21244 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0edbeff8-63b7-3819-a561-8d4f5cb63e57 | -12.09653 | -64.24196 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfcfcd6c-ace5-320a-855d-410c8ff4208b | -10.63601 | -69.35795 | 2025-10-12 05:04:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20c136b8-bb2f-3c33-9837-58a784ffe637 | -14.93375 | -46.74426 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 965924e7-7366-3701-b95a-4999403cf8d0 | -9.84579 | -59.79422 | 2025-10-12 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a85087e-6a16-3993-a662-94c0b171558c | -9.76106 | -65.05494 | 2025-10-12 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86bbc63b-b8a7-3a4c-85fc-57a22d19e272 | -12.2917 | -64.02963 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cef9f9f9-36ae-3d8a-a9ed-3bdc9f7406fd | -10.14605 | -44.55695 | 2025-10-12 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d63d97dd-4c4e-315f-ad20-ac4507f3a6a9 | -13.01388 | -61.4402 | 2025-10-12 05:04:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2469d6a3-6414-3c4a-bc4e-1c7a29d0b325 | -12.2122 | -64.35951 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c56e5b10-0d14-3075-a3e1-a523962f3941 | -14.9333 | -46.74833 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3ddf596b-6696-3695-84f0-df1a2f31d4d3 | -12.21407 | -64.37566 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66510e98-3a6e-371e-858e-3e274c04ad0a | -13.46416 | -60.97538 | 2025-10-12 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0fddf649-505f-340a-94cc-dee4b9935087 | -9.08313 | -48.0278 | 2025-10-12 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98926dfa-287d-3f62-a1ec-47a243614d83 | -11.76136 | -61.06662 | 2025-10-12 05:04:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a47357f0-1b13-394a-9277-0e37b1cc939d | -8.47477 | -46.23461 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b275ad7a-2860-34eb-b4c7-f6d5a555dcd8 | -10.5601 | -57.5193 | 2025-10-12 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README41.md)
