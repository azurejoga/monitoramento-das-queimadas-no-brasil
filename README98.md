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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4edb502b-4317-3924-833f-c285809f5a31 | -7.712 | -46.2531 | 2025-10-06 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| fcd3d778-2ad2-3a5f-b23d-418f62b670e2 | -6.5424 | -45.1374 | 2025-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 9e9d20e8-5cf9-35e5-85e1-c014ade9cc18 | -14.6321 | -52.535 | 2025-10-06 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 46534b3d-5bbf-3507-8cea-8a501b97622d | -6.5986 | -45.1328 | 2025-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| d7ca5126-5dc7-3df2-a505-9a33d8cb3f38 | -8.4673 | -54.6833 | 2025-10-06 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 67c0c09a-9c0f-3d74-8c0c-996a4b88e94f | -6.5989 | -45.1101 | 2025-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 5f956468-e0df-3383-9a6e-b1357cc142bb | -8.5196 | -46.3323 | 2025-10-06 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 18b06c74-78f7-3251-9452-e8d5109c5739 | -7.8687 | -44.1227 | 2025-10-06 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 726bfc8e-6ecf-3070-9586-470018796456 | -7.8121 | -47.3759 | 2025-10-06 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| c88a78f0-9434-3b0e-9de1-51564aad002d | -8.5584 | -46.2387 | 2025-10-06 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 2f38108e-51bd-3817-9588-db4492b723de | -6.5941 | -43.7333 | 2025-10-06 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d7e65d2d-05f7-3f23-a241-ff13cabcd1aa | -8.8803 | -47.6061 | 2025-10-06 14:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 18248db1-5124-379c-ba8d-62b537c47b4c | -14.6325 | -52.5137 | 2025-10-06 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 64e14d65-0afd-3093-921e-32549a6b90f5 | -7.348 | -45.227 | 2025-10-06 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f3adc0bf-2203-34af-8708-de1d353c01da | -8.5578 | -46.2836 | 2025-10-06 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 74155fc6-94f7-3872-af1d-ce045d7c9f99 | -13.2703 | -47.8175 | 2025-10-06 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e6e2309b-020e-3a22-b270-d5c968a73567 | -10.4099 | -50.3324 | 2025-10-06 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 1b8aa9a0-fd80-30d6-ad63-93db1f6e2ab8 | -18.2773 | -53.3082 | 2025-10-06 14:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 6602974d-ce10-3586-b2bc-64b7a3dd7bd2 | -6.5611 | -45.1359 | 2025-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| f8618aa5-ad32-33ac-8d60-ca6a44436b3b | -11.0697 | -47.9147 | 2025-10-06 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 16f5661f-b42a-3ed0-8750-6a78791eb6db | -10.0217 | -48.2994 | 2025-10-06 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 821b6aa5-71c8-3b37-82ef-53a2ee0e18da | -9.6804 | -48.4014 | 2025-10-06 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0854ca72-d083-3047-ad92-95a19667bddf | -9.6614 | -45.6667 | 2025-10-06 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 739d3257-0094-35ec-a9e5-323412ef06f1 | -9.4863 | -46.0039 | 2025-10-06 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 1e63c26a-8741-34f4-a047-7928069c0b3e | -7.2776 | -44.8007 | 2025-10-06 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| df5bbf9f-3e51-3fcf-b4a6-a40cd7f4e6aa | -9.9215 | -50.1682 | 2025-10-06 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 20fb8604-5392-35b3-b30b-fc55657183d2 | -15.9842 | -50.8395 | 2025-10-06 14:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 007f30a4-3b20-3400-8377-ce1222397cb4 | -7.8074 | -44.5209 | 2025-10-06 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 448993b5-8125-37a1-bc79-a36116267b8b | -7.2389 | -44.8955 | 2025-10-06 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 1764498b-5198-3b77-8774-fa0e853888e1 | -7.7182 | -42.5688 | 2025-10-06 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 38d2f986-9b45-3061-923c-7f1848fbb970 | -14.6135 | -52.495 | 2025-10-06 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 1a2c3f80-ec66-3950-8933-425fc348e814 | -12.9653 | -51.0457 | 2025-10-06 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 830d2f27-9b37-3508-9ca9-7dbc20bb87e7 | -6.6016 | -44.8369 | 2025-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| eeeb3f48-c7bb-3f2a-96c6-352ecd0aedd3 | -10.4054 | -45.3931 | 2025-10-06 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 7f9d7c08-3d8b-3305-a08a-a7fb5d2176c7 | -7.5329 | -43.8552 | 2025-10-06 14:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 2870c15c-5b76-36f1-856b-593cee93f559 | -15.3545 | -56.9287 | 2025-10-06 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 318.4 |
| 4b874783-206e-301c-bf41-ba13a3ed5885 | -6.7437 | -45.6185 | 2025-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 7e7c459d-728e-32c3-bb5c-cd404d2ba1de | -7.2778 | -44.7778 | 2025-10-06 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 189bb1f4-62ba-34fb-834b-425a5c9cee6e | -6.454 | -44.5978 | 2025-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 6e00809f-267f-3e28-b420-18116c6bd75c | -5.4155 | -43.4552 | 2025-10-06 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 04d88621-30e9-3806-aa74-fa1bc94a078f | -13.2708 | -47.7951 | 2025-10-06 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| ffcb9353-2e8a-39c3-8df8-fd3b67b1d992 | -8.5581 | -46.2611 | 2025-10-06 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2f721e8f-2eef-3302-8a3b-f15d5b81e2c8 | -9.683 | -48.2044 | 2025-10-06 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 9a713f4a-8e43-3ce6-9db9-a509707b9507 | -9.6801 | -48.4232 | 2025-10-06 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 9ddc8951-9733-3198-9c8e-7b12e30f12e6 | -4.0567 | -42.5354 | 2025-10-06 14:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| e53a3299-06c9-3250-9118-03d83997ec30 | -12.3917 | -51.0726 | 2025-10-06 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 3ce8f455-dde1-3d73-bb8b-762f298390a5 | -6.523 | -45.207 | 2025-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| dcfcf39b-0c53-3d21-bbb8-d9dc6276ec34 | -12.3914 | -51.094 | 2025-10-06 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 86c96930-bf21-3c7e-a61b-004967d0f643 | -16.0086 | -55.9949 | 2025-10-06 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 422d698b-75d5-337c-a6cd-8d5438ec669e | -10.391 | -50.3344 | 2025-10-06 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 43275c17-71e6-3ed8-8a3d-6f7c1977679b | -7.2723 | -45.2792 | 2025-10-06 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ea5a7826-4d5a-39e8-a625-8571586b1360 | -6.6567 | -44.9462 | 2025-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| cd927104-0c2f-3d79-b533-9935dda3e8db | -12.5733 | -48.1393 | 2025-10-06 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 9ee6e7b4-0f0c-31cf-90fc-96123bf145d7 | -6.5799 | -45.1344 | 2025-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| c4830a76-e16c-3973-860b-14e0d73c1976 | -10.1874 | -45.9889 | 2025-10-06 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 2eac9ea6-4f83-3e78-9e01-ff0b0c1ee270 | -3.2152 | -42.6717 | 2025-10-06 14:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| adb75aa3-422c-3254-a965-44a91794eab0 | -7.7938 | -42.5607 | 2025-10-06 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 3e09a623-90fe-3470-b309-1b6074ed4c26 | -5.4343 | -43.4538 | 2025-10-06 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b7cc1f46-8f11-3b03-906d-85dbe93ba39f | -8.1891 | -44.1357 | 2025-10-06 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 15896424-dbbf-3bb9-a3b3-d8a33018d31a | -18.2574 | -53.3114 | 2025-10-06 14:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 4ddd145f-8ee3-3afc-9b1f-064e76ef0054 | -8.5393 | -46.2631 | 2025-10-06 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 9eb383f3-6842-3fc2-9cff-286e29c2accb | -12.9848 | -51.0219 | 2025-10-06 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 142.3 |
| e5b88e4c-d878-3a68-85ee-9810acafab99 | -9.9024 | -50.1914 | 2025-10-06 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ea5ad322-b938-3642-a404-3a9d6d4df782 | -12.3793 | -63.7294 | 2025-10-06 14:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fa09b80f-0786-36e8-8940-58fd2cb516d0 | -15.2012 | -56.8435 | 2025-10-06 14:40:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| c6edd952-b379-3845-aea9-b8907d7ac359 | -17.9308 | -55.8758 | 2025-10-06 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 8c3b0744-c2a2-368f-b75c-9d8345dd4592 | -10.6335 | -50.5651 | 2025-10-06 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| db943b99-1633-3fba-b348-ce9de49bd7cf | -7.7371 | -42.5668 | 2025-10-06 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 37d35522-b98c-3c97-aa72-56a9aa34bcaf | -7.793 | -44.1535 | 2025-10-06 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| e5166681-94f6-3d77-a179-ed35b6b9fbd8 | -7.3577 | -44.3575 | 2025-10-06 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 030cf070-73cb-3742-83b3-67192a6c221e | -6.7821 | -45.5251 | 2025-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 07001a04-9b57-387c-a7b9-6e8ab856c1be | -17.2517 | -46.9204 | 2025-10-06 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 81a2b12c-f737-30b4-813b-821eec37c3cb | -7.4276 | -46.5239 | 2025-10-06 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 1a5ab71e-56dd-3bd8-a0d7-8a1e6b395d5c | -13.2515 | -47.7979 | 2025-10-06 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 6c6c41fe-4697-37ee-a645-7fc1808d4832 | -17.2717 | -46.9164 | 2025-10-06 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 7705df15-44c1-3408-84e0-dd011611beee | -10.022 | -48.2775 | 2025-10-06 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 91df2eb2-548d-3911-aeb5-d2fe8322f658 | -13.7279 | -48.0836 | 2025-10-06 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| bd9376a0-11e7-3cd1-a3f6-9c4c550084c2 | -7.0572 | -44.3393 | 2025-10-06 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| acaaf46b-7d4f-36ae-8bcf-7ab3ea5b15ae | -7.7749 | -42.5628 | 2025-10-06 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| fa0a7fd2-fd83-3ac3-b1a5-006e6e6f2062 | -12.9841 | -51.0648 | 2025-10-06 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 281.6 |
| fad3727c-be95-3cc0-8db6-47539811088b | -10.1687 | -45.9686 | 2025-10-06 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 59f187ca-6bb6-3b7d-afbe-6074fe8068fc | -8.6694 | -49.5369 | 2025-10-06 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 45eec60e-f35e-346b-a850-5289f7dbe40d | -8.88 | -47.6282 | 2025-10-06 14:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3da443b8-c75a-3b89-974e-a221f3a0aa6e | -11.6647 | -44.2702 | 2025-10-06 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 90aab16e-8f4f-37bb-b372-ad4b04e411b6 | -15.9838 | -50.8614 | 2025-10-06 14:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d1e78e8f-a96a-34ca-99b9-8cff3bc81e66 | -11.8033 | -45.0856 | 2025-10-06 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 4c560d26-d6d0-31a1-b605-e5b302d0e635 | -8.6835 | -49.9419 | 2025-10-06 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| caf24e44-6e8c-3e04-b33f-ec7fd3ceefe5 | -8.5193 | -46.3547 | 2025-10-06 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| f74aaeee-703a-3e19-b9ce-b90d13d0233e | -7.7746 | -42.5865 | 2025-10-06 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 07803ada-3f85-3204-8fb0-30dd54b41348 | -12.8958 | -47.2684 | 2025-10-06 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 367f1cb3-bcb4-3f7d-ac13-8a421096acaf | -11.8447 | -44.9176 | 2025-10-06 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 85f6bbc8-c545-3de8-89ba-222727ab355f | -12.9103 | -54.7352 | 2025-10-06 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| e843057d-1919-3f8c-af15-717c6c0fbe55 | -8.8534 | -46.7451 | 2025-10-06 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 6629110f-0aaf-31cf-91af-57e587fb5839 | -7.5969 | -44.8165 | 2025-10-06 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |


