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
| 327f2dfb-6178-3fb6-97b3-c0a5ebddebcd | -11.6647 | -44.2702 | 2025-10-07 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 01a0f8b1-a71d-31b1-9870-938bcccd6fc3 | -10.9109 | -47.1129 | 2025-10-07 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 41660261-8486-3559-b31c-581645f989f9 | -8.5393 | -46.2631 | 2025-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| a975d3fc-c11e-30fa-a15e-2591641e6c27 | -7.6932 | -46.2548 | 2025-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| d8cc71fa-9078-30d0-91bf-e66f6fc0a42e | -10.9477 | -51.1058 | 2025-10-07 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 134.1 |
| b0747c0f-40db-31ff-b1d5-6ebba1780ee2 | -6.0614 | -38.896 | 2025-10-07 14:20:00 | GOES-19 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 97a6144d-f1d9-3278-bc4e-675f26d084df | -15.5808 | -52.5769 | 2025-10-07 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 4655ec45-ff89-32cf-b0b3-3bd3db388426 | -7.6651 | -45.4245 | 2025-10-07 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c96e349e-d76d-32d8-a207-c3f79ec92355 | -15.6198 | -52.5715 | 2025-10-07 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 70546537-115a-33c0-b4eb-301c336ad323 | -9.3389 | -45.7266 | 2025-10-07 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 57c03196-ed31-3ad6-932d-213b3e7dcf36 | -8.1801 | -43.3679 | 2025-10-07 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.7 |
| 6e9d41fc-ac33-344b-8368-a3b23ffb6e8b | -9.9212 | -50.1895 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8111e3f7-91f3-36f9-a29c-46a4bc71cc9e | -10.3854 | -47.9956 | 2025-10-07 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 9c8f516b-ed98-32eb-9c1d-bf037405c6c7 | -13.7927 | -45.7627 | 2025-10-07 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 2740fc87-712c-32e7-8e1b-009858a654b6 | -12.5349 | -48.1446 | 2025-10-07 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| c655ed11-a5ff-3b7a-879b-92ad4181bbc7 | -12.5541 | -48.1419 | 2025-10-07 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 42a79438-63f6-302d-8875-82bb6c9720fe | -8.5207 | -46.2425 | 2025-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 0ef0b4ee-b2e6-30d0-a570-dc526e79379d | -8.6519 | -46.2964 | 2025-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e16cbdc9-20e9-371a-9197-5990122adde8 | -8.5584 | -46.2387 | 2025-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 8d9806e1-34ee-3970-9a1a-01ea1e64430e | -8.1804 | -43.3445 | 2025-10-07 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 335.9 |
| 80a4a52b-a330-32a4-8feb-65afcc6f62e5 | -9.4068 | -46.2831 | 2025-10-07 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| fb2fae7f-169f-34de-a1bc-7ede4982a03e | -14.8641 | -51.4373 | 2025-10-07 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 884ed2f7-70ca-329c-8438-7fb599d347d6 | -4.0569 | -42.5118 | 2025-10-07 14:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| d25588c4-454c-3d09-a277-7a13ca59263a | -11.0448 | -50.926 | 2025-10-07 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| c3a8ac8d-1cf4-3b63-98ce-64ed917be186 | -10.0868 | -50.5141 | 2025-10-07 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 6ff1e9fc-7748-36fd-8288-08c77f5a7e52 | -8.9759 | -47.4864 | 2025-10-07 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 86777ec5-c799-3a71-923d-80bd3c360fb8 | -11.8029 | -45.1087 | 2025-10-07 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 6d465b21-7cd8-3076-8014-d356965584af | -11.2436 | -50.2645 | 2025-10-07 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 76f948a3-0004-3fba-8b13-9c17d4e9a444 | -8.5007 | -46.3342 | 2025-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| a8445566-460f-3c1a-9658-c3e6f2faf7ee | -10.6513 | -46.6978 | 2025-10-07 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| b3f4ad57-87bd-309c-87c8-2f348d6d54c5 | -14.6327 | -48.3219 | 2025-10-07 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 36e0dd69-16be-39ed-8bdf-519c0c07b165 | -12.0511 | -45.164 | 2025-10-07 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 468c72cc-dbe4-3632-bbd4-97c2b0c3d2d9 | -19.5782 | -44.6442 | 2025-10-07 14:20:00 | GOES-19 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 160.0 |
| b58fc935-1a48-3c54-b764-fe88770c807e | -11.0454 | -50.8834 | 2025-10-07 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 408710ae-ab3a-3751-bb62-ad921f9aa2b7 | -9.6804 | -45.6645 | 2025-10-07 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 234.9 |
| 351eca20-c3c4-3228-9bbd-d8d1c6c9d477 | -11.1644 | -54.8804 | 2025-10-07 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 247.8 |
| 21c7f9fd-25b0-3175-aa72-28ad1439e843 | -7.6648 | -45.4471 | 2025-10-07 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 903d184a-f6a6-3cfe-8503-a332c4abe630 | -10.2129 | -54.1262 | 2025-10-07 14:20:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 3ba3220c-3f9c-3bcd-aca4-160e4909822d | -10.3535 | -50.3169 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 23216abb-26be-3721-94cd-05a72f8e7c93 | -11.7641 | -45.1375 | 2025-10-07 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 7ebc1c3f-ad61-330b-a94c-1332d127056e | -3.1319 | -44.4119 | 2025-10-07 14:20:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| cfd88774-01cd-38a5-b37d-04cf944c7f83 | -10.4466 | -50.414 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| d973634f-efa6-3e41-955b-13fbb35c13f0 | -11.9479 | -51.4636 | 2025-10-07 14:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3b8a7f25-2c20-37d0-a6b8-9cd36550bd3f | -8.1615 | -43.3465 | 2025-10-07 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 44036ba9-313a-3d29-a4a2-72b12b599bee | -3.9135 | -41.5447 | 2025-10-07 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 43a5edd1-e25b-3d87-b6aa-7c5255b8611d | -10.4655 | -50.412 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 3da54b96-75bf-3b45-a330-8c4b4ebbc349 | -8.2266 | -44.1548 | 2025-10-07 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 170.8 |
| f08c4765-0e4d-3636-bb04-b3e0e4d42c2a | -7.4666 | -43.0909 | 2025-10-07 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |
| d4bcdef8-0fd9-3afc-9bf8-f452b3a36637 | -9.9398 | -50.2091 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 0d023e0f-5fac-347a-8dce-dc6e4b36cfd8 | -10.3529 | -50.3596 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 3064e08b-ddb7-3ef9-9d0e-a668a49f85c8 | -10.2057 | -46.0319 | 2025-10-07 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| a1ef88cb-40ed-3f26-870f-3c01bf7b2dbe | -6.9704 | -42.0023 | 2025-10-07 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| f4ec75b0-10b2-308d-9dae-e8d804644ed8 | -10.2968 | -50.3226 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 984bee74-eaf2-3820-9c1d-942967c4d084 | -15.3979 | -48.0164 | 2025-10-07 14:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 9bda08c2-3a12-376d-8c0e-140d47c946e0 | -10.3247 | -46.9612 | 2025-10-07 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 70fb920e-18ff-3d72-930f-170225162d9c | -12.9294 | -54.7333 | 2025-10-07 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| c4646007-55f1-38f7-a547-a22030f53ea0 | -11.7409 | -45.371 | 2025-10-07 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 330.8 |
| fdc2e8b4-0b15-3890-b04b-863c7ba33346 | -10.0865 | -50.5354 | 2025-10-07 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 4f55c2da-ef7a-348a-8972-211dc248b152 | -12.1652 | -50.9287 | 2025-10-07 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 142.9 |
| e4498faf-1eb2-3d93-88d8-61624c091689 | -5.381 | -40.9871 | 2025-10-07 14:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 450.8 |
| adc4f037-6e90-3de7-9e8b-17d36647a00f | -13.0009 | -46.7795 | 2025-10-07 14:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 60c47315-2817-3d24-ad0f-b73c4c0d740a | -4.2847 | -42.0248 | 2025-10-07 14:30:00 | GOES-19 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 437dff74-39cb-38c7-9dec-c47a392c434c | -8.5004 | -46.3566 | 2025-10-07 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| bc27f96f-254f-3df6-9008-a298ef0dab13 | -12.3471 | -50.2642 | 2025-10-07 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 4defa707-1f38-314c-abda-fde3170da6a4 | -14.8641 | -51.4373 | 2025-10-07 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 240.2 |
| a9f0def5-d9cf-3913-9cb6-247b1006d82a | -12.0511 | -45.164 | 2025-10-07 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 313dcae6-2a5c-3159-b841-9a2b9bb5fc2e | -8.9306 | -46.6033 | 2025-10-07 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c802d8a7-eac9-3207-a933-8cae0175850b | -8.1885 | -44.182 | 2025-10-07 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| f52e0029-907d-3dcd-a8d4-942f0f1bde82 | -10.6513 | -46.6978 | 2025-10-07 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| a7da5809-3dc9-382e-a70c-c6823e3a2935 | -8.1801 | -43.3679 | 2025-10-07 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.6 |
| 1904c87d-1b9c-379d-8a28-2a9aa29ecc1a | -8.6519 | -46.2964 | 2025-10-07 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f485c83c-1d9c-384f-a33b-25fd882ea50e | -3.1306 | -40.9824 | 2025-10-07 14:30:00 | GOES-19 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 128.3 |
| 99aca903-4ae7-312b-b08c-4e2c4426d8bb | -7.6648 | -45.4471 | 2025-10-07 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| b410aac0-b0a6-3654-bcd8-bf4f1ee56309 | -10.1573 | -45.4701 | 2025-10-07 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 575b4e5f-e582-3517-b76e-e2ad53eef6d6 | -11.7201 | -51.4465 | 2025-10-07 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1e322471-da30-3989-98c9-430493637f07 | -13.004 | -51.0195 | 2025-10-07 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d2a34d02-72aa-3929-88eb-3d97739b1299 | -11.0451 | -50.9047 | 2025-10-07 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 9e42e6cc-6246-3d1f-88ce-6bb78d5d5077 | -10.0679 | -50.5159 | 2025-10-07 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 9827880f-02b6-3b9d-af6b-e63930d1b509 | -10.0217 | -48.2994 | 2025-10-07 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 74bba142-c326-3d02-8fb1-f83c87709cb3 | -10.8731 | -51.0289 | 2025-10-07 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 88ba7889-66d5-3fe5-973c-9ce7d7d672bd | -9.2973 | -46.0026 | 2025-10-07 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 7cbcc990-5a93-3df0-bbad-18b2084adb81 | -3.6328 | -41.536 | 2025-10-07 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 9b8b6844-2076-349b-bcf8-622f0e17f288 | -8.613 | -44.9189 | 2025-10-07 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| da711738-6b60-3aaa-bfbd-44ff1e89a247 | -12.1461 | -50.9309 | 2025-10-07 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 141.7 |
| da716a79-6f11-3bf9-8197-159505e9b268 | -3.8761 | -41.5468 | 2025-10-07 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 3e20bb77-8fa5-3df8-be68-f9c7c583e541 | -9.9212 | -50.1895 | 2025-10-07 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| de9f941c-ef63-30f2-96c8-dd43084e911c | -8.6397 | -47.2769 | 2025-10-07 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 304c2701-40af-38e9-974c-04489248fba9 | -8.0866 | -44.791 | 2025-10-07 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| f898a053-90f2-3126-8faa-171f9111f460 | -3.9961 | -43.2418 | 2025-10-07 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| ca528a7e-0e72-3fd9-9711-415c9c58fb92 | -12.1655 | -50.9073 | 2025-10-07 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 02ad2774-b6f1-3269-af27-3935466d1dc3 | -8.1055 | -44.7891 | 2025-10-07 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 6d0caf36-d0c8-3c96-b81c-254d4e368b1f | -10.9106 | -47.1353 | 2025-10-07 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7b8fa109-884d-3034-8f70-98361d5076b9 | -9.4178 | -46.8637 | 2025-10-07 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 4aecfe39-8572-3a04-9e44-3f0a821da51d | -5.3999 | -40.9856 | 2025-10-07 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 162.6 |
| eb632965-3128-3ef7-9cd9-fa40f259e044 | -10.3665 | -47.9978 | 2025-10-07 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 70f4e7c1-15e0-347f-888f-fcb998a47f5d | -9.921 | -50.2109 | 2025-10-07 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 9f269109-fa01-3757-bf24-06f98ae4fc4e | -7.4666 | -43.0909 | 2025-10-07 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 135.9 |
| a276771c-2341-31ba-8669-0464d75873f9 | -9.9024 | -50.1914 | 2025-10-07 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 1fb51f1e-f1eb-37ab-a8e2-4d9e21d3ebf0 | -10.9109 | -47.1129 | 2025-10-07 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 457.2 |
| 55b070be-bbe1-3b1e-854a-5d6444efb9f6 | -8.5584 | -46.2387 | 2025-10-07 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.1 |


[Clique aqui para ver as próximas entradas](README129.md)
