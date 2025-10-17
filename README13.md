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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e5f2c46-d005-3813-95d0-e999a3bb154a | -3.5213 | -52.4728 | 2025-10-17 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e570b30b-4ef7-3122-b2de-71644449437e | -12.9175 | -47.1303 | 2025-10-17 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 667b24de-1721-3105-9cc0-e6218b818c3a | -11.5733 | -48.5568 | 2025-10-17 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b1e9b149-34e1-3cbb-8a7e-5721a6be74cc | -4.3871 | -43.4292 | 2025-10-17 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 3130b0cd-6054-3bb9-ab32-d771afca9080 | -3.236 | -45.9639 | 2025-10-17 00:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 264.8 |
| 7c604102-0119-378f-9248-8b04961a156e | -10.2935 | -44.0455 | 2025-10-17 00:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| ab19d7e3-ba31-33d9-b7f7-df5a4e6acbf4 | -9.879 | -47.6779 | 2025-10-17 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 6c62f00b-3b31-3a91-97d0-d7c3f451b430 | -3.5212 | -52.4932 | 2025-10-17 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 9e8d7c2a-0465-3d0b-a39f-84668577995c | -11.4748 | -44.1819 | 2025-10-17 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| d06489cf-92ad-3670-bae0-a00103314aa5 | -8.1996 | -43.3189 | 2025-10-17 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 537413e6-7683-31ca-b66d-19e4875c01ee | -11.398 | -44.1933 | 2025-10-17 00:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 937bccef-ecb2-3663-955c-699f37ff9992 | -4.4246 | -43.4038 | 2025-10-17 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 435.0 |
| aec407c7-9635-3b9e-bb94-14b5e29cd356 | -4.4058 | -43.4282 | 2025-10-17 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 1c46ccf9-b275-30b0-9f72-643b2ba09efc | -4.484 | -42.9335 | 2025-10-17 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| d925fb76-58a9-3058-86ef-e0cd90fde270 | -11.5921 | -44.0472 | 2025-10-17 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 3b2d507a-a78d-3d7b-9e25-a1912108145d | -16.0324 | -43.4953 | 2025-10-17 00:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 0d93a6db-dd3e-3b95-9fb7-fff178013de2 | -10.4941 | -43.4315 | 2025-10-17 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 293a46ed-ef55-33b0-8256-115bb17d6865 | -9.898 | -47.6758 | 2025-10-17 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 560c154e-df85-392f-8fce-e7b28a134358 | -10.1528 | -44.5289 | 2025-10-17 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| fb555f75-2ed8-3ff2-8d1d-cb90fd7e9157 | -3.2545 | -45.9855 | 2025-10-17 00:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 8638b819-559f-3018-abae-e60ae380ee50 | -2.7441 | -48.3022 | 2025-10-17 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 02e5d0f0-e6d8-3250-85da-93fc6db6ee92 | -10.5136 | -43.4052 | 2025-10-17 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 311fe485-bc67-32c3-826f-e20406d3d70e | -7.1949 | -45.4899 | 2025-10-17 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 22eb5668-8bbc-30d4-ab42-fcb3454edb10 | -7.9631 | -44.113 | 2025-10-17 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 244f4b12-fdb8-3b49-bddb-29f7d4655378 | -3.2546 | -45.9632 | 2025-10-17 00:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 270be352-9b75-3a85-b8f4-273c99b1a37f | -2.7585 | -49.3922 | 2025-10-17 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e9aa741b-3853-341c-8bdb-de9f8214718e | -4.4059 | -43.4049 | 2025-10-17 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 856.5 |
| 527f623e-bd5b-389f-be96-f9759b3886ec | -9.7113 | -48.9202 | 2025-10-17 00:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0b1e1353-427f-3b91-89b1-a23b11165b31 | -2.7401 | -49.3927 | 2025-10-17 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| b0fa8cb2-cb55-3fc4-96d6-3cd7a6fd50b9 | -12.9368 | -47.1275 | 2025-10-17 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 10a720b1-1abb-3f3e-ba46-0e54d0d443a8 | -8.1149 | -45.5622 | 2025-10-17 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ea899828-434f-318e-86a4-b9b824481a47 | -10.2745 | -44.0481 | 2025-10-17 00:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 719199ab-5d7f-3521-8bd9-1d71bd54e1c6 | -10.5132 | -43.4289 | 2025-10-17 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0aa9c5e8-1919-3f71-a801-332eaf0e172c | -11.5729 | -44.0501 | 2025-10-17 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 220cd666-55e9-33bb-a436-05a629b038d1 | -10.4949 | -43.3842 | 2025-10-17 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 6fffedde-d92e-35b9-bc8c-e65131834bc0 | -2.7401 | -49.3715 | 2025-10-17 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| f7f97585-4259-3a40-8414-f69abe6030af | -4.3874 | -43.3827 | 2025-10-17 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e4ea5e81-c715-3697-b52f-2d5dd71f12e0 | -4.9548 | -44.956 | 2025-10-17 00:20:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2af75222-6ab0-3c71-9be3-81be5928fc38 | -9.0821 | -48.0252 | 2025-10-17 00:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 8bdc2a6b-7268-3585-9a9d-3cb81e865177 | -11.5917 | -44.0707 | 2025-10-17 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 7c963603-1066-3abf-8917-adfb58416055 | -10.2939 | -44.0221 | 2025-10-17 00:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 95761921-94a3-390d-95a5-1036dc23153c | -10.4945 | -43.4079 | 2025-10-17 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 5114a42d-af06-363e-8cc9-91840133c027 | -7.9442 | -44.115 | 2025-10-17 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 1b9b4199-f53f-3cb5-b235-b542f81b37c3 | -3.5028 | -52.4734 | 2025-10-17 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 48115e53-6c59-32ea-9d8a-458b3c68e897 | -3.5028 | -52.4938 | 2025-10-17 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 264.7 |
| ed8968b9-38d0-32eb-a623-e8317457282f | -8.1337 | -45.5603 | 2025-10-17 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 8b557809-5aa3-322a-966a-672d89ce577c | -4.4248 | -43.3805 | 2025-10-17 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 169.4 |
| d05a0ca0-9963-37e3-aa15-5f5217b10ddb | -2.7586 | -49.371 | 2025-10-17 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 75ca40d1-543b-39c3-8c6b-c7f5a72d48c0 | -18.0898 | -42.4475 | 2025-10-17 00:20:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| 2dcb90e1-8417-37b5-89fc-b45c0c164f73 | -4.3872 | -43.406 | 2025-10-17 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 207.2 |
| 70e63652-a57f-34bd-b2d2-422fb775cf4c | -9.7302 | -48.9183 | 2025-10-17 00:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 986d9500-8046-3869-842e-ecffb47123c4 | -10.534 | -49.5471 | 2025-10-17 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9271e918-cdb3-3ccb-a6c1-5d95e537bc5e | -10.2748 | -44.0247 | 2025-10-17 00:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 00e38ff6-6f05-3763-b127-8a62b4e9075e | -10.2745 | -44.0481 | 2025-10-17 00:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 157.9 |
| a3899007-c0c1-33db-9111-de007ce75799 | -3.2545 | -45.9855 | 2025-10-17 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 06c1fffc-35f6-3e75-ac59-e87c22b4ee5d | -10.5132 | -43.4289 | 2025-10-17 00:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| feec39cf-3079-3752-ac98-a639d0974163 | -10.5837 | -47.3978 | 2025-10-17 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| cd7c7286-6351-3007-8754-f5addda6608e | -8.1996 | -43.3189 | 2025-10-17 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| e8058dae-7027-366e-99f8-4cf86de291a3 | -11.398 | -44.1933 | 2025-10-17 00:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 492c25c9-d7a5-3081-8eea-35a4113c3b6e | -4.3872 | -43.406 | 2025-10-17 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 5ef4583c-4554-3078-8b25-83b1ed4bd6ce | -11.5733 | -48.5568 | 2025-10-17 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| f0196f9e-992d-3a4b-bcd4-29d9e7097cb3 | -4.484 | -42.9335 | 2025-10-17 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 31a78a0c-fea3-31df-b3c1-b60a8f69c6ca | -7.9442 | -44.115 | 2025-10-17 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| ae7b8522-7f06-39c5-8a16-23464c9b7926 | -10.514 | -43.3815 | 2025-10-17 00:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 025975ef-0f95-3d9d-8c68-273bb9c51570 | -10.5136 | -43.4052 | 2025-10-17 00:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 0659e2aa-ed37-3371-a26a-93f50a8bbd4e | -16.0125 | -43.4996 | 2025-10-17 00:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e0ee88c4-8bbf-3946-8ecf-012925f04d43 | -14.3223 | -51.4689 | 2025-10-17 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| e4bbbb40-cf42-32b0-bf55-7305f9940136 | -10.4941 | -43.4315 | 2025-10-17 00:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 2139314e-aebd-35b7-81ba-fdf5ae7baa1a | -7.9631 | -44.113 | 2025-10-17 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 692e317a-12bd-3d68-9a17-8d0851c721e0 | -4.4248 | -43.3805 | 2025-10-17 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 168.6 |
| ab3725f3-229d-3f23-9c51-3b45e806f46f | -10.1528 | -44.5289 | 2025-10-17 00:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8186ad00-1027-3c8b-8c20-0cb08c251e72 | -2.7401 | -49.3927 | 2025-10-17 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 6882c891-92df-334f-8bc1-d0fa11c4188a | -3.5028 | -52.4734 | 2025-10-17 00:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ea1fbd02-3e06-37df-8695-9085a9d407a5 | -4.4245 | -43.4271 | 2025-10-17 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 72cf8814-2cc4-3478-bd30-2e0931329328 | -3.5028 | -52.4938 | 2025-10-17 00:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| c9ac2a09-d94b-3d2a-9c8b-bd8d39f90ed6 | -11.4773 | -44.041 | 2025-10-17 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| cb2351de-582d-30bc-8e1d-e4974f601971 | -9.879 | -47.6779 | 2025-10-17 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 6f1220fe-301d-333c-a16a-c5d9cadd2dc1 | -3.236 | -45.9639 | 2025-10-17 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 287.0 |
| ff49648c-395e-351b-bd60-b4558bb2ad5f | -10.5644 | -47.4223 | 2025-10-17 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 5968800b-411f-3b22-a3c7-8dd3f0dc178a | -4.4058 | -43.4282 | 2025-10-17 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 6440da27-dd9b-3ec7-92cd-938703fa6bdd | -4.4059 | -43.4049 | 2025-10-17 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 637.1 |
| 8de251e5-da0f-31d8-aa15-52933149ef11 | -3.5212 | -52.4932 | 2025-10-17 00:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| d7d48d10-5f08-333e-8c3d-01963205ef8b | -16.0324 | -43.4953 | 2025-10-17 00:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 8b67a101-d1ff-3aa1-b714-91c469ffd993 | -11.4939 | -44.179 | 2025-10-17 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c9cc50db-c8ff-32c4-9fc8-956539b45d9c | -2.7401 | -49.3715 | 2025-10-17 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 1e1ff155-b4e4-3440-868e-518d6d5e733f | -4.3871 | -43.4292 | 2025-10-17 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 4195d9ac-313a-3ad9-8241-466bba33f6a9 | -10.5641 | -47.4445 | 2025-10-17 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 21e6cb62-60df-3508-89fe-0d116e28d504 | -8.3885 | -46.2782 | 2025-10-17 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| cfa25615-be7d-37fd-902b-72ef892bb1ad | -3.2546 | -45.9632 | 2025-10-17 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 4086a397-e3b6-32dd-9528-2b00b3b0b57b | -2.7441 | -48.3022 | 2025-10-17 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 41a23a88-4d97-334a-b6e5-e71d85cc51db | -7.1949 | -45.4899 | 2025-10-17 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| f7899880-6a37-3290-9ff6-3ac948976873 | -4.4061 | -43.3816 | 2025-10-17 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 286.2 |
| baf8ab5d-d0bb-389b-b8ab-3b15f5f2c558 | -11.5921 | -44.0472 | 2025-10-17 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 1223fd86-d4f6-3573-945f-5a4f7254e674 | -10.2935 | -44.0455 | 2025-10-17 00:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 146.9 |
| a365023e-de82-3875-be40-e9e6bbf02810 | -8.3887 | -46.2557 | 2025-10-17 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 71b004cf-35f3-3d2e-bfc6-095c87dc2401 | -11.5729 | -44.0501 | 2025-10-17 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a737ee3e-b5fb-3073-9d00-63ebfd93dca9 | -10.534 | -49.5471 | 2025-10-17 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 93ab5e37-5db5-3f20-8044-1c7698d2414c | -10.2748 | -44.0247 | 2025-10-17 00:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 03ebf44f-ba11-3ddf-bc39-5d6f190c3345 | -11.5917 | -44.0707 | 2025-10-17 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a05b473b-0d5b-3b9c-800a-55e1934bb880 | -11.4581 | -44.0439 | 2025-10-17 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |


[Clique aqui para ver as próximas entradas](README14.md)
