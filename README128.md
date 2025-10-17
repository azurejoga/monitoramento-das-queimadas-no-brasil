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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2266efdf-46ea-3200-9632-b2430bcbef28 | -12.0879 | -47.4277 | 2025-10-17 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 3ad5da5b-d0d3-3289-abdf-6bd0babceb81 | -7.8499 | -44.1246 | 2025-10-17 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e5ce2504-bbfd-3c87-95c8-022d2c3bdd5d | -12.1278 | -47.3329 | 2025-10-17 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 72761b6c-c562-3a5e-ad8b-c1b42c375533 | -7.7572 | -42.4696 | 2025-10-17 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 238.0 |
| 8cbdee5d-a7bb-34c2-8b79-60caeaefd9a9 | -13.8942 | -45.5378 | 2025-10-17 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 848d70cf-d730-39a0-bb29-1d442ee51e47 | -10.2939 | -44.0221 | 2025-10-17 14:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 356.7 |
| 00353066-c0e9-3d8f-96bf-ec66514afa28 | -5.4561 | -41.0054 | 2025-10-17 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 137.7 |
| de80ee4e-9a28-3a69-bfb9-2caae3d62a97 | -8.1993 | -43.3424 | 2025-10-17 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 366d5387-b6d7-3f7b-9ff1-c9f091ee5e6e | -12.487 | -45.4664 | 2025-10-17 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 06e82a75-1579-3d2c-8435-9617dfa7e581 | -12.7374 | -48.6247 | 2025-10-17 14:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c54f365f-9f96-32ad-956f-9f6c954ecd98 | -13.2451 | -47.1036 | 2025-10-17 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 7804c287-c7e0-3a98-b6ee-15c12c8671a1 | -12.1682 | -45.0539 | 2025-10-17 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| bbeceb70-f324-368d-b507-9969a0f56bb8 | -6.5898 | -44.15 | 2025-10-17 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| e255aa49-156a-34be-80ac-b95a0c016712 | -3.6318 | -41.7037 | 2025-10-17 14:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 13c1997f-6168-3cab-b766-bc9512ba8aec | -4.5733 | -43.511 | 2025-10-17 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 6073e2da-fcd7-39ab-a150-0ec1f6abafe9 | -10.514 | -43.3815 | 2025-10-17 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 44579330-72ec-3b7f-beef-930ec471869b | -8.2561 | -43.3361 | 2025-10-17 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 4464a15c-922f-39d2-a6a5-7f39218b11b3 | -13.4977 | -51.2992 | 2025-10-17 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| e42d9285-64e1-3b70-84dd-5288ff0b18d0 | -7.831 | -44.1266 | 2025-10-17 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| ac2b93fa-f719-367f-96ee-5cc19f8d801a | -6.2012 | -41.7389 | 2025-10-17 14:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 62adfff9-6831-3fe3-8ff1-d3bf3d4819bc | -5.8718 | -44.7801 | 2025-10-17 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 919fa8eb-7efc-3c8d-a037-e25bc9f76465 | -10.5132 | -43.4289 | 2025-10-17 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 36a82ac8-f8a6-369f-a310-ff3979fcdbd3 | -10.534 | -49.5471 | 2025-10-17 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 305b7994-ca27-31a0-be40-b49895a5e03d | -12.4678 | -45.4694 | 2025-10-17 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 0a5c2fe7-1ccc-3395-9d2e-1742fff5867e | -12.8308 | -44.6004 | 2025-10-17 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 60e725e9-b585-338c-ad39-7b2025268167 | -14.8851 | -52.438 | 2025-10-17 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| acf05d7b-0198-3699-9bb7-32170fa37ac9 | -11.3988 | -44.1464 | 2025-10-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| b446ea6d-17de-397b-9efd-e2c7939fabc5 | -12.9607 | -47.9294 | 2025-10-17 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| acabb036-3f5a-347e-8553-93afd1e5919e | -11.4188 | -44.0966 | 2025-10-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 6a5a6f1c-7908-3824-9f36-fb7f04ae5e09 | -12.284 | -47.1544 | 2025-10-17 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 25cedcad-005a-3ad0-9b14-5357b1c4e926 | -10.9942 | -47.8797 | 2025-10-17 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 8f4e4c9d-6541-316d-aba2-d573838f0e43 | -10.9376 | -45.4375 | 2025-10-17 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 694795ab-b046-3e2e-9273-05590cb9cb75 | -6.4114 | -45.1253 | 2025-10-17 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 16ec4073-5d38-3c96-ba63-a8e1a816980b | -3.9822 | -42.4924 | 2025-10-17 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 141.4 |
| 239fb439-df04-3a7d-8f38-d29f882ed3d8 | -14.8657 | -52.4405 | 2025-10-17 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| f592679d-3bad-340e-949c-3537eb400e76 | -12.1678 | -45.0771 | 2025-10-17 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| bbe95ea6-0fe7-313e-8ad6-0e4cb65f611a | -12.9265 | -41.8118 | 2025-10-17 14:30:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 296.4 |
| 867fcb84-9a1d-3dee-9a6f-06c9715491a6 | -8.2371 | -43.3382 | 2025-10-17 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| f88e2e76-d3ea-3a8c-b2cf-d54b87fc732f | -11.5921 | -44.0472 | 2025-10-17 14:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 2103a826-b187-3aaa-be87-bcd41552d7e3 | -14.8854 | -52.4167 | 2025-10-17 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 822f8e13-bf3d-3a9e-af91-40054144e796 | -12.5342 | -48.1889 | 2025-10-17 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| e8d03279-43d4-3587-a6d8-d05d9313c4ca | -11.4581 | -44.0439 | 2025-10-17 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 29850abe-c811-3f13-a732-122848965d9e | -11.5724 | -44.0736 | 2025-10-17 14:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| dd2527d3-f85b-388c-b42d-e27c6d15d7d3 | -8.1807 | -43.321 | 2025-10-17 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| e9de5a98-2455-3c2c-8fe0-a0ac3dd766e3 | -10.6028 | -47.3955 | 2025-10-17 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 9181f51c-894d-34bd-9515-cb633e073e14 | -9.879 | -47.6779 | 2025-10-17 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 57240029-1f39-30de-8903-424064057693 | -9.898 | -47.6758 | 2025-10-17 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 295b1e7e-0a5c-3370-86b8-e504e38c886f | -5.2674 | -43.2561 | 2025-10-17 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| dccbf9c2-f515-3d4c-9855-9b38dfdf1ed7 | -7.0238 | -45.7077 | 2025-10-17 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 99cbc073-9874-392d-bcf2-7fd050644253 | -6.1737 | -42.5985 | 2025-10-17 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| b14b1803-472b-3da0-8e6e-1dd400b26ca0 | -9.9828 | -47.0234 | 2025-10-17 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 311.1 |
| 86910092-33b3-3cb5-b6b4-1118aa388d3f | -9.6807 | -45.6417 | 2025-10-17 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a72ab349-d531-30cb-959f-7a57e75b402c | -9.6389 | -45.9186 | 2025-10-17 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a7e8c7fb-ccd0-3671-99af-064ce5a65f34 | -14.866 | -52.4193 | 2025-10-17 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a61e0fc8-0f96-3e74-a5ae-a5339ba16915 | -9.7165 | -44.4917 | 2025-10-17 14:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6ae57481-526c-3618-a03c-19ca3074d4da | -6.3544 | -41.4846 | 2025-10-17 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 84746bd3-1ad9-366c-8563-3fef763ae8e2 | -4.1525 | -42.1989 | 2025-10-17 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 131.0 |
| 22e636bf-7722-3b3b-b5b6-396e3d00e2d7 | -10.8797 | -47.9157 | 2025-10-17 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| fe57ac88-88a4-3400-947f-6e2093a626b1 | -9.9831 | -47.0011 | 2025-10-17 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 8bef8b96-5307-31ca-aae7-0bc1c372ba53 | -6.411 | -41.4793 | 2025-10-17 14:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 6621cde1-48f4-3483-accd-996222c24ac0 | -12.9459 | -41.8082 | 2025-10-17 14:30:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 151.8 |
| 5cd766f6-4fcf-37ee-9ddf-2d71b7b99888 | -10.2748 | -44.0247 | 2025-10-17 14:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 98dcc5f3-cf55-3952-b44f-6623e21829f2 | -8.1618 | -43.323 | 2025-10-17 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 9006383c-6f3c-363b-b667-95126cfbf2c8 | -11.8763 | -49.8903 | 2025-10-17 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 4a032292-952b-3629-871d-63704e36c0f3 | -5.7992 | -42.4876 | 2025-10-17 14:30:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| f128af27-c50e-3955-a42e-282c616a1ebf | -7.1086 | -44.7931 | 2025-10-17 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 55428940-089b-36b6-950b-62a7d26f1689 | -10.8101 | -43.9275 | 2025-10-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 391e39db-f09b-3347-bea9-c3b6f21468bf | -8.2747 | -43.3575 | 2025-10-17 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 5ecef1e5-12e4-3ca6-93f8-1533fae9f7ac | -13.477 | -48.0989 | 2025-10-17 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| e8c93088-8030-3610-92dd-7b14a6360b17 | -4.4248 | -43.3805 | 2025-10-17 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 4ffb094e-c2e2-372e-a078-eb4aa464ae71 | -14.1754 | -47.9252 | 2025-10-17 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 170.0 |
| ee089f47-d3ee-36e1-bbcc-706610656e48 | -14.1944 | -47.9446 | 2025-10-17 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1b89384b-40c3-3fc3-899f-090af2b4c543 | -3.9635 | -42.4934 | 2025-10-17 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| ee6148c7-9491-3f50-a674-44728a57fa80 | -7.8307 | -44.1497 | 2025-10-17 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f4978477-e0f1-3f0c-829c-21a242b5403d | -10.1063 | -47.6525 | 2025-10-17 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 908c4e45-fbf1-3ada-b6f1-37bef1e854a9 | -5.9251 | -43.0662 | 2025-10-17 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 200.5 |
| 8e1c9f52-7f2d-34c8-9229-5e8dd899699e | -4.4061 | -43.3816 | 2025-10-17 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| b736a5c8-7885-3637-9da1-a7892a0655b1 | -11.3992 | -44.1229 | 2025-10-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 166.6 |
| cf306091-a9c3-32f0-8540-acae14fe4e94 | -10.5136 | -43.4052 | 2025-10-17 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 0ad55168-2fa2-3493-afff-57d062638058 | -11.4184 | -44.1201 | 2025-10-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 4931d380-fff2-3d20-85a2-c3419ae77a3e | -8.293 | -43.4024 | 2025-10-17 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 165.4 |
| 2e2bf0b9-bf58-3f40-9b84-c5024bde4f36 | -11.4585 | -44.0204 | 2025-10-17 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| dbc71abf-e4d1-3d3c-ad63-7d9687699a42 | -4.4446 | -43.2164 | 2025-10-17 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 1e73f0b9-9283-33e3-9b80-d95d55946a28 | -3.7628 | -41.6967 | 2025-10-17 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 8ae340a4-4368-3ec3-8522-f0e144e1174f | -10.9748 | -47.9042 | 2025-10-17 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d2e143c0-224f-3cbd-a3be-77329152c968 | -4.1338 | -42.2 | 2025-10-17 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| da6e47ed-4577-3254-b30f-a83e08b06ecc | -11.3603 | -45.2646 | 2025-10-17 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 31c7aaaf-f22f-3690-aec0-d75fbbe1e9a6 | -10.1517 | -44.5984 | 2025-10-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 48bf1062-e840-309d-8d73-ea1dbf880590 | -7.1086 | -44.7931 | 2025-10-17 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 4fcf5c4e-fde3-340d-8953-96d08fde85b8 | -12.4264 | -51.3027 | 2025-10-17 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8334e69d-93c1-3116-ae37-7be03fb5feb7 | -5.7992 | -42.4876 | 2025-10-17 14:40:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 46c3b211-eaa0-32c3-96e7-1037b1157c4e | -14.8854 | -52.4167 | 2025-10-17 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 1b70edf5-eaef-325c-bf4c-99550ce7e713 | -11.496 | -44.0617 | 2025-10-17 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| dccbf61e-0cb3-38c3-826b-5d3139c5cc3a | -8.5233 | -44.5614 | 2025-10-17 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 895e0d01-227e-306a-a8ec-1e6459330cac | -9.7165 | -44.4917 | 2025-10-17 14:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 95264a43-b3c5-3e1d-8cbc-0bd4932fac07 | -10.1528 | -44.5289 | 2025-10-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 3b50474b-88ad-3c8d-b488-d693c3fb9d6a | -6.3878 | -41.8899 | 2025-10-17 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| ae2143ec-7f1c-32f7-a7dc-9264f148b83a | -10.9228 | -47.5786 | 2025-10-17 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c72b7684-493b-3ea7-9299-fd2585bc1f5d | -10.6024 | -47.4178 | 2025-10-17 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| ae51d8ee-357b-34dd-a8d2-55073b602689 | -12.284 | -47.1544 | 2025-10-17 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |


[Clique aqui para ver as próximas entradas](README129.md)
