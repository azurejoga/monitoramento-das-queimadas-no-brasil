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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c0c8cf2-6fbb-3bde-a6e6-5778371d5919 | -7.1578 | -59.3382 | 2024-10-09 01:27:42 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4750241-5a41-3898-a93c-ea3f4626c09c | -7.1596 | -59.345699 | 2024-10-09 01:27:42 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 172b2ee1-bc7e-3875-9ca1-b40f238ea33d | -7.1919 | -59.756802 | 2024-10-09 01:27:43 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 444f9757-2df2-3b91-a1b4-07a50312d53f | -7.1935 | -59.764099 | 2024-10-09 01:27:43 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4c7cb63-0445-3f06-986f-072a4bee4a34 | -7.1952 | -59.7714 | 2024-10-09 01:27:43 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d21446f9-aa2a-3e64-8748-c47cc6044282 | -7.1837 | -59.766399 | 2024-10-09 01:27:43 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8796154b-de96-3273-8032-f70a6dbb8f06 | -7.1854 | -59.773602 | 2024-10-09 01:27:43 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4229118a-c53a-3ee2-9e84-a147642594f3 | -7.0276 | -59.399601 | 2024-10-09 01:27:44 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 754bc245-b555-391d-9c9f-61504f0d2cea | -7.0293 | -59.407001 | 2024-10-09 01:27:44 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e16b5477-330b-3b7a-ad24-207705a8e33d | -7.031 | -59.414501 | 2024-10-09 01:27:44 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc9863dd-8cb4-37a8-b999-f5ca4d15c4bf | -7.0161 | -59.394299 | 2024-10-09 01:27:44 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db0dc160-c911-399c-bcef-339a05d178d3 | -7.0178 | -59.401798 | 2024-10-09 01:27:44 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4333acfe-cea2-3d6f-8e33-ccbae9cd163a | -7.0195 | -59.409199 | 2024-10-09 01:27:44 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70d55871-ebd2-3c19-80c6-c4655e6ef710 | -7.0212 | -59.416698 | 2024-10-09 01:27:44 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af627abf-1820-319f-8a44-6c1c35365397 | -6.919 | -59.780899 | 2024-10-09 01:27:47 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71bfe74a-7722-34ab-a4d6-12b73963891e | -6.5308 | -58.407902 | 2024-10-09 01:27:48 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f3b1d80-1d5a-31e9-a7a6-62a54baff9ed | -6.5172 | -58.393501 | 2024-10-09 01:27:49 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 458589f4-6627-3453-8dc0-7f37cf14f488 | -6.5191 | -58.401798 | 2024-10-09 01:27:49 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9f0cd13-e1e1-31e6-afb8-665deb4e1715 | -6.521 | -58.410099 | 2024-10-09 01:27:49 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 41bd4630-d6a8-3b72-b356-4b4c0a2cbbcf | -6.523 | -58.4184 | 2024-10-09 01:27:49 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39bf7d28-5dbf-3f52-a130-d0dda674f498 | -6.7691 | -60.027699 | 2024-10-09 01:27:51 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5d36d5-dbf5-3813-9dfd-6164ffdf37eb | -6.7708 | -60.034901 | 2024-10-09 01:27:51 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 129de860-eb57-379c-957d-a3ba9fc7a2b1 | -6.7724 | -60.042099 | 2024-10-09 01:27:51 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc792cf7-a242-31d6-99c4-d619ccbd254c | -6.7741 | -60.049301 | 2024-10-09 01:27:51 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 924827c1-20ad-3360-b4e4-3133bcf826fb | -6.761 | -60.037102 | 2024-10-09 01:27:51 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0555731-133d-323e-b849-54cb1c837484 | -6.7626 | -60.0443 | 2024-10-09 01:27:51 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8a75160-694e-3440-a807-41342beff212 | -6.7643 | -60.051498 | 2024-10-09 01:27:51 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2edfbc46-bf22-3b58-9daf-680c8f74d35f | -7.3051 | -64.650497 | 2024-10-09 01:27:54 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37b38b3e-644c-31d3-b53b-3eb27ce76606 | -7.3596 | -64.665001 | 2024-10-09 01:27:54 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3868aba0-ed7d-39b9-91f8-f68df90ec743 | -7.3577 | -64.656601 | 2024-10-09 01:27:54 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5c387c9-a7e9-3eca-bf74-bf2f72165402 | -7.3479 | -64.658798 | 2024-10-09 01:27:54 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 760367d1-2907-34cf-ab53-2c98959c2bc1 | -7.3559 | -64.648201 | 2024-10-09 01:27:54 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00483969-e40a-37fc-96c8-b9c07e8b308c | -6.822 | -64.318298 | 2024-10-09 01:28:01 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a696774-695d-3726-ab8d-c5bfab030d55 | -6.8202 | -64.310303 | 2024-10-09 01:28:01 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c0039dc-6648-32f4-9a26-64cb57e0e06e | -5.0797 | -60.213501 | 2024-10-09 01:28:14 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 818384c0-ae50-3841-9a24-c3f3f73d8e2a | -5.0911 | -60.218498 | 2024-10-09 01:28:14 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8e81f0d-7030-3f88-884a-32b10695dd54 | -5.0895 | -60.2113 | 2024-10-09 01:28:14 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5788d6c-16f6-3e3e-bb45-66858310ba9d | -5.8948 | -63.887798 | 2024-10-09 01:28:15 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2aef746f-398b-3f5c-a53d-b6927d09c1fe | -3.5584 | -54.3382 | 2024-10-09 01:28:17 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ec8d1ad-4c63-30b3-b10b-f04c7f359695 | -3.5546 | -54.3218 | 2024-10-09 01:28:17 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc6b7f96-9e0c-3483-9685-79981b462afd | -3.2548 | -54.180698 | 2024-10-09 01:28:21 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9ed9f6c-7203-332a-bdab-ecf33ab2b971 | -3.2507 | -54.1637 | 2024-10-09 01:28:21 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43c6ddd9-f425-3f7b-bf94-ef75dbeb801a | -3.117 | -53.7285 | 2024-10-09 01:28:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6b659b7-608f-3c6d-8a14-e95f813e3e62 | -3.1126 | -53.710098 | 2024-10-09 01:28:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbfa1ab3-3e45-330e-9e4f-e8532516b039 | -2.9585 | -53.707401 | 2024-10-09 01:28:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48874081-9704-34aa-848d-3ab8da9e0836 | -2.9726 | -53.723598 | 2024-10-09 01:28:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 846be071-af8f-33b9-a700-88a90a36e719 | -2.9682 | -53.705101 | 2024-10-09 01:28:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 280fa194-05a8-3e3a-90c3-2d01dc79d380 | -2.9638 | -53.686501 | 2024-10-09 01:28:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8730424-2583-34d7-ad0b-5ce76786c980 | -4.2919 | -60.013599 | 2024-10-09 01:28:26 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e58bdd49-f1fc-38f9-8624-fa897cf0b6ad | -4.2902 | -60.006199 | 2024-10-09 01:28:26 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f618491-1f82-30f7-b5e6-733c6ec65a75 | -4.2886 | -59.998798 | 2024-10-09 01:28:26 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97400397-39e4-3da5-bbbe-b61860fca26c | -4.277 | -59.9935 | 2024-10-09 01:28:27 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 62999393-4ac3-3080-b6e6-fa8c6dacb8fd | -2.8007 | -54.340401 | 2024-10-09 01:28:29 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9095ccc6-b98f-34b5-ab7f-1df4d85722e6 | -4.1055 | -59.874599 | 2024-10-09 01:28:29 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f52cbbd-e80d-3dc2-bcf5-f888cc972587 | -4.1038 | -59.867001 | 2024-10-09 01:28:29 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 634262a5-2765-351d-8f64-bf901fa2fe32 | -3.0109 | -59.0984 | 2024-10-09 01:28:44 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e37de012-985e-3e0e-a52b-47cfd9a15aeb | -3.009 | -59.090099 | 2024-10-09 01:28:44 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8140a82f-7ea9-30a4-bc7d-a326a053363f | -2.6854 | -59.566898 | 2024-10-09 01:28:51 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd3885c-45da-39d2-b467-b427f23003d0 | -3.0428 | -61.682701 | 2024-10-09 01:28:53 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 750238ad-2c7e-3966-b71d-3f40f9e53b11 | -3.0412 | -61.6758 | 2024-10-09 01:28:53 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f222103e-f8b4-3ef0-a3ec-c1b360f6c12a | -3.0397 | -61.6689 | 2024-10-09 01:28:53 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa5deb86-24e2-3aaa-9a62-d50b74920b59 | -1.0966 | -53.610199 | 2024-10-09 01:28:54 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04a2081f-955c-3687-a5c1-13e2f87c7bcc | -1.0919 | -53.59 | 2024-10-09 01:28:54 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f6de8c4-ac49-3762-9e7e-2068e4a9c122 | -1.1063 | -53.608002 | 2024-10-09 01:28:54 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8cb5731-e63f-3a92-b3e8-77368e060810 | -1.1016 | -53.587799 | 2024-10-09 01:28:54 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12a405c9-07aa-3445-8f67-8492bf071dcd | -3.6321 | -64.996696 | 2024-10-09 01:28:55 | METOP-B | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46fd84e3-f66a-3b70-90a8-f7f96506a4eb | -1.11 | -53.6173 | 2024-10-09 01:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 9757bc54-51da-3919-bb27-0838f807c888 | -1.1284 | -53.6171 | 2024-10-09 01:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 791e37e9-8c63-39b5-af07-1dccf3b7e64a | -3.8007 | -41.6229 | 2024-10-09 01:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 35d6e37e-1461-3831-9fe2-87c540235857 | -3.8008 | -41.5989 | 2024-10-09 01:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 136.0 |
| 52b4bdd1-dcc2-37e5-b33f-8e88c0343755 | -3.8196 | -41.5979 | 2024-10-09 01:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 81092878-dda8-3355-b033-a2d887f5f7c2 | -3.9021 | -46.4689 | 2024-10-09 01:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 945f36d2-bfd2-396a-9514-6636e8574dea | -3.9023 | -46.4467 | 2024-10-09 01:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 01d266ae-e297-3faf-96a2-f55c89c5ed92 | -3.9207 | -46.468 | 2024-10-09 01:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 6e78319f-2b6a-3529-b591-e43bb2f40817 | -3.9208 | -46.4459 | 2024-10-09 01:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 3bfa18eb-5506-33df-9e3e-24b30f4b57cf | -3.9393 | -46.4672 | 2024-10-09 01:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 7ba88504-e230-3315-8acb-33d0f3f06511 | -3.9394 | -46.445 | 2024-10-09 01:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 6bb7b81f-83cf-3ca5-82ad-019cd3b39448 | -5.4421 | -49.5559 | 2024-10-09 01:35:37 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a9b1ca85-d001-3bef-9223-077f66e670c4 | -6.7613 | -60.0751 | 2024-10-09 01:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9f8400dd-73e9-3a65-9882-a00da1b82de2 | -6.7614 | -60.0559 | 2024-10-09 01:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 174.2 |
| b7593233-7bfb-3aad-8a5c-55eb060325ad | -6.7615 | -60.0367 | 2024-10-09 01:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| bddf71ea-21ea-3263-b94d-db72cbcfd961 | -6.7797 | -60.0744 | 2024-10-09 01:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 63f54dd0-757a-3f81-8754-c2a72ba5c853 | -6.7798 | -60.0552 | 2024-10-09 01:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 225.9 |
| 28c6ff55-a3c6-34e6-bd6a-28738a3de2bf | -6.7799 | -60.036 | 2024-10-09 01:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 94d45687-052c-3ca6-904a-706e2c131fae | -7.1871 | -59.7893 | 2024-10-09 01:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 3b5c0e39-0fe4-3a35-a3b0-d1d38aec97ae | -7.1873 | -59.7701 | 2024-10-09 01:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 75c80374-c18c-3e56-93b4-c8911af6e6ca | -7.2435 | -59.633 | 2024-10-09 01:35:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| ddf92d5c-43b2-3420-8848-e387a40e7857 | -8.4919 | -48.6476 | 2024-10-09 01:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 131.0 |
| fb0ec481-d6ee-3c86-83e4-c6017e62dee0 | -8.4921 | -48.6259 | 2024-10-09 01:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 8ace725d-6789-3b07-bb19-cf32015965ee | -8.5107 | -48.6459 | 2024-10-09 01:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 49c9cabe-d8ed-396d-b46f-b052c3a2178d | -8.5109 | -48.6242 | 2024-10-09 01:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 9c3ae860-a470-3a43-8450-f27bb67e2313 | -9.4635 | -66.7469 | 2024-10-09 01:36:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ea0156ad-1107-3d12-ad28-2e75968779da | -10.3894 | -61.2502 | 2024-10-09 01:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 83548131-f9ae-3136-a0f2-2aaf850680f9 | -10.3895 | -61.231 | 2024-10-09 01:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e0735b04-855f-3d3c-b3d4-d39a5a57a1cc | -10.3843 | -64.8255 | 2024-10-09 01:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 37.0 |
| fa704cf8-2859-3f52-a2b6-e80e623ea4d4 | -10.4287 | -60.9979 | 2024-10-09 01:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 85efcecd-744e-363c-ade8-c5d270e7fa2e | -10.6068 | -55.9169 | 2024-10-09 01:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 03f506b4-6192-36d1-a5ec-d34ab28af08b | -10.6253 | -55.9355 | 2024-10-09 01:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 97b7f636-f024-3a3c-b6f7-30bafd2d7a3f | -10.6256 | -55.9154 | 2024-10-09 01:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 167.5 |
| ca47bb58-6f26-3746-aca5-6fc52bcf2b81 | -10.6258 | -55.8953 | 2024-10-09 01:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |


[Clique aqui para ver as próximas entradas](README47.md)
