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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e97fbce-02c0-36df-b03b-1b265ee966c6 | -7.8862 | -44.2365 | 2026-10-07 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 711026a6-2d70-3b61-b7f5-1e3cb06c020f | -7.1814 | -55.1036 | 2026-10-07 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| fbe67180-1e0b-3965-9193-23862feb93bb | -11.7947 | -46.683 | 2026-10-07 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 4b916a50-5318-3e5f-8987-2f11714ae333 | -16.0502 | -39.8291 | 2026-10-07 13:40:00 | GOES-19 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 113.1 |
| ee37d82b-032d-3f07-9d8f-e23a56107397 | -7.7592 | -43.8325 | 2026-10-07 13:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 21858112-cc70-373b-b9f7-4aa8566adfb3 | -7.1813 | -55.1237 | 2026-10-07 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 0673184c-fdc3-3a8d-a827-05b328f282be | -7.2 | -55.1026 | 2026-10-07 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 64b93c83-509a-352d-a73c-3dc321c445a4 | -8.5844 | -45.6729 | 2026-10-07 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e71bbf56-8be9-3950-a18b-3a2b488512f4 | -8.5051 | -54.6202 | 2026-10-07 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| eea199b4-bf77-39ed-9000-09b417098068 | -7.8789 | -72.3492 | 2026-10-07 13:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 88b67a8f-2256-347d-aac7-c17a1a03fe71 | -11.0642 | -45.854 | 2026-10-07 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 336.4 |
| f4db7f01-e47f-389f-b67e-6964d6eb7ea9 | -11.8508 | -43.5361 | 2026-10-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 5c6581c6-07ce-3341-8b6a-bfada96ccf98 | -11.3745 | -46.6948 | 2026-10-07 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f98aabe0-8e00-3953-8304-f4041bd873c0 | -10.8591 | -50.6692 | 2026-10-07 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| da04290c-b858-3736-8aae-6cb53f731113 | -11.7143 | -43.652 | 2026-10-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 44b6189d-fbaa-3cd9-9d80-f44f62001707 | -11.3742 | -46.7173 | 2026-10-07 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| cf5af94d-a85d-30c7-a9a7-036e23b6198e | -11.8503 | -43.5598 | 2026-10-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 49ab8ed8-da38-3f36-a275-d4253e5aaa43 | -7.2816 | -46.1571 | 2026-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 82749058-4ce9-3a38-9cdf-f7c9f12ed295 | -11.7755 | -46.6856 | 2026-10-07 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| aacb9c30-c15c-340f-9d9c-2e09b4f3d5cd | -7.3475 | -45.2725 | 2026-10-07 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 4d63a68c-39a3-3442-aaac-c89ae88961bc | -7.7399 | -45.4627 | 2026-10-07 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 3140d7e6-240a-3d48-aa2c-79b396023a61 | -9.432 | -45.8293 | 2026-10-07 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.1 |
| b6851bf3-a810-3dda-867b-fc12e131c749 | -7.8146 | -45.5009 | 2026-10-07 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| fca894eb-2192-30e4-ab24-b0b249c887ac | -11.7139 | -43.6757 | 2026-10-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 9d9e52ec-d959-39bc-a396-e09fd116d673 | -8.6514 | -44.8689 | 2026-10-07 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8effd28d-081c-32c0-9efc-aa3c3ab87350 | -7.8679 | -44.1922 | 2026-10-07 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| d60c2ef6-9239-3368-a969-0f6056a9fd4b | -15.4011 | -46.0781 | 2026-10-07 13:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 7b5b98f1-46f4-3a04-bb20-5ebeecc1e7f8 | -7.5568 | -46.7128 | 2026-10-07 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 43f584ec-e9bd-37d3-b243-df47b19ebd08 | -9.4509 | -45.8271 | 2026-10-07 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 7f59b5ca-a28c-39ec-a73a-1094a53cb7a2 | -11.7751 | -46.7082 | 2026-10-07 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c5c7a533-8318-30d2-8136-b50915debd07 | 2.1267 | -50.8371 | 2026-10-07 13:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f61a3c84-1086-3573-ab60-b5fd3f83183a | -7.3935 | -46.2144 | 2026-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 150d12a8-73f5-3c58-9cba-90fc71f224dc | -8.524 | -54.5987 | 2026-10-07 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 0220d0b7-0a29-3de8-804f-297968225a99 | -11.1556 | -46.0916 | 2026-10-07 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 237.0 |
| aa7423ea-8848-367e-ac96-f5d0fa361b2e | -12.2132 | -44.6991 | 2026-10-07 13:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 14672bbe-ec51-3d39-96dc-4e1ee826813b | -11.1988 | -49.4297 | 2026-10-07 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| cdd894f9-dc74-38dc-9c72-f2bcf969e240 | -7.7213 | -45.4418 | 2026-10-07 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 43cef0b8-0363-3c5b-9904-421d7e10c00b | -7.5286 | -45.8659 | 2026-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 54efb6c4-b376-3b86-8968-99ddfd8cff59 | -7.5284 | -45.8885 | 2026-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| ea136bc4-0645-3af0-a86f-66e82a3b552c | -7.1891 | -44.3042 | 2026-10-07 13:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a482758f-2a54-38b2-84b8-8ea899e51d0f | -7.7595 | -43.8092 | 2026-10-07 13:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 136.0 |
| fe2a53b6-92e5-3f4f-87d1-72dfd91f82a0 | -11.8311 | -43.5628 | 2026-10-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| c889d75e-7af3-326f-86c9-44d8979b81a8 | -7.721 | -45.4645 | 2026-10-07 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 853ba84c-2d31-3da9-b7ce-df76228d6a8d | -11.0646 | -45.8312 | 2026-10-07 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| f45848f8-445a-319f-a9b3-47b99ffb62f0 | -11.8315 | -43.5391 | 2026-10-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 0855d9d3-c5e0-3c56-b847-4161abcf8ece | -7.3935 | -46.2144 | 2026-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4164689d-f934-3952-83e5-95ca141752a4 | -11.3937 | -46.6922 | 2026-10-07 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| fb90e42f-a2d4-3f35-8fc2-ea5363eda511 | 1.5283 | -56.0227 | 2026-10-07 13:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 00ea09ff-6eda-3b0b-821b-65e449aab25d | -11.8311 | -43.5628 | 2026-10-07 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 7dba3ba6-d329-3b68-9b2a-201103470496 | -11.7143 | -43.652 | 2026-10-07 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| e258ede5-338c-3136-80e6-706e66dc89f8 | -11.1556 | -46.0916 | 2026-10-07 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 276.2 |
| 656127ec-2742-3802-b820-ade0bd2494bc | -10.9949 | -45.4298 | 2026-10-07 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 6a4bdd90-9073-3878-803b-0cd53b6aa479 | -9.3619 | -45.4288 | 2026-10-07 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1826bb59-8135-31e1-8a15-19e456cb6a82 | -7.7579 | -54.9499 | 2026-10-07 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 74deabf5-91d4-39f3-a0ab-07288f19f3fe | -7.5571 | -46.6906 | 2026-10-07 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| b26f9dd7-918e-35cd-84e8-5b6c55d8995a | -6.9925 | -45.1223 | 2026-10-07 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| b8b439b1-575c-3ac5-bd7a-da874b0b6c46 | -7.8676 | -44.2153 | 2026-10-07 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 186.9 |
| ed25a465-61c4-3ec3-bf7c-e29b3277602c | -7.5568 | -46.7128 | 2026-10-07 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| bbf2e05e-93be-39e2-9bb6-2345550d663f | -11.8503 | -43.5598 | 2026-10-07 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 308.5 |
| b2119a9d-fa55-32d3-87f9-c6aaf98ee560 | -6.4413 | -55.0224 | 2026-10-07 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 84c96bbd-50f0-386a-8da1-a3f4885ecbda | 3.5842 | -60.8513 | 2026-10-07 13:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 617ad309-32c6-300e-8cf3-21c04c1012c5 | -7.7213 | -45.4418 | 2026-10-07 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 917758a5-3fe9-3089-a1c8-813f027d6cce | -11.3745 | -46.6948 | 2026-10-07 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 5c9345ff-3f92-3e91-ad06-24423698cfbb | -11.7943 | -46.7056 | 2026-10-07 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 3dbe0ce3-b094-31d6-baf4-f59c8d54e7b2 | -12.2132 | -44.6991 | 2026-10-07 13:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 237.6 |
| f151370d-1771-315e-b05d-1f5ebced3103 | -8.5356 | -55.383 | 2026-10-07 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 9d228f9e-8fe4-3e15-88b9-459ddee8e739 | -10.8591 | -50.6692 | 2026-10-07 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 8ba6aa35-1fd1-3ed6-b6f3-4e31e4b551e5 | -7.3475 | -45.2725 | 2026-10-07 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 1f33938c-c036-327e-ba8a-c5d386ce203a | -7.5756 | -46.7112 | 2026-10-07 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| fc39499d-4776-3f07-b58f-9007fa4a8a86 | -11.3742 | -46.7173 | 2026-10-07 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 4a3dd259-776c-364a-bfa9-db93cce55e1d | -7.1814 | -55.1036 | 2026-10-07 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 18f77c74-d479-3a4d-9d5f-f53d4d171811 | -7.8789 | -72.3492 | 2026-10-07 13:50:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 5404a01c-bd71-3a44-8e48-65717b706a2f | -7.5284 | -45.8885 | 2026-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| b239c76f-30af-381c-a74b-1550c5dfd5e2 | -12.2136 | -44.6758 | 2026-10-07 13:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 9cef8d32-97db-3a1c-baec-71dea342145b | -7.8865 | -44.2134 | 2026-10-07 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| caa72a5e-5849-3d08-9624-4e2d7473b4bf | -11.8508 | -43.5361 | 2026-10-07 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 290.6 |
| 64d934a4-ea9c-3aa7-a1ff-1dabe97347ef | -8.5844 | -45.6729 | 2026-10-07 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 8d3d2a63-b056-3215-b2b7-26011ab8c729 | -8.6514 | -44.8689 | 2026-10-07 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 1de5a825-3b75-37cf-a129-79112bae366b | -7.2 | -55.1026 | 2026-10-07 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 7daf3420-2d6b-3814-95c9-1627a8d91942 | -11.8315 | -43.5391 | 2026-10-07 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| dd65c135-6e68-3b42-b3c3-4cd6c9f95e5e | -7.721 | -45.4645 | 2026-10-07 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 3c99a04a-60c9-3914-8982-959d587b73fd | -15.4011 | -46.0781 | 2026-10-07 13:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 99697096-d6fb-310e-ba5a-4fecb1e12b8a | -11.7335 | -43.649 | 2026-10-07 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 0205cccc-219d-30bd-919c-c37aa0f2024a | -7.5847 | -55.7205 | 2026-10-07 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| a56a783e-d8e0-307a-a666-e723de0dd615 | -11.7751 | -46.7082 | 2026-10-07 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| a6b1b587-d65d-3c0b-bc4b-568bb2aeaf80 | -7.1813 | -55.1237 | 2026-10-07 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 7c675608-cea0-3b77-953d-9cf722f55699 | -16.0302 | -39.8341 | 2026-10-07 13:50:00 | GOES-19 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 105.6 |
| 10b0935d-f523-3ed5-9a14-b415331524c0 | -11.0935 | -47.6019 | 2026-10-07 13:50:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 3d506455-a453-36ac-b113-70fa6d08070c | -7.7399 | -45.4627 | 2026-10-07 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 8ca99e3b-aab5-37fb-b41c-c38f8ef9f8f4 | -7.5286 | -45.8659 | 2026-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 2dee7af6-1d06-35a5-98bc-e5c5ed8f01c4 | -11.0459 | -45.8109 | 2026-10-07 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 1d56c7f4-8422-357e-acb2-830846b2c177 | -10.9762 | -45.4094 | 2026-10-07 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 0aee8d8d-a42b-3fb9-b623-71a8ef53425c | -12.9959 | -47.0511 | 2026-10-07 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 59206955-f8bb-3360-bb02-b0c4b457e54a | -6.935 | -45.2408 | 2026-10-07 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| cfd1fa21-f835-36ae-b765-c027393b348e | 3.5263 | -51.2778 | 2026-10-07 13:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a52acc1d-74fa-362b-a836-260d3b45d0d6 | -10.9953 | -45.4068 | 2026-10-07 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 9519a3ae-59ba-3428-8b45-f935e294467e | -7.8679 | -44.1922 | 2026-10-07 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 99dd52af-3bb8-3f0f-bd3a-ffc8853fbe6f | -12.2758 | -44.4329 | 2026-10-07 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 7c75b87c-af14-37ea-9c4b-2bdb11c32796 | -11.7947 | -46.683 | 2026-10-07 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 2518f581-3336-3c6c-89ab-9ec65e446e4d | -7.8146 | -45.5009 | 2026-10-07 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |


[Clique aqui para ver as próximas entradas](README131.md)
