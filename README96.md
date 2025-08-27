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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfebc796-7cb7-39ed-81a2-02a97b6c59f2 | -8.1587 | -45.0579 | 2025-08-27 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| e669c4c9-4e5a-3bcc-86ea-7632c58aa81a | -7.4734 | -61.4037 | 2025-08-27 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 7c1c2ea0-07a1-3a31-bbda-cc9cf754f9e7 | -8.459 | -43.7113 | 2025-08-27 14:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 881dce2e-61f7-333d-87f2-512fd27e0847 | -5.663 | -45.136 | 2025-08-27 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9164d73c-15f0-353f-bb18-fe41fa23cbce | -8.4596 | -43.6645 | 2025-08-27 14:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 209.0 |
| f6e362ad-531e-36dd-8b8f-cf83bf2a05fe | -9.1007 | -49.5835 | 2025-08-27 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 159.9 |
| ee7f94ea-f18f-3671-a6fc-776f6be69723 | -13.0674 | -46.3153 | 2025-08-27 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 56cdacb1-9d83-3b7a-92fa-155d83ddbcc9 | -7.7359 | -51.1379 | 2025-08-27 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 06847b93-c810-304f-8a5d-9bc36082aa12 | -9.4062 | -60.5326 | 2025-08-27 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| c0402fa4-bab0-35ba-a745-c110f62b40b7 | -8.2707 | -45.1377 | 2025-08-27 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 470af6b5-c686-3cde-828c-f729b3ed0447 | -13.3843 | -46.879 | 2025-08-27 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 0c46d308-9e6e-3ed4-b87c-e89bfebd2cae | -9.8286 | -64.2824 | 2025-08-27 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| bdb58303-a391-34f7-8366-66b60bd2f5c7 | -7.5673 | -47.4851 | 2025-08-27 14:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b3bff6d3-2651-3fc0-82e1-71393b6d38d9 | -12.7067 | -48.1873 | 2025-08-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| f9d12969-fa09-38b1-847f-05235df01819 | -9.418 | -48.2756 | 2025-08-27 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 806b030a-8d4f-3e74-8018-f521f7a95054 | -8.271 | -45.1149 | 2025-08-27 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 496eadd0-f6a2-35c6-820e-69fb5f17f385 | -9.0821 | -49.5638 | 2025-08-27 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 6b3f17a6-a1ca-338c-8715-a199445d04b0 | -10.2743 | -64.4907 | 2025-08-27 14:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| a568c92c-ac06-3ad6-b4b9-b868e02071bf | -9.0819 | -49.5853 | 2025-08-27 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 6bc0ba9c-4e9b-3d7c-a0dc-32bdbd83701b | -9.4064 | -60.5133 | 2025-08-27 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| a6726f1a-35ba-327f-92b2-cec7a7bcae8f | -7.6414 | -42.6718 | 2025-08-27 14:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 176.3 |
| 35e4f729-1096-3182-ba8a-e93f4bf94813 | -12.7643 | -48.1792 | 2025-08-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 151a3454-e754-3bbf-a1aa-01a643e15475 | -6.4355 | -44.5764 | 2025-08-27 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 321.3 |
| 6e06d869-f686-3c05-ad21-422d0501ac08 | -9.6574 | -64.9845 | 2025-08-27 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.3 |
| bae51c2e-08cf-3ed0-bfb9-6c065a97d335 | -8.8842 | -60.7507 | 2025-08-27 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 200.6 |
| 3933dbea-6e89-38dd-b84f-c16994800f2d | -11.5694 | -47.6081 | 2025-08-27 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a4e122cf-2f2d-3067-b66a-19cfda124328 | -11.3146 | -43.5008 | 2025-08-27 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.0 |
| ff7dde40-2d05-38fb-b5a8-2d1f9e15bae1 | -12.804 | -48.1072 | 2025-08-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 45472ee2-037c-38da-9b5d-439fc44b263c | -9.2092 | -59.4997 | 2025-08-27 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| c21c32c8-c4f5-3abb-a142-ba7a80ccfe80 | -12.9266 | -44.6314 | 2025-08-27 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 6de1b3d8-e417-3fa3-b38c-15d5a53f995f | -10.2742 | -64.5096 | 2025-08-27 14:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 6200aa27-64f9-3e08-959b-5908fb9a05b0 | -6.1783 | -44.0457 | 2025-08-27 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| ed6b0aec-e323-3a90-9d54-de25c87acb19 | -6.6201 | -53.3169 | 2025-08-27 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| cbbf2469-b004-3106-8f56-822bc59eba61 | -13.067 | -46.3382 | 2025-08-27 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5c75db84-1d54-3a22-b33e-5d666b9ac7e1 | -12.7843 | -48.1321 | 2025-08-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c0a33fc2-422d-3a84-a18e-e1679666f7e2 | -10.786 | -60.7848 | 2025-08-27 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| a0c98c31-995a-3f47-ad65-12f5c0cce1ff | -8.8839 | -60.7891 | 2025-08-27 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 50cb0985-0b95-3e68-bc43-b96eb1b86eca | -12.7447 | -48.2041 | 2025-08-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b5d9b72f-986f-3221-88a6-8f6846c9f1b5 | -8.4593 | -43.6879 | 2025-08-27 14:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 400.8 |
| 5e82042f-add2-3176-8da5-50b26efbb91e | -6.4357 | -44.5535 | 2025-08-27 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 545424c2-c87b-3c69-80f3-a066b13ae29e | -11.9208 | -47.1375 | 2025-08-27 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 3216912a-102f-34a0-91ad-70d28c6e0b47 | -15.6171 | -52.7207 | 2025-08-27 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b8be37c3-de8c-3e1e-93eb-1ca56f026281 | -12.7259 | -48.1846 | 2025-08-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 96b292f5-31de-3712-adf8-ad0dfae5d65b | -13.6097 | -48.2126 | 2025-08-27 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 172.0 |
| ae6e06bc-8a93-3625-820a-70f9b6c070b2 | -6.4543 | -44.5749 | 2025-08-27 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| a2dc8e94-7673-31d8-bd84-3a6a7215408a | -12.8036 | -48.1294 | 2025-08-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 76408362-6a48-3003-8354-db166936b210 | -11.3338 | -43.4979 | 2025-08-27 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 4c397307-202b-304a-a3a8-acacc0a87047 | -8.2522 | -45.1168 | 2025-08-27 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| c7d6bfaa-ba04-368d-93f0-3f6b514858ec | -8.9026 | -60.769 | 2025-08-27 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e3090704-0964-3e26-b914-a0b1a29bf05c | -9.0816 | -49.6068 | 2025-08-27 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 8424787d-6d30-3195-96b6-1d239c7c8a91 | -13.6291 | -48.2097 | 2025-08-27 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| bb3d7772-6560-3766-a49b-39067f38eb66 | -13.4036 | -46.876 | 2025-08-27 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d42cea87-add6-3627-9280-c5c50829452b | -13.4032 | -46.8987 | 2025-08-27 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 05f9d57c-5f12-32a0-8c33-624c2c573679 | -8.8841 | -60.7699 | 2025-08-27 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 424.8 |
| 9f9daa57-daab-30d2-8397-20f8eb260bdb | -10.8698 | -47.3186 | 2025-08-27 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 3c95c04f-7199-37e1-84ec-5c483f95a262 | -11.1583 | -44.7859 | 2025-08-27 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| f4b1f217-afcf-3c20-809b-f55b02685102 | -7.6411 | -42.6955 | 2025-08-27 14:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 185.8 |
| abc46f57-59a1-3f26-857e-532b8a6215bc | -11.2505 | -44.9808 | 2025-08-27 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| cbfbb2b7-9694-3aa5-b8ea-c13a1adf09f8 | -6.8774 | -43.5919 | 2025-08-27 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 357.3 |
| 35d35ec2-3f5d-364a-9960-4ee9a20fd030 | -8.2519 | -45.1396 | 2025-08-27 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 417aec1e-4612-3427-b158-bb205965ac2d | -7.4414 | -42.0501 | 2025-08-27 14:00:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 130.2 |
| df89cbf3-44e8-3bed-a82e-fc59d06ae981 | -17.8471 | -47.7428 | 2025-08-27 14:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| db3fdd99-27e9-3ed7-b014-1ead75afd2d2 | -9.1004 | -49.605 | 2025-08-27 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 5c53eda7-d6c5-3d34-9ad5-fdf4655b1010 | -6.4353 | -44.5993 | 2025-08-27 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 5993c308-bcd6-30e1-8b25-2a5ef813556a | -12.784 | -48.1543 | 2025-08-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 187e962d-be9c-3060-96d6-e1af1d4e3fcc | -12.7263 | -48.1624 | 2025-08-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| ae8e3833-74b5-3160-9301-74c3fc5be726 | -8.4596 | -43.6645 | 2025-08-27 14:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 201.9 |
| 2ce05c03-8b36-3c41-a1ee-1712c59071f1 | -9.1715 | -59.5599 | 2025-08-27 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 690f1b14-d22c-3c03-8069-fde639cd5df9 | -9.4064 | -60.5133 | 2025-08-27 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 5d76b903-22b6-3727-946a-69240d37fc62 | -12.784 | -48.1543 | 2025-08-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| bc7037df-9598-3d41-8e49-0a590e815972 | -13.6097 | -48.2126 | 2025-08-27 14:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 29aefacb-a0b4-3807-952f-42bbd0d9956b | -9.9352 | -46.38 | 2025-08-27 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| fb899802-c4fe-37e8-ad64-8b69178fae58 | -11.2505 | -44.9808 | 2025-08-27 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| e675a6ed-f9de-3d70-9a45-0dee15b70f07 | -8.8839 | -60.7891 | 2025-08-27 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 2911a4fb-9940-3d09-a714-ed9f9099bff8 | -13.067 | -46.3382 | 2025-08-27 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 3a5a758f-ad42-3e87-950f-6f002ebdfaa1 | -15.6171 | -52.7207 | 2025-08-27 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| a5e26f98-da76-3f24-bc49-7e184ae06ed1 | -7.6414 | -42.6718 | 2025-08-27 14:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 143.0 |
| 410f9f6b-bcfd-35f5-bf3e-e4de319f00d2 | -12.7643 | -48.1792 | 2025-08-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 7dc534a2-ee47-359d-84f9-eaf79d6dd94a | -9.4062 | -60.5326 | 2025-08-27 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| b13ddd97-d1fb-3517-9259-169c59e4da16 | -7.4414 | -42.0501 | 2025-08-27 14:10:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 114.1 |
| 6fb02888-7e48-3b1e-811c-eef670cd527f | -6.4355 | -44.5764 | 2025-08-27 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 224.6 |
| fd257ba0-a38c-3d09-a9ac-61a8159d87b3 | -11.3342 | -43.4742 | 2025-08-27 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 6ac4ee6b-c9d9-390b-be04-1f4ef21263a3 | -17.8471 | -47.7428 | 2025-08-27 14:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 2dbb179c-c44c-3be9-97d1-db7a369a0b0d | -6.1783 | -44.0457 | 2025-08-27 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 97cd7a1e-13f1-3d71-9d57-75995620f783 | -15.0975 | -48.4029 | 2025-08-27 14:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 5b59efdd-58ca-3b57-ad35-f0d772c92c0c | -7.6411 | -42.6955 | 2025-08-27 14:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| 31de0a19-f1a9-3e04-a373-816343ac7f4e | -10.2742 | -64.5096 | 2025-08-27 14:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 98.3 |
| e53b7d71-be89-334f-9263-c06e0ee99b4d | -5.7887 | -43.6134 | 2025-08-27 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 72c65215-24f3-3139-ac60-b1462a8550f8 | -9.1007 | -49.5835 | 2025-08-27 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 02f7478d-8acf-399c-9ec7-9b9d97b165d3 | -6.8413 | -58.9552 | 2025-08-27 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 105311c0-27cb-3cfb-8498-a78909bda5bd | -9.8286 | -64.2824 | 2025-08-27 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 99ac43dc-eda5-3b75-b556-dfa7a0b9c7b7 | -6.4357 | -44.5535 | 2025-08-27 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 4e7667ae-adc9-3e2f-ae45-b6f01db6ea7a | -6.4353 | -44.5993 | 2025-08-27 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 9b91858b-e250-3467-835e-71d17260af6f | -12.7263 | -48.1624 | 2025-08-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 35a6bb6b-18df-3c71-a050-d74bf76b0b53 | -9.0819 | -49.5853 | 2025-08-27 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 215d1b56-d749-3cc4-be4c-ed4b0dfc63dd | -13.0674 | -46.3153 | 2025-08-27 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b64d6ec8-b845-3817-a4dc-9b9a1fbe056b | -8.2519 | -45.1396 | 2025-08-27 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 0317fade-fa77-37ef-983a-aa0820dbedd5 | -8.2522 | -45.1168 | 2025-08-27 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 6f31ed0c-dee6-3c88-a0db-0d0abc86606e | -8.8841 | -60.7699 | 2025-08-27 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 354.8 |
| 01b1d0ab-196d-3213-8a52-b651aca69777 | -12.7447 | -48.2041 | 2025-08-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |


[Clique aqui para ver as próximas entradas](README97.md)
