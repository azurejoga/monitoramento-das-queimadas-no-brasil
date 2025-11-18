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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5dc217ad-4abe-3972-b4e1-65e297644f1f | -4.17846 | -44.23971 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65affb46-9949-3173-96f4-f788db3f3033 | -3.65263 | -50.22287 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d8b65f2-583d-329e-bcf3-6d31a0442fb6 | -7.63073 | -42.58508 | 2025-11-18 04:21:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| aec1c357-f1cb-38fa-8ef8-883d37b47ab8 | -6.15993 | -46.10551 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aabda335-d293-369d-987e-23844130076c | -10.84724 | -44.1018 | 2025-11-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03ce18d7-af01-38d3-97af-571163915213 | -4.52935 | -46.41575 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6d1c516-b203-37d3-ba45-6afbfc4acb01 | -3.46922 | -50.23879 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5fd66ee4-c540-36a5-8737-abbf07565a8e | -11.43387 | -43.31745 | 2025-11-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97581c29-6fa2-350d-a1df-a738b4562166 | -8.29369 | -43.95459 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9408686b-b1ed-3c84-99a3-0c4044ee5cc3 | -5.4832 | -41.38261 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 47838554-ed23-391c-a8d1-3e7f10c2b4ab | -4.42626 | -45.54093 | 2025-11-18 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 010abd20-a91f-39cb-8fc9-348cac13c344 | -7.94538 | -46.82207 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25700b41-fb97-318c-a31f-801d29be7ce8 | -4.18507 | -44.24073 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a6d1673-38ee-34e7-b1df-41c6283cf913 | -6.35959 | -41.78679 | 2025-11-18 04:21:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3b0c4ccb-76b5-31fa-a522-c4dab3082a6a | -5.18557 | -46.07082 | 2025-11-18 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14ee3867-93b8-3405-9aea-2d99495ae752 | -9.84047 | -49.04839 | 2025-11-18 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da9d7ffa-cd6f-3047-a2b5-44588651b448 | -10.79781 | -45.15287 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a04c019-0ba4-393f-9c65-70f818052791 | -8.46325 | -44.70579 | 2025-11-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bb27782-d237-3491-bf9d-ffa04ca72fa9 | -5.95872 | -45.35933 | 2025-11-18 04:21:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1df9f1b8-92c1-3af8-97a0-22b1548dfc59 | -4.27247 | -44.24796 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa0a92b9-15c1-3d05-b9cf-71dd69669f3e | -3.14957 | -51.4922 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72b61ed0-917d-35c1-a818-a66807b5e1f6 | -5.47923 | -44.68953 | 2025-11-18 04:21:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7a08b66-f40e-3d26-b4cc-9838f27d5760 | -3.1609 | -50.16505 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d5c4af3-a67f-3a0b-8bc3-3bbc35e6a892 | -6.60918 | -47.79412 | 2025-11-18 04:21:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed4cf6a2-8ec7-3987-8685-8b681a47df19 | -10.76553 | -44.81224 | 2025-11-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 528a7b05-1e94-31a7-a524-43bced8eab43 | -7.94879 | -46.82264 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cdece9e-3b49-35d1-ad54-e756cc5bba16 | -4.64895 | -45.53145 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64df0512-c332-361f-b38f-e08d38c95972 | -4.27139 | -44.25483 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d35ad7b-b9ba-3233-8e66-1cab417da014 | -4.18615 | -44.23386 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9dcf62ac-43f0-3bfc-bc2e-0166574c8df8 | -3.80275 | -50.13018 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c305b1b7-8fc5-313f-a61b-83223bbfd575 | -3.64346 | -50.16954 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0f028f9-d6d8-38c8-8328-191ebab3c492 | -8.29974 | -43.93738 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 176c6a1f-e84a-3f52-a7e3-fdb6ff2826a9 | -10.29341 | -48.89882 | 2025-11-18 04:21:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f6ff38f-c78d-316c-ad13-93025398248c | -3.32909 | -51.5079 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eacdfef5-6cbf-355b-adc4-6e13815a7117 | -6.1607 | -47.34223 | 2025-11-18 04:21:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16ad6a00-fc1a-3dee-9478-db802dd2a490 | -10.50648 | -43.94866 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63e52497-f62c-3194-ae54-1ed99a1979f4 | -6.32619 | -46.12469 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95bc57b7-235b-369b-8938-650056d494e0 | -3.51505 | -50.34588 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71082037-f0f7-3918-a662-ce7898f1b2c9 | -10.50255 | -43.9518 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b190da9-674f-3452-9c2a-0ba710382acc | -5.38234 | -50.48403 | 2025-11-18 04:21:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcd6a634-b700-3abf-ab87-3dacc28d1886 | -8.29036 | -43.95741 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7339e252-a553-3bfa-9dcd-aa32ce93076b | -4.38335 | -46.03617 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0873925-22c1-393d-bc1f-2135e468fe40 | -10.76221 | -44.81171 | 2025-11-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d1ae6d6-a2bd-3172-a669-a94999de5456 | -8.46717 | -47.97697 | 2025-11-18 04:21:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b8a306f-6dd5-390f-af1b-defee2a5ecd0 | -4.97408 | -41.84841 | 2025-11-18 04:21:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6f35a147-7b5a-3648-945c-ef4c56696a15 | -8.21316 | -45.04306 | 2025-11-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a0098f20-412a-36aa-b418-38ef3c6eb9ec | -9.60955 | -44.37373 | 2025-11-18 04:21:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 940ce114-13e5-3a15-a19d-1873158820ef | -8.0934 | -46.05826 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac96a6df-8e9a-346a-aeae-102ea22efd5d | -7.07127 | -46.04771 | 2025-11-18 04:21:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a92bc0cd-014b-3f84-8daa-4048ec234489 | -5.75441 | -45.1021 | 2025-11-18 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e8cd900-f32c-3a4b-a7ae-4cdfc75f5163 | -7.96263 | -35.24376 | 2025-11-18 04:21:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| af7f1654-168b-3f99-a875-a963f223bb36 | -4.75877 | -45.77666 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62f2289b-edac-3d99-b9c2-0ed7921d8547 | -6.9394 | -49.67097 | 2025-11-18 04:21:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d267a743-92eb-3875-a2df-3e0d319bf7e1 | -7.96652 | -38.27732 | 2025-11-18 04:21:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 313a144e-2c3e-3de3-8ae6-506dadb4c6e3 | -10.29413 | -48.89451 | 2025-11-18 04:21:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29b668c7-c897-38f4-981a-2ad31611e480 | -4.53043 | -46.4157 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc7be44e-026e-38b2-8d2e-c6f8b996a0d1 | -7.38163 | -39.12718 | 2025-11-18 04:21:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5eae9d60-a25b-36a2-9157-6abb61269c31 | -6.1943 | -49.54016 | 2025-11-18 04:21:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b91a093-234a-3783-a02b-d6c643118008 | -7.14632 | -44.92562 | 2025-11-18 04:21:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3aeebb81-d395-39ac-8f42-79b055ebaf57 | -3.16455 | -51.49269 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| da4750b4-cf18-344e-aff4-89f3399e62c9 | -6.37139 | -42.31475 | 2025-11-18 04:21:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| de4ae217-fb30-3048-ba11-ee0681c5d5f8 | -4.7712 | -44.92838 | 2025-11-18 04:21:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e22fe098-5fc2-393e-95f2-7f11828e3f0e | -10.51834 | -43.96175 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edae5d8d-6546-3864-af4e-9ef9db7e0e5d | -4.14241 | -46.35582 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c8530ac1-979b-3c53-aeca-4cc7ee1f32fd | -10.66201 | -49.36821 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bce2cb9b-579c-32d3-ab69-e3a903ab4c62 | -10.85395 | -44.08047 | 2025-11-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 850f74e6-b592-3f2c-a538-618b1c2f9e9d | -9.74291 | -43.94376 | 2025-11-18 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 53283434-217c-33ae-a9a1-bd44234154b1 | -8.58658 | -44.10863 | 2025-11-18 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56a5a7c0-3642-394b-b1c4-1cd662263cbb | -4.42965 | -47.57696 | 2025-11-18 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22d62ad5-56f0-3ed8-a502-689e4dccad9f | -5.36414 | -44.85842 | 2025-11-18 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e9e21563-72b4-32f1-b0a4-afd39c806efa | -10.85454 | -44.09922 | 2025-11-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1a022dde-07d5-393b-b489-a824109bf276 | -4.14302 | -46.35198 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2b0252d9-81c2-3389-8c9e-426749fe4165 | -5.03981 | -46.82483 | 2025-11-18 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc7f76eb-ee82-34ae-8bf9-22b4223652d4 | -3.64414 | -50.16537 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98fdda45-8cca-3344-a492-9470dd675e34 | -6.3584 | -41.79478 | 2025-11-18 04:21:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 18666161-2d78-3e10-b5cf-bdb031a5a1ba | -6.71442 | -47.79361 | 2025-11-18 04:21:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 964ca8fe-f2a1-39d7-8d6a-01869855453e | -3.65382 | -51.77899 | 2025-11-18 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 475da5c5-27b9-3629-ba63-d050d03cc975 | -8.10285 | -46.06339 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f282e20-ba69-3aca-9acb-2c36f91f471a | -4.4036 | -45.9753 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c827f832-c105-30e7-b43a-d8e5fe86f2e7 | -10.6605 | -49.37727 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9705cb89-161f-32d2-91dc-4c843cb37331 | -3.2409 | -50.49948 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65ee4130-fabb-3e94-a38c-5d653086bd62 | -9.40331 | -48.44569 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 227a102d-8487-336d-bc17-1345048c8518 | -5.57748 | -47.08888 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79f575e4-2bdd-3ac2-ad1a-7e29d6dfd511 | -8.29891 | -44.00986 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 990671b9-f7db-38c9-9900-7af0a55e1630 | -10.67978 | -44.26202 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5264fe0-fe75-3462-b739-7423c0009eb7 | -4.97367 | -44.67977 | 2025-11-18 04:21:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a906c7c6-d1c1-32de-8df2-2a8356ca6351 | -10.34941 | -48.92439 | 2025-11-18 04:21:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ce8b56e1-5b17-3293-83a1-57eeb712d6e7 | -6.71801 | -40.80236 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| eec712c9-2371-309a-88e9-b6614a02e39b | -3.47294 | -50.24371 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fafc5214-d9b8-37aa-85e3-68c9afd83323 | -8.55118 | -46.04825 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c395e0e-e437-3e55-b750-1702546e247d | -6.93051 | -45.3462 | 2025-11-18 04:21:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 55e8b4c8-304d-3869-9de6-3e20f2f1a985 | -9.16062 | -50.14202 | 2025-11-18 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1436f14-a3d9-3475-bf16-00829252d7a8 | -4.42962 | -45.54143 | 2025-11-18 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81e423be-340a-3779-bf6c-c88e027a187a | -4.19989 | -44.23247 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8c070f49-b2e5-39ba-b80d-1c75195ea8f1 | -7.67667 | -45.34074 | 2025-11-18 04:21:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 772d1c61-66e2-3f6f-8dce-8a1d528a2f4b | -3.16526 | -50.16293 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8183a3b8-7d2f-317c-a9b1-486caf5579d9 | -10.86185 | -44.0966 | 2025-11-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3856152c-bb07-3083-b9e8-a125326db368 | -4.19551 | -44.23883 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b4632ee-2859-33be-b902-f46e006957f9 | -4.18783 | -44.24469 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cd4ccf3-7d7a-3864-903e-efa411683851 | -4.64716 | -47.94738 | 2025-11-18 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |


[Clique aqui para ver as próximas entradas](README25.md)
