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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 137be3f6-8807-3050-9544-7df5d2c6c0d2 | -12.99846 | -46.78185 | 2025-10-08 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e635157f-ce58-38a5-b4f6-dbfacacd63b4 | -7.47518 | -43.09898 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 017f0918-1d2c-3f81-8949-2f4d6585706c | -5.72981 | -43.61011 | 2025-10-08 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e15edc9f-794e-384e-ada1-176ff402ecbf | -11.99999 | -46.76862 | 2025-10-08 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 08c1644a-0a9a-3013-be21-f1bcf9bce3bb | -7.02561 | -42.87807 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f1dfaa7f-4353-3b02-918c-e5a8806984fd | -11.16741 | -54.90651 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81274b75-25a2-3c3b-a9e1-d783c46e81a8 | -11.70924 | -46.36042 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22f72ccd-9be2-3c6b-9326-8b2c8f5a1b1b | -13.34094 | -47.56099 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34dc897f-7a93-39c0-9dda-8811296ffbc5 | -10.94397 | -51.02856 | 2025-10-08 04:17:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a862a4ce-830f-3cc7-9120-b73e52c149e0 | -9.97561 | -48.78428 | 2025-10-08 04:17:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7aa65589-a4c6-3c19-bd8e-d39168b96a90 | -11.67072 | -46.40067 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 202e58d3-c4bb-381c-bb51-95c94ed55260 | -12.53005 | -42.34407 | 2025-10-08 04:17:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0690ed8c-caea-300a-b11b-a6749e33295d | -11.14768 | -54.8912 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f66e471e-fa23-3ae4-a48d-dccab3c46de8 | -4.42286 | -40.74883 | 2025-10-08 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6637f606-a646-3e2a-81e9-36da866347ec | -12.15644 | -51.44212 | 2025-10-08 04:17:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 898c6973-616e-34be-b8e1-1c50ad89f5cf | -11.17322 | -54.90765 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdab09e0-6488-3c13-ad76-74c5582140bc | -13.08348 | -47.93431 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd4e5e31-a847-3743-a36b-cb2f7c0dc2d3 | -11.18233 | -54.86784 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2865f96f-4117-350b-b8d8-ad12b31b0d9d | -13.02404 | -47.9105 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b57219e-d30a-30e5-a51d-b32c8281dd48 | -5.1406 | -44.96776 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5fe75b79-ade9-3eb9-8213-0cb599a95470 | -10.86897 | -53.74012 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d02a0174-2ee4-3910-9595-93d4c85e01d8 | -3.22158 | -47.12709 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f01c44a3-5e31-3898-9fed-fd283059d879 | -11.17583 | -54.86425 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a419fc5-75d2-3741-927c-164a2a7185d4 | -7.78948 | -42.40944 | 2025-10-08 04:17:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9c3f2043-d62a-3fd9-b453-f94c5b3a7908 | -11.44921 | -50.20577 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6e61faf-1e19-3a1f-830f-60fe26a30181 | -13.34159 | -47.55709 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d9ec45e-7dbf-3122-862a-cb320cdc2182 | -6.4213 | -47.24583 | 2025-10-08 04:17:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a455b8f-f9a6-3299-bb34-3f00a486230f | -7.44976 | -43.15209 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f05016ae-0cf8-3ee9-85e0-aac997fe7a70 | -11.17087 | -54.88915 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 93c8899e-bd88-3805-83f3-492e8efc7997 | -10.85611 | -47.11552 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fb352a6-a026-3d16-87cc-cd86c1265339 | -9.54599 | -47.76843 | 2025-10-08 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c22ea828-6c92-3e47-9583-c3575fa116d2 | -7.00508 | -42.8784 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| b246c81f-2fbf-3c05-9c36-575fc3c45347 | -9.68149 | -49.9313 | 2025-10-08 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b81f7b8e-ad73-39cd-9a77-ab94840f6cbd | -11.18342 | -49.77946 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5e5771f-6572-33f6-9275-aab91d20947b | -5.50223 | -39.70311 | 2025-10-08 04:17:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 34ad1541-c9d7-376b-8a91-944e93478759 | -11.18904 | -54.88883 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 76c51333-99da-3055-b538-fe9560749902 | -12.98875 | -46.77616 | 2025-10-08 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c21382eb-ff38-380e-b47f-f60358002ce6 | -11.38031 | -54.34908 | 2025-10-08 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db0629ab-eb87-3fd9-91b8-0c820f6e74ce | -10.42217 | -44.49881 | 2025-10-08 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87f70cf7-d362-3aa0-a960-68e96c05d70f | -11.78145 | -45.05788 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d97c8b37-0a41-3811-af21-3931874da500 | -10.41312 | -50.22519 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c43d9b7-e9c2-300f-a20f-6ff50c05066a | -10.22431 | -48.1727 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e5e53da-e1b5-358b-95c6-021bbc3f27cf | -3.14143 | -50.30302 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3b06981-c3d1-3c26-89bd-d074dada6a4f | -11.1593 | -54.89358 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df9c0160-6c39-3509-a59a-c4433c49e611 | -12.23329 | -43.78438 | 2025-10-08 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2708d6e1-9e7d-3bb8-b194-9ed24cfc137c | -5.35874 | -44.44409 | 2025-10-08 04:17:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1cf39577-549c-37e9-a7e3-20ebf1ef63dd | 0.93555 | -51.11962 | 2025-10-08 04:17:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99d2b031-c7f6-3b43-adcd-c1b0608b86da | -11.76159 | -45.13878 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b2bc5cd-8dd2-3037-ae17-e34da51d9e90 | -11.81716 | -49.51789 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a0056f7-269c-328d-8e48-0899e9ff3de0 | -11.13845 | -54.87658 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81107d92-6c1b-327e-9474-cfb0603ba803 | -11.73554 | -43.14978 | 2025-10-08 04:17:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65dde03a-d34e-3a9b-93f3-cfa8eceae5fa | -12.02483 | -45.21099 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8aaba970-03c6-3c16-ab95-90eeaac59a31 | -7.71776 | -42.38361 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 80be96c8-13b9-3c4e-a60c-41920395f46c | -2.88752 | -50.72979 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45b8a9e3-bd93-3231-956d-fcea41e59d6e | -5.13667 | -44.9603 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 28146dc4-b997-312a-834c-cd08b3b39317 | -12.92554 | -46.82479 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 396b0900-1692-3cb3-ba00-6adc8c4b0f11 | -11.68877 | -50.97057 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cf5bfa4-e4bc-309b-b34d-ee80dcfda53a | -6.6425 | -43.80185 | 2025-10-08 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 93e2fcbb-2d4a-3e54-bea1-ddf5f7449213 | -11.45678 | -43.48895 | 2025-10-08 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 690a31c2-e3c2-37db-9ded-d687b993c102 | -5.03527 | -43.61194 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 543e93f9-188c-34ad-b7b0-6f9d45d12f42 | -5.38996 | -45.20512 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d536081-e3de-3184-b4ae-0c69dd53e37c | -10.67862 | -47.55053 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4d93c8e-6cf6-3f8b-9775-efc463539862 | -7.78221 | -42.41195 | 2025-10-08 04:17:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fb9f9c3f-e7e3-37f0-8355-182285f1d445 | -5.71446 | -44.66456 | 2025-10-08 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4debcf23-1f67-3284-a379-d643693d24f5 | -11.15751 | -54.87156 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6325283f-3a9e-37f0-a11d-7b4a4cc993a6 | -11.69735 | -46.34659 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 627824eb-cdb9-3055-af36-8602089f8c9f | -12.94596 | -46.85228 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f963dd60-e4bb-3268-8b9a-89f64efa880c | -10.5009 | -49.1412 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 40b6f64e-3b88-339d-990d-67dfe0b58580 | -11.71466 | -50.98006 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ca9248a-962f-3fb5-8f44-e8b33117a3b5 | -11.15512 | -54.88393 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04245129-bcd0-34ca-b164-e029a6809946 | -11.69985 | -46.37451 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae6b5f50-5a59-3c4e-bfc6-55a007fe7ace | -14.07739 | -42.11868 | 2025-10-08 04:17:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ffe3b6a3-1cf0-3943-804e-8b4ebaacfc3a | -12.32135 | -50.269 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50a27b38-5e4a-3c4c-b5ed-cb3d7bf48c94 | -5.47115 | -42.20881 | 2025-10-08 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e658dafd-fd0a-3bfe-a743-087e69491e9b | -13.04999 | -47.88973 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f45d371-2da2-39ef-85a5-f0c2e1fd252b | -13.28556 | -47.15779 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b5aa1a3-1957-3f94-a529-ede0ad238d93 | -10.86452 | -53.73886 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8fe84e4-7fb1-3b52-b530-12965466b5ae | -11.3825 | -54.35014 | 2025-10-08 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a1d31ed-e579-3914-b1fd-fe8ed2a44b2c | -12.94441 | -46.84006 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 634dbe5b-05dc-380e-b007-8beae3fef624 | -5.50984 | -45.918 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd602238-68d5-3951-8f65-72bb025a96ab | -11.17989 | -54.90454 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3249981a-320b-3812-98a7-4f089b368c63 | -11.74059 | -50.93896 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 923a7529-c5a0-3128-b6c3-aa60ff5be1d2 | -5.1326 | -44.96355 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 866a4ae0-9932-3a3e-bc56-7258125b5303 | -7.01343 | -42.89044 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 368db8ac-ee38-3d26-8a23-4ee28d5b5abe | -11.73897 | -50.94783 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 4e70a06e-6933-3de2-a184-c5ff5313e309 | -12.24107 | -43.77836 | 2025-10-08 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12bdfddb-3c1b-3a2a-a680-5540e9c9e84c | -12.36476 | -46.49141 | 2025-10-08 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45f936ad-d70c-336c-9fec-b973891b0d5b | -13.26219 | -47.78628 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bacf2464-09bf-3ebf-a93c-640d2713635a | -5.1609 | -46.92584 | 2025-10-08 04:17:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00275637-7e0f-35d5-b235-bbd0b6c9f5f6 | -5.14299 | -44.96515 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cdbe86de-24d5-37e3-a00a-3749d7020ebd | -5.2568 | -45.27173 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b88db1b5-c978-3b3a-b9e1-a977049bbfb1 | -4.4032 | -49.7704 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02ec2101-3d94-3e90-9192-c80db9777368 | -11.7889 | -45.13967 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ba90bde5-157c-3f42-9594-a11dc4dca7f0 | -11.44705 | -50.21785 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d29c4e85-0ff3-33b4-b46c-39e531059184 | -5.85567 | -44.30758 | 2025-10-08 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4295003b-55fd-301a-9d30-6f85de6cdf3a | -11.85533 | -44.91712 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01ff2cd8-22a9-34cd-87cf-fa10971c568c | -10.83204 | -49.39027 | 2025-10-08 04:17:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 740a555e-de89-3457-8b46-75db527a31f4 | -12.94469 | -46.86 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2cd77ced-9252-3369-ad37-99457d514f52 | -4.94871 | -45.79148 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0f5a776-2bd6-31f8-bb72-aa630ca6187a | -13.49913 | -43.79001 | 2025-10-08 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README38.md)
