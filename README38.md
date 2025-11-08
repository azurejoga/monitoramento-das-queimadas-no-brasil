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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77bd32c2-f7bc-3ac0-8a29-879f90149f1b | -9.71533 | -61.2989 | 2025-11-08 05:48:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbfd312d-44d1-3460-bc5c-313b9e2196f0 | -10.18992 | -62.14797 | 2025-11-08 05:48:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bae3266-0fd9-3190-8c0b-a0f1f1200496 | -9.86629 | -64.8873 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca049db3-1307-343f-8633-90de26bccefb | -10.98813 | -53.98561 | 2025-11-08 05:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c50fc74e-aef2-3467-abb6-2fdb9b1430b3 | -9.58167 | -66.68819 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc9b9505-b159-3b8b-92ca-4edcdd90a71d | -7.81111 | -61.57299 | 2025-11-08 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88a0b477-5095-377f-a1ba-615f65699b34 | -9.42736 | -64.36388 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3fbb7d92-7b9b-3f69-a816-9b5d33671156 | -9.56402 | -66.05151 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81625f66-e5cd-3f87-b044-1071bfe6155e | -10.9995 | -53.98825 | 2025-11-08 05:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 181ae260-dfcf-341e-9163-ee0ca6bb6e34 | -9.68458 | -66.34939 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32a7cea7-7dd6-3be0-bf5d-def038a9376b | -8.6239 | -66.81304 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb217865-9084-3476-a6af-e5f5bc306764 | -9.92736 | -63.64014 | 2025-11-08 05:48:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6c97579-d2c3-3233-bd03-999d285717c0 | -8.59857 | -64.11225 | 2025-11-08 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 620f9afc-a0e9-3165-a546-bc3df33110c4 | -8.01764 | -61.52079 | 2025-11-08 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a05b1bf5-3c41-3ad9-85e1-c25e3b76f414 | -9.27158 | -63.19691 | 2025-11-08 05:48:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b2a994c-eff9-39af-bfe3-c7648494a602 | -9.77811 | -62.50542 | 2025-11-08 05:48:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 813cb693-3dac-35d5-8ece-6ce35ba69a04 | -10.06489 | -63.05267 | 2025-11-08 05:48:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2979096c-592a-32a8-acc1-6da315237302 | -8.67308 | -66.86708 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bc18e17-d3b2-3678-aa69-97c0f28c5c35 | -8.60487 | -66.8023 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b54d68b3-32f4-3871-bbda-f530e8921bfb | -9.85878 | -65.26031 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c56f80d-4fab-3320-b0b9-fba3fcb9f7de | -9.30712 | -65.8231 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a748d06e-93d9-3735-b400-1211cd5bce37 | -9.0948 | -66.00539 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62809d57-0185-3374-ad76-e7b8d40c70ca | -9.96176 | -64.73357 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 905d114f-43ea-3a45-a63a-07e756613fbb | -9.96057 | -64.74165 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fe012cc-d192-3614-969b-6ef9e9560f97 | -9.09535 | -66.00181 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e385f76-2422-33ad-8752-b2c5104f1b48 | -7.01312 | -71.62964 | 2025-11-08 05:48:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83b4162e-a8d9-32f1-ba45-01767b53834b | -8.62667 | -66.81704 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d2b2dc5-ccab-37be-a9be-3e635c42add0 | -8.63335 | -67.03508 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eb69e6c-e713-3d08-924d-263fad6cabe4 | -8.56522 | -67.01303 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e35aa98d-c92d-37f6-a6aa-90ca3eca6326 | -8.62075 | -66.76559 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f6b7d64-bbf6-3049-85fd-bfd90883f309 | -8.60516 | -63.33283 | 2025-11-08 05:48:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 486a833b-abe8-314c-95cd-74722999b0a9 | -9.42981 | -64.36274 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21624007-ad39-30d1-8686-032faa1cac00 | -8.73151 | -66.66577 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0315ebd4-3e7d-3096-a95d-df6f94d50e9d | -8.25773 | -71.11684 | 2025-11-08 05:48:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 488adaf7-d090-300f-98b4-7400bb9df641 | -8.63941 | -67.03959 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 043c79e5-8a0b-38a1-be25-5b56fd456e14 | -9.30656 | -65.82674 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de037d53-cee5-3fae-9af7-7379fd745406 | -9.44216 | -59.20864 | 2025-11-08 05:48:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| ea8ad80e-6363-3333-a8bc-3935b106913e | -9.94011 | -55.547 | 2025-11-08 05:48:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 22c59105-2b8c-3425-8b95-6cbfdaf6b69d | -9.08247 | -61.69012 | 2025-11-08 05:48:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30025585-4c21-38da-a47d-cc9ffbb3f849 | -8.63665 | -67.0356 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51719d9e-f870-3915-bc34-9939f666c9f7 | -9.30938 | -65.83092 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f76e2e2a-5c51-3c8b-a577-9fdcde78d700 | -9.27236 | -63.19538 | 2025-11-08 05:48:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f3e76ac-302d-31e9-91df-4f4816f664fc | -8.6328 | -67.03855 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6861caaa-e87a-37fd-9a78-7cb89c26c0c0 | -11.20217 | -53.82497 | 2025-11-08 05:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0bf4fc80-0909-31e6-803c-3108e5702ab6 | -9.54366 | -66.73618 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eabfb34c-2a85-3d09-b3d7-b0b02767f985 | -8.6246 | -66.76263 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36dc9910-1381-3904-8539-d5d3ed2db2ea | -3.9292 | -45.0128 | 2025-11-08 05:50:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| fe318f2a-6dfc-3541-981e-d42d09c554f5 | -3.6634 | -45.9463 | 2025-11-08 05:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 112.8 |
| f2b4311c-3aa0-3c97-abc3-7ead8793e7f7 | -12.43157 | -63.16199 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c611afd7-0b27-32fd-9c31-b4ab3dfac22b | -12.4574 | -63.15147 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0764f4d4-f59f-3e8d-8e66-ee80ff26aed6 | -12.43603 | -63.15907 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4076c649-1416-3d16-ab7d-37a1c28c2568 | -12.45293 | -63.1544 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c29e34b7-9b0a-39fb-9a0c-47f671becdea | -11.85159 | -63.67934 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d33f020-4d29-3532-957d-fb513306571a | -9.66604 | -67.02113 | 2025-11-08 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bdbb92e-07ca-3606-bf70-741a53d09d5c | -10.28592 | -67.27731 | 2025-11-08 05:50:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e8e8ead-6e13-3ef1-b2b0-a2e1998df91d | -11.71954 | -61.42164 | 2025-11-08 05:50:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 054e8f18-6a55-3397-a4fd-270e60137e2a | -11.86766 | -63.36554 | 2025-11-08 05:50:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de057d71-421e-3937-bf1d-d95a5a4d4baf | -11.73413 | -59.31229 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 12e72be1-6543-3322-815b-e909a1983a3d | -10.28262 | -67.27678 | 2025-11-08 05:50:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dcdc1c55-4fa1-3dd1-993d-77fbeea4717c | -10.85763 | -69.39697 | 2025-11-08 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66fe8198-d489-3e89-b35c-efdc001f68bd | -11.56223 | -61.6947 | 2025-11-08 05:50:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d759aa4a-cb9a-3a07-8b5e-8131be153315 | -11.7294 | -59.30838 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 998b4ad5-bf39-3707-8f1c-6687997302b4 | -9.62494 | -68.60054 | 2025-11-08 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84680cf1-a82c-396c-bb64-fdea5c714b12 | -11.73023 | -59.31873 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5842fede-f0fb-3f4b-bd16-50bdb45f87cb | -12.58877 | -62.9808 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b460e35-db15-3ee8-9ca4-f2073f040dbe | -11.73451 | -59.30918 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 477ebfcb-b88b-37d1-a687-e8843ea50c6f | -12.43555 | -63.16258 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64c53dd9-5f42-309f-bdf6-34458deca77b | -11.73613 | -59.31332 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bfbc8ce2-2348-3fd5-9c39-ffa10db5a495 | -11.06064 | -60.88256 | 2025-11-08 05:50:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 970a1722-b029-3d5b-a0de-5b868c099641 | -10.28316 | -67.27328 | 2025-11-08 05:50:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 96d234bf-55b4-3e97-b8f0-88d15315faea | -10.94498 | -65.20716 | 2025-11-08 05:50:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6a60806-2d3b-3345-a041-595e03b10df9 | -11.75584 | -61.07551 | 2025-11-08 05:50:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a939088-b1d7-3300-93fb-9206637b09a2 | -11.72827 | -59.31772 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 445e3dd0-ea64-3a28-977b-bf131d708e94 | -11.85226 | -63.67453 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58e020bc-b105-3fc5-bc69-07606283ac70 | -11.96636 | -64.03928 | 2025-11-08 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90941ab2-4f3e-3df7-a537-5958b0d318d0 | -12.44894 | -63.15381 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc30629b-5d31-3923-bada-94299ee672e0 | -9.74835 | -66.49043 | 2025-11-08 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c01e9064-9550-3d61-b8ec-9bfc46d58767 | -11.73184 | -59.30633 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62b90aeb-548d-35cb-b478-96dd506d69cb | -11.71963 | -59.32031 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28e00fc7-19c3-3ab7-9423-65ab3c372f19 | -10.51919 | -68.04807 | 2025-11-08 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a6e38cb-835d-316c-8030-32ffa03334fc | -10.26463 | -67.37041 | 2025-11-08 05:50:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17a755de-2d94-3cc9-8cec-f28c53ed0ad9 | -9.62828 | -68.60107 | 2025-11-08 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca0139bb-993f-3a61-8615-38395797f3d4 | -12.45341 | -63.15088 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3da1b395-10d7-36e0-add7-8c200227a937 | -11.86554 | -62.89077 | 2025-11-08 05:50:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9706f53b-14c4-38c8-85d9-e3588d07ac6b | -10.28647 | -67.27381 | 2025-11-08 05:50:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 22b9c353-e7a6-36ce-ad6d-a4b3bab513ba | -9.62551 | -68.59697 | 2025-11-08 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ccdeaa5-3693-3c53-8178-3840ff4bdae6 | -11.86603 | -62.88723 | 2025-11-08 05:50:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cbeae39d-21ad-3973-aae2-b4c1881c83ba | -12.41339 | -63.13026 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d957262e-d413-3a6d-8742-8a3ea8655198 | -11.14083 | -68.69845 | 2025-11-08 05:50:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9abd2ff3-1ab4-3360-bc4f-2e3c94cbff5f | -11.05752 | -62.54515 | 2025-11-08 05:50:00 | NOAA-21 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5a6a85f-dfa5-3ff2-ac9f-3e3bce9962e9 | -12.14236 | -63.05638 | 2025-11-08 05:50:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87d99e4b-1980-36ed-8762-e19e89378b3e | -11.72753 | -59.32385 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1675c5ca-c36b-32fe-a090-990853439590 | -10.05361 | -64.99105 | 2025-11-08 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ea7927d-20ba-3b49-a3f0-38c3e8ddca95 | -11.73654 | -59.31022 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42399a09-695b-3f50-8f7f-b4d172b0e9b1 | -10.63628 | -63.47494 | 2025-11-08 05:50:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d12a73ec-ba8c-347f-916c-c5cb47b4e4a6 | -11.72978 | -59.30528 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aca6effc-964e-32a9-9532-c00d899badee | -11.23888 | -62.61608 | 2025-11-08 05:50:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6301ac43-d1d9-3116-aff2-8636c2abd899 | -10.64234 | -68.89914 | 2025-11-08 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b84ac079-8b8c-37c2-8109-9fbf00f9719f | -11.71012 | -61.42467 | 2025-11-08 05:50:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9276f9d7-92b9-357f-adcb-05f0f4ea3d87 | -11.86957 | -62.89134 | 2025-11-08 05:50:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README39.md)
