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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e6f4b03-b9cc-3168-aa9f-530636120730 | -9.71386 | -48.2974 | 2025-09-12 06:08:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a06cc9b4-0d04-31ac-b467-0aa7d3285200 | -9.0364 | -47.06345 | 2025-09-12 06:08:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| dce27867-8b1c-3af0-abb1-fb8571556ff7 | -6.96233 | -44.82952 | 2025-09-12 06:08:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1973a259-e359-3e5f-89b8-f9030720e785 | -9.06444 | -50.50253 | 2025-09-12 06:08:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bcd5694b-b387-3440-90cf-b1364174d1c0 | -9.0649 | -46.94724 | 2025-09-12 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1457291f-4e27-3173-8b10-8882d9431943 | -8.9517 | -46.72996 | 2025-09-12 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| d16faeb8-8b6c-3e70-8768-5a13f88e75a1 | -9.6761 | -47.5376 | 2025-09-12 06:08:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3c6f6bf0-059b-3296-859a-1db769536453 | -8.88274 | -49.93199 | 2025-09-12 06:08:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9879cce2-1568-3e30-8ea6-7540ee2ddb79 | -4.48012 | -48.1134 | 2025-09-12 06:08:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 61595fbb-9a50-3990-9b83-b13fa0fb153f | -9.77673 | -47.85397 | 2025-09-12 06:08:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 098f9153-bc97-31c5-907a-4ebdc595a2ab | -6.82341 | -52.78576 | 2025-09-12 06:08:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2566da4a-7059-3c27-bded-a79a3148828b | -8.42649 | -47.25235 | 2025-09-12 06:08:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 87bfeb47-12ec-3e5c-840a-15f464fedcc4 | -8.8902 | -49.94213 | 2025-09-12 06:08:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 49c7cf0b-f16e-39ca-9e69-75d7bb711c0d | -7.75325 | -44.76115 | 2025-09-12 06:08:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 4dea5183-a6c1-329d-9910-af9e29e228d4 | -8.17948 | -46.09816 | 2025-09-12 06:08:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b614a81e-7314-3b6a-8eff-19eaced48cd0 | -9.0462 | -47.065 | 2025-09-12 06:08:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e8581260-0cb6-3f48-a1a8-2817fc3ae385 | -9.05095 | -47.03206 | 2025-09-12 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f7ee297d-d400-32ff-876b-f46698e2a7f5 | -8.087 | -50.18722 | 2025-09-12 06:08:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 33b3301a-1c72-3b3b-9fa7-6e4d2a9185c1 | -8.89286 | -49.92447 | 2025-09-12 06:08:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ddb0a164-fa7c-3617-9a51-97da3b3dc6a2 | -9.07321 | -46.96013 | 2025-09-12 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| af0b8255-669f-3ed4-aa82-2ba8a09d2c9d | -9.7782 | -47.84359 | 2025-09-12 06:08:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0be1b3c4-37a0-3f2a-9bf1-a13e121a279f | -6.68272 | -44.12599 | 2025-09-12 06:08:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f4da752b-3750-3e83-b004-6d5bb2102f29 | -3.22254 | -47.12603 | 2025-09-12 06:08:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| facca182-e84c-3cdc-843a-bfd10dd59de7 | -9.03795 | -47.05266 | 2025-09-12 06:08:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c28ed69e-a227-3b8c-8b25-cb016a28d938 | -9.07485 | -46.94827 | 2025-09-12 06:08:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 97234d96-8760-323e-bbb5-e8bc32f81573 | -9.04934 | -47.04322 | 2025-09-12 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 66722915-4d6e-318d-985c-6e5eb847865a | -9.86689 | -46.4809 | 2025-09-12 06:08:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8d075727-0130-3b20-b1a2-ab482c5d8931 | -9.03483 | -47.07439 | 2025-09-12 06:08:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 72ce2524-fbb3-36e7-b7b0-849da42152a7 | -9.72391 | -64.93244 | 2025-09-12 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89ad0cee-64cd-3eff-bf0b-70462005d924 | -9.44323 | -67.06929 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80cb87f6-1aba-3faa-bb75-aaccaa5847e6 | -9.05069 | -67.45278 | 2025-09-12 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52568f52-658c-340d-b30a-48c5decb22fe | -9.81008 | -61.51484 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5e1644f-dcba-34db-b02a-9a6004f51650 | -9.21374 | -59.3884 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a9d40b6-cea5-3e59-938a-a17de64d606f | -12.42028 | -63.88916 | 2025-09-12 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca9188e0-5c80-3639-87c1-1ba3dbe003d4 | -9.35268 | -65.45508 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f00f5130-441b-3c11-837a-e2e489adec44 | -11.10439 | -68.69688 | 2025-09-12 06:08:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b33c9175-11a1-3911-805c-1efeb1b0c473 | -9.33369 | -65.73144 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6a3ecea-a994-3bed-8489-37e9ba371f57 | -11.87196 | -58.81643 | 2025-09-12 06:08:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d452c301-6188-35d0-abec-ab16c7c361bf | -9.50107 | -66.79788 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8e6d2f3-ccd5-30ef-b505-b6a49c1bd94a | -9.28889 | -65.60737 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f86fd21e-1124-3f92-8cad-a09d6be329ed | -9.21976 | -59.39539 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d516b6ea-3df9-3f25-868a-2033249f897a | -9.50054 | -66.80169 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2f15269-65e5-35dd-917f-a1e85591755f | -11.87494 | -58.81399 | 2025-09-12 06:08:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2f47d45-f449-3733-9e79-395cd5bf9342 | -9.29014 | -65.59836 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8e635b46-e617-3d92-9a8d-367273f447d5 | -9.2145 | -59.38218 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24925555-63a7-35fa-afa4-8ba222ae1afd | -8.88008 | -69.34983 | 2025-09-12 06:08:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4af18a78-28ad-36f3-8bb0-12c14ce6f127 | -9.50299 | -65.58139 | 2025-09-12 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2264783e-a21c-35f1-9907-5fed1bc181cf | -9.34776 | -65.45152 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17859425-278b-35a8-bbe2-315e43bc81ce | -9.79213 | -61.51262 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97eb9c04-b844-39da-a3e0-c1ade9a97602 | -9.3475 | -65.45908 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 643b2ee2-78f4-3919-bee1-d0eaed81f440 | -11.86692 | -58.82086 | 2025-09-12 06:08:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45aa697b-f62c-39ca-b68d-f3fab0241b38 | -9.79811 | -61.51341 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 199fe1d7-0cee-3383-9a36-f4a3361997df | -10.39378 | -69.70659 | 2025-09-12 06:08:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 722e780b-2547-30a6-9862-6b2bbf616bf9 | -9.72937 | -64.92799 | 2025-09-12 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7465ab5-9862-33f8-85d3-72fd40ddf346 | -9.33309 | -65.73585 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d88f317a-c802-3ce7-bef2-265e3bc0127e | -11.87349 | -58.82769 | 2025-09-12 06:08:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16a7ed84-23fb-3255-b9d8-ace421fd263d | -9.23474 | -65.80027 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 772f0547-d350-3312-82dc-a581ddf29739 | -9.80952 | -61.51933 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63d3e222-10b8-3d62-888e-8b3aef8dac0a | -9.29852 | -65.60417 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 15024c32-b899-3c2f-94e8-f87146103c91 | -9.33491 | -65.72247 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f3ca6b6-5c35-3d4f-abcd-d63f8ee693ff | -11.86769 | -58.8136 | 2025-09-12 06:08:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5154411-dca5-3c0a-bdf3-991554468ed1 | -9.34813 | -65.45444 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35f356f7-4df8-3f9b-aac8-c90c8eb3036e | -9.22127 | -59.38298 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61cf2f78-0183-38e5-bc98-734cfcc5e9e8 | -9.79756 | -61.51783 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b13d498-2dbc-334b-b872-4d901ed1f8eb | -9.50752 | -65.58204 | 2025-09-12 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 199197d7-da6f-35d6-a6b8-8709781d5404 | -9.51205 | -65.58268 | 2025-09-12 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 92af67c8-274a-3302-a38c-06e406b3217c | -9.80895 | -61.52382 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74abf8c7-5406-3a2e-b542-874f234d84e5 | -9.23919 | -65.80087 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b00f61c0-b65a-3b18-82f0-b9f9ea1b50d0 | -9.35231 | -65.45216 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd3cbd2a-fdcc-312d-86dc-7c9fccdf2956 | -9.29529 | -65.59445 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 70b068eb-b2ac-368c-8b5a-966b8674e0c7 | -9.80353 | -61.51863 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4cbbd80-d84f-3ce5-b3a8-a5ca737184e5 | -9.32982 | -65.7264 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2289611b-3cb1-3a89-a0a2-6afc8a7850e4 | -9.29078 | -65.5938 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e1878250-333c-37aa-b67c-a5f86e2199c5 | -9.34875 | -65.4498 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd814d4b-c560-3f84-abf9-f5c5b8c39a90 | -9.03732 | -65.40259 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 118e60e8-ae85-34bd-87d6-0f7d0cb42ff5 | -9.33343 | -65.45426 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fb76587-8f83-3c16-a936-bbb9e1fc2d03 | -9.33799 | -65.45489 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71488e85-b2c2-3a5a-bcd6-f99bb30d21f1 | -11.79503 | -62.73783 | 2025-09-12 06:08:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 79a4d8e8-6ebd-30d8-9eac-35b7b1acf2d1 | -9.32862 | -65.73525 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c836d65-28d2-3b37-8a37-83f016dfb687 | -9.33733 | -65.45954 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12411cb7-0e15-3f9d-98f0-7ab0e078b324 | -11.87417 | -58.82125 | 2025-09-12 06:08:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ebc98af-a44f-31d9-80bb-f9acdeab1f88 | -9.3471 | -65.45615 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9ab042e-fb81-39d7-ae2c-94d2f9b8c9b3 | -11.87118 | -58.82341 | 2025-09-12 06:08:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44795684-03d2-315b-95bd-0e14db46cda7 | -9.3432 | -65.45088 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc742f43-c96d-3986-b93b-f0fa41f15cef | -11.77556 | -64.93884 | 2025-09-12 06:08:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49ac5f86-3c74-3268-af90-918d4ec62a45 | -9.32921 | -65.73087 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40f77a95-1fe3-3966-ace7-9f54123f4fad | -9.5016 | -66.79408 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbeed931-9850-30a4-b551-6b8d998cc706 | -11.10506 | -68.69223 | 2025-09-12 06:08:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0350e1dd-27ea-3112-a292-889a5907ab54 | -9.35166 | -65.45677 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17261332-eb22-317f-8877-41f204a0eef6 | -9.80297 | -61.52306 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87639c39-11fa-31c3-b470-075f09e307a1 | -11.87846 | -58.82354 | 2025-09-12 06:08:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7294d88e-266a-397d-8532-01e49b10d3ac | -9.29465 | -65.59901 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c700f322-fd5a-385f-8c82-6e9ed949ad7a | -9.22051 | -59.38923 | 2025-09-12 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68c69f1c-993a-3a0c-9f27-f586f5c7f934 | -9.33277 | -65.45893 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f89623f4-2da7-392c-858e-5732d202755c | -9.72462 | -64.92732 | 2025-09-12 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60bb7208-6534-3e18-a1ad-06690339a2c7 | -9.29339 | -65.60802 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d1281f3-1fae-3029-b658-ca1cb3be4de1 | -9.72866 | -64.93311 | 2025-09-12 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44b5d709-c39b-3ffd-8e6d-17a923111b74 | -9.3343 | -65.72698 | 2025-09-12 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0db25f97-7077-3d89-abd5-d54615bd3495 | -15.9264 | -51.8001 | 2025-09-12 06:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| c3a14fba-954f-380b-8fb5-1040e2faa42c | -11.5454 | -50.4019 | 2025-09-12 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |


[Clique aqui para ver as próximas entradas](README117.md)
