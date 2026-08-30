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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8da11002-8d18-352b-8d9d-9cd077b15cbd | -8.631 | -66.5473 | 2026-08-30 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 48c7ef70-d10c-394e-b53f-a56dc375c8c0 | -9.1525 | -59.619 | 2026-08-30 16:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| cd7ae255-e636-393f-9a4c-318b00862f33 | -6.0 | -45.0889 | 2026-08-30 16:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 7cffa7a7-92b0-30af-95c6-b02a3883f1bd | -9.8992 | -64.9757 | 2026-08-30 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 74226be9-fac7-3922-8eba-5225e7b1d09f | -12.209 | -50.5601 | 2026-08-30 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 6d6a2d88-65a4-30dd-b620-8591834e7120 | -6.6226 | -58.4995 | 2026-08-30 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 3933c8d3-801c-3084-b7d6-fb4aba829d38 | -10.7641 | -50.7005 | 2026-08-30 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 4c733d11-4362-3b4d-ba2f-51b6e79ae99a | -8.3679 | -57.6737 | 2026-08-30 16:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 237a047c-94f2-3f40-9584-329720e8aabb | -10.937 | -50.5118 | 2026-08-30 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| c8594333-9f4e-3d77-b7f8-2d426b41debe | -7.9611 | -44.275 | 2026-08-30 16:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 765c4118-b073-3342-9cf2-2af82494337e | -8.9253 | -66.9477 | 2026-08-30 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| bb91d296-18a8-3c72-9147-e9435c1f2769 | -5.9636 | -57.6704 | 2026-08-30 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f3ae0cd6-b563-360a-a702-d7af4fadff01 | -11.2446 | -45.3267 | 2026-08-30 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 89f7cca5-fad1-306b-b41c-4d9b8d7764b5 | -9.7873 | -59.4479 | 2026-08-30 16:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 79ee8958-074c-36bb-b901-5d1d055f4896 | -12.1892 | -50.6053 | 2026-08-30 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 59daec6a-b334-302b-a2ff-ebe1e922e0f6 | -11.1634 | -50.5727 | 2026-08-30 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 93d4c1c4-14dc-3f28-b710-ab39a4051cfd | -7.5644 | -49.5857 | 2026-08-30 16:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| aaf443c6-c9f1-36e0-b063-e85262227dc6 | -7.9907 | -46.5177 | 2026-08-30 16:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 45e1dfd7-88cb-3312-ab01-93a4f3bf7bcc | -10.7839 | -50.6346 | 2026-08-30 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 206dbd16-5e34-3b7b-b7fa-b2150c4bb44b | -10.9405 | -50.255 | 2026-08-30 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 26d40860-2572-3f87-b471-de51d95e155f | -8.1432 | -64.0053 | 2026-08-30 16:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 14ea1952-f709-3aaf-9ef9-3c10d6be91b9 | -8.5925 | -66.9564 | 2026-08-30 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 213.0 |
| 860bbb20-c840-3823-b68b-3ebba5635af9 | -13.4191 | -51.4159 | 2026-08-30 16:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e77e4cad-8ef9-3936-9d1e-f733d85868f0 | -8.5739 | -66.9754 | 2026-08-30 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8240f892-2bad-3bc2-a5e2-a798062ee979 | -8.574 | -66.9569 | 2026-08-30 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 746571e6-af61-37a8-9947-34f59fe34fe2 | -7.5272 | -44.3413 | 2026-08-30 16:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| ccb19308-f0c7-3a71-b0c1-696ace53a625 | -12.3232 | -50.5678 | 2026-08-30 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| fe46adb4-9345-358a-8b99-3610624d3182 | -6.8019 | -59.4008 | 2026-08-30 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 971d7f47-6a90-3cb3-92dc-c917519643b9 | -10.9402 | -50.2764 | 2026-08-30 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 3059af97-01be-3adc-a4eb-c7339711e8aa | -3.9707 | -60.0258 | 2026-08-30 16:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 51814feb-6b36-3cf0-a82e-12af0bf8be68 | -10.7644 | -50.6792 | 2026-08-30 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c3cf4c93-4560-35f5-83e8-4b157e370848 | -8.3902 | -62.7152 | 2026-08-30 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| b6b25e4e-58dd-3b6a-adfc-1467df50c455 | -12.1902 | -50.5409 | 2026-08-30 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d57a74ff-03f2-3d98-8f50-bc3e99b24bc1 | -14.2989 | -51.7072 | 2026-08-30 16:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 71710898-7915-31ab-9ab4-2e84136688a9 | -7.9422 | -44.277 | 2026-08-30 16:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 6c46e546-41d3-3815-8a35-ce1b0b4af7ef | -10.9592 | -50.2744 | 2026-08-30 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| ab4f4ded-fc5c-3628-8583-e512a5da5d1b | -8.4904 | -70.2392 | 2026-08-30 16:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c7396341-db30-33e5-9c86-4c7fe2c7585b | -12.3229 | -50.5892 | 2026-08-30 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 260cf1f4-d93e-35f0-975a-5d91a499082a | -7.2562 | -60.6302 | 2026-08-30 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| d465fd0d-3c5a-3ccc-aa7a-768c2d565c9e | -10.8249 | -45.3382 | 2026-08-30 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| ee8b1400-86d7-3aea-b858-6c4ba13b00b1 | -9.1523 | -59.6384 | 2026-08-30 16:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 72e28224-e81c-354f-9a64-17c6f6ee23b3 | -9.908 | -67.0131 | 2026-08-30 16:40:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 1fc5a018-68c2-314a-899e-c1dcb4cd2468 | -3.6399 | -60.5466 | 2026-08-30 16:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c53021e4-bd3b-373e-9b7b-a0f9b78c04ca | -10.8249 | -45.3382 | 2026-08-30 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 269.3 |
| de3e9195-2fc7-3dce-b038-2c2b7789c67f | -12.285 | -50.5724 | 2026-08-30 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 0f7b5b08-b390-3bd9-9295-d134dc9637a9 | -12.9216 | -45.8812 | 2026-08-30 16:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 203.8 |
| cdacdf25-72f5-38e4-853f-7a4ed71f001c | -10.8463 | -50.2224 | 2026-08-30 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| d232ddb8-7651-31ac-9b7b-3c0416fc852d | -6.8019 | -59.4008 | 2026-08-30 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 991c92c9-582c-3f70-b6e0-5dc647091851 | -12.3041 | -50.5701 | 2026-08-30 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e9c21194-3354-39c1-83f5-9c8074d776be | -12.2086 | -50.5815 | 2026-08-30 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 3227f5c0-4362-3260-a81c-99ca798d0143 | -11.1919 | -51.2496 | 2026-08-30 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| e0708522-9628-3e3e-bb1e-ed7eb2345ef8 | -8.5925 | -66.9564 | 2026-08-30 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 285.3 |
| 0d662d12-9f06-34f7-bed7-1c9228a04478 | -8.5739 | -66.9754 | 2026-08-30 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2bb05c89-b716-33f4-b772-29a1d8be1fff | -10.7434 | -50.8302 | 2026-08-30 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| f7de1be2-016f-3942-9518-346f8d84cff1 | -7.9422 | -44.277 | 2026-08-30 16:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 372.2 |
| 53533014-eb44-3ae8-b569-ba8f0e07f7ed | -8.574 | -66.9569 | 2026-08-30 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 9fd17792-8490-38e0-834e-7fbebaed0bdc | -5.9636 | -57.6704 | 2026-08-30 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| fe9fd5a6-3b23-3dae-a899-cdfd4c3d5bbd | -7.9907 | -46.5177 | 2026-08-30 16:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| ab5138af-74bf-35d8-86ed-2b3f296502aa | -15.3651 | -53.8097 | 2026-08-30 16:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 891cae72-1e9d-3e8c-949c-25d5352aaa91 | -12.209 | -50.5601 | 2026-08-30 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| b0acabb6-a728-3645-a1d4-262a3716e34c | -7.546 | -44.3395 | 2026-08-30 16:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| e863cc7f-551a-3198-9c45-eeaa9407cfd6 | -8.1534 | -45.4904 | 2026-08-30 16:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 46c606cd-3fb5-379c-a6b3-6659de6aa28b | -7.3479 | -55.1544 | 2026-08-30 16:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 9ec78d13-99a8-35a8-8e95-a36da900217b | -9.1711 | -49.9835 | 2026-08-30 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| feac70a7-ab6a-3813-9e2e-27f412587453 | -7.9611 | -44.275 | 2026-08-30 16:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 177.4 |
| accdeaf1-6ba3-3c30-9db6-fc52c8ac78a1 | -5.982 | -57.6697 | 2026-08-30 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 77d9d600-19c1-3b89-ac72-9273378ad7f7 | -10.7431 | -50.8514 | 2026-08-30 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3e2c59f6-987d-33de-90b0-78589c129a34 | -6.6541 | -59.4452 | 2026-08-30 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 9f499a47-f35b-3ed1-9e02-a1990e674b7d | -7.9419 | -44.3001 | 2026-08-30 16:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 905.3 |
| f4b298a1-dc13-3371-a718-0976fca4e070 | -11.172 | -51.3151 | 2026-08-30 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| b259ea62-871a-329e-8061-b9d877fcd62e | -9.1525 | -59.619 | 2026-08-30 16:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a63f73d3-0236-35a1-a097-101cdf23901c | -14.2989 | -51.7072 | 2026-08-30 16:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 989caabf-d318-35ff-abaf-476b48813b18 | -7.8228 | -73.4067 | 2026-08-30 16:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 56.4 |
| f4bb9d05-b8ba-39ce-8d94-69400d3a80dc | -10.3296 | -45.3799 | 2026-08-30 16:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 1450d5d5-1793-3c29-b268-59e041fbed60 | -12.3232 | -50.5678 | 2026-08-30 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| c2e6197b-24fd-3d04-bb7b-47b230e459fa | -7.5272 | -44.3413 | 2026-08-30 16:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 5053f5e3-e504-35cb-bb08-018dfe9046b0 | -9.6941 | -65.077 | 2026-08-30 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ebba6ad7-3cae-3005-a24a-312e391acb5a | -10.5601 | -50.4022 | 2026-08-30 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| a505c6f7-a5a9-3c4c-8906-7db258100676 | -9.1523 | -59.6384 | 2026-08-30 16:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 65f97d22-b8dd-3cc0-aa8a-b18272b1f2ea | -7.1121 | -42.7963 | 2026-08-30 16:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| fd2e8cd4-55c4-31d6-b2b9-1ee8f6a78f05 | -11.1634 | -50.5727 | 2026-08-30 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 2654d6bd-5e63-3580-8da4-971c446676c9 | -10.8653 | -50.2203 | 2026-08-30 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 7bd9638d-084a-3ac8-b5fe-158d7db16b72 | -12.3809 | -50.5393 | 2026-08-30 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 809b3dfa-c147-36b3-90c1-11f4b6f6dab0 | -12.3427 | -50.544 | 2026-08-30 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| c7e4106e-79e3-3bcf-a388-5d7bb8edf9f1 | -8.5925 | -66.9564 | 2026-08-30 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 150.4 |
| c495ca43-1448-3b4a-93ad-0957035a2686 | -11.1545 | -51.2112 | 2026-08-30 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 0ef2146d-c9b8-3859-bc13-d1296d2ca8df | -10.918 | -50.5138 | 2026-08-30 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 93fb45d5-0d74-37b4-b044-287fc09715f4 | -11.2109 | -51.2476 | 2026-08-30 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 057feb21-a646-3d23-944c-695e2194d701 | -6.0 | -45.0889 | 2026-08-30 16:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 236.8 |
| 0e2dde93-9b03-3e2c-afb0-c638e90ee03f | -12.3232 | -50.5678 | 2026-08-30 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| f2e5ad41-34d4-3949-9c7a-8c238edce8e7 | -7.9422 | -44.277 | 2026-08-30 16:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 193.1 |
| ea292e15-fd4a-3ab4-bbe7-4e14a140b0bb | -8.574 | -66.9569 | 2026-08-30 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 5e85e6d9-c24f-3276-b184-86e1139ba1d3 | -7.5272 | -44.3413 | 2026-08-30 16:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 1fc5bf0c-8b5b-3619-bb2b-0975215a3ac7 | -10.4794 | -64.5012 | 2026-08-30 16:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 71973b49-a3a6-3226-a521-72084e20ae09 | -10.5596 | -50.4449 | 2026-08-30 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 4b60d5f3-c087-3bbd-a586-f85aefb589d7 | -7.1121 | -42.7963 | 2026-08-30 16:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 184.0 |
| 397381bb-08c7-3d92-8385-7cae77a99adb | -8.3679 | -57.6737 | 2026-08-30 16:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 9ac065c5-0c59-3249-bccb-e4683c2ce358 | -6.9872 | -59.2582 | 2026-08-30 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1015294d-381f-35c0-8133-0c280cc7b887 | -8.631 | -66.5473 | 2026-08-30 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8751893a-9d36-3e48-bc49-854150e38fa9 | -10.8249 | -45.3382 | 2026-08-30 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 457.7 |


[Clique aqui para ver as próximas entradas](README99.md)
