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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33a9a0a4-654a-3a55-9b2a-4588277aea97 | -8.5554 | -66.9945 | 2026-10-01 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 3d100120-eaea-37c0-a66d-2baabd282892 | -5.7376 | -45.1533 | 2026-10-01 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| c68a1cbb-345e-3717-a4ee-f5a493b555df | -3.1838 | -54.104 | 2026-10-01 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| c72bda76-fd6a-32e9-bd7a-78931ce5b91e | -9.1408 | -64.3836 | 2026-10-01 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 513904b3-d9c8-3d4f-b717-8ead42245e39 | -3.1655 | -54.0844 | 2026-10-01 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 190.2 |
| af0a25c5-4585-3a06-897f-bb7cde26c9c5 | -5.9993 | -49.566 | 2026-10-01 02:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 06799058-2c33-3675-aa8a-e1068f3cfe36 | -6.1299 | -47.2884 | 2026-10-01 02:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 9a8122a4-c15e-3ebb-8e34-1632b9c6140e | -4.4506 | -47.9329 | 2026-10-01 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b237356d-b5de-313b-b0c3-3cbdfc0e2d42 | -8.6497 | -62.6672 | 2026-10-01 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f5cb34ed-537d-3fde-a530-0b3e519d8dca | -10.7664 | -50.5299 | 2026-10-01 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 6a46404a-17b5-3970-88fa-438d1705de2c | -5.1252 | -56.0143 | 2026-10-01 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 33031985-082e-37a3-8a58-251504593445 | -3.1656 | -54.0643 | 2026-10-01 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 19fc5434-9841-303d-8cf0-624bcbeedea3 | -8.5553 | -67.013 | 2026-10-01 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| e959c944-4f2d-3ce3-95d4-0f8b160df59f | -2.908 | -54.151 | 2026-10-01 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 821a0625-0bcb-39a1-8628-c5dda472806a | -11.79 | -50.5 | 2026-10-01 02:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b27a8ef2-7075-3f21-a9ed-0f55eadaa8dd | -11.41 | -43.39 | 2026-10-01 02:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c29b58de-6308-3b5a-9c72-8771ace4603d | -3.17 | -54.12 | 2026-10-01 02:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a68980b-64d0-3d4a-b8cc-18077715174e | -11.45 | -43.49 | 2026-10-01 02:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ca7cca2-007b-3b34-ba24-f89782b97fed | -4.26 | -50.75 | 2026-10-01 02:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcfef007-ee5c-342d-b6e5-bdeaad70a428 | -4.29 | -50.76 | 2026-10-01 02:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14f38815-336c-3364-9ef6-dbec59a79e84 | -4.26 | -50.81 | 2026-10-01 02:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2566236e-c29d-35cc-87c0-5cc39330994b | -4.29 | -50.81 | 2026-10-01 02:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1829029-d0c3-35f5-be31-ff9011659453 | -11.44 | -43.4 | 2026-10-01 02:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9835a47-bdbb-323d-a71c-386064154450 | -11.42 | -43.43 | 2026-10-01 02:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eeb1abda-5b7a-38f3-8a71-3095e3353c29 | -4.23 | -50.75 | 2026-10-01 02:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c5c311b-4aa4-3119-afe0-866f70360d82 | -11.45 | -43.44 | 2026-10-01 02:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3701ccf2-c358-3d48-9fe9-a1be15ce09f5 | -5.7542 | -43.2901 | 2026-10-01 02:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 67fafeda-6c54-325e-84f5-6a64fc5e2684 | -8.5738 | -66.994 | 2026-10-01 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 2db2415c-f786-3e1a-9ce2-6647b75567e0 | -13.1156 | -51.2193 | 2026-10-01 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 48701f92-5aa6-378d-a164-d75e59605089 | 3.2742 | -60.6105 | 2026-10-01 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 681e9d63-ae02-359a-b501-7bcfb6abcf0a | -3.5808 | -51.4832 | 2026-10-01 02:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 973b9520-6d39-3064-869d-d827ec4d398e | -13.0584 | -51.205 | 2026-10-01 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| cc649744-9ba0-349e-be96-6769bafb4836 | -5.7355 | -43.2916 | 2026-10-01 02:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4a1adcb4-4182-3693-8e80-2960f6e10eb8 | -11.2087 | -45.1939 | 2026-10-01 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1c101ca7-98fc-37ef-8b7a-bf657e8986e5 | -3.106 | -50.2896 | 2026-10-01 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| b8c67bd9-2a81-3b36-b4a2-47aac5204505 | -3.295 | -53.8597 | 2026-10-01 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| a53e4e51-d18b-3606-b222-2bd2fc3ba2d8 | -8.5554 | -66.9945 | 2026-10-01 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 166.4 |
| e243bece-cf95-336c-a064-857e2a12edb3 | -3.1655 | -54.1045 | 2026-10-01 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 197.4 |
| 95b5b79a-c001-3767-965e-930aed7be1dc | -4.4507 | -47.9112 | 2026-10-01 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 22bbf181-c2b5-3caf-b6a9-36c5e1bc5ef5 | -6.0179 | -49.5648 | 2026-10-01 02:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| aa091e30-4b48-3085-bfaa-436d7f7b251a | -10.7664 | -50.5299 | 2026-10-01 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| d5cff898-57da-3f47-ac3f-c0a86acdc2df | -13.0968 | -51.2003 | 2026-10-01 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 50d2e389-838d-3834-b718-ba2feb4d9732 | -3.1838 | -54.104 | 2026-10-01 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 1f895a9a-0aac-30e8-89ce-d314b99e0f10 | -11.8291 | -50.4977 | 2026-10-01 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 928cb1d1-edc7-35fd-8cd9-b08828bf1e3c | -11.8287 | -50.5192 | 2026-10-01 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 8c940ba8-5948-3f6b-a324-a58c31c976dd | -12.1857 | -48.4345 | 2026-10-01 02:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| e11d8c7d-7ef8-397f-b015-2301b7c1219e | -11.8478 | -50.517 | 2026-10-01 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 6e77cf10-0108-3e07-b304-b4e0c5d9bac9 | -9.1222 | -64.3843 | 2026-10-01 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 129.1 |
| c17a021b-cf9d-3051-8388-7bdee199d230 | -5.7563 | -45.152 | 2026-10-01 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| a0e6789e-59bc-37bd-9c62-88ed818e91fc | -13.0964 | -51.2217 | 2026-10-01 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 2ef8b3f4-3b52-3ebb-9170-62dcbf685fa9 | 3.2924 | -60.6101 | 2026-10-01 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.5 |
| a0a36397-f5de-3ef9-beb0-599fd691529d | -8.5369 | -66.9949 | 2026-10-01 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| d2072954-f7b3-3ea7-8c24-e39e08442bb3 | -4.4506 | -47.9329 | 2026-10-01 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| dbbe8c0f-4718-382c-8471-1717a487d4ca | -3.1839 | -54.0839 | 2026-10-01 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 9f041ff3-d2b5-3569-af9d-5393174b8b53 | -9.1223 | -64.3655 | 2026-10-01 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| f7a0df98-b642-3cda-85e0-556e18348308 | -3.1245 | -50.268 | 2026-10-01 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e89e2ad8-3ba6-31ba-bc03-eef83292f1e1 | -3.1655 | -54.0844 | 2026-10-01 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 192.1 |
| 9a6f918b-d66f-3a15-b8ad-44f01a94cbb8 | -11.81 | -50.4999 | 2026-10-01 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 8c6e33d3-70f3-3b6d-82c8-eff420fe82c2 | -8.5554 | -66.9759 | 2026-10-01 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 6aa2935a-4dfb-34f6-86aa-1f51298f9823 | -3.1245 | -50.289 | 2026-10-01 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3f654a59-f637-3bf1-8d97-6f32424c7887 | -9.1221 | -64.4031 | 2026-10-01 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 2e6d007c-ad09-3595-a078-fae0559215b8 | -8.5738 | -67.0125 | 2026-10-01 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1c560a7d-42a9-3cf7-b5e0-9aef4516e046 | -2.908 | -54.151 | 2026-10-01 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| df27f82d-340d-3de9-ab63-3a5b7767d298 | -5.7357 | -43.2682 | 2026-10-01 02:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| a2c8003d-ae65-3045-b2b8-4b07253272fe | -11.8097 | -50.5214 | 2026-10-01 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f23f47b7-621d-33fa-938f-e24a81e3f307 | -20.1886 | -47.397 | 2026-10-01 02:20:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 5c60e39c-6ca2-37d5-ab63-d96b125ff214 | -13.116 | -51.1979 | 2026-10-01 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 56729129-6383-3ca9-89db-f14235cc3e19 | -5.7376 | -45.1533 | 2026-10-01 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 2fcbc1ff-94fb-3949-a266-57b9338231ac | -10.7667 | -50.5086 | 2026-10-01 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| f272a3e4-8ee6-38b6-879b-4bf7d49a2850 | -5.9993 | -49.566 | 2026-10-01 02:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 80cf7264-8d30-3215-89db-7c21f22e7314 | -9.2054 | -45.8095 | 2026-10-01 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 23e3c3b7-5499-38be-8ce8-66bc500bf5df | -5.9993 | -49.566 | 2026-10-01 02:30:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1a597b0e-d19b-3cba-8de8-ec42d6c15a4e | -5.7563 | -45.152 | 2026-10-01 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 35312eda-6534-3b8a-9d00-6392946e87c5 | -9.1222 | -64.3843 | 2026-10-01 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 7d9fb847-a1f1-3212-8bd1-5f63a0d6808c | -9.2054 | -45.8095 | 2026-10-01 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 63b8fa51-6d8c-32a7-b4d8-25b00d4a04e1 | -9.2243 | -45.8074 | 2026-10-01 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| d65e36af-6e27-3ae8-94aa-96b173bb1051 | -3.1655 | -54.1045 | 2026-10-01 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 183.5 |
| 3ee2fbf9-a9e1-313f-8fae-0a3ac59434d6 | -12.1853 | -48.4565 | 2026-10-01 02:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| cbef972f-65e6-36bc-bb34-1bef3ad71baf | -11.8097 | -50.5214 | 2026-10-01 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 1abfa6c9-1a12-3e35-a951-135e24de89e6 | -3.5808 | -51.4832 | 2026-10-01 02:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 661ad781-cb6f-3896-8450-5dfb7661dd58 | -3.1838 | -54.104 | 2026-10-01 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 298c5c11-08e5-38ac-9cf2-52ff09e4be8f | -4.4507 | -47.9112 | 2026-10-01 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 10186a4b-53e7-3d99-8bef-0a26913d9e0d | -3.1655 | -54.0844 | 2026-10-01 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 173.7 |
| 607dc39b-a009-3256-99de-ba7651ad702b | -12.1857 | -48.4345 | 2026-10-01 02:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 0308748c-ec31-31e7-b3cb-b6055aec809a | -3.295 | -53.8597 | 2026-10-01 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 7166d5ce-ff05-319e-ae9f-e495bac953f6 | -13.1156 | -51.2193 | 2026-10-01 02:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 69a777d7-0cfa-3879-b644-9cb585f45eb5 | -9.2051 | -45.8322 | 2026-10-01 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 053efde8-55cc-3dd5-83e4-45123a85daaa | -3.1245 | -50.289 | 2026-10-01 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6e97d760-3498-3bbb-a29c-59d21b5e017c | 3.2742 | -60.6105 | 2026-10-01 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 5a325c6f-d353-315f-b128-50625bcaee84 | -11.4037 | -51.0148 | 2026-10-01 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 7f7b95e5-9ffc-3a0c-b0c5-818f3dc19071 | -6.0179 | -49.5648 | 2026-10-01 02:30:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 809d5e86-fe43-3449-9876-b5a7bfd37fb7 | -9.224 | -45.8301 | 2026-10-01 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| c41b4be1-e67f-3dd6-aa7c-9dc9fd911f6d | -11.8287 | -50.5192 | 2026-10-01 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 4727fc28-bf54-3795-a993-00cf4b769831 | -5.7355 | -43.2916 | 2026-10-01 02:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| d0c1783c-b4bd-338d-96f6-8e457e7e0f13 | 3.2924 | -60.6101 | 2026-10-01 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8974aab4-04af-36bb-bca0-21f6e99ec51c | -2.908 | -54.151 | 2026-10-01 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 96c1ea23-3b51-3870-9471-b9f7aba390d3 | -9.1221 | -64.4031 | 2026-10-01 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 9262865a-0c00-34f0-90c9-20ec56a4636f | -3.1471 | -54.0849 | 2026-10-01 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 5fec91f2-de59-3b03-ac5a-246e1be507b4 | -4.4506 | -47.9329 | 2026-10-01 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b9f7bf35-9ac6-357a-9127-269b764e8225 | -3.106 | -50.2896 | 2026-10-01 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |


[Clique aqui para ver as próximas entradas](README17.md)
