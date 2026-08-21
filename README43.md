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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee0173f4-bec1-3505-9194-a0a4375355c8 | -6.43683 | -52.73176 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dca7463-d298-33a6-9a67-d252e17f6d5d | -5.66562 | -51.64684 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ce196d7-7e4f-3b0b-979a-fea6ead9eca2 | -10.72329 | -44.78234 | 2026-08-21 04:46:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 60afe635-a2dc-34e0-9678-03a14e94818e | -11.32778 | -45.01543 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 053c40f2-fc83-34cd-84b4-7b0a55801117 | -6.43299 | -56.18683 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeeb5272-9908-348c-a792-9e06eaa30403 | -7.77835 | -61.16657 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 05260f77-aed3-3243-a800-b60087abb21a | -9.40532 | -60.42183 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 65d3ae16-51ac-3f89-844a-35a09a65d326 | -9.07067 | -60.43309 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15f550b6-5913-3e62-ad0e-b9e489bfc242 | -7.02024 | -48.0386 | 2026-08-21 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| eeed3f18-4228-3d29-be6b-42444a722d2f | -4.44567 | -55.3919 | 2026-08-21 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5958f722-5df9-3f2d-b758-f581177e6f44 | -6.24445 | -43.68446 | 2026-08-21 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aafd9ef8-1415-38be-ad93-c7de692eea69 | -9.05776 | -50.88918 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8904c270-310c-30d0-93da-e31e419cbea4 | -6.01682 | -57.80558 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e01d4464-3992-39f3-a738-cd96d354a8dd | -11.493 | -45.10611 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02feba2a-19c3-3e0e-b1bd-b7eb7aea9924 | -6.24519 | -55.42229 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5c4138d-3e7e-353b-80b2-3e3709b4fafb | -11.08727 | -47.59608 | 2026-08-21 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 467b1d9a-2ae5-3225-814b-d9f7adc316ab | -7.27318 | -47.45647 | 2026-08-21 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9782fcac-9ac3-305e-8639-cb32d3c39a8b | -9.22011 | -59.65696 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cbdd676-487a-3a56-a305-3f7a36f6aba9 | -3.84415 | -59.38075 | 2026-08-21 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51923cd8-665e-3313-9925-3b51995e3b5c | -6.89977 | -55.71968 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bae49e3-fb95-3e5b-8660-7e4b1549a7a3 | -6.71312 | -59.08784 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20b57d22-4e80-3776-ae90-7f263918752a | -5.8235 | -57.63836 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2ba51d0-c349-37c5-b0d4-424b7ece7d44 | -6.72096 | -59.10027 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87ae4586-9b1d-3efc-91b0-e97b32976178 | -9.21587 | -59.78178 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57d94039-ecea-3bfb-8430-df3408245417 | -6.80586 | -59.0146 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2e27a849-2886-3031-a87e-daac38f77df9 | -10.52171 | -50.78046 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68b0fff2-9798-399e-9173-37ab8eef1f69 | -6.22698 | -55.48351 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5b79fd4-3065-3ca8-bdd1-94cbf02257e8 | -8.53903 | -55.3172 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07a51cfd-f204-361b-b0d1-5d184b81b60a | -9.21831 | -60.77446 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 037336f3-3a0c-39bb-bbb5-38d8b23ca7c5 | -4.4685 | -55.40077 | 2026-08-21 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d74a83fe-46b5-3c1d-bf0e-af910d12ecee | -11.49425 | -45.1053 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a2938e1-a7eb-31ec-87c4-339d75db25a4 | -6.6538 | -56.34468 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b78bb40a-9edf-3076-9401-4150eb8de573 | -4.0501 | -50.29932 | 2026-08-21 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1006d8ed-0229-3619-b269-af6b0637cfc2 | -7.37508 | -45.8078 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 79766432-6415-34a6-b0a2-bddcb10eea92 | -6.00857 | -57.79942 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e1d3d73-47fe-39e4-a557-2219fc179d12 | -9.11465 | -60.33739 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7da64b2b-2875-3ff7-b380-94ce93e10261 | -8.55545 | -55.32289 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d5fec98-d754-3068-9a0a-32d27bb38cb0 | -10.80481 | -50.27459 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 568ae122-7cfd-3f31-a8eb-5d5d8e4bd767 | -10.7725 | -50.30399 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 861a99ff-c289-37e1-ba0b-c80b94113b5f | -8.58911 | -54.71373 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6f91ac5-9635-3225-ae16-f9a6bbe49e1e | -7.6054 | -60.96019 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50c18017-c414-3100-bc12-9e6bc92ca35d | -3.84693 | -49.04428 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 041d34a0-26a8-3a0c-9283-2db361502ca6 | -8.09716 | -51.66989 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6078bb51-b6aa-353b-aada-8fbf3975af5c | -9.21097 | -59.78094 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c187c618-2d46-3350-8038-c61246c6abfb | -9.21526 | -59.65602 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6540a305-775f-3953-8296-6b8de3e74f4a | -8.58111 | -54.78494 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a477ed02-db43-3da0-89d1-b3196ef35ac4 | -9.50387 | -51.67664 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e52672f-1672-39c2-8d28-abca750629e8 | -6.01299 | -57.82834 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90bd94dc-898d-3dde-be0f-534abf7b016a | -9.17674 | -57.00183 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7593edc-8125-3ba1-af84-9a7541760fea | -6.95765 | -52.81395 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6913a21b-4d9e-354c-b050-099ed58803cf | -8.61848 | -54.71436 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aed99dac-cef0-3d0c-ae12-9f0014c23ac5 | -7.05673 | -56.50854 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bebe0371-2898-3282-a304-635ac0cc1309 | -4.11302 | -48.9323 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8cf070b7-ff22-32d1-b81d-16d218d6694f | -8.4541 | -46.95773 | 2026-08-21 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33089a00-d32b-30a0-b95b-ddc01f2498ac | -10.6338 | -51.60162 | 2026-08-21 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 28fc283d-dccd-3ac3-87fb-d326213bf5b9 | -4.10812 | -56.36556 | 2026-08-21 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d883de8e-1262-3071-b765-a664028339c3 | -6.77235 | -59.45168 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea8c020f-8e9e-35b2-9fbe-bb357af6f5b7 | -9.20908 | -59.76358 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 67a43ebb-ef7f-3104-9a4d-cc0b6f64c088 | -9.80232 | -46.649 | 2026-08-21 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 136e1013-0e93-3321-9e0f-4ab1525e9a22 | -7.45743 | -46.15672 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd6dfb1a-b56b-37b9-bb90-1f239e1d06fa | -6.11237 | -53.07287 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e5f63c35-5b14-3ff1-b237-e796310ee7fe | -9.21842 | -60.77517 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 302cdae0-f3cc-342a-a140-68a2536a01fe | -6.43063 | -52.72706 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a9ea1c7-3274-3ab9-9df9-5bf09bea5211 | -5.82109 | -55.71823 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e11bc93c-1f3b-3668-a670-21825e38b494 | -8.583 | -54.75093 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2456b8c3-7976-36ba-b225-61ff9e016a15 | -6.89842 | -59.43814 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f50796f2-47ff-3503-8872-4719d386362a | -6.87853 | -59.43471 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66dc2322-721b-341c-b14f-4d089f011c94 | -9.05424 | -50.8453 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83675605-0b96-3497-bc17-1a5ed770f106 | -6.65667 | -56.35237 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98a82307-8883-3cbc-a418-f9c369b56c9c | -9.46147 | -51.64143 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f5bb28b-f5fd-3f82-8a18-091d45decb1a | -6.1279 | -59.91588 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c622e936-20ec-306b-81f3-6f161ee80651 | -10.77646 | -50.3008 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fe2d0dc-83ef-3d83-8900-9ca84f9e20d4 | -10.63326 | -51.60513 | 2026-08-21 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f239336f-6d23-372a-bd6d-561efcbc8d0f | -10.80139 | -50.27406 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 318d9ea2-adf6-3169-926d-8584b424e8d5 | -9.20322 | -60.76835 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d63b1882-c7d9-3754-b1e4-6c939acd9993 | -6.88255 | -59.41204 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d85e4a1-2ed4-37c2-b7fb-49ea9b1e2ebb | -9.20422 | -49.92106 | 2026-08-21 04:46:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b18195c5-bf27-3dff-ba5d-7f55302aac7b | -11.32721 | -45.01983 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d6e7cc75-c1c8-3426-a964-eb2899af0ad7 | -8.58831 | -54.78611 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3f64bc8-ac17-3044-9936-88cbf9da85f4 | -7.02687 | -56.61561 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38bcc3b6-3e73-368a-9c5d-d2b29bd0482e | -7.03375 | -45.89532 | 2026-08-21 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26e9f952-da13-3759-886c-c37d9c2d0cdf | -8.61714 | -54.72263 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21636a52-8649-3471-bed4-f4bb77add56e | -10.76005 | -50.31733 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3c4ad2de-6b99-3f6e-8cef-493e27854bc5 | -7.0546 | -59.83942 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 43aad21c-740c-3112-a091-d839b4c5832b | -9.45707 | -51.64788 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb6a034e-ea49-34bd-bdaf-cfb68b9a5e09 | -4.17919 | -49.39825 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2406f24-8d72-3d00-9b8f-30eace9144e3 | -9.0655 | -50.88314 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 497be989-0bb1-3701-95b2-9c220a4b25fd | -7.60454 | -60.82995 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c78ccce-448a-3fe8-8c18-9b47c453ed54 | -9.05306 | -50.83077 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16674a97-d973-34bf-b5a7-7cf097d158ad | -5.9985 | -57.85902 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 541e467b-ab2a-3ef1-b854-af77e2eddade | -11.32378 | -45.00978 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc1139b2-1b17-32d9-aa20-04e0f555b895 | -2.70921 | -54.75981 | 2026-08-21 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bf178c2-d37c-3774-b71e-d3ccf5d51802 | -7.62835 | -45.76423 | 2026-08-21 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e68ba57-b887-3dde-8493-ca8cbda235f0 | -6.57985 | -58.98325 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4dcf01ec-ba98-38f5-98e6-63ef6da2b540 | -9.21613 | -49.9115 | 2026-08-21 04:46:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33ffa7a9-2124-359d-9596-edf59e4f5291 | -5.86977 | -57.66475 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c96925c-6a58-3065-ade2-c3a30a5a8aea | -9.22177 | -59.7771 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd738cfb-29d3-3b59-99ab-d4776494836a | -9.05598 | -60.44196 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f2eb1f7-cf94-3971-8540-72f7f183fbb1 | -6.555 | -56.26171 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 266d9f86-8125-3235-8570-6606fa7d8162 | -10.52967 | -50.81856 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README44.md)
