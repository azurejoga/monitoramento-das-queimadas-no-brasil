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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbd1fafa-2ccc-3c27-9f1f-eb69faeb2c94 | -7.0166 | -44.6184 | 2026-09-15 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 98622a47-5f06-38be-9f80-6fbcb0b7e98f | -13.7722 | -48.8087 | 2026-09-15 14:20:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 68c142cb-9d01-3455-9078-21348f150805 | -10.6641 | -54.1491 | 2026-09-15 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9a0e81d4-7932-3546-b2c4-8659692f5a73 | -2.7768 | -49.4553 | 2026-09-15 14:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| fed872b0-8d2f-3e87-8ba5-4798c6260208 | -15.5397 | -53.8081 | 2026-09-15 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 1d739a3f-71b8-333b-8c88-2a098665e1b9 | -15.5199 | -53.8317 | 2026-09-15 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 27ca486c-7f18-315b-8c6c-1cbcdc506473 | -11.9033 | -43.8112 | 2026-09-15 14:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| ee18ce7d-e6ba-3499-9755-1a8365c35ab3 | -10.792 | -46.2071 | 2026-09-15 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 66ed7afb-d0e9-374b-9646-b6a9bebb3c47 | -10.7535 | -46.2347 | 2026-09-15 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 549d7777-1274-3536-88ee-be703a880039 | -11.3642 | -43.9407 | 2026-09-15 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| dfe18c8e-02a0-33b0-bb35-b00af2c30aca | -10.312 | -45.2907 | 2026-09-15 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 1015d17d-fa6b-313a-9b2a-9ee49b76f7c8 | -11.2113 | -54.1208 | 2026-09-15 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| f36a478f-c8e3-3555-9f31-7bb563daa262 | -10.8665 | -46.3105 | 2026-09-15 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 315.2 |
| c00a5856-9983-34a7-afd4-9a0417acbf07 | -5.144 | -55.9345 | 2026-09-15 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 2d7188af-ef32-338f-8756-7bf66f85c34b | -11.2302 | -54.119 | 2026-09-15 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 6c3842e3-3a60-34c2-94b4-9639747882d9 | -13.7006 | -51.8061 | 2026-09-15 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c31f696f-edad-3f81-bf76-8409b302d033 | -13.5719 | -51.4605 | 2026-09-15 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| af1d5ebf-adae-3ab5-b514-0b93f2e3e045 | -9.475 | -45.4612 | 2026-09-15 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 155ccc00-3a02-377a-852a-e38c9d6c4d7f | -12.6824 | -54.6968 | 2026-09-15 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| d4d610b4-8cde-3c8b-ab4a-da9be82c9ea8 | -13.287 | -51.2832 | 2026-09-15 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| c671fbc8-ceab-3014-9b0a-06599e976a33 | -11.9715 | -52.4715 | 2026-09-15 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| acf7891b-2e5f-3f71-b145-6825bf4e8eac | -10.7726 | -46.2322 | 2026-09-15 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| f94535cf-39ce-329c-8a0d-8422a63dfead | -7.082 | -42.1346 | 2026-09-15 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| 74d78e2b-2fe9-38fe-860a-1e5886c4e4a9 | -9.4139 | -50.1103 | 2026-09-15 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| fcca1ada-7d79-3282-84c8-bfd6eac9178a | -9.3758 | -50.1565 | 2026-09-15 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 11233650-c863-3e7c-9591-410820ee5e18 | -6.5837 | -58.8498 | 2026-09-15 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| eda66ce4-2b7a-3268-bd34-1ce1294ce6fe | -8.5468 | -50.4423 | 2026-09-15 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 980ad45e-3183-31c4-8340-d474e8adfab2 | -13.553 | -51.4416 | 2026-09-15 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 45.3 |
| f73db0fe-8497-3ffb-8148-b70e73cbc9ea | -9.3765 | -50.0925 | 2026-09-15 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 341f51d8-aa9d-38c7-bd83-c1a557e205af | -10.3116 | -45.3136 | 2026-09-15 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3052dd02-d1b3-35ee-b16c-ab613d772e9d | -6.0256 | -59.9293 | 2026-09-15 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 245f42fd-bf2e-3dfa-869e-18f9482f0915 | -8.4852 | -44.5885 | 2026-09-15 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 974254be-bb28-3f2d-b278-471fff1f673a | -15.5195 | -53.8527 | 2026-09-15 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e1068fdd-e8a2-3f9d-894b-a87bea410302 | -2.9025 | -50.4004 | 2026-09-15 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| cf8dbce6-5375-3eca-8038-a06f2b960123 | -9.3575 | -50.1156 | 2026-09-15 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ddbee5d8-28c7-3a58-873c-67b7d9914b2f | -7.1525 | -44.2154 | 2026-09-15 14:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 3e2f11a1-c7bd-38c8-8387-536cd96ae410 | -12.3277 | -47.9513 | 2026-09-15 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 211.0 |
| 5d9fe941-6524-39be-aada-8b64c01225e5 | -13.3059 | -51.3022 | 2026-09-15 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 03e757ab-fb00-3b94-8f59-6fa2f5e86afc | -6.6021 | -58.849 | 2026-09-15 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 67b3b3eb-f300-3d95-b083-db8437b76078 | -13.5722 | -51.4391 | 2026-09-15 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 1c9dfc70-a5b4-330a-b350-6ced8cf1634d | -13.2424 | -51.672 | 2026-09-15 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| b52f5c2d-4577-309a-a415-2d3594fefda9 | -14.013 | -53.8917 | 2026-09-15 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| cd6362a8-fdaa-39e6-896e-10881e447c1d | -10.0008 | -45.7851 | 2026-09-15 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 145.6 |
| e1820a03-afbc-3473-a9c4-d8b8df6f9ebb | -13.3199 | -51.62 | 2026-09-15 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 0b3a16a4-983e-3aba-844d-b2f04b996ac0 | -9.1337 | -65.8253 | 2026-09-15 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| bef459f7-42f3-3be8-98f7-d1043c22155f | -7.0823 | -42.1107 | 2026-09-15 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| 9e57d35f-f9d5-31c6-8630-0dd431fe049f | -14.6969 | -48.0209 | 2026-09-15 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 04221d38-d034-3aa2-9b10-7cd5c282f184 | -10.8855 | -46.3081 | 2026-09-15 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 780.1 |
| c98adc21-840c-3e93-aca1-2fb705784aff | -15.539 | -53.8502 | 2026-09-15 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 9cb52026-9c9f-311b-84ef-dd7546f40f9c | -15.3602 | -52.9678 | 2026-09-15 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ceb96a93-f1ef-3b38-a2c7-2a6e79ecfc4a | -14.6974 | -47.9985 | 2026-09-15 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b6fb5324-e98d-3864-84e3-7bb3168f17a8 | -5.5286 | -43.3771 | 2026-09-15 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| bd8833ec-07d3-3883-9878-463dddf67b18 | -9.494 | -45.459 | 2026-09-15 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 274cac61-8939-3742-b698-e506330ed0f0 | -5.1256 | -55.9352 | 2026-09-15 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 173.3 |
| 4b2be511-a245-3f0f-8849-489a7261e783 | -5.8321 | -52.0887 | 2026-09-15 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 38003d3f-ec19-3fd6-9b9f-ec37802ae391 | -10.6829 | -54.1475 | 2026-09-15 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e736b683-0e06-3eb3-97ce-3480786a4b7c | -10.0008 | -45.7851 | 2026-09-15 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 23ad7498-b329-352d-aecb-832034964f9c | -9.769 | -46.0841 | 2026-09-15 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 54546820-d7d2-302d-a126-9566bdcf36f8 | -2.7768 | -49.4553 | 2026-09-15 14:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 8c7ca556-4b04-3312-b4f2-2203bfff35ac | -7.1711 | -44.2367 | 2026-09-15 14:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 242.2 |
| d0d008ea-19ef-39b9-b4f9-9c6a594c5459 | -10.8855 | -46.3081 | 2026-09-15 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 526.9 |
| a1840e7b-f04d-3104-a4fe-3e830b22c12f | -13.2232 | -51.6744 | 2026-09-15 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 7834c064-e48a-378e-abd8-9521fed6902e | -10.6641 | -54.1491 | 2026-09-15 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 71291da3-deff-3e78-bed6-941099ca4211 | -14.013 | -53.8917 | 2026-09-15 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 0e853acf-d63d-3500-a1f4-9b527c63a2f1 | -13.3062 | -51.2808 | 2026-09-15 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| ad548cec-d6f0-3c1f-a413-ba86dd5f373e | -15.5397 | -53.8081 | 2026-09-15 14:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 836ff341-96f0-3cf4-b602-eb08ab2f202a | -9.3765 | -50.0925 | 2026-09-15 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 6e23fb19-45c2-3904-b96f-4669efbece66 | -10.312 | -45.2907 | 2026-09-15 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 927ca51d-7c9c-39bb-862e-520e2980b018 | -9.1337 | -65.8253 | 2026-09-15 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 5a384ac1-318a-3ee0-915a-7c66119613de | -13.7722 | -48.8087 | 2026-09-15 14:30:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 0a652316-2204-3ae7-a685-b01142514bd0 | -11.8365 | -50.0028 | 2026-09-15 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 910cc7f9-9c02-3e5f-bc83-ea0095679791 | -3.4943 | -54.6567 | 2026-09-15 14:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 069e16a3-6756-383b-a413-e120b3b97c77 | -9.3577 | -50.0943 | 2026-09-15 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 57f6797d-9ac6-3b65-92aa-98e42a5611ab | -6.0256 | -59.9293 | 2026-09-15 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b425b491-ec8e-31a0-9ca0-7fe32c3032c2 | -15.539 | -53.8502 | 2026-09-15 14:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| c7bb1fa5-a132-345f-9b24-4f5a264817d2 | -13.7006 | -51.8061 | 2026-09-15 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| bc242032-0bd5-332e-86e8-3d26750706cf | -10.6827 | -54.1679 | 2026-09-15 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| fb0bcc6e-72f0-35e9-8238-0e8c5a87841d | -13.553 | -51.4416 | 2026-09-15 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| c7810c03-3a71-3ec3-97bf-a99b9b8462eb | -13.7002 | -51.8274 | 2026-09-15 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f6ac7615-7414-3530-a8ac-35aa7730a908 | -6.6952 | -58.7097 | 2026-09-15 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 15af4ee6-6fb5-35bb-bad5-2b097541362c | -12.0471 | -49.9344 | 2026-09-15 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 0ac5398e-025b-377c-935a-ec7fa6d7f6bb | -11.4357 | -51.4351 | 2026-09-15 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ae417483-fae3-3e10-bc3d-0c575ce95b25 | -13.2424 | -51.672 | 2026-09-15 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 6cf791c5-43e0-3938-b761-cca465a62ee1 | -9.7358 | -47.0958 | 2026-09-15 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 59a72da6-bfd3-3d09-b103-c235f8f6e88d | -13.5722 | -51.4391 | 2026-09-15 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 19fc2537-f99a-34ed-bbf3-8257ea5521bf | -10.414 | -48.6495 | 2026-09-15 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 1004d512-56ca-3a92-a3a0-c3884dcc6e19 | -11.3638 | -43.9642 | 2026-09-15 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 5c268a90-e56e-3297-b2b4-fcc98eee76df | -10.2922 | -45.339 | 2026-09-15 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| b359d3fc-2fde-38f6-87ff-f4ef699a275f | -14.0133 | -53.8709 | 2026-09-15 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ba9e9ec6-c174-37dd-a861-b7deabaff3d8 | -2.7767 | -49.4765 | 2026-09-15 14:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 886318b5-a416-39ba-bf1e-760808cca3d8 | -8.638 | -44.4567 | 2026-09-15 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 443.4 |
| 487adf7a-6fed-34bd-8ca2-2399f2f4dffa | -6.0169 | -52.1614 | 2026-09-15 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 41cfe1c0-6045-3e23-9108-64204e3e2bb0 | -7.5608 | -62.33 | 2026-09-15 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a597e0d4-a5e3-3498-9a2b-5ab36fb0ae0d | -7.1525 | -44.2154 | 2026-09-15 14:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 82d81b43-8df5-3aea-8bf4-bf99f57f826a | -13.3059 | -51.3022 | 2026-09-15 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b516294f-126f-36c0-9e51-7ba70792ba83 | -13.3202 | -51.5986 | 2026-09-15 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 8b4bd6d0-3943-3d9a-83ea-e129ba57ff5a | -18.1709 | -51.7685 | 2026-09-15 14:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1eeee472-c035-3cfc-b34e-dec04dda2aef | -11.9033 | -43.8112 | 2026-09-15 14:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| c04ab8c0-eaa8-31e2-a5a0-6839dc88617f | -12.6826 | -54.6763 | 2026-09-15 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ce51dc4f-6cd1-3da6-891c-1938e89bde5c | -13.3199 | -51.62 | 2026-09-15 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |


[Clique aqui para ver as próximas entradas](README81.md)
