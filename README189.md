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

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 101771e7-1da8-351d-8bb8-fb0984c7f4b8 | -22.679 | -47.3927 | 2024-09-26 13:47:11 | GOES-16 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 321.2 |
| c99ed5d9-c8f6-37f1-9532-c3405d087f8f | -5.212 | -47.9577 | 2024-09-26 13:55:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 25eb95a6-5128-3bde-95fb-01a42f456aa9 | -6.3249 | -42.5145 | 2024-09-26 13:55:42 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| e40098f7-bdb2-339b-85a4-beb5cacc882d | -6.7908 | -41.2254 | 2024-09-26 13:55:45 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| aea76e96-e85f-3e7b-a335-a0489146760f | -6.8025 | -59.2851 | 2024-09-26 13:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| bed4d3aa-284c-3f0d-aed5-d1c433b610ce | -6.8024 | -59.3044 | 2024-09-26 13:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 9d28840d-16b1-3186-8f86-5477cc7c8485 | -6.8023 | -59.3237 | 2024-09-26 13:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4a8982be-b26b-3a5f-85c9-0e286cf29c0f | -6.784 | -59.3052 | 2024-09-26 13:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7420122d-b66e-359c-b6cb-9560daaf432a | -7.0595 | -44.1316 | 2024-09-26 13:55:46 | GOES-16 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 36aa64d1-f8f1-3684-9179-11e7665688a3 | -6.9306 | -63.1053 | 2024-09-26 13:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 97c00cc5-6208-3b76-9647-a5d78483c3d8 | -6.9305 | -63.1241 | 2024-09-26 13:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| c7a4e201-e819-3f93-9d43-f6af0d300c78 | -7.2944 | -43.3191 | 2024-09-26 13:55:47 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 57fe5c5b-d39c-339c-aa78-63963c581739 | -7.0981 | -59.2343 | 2024-09-26 13:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| ebe14a2e-0115-306d-865f-7d3644241199 | -6.9682 | -62.916 | 2024-09-26 13:55:47 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 2308547f-ac2f-3a18-b41e-1efb43a8c20e | -7.3695 | -43.3352 | 2024-09-26 13:55:48 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 18af981d-0846-3501-9382-64773f2e0721 | -7.3606 | -44.1035 | 2024-09-26 13:55:48 | GOES-16 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| a0e79046-9c4e-3719-8ef9-94da48b3051a | -7.2627 | -59.4974 | 2024-09-26 13:55:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 50c41583-3771-3841-9a7b-045adc660b36 | -7.2007 | -60.6515 | 2024-09-26 13:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6677e20b-b31d-32bc-9bf9-35792900f87a | -7.2006 | -60.6706 | 2024-09-26 13:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 6f8e260b-6d75-3728-be60-3f806e4d4715 | -7.4777 | -43.7444 | 2024-09-26 13:55:49 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| f18ec605-1345-3116-9c85-09685fbf58a9 | -7.4761 | -43.8839 | 2024-09-26 13:55:49 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c2d9ce79-6b36-345f-afbe-4bdf07cde27a | -7.4774 | -43.7677 | 2024-09-26 13:55:49 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 82810916-402d-3960-8b66-896796c82af1 | -7.3824 | -55.4924 | 2024-09-26 13:55:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 0c3f8330-8d69-34cd-a526-3d109459465c | -7.3639 | -55.4935 | 2024-09-26 13:55:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| eb27ce1c-5bc2-358b-847a-2e80a32eca00 | -7.3637 | -55.5134 | 2024-09-26 13:55:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| c9f11c75-e80f-3d03-9d30-c09555ff7d76 | -8.2736 | -44.9091 | 2024-09-26 13:55:53 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 28c042a3-73b3-394e-a70b-c84b49f146b1 | -8.2739 | -44.8862 | 2024-09-26 13:55:53 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 8d375e80-567c-3125-b8bf-60fce3a0db11 | -8.1075 | -55.39 | 2024-09-26 13:55:53 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 557ce9e9-728a-3038-8907-a3772a1b8915 | -8.3805 | -45.3994 | 2024-09-26 13:55:54 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 94be7d31-36c0-3ee5-b7d6-40b05abda8f4 | -8.3904 | -54.9505 | 2024-09-26 13:55:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 38e6ea74-3297-3f17-9db2-f336f29bc5a0 | -8.3155 | -54.9956 | 2024-09-26 13:55:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 85c9e197-fc88-3a27-9ee7-6b50f40342d9 | -8.2969 | -54.9968 | 2024-09-26 13:55:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 830f84ba-2e99-3b5c-9b21-0fe2b3dafb4f | -8.5187 | -55.1834 | 2024-09-26 13:55:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 82339487-bc30-35af-a6c0-381329d41b43 | -8.5185 | -55.2035 | 2024-09-26 13:55:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 0121f88e-fe60-3e69-a37c-d770a2acbabb | -8.4646 | -62.6556 | 2024-09-26 13:55:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 79ba63f4-b87c-3fde-b0ec-9cb5b75c4a22 | -8.8387 | -44.9858 | 2024-09-26 13:55:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 160.2 |
| b0f8ffca-21eb-3ec6-97f6-fa4d3973972b | -8.839 | -44.9628 | 2024-09-26 13:55:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 631bcdd7-770c-39c6-a2c9-70cc0939dc96 | -10.3589 | -49.9098 | 2024-09-26 13:56:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 69188f2e-76bb-3c20-a90a-f14ff6bca4d3 | -10.2754 | -50.5166 | 2024-09-26 13:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 5e0e3f96-cc5f-36be-9cd8-edb9f0c2056d | -10.2751 | -50.5379 | 2024-09-26 13:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2044621c-a546-3b61-8215-ef48ec087c80 | -10.2565 | -50.5185 | 2024-09-26 13:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| ee93dde4-50ea-3ea1-955e-66e0d5b4029e | -10.6456 | -45.8407 | 2024-09-26 13:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| d159aaa0-4b6d-34c7-92e7-3ccf27252481 | -10.6265 | -45.8432 | 2024-09-26 13:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 488c5794-a401-3e23-a5e9-734859e338ca | -10.8348 | -45.907 | 2024-09-26 13:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 6b4148ad-b196-3efc-bf79-2d4baf4b24af | -10.8352 | -45.8843 | 2024-09-26 13:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 5897922a-1e6c-3330-93fe-759fbcecaf8a | -10.6846 | -50.9847 | 2024-09-26 13:56:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1af03cbd-d62c-312d-945a-5cd6d07ecb58 | -10.6657 | -50.9866 | 2024-09-26 13:56:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 42e1f582-0239-3a5e-9794-43f7a2af74df | -10.5878 | -54.2375 | 2024-09-26 13:56:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 26b2c1ec-6adb-36ca-990d-b405578c89a6 | -10.8525 | -51.1581 | 2024-09-26 13:56:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 66530512-806a-3ca6-8598-6be47579ee63 | -11.0991 | -51.1111 | 2024-09-26 13:56:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| abfb9066-378d-35de-86de-06ae68198644 | -11.0569 | -51.4328 | 2024-09-26 13:56:09 | GOES-16 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 28aa9991-c4aa-3f5b-9ab8-ea6d2b61ab67 | -11.2317 | -46.1041 | 2024-09-26 13:56:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 9d6792f5-7477-3b8f-b1ea-c00958fbbe5f | -11.1847 | -54.7565 | 2024-09-26 13:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 199.9 |
| 5c3a53c5-1b1f-3407-a016-dcd1cce4b5e8 | -11.1845 | -54.7769 | 2024-09-26 13:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 215.3 |
| 0a752acb-7ca0-37f1-80e7-b1bcddefffc6 | -11.2123 | -51.1415 | 2024-09-26 13:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| e0615f05-83dc-3e6c-b41a-1e0bddf72bbf | -11.212 | -51.1627 | 2024-09-26 13:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 75913f61-206c-35b5-936c-f753c2ff89e7 | -11.2117 | -51.1839 | 2024-09-26 13:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a9473c1d-5644-3c43-afe5-b8336e88cb50 | -11.1931 | -51.1648 | 2024-09-26 13:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 9f07e794-74bf-3dfb-a32d-7ea4b36123a9 | -11.133 | -51.4038 | 2024-09-26 13:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| e6897c39-789d-3cce-b83c-b62cfcbb8c82 | -11.6988 | -47.8576 | 2024-09-26 13:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b19fccf7-a8f3-3e29-ace7-3c8190d11e38 | -11.8613 | -49.6327 | 2024-09-26 13:56:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 45f8e7af-907e-3c22-b8ca-42372b21807f | -11.8609 | -49.6544 | 2024-09-26 13:56:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 6eb83355-e1ca-3167-86c7-98ae3dff94c1 | -11.8425 | -49.6133 | 2024-09-26 13:56:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 06b9de8e-fb77-3b7a-9391-e4975639dabe | -11.8422 | -49.635 | 2024-09-26 13:56:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 5c4f3a60-56e3-3a25-a2f4-8b2c55c4b981 | -11.8536 | -47.7264 | 2024-09-26 13:56:13 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| caf1ff35-3b1d-36f5-bfbc-718979081188 | -11.7849 | -50.9086 | 2024-09-26 13:56:13 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| ab6bb311-f7b1-3720-a14d-134b389c5a58 | -11.9564 | -47.2893 | 2024-09-26 13:56:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| efa4fc02-9d31-3f7a-b1de-944207ecdd09 | -11.9369 | -47.3143 | 2024-09-26 13:56:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e1b1c3d4-58f8-3137-8b8d-17158d60e2d2 | -11.9365 | -47.3367 | 2024-09-26 13:56:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| cdfd4ce3-c66c-31cb-859f-1fe452e5cadf | -12.2053 | -50.7959 | 2024-09-26 13:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a1e6e0df-6494-3b2a-8fd4-85787c2075c0 | -12.205 | -50.8173 | 2024-09-26 13:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2a321760-eb18-3e5f-8dc9-86c4a472096e | -12.3051 | -50.5056 | 2024-09-26 13:56:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 751616dd-8995-3987-9f2a-cd6475fd75ab | -12.3048 | -50.5271 | 2024-09-26 13:56:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| dec568a2-4dd0-32a4-8dd4-d94a74707c0d | -12.286 | -50.5079 | 2024-09-26 13:56:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5eacda89-74b7-3612-b09d-ac70c52b3e91 | -12.2857 | -50.5294 | 2024-09-26 13:56:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| db923d2e-7e15-35eb-8bff-704b2a6be6fa | -12.2261 | -50.6865 | 2024-09-26 13:56:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 9d612594-da1f-32c5-a8d9-7f7befd39fa0 | -12.4974 | -50.4177 | 2024-09-26 13:56:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c3166ca6-7c2e-3dbc-bead-85dd55237aac | -12.7158 | -45.569 | 2024-09-26 13:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 4045515b-09e8-36e2-9a1c-ecf935829330 | -12.7511 | -51.2853 | 2024-09-26 13:56:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 01a65a3f-24d5-3b37-a11e-56a969484a56 | -12.732 | -51.2876 | 2024-09-26 13:56:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 12903a3b-6480-395f-8352-8551f02cd473 | -12.6083 | -53.1755 | 2024-09-26 13:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c3cd1c8a-ae66-33d4-8a46-f635d3a63c0c | -12.5892 | -53.1776 | 2024-09-26 13:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0be44cc5-ad85-3be7-b4ad-dd5350ed6379 | -12.5464 | -53.5147 | 2024-09-26 13:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| eebcd23e-da2f-3d2f-81eb-c6adae48d276 | -12.9516 | -45.3242 | 2024-09-26 13:56:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 6d26f4e7-2cb2-3a93-b706-d7911d66ce67 | -12.8674 | -51.1859 | 2024-09-26 13:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 7f30d0a4-20a3-35ed-92d9-90c60c4d7d27 | -12.8657 | -51.2927 | 2024-09-26 13:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 28106d1e-d6ac-3e9f-81b7-f2bd29a0ddeb | -12.8486 | -51.1669 | 2024-09-26 13:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 494d1695-6b24-38f1-8092-c4bd79fca100 | -12.8465 | -51.295 | 2024-09-26 13:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 03dda083-2b27-35b4-aa9f-60f311682c26 | -12.8462 | -51.3164 | 2024-09-26 13:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 02a8306f-5cf2-3913-b882-b3ea2677741e | -12.8297 | -51.1479 | 2024-09-26 13:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8812e541-b0bd-3c6b-9028-73eafe81a012 | -12.8106 | -51.1502 | 2024-09-26 13:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 3be5fb2b-64a7-347b-a51b-3eb0527e969e | -13.1418 | -48.5464 | 2024-09-26 13:56:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 427d231b-c7fe-30b0-97a9-557e5d226451 | -13.7335 | -50.9902 | 2024-09-26 13:56:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 72d5c280-8e28-3f0d-9286-2dfb98720d7d | -14.57 | -45.7205 | 2024-09-26 13:56:28 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| ea4d4d78-9b64-3c86-abe5-c35a9c556de7 | -14.5705 | -45.6973 | 2024-09-26 13:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| db5066e6-9432-3ab4-a864-ae424c7100ce | -14.5515 | -45.6775 | 2024-09-26 13:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| b3da06ae-d26a-3067-8fb1-c5ef618de621 | -14.6924 | -45.4665 | 2024-09-26 13:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 9ac306cc-45ff-3241-a33c-0407ffa749b2 | -17.8068 | -43.2338 | 2024-09-26 13:56:45 | GOES-16 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 5621c3ed-dd16-3ceb-9598-712611280f07 | -17.9929 | -44.4514 | 2024-09-26 13:56:46 | GOES-16 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 135.6 |
| b0d8c2c4-6920-3c07-b317-17a4ad0a9f47 | -18.9102 | -49.1674 | 2024-09-26 13:56:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.1 |


[Clique aqui para ver as próximas entradas](README190.md)
