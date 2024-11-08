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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7eadf0f-20a7-3be4-8b4f-7f0d3df04b72 | -4.5209 | -45.6804 | 2024-11-08 02:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 285.7 |
| e2eb2d51-4156-32b8-9953-70b28aed27fe | -3.967 | -48.15 | 2024-11-08 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0fb3a182-bd5d-3d8b-b05c-cf313470de58 | -4.521 | -45.658 | 2024-11-08 02:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| fc24e301-b06d-330c-9b9b-4ed461af6dd8 | -4.5021 | -45.7039 | 2024-11-08 02:50:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 465d38d7-7df5-3cac-9470-a8ac8b55c12d | -3.9854 | -48.1708 | 2024-11-08 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 831fb1c2-0da8-304c-aaba-f7ed461690b0 | -4.5022 | -45.6815 | 2024-11-08 02:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 117.2 |
| cff3b5cb-34d1-3da3-85e8-7863bd30ccd0 | -2.8016 | -52.9414 | 2024-11-08 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 8177a14c-aa5a-3885-87fd-dc0e686b1d0d | -1.4982 | -52.0673 | 2024-11-08 02:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 483f3e5e-5586-3ef1-895d-55f156983556 | -3.9485 | -48.1508 | 2024-11-08 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 1f0a3e42-3f65-38e4-b5e0-60038bf7bce0 | -3.5632 | -47.3629 | 2024-11-08 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c97b73b7-7081-3c1c-93f3-c3115f107eab | -2.6214 | -51.7585 | 2024-11-08 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| a5045659-6f41-33cd-b63a-d156d66ecac4 | -2.82 | -52.9613 | 2024-11-08 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 6c1479ef-0a44-3bd3-8405-1c2695c1b70c | -4.5022 | -45.6815 | 2024-11-08 03:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 157.6 |
| fed0d22a-6df8-39db-8c3f-137827a7151d | -3.967 | -48.15 | 2024-11-08 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ff470ec8-65c4-31b6-b1cb-9c9a15891629 | -2.8016 | -52.9414 | 2024-11-08 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 310a7c3b-b6ac-3d40-bf7a-eff061c0003a | -4.5021 | -45.7039 | 2024-11-08 03:00:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 794fe981-9eeb-3ccf-a6c2-73d3231bbcc8 | -4.521 | -45.658 | 2024-11-08 03:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b4379c4d-b10f-3c4d-ab61-66a4efe5bbd5 | -1.1489 | -52.0099 | 2024-11-08 03:00:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 57c0d18b-0e0c-3184-acc7-8be9a4710d82 | -3.9669 | -48.1716 | 2024-11-08 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 2ed006da-eec2-353a-ae7d-e38eef2be51a | -3.5447 | -47.3636 | 2024-11-08 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| f7310835-395e-306c-846d-9256753c239d | -4.5395 | -45.6794 | 2024-11-08 03:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 9cb48cb1-7b04-390e-b99e-4c79f8a8a4ed | -4.5207 | -45.7029 | 2024-11-08 03:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 4fc3988d-c89e-34c8-9750-785adb3ab6e5 | -3.9854 | -48.1708 | 2024-11-08 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 5d8068fd-acba-3d31-a0bb-9f640711bbe0 | -4.5209 | -45.6804 | 2024-11-08 03:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 306.2 |
| de23a9b2-c43d-3e5a-bda8-bd363b111691 | -2.8016 | -52.9617 | 2024-11-08 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| cb69329c-6d0c-3d37-9459-c49fb6781066 | -3.5446 | -47.3855 | 2024-11-08 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 10ce2328-8675-3852-9655-7d8c4b36b412 | -1.4982 | -52.0673 | 2024-11-08 03:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 05bd172b-476d-3b08-bc37-d62dc4b56c1e | -3.5631 | -47.3847 | 2024-11-08 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 92019505-31cb-341b-907e-6ad7e9f0be32 | -3.1641 | -54.4854 | 2024-11-08 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e5b87315-f1c4-3958-9d06-bfe945cc2b68 | -4.52 | -45.7 | 2024-11-08 03:00:00 | MSG-03 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19b1a083-636c-3fb8-a394-907cca8ec317 | -4.52 | -45.65 | 2024-11-08 03:00:00 | MSG-03 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| baa787e3-292f-3a0d-8ef6-18fa6ea453d9 | -3.5447 | -47.3636 | 2024-11-08 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 077d2251-e2fb-3e8e-ba3b-6299e8409036 | -4.5022 | -45.6815 | 2024-11-08 03:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 95.0 |
| ff46e69d-13d2-359b-947b-1fcd1f7f3711 | -2.8016 | -52.9414 | 2024-11-08 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 8ce72b78-7ba5-3423-9429-45ff710127e5 | -3.5631 | -47.3847 | 2024-11-08 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| de566dfe-92b1-3d68-91b9-df4d9c1b26c1 | -4.521 | -45.658 | 2024-11-08 03:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| b7f12100-689c-3443-8bf4-50c2fc413153 | -1.1489 | -52.0099 | 2024-11-08 03:10:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 884d14d3-9f97-36ed-ad40-ea03739cea30 | -3.9483 | -48.1724 | 2024-11-08 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| cb68356a-9744-3a7a-af51-5c3e07f72883 | -4.5209 | -45.6804 | 2024-11-08 03:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 340.6 |
| 8dad25d0-ff0b-3dae-8e51-08a257611fce | -4.5207 | -45.7029 | 2024-11-08 03:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 162.7 |
| 2c86620b-313c-3a57-a41b-ba4fb7ec1052 | -2.8016 | -52.9617 | 2024-11-08 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e7929b54-d9f7-3ca6-94fd-6d733cd26f76 | -3.9669 | -48.1716 | 2024-11-08 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 917d713a-585e-3881-a6e6-f1706c50570a | -3.967 | -48.15 | 2024-11-08 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a0db7485-a520-3e10-9d9d-0c4d4f6569d8 | -2.82 | -52.9409 | 2024-11-08 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| cb4a7101-1fa6-355a-86ab-53139608a242 | -3.9854 | -48.1708 | 2024-11-08 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e9935632-91ad-3fc1-b953-206afaad1e5f | -3.5446 | -47.3855 | 2024-11-08 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 7b8118c5-ca9f-33db-96cf-03627c6b683c | -4.5395 | -45.6794 | 2024-11-08 03:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 3926ffb9-7809-373a-9910-2159273b1daa | -3.1641 | -54.4854 | 2024-11-08 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| c3d6e0d9-f674-359b-aa86-afa7d85d052c | -9.57566 | -37.81615 | 2024-11-08 03:12:00 | NOAA-21 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1c962b85-bf74-319b-be04-ac76771ca431 | -9.58356 | -35.7634 | 2024-11-08 03:12:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ad7c7b5c-679b-3190-bfdc-f882c96dbd83 | -6.26923 | -39.37358 | 2024-11-08 03:12:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1b9343df-aa63-33de-9bda-3725aae9a2a2 | -5.79359 | -35.38235 | 2024-11-08 03:12:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e6596cc8-59df-3225-aca2-5ec1aa59b4ae | -10.2232 | -36.23844 | 2024-11-08 03:12:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6f43d9c0-d008-3338-98ac-dbe81c57cf4c | -7.77485 | -35.14739 | 2024-11-08 03:12:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 75410772-e53d-3fb9-82fb-345b166a607e | -9.58406 | -35.76129 | 2024-11-08 03:12:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e5a18180-bf36-3457-8b53-b88a9d716bf3 | -6.26283 | -39.37257 | 2024-11-08 03:12:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dfbe7110-5edb-3813-98fa-787802f36c74 | -10.22418 | -36.23299 | 2024-11-08 03:12:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c537d664-1657-3d7a-9c85-08885dcb86e9 | -9.58314 | -35.76654 | 2024-11-08 03:12:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4f6d8ad5-f0dc-3091-89bb-8f727ac40a3d | -4.79987 | -37.74776 | 2024-11-08 03:12:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1bca078d-06ee-3199-9ba3-2a6aee1fec8b | -11.72717 | -38.33483 | 2024-11-08 03:14:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 946d055e-e54a-3004-81d6-48e257f7c1b2 | -12.77141 | -38.45844 | 2024-11-08 03:14:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2ab5c7e4-2d7c-37bd-a8c7-897658024555 | -12.76894 | -38.46122 | 2024-11-08 03:14:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2987f4f4-82c9-3393-8a9e-edb2a5d4ba60 | -11.72785 | -38.33521 | 2024-11-08 03:14:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 417b53a0-39ef-3512-bf48-df3d23ef065c | -12.76958 | -38.45789 | 2024-11-08 03:14:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c4d0b028-3073-3a5a-b83c-c54a4048960b | -15.41316 | -42.20224 | 2024-11-08 03:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7a631c75-bf64-325d-a98b-aff3c7bca11c | -12.77073 | -38.46185 | 2024-11-08 03:14:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0d895547-9063-327c-83b6-a684b6378820 | -11.69288 | -37.64753 | 2024-11-08 03:14:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 74e47137-7f42-31b4-835d-d649409e514d | -12.21234 | -38.98326 | 2024-11-08 03:14:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b44f2180-eb93-3fba-b026-b7d0597ceed1 | -21.1866 | -40.96029 | 2024-11-08 03:17:00 | NOAA-21 | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 162b0697-ad7e-39fa-a4e2-be064acfaaeb | -21.18834 | -40.96074 | 2024-11-08 03:17:00 | NOAA-21 | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a9174729-b621-32df-a825-0b30e5251a2b | -4.5022 | -45.6815 | 2024-11-08 03:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 3fe3ffcf-92c6-3251-8b97-cc094e4c6687 | -3.9854 | -48.1708 | 2024-11-08 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 92e1ca47-c5ad-3568-8d64-78edb80b2de5 | -3.5631 | -47.3847 | 2024-11-08 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| cb0192f8-12de-384a-aed8-a671773fb6d6 | -3.967 | -48.15 | 2024-11-08 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 72ff289d-891f-30d5-93e2-30ae694f64ab | -3.5446 | -47.3855 | 2024-11-08 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 927949ee-f92c-34df-9c82-acee5563f12e | -3.9669 | -48.1716 | 2024-11-08 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| d9a5e5b7-3d0a-3955-95bc-3697e5fe24ba | -4.5209 | -45.6804 | 2024-11-08 03:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 326.5 |
| 884115b1-54c0-3aee-8abb-d425ba3af89c | -3.5447 | -47.3636 | 2024-11-08 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| fa132b00-8a19-379c-8602-2f5d86baae83 | -4.5207 | -45.7029 | 2024-11-08 03:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 128.1 |
| c33b3b98-920d-3000-a7c6-202f4373d4ff | -2.8016 | -52.9617 | 2024-11-08 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f8541374-c1ba-344a-bfe9-da198004359b | -4.521 | -45.658 | 2024-11-08 03:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| b234ca1d-939c-3d38-95be-1e802c977cfd | -2.8016 | -52.9414 | 2024-11-08 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 3b7d4215-3e66-387c-be2c-7d4ea976ce15 | -4.5395 | -45.6794 | 2024-11-08 03:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 99.3 |
| c710d364-d722-341f-9d82-7f24d39cb32d | -1.1489 | -52.0099 | 2024-11-08 03:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 3f9d2dcf-cfcb-37a1-873e-4d68489a9b3d | -3.5446 | -47.3855 | 2024-11-08 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| de94cc82-02c7-3f0f-81e4-5d569a9693e5 | -4.5395 | -45.6794 | 2024-11-08 03:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a06641bb-b836-308b-b704-d38cef9767c7 | -4.521 | -45.658 | 2024-11-08 03:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| b9b8db29-7653-33a8-b843-ca734cd78c6c | -3.5447 | -47.3636 | 2024-11-08 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 9fc65d24-3d23-34b7-a7c7-d1b2b65227a7 | -1.1489 | -52.0099 | 2024-11-08 03:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f45c1848-a71e-3a88-94e7-062ae85496ea | -3.1642 | -54.4654 | 2024-11-08 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 07fb0088-7154-3ae3-854c-4e8b6078f757 | -3.1641 | -54.4854 | 2024-11-08 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 888f6dc0-6ea7-35b5-8a2a-68e0de700f81 | -3.5632 | -47.3629 | 2024-11-08 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 9d87c3e1-c97a-3e69-b3f8-ee365c0becfd | -2.8016 | -52.9414 | 2024-11-08 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1163243d-1c2d-3fd3-b894-57886035e48b | -3.967 | -48.15 | 2024-11-08 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| afba9fc8-059e-31c4-b4de-84614894807b | -3.5631 | -47.3847 | 2024-11-08 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 5d46c531-9cb9-33fc-a8d1-93d592bea990 | -4.5022 | -45.6815 | 2024-11-08 03:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 8414e60b-a063-3cc8-b655-72ec5a331d23 | -3.9669 | -48.1716 | 2024-11-08 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| d5016362-334a-3df7-a027-7dcd8ed3a163 | -4.5207 | -45.7029 | 2024-11-08 03:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 114.7 |
| c09e655e-8120-3195-8f17-bb1a761bdfcf | -4.5209 | -45.6804 | 2024-11-08 03:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 249.8 |
| 2c3dda7f-8c3e-37fb-bc97-d3703bb4efe1 | -1.4982 | -52.0673 | 2024-11-08 03:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |


[Clique aqui para ver as próximas entradas](README13.md)
