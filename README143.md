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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b945b6c-1c5b-3451-a6b0-0898b566b413 | -10.64887 | -58.76421 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aabd052b-bbee-37a7-b86f-575fc89b17bb | -10.64839 | -58.7679 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09cb452a-7b83-30f4-97d0-e8e5d3d1b08b | -10.64792 | -58.77165 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f33c770b-a2ca-3999-a2f7-32add6bab3d2 | -10.64358 | -58.76356 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 911a273a-8373-3b13-b169-def5700109ac | -10.64308 | -58.76743 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8433d68-91b8-3002-b5a6-286f43be6c74 | -10.57683 | -59.40347 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1fd212f-90c8-3409-ab96-2ef428d6ebb8 | -10.57644 | -59.40644 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63374a75-3268-38bc-a082-b8e9d399fd55 | -10.5383 | -59.31558 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a4e1f45-25ea-3b6d-8f73-8038b9c5198b | -10.53788 | -59.3187 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 010483b1-2c28-3bf3-8064-aeb87fa9835f | -10.53649 | -59.3162 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae0a6a92-9dfb-3421-a3c2-79cfff4d1d9d | -10.5361 | -59.31931 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5cd1ed6-779e-3823-ab40-43c76889ec50 | -10.53323 | -59.31487 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf7af4dd-d3ac-3af2-a92f-798fb32da501 | -10.468 | -58.75974 | 2024-10-12 05:48:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f83aa6bc-bbb3-383a-b340-5102e4aa7b2d | -10.29839 | -58.99799 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e16c56a-884b-3bab-9719-bdd15b9367ea | -10.29361 | -58.99425 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 90a199d5-3dfd-3b8c-a293-f37a03717e4f | -11.83502 | -58.84086 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 497d2eca-b0ab-351f-83d2-3c2160baffe2 | -11.83375 | -58.85095 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2c3458c-f9e0-304f-aaba-709f91c02a8a | -11.83289 | -58.85784 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a443ba23-e854-339a-8193-d37f4b9c5f6b | -11.83053 | -58.83336 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 764df4c3-2be6-3f24-8636-70cf029b275e | -11.83009 | -58.83681 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b269273e-08d9-340c-8917-8d3b78a3194b | -11.82967 | -58.84024 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e4eb4a79-7e11-3087-a5c3-880591179709 | -11.82881 | -58.84706 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cd0290ed-e5b0-3e4d-8b07-b1dbd5fca45f | -11.82839 | -58.85047 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 054806b3-a2b5-30a3-83f0-09ec9c9861d2 | -11.82432 | -58.83952 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2b08e177-257e-335d-bd3e-60870424336c | -11.82263 | -58.85308 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cb2edc4-4c5b-385f-a619-5cdf5e8ed6c8 | -11.83997 | -58.84469 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51bfcc0c-002d-3e67-a346-b30572c46be4 | -11.83954 | -58.84803 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ce660b8-daeb-3a6d-9ebb-4ad5125724c9 | -11.8346 | -58.84421 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0aa9a2e5-6921-3990-80e9-a479fe2b6ecd | -11.83418 | -58.84756 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40a728de-5667-38fc-bb68-21bc962231bf | -11.83332 | -58.85436 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86ccb56d-0c02-3a40-942d-2b75d47b431e | -11.82924 | -58.84365 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 68dbeada-ee8b-3ee2-b65a-48c3c198c01d | -11.82796 | -58.85387 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5ecb331-3369-3734-94c5-ae3ff559771f | -11.82754 | -58.85726 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12e6cbdd-7b05-35b2-8f90-8433b8ed44d2 | -11.8239 | -58.84295 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2a8207bf-10e9-3ff7-831b-91b81fe9f69f | -11.82347 | -58.84634 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1550c3be-50c8-3e7b-b4c3-fe41ff1d2e11 | -11.72106 | -59.28447 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4d75b51-f1b4-3238-84c2-8f1572185b9a | -11.72068 | -59.2876 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c05fa783-765b-398f-860d-e18a18e54bec | -11.71992 | -59.29375 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31280c6d-ba72-365c-b9bd-084871fb65a4 | -11.71954 | -59.29683 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f33d891-109c-3330-a256-de1cc5d86b44 | -11.71914 | -59.28614 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e5a986a-5c05-335c-ab3b-60ec37b490cd | -11.71873 | -59.28924 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96b2cc04-d8e6-3db9-80d3-38ae6e44921e | -11.71793 | -59.29537 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d76bde04-67da-301d-828d-067d765a3122 | -11.71667 | -59.27742 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a873da9a-782d-3645-8829-df3af0dc09a8 | -11.71628 | -59.28059 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cda4acf4-96cd-346d-97af-eecda706d88f | -11.71589 | -59.28373 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fe2f4fc-f2e7-39eb-8efb-7474a172d7b3 | -11.71551 | -59.28685 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 178879d6-608b-3687-97c3-fdb2e40de02d | -11.71475 | -59.29306 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a19ddf2-afde-3785-b0a5-e697c1f3f864 | -11.71438 | -59.28227 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8330f4c5-4884-3a6b-9bf9-2ae0bf663a87 | -11.71397 | -59.2854 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03e3d383-8e87-3466-b0eb-c5fbf7bc7613 | -11.03832 | -58.97657 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c537ce12-f54f-3836-8567-f12e4f35eac0 | -10.99734 | -59.00655 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be433735-b1d4-34a5-ab97-9b2925021d60 | -10.99695 | -59.00973 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59577721-c7fe-3209-99f6-2b9d68ed0811 | -10.99656 | -59.01292 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fedf748a-6e87-3850-8585-e258f0d85880 | -10.99656 | -59.0093 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28abf74a-8d3e-336d-90cd-690df12a1a39 | -10.99614 | -59.01248 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fda3b96-f6dc-3eea-9e01-6d655c03e0d3 | -10.9909 | -59.0157 | 2024-10-12 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0845ec4d-02f0-333e-a4ce-1aa760fc0770 | -12.33526 | -59.87394 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a20440de-f1d4-370a-82b1-b51d3d846452 | -12.33489 | -59.87691 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10c46b76-d0f7-3678-ae3c-a6dc462dce06 | -13.76554 | -60.56889 | 2024-10-12 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9589f290-283c-39e8-abc9-5a6a10568ff5 | -13.74256 | -60.59396 | 2024-10-12 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b07e42d8-1606-38e2-9af6-38491920ab62 | -13.74187 | -60.59945 | 2024-10-12 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ee3ff09-b329-3805-b645-70f187b9653b | -13.737 | -60.59882 | 2024-10-12 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2c4339aa-ffca-3668-8e68-61362664074e | -9.26727 | -60.82039 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3da1158-e287-37ef-8205-fb08b5ae64c1 | -9.26666 | -60.82495 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b92b29c3-411b-3658-a5c2-24a2e9f5850b | -9.265 | -60.82236 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf801999-6916-3b0e-abb8-3399d853421d | -9.26277 | -60.81977 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b6e92b3-d230-3f09-b121-ebeb1e61c6e8 | -9.26216 | -60.82432 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63804d74-e199-3761-8dd3-45635076af3e | -9.2605 | -60.82173 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0fc5c31-97c7-3098-a4a0-838993801879 | -9.20518 | -60.79082 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcbab1d4-b2a9-3d06-beca-430fd846d36b | -9.20455 | -60.79538 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eea2eeef-a223-3c5f-b51c-593a8aeaa6d1 | -9.20393 | -60.79992 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3dd708f8-ba72-3620-81cc-d4f90411c037 | -9.20068 | -60.79019 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10494009-4b9a-3204-baa7-5202ee81680a | -9.20005 | -60.79477 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c011c2d-25df-3e0b-91fc-adb097d9c460 | -9.19515 | -60.69606 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd7d558c-cc21-39f7-bc89-36a81675c9fa | -9.18999 | -60.70006 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a82fabb4-4da3-3661-90d1-5518fca9a88f | -9.18128 | -60.76411 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6433f75c-39b4-3100-8abb-1415207958e1 | -9.17702 | -60.69354 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f973bcd-e358-37e8-88c3-5d8313b92128 | -9.17677 | -60.76346 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66b184fc-85a3-3d6e-82f2-1ad0632723a2 | -9.17536 | -60.69503 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01085140-c8f4-3b9e-b3a3-dcb94fc7e188 | -9.17249 | -60.69287 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e76d8291-e7c1-3ee9-89a9-521ec0333d0c | -9.07974 | -60.58247 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b5547cf-9767-3e8a-b796-556cf2653acf | -9.0794 | -60.58141 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9a29e81-cf18-3635-bb4d-0eeb1e0aaeb3 | -9.07616 | -60.57145 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 267b00e0-19f7-3d6b-ac88-f2f136287beb | -9.07517 | -60.58185 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37c72379-eabd-3fed-aa8d-359d6108ee4c | -9.07484 | -60.58079 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59bf1af5-3076-31ee-ad28-1b4112c5bdfa | -8.64589 | -60.74573 | 2024-10-12 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfa4a9a2-a652-3fd1-9209-8d39e2ebf002 | -8.64141 | -60.74509 | 2024-10-12 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a1fcee2-cbe5-3454-bfce-9dd5b11ccee2 | -9.27143 | -60.27371 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee113461-5e70-38cf-a0d6-3fcb6d6983e3 | -9.2355 | -60.36378 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f2bd2df-e8b9-36aa-a203-ad01ef81cfd7 | -9.23484 | -60.36867 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f623014-f2b4-3dfc-918b-15c243b38628 | -9.23087 | -60.36308 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdf7609c-bb28-369e-8db4-1551afc1275b | -9.23021 | -60.36798 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23cfefe7-7af2-3c12-a40b-b96cdde46741 | -9.22963 | -59.7526 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b348c5a-731f-3c84-88dd-96b80bbc52b7 | -9.22479 | -59.75194 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 386a8d93-fc4a-308c-b513-0d9327f5ccd6 | -9.21707 | -59.77275 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0973fd0-47c4-3fde-8b92-3eaa83804f78 | -9.21224 | -59.7721 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c7270ec-3d0b-30db-bf89-f843b317d2dd | -9.21153 | -59.77737 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 894e45bc-1bca-352a-b7a9-0ef35a7d7833 | -9.16138 | -60.39534 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 73058354-97f0-39f1-9b13-ebb7e5316abd | -9.15676 | -60.39465 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 238514d5-6099-303c-8082-8c04e6633de4 | -10.7491 | -60.74594 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README144.md)
