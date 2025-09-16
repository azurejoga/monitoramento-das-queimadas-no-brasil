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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c7a1a56-853c-32e2-bb28-3dc94ce9510b | -13.2993 | -54.2207 | 2025-09-16 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| cbe32005-04a5-3e7e-a12d-cdb649ef0d79 | -13.2993 | -54.2207 | 2025-09-16 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 136.9 |
| f564c60d-63b8-3e0c-880d-68e5b3aeeb5d | -13.299 | -54.2414 | 2025-09-16 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 662c9aaf-d916-3936-a42c-335bd026a293 | -13.2801 | -54.2228 | 2025-09-16 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| c2438171-48d9-3d2c-a1a0-e51463f51fcd | -13.2798 | -54.2435 | 2025-09-16 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| d0dc4401-a5dc-31db-9eb3-45fdc63ff0bc | -7.80514 | -71.98147 | 2025-09-16 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a730811-ddc5-353b-a036-2a0a0b507a73 | -7.80793 | -71.96328 | 2025-09-16 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec24889a-bad2-3d0d-8966-9fc2fdcf4b74 | -7.91132 | -71.74221 | 2025-09-16 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83f334b1-e8e7-33f2-8aa7-ff9e227fa240 | -7.80763 | -71.96437 | 2025-09-16 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4971c4ca-a22b-3486-8c89-fadb5fbb0a02 | -8.03037 | -71.36308 | 2025-09-16 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acf8ae35-c668-3f5b-9eae-55a6d844917e | -8.03497 | -71.36373 | 2025-09-16 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcccab8b-b4d7-34a2-bbcf-8a0f7d4d1a75 | -7.80074 | -71.98085 | 2025-09-16 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66084e51-c029-3da5-8bc1-f32ed147789d | -7.91195 | -71.73779 | 2025-09-16 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab84af7a-79bf-3596-88fc-f778e93a212b | -13.299 | -54.2414 | 2025-09-16 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 573fb6f6-29e2-327e-a38a-ac966b158555 | -13.2801 | -54.2228 | 2025-09-16 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| cf040c34-4e5b-33ef-a133-c0a3eb680f2d | -13.2798 | -54.2435 | 2025-09-16 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 50085303-87e8-3341-adcc-8df53da9f66e | -13.2993 | -54.2207 | 2025-09-16 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| d0354ac4-39fa-325b-a3b1-1edcc2f11f13 | -16.0751 | -59.4176 | 2025-09-16 06:40:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 5aac7d21-b4fd-37cb-9109-5cd85cde96aa | -14.5168 | -47.3304 | 2025-09-16 06:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 11a96226-9c21-3df6-a8d3-da687120f76a | -13.2993 | -54.2207 | 2025-09-16 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| b9945101-3aaa-37d8-9f36-78e6b14fe44a | -13.299 | -54.2414 | 2025-09-16 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 07f10d57-0cce-30e0-a807-783558529cb7 | -13.2801 | -54.2228 | 2025-09-16 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2954aa09-9b91-3cf1-8398-819f218623ec | -13.2798 | -54.2435 | 2025-09-16 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3b030f46-ad9a-3bba-bd61-4870dcf8cb4e | -13.2801 | -54.2228 | 2025-09-16 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| ba5be8dc-cd09-3ae3-9955-9f92c803ff27 | -11.7151 | -46.8739 | 2025-09-16 07:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8b15ea0d-76f9-324a-bc12-713c992bedcf | -13.299 | -54.2414 | 2025-09-16 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 4debe6f3-8302-33e9-a054-21dbbf6d6f6e | -13.2993 | -54.2207 | 2025-09-16 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 4f8ec542-e4d9-3c62-a1a2-14d51a9e2db7 | -9.30612 | -65.59816 | 2025-09-16 07:03:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c7738679-269e-32ef-87cb-5151e6c982f0 | -9.18497 | -62.52127 | 2025-09-16 07:03:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 08da7380-4501-3920-88f6-776d195cd4b6 | -10.36556 | -61.25628 | 2025-09-16 07:05:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dede619a-c6c6-3e8c-847d-3a35c9aef3ad | -10.36658 | -61.25137 | 2025-09-16 07:05:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e1c8e9f1-862c-3b7b-8121-ddea470aa836 | -16.47006 | -55.0966 | 2025-09-16 07:07:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 40.7 |
| 978cacd5-ee17-348e-b9f0-9beced010c0b | -13.2801 | -54.2228 | 2025-09-16 07:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7b90a8f0-7879-3e1d-9b9b-9a0640485ce5 | -10.7302 | -46.5082 | 2025-09-16 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| db29341e-7523-31aa-a91d-acd34a5138af | -10.7112 | -46.5106 | 2025-09-16 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| c14a2857-ee81-3b12-b0cb-a329494e3fef | -13.2993 | -54.2207 | 2025-09-16 07:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 236b5fb7-b8b2-3b4c-8fdd-797f004afc5e | -16.491 | -55.1067 | 2025-09-16 07:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 0d009dd7-0e17-36a1-a677-49f4e3aa1276 | -11.7151 | -46.8739 | 2025-09-16 07:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 573e45c6-da0d-3da7-8577-a243245291e1 | -16.4714 | -55.1092 | 2025-09-16 07:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 3b5735ff-8b48-353b-912c-dce402c12a26 | -13.299 | -54.2414 | 2025-09-16 07:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8ecb8efd-f260-373f-bed8-671f99d38d79 | -10.7112 | -46.5106 | 2025-09-16 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ff241675-f632-356e-8863-bc39804f627d | -11.7151 | -46.8739 | 2025-09-16 07:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| b94b0641-224d-374e-a4ec-49709d6cef5e | -16.0192 | -59.2427 | 2025-09-16 07:20:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| d8526df1-973f-3c44-8ec2-18d3abf1184e | -16.491 | -55.1067 | 2025-09-16 07:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| ef9d86f9-a370-3b16-a0fb-e39f58415b18 | -13.2993 | -54.2207 | 2025-09-16 07:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 811adcad-d94c-31bd-9f75-cbfa2b2ace4d | -15.0974 | -52.4731 | 2025-09-16 07:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| f34b1135-1783-3fd6-b3d9-daa6ac9948ca | -10.7302 | -46.5082 | 2025-09-16 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| d21670e9-8b3c-3e33-aaef-86c192f4be81 | -10.7112 | -46.5106 | 2025-09-16 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 444fb9e2-3317-3024-bf2c-6ee51073c0f9 | -11.7151 | -46.8739 | 2025-09-16 07:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 6aa4fe88-8980-34f7-b37f-2073577c88e8 | -15.0974 | -52.4731 | 2025-09-16 07:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 59fecd05-5380-3daf-89da-f02937a0d723 | -16.4714 | -55.1092 | 2025-09-16 07:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| ddfe8bd0-f663-3972-9fb1-4284019e90fb | -16.4718 | -55.0883 | 2025-09-16 07:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| d066ce18-7df6-3eae-b0b1-954acd58843c | -16.4914 | -55.0858 | 2025-09-16 07:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 56c07d65-d271-38f8-8021-9d0ec1f4aa18 | -23.2571 | -48.2851 | 2025-09-16 07:40:00 | GOES-19 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.7 |
| 61c535f7-9bf3-35fa-89ac-a5aaeb6c1e1e | -10.7112 | -46.5106 | 2025-09-16 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 0b1a4aec-d995-3383-9b0c-58b8a7c01ff0 | -11.7151 | -46.8739 | 2025-09-16 07:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 0a67f0df-7c99-379d-b2bf-30e889929ba1 | -10.7302 | -46.5082 | 2025-09-16 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 23ca147c-d123-3e33-be83-7f3b6dbb0ab7 | -16.491 | -55.1067 | 2025-09-16 07:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 42dc13a9-2216-302f-afd0-77eb76ffe888 | -10.7302 | -46.5082 | 2025-09-16 07:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a5e8c724-ebf3-30e4-90f0-42a3ca83b713 | -16.4714 | -55.1092 | 2025-09-16 07:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| db9d3301-3113-3d53-9b1f-d1b69a54df1e | -23.2571 | -48.2851 | 2025-09-16 07:50:00 | GOES-19 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.1 |
| a4f8a734-ae12-398b-8161-f493145b2d5a | -16.4718 | -55.0883 | 2025-09-16 07:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| a74eabaa-aef9-33b8-b41c-ae60159a5e3b | -10.7112 | -46.5106 | 2025-09-16 07:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4d242f18-a8b9-361a-a921-a10214672cbd | -13.299 | -54.2414 | 2025-09-16 07:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| c31d0db3-7b48-3f29-8a16-3a500ef2c7c6 | -16.491 | -55.1067 | 2025-09-16 07:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| f1bda37c-0a4e-36af-a28c-f26dcb6dd0a6 | -16.4914 | -55.0858 | 2025-09-16 07:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 12043fc5-5988-3525-8435-6de39d738ecb | -13.2801 | -54.2228 | 2025-09-16 07:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2e97f0a8-7e55-368c-8dfc-fb66cb0ff633 | -13.2993 | -54.2207 | 2025-09-16 07:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 7664c930-7004-3675-bf96-709a61263955 | -13.2993 | -54.2207 | 2025-09-16 08:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 5252a97b-d529-353a-8f12-9417fbdb1422 | -13.2801 | -54.2228 | 2025-09-16 08:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 12973e78-bae6-31cd-928c-33c655a59ba9 | -22.2642 | -52.4363 | 2025-09-16 08:00:00 | GOES-19 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.7 |
| ed8b6067-0b10-3fae-9c55-e94998663fb3 | -11.7151 | -46.8739 | 2025-09-16 08:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f76531a6-1a16-3aa8-a4da-535be5b9c6e5 | -16.491 | -55.1067 | 2025-09-16 08:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 04d494eb-0c85-3b28-a0a3-da4fbf61cc6c | -10.7112 | -46.5106 | 2025-09-16 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f60130f9-871d-37e2-8750-a31fc353e9ba | -16.4914 | -55.0858 | 2025-09-16 08:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 320a9bc7-79c9-3786-973c-e979c170076c | -16.4714 | -55.1092 | 2025-09-16 08:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| f25cf56a-829a-31a0-84dd-88b42030d083 | -23.2571 | -48.2851 | 2025-09-16 08:00:00 | GOES-19 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.6 |
| 031ca02a-f554-3217-970e-87ebe4d8a8a7 | -12.6729 | -47.9258 | 2025-09-16 08:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 4b0d03b0-03e1-3812-a987-7b2d481b6fd3 | -16.4718 | -55.0883 | 2025-09-16 08:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| ca14f5fc-a492-3610-8569-2182ada020ab | -15.5145 | -48.0414 | 2025-09-16 08:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 4b05d854-bffa-3fb1-91d0-f536a419b5ad | -13.2993 | -54.2207 | 2025-09-16 08:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 8223d04f-dd0c-3dec-abcb-300cf9f49af4 | -16.4914 | -55.0858 | 2025-09-16 08:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 2d8bc94f-a31d-3de6-8e24-da043594886c | -16.4714 | -55.1092 | 2025-09-16 08:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 119.3 |
| 55600733-01fc-3ca8-a4b6-91eccf18945a | -15.5341 | -48.0381 | 2025-09-16 08:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 80be4805-d3f0-30bc-9925-cfc4a6f5264c | -16.491 | -55.1067 | 2025-09-16 08:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 131.0 |
| 7f069ef6-2e37-3e3a-9c52-b6a6528369e3 | -11.7151 | -46.8739 | 2025-09-16 08:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f7a99f6e-d3c9-38c3-b30e-c2a13ee22bb1 | -14.7823 | -51.6845 | 2025-09-16 08:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 05719258-b664-39a3-9e11-afeed47ab0e6 | -11.7151 | -46.8739 | 2025-09-16 08:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a60f5469-4e5b-3e9f-ad14-6e6f7370ef54 | -16.4914 | -55.0858 | 2025-09-16 08:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 5ed683ed-e93e-37b2-b478-2e92d651f32f | -12.6729 | -47.9258 | 2025-09-16 08:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2a675988-c2cd-3d59-b1c0-42d2d678b89b | -11.7147 | -46.8964 | 2025-09-16 08:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 01dcea9f-c59a-3be6-b1eb-d796c0856dcc | -11.7342 | -46.8713 | 2025-09-16 08:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 55dc04e3-3c3a-3ea2-9ad0-c2eb680c021d | -12.6906 | -48.0121 | 2025-09-16 08:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| e3549924-78ae-308a-b7a7-c559d1919dda | -15.5341 | -48.0381 | 2025-09-16 08:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 80.5 |
| afe30b1c-52e2-3297-996d-8f761bc3dda4 | -16.491 | -55.1067 | 2025-09-16 08:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 141.5 |
| 913c668a-8b13-36cb-b8af-9b4bcc619335 | -16.4714 | -55.1092 | 2025-09-16 08:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| 93895d9e-1625-30e0-b333-c335b891c6fe | -16.4714 | -55.1092 | 2025-09-16 08:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 97040af1-8369-3848-97c1-4c59479dcfae | -16.4718 | -55.0883 | 2025-09-16 08:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| f913240d-096a-3040-b791-5bcc348f4526 | -15.8022 | -52.1829 | 2025-09-16 08:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a7ff7a7d-4bb4-3814-93a0-50b4709ef949 | -16.491 | -55.1067 | 2025-09-16 08:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 119.7 |


[Clique aqui para ver as próximas entradas](README85.md)
