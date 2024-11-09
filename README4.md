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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05d5c55a-5783-31d4-8fa8-916a8eb46902 | -4.43607 | -48.06519 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 6066fc61-6d43-325b-9999-ef4b9aaeb280 | -2.15214 | -49.14052 | 2024-11-09 00:39:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 0097ad53-2a92-3be9-99e7-6911a0739054 | -2.92747 | -49.3517 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b89b0b6d-bb49-3afc-b963-ac939c206ccf | -3.41006 | -46.05534 | 2024-11-09 00:39:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b4fe416e-99a3-369a-ae0e-7b9c0fc073cb | -0.39483 | -51.95473 | 2024-11-09 00:39:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2535cc4f-9403-3869-8557-72ce32b4c7fa | -2.52724 | -46.19626 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 41a521a4-7750-3618-a756-3e657e53168a | -3.59215 | -47.36334 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 4d814ea7-86c5-3a16-927c-e0567867735d | -2.73155 | -51.72499 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 577ffb3e-a772-3d58-a4bf-6558368b1851 | -3.21814 | -50.39376 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 15d73b46-ece2-3db1-b9c3-a6dfb2d8fccb | -3.83167 | -46.50456 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3d93896b-fd72-391c-ae70-c9bd1010740e | -2.51585 | -46.38182 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f48f1636-3162-383c-a1ff-c99c34a7ddd6 | -3.59505 | -47.38415 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 03acd872-40d7-30f6-b07b-b52b25631ae8 | -3.6571 | -43.7247 | 2024-11-09 00:39:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bb8846d2-5094-35e5-b8a0-e9212e386808 | -2.86629 | -51.47924 | 2024-11-09 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 6e765589-40a5-3deb-8cf3-17de470b89c0 | -4.20268 | -50.62517 | 2024-11-09 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| b610be51-6f85-313f-bbb2-a1e3372a2679 | -3.52915 | -50.87616 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| a19fa28b-f922-3b71-b079-5298e75bb6d9 | -0.39356 | -51.94858 | 2024-11-09 00:39:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 03d75f0e-5912-3233-b24f-e65df35b93c5 | -4.74473 | -43.86125 | 2024-11-09 00:39:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 39db8827-7d67-3811-ba39-94944f0e8405 | -2.10544 | -46.21209 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8fc9b435-5f1d-3581-8c83-c64e4a87d4aa | -5.45438 | -43.27025 | 2024-11-09 00:39:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d7c5a6b0-c7f6-3d18-9abf-520decb3defc | -3.32472 | -49.90998 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| f024d1f1-f17c-318c-b7f3-f00f0544a26c | -3.75539 | -45.95468 | 2024-11-09 00:39:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 4461e647-8afb-35ad-a916-54eff4eb4b7d | -4.61037 | -49.57289 | 2024-11-09 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| fca326a2-5ac4-3693-b760-89bb01152e10 | -6.39329 | -39.71106 | 2024-11-09 00:39:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0556256b-ce61-31b2-8948-466109c22003 | -3.5988 | -47.34112 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 443.9 |
| 679ca1a2-7a1f-3bb6-bdea-afc67be59afc | -3.38275 | -52.3554 | 2024-11-09 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| e56c4605-1094-3555-abcb-69c6f50808b8 | -4.20441 | -48.5364 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| fe6dfaa6-013c-394d-a2bc-ab3706fa0424 | -3.59203 | -50.26796 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0abd603d-c2a8-3c7c-ae09-d42e31e9057e | -3.35192 | -50.11409 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9d73390f-86b2-3fd6-92dc-94f6fd4a6b11 | -0.91638 | -51.65987 | 2024-11-09 00:39:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3a2b02ce-3fc5-3d11-859e-ed2563714229 | -6.27751 | -44.53923 | 2024-11-09 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| f2783357-e337-3676-ac39-9110bc66149a | -3.35405 | -50.13006 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 24f5ab2f-92db-3cad-9c84-e9fda2da5345 | -3.27085 | -46.31237 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 2d998c38-7de3-3c2c-8967-47629fdabcc2 | -2.01648 | -48.01693 | 2024-11-09 00:39:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78d01b9c-5206-3757-aeb5-9278db442e6b | -3.10686 | -53.32379 | 2024-11-09 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b001426c-a636-3542-ae20-fe7049eb2451 | -2.82305 | -45.47249 | 2024-11-09 00:39:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 91f09043-e587-3ea8-a1f1-006db9d39094 | -4.5059 | -42.88484 | 2024-11-09 00:39:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8ebd19fd-7d18-36ef-b313-bf6088865279 | -4.61531 | -45.97952 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4ba70cec-8e87-3a6b-a7df-eb88ffa65bf5 | -3.23689 | -50.44263 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| dd8dcf31-04f1-3f57-9fb9-d7bcc4f39e3c | -4.21501 | -50.62337 | 2024-11-09 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 06b0ef6a-f638-3ca6-bbe3-960d61d0d12a | -2.5545 | -45.20522 | 2024-11-09 00:39:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8be8175c-ceae-38e7-b8dd-174c362483a6 | -6.42149 | -44.05556 | 2024-11-09 00:39:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d1ca68bb-9a1f-3898-bc14-814c67f192f5 | -3.036 | -50.31303 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| c0fc037f-f2ba-3021-a4c9-d7786cbdcd74 | -3.238 | -50.27321 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ad9fa5f6-3de4-318c-a232-c984b8b10fdd | -2.20141 | -48.38897 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8eff8b60-d805-3abb-ade1-e583d04e2716 | -2.56681 | -47.34219 | 2024-11-09 00:39:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| b14fcd5c-554c-3e27-93ad-fc204f8f0b62 | -4.43585 | -48.07084 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| fa3ac20c-b298-3e91-a6eb-7a091c367a11 | -5.18039 | -44.00474 | 2024-11-09 00:39:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 82b0c06f-23e7-3518-a811-187f3e311d00 | -0.22024 | -51.65049 | 2024-11-09 00:39:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 4d23b51e-989b-3ebf-aa9f-c21f8e5abe56 | -3.0338 | -50.29682 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 41f7e455-b39d-35da-9e05-14b11435aa75 | -3.26308 | -46.32298 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d7455869-176d-30a4-8714-dd8b68b94ea0 | -3.15037 | -52.97461 | 2024-11-09 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 680.3 |
| 8b6cef7e-02e3-30d7-9ba3-6fbea52424b2 | -1.69991 | -48.15674 | 2024-11-09 00:39:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5fd8940e-1d14-39bf-9c31-abc074d9b227 | -4.86802 | -45.67255 | 2024-11-09 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 24.3 |
| da632bbd-50f6-3eff-a0ef-6f1fa07da650 | 1.31217 | -50.73289 | 2024-11-09 00:39:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 48349e23-2b44-33f4-b7c0-f2224388e4c4 | -2.1067 | -46.22116 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| e7be9914-f977-36df-90a4-8ab0e95e6a1e | -5.68909 | -46.43506 | 2024-11-09 00:39:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 02158559-2b64-3151-ba2f-a239bfd988b8 | -4.61769 | -46.53668 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8b1db676-2132-3ce7-a24b-e8d0e64670ed | -1.51091 | -52.18856 | 2024-11-09 00:39:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| ef8d6fa5-8d56-3574-a731-f1553662e9b1 | -3.07004 | -50.56419 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| e6a4261a-e52d-3b4f-b0b1-5301f0135f7f | -6.19059 | -45.44849 | 2024-11-09 00:39:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 004d6a83-b404-3fcf-ae48-ebace512ccf3 | -5.44537 | -43.27152 | 2024-11-09 00:39:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 9294a298-dd31-3716-9c58-2cf1955cb20e | -3.97187 | -48.1828 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 289.5 |
| e1065d2c-e763-36c7-bc34-5bba86aa4862 | -2.8712 | -47.90414 | 2024-11-09 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b50d9cbb-6af8-3152-bf84-8d1764032fab | -3.49963 | -43.98722 | 2024-11-09 00:39:00 | TERRA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ea469a68-48cd-324b-bbfa-4f55755cd91b | -2.23539 | -46.61909 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 898a3adf-fcc2-3d8d-b949-1656558512ea | -2.11315 | -46.20175 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6267c5d1-e0bb-3224-aed7-fdd3e743d136 | -3.17622 | -46.62896 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ac530adc-5a4e-3a18-b752-282c4167064f | -2.36134 | -46.7976 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 48016252-d88d-3e94-853a-6606debe870b | -2.23995 | -48.37188 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3b0752da-4aec-36b5-87fe-a5f14bb571da | -4.19074 | -46.17349 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ebd1e153-91b9-3c12-b964-db658ea3ef57 | -5.62533 | -44.82516 | 2024-11-09 00:39:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5823b70b-3894-3e53-b626-4abc1f877b4e | -3.4299 | -45.26352 | 2024-11-09 00:39:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7622c8ff-61e3-32d3-9d55-868e1b781607 | -3.11711 | -50.14743 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| f244be2f-b679-33be-89d1-ab589750a8d3 | -4.20433 | -45.87037 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 74f2e288-ca02-36c9-822d-84a72d947865 | -5.39458 | -43.62777 | 2024-11-09 00:39:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bed0b482-f73f-3329-aabc-80e50f8e5b88 | -4.43429 | -48.05906 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| f348a390-92c3-302f-953c-f1c3084b59b9 | -2.67991 | -51.83999 | 2024-11-09 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 64657302-6ba1-3425-9611-fc9a0309dde6 | -3.35308 | -50.26778 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 4ed7e8ae-aba7-38f3-9fd5-37dc697fc661 | -3.58924 | -47.34241 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 825.7 |
| 59c36704-70fe-36c6-90a0-a10182681801 | -4.20734 | -46.69424 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| c8174ea2-3e82-3a1c-916d-6d6be0e31d41 | -2.83069 | -45.46239 | 2024-11-09 00:39:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 80800fa9-e45a-3045-88ca-a4fddec72def | -2.21119 | -47.78557 | 2024-11-09 00:39:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4d2fb083-7d0b-3bfb-8387-463957768d0d | -3.34079 | -50.35367 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 15457dd9-31d7-3c3c-bb62-1e66aeaa562e | -2.86729 | -49.15337 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d1b13b93-a0ae-3986-b7c1-754711a33da4 | -4.62827 | -46.54505 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 78e543df-4678-36a2-814c-427d5f79030b | -4.38309 | -48.57685 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 7be117e0-dd1f-3678-91cd-5e0c7257b8da | -2.51463 | -46.3069 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 11809045-18ae-3e50-ac79-1f5f57c0d046 | -3.59069 | -47.35283 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2052.0 |
| 17b885e1-9a45-3262-816f-2d490d4ce9f1 | -3.40232 | -46.06573 | 2024-11-09 00:39:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1cabdcd8-ca94-3e88-a8c0-a44781618f1b | -3.15773 | -54.48846 | 2024-11-09 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| fc8cbffa-2326-3278-a90a-d11b237305b2 | -2.91946 | -51.68076 | 2024-11-09 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 2a02cf03-9e08-38d0-889b-0e2d69ab888b | -3.07238 | -50.58146 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b3c020f0-ca5d-3511-9814-21e7a7ead66f | -2.37706 | -46.77605 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 30adf07a-cad8-3426-9458-fc592f4ca5ca | -2.91983 | -51.66592 | 2024-11-09 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f17c1013-3aba-3fbd-ba9d-8caf4010c911 | -3.14796 | -45.95576 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2788592c-10f8-3af8-80fa-a5dca6cefa06 | -3.58256 | -47.36452 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4be6a25b-8050-367f-b61a-411ad1ed794f | -2.0828 | -48.41776 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 5408ae6e-ac9a-36b0-8d8f-6f1d35f74f2b | -4.43712 | -43.63845 | 2024-11-09 00:39:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3f8e570f-5752-3285-8713-7826c357d9ce | -2.07564 | -48.51328 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README5.md)
