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
| 4c9c1d97-0903-3795-b923-a6b089d4ff60 | -11.64449 | -44.86397 | 2025-08-26 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e531be30-7712-3d6a-b4a7-2425b37e4481 | -15.17789 | -48.18892 | 2025-08-26 00:28:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 894db50b-2054-3304-8e1d-49521437a7cb | -11.0863 | -50.00031 | 2025-08-26 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7b463d92-56fb-346a-b798-0e3739219fe5 | -9.17151 | -40.59805 | 2025-08-26 00:28:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 45.6 |
| 4446d333-bf1c-3e4e-9ab9-05f99bc858ec | -12.93808 | -46.30737 | 2025-08-26 00:28:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f07bbed4-5042-35b6-bb98-137deda3dcf2 | -14.24844 | -48.03765 | 2025-08-26 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a5b44f76-5a60-3a37-ad75-f22204b1c61a | -13.45596 | -47.00139 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8642e2b3-5be2-3d09-ae13-6d3387d4347f | -11.63447 | -46.20901 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ee3b08d2-04b8-3d8c-9c95-79945fe72d2c | -12.763 | -48.14248 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1718f7b3-5f4a-3f61-a9e2-ef6f309859ab | -12.93175 | -46.32667 | 2025-08-26 00:28:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0706828d-958c-362d-94c5-3e43c0885732 | -13.44454 | -51.16187 | 2025-08-26 00:28:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| e782697e-0cb1-322f-8ad4-2d477b252fa8 | -11.57233 | -52.10847 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 400f8b2f-7c14-3a8d-a006-c3876bf90f7f | -15.49683 | -47.8895 | 2025-08-26 00:28:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1b9f3b8c-7d12-3c5d-918b-c1a71720bd5c | -10.73895 | -47.05564 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e727467a-37a7-3916-bd36-6249c46bf5d1 | -14.42729 | -48.36359 | 2025-08-26 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c7a46799-7e0c-3be0-b22d-bc70ea616093 | -12.75778 | -48.10315 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a87acc23-1094-331a-95e4-b63bfacc4669 | -10.82801 | -48.32645 | 2025-08-26 00:28:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 3c289fa8-8ab8-383d-b7a6-3c9d696d9e3d | -11.30802 | -43.29328 | 2025-08-26 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fb04a2f7-ce4f-3b6c-ba46-0e3378b2e000 | -11.56744 | -52.10268 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 19b9f083-93d5-3422-9a76-a23dab9aaee4 | -10.74901 | -47.06332 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 728.1 |
| fd802b13-922a-3b02-a1df-42fc9b8772d2 | -14.36399 | -51.9208 | 2025-08-26 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 35f234f2-5e8a-336f-bea7-112732c6fdb1 | -14.32843 | -48.64642 | 2025-08-26 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ded3e9a1-bd71-36dd-b5e8-0fe37437a88a | -12.69996 | -47.87715 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5890357b-80e7-31f3-bef6-5012c282d4d9 | -13.05904 | -46.31998 | 2025-08-26 00:28:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 08b66f64-015a-334a-b9d9-dd187510a1a5 | -10.71745 | -47.11071 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5eb31828-48df-390a-a7e4-61b75506153d | -12.72755 | -48.15699 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4b565d14-c880-3213-b1b4-9a2f0e95dbdd | -13.59699 | -48.19212 | 2025-08-26 00:28:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 39be8235-102e-338e-b54a-bf41a2742bfc | -15.05981 | -48.69592 | 2025-08-26 00:28:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0cadc4a5-5a2f-337a-8136-d63f7c90312b | -11.6351 | -44.8561 | 2025-08-26 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 0ccfa2f3-78f6-36cd-aa5a-4191247b1cf9 | -11.5397 | -52.14 | 2025-08-26 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 313.5 |
| a5704186-1320-3ded-b69c-bbbddd3882bb | -11.1396 | -44.7654 | 2025-08-26 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| f4957d03-7dbd-392f-bb55-64a2e907babe | -6.7635 | -59.6718 | 2025-08-26 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| ea53d4ab-4d67-377a-9519-9d68c75faa34 | -11.14 | -44.7422 | 2025-08-26 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 23dd2720-3382-35a2-bf78-5fec6ea45d53 | -11.5587 | -52.138 | 2025-08-26 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 625.3 |
| 396fcce4-04f7-3861-bfde-80dcc12958e7 | -9.0415 | -65.7349 | 2025-08-26 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 7dc1340f-198c-3020-8e49-7363c6713fc2 | -9.1724 | -59.4436 | 2025-08-26 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 2aa21252-e7c2-3f25-b58f-43f2df897865 | -10.76 | -47.0424 | 2025-08-26 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 9c8470a7-08ec-301e-99e8-434fc63c42f0 | -11.54 | -52.119 | 2025-08-26 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 263.7 |
| f71aadea-19b3-31bb-a079-cd26f54a51e6 | -11.5584 | -52.159 | 2025-08-26 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 4c27483d-8538-3010-82fc-8e3f51c7691b | -6.7144 | -58.5732 | 2025-08-26 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| f83395b6-5fc1-329a-8b2c-139a9386cab4 | -11.6277 | -46.3899 | 2025-08-26 00:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| e60ee3c0-181d-3700-b1f4-a26ba7cdc8db | -11.559 | -52.117 | 2025-08-26 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 393.9 |
| d588bba9-ee87-3e63-96cb-b4f7c02ee120 | -10.7406 | -47.0671 | 2025-08-26 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 5325dbab-18c9-3406-a516-4d0eb4db4ca4 | -7.4039 | -64.3469 | 2025-08-26 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 30e57d3a-3809-390b-943c-25bf02872921 | -4.9606 | -55.8028 | 2025-08-26 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| aa81dc56-8c0d-329e-8a61-85c145f74145 | -7.8895 | -63.0171 | 2025-08-26 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| de430bd0-4f7c-36cc-be10-f4d51ab9ffbf | -4.9789 | -55.8219 | 2025-08-26 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 18ec78ce-5411-369f-9f71-b1f8769a8332 | -4.9605 | -55.8226 | 2025-08-26 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| c67bf6b4-18fe-34b4-9b65-edeb6699bc59 | -6.7819 | -59.6711 | 2025-08-26 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 7ec948b1-2469-33d8-a0cb-504bad9c7ef9 | -6.782 | -59.6519 | 2025-08-26 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| efe60c9b-8d07-392a-9315-7183f19756ed | -6.7145 | -58.5539 | 2025-08-26 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d4c93ef2-378b-335d-9487-2f0b856862d7 | -11.3126 | -55.1112 | 2025-08-26 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 20f6298e-9b17-3345-a3a1-859845e94c2a | -8.3396 | -50.5652 | 2025-08-26 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| ec369d49-bd27-3d8d-b2fc-45bf719919a7 | -9.1722 | -59.4629 | 2025-08-26 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 93999cec-8cc5-3be7-8182-6a6757fb70e6 | -6.9128 | -59.3578 | 2025-08-26 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 4d4de8df-efde-39ef-8be9-36b1c55e1254 | -8.3209 | -50.5667 | 2025-08-26 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 33fb80a6-fa1a-39a2-9f45-37a7953031fe | -7.3854 | -64.3475 | 2025-08-26 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 216.8 |
| c8a735ac-6ff2-3e53-ac33-b56660781097 | -10.4241 | -64.3903 | 2025-08-26 00:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 38.4 |
| c6648e55-f6bc-38ca-bd4f-11c0a3c3ba28 | -8.9874 | -65.4192 | 2025-08-26 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b9812a4b-e6f5-3f83-bd12-a7e8b5c9e1f2 | -10.741 | -47.0448 | 2025-08-26 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| c37f86f4-2321-3c93-80e4-489bc83a743b | -10.7597 | -47.0648 | 2025-08-26 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 262.5 |
| d1220fa9-1630-3986-9031-42016bff3ff4 | -6.9313 | -59.357 | 2025-08-26 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ebc07054-09c7-3252-b48f-ba8a117423af | -7.3541 | -59.6669 | 2025-08-26 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 23cdc65e-f2c3-39a6-b4d6-3eaa6f767cfb | -9.023 | -65.7355 | 2025-08-26 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 021bddd6-ad9c-3e41-b9b7-e780d242cdeb | -8.352 | -62.9436 | 2025-08-26 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a22c1631-4b48-3686-932b-da59751b099e | -7.4224 | -60.6236 | 2025-08-26 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 9b308892-835c-37f6-ac36-647ef1feed09 | -6.2459 | -60.0174 | 2025-08-26 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 283bc5c7-5dd8-35ed-b76c-e0d60506f54c | -10.7593 | -47.0871 | 2025-08-26 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 30bd14d7-231d-366d-8524-b2581716d910 | -8.9873 | -65.4379 | 2025-08-26 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1b7c3fb1-980c-3510-b53f-694ba88439ad | -11.6273 | -46.4126 | 2025-08-26 00:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b21f0cbf-4135-3438-8982-f959c3aa28aa | -11.1591 | -44.7395 | 2025-08-26 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 8270c665-2350-343b-83b8-f87ac9480e3a | -6.246 | -59.9982 | 2025-08-26 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 953cca10-2754-31ea-b460-97549f24982d | -9.236 | -60.9256 | 2025-08-26 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9cd2cc0e-6971-3f6c-b8fa-b2afc868372d | -9.2677 | -56.91 | 2025-08-26 00:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 75bb695c-fbc4-31ba-ba13-b510c4430411 | -7.3669 | -64.3667 | 2025-08-26 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 92a6fa69-b996-33e5-a188-161c0a18ff43 | -9.0231 | -65.7169 | 2025-08-26 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 49668480-2ab6-3c7a-8f7c-dc354d10952e | -8.9689 | -65.4198 | 2025-08-26 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| ab404d2c-5855-375b-8919-cd2884ac3b50 | -7.3854 | -64.3662 | 2025-08-26 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 05321202-ae40-302b-a52c-936925f22a56 | -9.191 | -59.4425 | 2025-08-26 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| b5445cd3-a29a-3dc4-8654-5f85d7dd51c9 | -6.6961 | -58.5546 | 2025-08-26 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 5bd94dbf-0814-3dcf-b84f-f84c37cee32b | -11.1587 | -44.7627 | 2025-08-26 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 7f6afc6a-50d1-3b16-9d93-b8d7d0dcfc02 | -9.1909 | -59.4619 | 2025-08-26 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 705587a7-bd07-3dd4-9a04-2dee2403db09 | -9.181 | -60.8131 | 2025-08-26 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ddc36f73-c51b-31ee-890c-b66cbf366597 | -9.1812 | -60.7939 | 2025-08-26 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| bb90ab4f-9b71-3280-b133-48c922eb35b7 | -8.9688 | -65.4385 | 2025-08-26 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e84dd44e-4754-3929-bfc1-a2c6b1d85ca0 | -13.1837 | -45.2865 | 2025-08-26 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| cbcc9332-8893-34f7-8d90-0cf2f102c210 | -7.8711 | -63.0177 | 2025-08-26 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f5697dd9-afdb-3584-ac2a-e356e818bed7 | -7.367 | -64.348 | 2025-08-26 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 6e8a82ab-93a7-3e20-83f1-e688d48a916b | -13.1644 | -45.2897 | 2025-08-26 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 5804449f-bb6e-350b-bb9a-c5de786200e9 | -6.9127 | -59.3771 | 2025-08-26 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| ced1739d-12f0-32ef-9612-41213f8d3a17 | -6.766 | -62.8659 | 2025-08-26 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 899e7325-8e5e-3c11-8b84-53e1d7cf90c7 | -7.21731 | -44.43322 | 2025-08-26 00:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1aeea3d6-d6a6-33f5-a84e-16fbc0668e05 | -6.14643 | -44.39426 | 2025-08-26 00:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 767f3837-15c7-34e4-9786-e7d60ed990c7 | -7.53397 | -50.53983 | 2025-08-26 00:30:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 096fa25f-1992-3226-a35b-84e9055e9368 | -7.66247 | -42.66726 | 2025-08-26 00:30:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| f548d5c7-cae2-3a7b-80ff-ddc7e07d3ef3 | -7.07852 | -46.06086 | 2025-08-26 00:30:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 067cee8b-8a8b-30e1-8097-269b5f3b035c | -8.07114 | -49.6593 | 2025-08-26 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 89f6a11c-096d-3537-afe2-7c0b891d4cb0 | -9.06004 | -49.56095 | 2025-08-26 00:30:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1b999a4a-cd6b-32bb-b76d-c2cd4ff43b50 | -8.11346 | -47.13036 | 2025-08-26 00:30:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 11007b38-e689-3e46-a65f-18f154b87a48 | -7.22051 | -45.31105 | 2025-08-26 00:30:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |


[Clique aqui para ver as próximas entradas](README6.md)
