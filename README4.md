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
| fbca5050-0c55-3fca-a607-6d60c0320be5 | -10.5246 | -50.2351 | 2025-10-23 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| be9a03f5-772d-3bd3-82b5-bea9fe1fa2dc | -13.8002 | -52.7664 | 2025-10-23 01:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| a850458b-6807-3be2-8e73-a9dd98ab82f4 | -3.0168 | -49.4906 | 2025-10-23 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| f818064e-0a92-38ab-8cdc-66b8fc21a0d9 | -3.0354 | -49.4688 | 2025-10-23 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| c0b1430a-7f6a-3476-8b25-5c403afdb0fb | -3.0354 | -49.4688 | 2025-10-23 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c9ef8d04-d52f-3b36-897d-0e0042c79966 | -10.3406 | -62.8401 | 2025-10-23 01:40:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 4990207d-b70b-3b4a-bc7a-1e89093671f4 | -3.0169 | -49.4694 | 2025-10-23 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 8032d588-88e0-38a3-a56e-5a92480e2821 | -9.1174 | -65.359 | 2025-10-23 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d704704d-4ffc-3a3a-abab-9fee576d581e | -3.0353 | -49.4901 | 2025-10-23 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| cee6d6ec-7edf-36dc-87c5-7808ab7e800c | -3.0168 | -49.4906 | 2025-10-23 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 9c61bbec-f391-3111-81d6-a445f5d8993f | -12.0036 | -46.7667 | 2025-10-23 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e0591a9e-1d3b-3009-ac9f-63975ff28c5d | -10.4645 | -49.1006 | 2025-10-23 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 39083156-bfd2-34c7-b030-a374c3e0cf1a | -6.6079 | -44.2176 | 2025-10-23 01:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 154.9 |
| ee0745b3-8f33-3e92-a006-54dd79592e8c | -10.4834 | -49.0986 | 2025-10-23 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 2975c829-848e-31d5-95c2-96e31ae85800 | -12.0032 | -46.7892 | 2025-10-23 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 84f06a0c-37a9-395e-91fd-39b5eef2542f | -6.5891 | -44.2192 | 2025-10-23 01:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 28002ce2-2dfc-36d5-a9d2-51c2123c8060 | -3.0169 | -49.4694 | 2025-10-23 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 8ac4c53a-bfa6-3c21-a70a-55b665ab2acf | -6.6079 | -44.2176 | 2025-10-23 01:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| fb15ce8c-7386-3286-bfe4-238cf902d3ba | -10.5249 | -50.2137 | 2025-10-23 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 29c76d63-4f1d-3364-bfdf-68d8bec84f10 | -3.0353 | -49.4901 | 2025-10-23 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| b44b4957-9f3a-39f1-a79b-2dc22299ee01 | -3.0354 | -49.4688 | 2025-10-23 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| d3888db0-af00-3c46-b05f-d252ef32c228 | -3.4763 | -50.0673 | 2025-10-23 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 25e5971b-fb6d-3108-a76b-57cffb0de31f | -3.0168 | -49.4906 | 2025-10-23 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 28015cc9-e817-3d10-8902-459e8393550a | -12.0036 | -46.7667 | 2025-10-23 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| b8959ad1-c0df-3340-b651-52e7110c43ed | -12.0032 | -46.7892 | 2025-10-23 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 75606d5a-d22f-37fb-a12b-01a9fec295c5 | -3.0168 | -49.4906 | 2025-10-23 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 02ebb0cf-fa4c-3641-a764-d546143f976d | -3.0353 | -49.4901 | 2025-10-23 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 463606fc-9f64-3c2d-9e3d-e9b0f9850505 | -3.0354 | -49.4688 | 2025-10-23 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 56fbc504-a46d-3fea-8fc7-f931d052f554 | -12.0036 | -46.7667 | 2025-10-23 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 2cc43dd8-0d9f-36c3-aff2-79d4f005a016 | -3.0169 | -49.4694 | 2025-10-23 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 5e5aff4a-431e-3a36-94c3-52344117a1bc | -9.1174 | -65.359 | 2025-10-23 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| abd2f313-bfc5-36d2-9e92-9af69fda3f34 | -11.3646 | -49.7779 | 2025-10-23 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| be33f136-7d32-311b-a3f8-f3f88db78d30 | -12.0032 | -46.7892 | 2025-10-23 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9983d686-a168-38e9-aeb1-f5ae601b59df | -3.0354 | -49.4688 | 2025-10-23 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 19862587-4329-3fdc-846d-c1838c77e33e | -11.3643 | -49.7995 | 2025-10-23 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4d0156a5-c4af-3b69-8b18-7854fdb78849 | -3.0168 | -49.4906 | 2025-10-23 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 243.0 |
| 14e57d54-492e-3ba1-8ef8-9829f90811ff | -9.1174 | -65.359 | 2025-10-23 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1fa92a72-2bd8-3977-8fad-56c3f192dbe6 | -12.0036 | -46.7667 | 2025-10-23 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 5f13454e-d5f6-38b5-9d80-0ffe925b540f | -10.3406 | -62.8401 | 2025-10-23 02:10:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 5d1a3e2f-74eb-3d20-bc91-998e6e8a9701 | -3.0169 | -49.4694 | 2025-10-23 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 1954ef50-f887-37e7-89ca-883c5cbecf4d | -3.0353 | -49.4901 | 2025-10-23 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 5242f04b-acfc-35e1-8178-7512f43864b4 | -3.0353 | -49.4901 | 2025-10-23 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 0a461661-2793-39b9-adf0-eb03b7c793fb | -3.0354 | -49.4688 | 2025-10-23 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 148c2c77-5809-32a5-a3db-ba436c636878 | -9.1174 | -65.359 | 2025-10-23 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 5abeccf9-a6b9-315b-8f87-53b2d10ca866 | -3.0168 | -49.4906 | 2025-10-23 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 208.7 |
| c88736f2-57f3-36b1-8bfe-763ef1c898d0 | -12.0036 | -46.7667 | 2025-10-23 02:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d3c28270-489a-3927-9739-975188a626c7 | -11.3643 | -49.7995 | 2025-10-23 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 56f2c540-af96-3d0d-a815-6e570d61063c | -3.0169 | -49.4694 | 2025-10-23 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 77ea739f-7c29-31d7-91aa-4bf34da3a18d | -3.0168 | -49.4906 | 2025-10-23 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 23fead72-a303-34c6-b1f8-ae4d2274b0b8 | -19.2672 | -49.3443 | 2025-10-23 02:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 5941e142-0e45-3f5d-b029-17c6749de130 | -11.3643 | -49.7995 | 2025-10-23 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 3a827203-7bb1-31b7-87df-59a607364d20 | -10.1994 | -36.3197 | 2025-10-23 02:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 247.7 |
| ca092c8a-4be5-32ac-a801-55ac5fb54bce | -9.1174 | -65.359 | 2025-10-23 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| ea34d973-49b6-32ec-9a31-be7ab5842a90 | -3.0353 | -49.4901 | 2025-10-23 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 2d997006-7881-3c67-a7fc-47b12d0cd77b | -3.0169 | -49.4694 | 2025-10-23 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 82b1ba9e-b791-366e-8b6f-650649aa22f4 | -10.1801 | -36.3232 | 2025-10-23 02:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.4 |
| 4143732f-2c6a-3622-adf2-bffaec3b1e9b | -3.0354 | -49.4688 | 2025-10-23 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| aad72319-bd5d-3ecd-b312-5e403a26de4f | -11.3643 | -49.7995 | 2025-10-23 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f54010d5-7919-3a72-a5d8-6822ae529da6 | -12.0032 | -46.7892 | 2025-10-23 02:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 23918865-1e29-3f61-b36f-b2f9e0f33a67 | -3.0169 | -49.4694 | 2025-10-23 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| c801d36b-9ac5-3c3c-9955-194d10d326cc | -3.0354 | -49.4688 | 2025-10-23 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 6f62791d-5976-319f-9f3a-ab6a815ccfb6 | -17.6173 | -46.5906 | 2025-10-23 02:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 44c76a5b-4a48-3a33-8980-0c2b87e52bc4 | -3.0353 | -49.4901 | 2025-10-23 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 99e73af5-23d3-3b9d-bee7-850ac0f3a79a | -3.0168 | -49.4906 | 2025-10-23 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 7dc16177-63d7-367c-a48f-e2fe9959fe4f | -9.1174 | -65.359 | 2025-10-23 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| b9e3da89-e4d5-33dd-a2e9-8db005458e27 | -17.6167 | -46.614 | 2025-10-23 02:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 39723c7e-dd7b-35b0-9401-a35f6fe429d7 | -3.0168 | -49.4906 | 2025-10-23 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 2437bc16-ed14-38ef-b8a0-fb8da452530d | -6.236 | -35.2004 | 2025-10-23 02:50:00 | GOES-19 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| 9c31ed25-bdee-33a8-bb41-0d2c63680ac8 | -17.6173 | -46.5906 | 2025-10-23 02:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| d71cd0ee-c701-3bf7-8e4f-5dcd52b6d1dc | -17.6167 | -46.614 | 2025-10-23 02:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 0c75848e-968d-3f26-b77b-7e2c2ec3d9f1 | -9.1174 | -65.359 | 2025-10-23 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| d023477d-5303-30e5-a8c1-14e372daff8c | -3.0353 | -49.4901 | 2025-10-23 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 0cad54cd-8757-39fe-bfab-27dcd009964a | -3.0354 | -49.4688 | 2025-10-23 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6eb7cd18-cf26-3b59-b5a3-9f298a418149 | -3.0169 | -49.4694 | 2025-10-23 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 65c81a07-0dae-388f-a4c3-1b8fe73050da | -17.5967 | -46.6182 | 2025-10-23 03:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 555d19be-4e9d-3ab8-b926-f195eb804b47 | -3.0169 | -49.4694 | 2025-10-23 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 93e10ad4-f113-34f1-91c3-b24fed29beb4 | -11.3643 | -49.7995 | 2025-10-23 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 7bcc6d7a-8f4a-3f9e-a7c4-91805041dfab | -9.1174 | -65.359 | 2025-10-23 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| fa552849-97ca-3b23-9213-16bd2612f425 | -9.6295 | -40.3392 | 2025-10-23 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 02a3f3b6-06e3-38ad-98ab-c3e54919f603 | -3.0353 | -49.4901 | 2025-10-23 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| b5af25d7-304f-384c-8be4-c64e6759c2aa | -9.6299 | -40.3143 | 2025-10-23 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 3f542df6-ea46-3496-bfc9-07d7ae267f59 | -3.0168 | -49.4906 | 2025-10-23 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 8e93de74-375f-34eb-bc40-e1efe4b8d00c | -17.6173 | -46.5906 | 2025-10-23 03:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 7209bc0d-74ec-3b13-acec-5e93f7f8b442 | -23.6812 | -51.6361 | 2025-10-23 03:00:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 58.6 |
| 95f97d3e-37bf-387b-bbcb-87ec4493391f | -3.0354 | -49.4688 | 2025-10-23 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 62bf93c1-9463-35a2-96f2-10b793944f06 | -17.6167 | -46.614 | 2025-10-23 03:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 2e5834a4-4f7a-33f1-b6a6-5e9bb4376b59 | -23.6806 | -51.6591 | 2025-10-23 03:00:00 | GOES-19 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 46.8 |
| 3c5d64d4-d767-3393-9f65-a8ec06d8bdff | -3.0353 | -49.4901 | 2025-10-23 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| dfe14046-06e1-395e-a414-c932f5b2dd23 | -3.0168 | -49.4906 | 2025-10-23 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| d35d1c8e-aae7-3d00-ab2e-848bb1d82f68 | -17.6167 | -46.614 | 2025-10-23 03:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 292.3 |
| 1bd8cfcb-6c68-3950-8d70-7856501d1e94 | -17.6173 | -46.5906 | 2025-10-23 03:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 133.6 |
| f93e75a9-5747-3964-9115-04c8242d9707 | -3.0169 | -49.4694 | 2025-10-23 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 77b95aee-1eee-3f3d-b5d0-6ad2f3dc2c29 | -9.1174 | -65.359 | 2025-10-23 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| b48cfdae-af77-388a-9a82-b5fee3151590 | -17.6161 | -46.6373 | 2025-10-23 03:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 3313a54d-cfad-3ca1-b6ca-548cbcac4ab2 | -3.0354 | -49.4688 | 2025-10-23 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ec44348c-dce4-3a27-94c5-67d4c3137202 | -17.5967 | -46.6182 | 2025-10-23 03:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 4be2f0df-c722-39de-8114-86ca7fca26dd | -17.5973 | -46.5948 | 2025-10-23 03:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 11426064-8e4c-3ceb-b3a1-fcfd74df11a6 | -2.87061 | -40.43061 | 2025-10-23 03:13:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4987a5b5-9960-380a-88f5-fc59be7a0350 | -2.87061 | -40.4306 | 2025-10-23 03:13:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b69765e5-1f47-3d14-a3a3-60114a34bb85 | -9.98157 | -37.04429 | 2025-10-23 03:15:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |


[Clique aqui para ver as próximas entradas](README5.md)
