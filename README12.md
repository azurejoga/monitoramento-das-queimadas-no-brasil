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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fde1a57-5307-36b3-9d66-bfc854193fda | -3.89719 | -54.69014 | 2025-08-24 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 717dd7e3-dfa1-3503-a5be-29cf2c36ed9d | -2.93365 | -53.7095 | 2025-08-24 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4b51b2d4-774c-31ad-9700-218ff47678a2 | -3.44336 | -49.04566 | 2025-08-24 00:52:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f89c695f-966c-3b92-aa33-c5a31efd3eac | -1.55601 | -54.54263 | 2025-08-24 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 13e56ec2-f6bd-3ba3-acec-5f919a0f3c89 | -3.84361 | -55.96983 | 2025-08-24 00:52:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 078d6d4a-1658-35a6-bb08-50e9e834929c | -3.05816 | -49.50239 | 2025-08-24 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e1377228-3eec-320d-b762-a0958216f9e8 | -2.93122 | -53.69189 | 2025-08-24 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| bf6a0f98-2fd6-3414-8d3c-5dc37d2b8516 | -3.60823 | -47.52922 | 2025-08-24 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| f7d3dde3-4466-3d89-99fb-bc757b75d783 | -3.60053 | -47.52453 | 2025-08-24 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 195.1 |
| 378b2584-1ea1-391a-ba97-2142f9475106 | -3.59367 | -47.5136 | 2025-08-24 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 3f06826d-32b0-356e-b7c1-609710012a40 | -3.65835 | -54.76028 | 2025-08-24 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4d2dabc7-38ff-3f68-b7b8-89065332c9f7 | -2.92361 | -53.70193 | 2025-08-24 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 072270a2-4eb5-390d-a5a4-c1e182f6d682 | -3.51294 | -47.21491 | 2025-08-24 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| e02ed5c7-759a-3202-abc7-ab6bf8a9066c | -4.04465 | -56.31504 | 2025-08-24 00:52:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d3796240-030f-34dc-a7a5-e800b7835598 | -3.59613 | -47.53086 | 2025-08-24 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 787e2ce4-ef27-385d-8cdd-7d6fd5298676 | -3.58175 | -48.15786 | 2025-08-24 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 951911b8-fb22-388a-b015-d5fd54159c82 | -2.91397 | -48.3139 | 2025-08-24 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 43610376-e544-32d6-aaea-1375d7c57cb8 | -3.51019 | -47.19612 | 2025-08-24 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| f4040675-42a8-3659-8eb8-dd053231c1cb | -3.58844 | -47.52623 | 2025-08-24 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d4ac053d-5b9f-3cf0-b1df-158230487be1 | -3.60313 | -47.54183 | 2025-08-24 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| fd427cc4-906d-356e-a1ca-75235b1f7d32 | -2.93244 | -53.7007 | 2025-08-24 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e9657e38-792f-346a-8c52-881dfbadc621 | -3.40174 | -52.83659 | 2025-08-24 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 55ba10ef-d8c2-3638-972b-72aac3c31465 | -3.43264 | -49.04722 | 2025-08-24 00:52:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| a8e0ef64-b9f2-3118-9586-03f025c01a64 | -2.26469 | -47.85373 | 2025-08-24 00:52:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| fed9e647-4848-3269-af34-047e402a4ab2 | -10.6131 | -44.3051 | 2025-08-24 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 889329eb-4c9f-35f9-9860-7b5d4a244826 | -3.5994 | -47.5359 | 2025-08-24 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a5cc039e-6952-3b5e-bebe-85af97118190 | -9.1536 | -59.464 | 2025-08-24 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 243.4 |
| 88551878-4dee-3b45-ad97-90f895615cd8 | -9.1533 | -59.5027 | 2025-08-24 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| fa7fe9a0-a7c0-3676-96cd-54bd5c6c7b19 | -20.3594 | -51.7023 | 2025-08-24 01:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 377538f0-e998-37ee-a348-3589086b078b | -8.6131 | -62.5929 | 2025-08-24 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b2020d5f-a032-3257-8ce5-52635fb57047 | -4.9605 | -55.8226 | 2025-08-24 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 3bac905f-d703-3d37-acfe-cca98dcaa10f | -17.4045 | -42.6186 | 2025-08-24 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0e2c0afd-ca89-344c-b8c0-478f34ba5c6e | -17.6183 | -44.2738 | 2025-08-24 01:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 62.2 |
| da5cf4f2-6367-314e-9703-0e0c9cc8c82e | -10.6128 | -44.3284 | 2025-08-24 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c5ec9f23-ee51-3662-a05e-2aba21128392 | -22.8039 | -54.0134 | 2025-08-24 01:00:00 | GOES-19 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 90.9 |
| 490e6295-02c8-383b-a467-503bb10e1a4e | -11.5055 | -51.8705 | 2025-08-24 01:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| cdc8496f-3072-38e2-a11c-b0c159366e82 | -10.6006 | -50.2058 | 2025-08-24 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| ec42bffb-7e3c-363e-8160-7f0ba172f454 | -14.8157 | -47.9118 | 2025-08-24 01:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| aa969424-a189-31ff-8c10-a5566767de63 | -3.5083 | -47.212 | 2025-08-24 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 66cb6a00-330d-3be5-afb2-2dae156e3ed5 | -17.3844 | -42.6235 | 2025-08-24 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 03a8b11a-e8bd-34cb-ade3-5113c447f667 | -3.5995 | -47.5142 | 2025-08-24 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a19e05c5-35a1-330d-99e7-b473598893f5 | -9.0232 | -65.6982 | 2025-08-24 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 140.8 |
| c675d4ff-4c23-3846-97d6-8ab4ce434a1a | -9.1722 | -59.4629 | 2025-08-24 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 187.9 |
| 6dd97f10-ed39-3a74-8712-4720419274c3 | -17.6176 | -44.298 | 2025-08-24 01:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 27d384dc-ce7a-3611-ae23-4083ee097fc4 | -8.9106 | -62.4289 | 2025-08-24 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 621db55e-d3c7-3d64-a51f-bfd47e03df88 | -5.4181 | -60.1784 | 2025-08-24 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 1853e32d-f56d-3c8f-a2e4-7d800872fe5a | -11.9867 | -61.0214 | 2025-08-24 01:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 40ecbfac-5e2c-380f-98d6-19532b60a054 | -9.1538 | -59.4446 | 2025-08-24 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 25f50a0b-6105-3bdd-875c-6c13efbcaed8 | -20.3396 | -51.6839 | 2025-08-24 01:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 3c4a08a0-4b5a-3886-96c7-3a987ee1a701 | -9.1998 | -60.793 | 2025-08-24 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 53968563-5f83-36ad-a3fd-032b9771ef68 | -20.3599 | -51.68 | 2025-08-24 01:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 165.7 |
| efd2e6ff-314d-35fa-a2f1-c841212d4a60 | -14.8153 | -47.9343 | 2025-08-24 01:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 8b896003-3b52-3b7d-8eba-38ee7cfd6c10 | -10.6009 | -50.1843 | 2025-08-24 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 21ae6840-f5d7-3731-9fb6-8238905bd609 | -17.5975 | -44.3027 | 2025-08-24 01:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 595f4d87-8bcd-327b-9df8-d8e6bde4b049 | -11.5245 | -51.8685 | 2025-08-24 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| b58159c3-989b-3153-aeac-832a5875b462 | -14.7984 | -59.6145 | 2025-08-24 01:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 3e2b0d74-a2f8-3344-abda-21f79a7bb96a | -5.4182 | -60.1593 | 2025-08-24 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 54846332-0d09-3af0-bd78-5d46e52bcf92 | -9.1441 | -60.7765 | 2025-08-24 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 19082fa1-c0de-3fd6-b7c3-f512d56eef91 | -5.4364 | -60.1779 | 2025-08-24 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.0 |
| b185cb1b-bcee-3234-aca3-1319751fc7d1 | -9.0061 | -65.3813 | 2025-08-24 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 592813a4-a63c-3027-8930-e427f6dda819 | -9.0416 | -65.7163 | 2025-08-24 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| eb0e5778-2f6e-3f02-961c-1ea9fc59ffdd | -20.339 | -51.7062 | 2025-08-24 01:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 916426e9-279b-3964-885b-88bf90d63527 | -9.1535 | -59.4834 | 2025-08-24 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 192.1 |
| d4e3267e-21eb-309c-aec8-a2617c374133 | -10.5937 | -44.331 | 2025-08-24 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| f4f42f28-36ff-3aa8-abea-fe0dd9c0ea56 | -9.1721 | -59.4823 | 2025-08-24 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 165.1 |
| b074f597-e3bb-3f19-bc70-cc6d31be5bb6 | -16.797 | -51.3419 | 2025-08-24 01:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 66a24b1f-9793-3b56-9360-8e2a35abb371 | -5.4365 | -60.1588 | 2025-08-24 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f7e58fab-84d3-38ba-98cd-bc1e3d49c127 | -9.0046 | -65.6988 | 2025-08-24 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 42c7182a-634b-35d5-842c-c1717e2026ad | -9.0246 | -65.3807 | 2025-08-24 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9d55ddc6-0917-3d7e-9f95-4c072b7c9ee3 | -16.7965 | -51.3637 | 2025-08-24 01:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 546910d0-91a1-37f9-a3df-4ae7b918a075 | -10.8078 | -46.4083 | 2025-08-24 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| f35fee6a-7c77-32bb-b604-d0fc820b3892 | -20.3701 | -46.7433 | 2025-08-24 01:00:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 66b4c42b-843a-326b-a59d-2824483d7f54 | -5.4026 | -44.9952 | 2025-08-24 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 677f4435-126d-3211-b3a7-c82fbf863da5 | -9.0045 | -65.7174 | 2025-08-24 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a2d65b23-4d03-3f87-bf2b-34414348f385 | -9.0231 | -65.7169 | 2025-08-24 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.7 |
| c2eb24b3-50b5-37b2-9290-e39880e5eba1 | -10.5819 | -50.1863 | 2025-08-24 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| bce33142-3f0b-32a9-b07b-fb3b2a3c7ccf | -9.1535 | -59.4834 | 2025-08-24 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 187.5 |
| 3995d40b-13b9-3a48-a78c-ae1bbdadeb4f | -22.8039 | -54.0134 | 2025-08-24 01:10:00 | GOES-19 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 135.1 |
| e0f44b38-470f-3ef7-8e03-c1003cf814c8 | -9.0045 | -65.7174 | 2025-08-24 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 66548994-cc57-3052-b3dc-0acaa2b81fa0 | -22.8045 | -53.9912 | 2025-08-24 01:10:00 | GOES-19 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 96.9 |
| 74bf3b55-8304-3be6-84f6-e93a1d950a2b | -10.6128 | -44.3284 | 2025-08-24 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 5cde8a09-5b68-33c6-9c67-3c8dbee44f09 | -10.8078 | -46.4083 | 2025-08-24 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| b12aca0c-5432-37a2-a66a-2d93ad4e7296 | -17.5975 | -44.3027 | 2025-08-24 01:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| e033ed71-19ff-3711-8df1-03c8e945c7e2 | -16.7965 | -51.3637 | 2025-08-24 01:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 53c396f3-1762-3f39-897f-d6f8b9b07942 | -9.0232 | -65.6982 | 2025-08-24 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 77d5904e-09c5-36a1-b039-bdcbc9e55e00 | -8.6131 | -62.5929 | 2025-08-24 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bd0ea835-8989-32ef-ac81-04ec514a143c | -3.5994 | -47.5359 | 2025-08-24 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 4cf61e34-d3f8-3362-8df2-be8b95dbf22f | -7.5534 | -63.8556 | 2025-08-24 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| a709d758-d087-3a6d-a6d0-e2ed85917dc8 | -9.1538 | -59.4446 | 2025-08-24 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 95d239ad-ac31-34d3-9f9b-d4ddad63b981 | -9.0416 | -65.7163 | 2025-08-24 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4d90b404-35e8-3ebe-b6c1-1b9a767f6c64 | -11.5245 | -51.8685 | 2025-08-24 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 1b7cbda8-d49f-301b-82a4-909139560b14 | -20.339 | -51.7062 | 2025-08-24 01:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 18509f33-ce69-338d-a9a2-53b1a46e0999 | -16.797 | -51.3419 | 2025-08-24 01:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 104.9 |
| d51eaf04-613f-3e5d-9f8d-8679eb0a3427 | -17.3844 | -42.6235 | 2025-08-24 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| eb5e6739-3bed-3c13-8af0-44397b1da1a0 | -9.1721 | -59.4823 | 2025-08-24 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 144.6 |
| fede1aa4-9e17-3ce9-84c3-e9035fc57724 | -20.3594 | -51.7023 | 2025-08-24 01:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 8fbad28c-2ac7-349d-b442-5f6a44003532 | -5.4181 | -60.1784 | 2025-08-24 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.5 |
| d3e7c254-14ed-3b1c-b0f7-e305ca479a14 | -10.4164 | -47.1732 | 2025-08-24 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ddb304c1-216d-30f8-971b-35d9c5b37fa8 | -9.0046 | -65.6988 | 2025-08-24 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| df08c943-d8c2-3c4c-880e-6c03b81a5b7a | -9.1722 | -59.4629 | 2025-08-24 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 171.8 |


[Clique aqui para ver as próximas entradas](README13.md)
