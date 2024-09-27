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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f30b719c-0462-3537-bc1c-0f9bc3009390 | -6.1183 | -50.973701 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d5ffdcb-5d43-381a-b23a-044515e9c369 | -6.1251 | -51.004501 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee3ce13b-bcb5-31cc-93c3-4e24ec5d7184 | -6.1102 | -50.983601 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f137dea-ed66-3967-bd67-6444aff557ee | -6.1119 | -50.991299 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5959238b-5401-3f85-86f7-4ddb985af5e6 | -6.1153 | -51.006699 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6108ca-e8f1-34ff-bc71-0de827c2f44f | -6.117 | -51.0144 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98856a64-9e45-3c54-83af-5e2a897165e3 | -6.1054 | -51.008801 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf83153e-3480-3417-aa20-df794591aae1 | -6.1071 | -51.016499 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 059a0ce7-6436-3763-a636-c5deef5f9e65 | -6.1277 | -51.1096 | 2024-09-27 00:35:50 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc9b53ed-a9f8-3780-a7c4-d97a4048b958 | -6.1294 | -51.117401 | 2024-09-27 00:35:50 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 676b601d-de30-35fd-bd84-b878a5dd3764 | -5.843 | -49.870998 | 2024-09-27 00:35:50 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5734ddc-6127-326f-8c9b-77bbfc80adc8 | -6.1161 | -51.104 | 2024-09-27 00:35:50 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 726fc827-6ff2-30f7-905d-f0fd0b643286 | -6.1179 | -51.111698 | 2024-09-27 00:35:50 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b0ebcba-17ae-36db-8550-733e73544a41 | -6.1196 | -51.119499 | 2024-09-27 00:35:50 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d56fb08c-af57-3837-b79b-95f841046830 | -5.369 | -47.809101 | 2024-09-27 00:35:50 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 732d3d15-2c1c-3cef-a408-b72cceb4c128 | -6.0926 | -51.043999 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8810ee-eca6-3096-aca6-9f18e5a74666 | -6.0944 | -51.0518 | 2024-09-27 00:35:50 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40b8b919-1b00-3da7-a25e-b7444cdc3215 | -6.0995 | -51.075001 | 2024-09-27 00:35:50 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 376b28cc-207e-327d-89fa-4aeadabc8885 | -6.1063 | -51.106098 | 2024-09-27 00:35:50 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61790e7b-9a0c-369b-b9bd-5d8c2a1e9567 | -6.1081 | -51.113899 | 2024-09-27 00:35:50 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee5f83cb-d572-3038-aaad-57301496bb07 | -7.77 | -61.2015 | 2024-09-27 00:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| b4a79add-6986-386c-aab6-864d905d61be | -7.7701 | -61.1825 | 2024-09-27 00:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.0 |
| abbdb839-9970-3e27-aba6-6ccf96e7300f | -7.8156 | -54.7252 | 2024-09-27 00:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 185c71e6-416c-3246-8357-709c77a8c9fe | -7.7885 | -61.2008 | 2024-09-27 00:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 4a1b8b35-b1aa-39de-b4c1-5b4a5f371481 | -7.7886 | -61.1817 | 2024-09-27 00:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 6eaa9849-fda0-3147-85b2-4d2618bf3f5e | -5.3573 | -47.848301 | 2024-09-27 00:35:51 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80b1165d-361c-379a-999c-244e4354230b | -5.6151 | -49.082199 | 2024-09-27 00:35:51 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d703cc2-534e-3778-8c39-e093c03175fb | -5.6166 | -49.089001 | 2024-09-27 00:35:51 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9e67e4e-aa9a-38b2-ac4d-6f6e1afe7530 | -5.6274 | -49.137199 | 2024-09-27 00:35:51 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77d54dbd-1e2f-3fb7-a2d6-98d185d97829 | -5.629 | -49.144001 | 2024-09-27 00:35:51 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b678491-a1fa-3d7e-b105-1008ce939af0 | -5.6305 | -49.150902 | 2024-09-27 00:35:51 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66af9d86-b020-3293-b1ee-aaa54c5b4883 | -5.7798 | -49.818298 | 2024-09-27 00:35:51 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f037261-a24b-3b4d-b670-cec2cbf728fb | -5.7813 | -49.825401 | 2024-09-27 00:35:51 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38ea4b32-96de-3ca9-ad72-0acb35eda20e | -5.7829 | -49.832401 | 2024-09-27 00:35:51 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c21ca4f1-a0c2-3387-850c-325d47877219 | -5.6192 | -49.146198 | 2024-09-27 00:35:51 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd98e2fa-3dc8-3369-b381-c32b9260cf73 | -5.6207 | -49.153099 | 2024-09-27 00:35:51 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96db09bb-6413-3417-9d0d-d41f9687d029 | -7.9081 | -62.9976 | 2024-09-27 00:35:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 9e016056-bad9-3015-af1d-4833f8ee455a | -7.9082 | -62.9787 | 2024-09-27 00:35:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 78a40213-02e2-34d0-8e89-9f8d5e9904ec | -7.9174 | -61.2909 | 2024-09-27 00:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| e7de72fb-bdc2-3ab8-9961-d91204704d7f | -7.9175 | -61.2718 | 2024-09-27 00:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 344f98a3-220c-3a9f-9539-9abd8e290a36 | -5.5558 | -49.001598 | 2024-09-27 00:35:52 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eae8bbc0-a18c-3b01-bd61-d3b99e206e63 | -8.3153 | -55.0157 | 2024-09-27 00:35:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 3fd7a4cd-858c-391b-a8eb-8260ca96ee90 | -8.3155 | -54.9956 | 2024-09-27 00:35:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 44c40e91-c35b-303d-92da-033f13dc0348 | -8.556 | -49.6112 | 2024-09-27 00:35:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| baab187e-e97c-36e1-a064-04b624d92313 | -8.5562 | -49.5897 | 2024-09-27 00:35:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e20f4f80-f742-37e1-b3e4-9f898c04dc8e | -8.5748 | -49.6095 | 2024-09-27 00:35:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 8a9e33c6-66f5-36f9-949f-547397f38bdd | -4.0347 | -43.229301 | 2024-09-27 00:35:55 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78372dbe-4c65-39d1-9119-5c05698cc0a4 | -4.0249 | -43.231499 | 2024-09-27 00:35:55 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36e14ddc-a3de-33eb-908c-7b0f22ee4196 | -4.0276 | -43.243301 | 2024-09-27 00:35:55 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e17a2823-e029-3a95-8292-a5e68586a4a5 | -4.6105 | -45.753399 | 2024-09-27 00:35:55 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1145610c-114c-3307-8cf0-32cf4ef2a87b | -4.6124 | -45.7617 | 2024-09-27 00:35:55 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d44d941e-49d0-3a1e-9786-547b426baed9 | -5.241 | -48.518299 | 2024-09-27 00:35:55 | METOP-B | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 881ff932-16f8-3f63-beda-b59a16e12ead | -5.2425 | -48.5252 | 2024-09-27 00:35:55 | METOP-B | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5aecbb02-ea34-3694-87fa-ef8cc755d99a | -5.2312 | -48.5205 | 2024-09-27 00:35:55 | METOP-B | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5e5780c7-a9ae-343d-8669-1ef3594f9041 | -5.2892 | -48.8237 | 2024-09-27 00:35:55 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e9c6f53-2495-38ad-8fad-c60c4353efa8 | -5.2794 | -48.825901 | 2024-09-27 00:35:55 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3a21aa3-c806-38de-9970-c144915b606b | -5.281 | -48.832699 | 2024-09-27 00:35:55 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8197b8b-cbea-3628-b7bd-338421b15be1 | -5.2561 | -48.859798 | 2024-09-27 00:35:56 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0445418-23d3-38ca-a721-d0636139b91d | -5.2576 | -48.8666 | 2024-09-27 00:35:56 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd7040d-f406-33cd-a62f-74b4e2195d9a | -5.2592 | -48.873501 | 2024-09-27 00:35:56 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e1476b8-172b-33f9-8ed5-da896674beda | -5.2478 | -48.868801 | 2024-09-27 00:35:56 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f94c491-e82e-3144-aebd-e06d7a46e3ce | -5.2494 | -48.875599 | 2024-09-27 00:35:56 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6926f5d7-8e6d-392d-a9d8-df78972f91d6 | -5.2509 | -48.8825 | 2024-09-27 00:35:56 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f16a6763-3451-3744-8b2c-c2e0a8b8f1b8 | -5.2138 | -48.8549 | 2024-09-27 00:35:57 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf68ac00-80d9-38ca-937f-611115350df7 | -5.2153 | -48.861698 | 2024-09-27 00:35:57 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2985e1c7-0ae3-34f0-a57f-e1a291104563 | -5.2044 | -48.950298 | 2024-09-27 00:35:57 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3517259d-b8d7-395e-91f0-2c89ac042c96 | -5.1915 | -48.938801 | 2024-09-27 00:35:57 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e13e495-d024-3eb2-a730-dba6c7c408d7 | -5.1931 | -48.945702 | 2024-09-27 00:35:57 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc1f8c5a-af74-32c8-bb69-db6b81e8bba4 | -5.2562 | -49.226799 | 2024-09-27 00:35:57 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69c58133-1e85-3f22-a90e-de8079697122 | -8.9978 | -67.3724 | 2024-09-27 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 0daf9c82-5a99-3258-abb7-4cfb28af1020 | -8.9978 | -67.3538 | 2024-09-27 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 86f0cda7-8132-3927-a3c3-a12ecc5f9b01 | -9.0163 | -67.3719 | 2024-09-27 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 351fb872-73fe-3055-a42e-8355e25ccd2f | -9.0163 | -67.3534 | 2024-09-27 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 58f3c393-8730-3aec-8db2-14390aa0defe | -9.0656 | -61.3934 | 2024-09-27 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8a0ae8f7-788f-3567-acb1-d92625f0b13b | -9.0657 | -61.3743 | 2024-09-27 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0cf49b26-6e58-3bc8-9c77-e4057ed7a82b | -9.1255 | -67.8877 | 2024-09-27 00:35:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4a06427e-4a73-3ff2-898d-6af1bfbb3763 | -4.478 | -46.297901 | 2024-09-27 00:35:59 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fed84c3f-6d96-33bb-9d38-8627f8b135b6 | -4.4798 | -46.305698 | 2024-09-27 00:35:59 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7db921f0-21c8-3295-9377-f83f6cafdc68 | -4.4816 | -46.313499 | 2024-09-27 00:35:59 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce8a50a6-9669-34ce-b802-6d2a474e3506 | -5.1668 | -49.470901 | 2024-09-27 00:36:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee6e43ff-a761-3b03-b5c6-4aa1cb9aded4 | -5.1683 | -49.477798 | 2024-09-27 00:36:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92acd5a2-b75d-3de1-bf7e-d3920db93989 | -9.5829 | -50.137 | 2024-09-27 00:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d368ab15-1c31-3865-9f8b-628b172846c9 | -9.6018 | -50.1352 | 2024-09-27 00:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 009bf141-1c51-364b-969e-07057dc0a36b | -5.3109 | -50.438801 | 2024-09-27 00:36:01 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c24ad71-dedf-35ba-a1b5-12fc9cc2d534 | -5.012 | -49.7453 | 2024-09-27 00:36:03 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27efbc11-7fe9-3ad4-8773-021e4ee33cb5 | -4.5551 | -47.991699 | 2024-09-27 00:36:04 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cc9ea68-f85e-3e2f-8bb7-747275f11d0f | -4.5567 | -47.9986 | 2024-09-27 00:36:04 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83620d07-0afe-31fc-b9b5-484c492a629f | -4.5583 | -48.0056 | 2024-09-27 00:36:04 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86b207f0-b098-3290-bdcd-dd4ec514ea90 | -4.7472 | -48.887001 | 2024-09-27 00:36:04 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa76b3a-46b8-3c94-9f12-81fb582f7f8f | -4.7487 | -48.893799 | 2024-09-27 00:36:04 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a448c51-be27-33cb-b088-70c09db93cd0 | -4.9616 | -49.888401 | 2024-09-27 00:36:04 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0951858e-4810-31d0-ae06-bded97b9acce | -10.3672 | -53.7858 | 2024-09-27 00:36:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 221dcd84-6cc0-32db-a04d-f82182a5fb67 | -10.386 | -53.7841 | 2024-09-27 00:36:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| f6be4d8a-cde6-3c24-a672-1c713bab5d1d | -4.1361 | -46.4245 | 2024-09-27 00:36:05 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51c0b04b-60a5-397e-a99e-126424edc59f | -10.6434 | -45.9772 | 2024-09-27 00:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 1d0c4b8a-c3c3-3eb7-a397-444c52d1e181 | -10.6438 | -45.9544 | 2024-09-27 00:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 3117d125-0b58-31fe-aa42-b1f9ed12967d | -10.6452 | -45.8635 | 2024-09-27 00:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 3d23fede-da0e-350b-ba97-b1973725f9a1 | -10.6643 | -45.861 | 2024-09-27 00:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d45dc888-13d0-306d-97a2-eb94f4ebe4ed | -10.4799 | -50.751 | 2024-09-27 00:36:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| ebf7e4bb-f6ee-3c6e-ae84-f2edd65d6d43 | -4.1335 | -46.683399 | 2024-09-27 00:36:06 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
