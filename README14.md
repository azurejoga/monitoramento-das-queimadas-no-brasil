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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbd44806-b00d-3f78-88ee-9c4df5bb8e77 | -8.3066 | -54.721901 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 207eb6fe-8aca-3a53-bbc8-f34b07cd2944 | -3.1786 | -54.1082 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 388e0c70-3f28-3516-9630-62f83c539bde | -5.1222 | -56.0285 | 2026-10-02 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d7ee95a-d45b-3f73-b642-976255347248 | -7.2718 | -55.597198 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b46b17c-5d90-3a0b-8110-dd6da99201cf | -7.6613 | -55.097198 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b09dcf00-5780-3dea-a89f-166708620e7f | 1.8122 | -55.598801 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a523b0a0-9b2c-3ace-80fb-464bec311557 | -6.4433 | -55.6292 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d779679c-ed4d-34c0-baaa-1c286bc60c56 | -11.8029 | -43.594501 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f4a18c7-6a49-3f4d-86bc-1ac015ab4408 | -7.3402 | -55.225101 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1277760-cc48-30f4-8fc5-4c90a10602bf | -6.3187 | -54.785198 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf0974d5-61b3-3729-ad77-0c5a29d76066 | -5.7473 | -55.743 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad5cb33e-15e5-3b61-8472-79971db9679d | -7.8444 | -56.6035 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8986d8a0-cab6-3d2b-a56a-78d2546baf44 | -7.6982 | -54.769001 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f13c4599-c18c-3946-a046-921894bd6504 | -5.8705 | -53.494999 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3382b33-d4cb-340f-b364-889753b5cf52 | -6.8467 | -55.544201 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9dab926-c678-309d-8795-493b990710e0 | -6.845 | -55.536999 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b49170c-83a8-3e3a-bf73-87e444bb1cb3 | -7.4605 | -54.988701 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dce51a3-172a-34bd-a8e7-a8e902d2ce90 | -8.2594 | -54.7407 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35713ffd-471c-3721-a935-e9c1d9cbb70e | -9.8371 | -44.829601 | 2026-10-02 01:12:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 11676d4b-1efb-3a46-b894-f10d26518ab3 | -11.7478 | -43.470699 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8cc24ff2-2531-38a1-accf-0a7a90d69cca | 1.7946 | -55.630402 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aed42054-e7a5-31dc-bbc6-3919729871bf | -6.1627 | -57.726501 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f014d555-4a1a-3208-8c23-7b58e67d2f16 | -5.8488 | -53.490799 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c86580f-498e-3d55-8f09-24c0fffac586 | -6.397 | -56.41 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1105887e-49fa-3456-bfc8-b4ad2b4d532d | -7.738 | -54.806999 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 733ac899-e29f-3f4d-a018-21143f01f71f | -7.285 | -55.609299 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 200f1476-3400-39ba-a772-acf14f4432ae | 1.816 | -55.581799 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3443a46d-5444-323f-97c8-deab4f2d1ac3 | -12.8244 | -51.476101 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cfdf0824-6175-33c2-a9b8-30d6aff94b6d | -6.7512 | -55.090099 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7435b2cc-5c96-3e29-a672-8507997930e7 | -6.0846 | -57.7005 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0faa63e-11af-3050-9853-e50c70dd6f59 | -7.1893 | -52.619099 | 2026-10-02 01:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25423c88-cc9d-3f37-a789-e901b5a2b0fd | -7.4156 | -55.5942 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4616bec5-5abf-352f-8228-8f6bb35a5387 | -6.4002 | -56.423901 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e731689-429f-36ea-99fa-019dfe94e638 | -9.8448 | -44.8582 | 2026-10-02 01:12:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 78cfd535-885e-3770-bece-bf99b17a9633 | -7.835 | -55.133801 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0078720f-c71b-30f5-a873-588793ff35dc | -3.0433 | -53.882702 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a433bac6-d846-366f-8d92-89fe7d9395a8 | -6.3414 | -55.3242 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c454eacd-6750-375e-9f68-f57d6eeaf5fc | -12.8009 | -51.4216 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3dee3850-15c3-37a0-ab42-dd5a3126e138 | -11.4823 | -43.440399 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f31e015-78cd-3eaa-9988-326c4ae87398 | -4.257 | -50.754101 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8bf417f-6ce5-32f9-9a72-c3728f7dc634 | -6.0657 | -57.618198 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3b91b16-afff-34e5-9224-a2f5c428d7a0 | -6.3448 | -55.338902 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a481515d-45c4-33e8-b88d-f2342580226f | -6.1678 | -57.703602 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0330f3-daae-33f9-aecb-db946eb0d751 | -13.0426 | -51.310001 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cabb82ab-6610-3209-b3a2-97f006d38ad9 | -3.0255 | -53.9827 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dce12bc-b5a4-3012-84f3-8527c63d0f11 | -6.1976 | -55.548901 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d54f3730-9330-31cf-bc7b-edf2227626c9 | -6.8546 | -59.282501 | 2026-10-02 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb2040eb-d06b-38c5-97a1-f7448a46b3df | -9.957 | -54.670799 | 2026-10-02 01:12:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d3bdc6f-370a-3255-8fd3-dbc8aaea178e | -7.7317 | -54.8241 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55879186-f2ae-3a18-aeb6-cf17a6c569c1 | 0.6236 | -54.408798 | 2026-10-02 01:12:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5d07cb0-807d-3330-96a3-16f0f6940fbb | -3.6873 | -55.492401 | 2026-10-02 01:12:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aafb0c5-e2db-3ef8-b8aa-d1ecaefe19f1 | -4.3093 | -50.800301 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70baa662-e2c3-3ecd-b457-4821c52eb559 | -6.2423 | -57.7593 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7ee1bcf-cd10-328a-ba19-3b954725b952 | -8.1817 | -54.805801 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba6deba4-dd17-3035-8c75-4dd29fe1b4d2 | -7.2833 | -55.6021 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 699c6103-0514-3a8a-8c36-2eb5b2f51d82 | -7.0594 | -55.616001 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ac7047d-79fa-329a-a23b-3acd4c91f3b9 | -12.5389 | -43.097698 | 2026-10-02 01:12:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f7e0e1da-234f-3342-bf06-823c1b10fcdf | -7.3222 | -55.237 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 643616c8-43d4-3693-9820-f761f5f078b3 | -7.7478 | -54.804699 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f912191a-c3e1-3ef9-9126-e664a136f302 | 1.7965 | -55.621899 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae619c51-55f2-354d-affd-b916f46fa585 | -4.1971 | -54.5826 | 2026-10-02 01:12:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf126f43-74cd-3208-9379-c0cc3df7d313 | -6.761 | -55.087898 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37c8f70b-95b6-33a4-a16b-030ae47b3db0 | -6.5043 | -55.892601 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af8e184f-2b04-3fe4-8722-b00c7578214d | -5.9947 | -53.540798 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b5ba287-78c6-3771-80cb-4697059a8a67 | -7.7496 | -54.812199 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8c3bfde-818d-3132-9fad-68c326b63662 | -6.3431 | -55.3316 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02866465-6466-30a7-ade1-c5687c8b0a3d | -3.8534 | -55.8074 | 2026-10-02 01:12:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bc917d4-9a36-3141-9970-247f6dda88ff | -3.1765 | -54.0993 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2639f9a0-718d-301b-99bc-fd23fc22b53c | -11.7387 | -43.437901 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f85d572-dcd5-395d-9a46-be19caabdf5f | -3.2802 | -53.838001 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40fce0fe-16a4-3a82-8d40-aefa27323eea | -11.4635 | -43.409801 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09e03454-3481-397a-bfd6-dcbb4ca6dcac | -9.0724 | -49.886002 | 2026-10-02 01:12:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1144d5a7-0f70-32cc-a490-c53e2dd3d953 | -10.7889 | -53.769501 | 2026-10-02 01:12:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6a260ec-e178-3762-8c6a-b30db434e57d | -6.8738 | -57.726398 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7e0051f-e9b4-3fe6-9d7f-6ac134d558b3 | -2.4612 | -56.076302 | 2026-10-02 01:12:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99740079-3791-302d-b687-e20aab970467 | -5.0063 | -56.285599 | 2026-10-02 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1c081ae-250f-3651-9036-aefc7ac0d743 | -5.9836 | -55.383202 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff2caa2-ac7f-30d6-93ef-8aa84042248e | -7.3972 | -55.2043 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b09ff32-ebea-3978-a60e-1bfc98a9e1ee | -4.2604 | -50.768002 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e6d9f8a-12e5-3006-889e-a23fd3021476 | -5.904 | -53.505901 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9462b763-12a5-3178-914e-989ced747432 | -7.6866 | -54.763802 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86d5d8b1-a9a1-3d58-9aba-45719813f3e3 | -2.0552 | -56.8633 | 2026-10-02 01:12:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e8b5203-cade-3409-9139-ff30e05330ea | -3.0213 | -53.9646 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9fe5e15-ca53-30c0-8614-1cee7fe5b3f6 | -5.9019 | -53.497002 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95d26d79-bb36-3c0d-ae98-ceee6b8b64b7 | -9.5167 | -45.3615 | 2026-10-02 01:12:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 36f4b22d-054d-3013-a651-79192c531d74 | -11.6981 | -43.624699 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 844167f9-7a5a-3a9a-a61f-ea1812201a9b | -6.0257 | -55.342602 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f126780f-fad6-3ad1-94bf-2b32c33ac73d | -4.6879 | -55.8022 | 2026-10-02 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b788a1d6-b417-35f0-9d5d-8650a82c2455 | -7.4979 | -54.972198 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 621310e2-461c-3695-b067-d0f54506a98c | -7.5783 | -55.1395 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56836956-3217-3d18-a5ef-4e2be9733d93 | -7.8367 | -55.141102 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34f9fc23-612f-3c0f-9c82-5ac5e988ae3a | -5.8466 | -53.4818 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeb8320a-f6c8-39d9-966d-935ffbff2b59 | -7.7594 | -54.809898 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 129165ea-2174-3b4c-b5a0-4587118f0cd6 | -11.4756 | -47.478802 | 2026-10-02 01:12:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86f377e6-a39c-3ee4-b4c0-6047a561297e | -7.5014 | -54.987 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef8ad04-aa64-389e-981e-8b9c62ac63df | -8.5367 | -54.557899 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a48ff439-584b-39cd-bf30-45d6a30853af | -5.9721 | -55.378101 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd5df46e-e92c-339e-8a3f-be474e223692 | -8.2518 | -54.663898 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f80d814-fbf1-338d-9d7a-5abaf9f7358b | -7.7363 | -54.7995 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f3e512b-2243-3caa-883e-c82e99f76fbf | -10.4167 | -53.768101 | 2026-10-02 01:12:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
