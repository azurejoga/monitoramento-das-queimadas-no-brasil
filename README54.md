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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4d03401-c5f9-3765-9dd4-b1050a304558 | -1.02876 | -47.0528 | 2024-11-07 05:52:00 | AQUA_M-M | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| b8a8421a-e3a7-34ee-81ca-0bc72dfcc574 | -3.2181 | -53.10386 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ef43b01e-b013-3765-859e-c8b2d7355df5 | -2.84033 | -52.9016 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 366645e1-a65b-333f-83f0-151e0abfedaf | -3.46447 | -50.37406 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5e64da6c-13e7-35e3-b22e-6df982dcd0c7 | -2.80175 | -51.48877 | 2024-11-07 05:52:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f45c7586-9655-3ea0-9746-0a83b285fa31 | -1.15055 | -53.70823 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 477e4748-6abe-3cb1-b640-2b7f0941185e | -2.23745 | -53.66603 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| bff10ab8-9040-32e8-b43d-b4cf3236a38b | -3.72957 | -52.27099 | 2024-11-07 05:52:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 99f87963-3c1f-384b-a4fe-8c057d8558b8 | -2.40036 | -53.62939 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d0413e34-59c4-3a4d-b2da-c2126666c508 | -2.03053 | -52.34085 | 2024-11-07 05:52:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5e2f25fb-035f-3fd8-b94a-4f7d5e56e84b | -2.43195 | -53.66124 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0b8719d5-4aa2-332e-b1fd-aea917952737 | -1.14023 | -53.71597 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| d6e0b345-06e8-3b28-b497-3f78bc6f0d20 | -3.20109 | -53.39788 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e8b8305e-163f-3b19-9e5f-41250b4e4ce1 | -1.53179 | -52.21333 | 2024-11-07 05:52:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 215328f2-8b67-3b02-ae6b-385c8becc5a5 | -2.82755 | -52.92666 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 08ad30ee-a6f3-3fe9-bc87-ff27a55cbafd | -2.66633 | -49.88015 | 2024-11-07 05:52:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 77a98089-127d-3a7b-907e-aca5265684b1 | -3.53032 | -50.3462 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 65aa9ba1-9cba-389c-939d-809e9efa5a60 | -3.2994 | -53.11345 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 74ff425b-91e4-36b1-860c-b72e31246bac | -2.24636 | -53.66732 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| b3215b69-77bc-3af5-947d-64b996397419 | -2.62026 | -51.28961 | 2024-11-07 05:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 758d747d-a590-397c-a82f-f7f8d35c196d | -1.45987 | -53.48791 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8dfab2f4-ab1f-34bd-b0af-c62938d620b1 | -1.16711 | -53.7201 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a2e432df-fc27-3e9e-bcdc-70bd0c81d223 | -4.0909 | -51.00184 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| df418faa-4ad8-328f-94f5-36ac671af38b | -2.76643 | -53.21397 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 85716d55-7afb-3177-8357-a4e10e9e60ae | -3.01032 | -53.43873 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| deac0be3-107b-3772-a5a5-a35f0535b8a2 | -2.95236 | -48.59704 | 2024-11-07 05:52:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| fa4b8978-e598-3701-9051-af0d23e90b3b | -2.44085 | -53.66253 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c40b392d-bda0-322d-8b0a-6ebe22d6ef0b | -3.64083 | -50.13819 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 268381c6-589e-3832-b35d-53b50abfc75f | -2.85071 | -49.80833 | 2024-11-07 05:52:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0ab2d22e-acd6-3db0-8304-cc0ba4afbbbf | -1.1416 | -53.70676 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7e44d391-b6d5-3145-a709-5a2410092694 | -1.69243 | -52.13144 | 2024-11-07 05:52:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb1b610d-b641-3cff-b935-cfdfb11aae49 | -3.03676 | -53.26257 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 131d8e77-34ca-376a-9fa1-3c3b01387961 | -2.81608 | -52.94294 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 4f48476b-6e5e-3c95-a894-1b06c278f2cc | -8.31345 | -43.58775 | 2024-11-07 05:52:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 89c06554-3bda-3e95-9f87-4f1ef9486117 | -1.15545 | -53.7368 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d7f9fde7-14f8-3d9d-9a6b-b44d13e9260b | -3.6632 | -52.3382 | 2024-11-07 05:52:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bee56701-9ca2-3256-8b1f-6aca70f6594c | -2.61543 | -51.75168 | 2024-11-07 05:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| af4329ab-03dd-3221-b0a6-27a70dd348e9 | -2.75627 | -53.22149 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a0f05349-8d25-3be5-bf67-6312b27f5be6 | -1.52329 | -52.14885 | 2024-11-07 05:52:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 498714b6-46c2-3142-ae20-4e7fbd4722dc | -3.58838 | -50.22108 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| fc2c9a77-aa56-3703-922e-61f63099fca1 | -3.70899 | -48.98906 | 2024-11-07 05:52:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8fd9ed3c-0766-3100-a895-55be8ffa48e5 | -3.74511 | -50.06223 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| afc6832a-8467-3a1b-bc6d-404c1412e6b4 | -1.18644 | -53.89649 | 2024-11-07 05:52:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8e64544b-c809-3c24-ad10-643a5417c9c8 | -3.66532 | -50.26016 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| da9beccb-6987-3279-b4f3-1e50c0afc880 | -5.98684 | -45.34779 | 2024-11-07 05:52:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 3e51ee0a-68ea-376d-b19a-25e99ae7df7c | -1.32392 | -54.63807 | 2024-11-07 05:52:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 03f6d4ab-c9af-30ca-afed-011a3adc412a | -2.65685 | -49.87202 | 2024-11-07 05:52:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2dcaeea8-a49f-324c-be12-6313e27f06e1 | -3.62275 | -50.19215 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ad45e532-7c18-3439-8e00-55e81e4b6f64 | -2.40926 | -53.63068 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3b72fdbe-8a8c-3529-97f0-d575b237e18a | -3.45476 | -50.37265 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 2c380df8-10e5-349f-934d-ad8685e416f9 | -2.84704 | -48.66792 | 2024-11-07 05:52:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a6e1ea70-53bb-3b13-9847-7856287cd016 | -2.28808 | -53.81756 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 1cf8f8f7-0f12-347c-ae26-6b60a08266df | -3.25192 | -53.36031 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 45111db4-3c35-3b76-9e68-48baf5f00c3a | -1.14919 | -53.71735 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 13037ab8-3ca5-3c1b-b8b2-1d73f7178a8e | -2.81085 | -51.49004 | 2024-11-07 05:52:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cf6a9a3e-f24a-3f05-9473-511923914c44 | -9.92101 | -48.55893 | 2024-11-07 05:54:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c43412e9-8cc8-359f-b371-c9157079ab48 | -9.92433 | -48.56469 | 2024-11-07 05:54:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2d8f876f-960f-3bc2-ad52-941f331304cb | -8.03027 | -49.63373 | 2024-11-07 05:54:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 52a2f9a7-c3f6-3ddf-af82-389976006cf2 | -10.73467 | -49.82778 | 2024-11-07 05:54:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ded6d494-a0d8-3e15-b480-bccb5aa02ca2 | 4.34341 | -59.83794 | 2024-11-07 05:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3fdb743-7e01-3c32-ae0a-47eda686193e | 4.33862 | -59.83915 | 2024-11-07 05:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a141bf10-e08c-36f4-b342-6bc891b81cc5 | -3.6048 | -50.2521 | 2024-11-07 06:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| cd98fd04-f85e-3e32-9a39-ba0b6b56187d | -3.6049 | -50.2311 | 2024-11-07 06:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| cb2600e2-7e59-3321-b53c-5b0dfb335343 | -2.2845 | -53.8023 | 2024-11-07 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 2bcaf616-aff9-327b-b51e-a314d6e2450e | -3.6602 | -50.2501 | 2024-11-07 06:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2aa74862-e92b-3b31-ad3a-71e82708a6fc | -2.82 | -52.9409 | 2024-11-07 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 18e6cc88-c92d-30d7-91e9-33a6d20d51ba | -3.5863 | -50.2527 | 2024-11-07 06:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| a530d67a-7728-3292-a7fe-6a3c9766184c | -5.9788 | -45.3621 | 2024-11-07 06:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| aa1ceceb-95b7-3422-a1d9-08ae45bfc9ea | -2.9464 | -48.597 | 2024-11-07 06:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 39c594ec-3ea5-3cdd-9c51-07216c672d27 | -3.6787 | -50.2494 | 2024-11-07 06:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 89dd202d-3a8a-30fa-b006-4669d4660cbf | -2.8537 | -48.6642 | 2024-11-07 06:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 4e6fa43a-2448-3030-8ef5-d11e48726c89 | -5.9975 | -45.3607 | 2024-11-07 06:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| e7425b17-08b1-35f1-8d8a-11d20a95bd04 | -3.5864 | -50.2317 | 2024-11-07 06:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 185.7 |
| e204f59e-5fd4-328d-af53-e6017cc1e7f7 | -2.8536 | -48.6856 | 2024-11-07 06:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 769a72ec-998b-3b1f-9018-cb9f10188778 | -2.2845 | -53.8224 | 2024-11-07 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e4f77017-a796-3497-a6e0-56016c91a239 | -3.5865 | -50.2107 | 2024-11-07 06:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 41843400-f8f4-34c7-b751-477d6fdc0125 | -2.6645 | -49.8814 | 2024-11-07 06:00:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| dd8db507-7749-34fd-9639-d80a644c4c47 | -2.2845 | -53.8224 | 2024-11-07 06:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6ac8a73e-63e3-3777-84df-f8b3eeb96533 | -2.8537 | -48.6642 | 2024-11-07 06:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 6b20375c-abcc-335c-a8bb-3652539c8bb4 | -5.9788 | -45.3621 | 2024-11-07 06:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| edec0f9e-ca58-3e0d-a0d6-1756b1f17635 | -5.9975 | -45.3607 | 2024-11-07 06:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| c9ad8afa-0554-3c18-a0fe-a809be51b89b | -2.2845 | -53.8023 | 2024-11-07 06:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6cc0ce7c-4b71-3d48-8445-524a216581b4 | -3.6048 | -50.2521 | 2024-11-07 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 53523078-55f2-31ff-86a4-a6e478c23256 | -3.5864 | -50.2317 | 2024-11-07 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 9e7a68a0-8f74-31b5-a38a-2c6c77f3aba2 | -3.6602 | -50.2501 | 2024-11-07 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 8044958c-69e5-32d5-bd6f-549f6e3140a7 | -3.5863 | -50.2527 | 2024-11-07 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| fc41bc9d-ddd2-38d8-8398-e5575c384236 | -3.5679 | -50.2324 | 2024-11-07 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 1a2a0fd5-0a1f-39b3-9165-9ac9d56c88f3 | -3.5865 | -50.2107 | 2024-11-07 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 4a4e08e7-809b-3b37-897a-09a8879dda75 | -2.8536 | -48.6856 | 2024-11-07 06:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 9d64db4e-07d2-3064-82f9-1367f8cd6157 | -3.6049 | -50.2311 | 2024-11-07 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| e0dda34c-2328-3559-9545-add3b10ddb96 | -2.2845 | -53.8224 | 2024-11-07 06:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a6ccab23-e03b-36bb-9c12-4bb603e14e4e | -3.5865 | -50.2107 | 2024-11-07 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 4f8e728e-e8c6-373d-ba7f-c34b7ae0baec | -2.6645 | -49.8814 | 2024-11-07 06:20:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 7e21af3f-2d53-3a99-9220-b9eedc3122f1 | -2.9464 | -48.597 | 2024-11-07 06:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 8ddef970-639f-344d-aedf-61c91269a42b | -3.6049 | -50.2311 | 2024-11-07 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 227.9 |
| 30ddafa8-4905-313a-8481-8e42a94edd6f | -2.8536 | -48.6856 | 2024-11-07 06:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 7c00e857-d314-3d35-ac44-f0e10c743d15 | -3.5679 | -50.2324 | 2024-11-07 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| cc713bf9-c348-33bb-a6b8-42e9eec1002f | -3.6048 | -50.2521 | 2024-11-07 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 14f896f9-f9de-3f46-b8dc-0ba6b2f31554 | -3.5863 | -50.2527 | 2024-11-07 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 9db2878d-17b1-3abe-8e05-947d0fe221af | -2.8537 | -48.6642 | 2024-11-07 06:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |


[Clique aqui para ver as próximas entradas](README55.md)
