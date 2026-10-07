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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dea3fb87-ed1f-3fbe-8180-9a04e5aa468e | -9.3394 | -65.4638 | 2026-10-07 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 3ce10470-abd1-3489-ad96-dc49fd080aa7 | -7.7579 | -54.9499 | 2026-10-07 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 9290a709-0cee-3617-9dca-ab45bb556096 | -6.3283 | -55.3276 | 2026-10-07 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| fb4507fa-9c72-31c8-9488-196ce26d6a72 | -11.8508 | -43.5361 | 2026-10-07 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 349.5 |
| 8ba02f9b-6266-3c07-8a5e-43ea85bdcefb | 3.0916 | -60.5757 | 2026-10-07 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 0dd33a14-c007-312b-bb33-325c6a7806bd | -12.1746 | -44.7051 | 2026-10-07 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 1e25bfdf-01fb-3ff0-aba6-b621f2970c02 | -6.4941 | -52.8132 | 2026-10-07 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7a623a5c-096d-38c5-ab73-1a9a8cd039e3 | -6.3492 | -43.8237 | 2026-10-07 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 7e360ad8-452e-3ff0-9d12-bbfc5c1577ad | -9.3619 | -45.4288 | 2026-10-07 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 9a748ff2-a5bd-3751-8aef-3a03bcefc137 | -6.9927 | -45.0996 | 2026-10-07 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| aacd4182-0bf5-3688-a64a-91b27fd4c9f9 | -8.6033 | -45.6709 | 2026-10-07 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d5d26b60-7881-3303-999e-7a0ecf639345 | -10.6199 | -60.4852 | 2026-10-07 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 29be185b-c3d5-306d-82be-36395f5b110f | -8.9054 | -63.3378 | 2026-10-07 14:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| b3080e76-bc57-38f2-9c96-71f949bee59f | -8.3022 | -44.1467 | 2026-10-07 14:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| d8a7a638-baf1-30b1-b331-f5d2d9616f2d | -10.9575 | -45.389 | 2026-10-07 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 38e61527-8637-3875-8999-59c7d2372ba0 | -9.4131 | -45.8314 | 2026-10-07 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| bcd6ab51-8e64-3170-b510-df3739aca7f2 | -7.8676 | -44.2153 | 2026-10-07 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 91006553-3830-37d4-843b-7aee47f21201 | -6.704 | -44.0017 | 2026-10-07 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| ce13663c-803f-32c6-837a-1718e8fd5c27 | -9.1356 | -65.4145 | 2026-10-07 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 49a6c9bb-eace-3a29-b507-e95e43f36571 | -11.6374 | -43.664 | 2026-10-07 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 34c62a72-089b-30a1-8e8e-7acf8de75002 | -7.1814 | -55.1036 | 2026-10-07 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 3b86d837-2287-36f0-bd02-ec03e8522703 | -11.6374 | -43.664 | 2026-10-07 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ec90e170-a80e-3b33-a27a-d908e67a45b0 | -11.7143 | -43.652 | 2026-10-07 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 74b67351-6f02-3857-9f1c-cfb820287d91 | -11.0935 | -47.6019 | 2026-10-07 14:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 9505b3b1-bacc-399c-bca8-3823c781ac11 | -8.2184 | -46.3396 | 2026-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 7951ba52-38e8-3bab-bb90-43c4aaeb7c2a | -1.4569 | -54.7761 | 2026-10-07 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 8760c11d-f7d4-3a57-9a2d-3ecf5ff2ccca | -1.2922 | -54.5585 | 2026-10-07 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 75ff7d3a-5a78-3de8-8709-8c1f08e4e777 | -9.4124 | -45.8767 | 2026-10-07 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 614482c1-8975-35b8-9d67-d032ce9a241c | -12.1554 | -44.708 | 2026-10-07 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 29f6fe89-eca1-343d-a1d0-a61496ce2795 | -11.8508 | -43.5361 | 2026-10-07 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 257.4 |
| 7f3209db-ca2f-36ea-8a3a-8d52fc7dbc47 | -7.7595 | -43.8092 | 2026-10-07 14:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| e3d6ce35-8b6e-38f8-a84c-66d82eccc698 | -7.7579 | -54.9499 | 2026-10-07 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| c8e3c7f3-6eec-3cc3-ab9d-4970f185ccee | -9.4492 | -44.6167 | 2026-10-07 14:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 151f219c-216e-3c5b-85ad-a65583eb9d47 | -7.1813 | -55.1237 | 2026-10-07 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| c9e26586-0731-31a5-87cd-42aabf1beb5b | 0.7266 | -51.3749 | 2026-10-07 14:40:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1f903f3f-e9fe-39dd-b911-17d2fac82a1e | -4.3154 | -42.9904 | 2026-10-07 14:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| c0dbf168-9ca6-3cc8-a72d-a91be111c328 | -8.9054 | -63.3378 | 2026-10-07 14:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b8edd0c8-c4fa-3ac9-8a31-597f95ef75aa | -11.0137 | -45.4501 | 2026-10-07 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 3f99b647-b644-3930-bda3-03c14e5bf0d2 | -8.5844 | -45.6729 | 2026-10-07 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 5277e6d3-c710-3272-83f2-f4c67e4e0ec7 | -6.1974 | -52.8295 | 2026-10-07 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 15326f5c-5b6b-3cf3-a8d7-b392f457e446 | -6.1217 | -53.0584 | 2026-10-07 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f5e52558-c126-34c6-b3ed-5045a308b229 | -8.1996 | -46.3415 | 2026-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 46e1d120-810c-32d4-bc94-6e0ef528c936 | -7.1814 | -55.1036 | 2026-10-07 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| e1dbe5fe-92b8-36cf-aec7-4497c423a01d | -7.3935 | -46.2144 | 2026-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a5c9e35b-b4c8-34b5-802d-397b62e82603 | -7.8789 | -72.3674 | 2026-10-07 14:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d211c47d-d650-3768-bf87-38de9d25a697 | -8.8364 | -62.4321 | 2026-10-07 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 838f51ad-2e3e-3509-b2f0-f79e08a1d23b | -7.8789 | -72.3492 | 2026-10-07 14:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 119.4 |
| defe03a7-3bf0-31cc-a27e-9210ce548899 | -11.2295 | -46.2403 | 2026-10-07 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| b8fc0af9-87ce-31fd-a9c8-ed68c9226e5a | -11.065 | -45.8084 | 2026-10-07 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| a5c7c637-61b8-316d-b28f-402ce43eea34 | -11.2337 | -44.8446 | 2026-10-07 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 194a68ec-4732-3d89-9d4d-2887d5e52316 | -9.3395 | -65.4451 | 2026-10-07 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 5e8e1cb9-ffb0-3420-8219-777f295b77f1 | -10.6199 | -60.4852 | 2026-10-07 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 60f410dd-93cc-3fdd-8ca9-508ee9aa5f86 | -6.704 | -44.0017 | 2026-10-07 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 2e0de4d8-591d-3df9-93f5-a1fe96f5102a | -6.1977 | -52.7886 | 2026-10-07 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1ed651b9-e519-360b-8516-42f7a61f5081 | -12.1935 | -44.7254 | 2026-10-07 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 5e823c2c-c1ea-3b37-a0b2-d970b6b3068e | -7.89 | -54.7206 | 2026-10-07 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 42e8d77b-819a-3f1b-a57d-bf0833a3ad17 | -8.3391 | -72.6012 | 2026-10-07 14:40:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 9c2d0fb4-15b5-3e9a-94e6-208ba51ee7e9 | -6.7228 | -44.0001 | 2026-10-07 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 02b5996f-138d-3713-a48e-3136950bc798 | -7.5756 | -46.7112 | 2026-10-07 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| a3f40b5e-4e08-38e4-a9fe-c0d773e09b98 | -6.2159 | -52.8285 | 2026-10-07 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 316.6 |
| 1c85d5ed-bea9-364c-9acb-629d83670420 | -11.3745 | -46.6948 | 2026-10-07 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 1871b691-9942-31fe-819a-a8ee126ff84d | -6.2161 | -52.808 | 2026-10-07 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7093b76f-f133-3743-9465-cb4983d63fb6 | -8.524 | -54.5987 | 2026-10-07 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 8cc44dc9-1b0d-339f-8697-14c00cd7dd40 | -6.0075 | -53.5122 | 2026-10-07 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| fd19a149-d6d1-3161-8089-e372101e8d0c | -1.8803 | -53.9701 | 2026-10-07 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f146729d-6074-3a63-bfde-08f6d821a237 | -10.8591 | -50.6692 | 2026-10-07 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a74410d0-2606-30b9-bbd4-c69aa7d06d51 | 1.6385 | -55.8047 | 2026-10-07 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 868fc550-6600-3e59-9630-87cd6db7a5e9 | -7.2 | -55.1026 | 2026-10-07 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 213.8 |
| e6b63656-ede4-3971-ad7e-3b63c348c174 | 3.1097 | -60.6133 | 2026-10-07 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 1904e3b3-2086-3ee3-9a9b-d7a96d0cb725 | -10.5287 | -47.2711 | 2026-10-07 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 8af8798f-8b15-3b84-a1d8-812a0552b20a | -10.9953 | -45.4068 | 2026-10-07 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 076f2750-aa9c-3cf3-a610-618926a799dd | -11.7362 | -43.5068 | 2026-10-07 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| ac2e4ac4-c541-3985-9e9c-6172e712c5ed | -4.1178 | -41.7963 | 2026-10-07 14:40:00 | GOES-19 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 7d7d56ac-d40f-30f6-bf36-eeb07f928894 | -6.7037 | -44.0248 | 2026-10-07 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 5052df4c-99c7-3e6c-a305-9b572d8ae977 | -9.8261 | -44.7781 | 2026-10-07 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 15fa3c0e-5f77-3775-800d-e0f138b1df40 | -6.694 | -44.9658 | 2026-10-07 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| fd316364-1fc8-3d54-a4e3-b7e357903e15 | -12.1742 | -44.7284 | 2026-10-07 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 404.3 |
| 73b11d3a-4727-3642-a307-71743a710056 | -6.4941 | -52.8132 | 2026-10-07 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f3e64749-7496-3dec-92f8-2f66459dc469 | -11.7139 | -43.6757 | 2026-10-07 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 7726f5a0-33ba-34df-a693-03eeba46d138 | -1.2455 | -49.062 | 2026-10-07 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 614f34e9-69f8-3bbc-aea3-5d416fbdfdde | 1.7671 | -55.5859 | 2026-10-07 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| aa7488d7-6eda-3efa-bc30-790d98e25fe3 | -7.5568 | -46.7128 | 2026-10-07 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| dd2e8274-de4d-3973-9674-3a164f014d99 | -6.0076 | -53.4919 | 2026-10-07 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 77f4b375-3eaf-36de-b3de-e44f2580cf39 | -11.2267 | -45.2604 | 2026-10-07 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 0c04b709-8fd8-3ebf-964f-3bb260da7340 | -11.1556 | -46.0916 | 2026-10-07 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| e0d6f785-a6b1-3e9a-bd74-13a548274006 | 3.0733 | -60.576 | 2026-10-07 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3f664518-87ad-3e17-ba4e-9c820d4ef442 | 3.5829 | -61.3432 | 2026-10-07 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 16dfe608-f75d-3085-a6d7-9f43ba444b00 | -7.5847 | -55.7205 | 2026-10-07 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8e6c4bb6-9a09-374d-9026-2d5d083bbd12 | 1.5283 | -56.0227 | 2026-10-07 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| feb0f12c-43fb-3f99-bb9e-5e5f84a0f72a | 4.2247 | -60.7051 | 2026-10-07 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2f9c74dd-394f-3615-bfd7-2055d52e2b8f | 1.7671 | -55.5661 | 2026-10-07 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 857bd0aa-d1cc-3416-b31f-dc38de3e7143 | -12.1746 | -44.7051 | 2026-10-07 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 377.5 |
| ee9e4238-0b14-3e93-be12-6daf909a1b8a | -10.8054 | -46.5662 | 2026-10-07 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 170.6 |
| efa1bc49-9db7-37fd-b41a-8fbcb38e1558 | 2.0048 | -55.8392 | 2026-10-07 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 17e3bb07-2ab1-3091-bb9f-e17eca8e39e9 | -9.343 | -45.431 | 2026-10-07 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| bd170c45-9981-3ed3-91a6-583e1b156ff5 | -6.217 | -52.6851 | 2026-10-07 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f03bd43e-c713-3f9c-9b6b-a1fb43d85b2f | -9.3935 | -45.8789 | 2026-10-07 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| d1374cb2-2aaf-3b3d-8bb2-61e0c46f1be9 | -6.1984 | -52.6861 | 2026-10-07 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 438a871c-75cd-37a7-821d-04df3eb34cb6 | -6.6943 | -44.9431 | 2026-10-07 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 71b8d146-d205-3135-a912-fc29904617a2 | -12.2132 | -44.6991 | 2026-10-07 14:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 207.5 |


[Clique aqui para ver as próximas entradas](README135.md)
