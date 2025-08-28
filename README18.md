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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27bf7ba6-3aa3-385b-b2ed-990c20170ecb | -11.3275 | -43.52124 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c996461a-1057-3de7-b730-456066cea489 | -12.96122 | -44.57599 | 2025-08-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c8a4885e-db34-33ff-83aa-b46b08385adb | -11.31587 | -43.53773 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65d4e4e3-ce70-3d7b-a5b7-7c7af895e2d7 | -11.32224 | -43.54617 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ef49260-46ea-3e7b-99b7-dcb0b69bfcec | -11.31807 | -43.53233 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b2d0ab6-4379-3a6a-b7ca-71f1d31cba33 | -11.32487 | -43.53372 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e7542f5d-31d0-3a55-a290-a14bfd95cab5 | -17.81797 | -44.51294 | 2025-08-28 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30aa5c95-2d04-3a54-8659-85aecdc246ab | -11.33586 | -43.54887 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| be525c90-c612-385f-a5c8-be1a927ad160 | -11.32945 | -43.54057 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dd288014-af07-399a-a7da-0583a0ee88b4 | -11.31714 | -43.53148 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6769e194-247d-3540-ad6e-7bd4bc859de0 | -19.00617 | -41.00381 | 2025-08-28 03:19:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 364cc3da-a41d-3163-b47a-f879901371ec | -11.31938 | -43.52613 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef898620-d6c9-3037-8acf-d4669a9ad625 | -11.32266 | -43.53914 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06427144-7250-31b5-becb-9802a75b67ad | -17.73599 | -42.67973 | 2025-08-28 03:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cefab934-18bf-3a2d-88c5-e78c1bf7d7dc | -18.07418 | -44.07156 | 2025-08-28 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a79d6104-2815-3b40-ad31-9206be340c11 | -17.75542 | -44.48917 | 2025-08-28 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5b2128da-05d2-38bc-8af2-d8ab41f4b56e | -18.07604 | -44.06336 | 2025-08-28 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fd1bb17-c4b1-3130-b97e-5d0968585923 | -11.31542 | -43.54486 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dca77c40-cd1b-3d49-ad9d-091be16f1222 | -12.95896 | -44.57553 | 2025-08-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 1a1652fd-8d34-3482-98cd-590d94959c4a | -18.99584 | -40.29233 | 2025-08-28 03:19:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 425e83e9-aac4-3402-aee0-07078a56ffc3 | -15.71099 | -41.75503 | 2025-08-28 03:19:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2918ba0a-c5ec-35b7-ac04-64a4ac3438d3 | -12.95973 | -44.58303 | 2025-08-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| decf9a8d-7d7e-3e92-8ed2-d0d24dd94259 | -11.32394 | -43.5329 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e55c7725-ff97-3c2d-9001-d1cb69e855be | -17.72355 | -45.53301 | 2025-08-28 03:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61e22965-21cc-3679-84d0-9026c050f189 | -11.33167 | -43.53511 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 733c9d93-8172-3764-b072-d8c3f21ad109 | -10.4736 | -57.9563 | 2025-08-28 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b3eb365e-f714-3f99-9c89-d4bcce8182fd | -8.4333 | -41.4316 | 2025-08-28 03:20:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 52a6c47b-4e96-3cba-94c4-57501d994ac3 | -7.3955 | -39.6845 | 2025-08-28 03:20:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 139.5 |
| 1a3c05fb-f1d1-357b-ae6e-ad62c294cfbb | -10.4549 | -57.9576 | 2025-08-28 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 7bbde6c3-eaa6-346a-a784-283b796bfd9b | -9.1154 | -65.7886 | 2025-08-28 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 274.1 |
| d8c553b0-7736-317f-b59c-5d37b200f052 | -6.8774 | -43.5919 | 2025-08-28 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 2abfc52b-c8e6-323a-8667-4fa47254477c | -10.4738 | -57.9366 | 2025-08-28 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 0ad7dff3-5505-3e92-a2e2-caf9cf3bcbed | -9.134 | -65.7694 | 2025-08-28 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 375f8a83-ca98-3ee8-8277-c949c6a84ac0 | -8.433 | -41.4559 | 2025-08-28 03:20:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| f1d3cd85-226a-31d9-8e88-13f4d340f8e9 | -9.406 | -60.5711 | 2025-08-28 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b20a557e-c3f9-37df-84ea-83aef02410e4 | -7.3542 | -59.6476 | 2025-08-28 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 3bf465c7-0166-3418-90b5-2afc240153da | -6.8772 | -43.6152 | 2025-08-28 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 8baef2cb-735f-3a39-95dd-ddf0abcb4acb | -10.8049 | -60.7644 | 2025-08-28 03:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| f1a7b53a-2559-3871-af29-7f5b387c17f7 | -9.1155 | -65.7699 | 2025-08-28 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 203.1 |
| 29cbf653-7588-367e-a3a7-380a55a7a91a | -8.9479 | -65.9616 | 2025-08-28 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b9445fbd-e895-38f9-9b75-c23e2cb421b9 | -13.4234 | -46.8503 | 2025-08-28 03:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 444b7f0e-39e9-37a2-98ef-349bd26666ad | -10.8047 | -60.7837 | 2025-08-28 03:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 05001ea7-ba58-35fe-9fd0-b9b814c7f45c | -8.452 | -41.4536 | 2025-08-28 03:20:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 7262b5ce-ef25-3dda-bb2d-1a49c3c225b2 | -9.1339 | -65.788 | 2025-08-28 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 222.6 |
| dc4d8c42-8c3f-3b0c-bc70-c870281f0f48 | -9.0969 | -65.7892 | 2025-08-28 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| c20a10c9-f2a9-3559-b118-e6c416b60789 | -6.896 | -43.6135 | 2025-08-28 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 47f71274-345a-344f-9e14-260b34611894 | -19.1144 | -44.02721 | 2025-08-28 03:21:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aae985de-0481-3770-a742-676def1d94e0 | -20.30191 | -46.03474 | 2025-08-28 03:21:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0a1b62f6-3a7b-35a7-a3e5-8c8435d8cff3 | -20.30332 | -46.02883 | 2025-08-28 03:21:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 82427995-59c1-3903-a416-31624df9bde2 | -19.11472 | -44.02505 | 2025-08-28 03:21:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0093fd9e-7c48-3181-a741-654b4fad42aa | -21.15103 | -42.44475 | 2025-08-28 03:21:00 | NOAA-21 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 6e29a5f0-0862-3d7c-b0c2-26e4a9af1ab5 | -18.95279 | -43.83349 | 2025-08-28 03:21:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33d5ed87-c451-34d7-9add-19b403f7c573 | -21.89593 | -43.30957 | 2025-08-28 03:21:00 | NOAA-21 | MATIAS BARBOSA | MINAS GERAIS | Brasil | 3140803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 82299ed1-5b24-3fa7-b3a1-8b7f5041486e | -20.0884 | -43.74916 | 2025-08-28 03:21:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| df0d0579-8ada-3e60-a9d2-292e1837caf8 | -21.89682 | -43.31065 | 2025-08-28 03:21:00 | NOAA-21 | MATIAS BARBOSA | MINAS GERAIS | Brasil | 3140803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 17148c6d-0614-3fdb-9d47-61c549d7301e | -18.95379 | -43.83332 | 2025-08-28 03:21:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| deeab92f-fb50-3c86-b8d3-b14b40994f0a | -20.31114 | -46.03877 | 2025-08-28 03:21:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| f55cbfa1-60d0-3ef0-852a-113c058f35fa | -21.02613 | -46.23356 | 2025-08-28 03:21:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ef132249-e0e2-3d8f-bfba-2795f78aa6cb | -19.24717 | -42.04885 | 2025-08-28 03:21:00 | NOAA-21 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 45f03544-fbab-3635-b2fc-ec701328f3e9 | -20.09516 | -43.74665 | 2025-08-28 03:21:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 37c83385-4fb8-3d9f-a537-e79a20e04131 | -20.30852 | -46.03651 | 2025-08-28 03:21:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6d1df43e-ab21-396f-a64f-350ad2796acc | -20.30601 | -46.03094 | 2025-08-28 03:21:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| de4e9388-fee8-36a0-9f57-744617b8e0a4 | -19.22885 | -44.4441 | 2025-08-28 03:21:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af1ed21b-802d-3cb8-9c0f-bd8e5b801c60 | -20.25223 | -42.00581 | 2025-08-28 03:21:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| abec38ce-7871-33b4-818e-7cd6661d961c | -20.30457 | -46.03682 | 2025-08-28 03:21:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| d310d8d3-f461-3dd8-b0f1-f5fb33cb92e0 | -21.14947 | -42.45185 | 2025-08-28 03:21:00 | NOAA-21 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b9a89e14-3736-3580-b485-4f65d66c9772 | -19.12076 | -44.02666 | 2025-08-28 03:21:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 70c885ee-5348-3eac-a87b-a4f8b18f9ce4 | -20.25081 | -42.01233 | 2025-08-28 03:21:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| dfc846ef-6549-306a-ae7a-bf355e80c3d3 | -21.34682 | -45.84368 | 2025-08-28 03:21:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6fd9e80d-c582-3b54-a9af-136229a27e00 | -21.15024 | -42.44836 | 2025-08-28 03:21:00 | NOAA-21 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 66cead35-87b7-3708-85e9-1d02833303d0 | -19.24874 | -42.04863 | 2025-08-28 03:21:00 | NOAA-21 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8a9f2cb3-48b9-3e0d-a227-38103f199891 | -19.11554 | -44.02229 | 2025-08-28 03:21:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0d75065e-ee34-30f1-8baa-71650c75cf77 | -21.02866 | -46.237 | 2025-08-28 03:21:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4667360c-3e60-34d4-953d-4ea525a749f5 | -20.08951 | -43.74433 | 2025-08-28 03:21:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8c3cc0d9-504a-3e65-9fe2-f8d23ea4a767 | -19.22544 | -44.44116 | 2025-08-28 03:21:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4db075d4-df1f-3eb5-b443-149d1af3ffe4 | -20.25153 | -42.00904 | 2025-08-28 03:21:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 52854d7e-3782-3e26-99c3-89877626ad85 | -20.30993 | -46.03058 | 2025-08-28 03:21:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 197b2b5c-48fe-3dfc-b0cd-ac2b8eaa5a98 | -8.452 | -41.4536 | 2025-08-28 03:30:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 167.1 |
| 5d05fe3c-2572-3b3c-9dfc-8a33f7692bbc | -8.4333 | -41.4316 | 2025-08-28 03:30:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| c3ab9c09-a27e-3fc7-80f1-c9ec7586548f | -9.1339 | -65.788 | 2025-08-28 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 209.4 |
| 31caa93f-be98-3c94-bd4e-8955e9bbd8ed | -8.433 | -41.4559 | 2025-08-28 03:30:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 114.2 |
| e33213c5-bbd2-334e-9e59-584903de80f6 | -9.1155 | -65.7699 | 2025-08-28 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 197.3 |
| 93e63401-c405-36c3-984c-04837e554d3e | -8.4523 | -41.4293 | 2025-08-28 03:30:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 53cee5ef-4e9f-3438-a2c9-e50d134a784b | -10.4738 | -57.9366 | 2025-08-28 03:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 497b0f5a-e97e-3e80-989b-1ce2a8b310bd | -6.8774 | -43.5919 | 2025-08-28 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e74f91f6-95c2-37af-934d-3939c46b372d | -9.1154 | -65.7886 | 2025-08-28 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 323.9 |
| 23f14afd-0892-31db-b901-99203b01c063 | -9.134 | -65.7694 | 2025-08-28 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 7674ff01-293b-3a24-b19d-79a1f64ed539 | -7.3955 | -39.6845 | 2025-08-28 03:30:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 212.5 |
| 078b4b81-0d36-3393-bb9a-2e0eb7350599 | -7.3958 | -39.6595 | 2025-08-28 03:30:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 9af3047b-4743-30ca-acee-0f0789708ed2 | -10.4736 | -57.9563 | 2025-08-28 03:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 33c7349d-3600-37d0-8b5e-e587f5c47bdd | -8.9479 | -65.9616 | 2025-08-28 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b1e15f0d-6857-321f-a65e-206b4f0ab180 | -6.8772 | -43.6152 | 2025-08-28 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 38b26fe9-683b-3640-b237-b38b90051318 | -8.4333 | -41.4316 | 2025-08-28 03:40:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 8f6eaa82-1972-3e81-a66e-ec519d772c99 | -10.4549 | -57.9576 | 2025-08-28 03:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 2ba3d5a3-bd29-31a0-b848-15d23d4bbd94 | -7.3955 | -39.6845 | 2025-08-28 03:40:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 145.4 |
| b2edc5af-bee1-326f-b2de-b11ed02a5872 | -9.134 | -65.7694 | 2025-08-28 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 15f1a8ff-d7bf-324b-96f9-9048e1902745 | -9.0969 | -65.7892 | 2025-08-28 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d30a7276-47a7-3d4c-a978-9e3bcf6d1104 | -9.1155 | -65.7699 | 2025-08-28 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 150.6 |
| ad4b5712-a028-380e-9d2a-3cb0cd79419b | -8.452 | -41.4536 | 2025-08-28 03:40:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 186cbb65-248b-3082-954a-f14ccdd1ea06 | -6.896 | -43.6135 | 2025-08-28 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |


[Clique aqui para ver as próximas entradas](README19.md)
