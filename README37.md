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
| abe7ec28-6f48-33df-9322-2c846aa791d5 | -3.93317 | -46.71499 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ab11c18-7e7c-3b0e-bd68-fe8853177330 | -5.70089 | -50.13491 | 2024-12-02 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af55bf63-6749-3cd2-8fa1-89eafa9f2c40 | -5.58173 | -45.20578 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22f46ee8-1360-3b9f-b0bd-ba95761cdc7b | -3.25226 | -53.62011 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4cf8c865-0448-3b3f-80c3-af9a0b9e9963 | -3.2369 | -50.65379 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46e16737-f060-3d0f-8ce4-aa60608f9670 | -3.93311 | -47.98281 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca48bf8b-15d8-330d-86f7-6e0e4a48caa6 | -3.60915 | -51.42523 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed4b42f7-7d97-318a-8c44-ecd219e856d7 | -2.85172 | -54.061 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c44d601-8bf3-394c-879f-2cfe53678725 | -4.00317 | -46.93295 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4397c2b8-842f-3914-a7e3-ab0e30f60707 | -4.91305 | -41.33986 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| ea934485-b3bd-3019-9ec3-2d49227cd2a5 | -3.27081 | -50.21201 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c31e3c97-f538-34a3-911d-814347371dbb | -3.74516 | -53.3917 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c00c0b67-b92d-3ba6-b20d-4e9ce9431e85 | -5.58452 | -45.20981 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b530763f-8ef1-3e42-86d3-e85428b95989 | -4.10887 | -46.11634 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a91f0cd0-54d5-34f3-bead-63892ed34e25 | -3.979 | -46.75127 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8448034e-4257-360b-9dad-589d429549b5 | -3.07168 | -50.98775 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f72d00ca-6cf3-3b74-b2b6-f1de17a52718 | -3.66191 | -50.44033 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 879ccda2-91a1-346a-9b84-3b7cc8f7861a | -3.46557 | -50.26867 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d9d4217-78ec-3856-8441-860b1dd53e64 | -3.26944 | -53.64039 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cc38aef-14fb-311e-bc3c-5c766d979974 | -3.89408 | -46.67994 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd80ed28-a9e0-352b-b961-b7309f350ac3 | -3.58583 | -52.05476 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7019229-f90a-3ff8-b5bf-74beac2df9d7 | -5.64875 | -51.46946 | 2024-12-02 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca6f9b43-5ad7-3782-8133-61539bed3ce3 | -3.82852 | -46.5611 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89fdc59a-5339-35c3-a8f4-c4517f5e8f01 | -2.99471 | -51.3316 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61a22a0f-54a8-341a-a637-89e00a25b00d | -3.96455 | -52.17767 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2bca9fdf-0c89-3c96-bab2-e08452a03340 | -4.05254 | -46.99191 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aed11450-9996-3588-a334-f392449adbb9 | -4.13585 | -44.8275 | 2024-12-02 04:25:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e74d5a2f-035a-3b0c-ab61-d6bab1f4ccf1 | -7.88416 | -35.13894 | 2024-12-02 04:25:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 62fab245-0af2-3c26-8a7e-878d2b15a569 | -3.10258 | -53.749 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39d924bf-7e3b-3014-bbe8-45d282f1368a | -4.19535 | -50.68517 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 701ef444-5f85-367c-91a1-21832e821dac | -3.39142 | -51.14715 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 606c59f7-2101-3264-a562-7dcd8a7f5912 | -3.10604 | -49.50723 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 192c6a7d-4164-30cc-9aa4-71c4cff8d85d | -3.80056 | -46.69363 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beb77f0c-fb35-3de0-9130-587e8610662c | -5.60958 | -46.36343 | 2024-12-02 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 569550d9-7e9d-34af-a523-1f5add67b75c | 2.44345 | -51.21223 | 2024-12-02 04:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b74722c-3964-3d30-92e1-a9e4a04a44b4 | -3.02911 | -51.01211 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f9ba3b3-a26b-3a5d-85ff-126f7948f786 | -3.33868 | -53.38055 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 844ab667-f4aa-3790-b8c8-e32563728b3b | -3.26288 | -50.21074 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8aa90b11-5130-311a-9ad7-df96dcf5033b | -3.26447 | -53.63942 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6f71071-9839-3a68-b3ef-0205b9f90d12 | -3.68512 | -51.69957 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 933a8a62-c6b8-35f3-84a8-e64d22dd6445 | -3.64978 | -51.12473 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 646e80ab-9ce2-3bf9-91c0-6785c0d1cf4b | -4.52807 | -45.73561 | 2024-12-02 04:25:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09f37a7b-ad73-3c88-9575-d0185bf7a7a3 | -4.58278 | -48.02694 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df07488a-3a77-3d75-b38a-a4bec9bd40d8 | -3.95113 | -46.00257 | 2024-12-02 04:25:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76dc5db1-cb80-3178-979c-7083e0fd365c | -7.88478 | -35.13417 | 2024-12-02 04:25:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c6e583fa-0c97-304b-ac2f-99b127e990aa | -3.0285 | -51.53991 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| df97d795-b94d-36b4-8f34-63a5d79b5aa5 | -4.59135 | -50.60424 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13acb0ef-13c8-34ef-aa9e-1b5d9bee5a20 | -4.08508 | -46.13747 | 2024-12-02 04:25:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 101dc373-caef-3464-a2fc-9666c489019c | -4.0386 | -46.86187 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f90e2b59-c2f9-3499-8b3c-02c5d325dc77 | -4.91387 | -41.33447 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 109e493c-bbc6-3f6d-8488-c915953fff0d | -4.19188 | -50.68104 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 24b89034-6fcb-3f23-9bfc-988c340b1777 | -9.75971 | -41.98234 | 2024-12-02 04:25:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0dd1135f-5ae3-37d7-a105-e87c9a3359c5 | -5.61489 | -43.4738 | 2024-12-02 04:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c428197-41d4-31e0-9a6e-0063197b9557 | -4.06636 | -51.06296 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d472803-e243-30e7-a8da-30e2d53474f2 | -5.60813 | -45.05844 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f0a7e8e-cf8a-399c-bd4a-f79ea0e1aa39 | -3.82963 | -46.61886 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 770de723-8d00-397a-8e35-2b89e4692532 | -3.77111 | -46.69649 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf162c38-b999-3502-8886-19702e5b1ea5 | -2.98808 | -53.88744 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 895ceddc-af85-3297-8a48-58d2551f49d1 | -2.89354 | -54.16418 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 153d830c-ab79-3ad9-ab87-8a377bd3efc5 | -3.93154 | -50.9818 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b7fb846-e888-3ca2-846d-d7ef31165add | -4.5738 | -43.35593 | 2024-12-02 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3500e69d-61ac-3cdf-b27a-be100d6dda18 | -4.20734 | -46.37369 | 2024-12-02 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4d9eb9c-9bef-3dfb-a14b-69d18a625b96 | -3.55348 | -51.45415 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 910ae147-5d77-3ca2-a396-f07b23cd0a6a | -3.66275 | -50.43515 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0b75705-091c-354a-a79b-c3e9f963d3e3 | -3.42582 | -52.10859 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37243553-bbd3-36bb-89f6-07f4e9e167ee | -4.2956 | -48.21627 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36b88a77-5424-34b4-b24e-bff0f4d33343 | -3.81554 | -50.95169 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6fb292c-a5ca-38c1-9aa8-73b0e1251ab0 | -3.85788 | -50.89843 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcc4ab4f-e1fa-3852-9f2b-7c0c24f78728 | -4.20999 | -48.12304 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9b34f2b-75f2-3f1e-a80d-233984f1397a | -2.81547 | -53.96066 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e25c533-a5eb-3bb2-8486-6a22fe5682de | -10.65162 | -44.4967 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 150ee41f-4b39-399c-be3d-9bad7dd923c4 | -2.62437 | -53.36389 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2e2f6c7a-9a2d-3df1-955a-20ae028d9284 | -3.2575 | -49.90001 | 2024-12-02 04:25:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88af479b-333e-3f8f-8799-f5377a7763a8 | -3.98961 | -49.87538 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f925d77-453f-3333-83e4-ae9f3bcae7ba | -3.67764 | -50.24411 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 970bea61-da7a-3444-aff7-aa926b9d720d | -2.74159 | -51.75175 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15890469-aa58-3b4b-98fb-449e5ac40fa0 | -3.70591 | -50.60549 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66f27b0b-c5cd-368f-9b22-d4ad84f23e05 | -4.54995 | -43.30046 | 2024-12-02 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da90357c-9cf8-3444-9bd1-8f708d51b766 | -4.06772 | -46.67816 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb5c16f4-9ec0-3c7c-ba69-f5f169ded4ed | -3.76485 | -46.51895 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd435d64-b0b6-3d7e-b900-58a5efcd1f93 | -3.94475 | -48.179 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ea049a9-b5cb-300a-9dbb-72cf68a91e6b | -3.53954 | -51.50023 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a65ddfd-aa36-3f76-940f-336c0fe77646 | -3.93486 | -46.40263 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0927f9d7-9d97-3107-8011-1c109b19fbb2 | -3.18059 | -54.33949 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f4f10bd-eb5b-336d-bedb-cc51536f1c97 | -3.11392 | -53.80591 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5f96c34-cc69-36bd-9f02-7d4bb9d52296 | -4.50485 | -42.07042 | 2024-12-02 04:25:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 25f053ec-9b57-3ccc-8710-f2a36f1ec11f | -3.33625 | -53.54478 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08e272fd-ed86-3782-a9af-3e772ecc2912 | -3.02491 | -51.01146 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 510be300-bfb9-3f08-a111-2a34dd8e827d | -3.19888 | -48.5765 | 2024-12-02 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe1f800d-9cd9-3a8b-9387-8f12a2ee28aa | -5.19873 | -43.86922 | 2024-12-02 04:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e07beee-3dbd-30b5-ab41-9e1515d1bba6 | -3.12927 | -54.52604 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74982160-df06-33dd-8b53-581723c71f2d | -2.97836 | -53.88284 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28b474c4-e374-3d13-a482-b75f05d83a44 | -4.33038 | -48.09418 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d43e0ab6-c118-332e-a2d2-44c275b8287e | -3.88747 | -46.40532 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccc258b2-6f63-3ad0-9527-6b2f91e078c8 | -4.31169 | -48.0919 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb71750b-9b86-384e-8289-49dbde3ef596 | -2.88024 | -53.331 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac8a837f-1221-307a-b921-56cd03929323 | -3.85418 | -46.52908 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c008691-8dcc-31a6-a64c-7a84a8b8fd6b | -6.86808 | -47.23989 | 2024-12-02 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3a790964-179a-3260-a781-9afa126203e1 | -3.2541 | -53.92521 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0479a3e5-ecb4-3bd1-a492-95e8c93c1d71 | -3.52606 | -50.76714 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README38.md)
