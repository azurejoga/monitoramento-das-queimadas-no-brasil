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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96d3ae75-66f1-3ea6-9b67-2caca8060947 | -5.87455 | -53.64579 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a5f539b-b3ef-3248-83b0-7e328f5b91a8 | -4.42973 | -55.34893 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c7ebba3-6c7d-3356-8539-c0f36b07376f | -1.93889 | -56.5968 | 2026-09-22 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9375b0fe-fc85-3239-9449-d8edcb0f8f82 | -6.38048 | -60.01499 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4c8dd0e-7da6-3a30-87bb-39f03a06b844 | -2.53005 | -59.55207 | 2026-09-22 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6d2ef86-4097-379a-9147-e1d600a7ba67 | -4.43313 | -55.34947 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 518ef731-e133-3bf6-b935-3734448f266f | -6.13581 | -59.96503 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8512525d-f687-3634-99e1-0f6222035a20 | -2.40735 | -58.28061 | 2026-09-22 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0bf2ec60-2680-39ae-ae86-b6d1a5b84bfd | -2.60411 | -59.76351 | 2026-09-22 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a60a09f7-7c21-33c6-94c6-0f221c6bf9ce | -6.44799 | -59.97694 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d3fdd6b2-a25d-3e95-a503-32fc2cf908f3 | -7.24567 | -55.584 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a8a6e52-2c42-3587-9e9c-87023b82c828 | -11.32301 | -54.04568 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a74caae4-c871-31a5-9999-86c9b1087c35 | -3.04061 | -57.41815 | 2026-09-22 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a694149e-9101-39b7-97a3-88aaa7774c9a | -6.58049 | -44.15235 | 2026-09-22 05:23:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 053213fe-b50e-3077-9cb9-8f8c5142c9d5 | -5.74878 | -45.08749 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4f6014ec-0202-3b5a-8b25-6f898df386ba | -5.45607 | -60.1459 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3046ce6-e8f4-3f2e-8fb6-f3b006bfdf08 | -2.50976 | -56.60541 | 2026-09-22 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 619fb514-b2d3-38fb-8161-0cafe338b368 | -6.17259 | -52.81021 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b527b66-6ce6-371a-8543-0a0db60d8652 | -5.8096 | -57.72805 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba466de7-6fbb-3d17-88c0-5ad61108b251 | -4.53753 | -54.90871 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9c8ae3e-5e0f-3b17-ac12-5781c1445eb2 | -3.68283 | -60.63166 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88f8b10a-dd40-3ac7-bbdb-ca6a69fa7d84 | -12.14042 | -61.16259 | 2026-09-22 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d4d781e-0403-3e79-8943-4bd628722056 | -10.54137 | -57.44318 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff4faebc-4cab-36c3-a003-3d3540eb09c3 | -3.47224 | -59.55563 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bebada3-b75b-3260-a3a2-a9691b0f605a | -3.46867 | -59.55504 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f62de98-720c-3b74-8727-597e71641023 | -6.11609 | -57.75562 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 712dbd92-0f1e-3413-9112-c15d15b43089 | -6.71331 | -59.45358 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eba7e1f6-2309-39be-b6db-842075ffdade | -10.52332 | -56.78882 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ece372c4-4e5e-304e-992c-47fd21ed4fe5 | -14.76829 | -48.4501 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74661dff-b9a6-3db2-92b3-62e16a736308 | -5.94159 | -59.98388 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 354434fa-cd46-3395-bee9-5ecce2757139 | -5.4882 | -60.13012 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 475c9594-b1dd-36a4-bc9b-ba8a674daca6 | -6.01394 | -47.9044 | 2026-09-22 05:23:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4187ff56-d6d9-3228-bd8e-3074df51a7e8 | -5.83837 | -53.47879 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e8edc29-22eb-3024-b13f-cd0f2d488c4a | -7.58812 | -57.68692 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18938592-60ca-3f0c-915f-81bcb87c8939 | -6.00896 | -47.9029 | 2026-09-22 05:23:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f711351-4f32-3c3e-9b00-8233f6b1409a | -6.06717 | -57.86943 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b58e0f1-8173-354e-9934-bd2995148fbb | -6.22703 | -56.04121 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fdb5512-3738-3d09-a24a-3a67d9e71c03 | -3.47558 | -59.59239 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06564927-c0a6-3340-83ac-863df0324e9e | -3.414 | -60.19728 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f34b2e48-bd25-391d-8994-15fb167f8e75 | -4.97181 | -55.83327 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b1fbf62-12d5-3bae-b966-f590db4a4d0f | -1.99474 | -56.54541 | 2026-09-22 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02dcac9d-3837-393e-a98c-2f13c817ddd7 | -2.88373 | -54.08067 | 2026-09-22 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84c01290-1edf-3371-b824-f4c289c13815 | -3.46246 | -59.52508 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e7e20c2-799d-32d2-8e91-4fc631b76038 | -3.29499 | -57.85965 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0cccd065-847d-3eef-a20d-965430c3d940 | -5.99678 | -57.71889 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17e467d8-16ac-39e8-ba3b-54ce2493a779 | -4.08857 | -62.08776 | 2026-09-22 05:23:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed29dcb8-1af8-3d26-9176-aef568f4d2b0 | -6.30951 | -59.94368 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcb59e5f-1a49-35ad-a56d-7f40406a4833 | -3.47188 | -59.53486 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3e1eda4-97b2-3573-a69a-119b06e514bc | -8.17552 | -54.81809 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b52d688-e7e8-3a7b-b8e4-ea3893e2f4f3 | -4.38882 | -55.03056 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5c6941c-e533-3fba-a21f-d67c2b8c0290 | -5.88423 | -51.57939 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6e68afd-4e1b-37b3-ba9d-a40ce4f95254 | -14.04432 | -52.05672 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 200fc330-95e9-3cfc-b6f7-454b74084605 | -13.51631 | -51.52077 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 4724e116-ef04-350e-b0bb-6f38260a6e15 | -8.79705 | -44.2858 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ad1485ec-ee0e-3bcc-abf6-e0efa1abe2c4 | -6.52188 | -58.30559 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d4c4b42-05d6-379a-be78-513e83539175 | -6.84114 | -58.98838 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 188d8670-84a1-3d49-9e8a-43dc9b582ea2 | -6.55223 | -56.03543 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d068257c-885a-331e-ae67-9e50dea470cc | -6.74312 | -59.07394 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d19bc374-378f-3cd7-bbfc-9c28064c2c0c | -4.18277 | -51.24735 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3725f95c-98b2-3986-b082-8564508c4af4 | -6.70358 | -59.96024 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b3fa2427-ff6f-3b12-8818-5cd977bbaabb | -6.76008 | -55.61871 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1addd80-104d-3e0b-b0f4-fdfe84b2d1ea | -4.07836 | -56.22786 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8770ecbe-d16b-33a3-87a1-c839989b362c | -8.14924 | -54.79735 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e64ba8ae-a47b-3b15-a8b1-bd315d5d7e61 | -1.32628 | -54.66405 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15ef3c83-20f8-33f5-9a92-24a41299adbe | -6.08168 | -57.693 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eddc8ebf-14de-3fb6-baa5-6c546ea068a9 | -6.62849 | -59.93247 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 62315683-1552-3f90-8851-dd6648258e97 | -3.83104 | -57.1685 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7d8ca27-1384-3b3a-9d58-1172e305680f | -3.38292 | -56.94147 | 2026-09-22 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8f6fb9c-1d9d-3dc5-bc5d-0227655a0f87 | -1.7786 | -54.78393 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad575393-f12c-3f98-b116-b3ea1a521019 | -12.40616 | -47.08327 | 2026-09-22 05:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d13a7e25-f694-3812-85c0-ad058dd15244 | -8.11436 | -49.58384 | 2026-09-22 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 480ea882-2eb3-35a4-84fa-4ce1a31c842e | -11.81099 | -58.17276 | 2026-09-22 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56dbf507-ec33-37da-b4cd-c0e9deda862a | -7.58811 | -57.6655 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df4ea45c-ec95-3e64-99c0-8a41f6a2e44e | -4.52524 | -54.9643 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 028be445-89a6-3349-8dfc-083848b0043a | -3.77997 | -60.74842 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ce3431f-231b-35e1-84b5-384ff817e7a5 | -8.79202 | -69.02706 | 2026-09-22 05:23:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46cee96f-9db2-3cae-a0cb-14a3fb5963be | -7.59753 | -57.67057 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c5996a2-010c-3c39-8fc4-c53aa1fdbe71 | -3.61249 | -60.56682 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d69116bc-f876-3fd6-806e-94f29944ef44 | -3.45852 | -59.25535 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c990845-499c-3997-a20c-1096f47ff9ac | -3.4463 | -50.60464 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffe99a01-de0c-3685-a30c-bb1ef5fb0f4e | -2.93794 | -57.80339 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f6ddaeb-90ab-34ab-9e7a-85990f8fc1be | -6.725 | -55.07463 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2f55e4d-7c00-32ac-9b6b-a95ed2588e5e | -5.8755 | -52.12852 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b5aa1db-bbb1-3f5d-a461-6759e9dd3908 | -6.3169 | -59.9652 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fbc2c60-ca1d-329f-a6ed-8cb8cb31f02c | -13.86237 | -51.84764 | 2026-09-22 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a347e18-6965-3921-9986-4036f16e51a5 | -6.30739 | -57.74301 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fd44c1f-17d7-3d0c-97bd-f1d63c0232eb | -5.85916 | -49.77972 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0d1a932d-f38f-3d23-b432-127f9188bf5a | -13.92261 | -48.56698 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f4c0775-4725-391b-b2f6-4ec29e23d5c6 | -4.54575 | -54.9362 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ce26f82-1414-3e6c-bd9c-6a55af8ea6b4 | -5.21584 | -56.07441 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 459b140f-ebc5-33db-981a-2b0bae7fe4f9 | -4.77927 | -56.15129 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6385f48-731f-3be8-9925-3bb77602f693 | -6.6451 | -59.9191 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 735a869d-2698-337a-a5c9-57e8af00267a | -6.14916 | -57.84301 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a11acae-a045-389f-8192-0a37fbc79742 | -7.39791 | -55.21738 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a340052d-5677-39fb-8c84-ec58efa575c3 | -3.22758 | -53.95377 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ed6de76d-113c-37e5-b911-ced95c844010 | -9.5621 | -66.04041 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28505eda-c13c-3502-9f71-07b41b930146 | -6.09721 | -57.68119 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a0825d20-84eb-3b7f-b1e1-b2f5e91dfda5 | -3.72248 | -60.57777 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f0310821-6293-33f7-93b8-f01cff80d2c8 | -6.46147 | -59.98318 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3c4d946-496a-3854-befe-e2be54130e58 | -8.10178 | -55.35059 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README93.md)
