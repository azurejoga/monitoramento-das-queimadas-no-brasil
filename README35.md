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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de0a8239-79b6-3418-92d1-b1bcf6c0d443 | -9.006 | -65.4 | 2025-08-26 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 39899341-539a-3e55-b46c-dece5b45c2e4 | -11.502 | -52.1229 | 2025-08-26 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| c0b4b1d3-4f95-3112-bfd2-9d666e8747ab | -8.8734 | -62.4495 | 2025-08-26 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 8e8631bc-5dd9-37c2-9806-c5f681ee1aa6 | -11.521 | -52.1209 | 2025-08-26 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| d742698b-26f6-3b9b-b97a-830ccf7d1d08 | -9.1717 | -59.5405 | 2025-08-26 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| e72f0fc5-8431-320c-bada-241845da6ab7 | -6.2275 | -60.018 | 2025-08-26 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 22d785ae-82d5-3ee7-8302-f0bc72191bc1 | -6.2276 | -59.9989 | 2025-08-26 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 5e8c9b1a-331d-3926-b28d-90f39fb0f790 | -8.9874 | -65.4192 | 2025-08-26 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| b5e86ecf-6aa2-3c45-891f-d34617bbb53d | -9.1904 | -59.5201 | 2025-08-26 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0a5747e5-a09b-35ec-ae0f-57c0280a9d56 | -6.2459 | -60.0174 | 2025-08-26 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d538df68-1be0-3991-a902-857d29ab8f66 | -8.855 | -62.4313 | 2025-08-26 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 8f1cac5f-28dc-3fbd-8c44-e9dd766b1771 | -9.0231 | -65.7169 | 2025-08-26 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| a6df34be-3302-3a38-b1b2-94c8efe468ae | -6.8229 | -58.956 | 2025-08-26 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 143.7 |
| fa6a59a2-b057-3552-9f24-72fa18b1ce7f | -11.1591 | -44.7395 | 2025-08-26 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 635ac065-5682-3be1-8fb5-127d13973965 | -8.8548 | -62.4503 | 2025-08-26 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 148.4 |
| cb4ceea6-ec6d-31e0-8ce9-83e9cfa46fb5 | -6.8043 | -58.9761 | 2025-08-26 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5ec25f65-dd7b-36ca-8555-92ef5d47acdb | -6.8228 | -58.9753 | 2025-08-26 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 3a13a650-59f2-3ff2-876a-2470651f22e6 | -6.79713 | -44.34197 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99cff37f-df7a-3e8f-b17d-e5f20ebc5560 | -7.59498 | -45.2276 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1dd98e6d-951b-3faf-b66f-1cb813655c46 | -8.12692 | -47.12047 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18cdaaf6-3355-3d22-9ba1-b450e08ff177 | -11.14847 | -44.75304 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f134f5a-87bd-3edc-b333-9827b23e2765 | -6.08759 | -45.90437 | 2025-08-26 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 950afdc3-d612-3615-8cea-9bbf650aa849 | -6.29773 | -43.77779 | 2025-08-26 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37686bef-d68a-3dca-a420-e1a30be77a32 | -11.15907 | -44.75105 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d03705da-6266-36c6-afb9-d063108cebe1 | -8.24776 | -45.0994 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eda43623-a67a-37f5-90fd-0bdbdb08c9d2 | -7.65179 | -42.67767 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18dc37d0-e537-3894-baf3-f1f73cb96668 | -8.91253 | -44.85173 | 2025-08-26 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 748907f8-f1b2-3d93-b2ea-ce5ae18f61b0 | -3.42777 | -49.05144 | 2025-08-26 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e000227-7962-372f-9cf7-d1755bde713b | -7.3021 | -44.52846 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f7bdb05-41dd-3f35-acd9-ec5ccde58c50 | -11.29128 | -44.92888 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e99c4987-024b-34d2-b3b5-50f61d7eb269 | -9.06358 | -49.55724 | 2025-08-26 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66959989-afd6-3458-8694-8d98dbed16b8 | -4.07679 | -48.04726 | 2025-08-26 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea5b0183-f06b-3272-a50f-a48b56414363 | -5.8762 | -42.41213 | 2025-08-26 04:21:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dce62a1d-1af8-39c9-8318-488a22541de1 | -5.47035 | -42.61705 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3f99b1f2-b511-39d3-a3b1-1ed7d152e40f | -11.15016 | -44.76431 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a995dc6d-1b77-3aec-8cbf-b4e574acd715 | -5.48373 | -41.41324 | 2025-08-26 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aef2c9fc-0ee3-3f75-b9c5-81cc06015fba | -8.07467 | -47.30953 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f312590-7e45-35af-84f0-bdc7d2c21b34 | -6.5257 | -44.4347 | 2025-08-26 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca53eb9f-56a1-3df8-80c1-defc7f13f3f4 | -7.47686 | -45.03031 | 2025-08-26 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a53f7410-65d7-31aa-9f2f-e8608027685a | -3.91879 | -47.6861 | 2025-08-26 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbf21b8a-596d-32e3-b237-b2d953218cd7 | -6.8927 | -44.42148 | 2025-08-26 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c6bdb68-fdc4-3e30-a51c-1d78e7ba6266 | -7.30597 | -44.52551 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1fdfc4d-0369-387d-8fc0-26fd3e6124ef | -8.3093 | -47.24336 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ea0a515-2ad6-390d-90b7-6bf03f5b4318 | -5.47092 | -42.61337 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bd738784-644e-34cb-b74d-eb65e229140d | -6.34886 | -43.6596 | 2025-08-26 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb8e02e8-952b-3e31-bc9e-419b247a6d6e | -4.93749 | -42.72332 | 2025-08-26 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 847a880d-ba81-3434-8422-0d1ad8d3b7a8 | -5.81241 | -42.29814 | 2025-08-26 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c69e5a4-179d-3340-b03b-a76a581bcb99 | -5.55379 | -45.57032 | 2025-08-26 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17928a51-fd04-34b7-a169-43b638e9065f | -6.87495 | -44.40444 | 2025-08-26 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35a4217b-51ff-3830-9740-0e43352b1914 | -8.29289 | -46.3334 | 2025-08-26 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb64573e-51bb-32f2-97da-c627b313f0ba | -7.30264 | -44.52499 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 113f38ec-96e0-3fef-b043-f3e3f1ecb2cb | -6.34309 | -43.58631 | 2025-08-26 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79471c6b-e6e2-333b-ba09-f9ef2820edb3 | -9.10785 | -46.06873 | 2025-08-26 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 488ca858-45af-318f-a571-02139c87755d | -9.25655 | -56.90572 | 2025-08-26 04:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5cc983e-d1a9-3679-bd0d-a4c37f166c3e | -4.07754 | -48.04261 | 2025-08-26 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 388582dc-f62f-3113-88a1-91d3a10151c9 | -2.67718 | -52.16101 | 2025-08-26 04:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 394d333f-96ee-3db0-8f7d-ab9cd3695921 | -4.41265 | -40.48801 | 2025-08-26 04:21:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e4922f30-e284-3b2f-8255-beceb5230c36 | -10.70191 | -47.11984 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b612afb-23e1-3db2-ae3f-e5339d518887 | -11.06466 | -44.59642 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19c84c17-3155-3b8d-a16e-ddab86fb3a4d | -8.37955 | -48.02171 | 2025-08-26 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86965dd1-6f7f-397b-8194-92c24953ca2e | -7.73828 | -50.29976 | 2025-08-26 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac10cc38-1687-3bed-979e-52e02bb92f07 | -6.56349 | -44.21648 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cc871e04-2e9e-3df9-a072-6f91e8fb872f | -7.44559 | -42.04401 | 2025-08-26 04:21:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 522cbdd6-7b50-3900-abfc-dcbe5a54d810 | -10.40243 | -47.155 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ccf015c-c226-33c3-b6cd-26639bc07830 | -4.96626 | -55.81982 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9d92ce49-5146-33ee-806f-53c1b45bb89a | -6.86717 | -45.65493 | 2025-08-26 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9ea119c-361a-3712-8613-20747c5de8e7 | -8.32788 | -50.57143 | 2025-08-26 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e35fd99-40c8-386d-b700-cb4cfb61ca3d | -7.61502 | -45.22345 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9e5dec38-3246-3deb-ac02-d92b66c6b1c2 | -7.66169 | -42.65954 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee1af52e-9b75-3228-8c67-a962ceb78791 | -8.07546 | -45.00771 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17ed9176-7454-3893-9779-20edcd275efb | -5.77972 | -43.60721 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f4b4f0c-012c-3340-b629-da388929961c | -4.969 | -55.82238 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2a4152b6-77f1-350e-b79e-11376b0a3487 | -11.15741 | -44.76179 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 21fc1157-c1e8-3fe1-80e1-df9bd6b94800 | -8.28276 | -47.23103 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3e5776e-5dfe-390c-b03a-6c9ebc97b459 | -10.81011 | -48.32161 | 2025-08-26 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5043d040-1288-3cc4-88b4-f9c47590e045 | -5.65589 | -44.35065 | 2025-08-26 04:21:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7979b3ad-6c9d-3dab-8c88-41ba928a4bef | -6.14042 | -44.38802 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 638f0f73-ee55-3f5c-8b8e-8706e4306898 | -5.87275 | -42.41159 | 2025-08-26 04:21:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 55d76a8a-59fa-325a-8717-afd6fc5a6c98 | -7.64832 | -42.67713 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e3eb2408-1edb-3723-aa9d-21ac5fc5cd2f | -7.74348 | -50.30433 | 2025-08-26 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01808814-b52a-30e6-8764-5aa10cc1eb6a | -9.27101 | -56.91475 | 2025-08-26 04:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bb577da-8429-39ff-8623-e4144ba9d498 | -7.73582 | -51.14436 | 2025-08-26 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e723c54-6c40-3d66-91c8-14400f036a43 | -8.07022 | -47.29289 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b64ca66d-cdc6-3548-b8ee-b4530147e1c8 | -9.10842 | -46.06518 | 2025-08-26 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ff879ca-3cff-3c6c-9199-e7ba5ccf8a7a | -2.93014 | -53.70182 | 2025-08-26 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 875a5c52-ed57-3afe-86a1-83014b1d8c33 | -4.86159 | -47.41446 | 2025-08-26 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20a50070-9b07-3565-a422-6b37f0302e88 | -6.46176 | -43.58641 | 2025-08-26 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 957c87f7-4030-3723-8cfd-1fd1bdbc1089 | -11.14741 | -44.78216 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1151f092-6688-3a85-8e96-e869a86fde81 | -4.67985 | -41.02751 | 2025-08-26 04:21:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 762e0ab6-079d-3596-a3f3-fd996352f278 | -5.48558 | -41.413 | 2025-08-26 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4e206c92-5ce0-356d-a844-68a44671f5c2 | -7.17313 | -45.15673 | 2025-08-26 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b607f15-cf2a-346c-bfe3-b4fc97cac734 | -6.69916 | -48.38189 | 2025-08-26 04:21:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6e973993-99c5-32dd-8a5e-56972e6ce72a | -10.53993 | -46.80487 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eebe27f5-2eb7-3aeb-b449-47da8c27adfb | -9.74775 | -37.91486 | 2025-08-26 04:21:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2ce2bc3a-0d9f-3df7-9525-7e18750376cf | -7.01834 | -44.37714 | 2025-08-26 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14a670a4-8a50-3fa6-9471-db1c1078f779 | -8.30771 | -47.23126 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9a63c68-1c28-3c08-9bc3-d1c9a2a33986 | -7.59886 | -45.22465 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64eac316-cc21-3c87-ace7-527984fd9c62 | -3.37726 | -52.71587 | 2025-08-26 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51c745d1-b345-3f53-a5ce-61f59a70d8f7 | -11.08843 | -44.77609 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 963055c0-e4c0-308c-b6ba-007e31ca20da | -7.82115 | -45.22453 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README36.md)
