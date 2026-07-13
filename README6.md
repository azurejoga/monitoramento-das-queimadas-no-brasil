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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cde383b-2b64-3cc2-83e3-24da0aa17754 | -9.34735 | -46.74017 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89ea7a6f-a978-3c17-8f28-1e44e5632c9a | -9.36893 | -46.73083 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc7ffea0-1074-3238-b3b3-16bbd0133fcb | -11.48907 | -47.62186 | 2026-07-13 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 81ce3324-81e2-3646-874f-e9155fc6d98d | -9.35406 | -46.74113 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e97f95f-06ab-3426-a38a-c45a97a2d203 | -8.0955 | -47.09531 | 2026-07-13 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00aba564-3626-30e6-9244-632d1bdc1fca | -8.12626 | -47.87704 | 2026-07-13 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a05cec4-faf0-38f7-a421-a759d64fba60 | -8.13195 | -47.87601 | 2026-07-13 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd6635d8-3d3b-309e-81a0-5a36e2e1ad7c | -16.5 | -52.603 | 2026-07-13 05:21:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b29461aa-1f3d-30e1-aa64-92ad95f3db5f | -10.1298 | -50.1047 | 2026-07-13 06:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| e9c94c87-4129-30a4-b199-e9943ca8ccc8 | -10.1295 | -50.1261 | 2026-07-13 06:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 22bbbf60-7f92-3be3-92e8-e5f71585a3e9 | -8.60317 | -63.4594 | 2026-07-13 06:12:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f3a69e9-d394-351c-b4c0-ffa9606094c5 | -8.60838 | -63.46014 | 2026-07-13 06:12:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee451b4b-f063-38af-a6ec-3e98ac1ddb0e | -10.1295 | -50.1261 | 2026-07-13 06:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| f8a88881-e16c-3544-80d3-a3a638162643 | -10.1298 | -50.1047 | 2026-07-13 06:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c7de6992-af7c-3334-80b2-c3e860fafa70 | -10.1487 | -50.1027 | 2026-07-13 06:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| b59b548f-4df7-3790-8201-662ff3ed38bd | -10.1298 | -50.1047 | 2026-07-13 06:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 20e7c83f-901d-35ab-a917-a3301c14d788 | -10.1295 | -50.1261 | 2026-07-13 06:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 6d285ef7-c578-3d96-a375-bef2edb87eaf | -10.1298 | -50.1047 | 2026-07-13 06:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| b5032626-6788-342d-969a-b4495fd31e97 | -10.1487 | -50.1027 | 2026-07-13 06:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 4be7c961-21e0-3176-bc25-acc02c87de04 | -4.94801 | -48.2492 | 2026-07-13 06:52:00 | AQUA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e9806813-73c1-38b9-a896-221c4a1818d8 | -10.12265 | -50.10621 | 2026-07-13 06:54:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ff322fea-f841-3296-aeb6-3db7f803e6e4 | -10.14942 | -50.09642 | 2026-07-13 06:54:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6ae3ed34-b3b6-3acf-b30e-02ee12bc63d4 | -10.1298 | -50.1047 | 2026-07-13 07:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 103a657a-eab0-3989-814d-6f5d650a960d | -6.5631 | -51.1126 | 2026-07-13 07:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6ffef0d8-422a-30fa-ac9d-34f914e6249a | -10.13 | -50.0832 | 2026-07-13 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ef9d260d-44fa-3d99-a0de-a4c4ed36cf44 | -10.1298 | -50.1047 | 2026-07-13 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.9 |
| e0c76d4c-f107-38eb-9467-615c0993201e | -10.1109 | -50.1066 | 2026-07-13 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 369f7689-5b1e-3e56-9328-cd3b146e015c | -10.1111 | -50.0852 | 2026-07-13 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ad2e631f-f74d-312b-8d0e-669bd3cf6baa | -10.1111 | -50.0852 | 2026-07-13 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 08cdcd3e-e7b8-3146-9f56-a135843e7f81 | -10.1109 | -50.1066 | 2026-07-13 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 943d15f1-5999-3d4f-b58f-6f22d2a465be | -10.1298 | -50.1047 | 2026-07-13 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 669829da-cd97-3dc5-aec7-b1a3c4500b2a | -10.13 | -50.0832 | 2026-07-13 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| cf9c5e13-fcab-3d34-924e-755a3051200b | -10.1109 | -50.1066 | 2026-07-13 08:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8c15fd84-9ed8-39e5-87b9-10f8277e0832 | -10.1298 | -50.1047 | 2026-07-13 08:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 75415b93-9432-3f13-a00c-9fc3975b0959 | -10.1111 | -50.0852 | 2026-07-13 08:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 445fb3fc-7c2a-3a60-816a-d5a71dbe0d53 | -10.1109 | -50.1066 | 2026-07-13 08:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 25999fe4-2a69-3b57-8782-d056fc539cfb | -10.1111 | -50.0852 | 2026-07-13 08:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1b2862c6-3ef8-3864-a791-b914229cb6b8 | -6.49539 | -42.21836 | 2026-07-13 11:23:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 5ce7377f-fd16-3965-b4f3-61d7079bb655 | -5.04798 | -38.00508 | 2026-07-13 11:23:00 | TERRA_M-M | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 04a692b8-cdba-394f-91ce-78259316b775 | -2.95385 | -41.05603 | 2026-07-13 11:23:00 | TERRA_M-M | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 70a7fd97-9626-36e5-8ba9-e1b9c98d5773 | -5.04662 | -38.01498 | 2026-07-13 11:23:00 | TERRA_M-M | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| cccb0cfc-3bba-3280-a4c8-64e1ac6abf0b | -6.94782 | -43.71886 | 2026-07-13 11:23:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b918f352-4c9c-39db-b04b-991fbeb6fdbd | -6.49396 | -42.22805 | 2026-07-13 11:23:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| eb3a8872-7b4e-347a-aee8-e40bc5c57934 | -8.41368 | -39.79422 | 2026-07-13 11:25:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 46cc30cf-b6bb-383c-9561-b4174db85da2 | -10.56349 | -36.8586 | 2026-07-13 11:25:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| f596644f-276b-3925-8ae8-050d8e83819f | -10.08927 | -40.53248 | 2026-07-13 11:25:00 | TERRA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 9e4560b9-b987-3dd1-a7b0-3f2cc9e77b7b | -8.51553 | -44.73524 | 2026-07-13 11:25:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| dff79de2-e37d-3f9b-9f28-31af12065e76 | -9.36713 | -46.7404 | 2026-07-13 11:25:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 43ac1162-b82c-3ca6-b37b-50f448f46a2a | -9.37668 | -37.82239 | 2026-07-13 11:25:00 | TERRA_M-M | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 9d879203-2bf6-35de-ad7a-a2faa93d41cc | -9.36985 | -46.72299 | 2026-07-13 11:25:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1ff7268a-05d4-35a0-ad21-5df6dfb66afc | -13.82499 | -44.97915 | 2026-07-13 11:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 01b2c0b8-fb90-35bb-a4f9-226c42ef830c | -16.35082 | -43.87967 | 2026-07-13 11:28:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 7ebd7ce9-12d3-324a-b202-5a97374fcb20 | -16.35982 | -43.88108 | 2026-07-13 11:28:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1af02ad9-9755-38ce-84d7-22964e1b6c3d | -11.94991 | -46.72868 | 2026-07-13 11:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6afc9853-a635-3a6c-a1f2-625d4039c0cf | -18.78007 | -40.17918 | 2026-07-13 11:28:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| d005c3ff-e1e7-3505-b36a-c8af259f3207 | -13.59514 | -46.54545 | 2026-07-13 11:28:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4b0439e9-96f7-3dc3-bed3-0e0433f1b9c6 | -13.02595 | -41.03156 | 2026-07-13 11:28:00 | TERRA_M-M | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 38a81545-9325-3f90-a3c1-a9f8fdcac096 | -14.23247 | -45.45395 | 2026-07-13 11:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a31b2215-ea42-38d8-8a7a-6840776d2aaa | -13.75801 | -46.24587 | 2026-07-13 11:28:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 9c9ca871-60b7-359b-9d49-3c76570cc378 | -11.94738 | -46.74461 | 2026-07-13 11:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cd15df99-0851-3991-86b6-67bef0444e9f | -9.3629 | -46.7359 | 2026-07-13 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| bb51906a-c5d1-3b9a-bb14-a354665fc6ca | -9.3629 | -46.7359 | 2026-07-13 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| ac264b78-b426-3455-b259-d6b4c5edba5e | -9.3629 | -46.7359 | 2026-07-13 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 997c3f8f-17f8-3b00-af74-bf60ce3b140b | -9.3851 | -37.8085 | 2026-07-13 13:40:00 | GOES-19 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 2b8b9eb9-cfa9-3c5a-8b36-04498cd2d40d | -9.3851 | -37.8085 | 2026-07-13 13:50:00 | GOES-19 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 37683749-49c0-375e-ae2b-f363da74dea0 | -9.3851 | -37.8085 | 2026-07-13 14:00:00 | GOES-19 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 121.8 |
| ae6f4e28-b988-3b85-a85d-2e42012acebc | -9.3851 | -37.8085 | 2026-07-13 14:10:00 | GOES-19 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 121.1 |
| 89785b99-ea8c-31a6-88c2-9a26c07ed725 | -9.3851 | -37.8085 | 2026-07-13 14:20:00 | GOES-19 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 108.4 |


