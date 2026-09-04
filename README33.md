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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16a1ad76-5a61-3e8d-bc86-49d5e6734f23 | -3.14165 | -61.21545 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae59bcac-31d8-38d3-8673-ad50bb15ddb4 | -3.07882 | -61.08625 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19df569e-a88f-3259-8c7f-66e470b026e4 | -8.10465 | -54.78705 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67577f0c-6fdb-360e-b874-d49a5d60d04b | -6.53108 | -59.93346 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ef2962d-bbc3-34ee-85bd-58c812a9028d | -6.59837 | -59.12056 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b70a3062-0cff-380c-a5b7-66d131e9993a | -4.09956 | -60.66124 | 2026-09-04 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63c66e0e-5d3f-3a08-ac33-c700fed96aff | -6.13472 | -57.68478 | 2026-09-04 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f178b7bb-9442-3653-aba9-b8b36eb56452 | -3.29383 | -57.88024 | 2026-09-04 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 104dadf5-6a5a-30a2-88d6-f55d57d095ed | -3.12686 | -61.23117 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfb30189-cc12-372a-971a-e2d60cfce713 | -3.16383 | -61.12431 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5520c182-d05d-3ec9-9ccd-5099795b5229 | -8.10539 | -54.78121 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db7d6351-a1b9-311c-814a-3bf9f0370821 | -7.55572 | -61.34373 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 10a2e26c-eecc-331c-a6d7-46bebc0d0b85 | -6.93789 | -62.88433 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c542620e-225b-3843-a5d4-7a7f2b84324b | -6.66994 | -59.94599 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c60868a4-cc06-3a74-8999-02b93b2038c6 | -3.1787 | -61.16312 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c1c0482-dcc8-3971-a5e0-044e65fd031d | -8.16762 | -62.7738 | 2026-09-04 05:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9a72eb3a-5f26-3764-8fb8-9de315b44825 | -7.46536 | -63.74761 | 2026-09-04 05:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 513b70a0-b6fa-3bca-bec5-72d196c2e393 | -3.61562 | -60.56523 | 2026-09-04 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b6f259e-3f4a-3edf-8d2f-8b8ea7f62481 | -7.55456 | -61.35179 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9926ec77-dda0-31b9-9cb0-48a20f4cf35a | -8.11872 | -54.78311 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a8185dd0-1fc1-3bbe-ad38-d0fee7c5f476 | -6.67392 | -59.95139 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afe2ce7d-a815-3b8c-980a-1173ec5dd587 | -6.63931 | -59.44159 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7a7120d-63ad-3714-a0a1-37be1e3c9dc5 | -6.68256 | -59.95741 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57a96620-2014-3ff3-b157-b6f0dca3904a | -6.68462 | -59.9431 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3afe81d1-022d-34d7-b382-4285d9f37f2f | -3.02345 | -61.49875 | 2026-09-04 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5495e680-da8a-3ae8-8694-90dfe4af2f43 | -6.67468 | -58.7668 | 2026-09-04 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6960b3c-c780-3d19-9ed2-711e133a9b08 | -4.48346 | -55.08191 | 2026-09-04 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 716a133a-a329-3650-b922-9241b68d20c6 | -7.09357 | -56.51702 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 487aa782-2c2f-3855-a7b5-8ae83fff8efe | -7.7944 | -62.34862 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e33961e-fe6a-32dd-883e-ba695a08f154 | -6.70628 | -62.85996 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d5206f5-7c02-3124-9b0b-7c57842b7335 | -3.14229 | -60.64449 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17ba55a1-ca3d-3c01-af7f-a26da13a1852 | -6.71011 | -62.86055 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2de325e-372e-302d-811d-9a220903633f | -3.77435 | -61.75992 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a622e460-7bf9-32dd-9dd8-eac786ddb4fe | -3.08133 | -61.17781 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de81d75c-1e06-3d56-bf8c-a94f13e43916 | -6.68513 | -59.9725 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 178a0ebd-65e4-38fa-9c0a-bc3a482b64cc | -6.68307 | -59.98681 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c7c6af16-11b3-38d5-9694-0fadcf78d8ca | -7.46782 | -63.74575 | 2026-09-04 05:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2b397a5-462b-312c-a365-fc51c2380d98 | -3.21821 | -61.17642 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1eac8711-b9d0-32ca-8add-853737d43226 | -6.69048 | -59.96831 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 76c5578c-94a1-3e49-8d44-dfbb11a40122 | -8.20476 | -62.7948 | 2026-09-04 05:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c958acd5-cfdf-3cc4-ad07-950f5aeddc68 | -6.68141 | -58.75588 | 2026-09-04 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30a7cbc5-4a17-3bb1-911b-a85e46c28890 | -6.68583 | -59.96767 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 734b2cd6-be63-3582-ad8e-056a410fd81f | -6.70556 | -62.86469 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7472bcaa-083b-3384-9205-ec9162778af2 | -6.67323 | -59.9562 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a5b5856-c87b-3f5d-8637-8c7425351e4b | -6.99478 | -62.98655 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de40a09f-57e4-3d9d-a66d-0e8859731deb | -4.12481 | -56.34336 | 2026-09-04 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6fdef79-1646-3caf-a3e2-9c5dff52772c | -6.69237 | -59.98805 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| de5367ab-1d4c-3471-94b6-88fd45d992b5 | -8.11205 | -54.78217 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b2c5946b-cccf-3a07-b567-4f05caba2024 | -6.68117 | -59.96704 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f274589d-1e97-3b89-b173-f9e8f6c6a0a5 | -3.20125 | -61.2318 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79cc15d7-53c2-3ca4-9d2f-7e6bcd1c1644 | -3.75935 | -61.75253 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c827a61d-b55e-3880-8ee6-1bf2ec0a3402 | -3.67573 | -53.74815 | 2026-09-04 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0dde4b4-20f7-3909-8c38-9332c8c3f8ce | -3.39075 | -61.32105 | 2026-09-04 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4de0f0eb-a368-34fd-a409-cc906e717f60 | -7.78569 | -63.38914 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be61efe5-455f-35c9-8502-34ee5daccedb | -6.37506 | -58.28836 | 2026-09-04 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 497f5c2f-e7e5-3d25-864b-a908344e2bf4 | -3.02423 | -61.49368 | 2026-09-04 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0330894-8f3b-328c-8d32-3b16ac8db321 | -6.67996 | -59.94245 | 2026-09-04 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d509bcc6-b6cd-3d12-97ec-df6ade441efe | -7.0139 | -62.98941 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46cade3b-7cee-325a-8733-e56ce0c290cf | -6.69305 | -59.98333 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b4fe750b-e9dc-375e-93a2-75c2cc4636f5 | -8.43721 | -54.68525 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61a83698-0913-3bbb-a1e5-e06dca4869b6 | -3.78302 | -61.75613 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20ad262d-57f9-3c61-a184-9649fb335a68 | -7.02225 | -62.98587 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f086bade-57b6-3888-9bfe-77449830a0b1 | -6.64414 | -59.44221 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4279c4b9-c3fd-3583-826e-cc686bdefefb | -7.61759 | -57.61597 | 2026-09-04 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8417f1f-a644-3358-a757-d287123e2f9a | -3.07176 | -61.07788 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbf14be9-45fe-38b8-bb73-3782e04c45ad | -7.01078 | -62.98415 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac5ed6af-d810-39dc-bf7d-40a15962989e | -6.15692 | -57.7607 | 2026-09-04 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 059ed5f0-8547-395e-ae4d-0589beb617d4 | -6.37551 | -58.28521 | 2026-09-04 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ec4268e-bfb0-3383-beaa-41f3ce87ea8b | -7.86186 | -63.75581 | 2026-09-04 05:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e43432fd-0e68-352d-a458-ca8526bc31f7 | -6.68978 | -59.97314 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 4f110828-531e-34d1-9a7f-5180fb5988b0 | -6.67583 | -59.9712 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6dfd9a8-f4ca-34a4-9634-529139f4a528 | -3.77398 | -61.75657 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a404df1-aa4d-344f-9b91-c18b0a09a2cd | -5.17798 | -60.28403 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db744435-044c-3b9e-90e4-c03c163ae1fb | -3.21805 | -61.15083 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fd8654a-fe75-3758-ae08-94d20eff5605 | -8.10905 | -54.78165 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a793c7f2-bea8-3569-ba92-80a15cbc47de | -6.99861 | -62.98712 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0980513-79e7-3b6b-9352-7a3ad2df8d51 | -3.08023 | -61.18492 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9c5842c-498f-30dc-a4ee-558f3a9e550b | -3.3913 | -61.31755 | 2026-09-04 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7a9dc53-73a8-3cec-9d60-523ac8fe8922 | -5.14677 | -60.31051 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5262ee8-9e58-3cab-9149-3c602cb31668 | -6.77457 | -58.9543 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d65c00c4-00ab-3329-9263-821ed57f1f18 | -2.70059 | -60.9601 | 2026-09-04 05:59:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 771dd09c-f7ff-32ab-b695-b350cf94618b | -3.78187 | -61.75777 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9ecadb7-c693-3003-a373-aac15d14ec07 | -7.5526 | -61.33507 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6c14171a-325c-3ad6-bc34-3291fcf6b908 | -6.13375 | -57.6917 | 2026-09-04 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b6606aa-95d1-38fa-a2aa-6bd9f170ab5c | -7.55631 | -61.33969 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 109a9b84-aaeb-34f4-ba75-8c5532458596 | -4.48971 | -55.08274 | 2026-09-04 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 361bfd4c-e984-3b5b-9950-9eeef5c5cd8e | -6.68186 | -59.96223 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 171edb8d-4313-3e7a-b01b-d9a7eb55b21d | -3.19881 | -61.14065 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07479e5b-4b8c-3759-ade1-31e44c4844d8 | -6.9979 | -62.99181 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6061761f-9004-3aab-8472-6a06219a3149 | -4.12365 | -56.35121 | 2026-09-04 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d152f2b-789b-35c4-ac76-fcb061bb7c54 | -3.21398 | -61.15022 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a593568-d422-3cf7-ad9f-464cc1ca5854 | -6.11737 | -59.96183 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82f2298a-f2b3-36e6-b1b5-e1aea305b818 | -3.07529 | -61.08207 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8733746f-1a73-3c1d-b2b1-df0d9c1690b9 | -5.85305 | -61.16728 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| baa9b622-feb1-346d-8202-e57f802833ff | -7.53733 | -60.72324 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34617481-383a-34a0-bd6b-d4439a9412d3 | -6.57064 | -58.56392 | 2026-09-04 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9067d7cf-b18b-319d-aca3-e17d719a3e76 | -7.73905 | -61.65097 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fec9bb02-602b-3b62-bcb5-39ccdee34a15 | -6.78456 | -58.95569 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbceb47f-4c88-3c43-9654-682e5e6d8244 | -3.02026 | -61.49308 | 2026-09-04 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8d4ff71-b659-3f89-ad3a-4be0532904a1 | -3.1603 | -61.12011 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README34.md)
