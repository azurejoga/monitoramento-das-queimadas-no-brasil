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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87671f39-b47e-3efd-b1e6-29ccc7d659be | -8.35 | -43.61 | 2024-11-03 14:04:37 | MSG-03 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e171ef22-19ff-3472-bfe4-05ac9c641cef | -3.55 | -39.28 | 2024-11-03 14:05:06 | MSG-03 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 31e32cf0-cfac-333a-a5d5-d718def5cb2f | -3.55 | -39.24 | 2024-11-03 14:05:06 | MSG-03 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 90fa36f7-965f-320d-83ec-12acb0c4668b | -3.23 | -43.35 | 2024-11-03 14:05:09 | MSG-03 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb022f0d-f683-31ff-93ce-5e1c0b53fed6 | -3.23 | -43.31 | 2024-11-03 14:05:09 | MSG-03 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b6452c7-4b11-3eac-ac15-40d794392fab | -3.42 | -41.33 | 2024-11-03 14:05:09 | MSG-03 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bb5f8dcf-df87-3988-838d-88cd9fc01a51 | -1.2756 | -53.3734 | 2024-11-03 14:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 9931838d-ecc3-3938-8766-3867e3835993 | -1.4029 | -54.1371 | 2024-11-03 14:05:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e6a8e1bd-92b5-37ee-b00c-26f708083f26 | -1.4029 | -54.117 | 2024-11-03 14:05:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 3fe2788e-1472-3e34-ab62-d432bb543b44 | -2.1695 | -48.7252 | 2024-11-03 14:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ba520581-36d6-3c93-894b-bf2b9d54ca5f | -2.6507 | -48.5629 | 2024-11-03 14:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3462c526-8586-378b-902e-2ec79f4f9a2a | -2.6322 | -48.5634 | 2024-11-03 14:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| bb533223-2dbe-307f-a55d-e0fcdbc5f3c0 | -2.6321 | -48.5849 | 2024-11-03 14:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| effe9522-bdaf-3798-a962-b73dc15dfac4 | -3.0202 | -44.4163 | 2024-11-03 14:05:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| e0b12dbb-5eda-3010-906d-7d97d439adfe | -3.0016 | -44.417 | 2024-11-03 14:05:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f8278c19-84d1-301c-b25c-b947fe62a3eb | -2.9647 | -44.3499 | 2024-11-03 14:05:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| d5bc40d0-65c2-31ae-800e-ac8b8c59e107 | -3.039 | -44.3699 | 2024-11-03 14:05:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 62244600-5f25-3ecf-80a0-a4e9ecd76068 | -3.2239 | -44.6361 | 2024-11-03 14:05:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 684e4eb9-e5c5-30e3-9aae-ee07b7786e4c | -3.2852 | -43.5549 | 2024-11-03 14:05:25 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| c7052e5e-01d6-3743-850e-dacd9cb42152 | -3.5397 | -44.759 | 2024-11-03 14:05:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 45a8e989-e2fe-3057-a3ca-477acdfbbdfc | -3.4792 | -42.2111 | 2024-11-03 14:05:26 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 6276ed00-54d2-3dc7-a94e-21063e11dcfd | -3.7246 | -44.9773 | 2024-11-03 14:05:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| deeb14b0-e4dd-3693-92f4-77250b92a409 | -3.6888 | -44.7295 | 2024-11-03 14:05:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| fcb6fc29-c844-3178-9302-049c74b45447 | -3.708 | -44.6148 | 2024-11-03 14:05:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 2fa725f2-805b-305a-9799-41b68b0ea1a4 | -3.614 | -44.7783 | 2024-11-03 14:05:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 9c6b0d28-ba89-372a-94d0-d9ddac3bd50a | -3.765 | -44.4297 | 2024-11-03 14:05:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| bc48aa3c-131b-379b-9999-3de8261eece7 | -3.8227 | -44.1293 | 2024-11-03 14:05:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 10744877-1177-3f67-86a6-8af063f3926a | -3.9308 | -44.7406 | 2024-11-03 14:05:28 | GOES-16 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 5585af85-488d-3a2e-a82b-1d55bf8edadd | -3.9111 | -44.9231 | 2024-11-03 14:05:28 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 4cffab35-d2a1-3a7c-9ae4-555bf77163b9 | -4.4241 | -43.4735 | 2024-11-03 14:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 883dec6c-54be-3d4a-a3fe-1909d958163c | -5.1579 | -42.9128 | 2024-11-03 14:05:35 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 019c8be5-44f8-3ef1-81aa-820306468d14 | -5.6003 | -41.6696 | 2024-11-03 14:05:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 07202299-c398-3d58-b81a-d2df67d74aea | -5.6517 | -46.4819 | 2024-11-03 14:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 78bdae6e-d842-3f8b-afcd-e1a594bc4d0c | -5.9927 | -41.9007 | 2024-11-03 14:05:40 | GOES-16 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 146.3 |
| 905a198e-e4d1-3675-8f47-450d454ef1df | -6.3348 | -41.5586 | 2024-11-03 14:05:42 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| bcb7c0db-2868-3c48-939c-326927600a57 | -6.5241 | -41.4688 | 2024-11-03 14:05:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| 292c5a65-9833-3ace-8800-a7fb8cb801cd | -7.3763 | -44.3787 | 2024-11-03 14:05:48 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 78a652f7-193e-3540-a0e0-c64c59464e17 | -7.6591 | -42.7646 | 2024-11-03 14:05:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 3c47031a-2f2e-387a-9292-555cf956ef37 | -8.3284 | -43.5857 | 2024-11-03 14:05:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6d04053c-e9c0-39aa-b021-e221eac7627f | -8.3281 | -43.6091 | 2024-11-03 14:05:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5480a552-7d9e-39b9-919a-529905bfa46f | -8.3473 | -43.5836 | 2024-11-03 14:05:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 50a8318d-d39c-30e5-a42c-d8db6f6a4790 | -8.347 | -43.607 | 2024-11-03 14:05:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 0fb769aa-77cd-3eec-bdac-b2e6f054a88e | -9.8018 | -43.8767 | 2024-11-03 14:06:01 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 034a9a07-1290-3b8a-b2c3-3e98910da0de | -10.012 | -43.8026 | 2024-11-03 14:06:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 5bda5ed0-a1b7-3e11-b789-3141a1a46475 | -10.0124 | -43.7791 | 2024-11-03 14:06:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 0a7367b1-831a-3184-94b7-b8182212690b | -10.2664 | -43.3689 | 2024-11-03 14:06:04 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 81.6 |
| b9cdbef9-89bc-3c34-b78b-0575a7eeffdd | -1.2756 | -53.3734 | 2024-11-03 14:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| c53f2704-56a5-31d4-b5e4-8aab3db5bd35 | -1.3846 | -54.1172 | 2024-11-03 14:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 53dc6196-4366-38e1-9c4b-7bfa9bf31f84 | -2.6326 | -48.4345 | 2024-11-03 14:15:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| c6e8a65c-2760-32c5-90f0-f3ebc40ccc16 | -2.6507 | -48.5629 | 2024-11-03 14:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 0f45d114-51d3-3eb7-98b2-4c8d1620d097 | -3.0017 | -44.3942 | 2024-11-03 14:15:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a7a7e2dd-e66a-3e6d-b4fc-e177af2041d6 | -3.0016 | -44.417 | 2024-11-03 14:15:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 7bdc27ff-0f3b-3d19-ab3a-1d1eb2aeee7c | -2.9647 | -44.3499 | 2024-11-03 14:15:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| c21ffe8d-3c1e-3e2c-8b86-76ba968e2d5a | -3.039 | -44.3699 | 2024-11-03 14:15:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a0ff105c-c3d6-309a-9bcf-f9abf918d479 | -3.225 | -44.4081 | 2024-11-03 14:15:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 17fbe034-4f8e-3bf4-90e5-621da74634fb | -3.2239 | -44.6361 | 2024-11-03 14:15:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6ce8ff06-ea02-3a69-a11e-d627eeecd5b3 | -3.1135 | -44.367 | 2024-11-03 14:15:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| fea83eed-238d-3317-9895-5e6dd90e94ba | -3.1316 | -44.4804 | 2024-11-03 14:15:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 654ba14d-e4a3-3db1-912d-ac4f12613a8c | -3.2251 | -44.3853 | 2024-11-03 14:15:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a7d73229-2629-3c54-bedb-dd9aff0a7f7e | -3.4335 | -40.4078 | 2024-11-03 14:15:25 | GOES-16 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 7fbd1847-3195-3752-b120-e4bd6b0ba517 | -3.4484 | -44.4214 | 2024-11-03 14:15:26 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 48ea3f4c-61a1-3357-89f8-cce9c9f8e30e | -3.765 | -44.4297 | 2024-11-03 14:15:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 60d45815-a33a-3d1c-ae67-86c9d0a48742 | -3.614 | -44.7783 | 2024-11-03 14:15:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| fafe397f-bcfa-35ad-90d3-e2fc1868f768 | -3.6676 | -45.1834 | 2024-11-03 14:15:27 | GOES-16 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 36e6889c-1420-35f0-820b-b0fc4139ff1d | -3.6888 | -44.7295 | 2024-11-03 14:15:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 110d3e3b-4ae3-3b79-aad6-6d7922d77098 | -3.7464 | -44.4306 | 2024-11-03 14:15:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 6f7e27b4-5897-398d-8a8d-8eb38482804c | -3.9308 | -44.7406 | 2024-11-03 14:15:28 | GOES-16 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 52507880-394d-39f8-ad5f-3118f781b425 | -3.9127 | -44.6505 | 2024-11-03 14:15:28 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1944849c-cd0e-3383-9e47-6b93748e592a | -4.4241 | -43.4735 | 2024-11-03 14:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 3c8d2f9d-76e7-30f2-9156-59c0682cdee8 | -4.4054 | -43.4746 | 2024-11-03 14:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 53fbb8f2-beb5-3f67-8d5b-7ffe5fcc49c2 | -5.1579 | -42.9128 | 2024-11-03 14:15:35 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 10d3284e-2a71-3cba-825c-df03269f5933 | -5.6003 | -41.6696 | 2024-11-03 14:15:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| e6eb9f44-9e25-3a41-9a7b-581ec7950c6b | -5.9927 | -41.9007 | 2024-11-03 14:15:40 | GOES-16 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 168.3 |
| dc456dcf-6536-3752-addd-68786a5d7b59 | -6.3348 | -41.5586 | 2024-11-03 14:15:42 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 7648ccaf-fd77-3c19-9a13-6ea3873af2bf | -6.5241 | -41.4688 | 2024-11-03 14:15:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 43dca579-b3ca-325b-a1b6-2684412c2281 | -6.5239 | -41.4929 | 2024-11-03 14:15:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 43f948bb-7a10-3663-9937-d0180ad5048a | -6.9971 | -41.3258 | 2024-11-03 14:15:46 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 9c9a207d-444c-3d6d-b095-e8b517ce05a6 | -7.6591 | -42.7646 | 2024-11-03 14:15:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 847ce94f-d546-3349-8d19-8400b926dfa9 | -8.036 | -45.8634 | 2024-11-03 14:15:52 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 84e65bf8-2c98-356b-a0e4-88c20ab9bdd3 | -8.347 | -43.607 | 2024-11-03 14:15:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| aac9679f-eba1-34d5-98e5-58e58e65b213 | -8.3467 | -43.6304 | 2024-11-03 14:15:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 135.4 |
| d63808c6-43d5-328f-8c89-5a43211ebcd7 | -8.3281 | -43.6091 | 2024-11-03 14:15:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| af466f1e-ffe1-38af-88a5-c5db5b8e983b | -8.3284 | -43.5857 | 2024-11-03 14:15:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e8985543-2916-3f29-bdc1-ebfc4b4465d1 | -8.3473 | -43.5836 | 2024-11-03 14:15:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| b5b54dcb-518a-3231-b4f5-b84ddb6c01c8 | -9.7827 | -43.8792 | 2024-11-03 14:16:01 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a49e21de-a19e-334e-a78d-e889260a8675 | -9.7099 | -46.2488 | 2024-11-03 14:16:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ecec2842-b2f3-36d0-92af-92ba80dad5df | -9.7096 | -46.2713 | 2024-11-03 14:16:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a5186528-41d5-3357-9886-c63c502f26f2 | -9.8018 | -43.8767 | 2024-11-03 14:16:01 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 972451b9-8ded-3d5b-84bb-4d6485f408a9 | -9.6912 | -46.2284 | 2024-11-03 14:16:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 01f65bfe-bcdc-36e8-913f-73643a2e158f | -9.7288 | -46.2466 | 2024-11-03 14:16:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ca661cf4-e7be-30f0-aada-fafe9edfcf3b | -9.8021 | -43.8533 | 2024-11-03 14:16:01 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| ccae17a0-3a83-3e5f-aa10-63152f5f6740 | -10.012 | -43.8026 | 2024-11-03 14:16:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 8a5ba083-1f8d-3959-bb85-3cb3ceddbeb7 | -10.2664 | -43.3689 | 2024-11-03 14:16:04 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 76312c14-fd4e-3e66-9afe-e47962183180 | -11.0176 | -42.9763 | 2024-11-03 14:16:08 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| adfaa56f-d744-32e1-b77b-5a87983725c0 | -2.1695 | -48.7252 | 2024-11-03 14:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a533268b-a6f6-3c60-a32b-022e42b24c05 | -2.4095 | -48.805 | 2024-11-03 14:25:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1f236346-58c5-3a30-8bcb-53b3162f1ef3 | -2.6321 | -48.5849 | 2024-11-03 14:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 56ceec6a-c2e2-32f1-a549-a8e951258526 | -2.6322 | -48.5634 | 2024-11-03 14:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| df289a36-8ada-3ce0-ba3a-df8376df0cf4 | -2.9552 | -56.7652 | 2024-11-03 14:25:23 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d1360e04-2233-3ddc-85e9-e5d174967f8e | -3.1135 | -44.367 | 2024-11-03 14:25:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 77.1 |


[Clique aqui para ver as próximas entradas](README94.md)
