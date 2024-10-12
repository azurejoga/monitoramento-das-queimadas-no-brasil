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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a14d09c-00c5-3365-b86a-f10064a0b6ec | -10.74843 | -60.75082 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a50b42c0-7270-323a-b2c4-1d9647d77587 | -10.46941 | -61.24957 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 985d9f82-fe48-3c89-922f-f94e1e7b8184 | -10.46879 | -61.25404 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 70fcf140-c839-35d1-826c-d59637ea31ac | -10.42949 | -61.0055 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 638be137-1f73-3c52-9eb8-afdba67dacaf | -10.4289 | -61.00992 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4125d22f-74f1-3ae7-8741-64904480cadf | -10.42498 | -61.0048 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8338d89-bfd3-328c-b1cd-434c3cea059c | -10.42439 | -61.00925 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ae68469-2dba-339d-84f7-faab6c2281d1 | -10.42301 | -61.00624 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e4e2fb6-e35f-36fd-9df6-b78add3e6095 | -10.41914 | -61.00095 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90231602-9642-3a02-9263-42697815cf35 | -10.4172 | -60.99403 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 890e12e5-f06b-38c2-a655-a35ee3de361e | -10.41529 | -60.99553 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1b1c011-f169-3e44-af02-a38b788dcf7f | -9.88338 | -60.82057 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03ed7d14-9c8e-3f33-b775-1f058a94bcf3 | -9.39532 | -60.90594 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 117b4fdb-ba04-3d7b-80ef-71ac3ebc0dd1 | -9.39084 | -60.90535 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee1b4f66-4630-340c-bbf2-2e97f7680e88 | -9.38899 | -60.91883 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e34084b-8ad2-306d-99d0-28810070837c | -9.38636 | -60.90474 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 498eaeff-0f53-3fca-85f8-4649090faedd | -9.38512 | -60.91376 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22b19a8a-256e-3a48-b578-bd83ffb4b93d | -10.06078 | -61.12477 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82ea91f7-0ccb-3097-8abc-778604f7ff71 | -10.05697 | -61.11954 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0596079-591d-3a40-87f6-7533db1a64b5 | -10.05254 | -61.11868 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e38f8a27-9865-329e-8878-4cfcfc37c88c | -10.45984 | -60.10552 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13438d45-5050-36d4-a853-60da4354bd2a | -10.45498 | -60.10521 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e35de03e-96d9-329e-9b83-7f6263a15fae | -10.45431 | -60.11032 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb5229d4-40f0-307e-a4f1-c3e2f7c3a440 | -10.34791 | -60.21587 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f8602e1-2fb1-3045-803a-7cf0351e8aa8 | -10.17006 | -59.86424 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 140651be-8853-36bf-b414-4284fa6492b5 | -10.16934 | -59.86971 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c672fc7-f194-35e1-b15b-89a6afc74aae | -10.40722 | -61.27424 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cb0f57d5-ac18-34b4-9f23-a20f5da96193 | -10.4034 | -61.26905 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f21360f1-d9f0-3957-b318-b4ebd9f7561d | -10.40323 | -61.23656 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec5d2be5-ec20-346e-a872-ae4e14df09fe | -10.40277 | -61.27373 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 142bf49c-62c5-3cd0-98a0-08ebd573b294 | -10.40214 | -61.27846 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 95dee5ab-bbf8-3fc9-9908-73f5385e084f | -10.40155 | -61.2828 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 57bca459-262e-3a94-a17b-ada5cf0ba1d8 | -10.40122 | -61.21777 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8e7e45e-3a39-31b1-bdc8-b5bf5e5acaed | -10.40099 | -61.28701 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bb89f4a1-72d4-336d-8a31-0a19d8a0e2ca | -10.40041 | -61.29127 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 61db31e6-d98f-35fd-86f7-451329dbf67f | -10.39958 | -61.26385 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05ab8a7e-cec6-339d-b2b2-f0f419a60e07 | -10.39881 | -61.23574 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84b66911-538d-37b4-9c75-330fbd4898e9 | -10.39831 | -61.27331 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e4cc1e36-cde1-345a-9763-4fe0da6931b1 | -10.39767 | -61.27814 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2f8df47f-3784-3d21-8a07-61b01b378711 | -10.39709 | -61.28244 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a0961d15-c242-3073-9299-d25b2bf08d84 | -10.39677 | -61.21707 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e11e3c8a-4d2a-3470-8edb-ac4b9eb3cad4 | -10.39597 | -61.29074 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 61406727-9cc6-3ae9-baf6-2686b389b861 | -10.39386 | -61.27281 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4494c8bf-9321-3975-ac89-ed9450029f3a | -10.39324 | -61.27745 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 249ff609-a258-39fc-b9d4-64d65be2356f | -10.39067 | -61.20408 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a966ebd3-1f92-3753-b12f-5e9484467152 | -10.38965 | -61.20237 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48cfa5f5-1f43-350e-8047-92ff186b1025 | -10.38684 | -61.19899 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dcf12d76-28ab-32ce-85ca-9d1fbc480a60 | -10.38624 | -61.26221 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99992d22-828d-36a4-b225-26da9fa5f1e2 | -10.38621 | -61.20348 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a3306bcc-3477-3504-9bc4-9cd43db26aea | -10.38579 | -61.19728 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 815ad708-581d-3588-9cb9-760a1f152114 | -10.38562 | -61.26688 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8fde0cc-400e-3a0e-bc9b-0e6f0514ce32 | -10.38559 | -61.20794 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b6eef241-6f72-3d72-ad32-040e33406b66 | -10.38519 | -61.20177 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e92567f-f0db-363d-bc12-297da1cf14ed | -10.38496 | -61.21239 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc0ee327-4caa-3320-8ed5-a9ffaf578765 | -10.3846 | -61.20626 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8fcc050f-3b6a-31f3-9d5c-22dea14b5cf6 | -10.38401 | -61.21072 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e815d3d-6c2c-39df-be5b-13021493fc07 | -10.38245 | -61.23029 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9d5e304-8c8f-38c4-9f40-5bd996fd2601 | -10.38241 | -61.26279 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8730cbe5-79cc-3063-b99a-492f34d56908 | -10.38238 | -61.19844 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0cbcfe55-4e74-3570-9569-327fea26275c | -10.38187 | -61.26108 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 504aadc5-95d1-3211-8c9b-99395a59d350 | -10.38181 | -61.23487 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e87204bf-416b-3a4e-80c0-ed7d342e6168 | -10.38175 | -61.20293 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dbb5eb27-157e-30f1-b588-41ce77fe6c31 | -10.38126 | -61.26571 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e713808-bc1a-3b64-8050-c894f264dce6 | -10.38113 | -61.20739 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fe434c47-515a-3119-8f50-953ca25daddf | -10.38104 | -61.23318 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f975da4-bb02-37f2-a793-09874b6d1faa | -10.38073 | -61.20122 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e48cbe92-cf0e-3323-8c85-96786cbaa338 | -10.38014 | -61.20571 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a03e213-9c3f-360e-85a8-403aa9b96b25 | -10.37955 | -61.21017 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a26ad8f-6696-3c6a-ac97-ba9e7fd3ddfe | -10.37866 | -61.25734 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5619922b-157c-3665-81ee-795fcf1bc4f0 | -10.37802 | -61.22963 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cff969d-58e1-3148-842c-2b7d41002ff7 | -10.37747 | -61.26014 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f6f8e30c-ec91-3453-95f1-6952b0fbaa50 | -10.37738 | -61.23419 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae56e65c-64f1-301a-8916-f94050a27842 | -10.37661 | -61.23247 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f83aecad-7e0b-3b0e-be5b-546324bc70e4 | -10.376 | -61.23705 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5a8039c-72c9-31db-b5db-1ffd28a386ac | -10.37425 | -61.25652 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| daf44e8e-15a7-3b40-9abd-b8cc6557fd52 | -10.37296 | -61.23342 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08efe24b-002f-32e7-9046-80dc91cb9210 | -10.37232 | -61.23793 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c16174e8-bb7f-3a4e-b887-3ab5e45e7f8e | -10.37212 | -61.17419 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae02540e-8912-3eae-8b8d-204115c6fbf6 | -10.37167 | -61.24263 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c1a1c42-2862-368c-b2c6-6a5a608af0ec | -10.3715 | -61.17865 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f26be1fb-12f2-3947-b215-08897a479d1f | -10.36984 | -61.25573 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a37a5e7-8d57-3d57-bde4-88968a62e804 | -10.36922 | -61.2602 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f89023b2-2728-3174-8199-a5f07acaa997 | -10.36853 | -61.23271 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45795b07-f092-3d6b-a84f-d8f40c16e309 | -10.36791 | -61.23716 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9cd5983-0abb-36e5-a4f1-68908d832e72 | -10.36766 | -61.17358 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46be5f48-7fb6-3325-9d9c-98ea11e091c6 | -10.36704 | -61.17805 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 755d5191-377d-385d-ab5d-235c22476c01 | -10.36347 | -61.23647 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fc3259d-49e4-3c32-a29d-5af5c17d7657 | -10.36224 | -61.24534 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b303cdc4-ec2a-354e-8c59-383e1e50d346 | -10.35841 | -61.24035 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23940e14-9064-3dc6-aa19-84a8e1a3a219 | -10.19044 | -60.89917 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a70944c2-cbe8-3433-acf9-6a88340b2b2d | -10.18977 | -60.90404 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1f7584e-57a5-340e-a905-6e94722f8db3 | -9.946 | -59.80081 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8060277e-6cfc-343e-81c0-a0e485fff993 | -9.94527 | -59.80609 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0c480a8-21a6-38b2-a38b-2162c2d7f1ce | -9.94395 | -59.80258 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 711a0bef-c4a0-33c9-a739-65f10701f270 | -9.94116 | -59.79992 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f73e709d-a975-3559-b55b-03744d3b140e | -9.94042 | -59.80525 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3047d93a-0b88-34ce-87cc-7e55d016ed41 | -9.93911 | -59.80163 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43da9a59-0aa5-313a-a906-1b524b280de2 | -9.93057 | -59.94257 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2f6561ac-d89f-31d3-8d48-8c7d66edc79d | -9.92634 | -59.90722 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c00f18a-2ff6-3705-b54f-4b418cf28d35 | -9.92578 | -59.90396 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README145.md)
