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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 692c3af4-cd02-3019-a2d6-5641ed9a8f75 | -10.7652 | -50.6153 | 2026-09-20 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 791.0 |
| ca8def94-b228-309a-9578-b745c281e07c | -10.8672 | -56.1775 | 2026-09-20 15:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 464e28a6-8a72-38f6-ae50-f1ce1ce84265 | -6.8215 | -59.1879 | 2026-09-20 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ddb4fdb8-c9a5-3d35-91bf-831d88cafd73 | -9.3575 | -50.1156 | 2026-09-20 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 379f2491-a528-3395-a0a7-8adef7b2ba87 | -3.3494 | -59.8097 | 2026-09-20 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 6e44e84a-6988-38e3-91fd-36e02dfc05d7 | -8.4797 | -57.6282 | 2026-09-20 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| a3edfc97-cacf-3945-9a7a-4dbb63138566 | -11.3809 | -44.0788 | 2026-09-20 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 609085eb-f276-306e-9f22-6b86cc926f77 | -12.6423 | -50.9144 | 2026-09-20 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 19fa2127-84ba-3da7-8dfe-9b53ee9444a8 | -11.1225 | -49.4601 | 2026-09-20 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 91e5946a-2305-3a1a-a4e0-1274741af6c7 | -11.9543 | -49.7728 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 41c6e851-1aaa-37dc-9fe5-69e02c4a1db6 | -12.642 | -50.9359 | 2026-09-20 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 9840db21-43c5-3639-b8e3-4c192138c578 | -11.0596 | -54.1755 | 2026-09-20 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 223.5 |
| 8bd7fd70-6fa2-304d-84ee-2a7a283a39f1 | -11.3813 | -44.0554 | 2026-09-20 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 7b8e5082-03fc-3eb1-ac21-af4a72ec3829 | -10.9694 | -57.1881 | 2026-09-20 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d40b9a19-bb7f-394d-8175-8c2cb5ff3f09 | -11.7162 | -54.5654 | 2026-09-20 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 9de5248b-62da-31ec-9f28-8dfda865e8bc | -8.4872 | -47.4462 | 2026-09-20 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| d88a6f55-bac1-3875-a7b3-76e0d9fec3df | -8.4737 | -47.0053 | 2026-09-20 15:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7aa00a41-76fc-3a34-98f6-184caee78c3c | -9.8397 | -46.4361 | 2026-09-20 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 60b85072-e234-3aa0-83fc-449cc9c88264 | -10.8668 | -56.2176 | 2026-09-20 15:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c787f020-3a8b-38b9-9449-9f801dac6578 | -12.8053 | -54.0669 | 2026-09-20 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 9b41b3fe-e906-3e92-9928-ac4fdcf2b741 | -3.0534 | -61.2767 | 2026-09-20 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d34636a3-2b33-3085-b311-338a4cee1a71 | -11.7351 | -54.5636 | 2026-09-20 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| f2b915fd-42b7-3c5f-b927-e0de3c7547bc | -10.4103 | -48.9112 | 2026-09-20 15:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 89ca2b91-ac59-3f8f-a2ad-64be2e35057d | -10.0956 | -48.4226 | 2026-09-20 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c8538299-0ccc-3407-9c54-be6fb463e673 | -15.4174 | -53.0236 | 2026-09-20 15:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| d6210c33-97a9-30c4-91eb-f879bf48be2e | -10.8757 | -57.1554 | 2026-09-20 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 78115215-859a-34ef-847f-bbe21eb49ea1 | -10.8759 | -57.1355 | 2026-09-20 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 1a9f00d5-9fb8-3204-b127-04dee3e8f733 | -7.3289 | -55.2155 | 2026-09-20 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 9baaf697-699c-3af6-a164-0740a33f8fde | -13.0177 | -46.9125 | 2026-09-20 15:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| f174b02c-1c6f-38dc-99c8-539225b16788 | -8.0278 | -61.3816 | 2026-09-20 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| da20e761-35ae-364c-8da9-87f5134aee32 | -3.4003 | -61.3087 | 2026-09-20 15:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 695afbc8-62a0-395e-84c7-cfde763fc35d | -3.3492 | -59.867 | 2026-09-20 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| d464e9fd-87d3-3d64-b927-850876d8c1df | -6.5829 | -58.9851 | 2026-09-20 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3cb9ba43-add7-30a2-a193-27ee6deb7949 | -10.0975 | -45.6597 | 2026-09-20 15:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 4bf6026b-bd1c-3876-a8fa-180b2da824e2 | -6.3197 | -59.9764 | 2026-09-20 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 795bcb6c-3ab9-3caa-adb9-3a78fca86171 | -10.2793 | -50.2177 | 2026-09-20 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 93e7a76d-af03-3a2f-b7e5-d7532b758035 | -3.5356 | -58.6939 | 2026-09-20 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 477e1fcc-5acf-3b66-9d0f-e68c08bebbcc | -16.9861 | -44.8693 | 2026-09-20 15:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 3d2666cb-1826-326f-8272-bbd44b541169 | -3.331 | -59.8292 | 2026-09-20 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| a68e20b9-816c-3dba-92b1-05c36ac3479f | -10.8856 | -56.2161 | 2026-09-20 15:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 442235bf-d725-36ff-b8f7-fe70f648c4f9 | -9.7049 | -58.1443 | 2026-09-20 15:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 912855be-2bd5-3507-bdc0-f6a4d62d909b | -11.0617 | -49.7261 | 2026-09-20 15:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 82ac408c-c706-30f9-a7e4-881e6c635e85 | -2.8974 | -57.7987 | 2026-09-20 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| e4f580d3-83e5-37ed-8739-c54b2e8587b3 | -12.0649 | -50.0185 | 2026-09-20 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b1bf7530-2624-3d1e-91ce-92009913d643 | -3.4455 | -58.2134 | 2026-09-20 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c01b0006-dc32-358e-8c84-04a8208c16f5 | -11.2336 | -48.3791 | 2026-09-20 15:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 6070332b-fd35-3c8e-b848-f5c621d87b01 | -8.4549 | -47.0072 | 2026-09-20 15:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f621ee32-7224-36b2-95ec-dbf2be9be35c | -12.1328 | -47.041 | 2026-09-20 15:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| a2d991d4-c7a5-3222-9d2a-4fff074c0250 | -3.4049 | -59.5794 | 2026-09-20 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 75dba4c3-d9b7-3dc7-938e-3095e3044432 | -11.0506 | -54.9309 | 2026-09-20 15:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 306.2 |
| 8a04eb98-1e54-3eeb-8974-6ebd112ae2c5 | -10.7463 | -50.6172 | 2026-09-20 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 438.7 |
| 9c745999-6a35-3a37-a11a-5a4b70c76c9f | -11.0614 | -49.7477 | 2026-09-20 15:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 164c0969-b207-3933-894c-3d023125b22e | -6.8031 | -59.1886 | 2026-09-20 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f5c2b689-8774-339e-9cb5-e0a29f6d9958 | -11.0256 | -48.3164 | 2026-09-20 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| cad2282a-6b40-3895-99cf-d443a112a973 | -6.4486 | -59.9717 | 2026-09-20 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 486.8 |
| 93046a9b-9496-3d12-ba00-2bb2735918d6 | -6.0925 | -57.6847 | 2026-09-20 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 076ab3a5-2fee-3017-99d0-49584a06ecba | -12.1524 | -47.0158 | 2026-09-20 15:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 64429a07-23e4-3f4d-9153-8f8d5ea75b6f | -13.5907 | -51.4794 | 2026-09-20 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| e36beb76-3df4-35c7-a1d0-e96e81d38fcf | -9.0544 | -48.7469 | 2026-09-20 15:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 192.0 |
| 065dfa2d-02b3-3684-99be-5cf1829db00f | -11.0412 | -54.1362 | 2026-09-20 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e39fd5a1-82b2-34a3-913a-57b0bcf8e589 | -3.1079 | -61.408 | 2026-09-20 15:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| c6730daa-d012-3afb-a9a8-056ba3b3ae4a | -6.7591 | -47.8777 | 2026-09-20 15:00:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 8370d945-aedf-3bc3-8cdb-8771ac6e8e3c | -3.5894 | -59.0581 | 2026-09-20 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a3618112-754a-32cc-a473-0bab2002ef7a | -11.9349 | -49.7968 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 7d42c159-806d-3d19-86fc-a3695047a9be | -11.0221 | -54.1584 | 2026-09-20 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a281f8ed-f6cd-338c-8a77-b919a6b8732c | -8.8735 | -49.7328 | 2026-09-20 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| fe28d22b-9d19-3690-ac09-70ea0c3aef52 | -12.0072 | -50.047 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 6131f2b6-5a91-35dd-a63b-e8375765b658 | -6.8216 | -59.1686 | 2026-09-20 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0b07d826-2c76-3276-8cc0-2016f2c682a0 | -12.0267 | -50.0231 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 8ee8d8a1-643d-3a3c-a8ee-34bdc915fcf0 | -11.3617 | -44.0817 | 2026-09-20 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 30f00433-2452-3144-9bc2-5cc78f11af93 | -6.1109 | -57.684 | 2026-09-20 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 986f82bd-6b21-35e2-ae6e-3e3518074264 | -11.379 | -51.42 | 2026-09-20 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 222.1 |
| c6d09918-f576-3301-beb4-3edc3c2aeb91 | -6.4302 | -59.9724 | 2026-09-20 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 180.0 |
| 64ce81e7-d022-3e7e-b2c3-a49329c7e41e | -12.2341 | -50.1703 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 3dddfba0-7496-3941-b225-1507c2b7e37a | -10.2784 | -50.2818 | 2026-09-20 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 308308c6-fa3c-37cd-a264-7c0f202013a1 | -13.9448 | -47.8494 | 2026-09-20 15:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| c0f6ad13-c2cb-3b8d-aaee-661b5fc19f47 | -13.4139 | -51.7358 | 2026-09-20 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| b85df37b-05a6-31f1-b22a-56deb7fd4cc4 | -3.3359 | -58.1191 | 2026-09-20 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ca16d49f-315f-31c5-87f1-9c375ea36f44 | -6.8433 | -55.7602 | 2026-09-20 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b7793775-6351-3c1c-ae1d-16560efb3f82 | -11.3793 | -51.3989 | 2026-09-20 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 2cce6359-cc39-395a-827a-c01232af63ba | -12.5081 | -50.952 | 2026-09-20 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1f599a95-6b16-358b-85da-0e123603c398 | -11.6621 | -50.2169 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 96e868ae-6a03-3c71-83ad-9a3b56b43bf0 | -9.6853 | -54.3318 | 2026-09-20 15:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| e10a493f-3892-3b56-a9b6-67c40954e3e6 | -13.5911 | -51.458 | 2026-09-20 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 66ee2574-c385-31e9-a83f-9da22eec6c72 | -11.7823 | -49.8152 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| ab9873fd-322b-3a5e-94a4-b4da2e76408f | -10.2976 | -50.2585 | 2026-09-20 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e2931536-0c75-39ef-b12f-c255c991fb72 | -1.5858 | -54.4353 | 2026-09-20 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 3c3174f6-794d-30f7-9b00-4663902542fc | -9.0355 | -48.7487 | 2026-09-20 15:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 42f46259-1a04-3762-be1f-69bb40352dac | -7.3564 | -44.4726 | 2026-09-20 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 82d5fe9f-460d-3c32-abda-796c9a216a47 | -7.785 | -44.8212 | 2026-09-20 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 6cc1a6f7-9b69-3ec1-b8f6-7919898a2a98 | -8.7003 | -45.4567 | 2026-09-20 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| fc6b35b5-665b-3b49-af59-a3a8bc0579a6 | -10.0953 | -48.4445 | 2026-09-20 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| d93c2bf5-215c-3085-80da-dc5b6956b8ed | -10.867 | -56.1975 | 2026-09-20 15:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 8aef401e-fedb-317c-95cc-d628756b916b | -3.3493 | -59.8288 | 2026-09-20 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 8fc5716b-eb21-3df8-b108-40086413e571 | -11.731 | -50.7014 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 172.5 |
| f389e81b-c340-3123-9ea3-b85af026000e | -7.8787 | -44.8577 | 2026-09-20 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 9b8fa69f-2f39-3b64-a20d-d42e05003873 | -11.75 | -50.6993 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 0fa9dc8b-07e8-36b5-b737-155f36a35306 | -6.1112 | -57.645 | 2026-09-20 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| eee12ff8-730b-3126-8ca2-9b993a0ca296 | -2.8961 | -58.3018 | 2026-09-20 15:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 56f22f21-b33c-3fb7-b8b3-c3444093ccaa | -8.3584 | -47.2157 | 2026-09-20 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |


[Clique aqui para ver as próximas entradas](README134.md)
