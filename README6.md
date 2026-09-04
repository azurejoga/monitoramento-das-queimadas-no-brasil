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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d32ba1c-600b-35ed-8f84-8aacba375e2f | -5.32376 | -60.13766 | 2026-09-04 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64a33d6b-e465-36d8-b647-8605e294abe1 | -3.54129 | -59.78713 | 2026-09-04 00:48:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d5985073-4e73-3ca8-a991-435b404ca4f4 | -3.62845 | -54.60897 | 2026-09-04 00:48:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 3343d0bd-cb9a-3ad9-80a0-90453a992d80 | -3.12339 | -61.22431 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9415bf80-6a64-33b0-bb5c-a5304835e156 | -3.07927 | -61.18282 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 842f6ab7-1c4d-31eb-9532-9cc93559ba2c | -3.0605 | -61.17652 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 607bd34e-a108-3086-abd9-45eada3d4d72 | -3.02055 | -61.4922 | 2026-09-04 00:48:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 60daea4a-22f3-37cf-ae94-030ba87e7bf3 | -4.47039 | -55.42851 | 2026-09-04 00:48:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| af762c65-4c38-30fb-bb01-c0e11b626d4c | -3.43334 | -60.4064 | 2026-09-04 00:48:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3bedc8e7-80b6-35ee-86ca-edb4275cc74d | -3.16769 | -61.15571 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| e2e01ada-bdcb-3c39-8ab6-977eb1a0182e | -3.20489 | -61.23079 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 85635304-20d7-3220-b777-d6ed2a5bd6ac | -2.95748 | -60.90325 | 2026-09-04 00:48:00 | TERRA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 77e7c958-b23c-3e1a-997c-d4b4945bef0f | -3.75812 | -61.75633 | 2026-09-04 00:48:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| c0a1c5a9-4145-3141-9411-08d0eb8cdb45 | -3.29761 | -57.88707 | 2026-09-04 00:48:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bcea5c93-e109-3a39-898d-00a731a4751b | -3.16649 | -61.14697 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d9e0f5c3-a35e-3e8f-b287-2537cfa0ba74 | -3.09805 | -61.18911 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f94b775e-e756-3e72-8348-50069b9d29da | -3.19128 | -61.19701 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 323b5d00-b1cb-324d-a74a-523b0e1c707b | -1.81803 | -53.98693 | 2026-09-04 00:48:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 2f066c38-0066-3a69-b717-bc72729a932b | -3.67383 | -53.75631 | 2026-09-04 00:48:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c315823f-8e5c-3461-b17f-de4eb0c61106 | -1.24207 | -54.52847 | 2026-09-04 00:48:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fc9d254a-7a2a-36bd-a367-d907e2494a2e | -3.33879 | -59.45616 | 2026-09-04 00:48:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 66854598-e479-3b50-a4a3-cd70b7f7a4e4 | -3.77709 | -61.76281 | 2026-09-04 00:48:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4799e429-605f-3595-b2e0-185fb2fed8c7 | -3.21586 | -61.16054 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 406a91c6-6c4c-3e91-9bcd-c01348a7dfa4 | -5.231 | -60.00404 | 2026-09-04 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7f2872f5-7b97-3535-bcb2-f73e482bece3 | -18.7363 | -48.908 | 2026-09-04 00:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 176.3 |
| f1c9e125-bd7d-3a13-8c37-4bc6fab09606 | -8.4668 | -54.7439 | 2026-09-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 96b9caeb-3690-36ee-8b17-5dd1b3eadabf | -8.1126 | -54.7871 | 2026-09-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 47d5400a-5fd8-3f90-b1e2-983eb4f77563 | -8.1128 | -54.767 | 2026-09-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b08adc2b-e3e0-32f9-b970-326c66af1749 | -8.4861 | -54.6619 | 2026-09-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 150.9 |
| b171f18c-2754-38dc-9a82-78f732152360 | -18.1505 | -51.7937 | 2026-09-04 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| a6e7aeab-902e-3d4f-949b-23b4ef18c268 | -8.4863 | -54.6417 | 2026-09-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| f6a2b5f5-6add-3d2f-8335-a6239b061bcb | -8.5048 | -54.6606 | 2026-09-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 466.4 |
| db6c7a94-8922-3690-bbf1-58e723070dd8 | -18.7358 | -48.9307 | 2026-09-04 00:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 383fe6f2-68f4-307d-8868-0dd342b2b33d | -8.505 | -54.6404 | 2026-09-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 235.3 |
| 3cf57125-472b-360f-b969-ac1abe2038ea | -18.7565 | -48.9039 | 2026-09-04 00:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 7f512db4-a9cc-3104-af86-13f7136f36a7 | -8.5046 | -54.6808 | 2026-09-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 72f7e1bb-d708-3d1d-8eb9-bff7385ed373 | -7.5476 | -61.3437 | 2026-09-04 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 9369f92f-3bf5-34d7-8c62-b2ff2982fd6e | -8.1312 | -54.786 | 2026-09-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 128e7063-78fd-3f4f-96b3-a357ad378040 | -8.5234 | -54.6594 | 2026-09-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 3669b988-baa4-323c-bd02-ddf4b1e83169 | -7.566 | -61.343 | 2026-09-04 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| f1e30607-6f76-34c0-89ea-a04c9ba73eb6 | 4.88538 | -60.09 | 2026-09-04 00:50:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3b8e2a22-f6c3-36e8-a8bc-c140342e81c3 | 4.88397 | -60.10073 | 2026-09-04 00:50:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| df1d8a98-1120-39d5-bf61-6a935179b0f9 | -18.7363 | -48.908 | 2026-09-04 01:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 6cbf0da7-01c1-35be-b9aa-53a2c539401d | -7.566 | -61.343 | 2026-09-04 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| fe35b80d-dd23-32ca-84c4-cbd096965d29 | -8.1126 | -54.7871 | 2026-09-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| a49d0375-cf58-3a58-84f7-3e292fb5bb38 | -7.5476 | -61.3437 | 2026-09-04 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 0070e098-cc7c-31a4-85d5-62051a31013e | -8.4481 | -54.7452 | 2026-09-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 601aa7ac-a7a0-344c-9554-03a1a7655957 | -8.4666 | -54.7641 | 2026-09-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 34419fc8-55d6-38d6-bd85-0be6ef3de90b | -8.4668 | -54.7439 | 2026-09-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 327.0 |
| 4c6d0c01-944b-3639-9f38-bb263f9244e5 | -18.1505 | -51.7937 | 2026-09-04 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f0074138-dd2a-3c3c-9cbb-0aabcf9bccdc | -8.1128 | -54.767 | 2026-09-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 39d1995e-2b6c-3b08-85fc-fc534d407b50 | -18.7565 | -48.9039 | 2026-09-04 01:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 9ac09d71-2bff-3926-990c-e6183206305b | -18.7358 | -48.9307 | 2026-09-04 01:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 0b537b1d-c689-3a62-ba51-49d6068a25fc | -8.4669 | -54.7237 | 2026-09-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 189.0 |
| 83c68781-c62a-3fc5-86f3-845dfab93330 | -8.4483 | -54.725 | 2026-09-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c1dc78de-da2d-34c3-abf3-e38016a9c5c8 | -7.566 | -61.343 | 2026-09-04 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| cbc39389-a113-332b-8950-d37b921eefe1 | -8.4668 | -54.7439 | 2026-09-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 8a5f1a27-8456-3525-ac4d-eeeda1fee374 | -18.7358 | -48.9307 | 2026-09-04 01:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 20eb2e94-ea35-3dca-a567-408209572fee | -18.1505 | -51.7937 | 2026-09-04 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 8b9b009b-ea4a-3383-a209-34253e3532e6 | -18.7369 | -48.8852 | 2026-09-04 01:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 50.9 |
| af1f6702-e386-31c2-b843-690a92d142e6 | -8.4669 | -54.7237 | 2026-09-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e2668d24-dc12-39d7-b2e1-0d7ef79a166a | -18.7565 | -48.9039 | 2026-09-04 01:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2f16f7fe-a6f7-3e1d-bc64-ee640c0e2e58 | -8.1126 | -54.7871 | 2026-09-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 6af4e31d-eb3e-3e7f-8bdf-817b68f3dd05 | -4.4655 | -55.4236 | 2026-09-04 01:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| ce50e34a-29ed-3240-b3ba-35e3e9fbedb3 | -7.5476 | -61.3437 | 2026-09-04 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| f0cddf95-50b8-3828-954b-230c0f952997 | -8.4481 | -54.7452 | 2026-09-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| f6f94eb8-59e2-3814-95b3-32cd82fce875 | -18.7363 | -48.908 | 2026-09-04 01:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 224.6 |
| bd580b08-b38d-3528-92c2-e7ee82f44b69 | -8.48 | -54.64 | 2026-09-04 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21ec4bfb-fd25-39e0-87a7-47092cbeba4e | -8.51 | -54.65 | 2026-09-04 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c97ebc66-2994-3151-962a-85710ee6bbac | -8.1126 | -54.7871 | 2026-09-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 0e890b3e-d879-3a0e-b4c2-f9e6eb3a8e90 | -8.4481 | -54.7452 | 2026-09-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 764efb45-795a-363d-b35f-fbfd107c5655 | -8.5046 | -54.6808 | 2026-09-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a52f9e79-e0fe-3b69-8ece-7ffece10fe01 | -18.7369 | -48.8852 | 2026-09-04 01:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 5769e7e8-ef91-341d-895d-c4f5726579b6 | -8.4863 | -54.6417 | 2026-09-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 5539d35b-cdba-3522-9c6a-2abd8a3af708 | -8.4669 | -54.7237 | 2026-09-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9b045555-cb03-34d8-8e57-961bda2ed04b | -8.4668 | -54.7439 | 2026-09-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 85345708-1e01-3776-8a2a-4509641b3d1f | -18.7363 | -48.908 | 2026-09-04 01:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 256.4 |
| 0c5cf5e7-c1b2-3f83-8cf3-fa4864f110d3 | -7.5476 | -61.3437 | 2026-09-04 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| b1d7a50f-33c1-3383-b4d6-7d667678d5a3 | -18.7565 | -48.9039 | 2026-09-04 01:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 262869ac-bc02-3a5e-a8b8-cc023c6ee99c | -7.566 | -61.343 | 2026-09-04 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 015a4cb0-08a2-3ff4-bae5-77d7d7227b0a | -18.1505 | -51.7937 | 2026-09-04 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.2 |
| d9d70e22-230f-39e5-8a30-9685cf5bd95c | -8.4861 | -54.6619 | 2026-09-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 180.2 |
| cb34c0b9-3595-36f3-85be-7e3c009b9434 | -18.7358 | -48.9307 | 2026-09-04 01:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 92.2 |
| bcb51b33-65ac-3834-be22-0007e4725967 | -8.505 | -54.6404 | 2026-09-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 408.2 |
| 79cd217f-5f91-36d8-8464-5a93266a9119 | -8.5234 | -54.6594 | 2026-09-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 26188ae4-6495-3db5-a217-a3f66a8333ca | -8.5048 | -54.6606 | 2026-09-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 587.0 |
| d2b878b2-2725-3642-b1ca-70c639d0b7ba | -8.4668 | -54.7439 | 2026-09-04 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 7b9129c2-f781-3986-b3d0-746410c2c904 | -7.566 | -61.343 | 2026-09-04 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 9f947eb1-530b-34cd-945d-0228e548865e | -18.7358 | -48.9307 | 2026-09-04 01:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 4d38ecf9-1d96-3622-8b4e-ffdaea877994 | -8.4669 | -54.7237 | 2026-09-04 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 657409bf-96ef-30ac-8fae-876380c813c2 | -8.4481 | -54.7452 | 2026-09-04 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 43a04d45-1d2e-3299-968b-1abdcd4a0a67 | -7.5476 | -61.3437 | 2026-09-04 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 2546e1d2-25f4-3ad4-b243-8477ffaa2415 | -8.1126 | -54.7871 | 2026-09-04 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 3ebd20b1-c678-380e-99ba-5e86b89a3e6a | -18.7565 | -48.9039 | 2026-09-04 01:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 8d663912-6155-3134-9b90-11152cc07857 | -18.7363 | -48.908 | 2026-09-04 01:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 130.2 |
| ab292589-a450-3abe-9261-aa4f5975f180 | -8.4669 | -54.7237 | 2026-09-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 6115fa8c-560b-3ed7-8d2d-bde8a326f544 | -8.5234 | -54.6594 | 2026-09-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| dee8aa23-6c22-3ef8-8248-1b6ff2c45950 | -18.1505 | -51.7937 | 2026-09-04 01:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e17e7b01-289c-307f-8717-74e982ed58b2 | -8.4863 | -54.6417 | 2026-09-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 6b0c6fb0-c629-3f33-a24a-c6dce06529a7 | -8.5048 | -54.6606 | 2026-09-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 434.7 |


[Clique aqui para ver as próximas entradas](README7.md)
