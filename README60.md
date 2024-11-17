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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 970c761b-5fbe-36e3-a537-0a0a33e02801 | -2.8614 | -46.7306 | 2024-11-17 05:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 2b000344-68d0-347e-a5b2-d541f7fab42a | -2.8615 | -46.7086 | 2024-11-17 05:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 1684721f-29c3-3ea8-b05a-0ac4ea061571 | -4.5616 | -47.9925 | 2024-11-17 05:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d8a8730b-a80c-333f-8f8b-f3d2bf5940be | -4.5614 | -48.0141 | 2024-11-17 05:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| b7733ecc-ad6f-3613-a86b-6c2fed7bbc21 | -2.6322 | -48.5634 | 2024-11-17 05:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 135cfa70-750c-3915-8784-cba9119d2913 | -3.75004 | -54.7225 | 2024-11-17 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ea6c6f0-0543-39ca-a7a7-5be74472f300 | -1.67285 | -47.97453 | 2024-11-17 05:22:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6bcb4b08-b4f6-33b0-92b6-07da9c73a1d2 | -0.94667 | -51.72689 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dcc2a168-ecfa-3f01-afd8-ff182eeb2f7a | -0.95937 | -52.41222 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6533b7a6-fa4a-3697-a1ed-0de2a09fda6f | -0.10607 | -51.61131 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5648c193-668b-3c6a-8b41-1c9fff591067 | -0.12823 | -51.62081 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 572f3c67-9d6c-304c-be5e-0a3f8d3cb031 | -0.10865 | -51.59521 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 2d2edcaf-41a4-3a2b-b1f7-27fdf9e6b65a | -0.83341 | -52.34211 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78c59e7f-2ef7-3faf-8b87-f63518f4b2a1 | 0.41184 | -50.86255 | 2024-11-17 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa2c158b-34ba-325d-816b-f05c9a8f02f9 | -6.49216 | -47.49558 | 2024-11-17 05:22:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8593f810-dd71-365b-be95-57253a1b771b | -1.67209 | -47.97961 | 2024-11-17 05:22:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fdf12edc-4646-331c-8793-27ab3ec3b3ac | 0.00071 | -51.22319 | 2024-11-17 05:22:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf0a1d0d-3146-3cf5-bd03-9273f0c50f4f | -3.45222 | -54.68372 | 2024-11-17 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57dbaba5-8c76-3946-8ea1-b266577e4360 | -4.72776 | -46.8394 | 2024-11-17 05:22:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 53c6616e-07bb-3694-91e0-c069809e1627 | 1.05926 | -60.59993 | 2024-11-17 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00c9b56f-dcfb-379b-be9f-250b5d1e0424 | -0.04865 | -53.2524 | 2024-11-17 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0bb9d4a-8e9f-39c5-b03d-4a1e87d635bf | -4.15209 | -50.77806 | 2024-11-17 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cb862e8-9871-3f3f-8695-826f04df8d44 | -0.10728 | -51.59537 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 56824de0-3ef1-3c4c-b1cf-33b5584f030d | 0.4169 | -50.86172 | 2024-11-17 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0fb1df1b-e5ce-313e-8918-67dcb5804d6f | -3.79651 | -51.37664 | 2024-11-17 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4f1160c-7466-30ac-a050-ad617889afe7 | -0.94313 | -51.63754 | 2024-11-17 05:22:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12fa6488-3916-38e3-b6f2-002414ba3ded | -3.71514 | -51.84492 | 2024-11-17 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd8d2f75-7e3c-3470-8991-f4ecd78915b8 | -3.7974 | -51.37068 | 2024-11-17 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5df7ff8b-7112-3cce-b27b-c8a8d309b02f | -0.90434 | -51.74235 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc775a74-83f3-3054-bab4-6cec31ba3267 | -3.34506 | -53.31397 | 2024-11-17 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 387dac10-f6e5-3d13-bf65-83d78eea79b4 | -3.75059 | -54.71878 | 2024-11-17 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f38c0d99-b41d-3819-a0a7-c754bedce3e1 | -0.94232 | -51.643 | 2024-11-17 05:22:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 236e6abb-cf1f-38ed-b4eb-b80dc9d8ea2a | 0.40677 | -50.86336 | 2024-11-17 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed7c6266-f506-3bc6-81ec-59445c475174 | -1.83683 | -46.59948 | 2024-11-17 05:22:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d4c5174f-8539-36d5-959b-5381eb516942 | -3.76459 | -54.56498 | 2024-11-17 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fdc0e914-e5a3-3e9c-bb3a-0d4ddae6d231 | -3.38961 | -53.26473 | 2024-11-17 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfce760f-2add-3b10-8480-8c07b7e33964 | -0.11214 | -51.59613 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 61f64ef6-a548-350d-b008-8130d588fd87 | -3.76564 | -52.31637 | 2024-11-17 05:22:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d60bfe06-f4b7-360a-9752-0725c2365334 | -1.83751 | -46.59827 | 2024-11-17 05:22:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d93567dc-24f5-3741-bca6-3b79a68a0ab5 | -0.31643 | -48.69714 | 2024-11-17 05:22:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9959ec00-5c51-38f5-8dc7-62ab24f4894a | -0.9418 | -51.72612 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fb8c2b3-f67c-3419-a5f0-208e69803142 | -3.74645 | -54.71812 | 2024-11-17 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f76f9b77-a57c-3d0a-a43e-1a2c707ec174 | -0.94479 | -51.72703 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bcaf661c-dc8d-330b-b43d-783756d8681e | -3.7983 | -51.36992 | 2024-11-17 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0001d6b-bf6c-39b8-b2e6-40d7587f571d | -4.22848 | -50.67801 | 2024-11-17 05:22:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bd2c275-623f-3038-89a0-0a93f25a31c0 | 0.61292 | -51.77669 | 2024-11-17 05:22:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 5b5b63f4-59c7-34ee-840d-0cfea9d031df | -6.4913 | -47.50222 | 2024-11-17 05:22:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5aeaa242-152a-314a-bf4e-7247c3af4e30 | -4.55921 | -48.0092 | 2024-11-17 05:22:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| cd3116d5-ddf3-3407-8fca-1899d7f01376 | -3.38891 | -53.26934 | 2024-11-17 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dad91341-d71f-3619-b27e-2dc61f560b14 | -0.90198 | -51.72541 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2c01d101-03d3-36e4-b152-51cd8f9f80b2 | -0.31179 | -51.50305 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49923e47-68f6-32f9-a75c-cce7a8e321da | -3.3439 | -53.29055 | 2024-11-17 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eadd9c42-2368-3ea5-bed4-425aa0e5328f | 0.40217 | -50.86712 | 2024-11-17 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 243ead0b-9355-3500-83b9-6316676f9359 | -0.31669 | -51.50383 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 85f009ba-acad-34cc-b1a5-34e6ce58dc30 | -0.94966 | -51.7278 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fff9967e-7afd-3b84-a2cd-55408c48198d | 0.52838 | -50.06005 | 2024-11-17 05:22:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6bdeb2f-c86b-3b34-9df1-187710267a8c | -3.70067 | -51.08238 | 2024-11-17 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7436c9a8-9882-3e29-ad34-4bf1219b8737 | -4.41761 | -50.50072 | 2024-11-17 05:22:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fe7e648-cef5-38e3-a21d-9b95da3ec45f | -0.92941 | -51.76324 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 136dd542-2a68-3d84-ba68-b62ddc190bb4 | -3.71597 | -51.83908 | 2024-11-17 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55b817a4-a218-34a9-a270-d7f54f84e001 | -0.95372 | -51.73398 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1e324cb8-01c0-3d4c-907b-d6ef42429aee | -3.3464 | -53.30497 | 2024-11-17 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ebd426b-67d9-30b9-9c64-a4f4616cc0b9 | -0.89037 | -51.80046 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00d57300-1b63-37b2-b3bc-180e8084730b | -0.31432 | -51.50297 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d72e96a2-c943-3fdf-874f-92dc83da1c3c | -3.71669 | -51.83952 | 2024-11-17 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32ee21a9-d50e-30c4-84d0-fc1b3a36bc64 | 0.51673 | -50.74201 | 2024-11-17 05:22:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc567055-3ce3-3756-87d5-e0937c01c4f6 | -0.95399 | -52.41631 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17bb5d30-960b-32cd-8832-b37c262b6df2 | -3.7459 | -54.72185 | 2024-11-17 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd5e1c7e-f2d1-338d-91cd-fcb928533807 | 1.58099 | -55.87808 | 2024-11-17 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fbc1fec-8fa2-36b6-a12f-ea8b50e4978a | -3.34573 | -53.30946 | 2024-11-17 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 914d5874-67ed-36f7-889b-513bea5965cb | 1.05982 | -60.60352 | 2024-11-17 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2179a263-ee41-3768-b88d-f1bfe6196acf | -0.94484 | -51.6431 | 2024-11-17 05:22:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 336a04e1-de9e-3743-8962-f13d28ea8ee9 | 0.61683 | -51.77071 | 2024-11-17 05:22:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 258190a1-b7bd-3318-9cf4-f0bdfd4d41dc | -3.70762 | -53.75096 | 2024-11-17 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 590758fe-181d-3858-a517-e8d9e0e86528 | -0.89948 | -51.74158 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e29d9cb-1dc2-3f7c-a53a-a1a5794349f5 | -0.04632 | -53.25401 | 2024-11-17 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d66a01f7-da32-38b9-a9f0-9897540ae5ea | -3.43282 | -53.32439 | 2024-11-17 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a49a8917-c6b2-37ee-a444-ebfcaa491ac6 | -3.33938 | -53.2897 | 2024-11-17 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d2c0142-b3a9-3f0f-9353-c89dda55fe15 | -3.79695 | -51.37367 | 2024-11-17 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b04018c-b160-3e0f-b414-4e8fad70211b | -3.7112 | -51.84165 | 2024-11-17 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5964dd87-a0d9-33b7-8c88-588db61ecfd6 | -0.15747 | -51.59252 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39b1517b-7518-3833-a931-34251351db0e | -3.19928 | -54.31923 | 2024-11-17 05:22:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51a5144a-71e3-3613-8e80-753cf81b175c | -1.22676 | -47.36029 | 2024-11-17 05:22:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 805220ab-896e-3b2d-ae5a-c15632595484 | -4.0346 | -50.88685 | 2024-11-17 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47c0524c-3d21-3e38-b1b4-e57317491cee | -3.34121 | -53.30872 | 2024-11-17 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4e869b3-edc4-3b73-b428-392d7f72e5d7 | -0.95864 | -52.41704 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 538ccdb9-1854-33d4-b415-3c2e8b8dea41 | -3.71625 | -51.84243 | 2024-11-17 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3203bffb-6ee4-38e7-b22d-30e093f78c6c | -1.9119 | -46.57163 | 2024-11-17 05:22:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 16ff4850-e2f9-36c0-a6e9-df7d74574ed1 | -0.12258 | -51.62524 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b33512d-e277-3cf9-ae00-ffb861b35d8a | -0.93036 | -51.73537 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39cb4892-c41e-33b9-8c70-2ac5c4959122 | -3.39279 | -53.27446 | 2024-11-17 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c604be90-b516-32f0-a4ec-333bebd48a8c | -3.87033 | -51.16735 | 2024-11-17 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 481fae11-ab24-37e7-afbc-e8f78af8a3bd | -0.40618 | -51.6248 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c338a5e-cf72-3b96-ba86-5961653e7fde | -4.22899 | -50.67436 | 2024-11-17 05:22:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8abfcd4-dfcd-3c75-8636-0398080e48cf | 0.41735 | -50.86467 | 2024-11-17 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84a56120-4821-3a4b-962a-26b00bb84756 | -0.88439 | -52.78625 | 2024-11-17 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95e2c5e8-2924-3868-a693-6389d7438c1d | -0.90174 | -51.94872 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ec51d49-215a-300f-adf0-ec4930e7eba1 | -0.95472 | -52.4115 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81fdcb79-58ee-3263-886d-e742dc3bf286 | -4.15259 | -50.77458 | 2024-11-17 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e17ecc9b-625d-3aa9-b5a9-e049020b86f0 | 4.08298 | -60.24752 | 2024-11-17 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README61.md)
