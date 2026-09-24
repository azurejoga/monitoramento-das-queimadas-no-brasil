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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e899132e-a54b-3a24-96b5-321df2bb7eec | -10.24001 | -68.2992 | 2026-09-24 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b3e2568-c2fd-3bde-8c34-36fe20fb87f9 | -7.97186 | -62.0424 | 2026-09-24 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc0315cd-cc1a-3fdb-8e10-7f0c43bddecf | -6.30944 | -59.95207 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b81f9a7-18c6-3780-a8f7-2afd31eb6d55 | -7.52539 | -70.39988 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f036be2d-46a4-381c-b0f2-4a87a2ea2d8a | -7.45823 | -62.31208 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dce46e5-ff73-3d68-8377-af70b2abe230 | -5.86738 | -60.1605 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb153f42-da81-3d2c-85ff-3d504ef10444 | -6.1002 | -57.67602 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b53bd388-4154-368d-8492-e0c6c2d04bc0 | -8.91035 | -71.3428 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76622a0a-622b-38ae-b484-ca307851f997 | -6.67772 | -58.55191 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 270f98f9-e3af-3928-a4e2-2540baaad00f | -8.30662 | -71.19628 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ed59323-f99b-30a4-bca5-413ed3a0f556 | -5.9981 | -57.72006 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 414593c9-c3e3-3f49-ae80-d9df372e2484 | -8.31882 | -70.53824 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20a96986-f5a4-39d1-94dd-02369f7b3651 | -9.49754 | -64.03547 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c41e85c4-bd47-38c5-86aa-b3820ce88e20 | -9.50836 | -66.76728 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 052ee450-d7bf-33dd-a814-dc8df2fb1fb2 | -9.04228 | -66.05483 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a0d565a-030d-34cb-93db-90e9129f2b8c | -6.08314 | -57.6224 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4879ccd8-f4c3-3352-8a68-449ff9745eb7 | -9.25701 | -65.44054 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ad733d8-e2f1-37c7-b532-51f305d1a222 | -5.65821 | -60.21344 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da30b3d1-be0c-39b3-bb9d-8f29c49baf0a | -6.1602 | -59.94358 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 204fa062-b770-322a-8cd3-4278e616d541 | -9.0427 | -65.42081 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24957a94-6c7c-3221-8940-6f942b2472f0 | -9.76573 | -65.06001 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53e04ae0-dd21-384f-8429-870a9a68c510 | -8.64615 | -67.02518 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adbd40f3-0c17-3e3f-b8c1-97c611e92f51 | -6.68242 | -58.55581 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f95e320-b8ee-39a8-a1aa-506212aef83f | -6.68138 | -55.05224 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14878250-00d3-3e05-af61-7c118bd38da0 | -6.10561 | -57.67669 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b86511aa-92e9-3228-a0ab-059f7d3bd646 | -8.63416 | -66.99069 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eedfcb1a-7cda-3610-8b59-6af8a330b91e | -7.87698 | -61.1785 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee1bb1af-b2cb-3d9f-9276-5dbd031ffe5b | -7.88971 | -61.17265 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4dddc36-f1f5-3d4c-a46c-03fe1140f456 | -9.49746 | -64.03203 | 2026-09-24 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2deb7a13-9689-3221-9ad3-99800f37b49f | -8.1815 | -64.04409 | 2026-09-24 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a11878c4-64c2-367e-805c-b6e9b8956491 | -7.66601 | -69.93269 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5088489-d448-3299-b374-3671af07b6c1 | -8.883 | -62.54406 | 2026-09-24 06:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f12a31d7-593d-3306-b8db-53fe7a3ac823 | -7.42031 | -70.1078 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a6255f8-2899-345b-b6de-e04c027b5345 | -9.93053 | -60.72018 | 2026-09-24 06:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a1f5d55-e23f-355f-ab7c-270ba4545f52 | -9.64585 | -67.06898 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f795c769-999a-3880-ba62-6e8795dc7379 | -7.89555 | -61.17952 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b95ddcc8-1632-3304-9e8b-e3bea9d5784c | -8.31182 | -70.54075 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba207d8a-269d-386b-b712-854fbe51a469 | -7.76645 | -72.98422 | 2026-09-24 06:25:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9a696c7c-013b-3629-86e3-e30d73cdaa27 | -6.0182 | -59.94191 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f6a87dd-7d33-38ad-b45e-16770047ea47 | -9.69881 | -64.91427 | 2026-09-24 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5468c9f9-103c-36c0-8bae-e84688c7b282 | -7.89627 | -61.17386 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa768b31-87a9-3bac-a6a2-89b5f274a7a9 | -9.50656 | -66.76071 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06e2bab0-6b10-3774-ab4f-ab48d37ab25e | -8.90394 | -71.34324 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3e81ce7-7bb6-3e8d-8694-e7b6116b0ce0 | -7.953 | -72.93483 | 2026-09-24 06:25:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3a247d8-3d3b-3a4b-80e1-03a3e027fddd | -8.88915 | -62.54483 | 2026-09-24 06:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c36663a0-cc5c-387e-89aa-ec8cf98f75aa | -7.52264 | -70.39349 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c120a01-24c7-3549-9293-f1e80879602a | -7.66666 | -69.92831 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83f87490-b255-3026-8b03-a09e33142485 | -3.80463 | -58.88558 | 2026-09-24 06:25:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca5ae02b-fd4a-3af3-861c-7ed639482fa2 | -7.52562 | -70.39819 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86b3565a-85f3-3626-a1b8-de5e01619ddd | -8.91156 | -71.3404 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad58ba75-f4a6-36d6-86c4-7c1af4e03195 | -9.9025 | -60.37425 | 2026-09-24 06:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 97b9539d-1fa3-3b93-86d3-eb0472b7fb44 | -8.63322 | -66.98738 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33de7281-beb3-317b-aab4-56e1c637da6f | -8.38656 | -71.07507 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ebe2a4a-812c-381e-93a7-4e6c5fec9423 | -8.77256 | -72.77673 | 2026-09-24 06:25:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a13d2f56-902c-37c8-8e7d-67aa5fb2dcc2 | -8.8877 | -62.54824 | 2026-09-24 06:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 847f8828-87ce-381b-924b-4feee86a1146 | -7.36718 | -70.11864 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 737e048b-e06e-3e01-a549-68300d088b11 | -7.70993 | -73.08287 | 2026-09-24 06:25:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3633c56e-4ca8-30c3-9801-6a2d40300201 | -8.92148 | -61.49296 | 2026-09-24 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 385c5f14-8323-35d9-b137-b66e0b09af2c | -8.19864 | -70.47475 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3999ec2f-e419-3395-9cc2-6b21eed0f96e | -8.91096 | -71.34432 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b0a2b49-e0d0-3272-bd02-cca41c217085 | -9.93201 | -60.7215 | 2026-09-24 06:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3acf3077-f5b2-39e2-bd2f-a81963fc25ef | -6.76915 | -63.14493 | 2026-09-24 06:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 572d70ef-0d8a-30a6-811c-17e79793d26d | -3.80799 | -58.89092 | 2026-09-24 06:25:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dffef47d-64fd-332d-ad88-f4bda37fafd6 | -7.90532 | -61.1696 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 454e528b-a528-3de6-a3d3-331dfe08ea50 | -8.92257 | -61.49226 | 2026-09-24 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9709474a-5047-3dac-b38b-7ddd82914728 | -9.0405 | -65.42312 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98cd3460-0a40-3b2c-90f6-0dd8e22704b8 | -7.66728 | -70.07547 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ea90415-85a1-3b88-b620-51e3caabb1eb | -9.75133 | -64.30563 | 2026-09-24 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7779ba72-e106-3702-9bd7-15afc1fd6e6f | -9.89271 | -60.36001 | 2026-09-24 06:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cc7427bf-f905-31a7-8dd0-62d561b8f15d | -9.04209 | -65.41116 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07d1f76d-6c68-3a87-838b-bde307bcd4f8 | -7.88168 | -61.18309 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fa3558f8-578e-371b-a9d1-016cca547de5 | -7.67096 | -70.07603 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8bd948d-6fde-3ad3-bfeb-2679887373a1 | -9.5059 | -66.76559 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 592f26ca-0f99-30d6-a9bc-5789873a9344 | -8.6417 | -67.02595 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f016852c-1841-33c2-acd1-777220017fa4 | -8.64623 | -67.02661 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5e6b501-b379-335c-b2c4-6f8a24324f67 | -8.02603 | -71.36143 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fdd8ace3-f4b6-3e2d-a62e-095aa7ff2c11 | -7.79556 | -70.62936 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e532871-d9cc-3f28-93ac-f1fdd4120ffa | -9.75179 | -64.30205 | 2026-09-24 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3813f08a-fc54-3fdc-9f2e-b5658ff7dd48 | -8.95063 | -71.53217 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55272460-2348-303c-b8f6-d897296142d8 | -8.92216 | -61.48745 | 2026-09-24 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc8defc8-3a98-340f-991f-fb0dc23430ca | -9.93816 | -60.72886 | 2026-09-24 06:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86e92927-98c6-3f12-bc20-57bfed4f2bd1 | -8.62868 | -66.98672 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92510b32-b3e3-3f29-a081-3aff64e8934d | -7.8751 | -61.18204 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a6635a5-b554-32b9-934b-2ea71c001d59 | -9.64583 | -67.07066 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1219fb6-3b85-3d54-a1d2-91d400c16828 | -8.65077 | -67.02723 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8813cc42-ce1b-39bd-a4a9-fc93caf086db | -8.64559 | -67.03118 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b174803d-32d1-36d2-a277-2953cb3ae76a | -7.89875 | -61.16847 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1735a0e6-bc5f-38df-8403-5c96543db51f | -8.35857 | -71.18779 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75aec098-8bc1-3b2d-8d30-f6a8de933d2a | -8.53905 | -70.78396 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 882cd60d-0c3c-3728-bc23-474ed10557a5 | -7.51839 | -70.39712 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c03804c-b53b-3151-b2e1-ee03381135a8 | -7.89698 | -61.16822 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32ebb046-e067-3a3a-ae73-319c2286dd03 | -7.8841 | -61.17757 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f775871-f4e5-3a01-88ab-596a3db1bb21 | -9.69924 | -64.91098 | 2026-09-24 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2af819a0-133f-3f4f-b68f-195c440ded40 | -8.02544 | -71.36525 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 08e054c7-94f7-3723-906e-8f15b01ee793 | -8.18198 | -64.04048 | 2026-09-24 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10681567-e171-3118-9e18-57312a269223 | -7.89041 | -61.1671 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed68e9f5-d346-39df-b159-c653aa211bd9 | -7.89144 | -61.17294 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80360b7e-f49e-3b98-b044-abe4c0bd230a | -7.51424 | -61.48321 | 2026-09-24 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| abeff651-c77a-32b7-9cf6-94687dc7ccd5 | -8.00523 | -71.31105 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2179a60-f2b4-3c41-8ef0-7f46793d9473 | -3.69042 | -60.55318 | 2026-09-24 06:25:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README87.md)
