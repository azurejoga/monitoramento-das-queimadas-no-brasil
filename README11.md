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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55204abf-a371-3620-887e-6b97fd3cda63 | -13.53987 | -43.01041 | 2025-10-14 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 9e96cd45-35af-3535-9451-40865585ce12 | -15.97741 | -42.17645 | 2025-10-14 03:38:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9446657e-b828-3405-af7c-e98b78e77c8d | -11.56356 | -44.05199 | 2025-10-14 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78e268e3-f4fe-36ca-a22a-3811ed7ed196 | -13.0406 | -43.21982 | 2025-10-14 03:38:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bc3e0083-118f-3e17-adc5-dcfa119c63f3 | -13.53512 | -43.00943 | 2025-10-14 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bfe65892-d061-3e28-bab1-232e5427314d | -11.51932 | -43.50412 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee7004d6-7322-3259-883e-02c40feec5e8 | -12.65961 | -43.42815 | 2025-10-14 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfee0ef7-d7a5-335b-9d43-735a29aa1cc8 | -15.80383 | -41.45736 | 2025-10-14 03:38:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b583ace-5315-3acc-be59-3ac1b2544b0d | -10.49016 | -44.17362 | 2025-10-14 03:38:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 814a81f6-fb45-38f2-bd7e-73c3349ad517 | -10.8066 | -43.95359 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9eeab528-742e-3c03-9a23-ea3cbe874c76 | -11.29276 | -44.02467 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 379d25f9-c091-3988-8141-72621aaf41fc | -14.31104 | -44.5823 | 2025-10-14 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e22dc768-8811-354b-8e22-ac4f5dfa0249 | -13.33152 | -40.76542 | 2025-10-14 03:38:00 | NOAA-21 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4701b95d-a558-3b6d-b362-e017ce71eed4 | -11.88224 | -42.46199 | 2025-10-14 03:38:00 | NOAA-21 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 28d63e70-f57b-386e-b306-bd89c4eddeec | -11.74442 | -43.28996 | 2025-10-14 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| dd41a5ea-207a-387f-ba4f-f5ddaaccfa87 | -10.82123 | -43.99289 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b85e2efd-e497-3e3c-af56-73168c3cac70 | -11.74497 | -43.28699 | 2025-10-14 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 39.2 |
| d785da65-d866-3c18-9260-2cace3286aec | -12.40954 | -40.92066 | 2025-10-14 03:38:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f94497a5-58d4-3b95-895b-7984e9e40ac9 | -16.7243 | -43.46875 | 2025-10-14 03:38:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ad36852-8542-3c9c-bc45-22dd622e9f06 | -14.39327 | -40.76467 | 2025-10-14 03:38:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7c200043-b942-380d-8753-6778c01091bb | -16.23869 | -44.05584 | 2025-10-14 03:38:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 82a349cc-b0c1-3688-8e01-f8356b2cea3e | -5.8893 | -42.8813 | 2025-10-14 03:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 02cdad51-7162-3ef5-83ac-f9dc984a2877 | -7.9442 | -44.115 | 2025-10-14 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 172.3 |
| d00f6e1c-2834-311f-aa6d-082c2fb4becd | -4.6696 | -43.1326 | 2025-10-14 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a536a30d-3d5c-3afa-bb3f-bfc3f592a261 | -4.8408 | -42.77 | 2025-10-14 03:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 3ec79544-f6e4-3f7f-9b77-8069c3cd3a26 | -7.9439 | -44.1381 | 2025-10-14 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 8c5a0306-777e-3eaa-8a03-72a3b7e0aca0 | -7.9253 | -44.1169 | 2025-10-14 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 304e41b2-3b49-3275-9a7f-b635ef992dfc | -7.9631 | -44.113 | 2025-10-14 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f92324ab-ac11-3363-b5c2-7a476a52698f | -19.82836 | -42.43779 | 2025-10-14 03:40:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7b37ed05-b151-3610-94c3-24be779ae2c6 | -19.8242 | -42.43724 | 2025-10-14 03:40:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 372c6800-34c3-390a-b367-029cc3cfb9f2 | -25.85745 | -50.40498 | 2025-10-14 03:42:00 | NOAA-21 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 7fa57308-97a0-3295-9495-d09e76269484 | -27.07507 | -48.97194 | 2025-10-14 03:42:00 | NOAA-21 | GUABIRUBA | SANTA CATARINA | Brasil | 4206306 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8e6d7520-2954-3e40-880e-61882d5246b6 | -27.0698 | -48.97048 | 2025-10-14 03:42:00 | NOAA-21 | GUABIRUBA | SANTA CATARINA | Brasil | 4206306 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 88886e70-4dd3-3cf3-8b9d-abb3c13b5175 | -27.07146 | -48.97145 | 2025-10-14 03:42:00 | NOAA-21 | GUABIRUBA | SANTA CATARINA | Brasil | 4206306 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6ae72ee8-cdae-3a9a-9d49-6f65cb7c2447 | -25.85398 | -50.40413 | 2025-10-14 03:42:00 | NOAA-21 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 57edeeca-a613-3812-9a32-eb55838eefd6 | -7.9442 | -44.115 | 2025-10-14 03:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| bcccbfb2-3960-33e8-a1f6-3a9cc70e73fa | -7.3942 | -39.7845 | 2025-10-14 03:50:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 44.5 |
| 42648bed-4022-3787-98af-8edc3191afa8 | -11.7401 | -43.2928 | 2025-10-14 03:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 8785dead-8916-3aab-ba2f-035aa4d83443 | -7.9253 | -44.1169 | 2025-10-14 03:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d2e66b03-0326-3fc3-8fb5-f6043dc44292 | -4.6509 | -43.1337 | 2025-10-14 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 72e503d3-52bf-35cb-830b-54bfde1cab96 | -4.6696 | -43.1326 | 2025-10-14 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 2136b043-96d2-32fc-8fcd-c0ffe5c6ca00 | -4.6509 | -43.1337 | 2025-10-14 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 0aa897a6-6196-30d3-801b-9dbaa9d58eaf | -4.6696 | -43.1326 | 2025-10-14 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3783b8c9-c709-33b6-958a-27688daa3814 | -7.9442 | -44.115 | 2025-10-14 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 288dbe49-f3ee-367b-b1a3-2ea052439ceb | -7.9253 | -44.1169 | 2025-10-14 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| b01a69bd-64c4-37ba-8f9b-d6798ea9033c | -7.9439 | -44.1381 | 2025-10-14 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| e0528cdb-d97a-3b1d-acc4-d8b270bce9ca | -7.3942 | -39.7845 | 2025-10-14 04:00:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 46.3 |
| acec7407-f04d-3392-9999-db3ea02452a0 | 1.46163 | -50.88211 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4cee3659-7b5f-31c5-ad14-c1e2b4319e6e | 1.46858 | -50.86914 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44763b20-412b-36b5-88c6-55cdfd7bf916 | 1.11268 | -50.98979 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a60ccc25-f8fd-3460-8403-1a2bab438c98 | 1.10595 | -50.99091 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 46b5f0b7-dc6e-32c1-9532-42e0c4b8f7fe | 0.39184 | -51.05098 | 2025-10-14 04:02:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c820843-31f6-33f7-b1e5-effb6368236e | 1.10687 | -50.99677 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3710164b-d010-35a9-a101-7444daa97a30 | 0.39095 | -51.0452 | 2025-10-14 04:02:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cabd596-9e25-3c95-a1e8-bc5f06ad549b | 1.11369 | -50.98046 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3db87752-0644-329e-87df-2b06d59ddd3d | 1.13749 | -50.7323 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 620188b4-7575-3a29-bc70-e55de124918d | 1.1366 | -50.72659 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c83807f-40e2-3dd1-8782-6cb9abdbf78f | 1.12356 | -50.95452 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79787c21-9d03-3812-9e85-04d4d36e5557 | 1.12269 | -50.94873 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c15dde2-fee2-3b5f-90de-553e3fdb181a | 1.10784 | -50.98739 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ba5e4c34-7572-3a52-beac-da2e3a5fde63 | 1.11457 | -50.98629 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 68b117bb-e49d-32e5-9cf5-01e633cdc6c9 | 1.11177 | -50.98399 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 364a0751-a383-3986-9cd7-390842e6d30c | 0.38973 | -51.05193 | 2025-10-14 04:02:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87d3de6f-3471-3729-8ccf-3ab7846a0ba5 | 1.1096 | -50.99911 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9ef4e532-0c1d-3117-921f-ad1749b42500 | 1.12057 | -50.95234 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a644926-d639-3d3b-9ce3-62e46bd8bcd1 | 1.10872 | -50.99325 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ec86e2f8-fe22-3cb0-9cf7-ace0309f0dc5 | 1.12638 | -50.94552 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 170e65ff-3c8c-361b-8555-3e06f24e25d1 | 1.12941 | -50.94764 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c87232d6-ccd2-3a07-8fe2-9883068750fd | 0.38881 | -51.0462 | 2025-10-14 04:02:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee9c6bcb-93c1-308a-a038-577c825558f6 | 1.13311 | -50.94448 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a090134-7b9c-3640-930d-1621cb35d03c | 1.1273 | -50.95129 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77714f53-9866-3617-99d9-ae1f4b38effe | 1.46948 | -50.87505 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4240f870-3c1c-35df-9c45-5462c62f16f5 | 1.10503 | -50.98504 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0a49306f-093b-3cbf-8e5e-e191a45bfad5 | 1.46366 | -50.88205 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9264827f-70c2-3caf-a9bc-0506ea68dc6c | 1.12168 | -50.74432 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6e15af5-6777-3d51-a42d-d7a3eab852a4 | 1.61421 | -51.03815 | 2025-10-14 04:02:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9eda78a-e356-3f53-8be1-4a1c1ac9786f | -7.92597 | -44.1362 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 086b9358-6ce1-3c9d-a71e-c84592e32d29 | -7.75674 | -44.72672 | 2025-10-14 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1039b359-aa17-3a96-85c7-5ef995192526 | -6.44597 | -41.82983 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5fc1711d-11b8-37c2-8a83-0be6a0034bf8 | -7.49884 | -42.14539 | 2025-10-14 04:04:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 04c00dcb-639a-36b6-8987-2f9b9fc5235d | -7.5314 | -45.81645 | 2025-10-14 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0ea646d-267e-361b-ad4f-0ff4940ddd63 | -7.95459 | -44.12972 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0e1d7125-62b2-3440-acf4-5d33c862022b | -7.92819 | -44.12267 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d559b9b9-9ad8-346c-b47b-64e68c58a9d9 | -6.33634 | -41.59689 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1d6934e-8052-315b-a4ab-63f4c99d01a2 | -7.92671 | -44.13168 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8d1d783e-4714-3e27-827c-8a84da0c79f3 | -5.29308 | -43.53793 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6915438c-5202-327c-9688-57d6e1d50041 | -4.39268 | -43.46922 | 2025-10-14 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27d5ba7c-feec-3615-b0e3-595363e4155a | -7.92762 | -44.12972 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6c82b080-d855-31b7-a684-64825a536361 | -6.21604 | -42.49407 | 2025-10-14 04:04:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6b667f50-cbe0-3121-8343-6317af4bb907 | -6.44195 | -41.833 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6b887696-e69f-3d48-a6c6-412685ee22d5 | -3.51039 | -49.7192 | 2025-10-14 04:04:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dea70394-e359-3141-86ff-90986a1beb38 | -7.62858 | -47.83703 | 2025-10-14 04:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11a8379c-13d6-3239-98e2-8326f10f6f62 | -4.91749 | -41.53691 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e886d8ad-6f86-33ae-96e3-871fd3558bf0 | -5.87868 | -42.87514 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 84aa7721-87b1-3e70-b128-21c89caea059 | -6.48545 | -44.10878 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0410ff16-09b7-3cba-a8f2-60c861ee9b5f | -8.43595 | -46.18914 | 2025-10-14 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 810ea608-8dbb-3bb0-b280-6c1c49ff3254 | -4.84631 | -45.21138 | 2025-10-14 04:04:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fee81204-1b29-3c06-8d29-000459e08737 | -4.00739 | -43.2747 | 2025-10-14 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dc391af-9702-34ee-89e0-7e5d530cba63 | -4.05217 | -47.25247 | 2025-10-14 04:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e63782ab-9373-32b5-b35d-5d0f82646e48 | -5.79073 | -43.89611 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README12.md)
