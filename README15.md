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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cf8e1e3-3a62-3698-ad19-6001dabc582a | -13.87807 | -47.46664 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d961cb9f-751d-3a72-9451-295d819aec1f | -10.0673 | -47.9153 | 2025-11-19 04:31:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc43a2d8-1043-38a6-9453-b7692f97afaf | -13.88474 | -47.42395 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a192b27-7bc7-3f12-82ea-aef1926491cd | -11.35138 | -37.42543 | 2025-11-19 04:31:00 | NPP-375D | SANTA LUZIA DO ITANHY | SERGIPE | Brasil | 2806305 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dd4f463f-4a93-387f-9e9f-fb873636c687 | -13.93507 | -47.51233 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b0c0c64-5011-3c97-bba8-4cabcf58419f | -9.39684 | -48.44833 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 09f9df8b-dc9a-33c5-b330-905e187365f4 | -11.03266 | -44.89395 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5f74d29-5c6f-3056-8e16-a9d0014dfb43 | -13.93894 | -47.50935 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6dcee4a6-a32f-3e47-a86f-5012ed5e690d | -10.64709 | -44.78117 | 2025-11-19 04:31:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c0bee9c-3f3d-3481-9c4f-42cb4812e03a | -13.51859 | -47.92068 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7caf636a-14e5-3442-9e65-9082e4bbd5f8 | -13.87752 | -47.47021 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2f534f3-a433-349d-9b90-b5aafddc8bb3 | -12.01223 | -46.76555 | 2025-11-19 04:31:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1325d155-8f79-3b66-8a05-156f46ae6e24 | -9.40023 | -48.44888 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a12416ac-0025-3010-b5c0-98680376e270 | -10.29242 | -48.89618 | 2025-11-19 04:31:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e44c8675-11eb-3bff-a734-f0b2c199ad71 | -10.87697 | -49.54315 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb582db7-bbba-3fbe-ad1d-3391eb3d4d46 | -10.35467 | -48.89823 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5dd5825-7879-3a7e-bde3-6cb654c2be6b | -13.89193 | -47.44341 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6df00ef1-ad84-351d-9c8c-07f815b55f43 | -13.88305 | -47.47845 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e798141d-ad5d-353b-b5c7-23f9225a35e5 | -13.89138 | -47.44695 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf639721-854d-3140-af98-bc75333960b5 | -10.78936 | -47.97786 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b66ceddb-f3c0-3436-8f8d-087e3e130ace | -11.02975 | -43.89372 | 2025-11-19 04:31:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b3f84f70-2930-370c-b8a9-8bb135bfe3ee | -10.76638 | -48.03588 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ddf6872-6ae3-36a2-8001-613d6a4a5fca | -10.79833 | -47.97983 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6059f24-fc52-34b1-99cb-b2f4d49648d2 | -13.89525 | -47.44397 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bbae888-6aea-327e-8022-8159d6e5adbb | -13.88032 | -47.40855 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96b8ca1d-4236-3986-80c4-3c06d280eec9 | -11.49996 | -48.23352 | 2025-11-19 04:31:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80290888-40f8-3f34-bc76-8219e355efc3 | -12.53221 | -48.75305 | 2025-11-19 04:31:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9163cc1b-d1ab-316b-bf0d-72348a4e62b6 | -10.69261 | -44.78822 | 2025-11-19 04:31:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9187a490-b93b-30b3-9529-5793abf297ce | -10.37896 | -47.53514 | 2025-11-19 04:31:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 349aa6a4-7a6c-3001-87e6-c934e7024ed7 | -14.39286 | -48.28007 | 2025-11-19 04:31:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 318db3a4-63ef-39a3-bb71-3bc59d46a963 | -13.91015 | -47.49725 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8253eae-7c0e-3976-bb2f-f8f9ddf37c37 | -13.51803 | -47.92422 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a35ee89-2739-3662-9104-a2de70a999c3 | -12.45889 | -54.44903 | 2025-11-19 04:31:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 487f4bc5-a6b6-3cc3-9082-0f0eb761a561 | -13.88418 | -47.42752 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d698fe9-792c-3e54-9391-97ba6c1377fd | -11.66946 | -47.97329 | 2025-11-19 04:31:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c2f1545-ea5a-3031-bea5-9f8c429ecd8f | -10.34822 | -48.9162 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8d4fd17-9998-3f17-a61e-13ceed7b466d | -14.53363 | -48.01113 | 2025-11-19 04:31:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c68e601-8f83-3b2d-a986-f4d0b81ebc2a | -13.92068 | -47.42953 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd0050a9-4777-383a-b82c-4c06939a8be2 | -10.64301 | -44.78454 | 2025-11-19 04:31:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99b05e28-cb67-3515-87a9-98c164b43b62 | -14.38954 | -48.27952 | 2025-11-19 04:31:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4945c510-5654-3ed0-b0cc-c683dfd796a9 | -10.69611 | -44.78876 | 2025-11-19 04:31:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9472ae5-456e-38c1-b521-50edf0528f74 | -15.28657 | -53.15329 | 2025-11-19 04:31:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba6672b4-644e-3fd9-ab65-c155257b2d6f | -13.89248 | -47.43987 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd2c0274-a3db-3a3e-9a5b-680283872ac5 | -10.9419 | -48.7071 | 2025-11-19 04:31:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 51bdae81-0e28-3f90-8e97-d2df50e089ab | -11.66613 | -47.97274 | 2025-11-19 04:31:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ea7199e-ee5f-3e4a-9714-8e2580e5fe9f | -12.04081 | -43.764 | 2025-11-19 04:31:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18b7361c-7289-367f-9fd1-41140c12e6b1 | -11.62323 | -43.90579 | 2025-11-19 04:31:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3bc3de9b-cf6c-33d2-a99c-235fc0b923c5 | -11.92902 | -44.22474 | 2025-11-19 04:31:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad9a1431-4f7c-3f39-a743-600ebdf8f27e | -10.35322 | -48.92845 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e084ae3d-ea26-391e-a320-5ad7b350d4e4 | -10.06453 | -47.91121 | 2025-11-19 04:31:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55e07c24-f19c-3b3e-ba62-e01ea6a309e8 | -10.74295 | -48.18221 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 638a4201-eb40-3bad-8635-356830c0c960 | -13.92068 | -47.47334 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10651f58-a9f7-3718-9ac8-c860016937f5 | -9.99891 | -44.07644 | 2025-11-19 04:31:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28f27cf2-e9d1-3cac-8535-5d99d116792f | -10.35262 | -48.93212 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 636de017-296d-3945-a9ce-80b7089de74e | -11.88443 | -40.94939 | 2025-11-19 04:31:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| aa939524-c547-3431-84b3-0843e47e81ac | -9.37107 | -48.41412 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6a382d2-5a1e-3dc9-93fa-404f58c19995 | -10.77593 | -48.1185 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd379664-5e0f-332c-ae1b-794c3b2d27b4 | -13.9312 | -47.51529 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9446d20-3945-3faf-8fe3-35c35f56ff17 | -11.20765 | -49.41288 | 2025-11-19 04:31:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35785fa7-bccf-310e-8680-091afd0402a8 | -10.87762 | -49.53929 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f7f1d95-8349-3a93-8a5e-c028dbbb6c15 | -11.28656 | -48.49967 | 2025-11-19 04:31:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd0ba654-8a5b-3aaa-a553-c151538dae1c | -11.21065 | -47.92369 | 2025-11-19 04:31:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9c9c0e6-d336-3685-b5c9-6232f3864efc | -10.54687 | -44.11943 | 2025-11-19 04:31:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03c607a5-5184-3a75-98fd-0424de90fc91 | -13.06995 | -42.13781 | 2025-11-19 04:31:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b6c63d28-cb04-3aee-85f0-f84cb7806d13 | -13.90083 | -47.40825 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e23154fc-7667-3c8d-bec3-7aa4bb252dd6 | -11.27808 | -48.5094 | 2025-11-19 04:31:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8db2ebc4-03a9-3ef7-85d0-9bcc7d806370 | -10.8106 | -48.09496 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 682dc0d1-048c-36bb-9304-7a12c3fd9671 | -9.39905 | -48.45619 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e64c024b-bf38-3845-98d0-ad69b8863c89 | -13.91902 | -47.48405 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d111ce7-7c86-3775-a6f4-be852b4795a3 | -13.43226 | -48.23421 | 2025-11-19 04:31:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8008c7ad-003e-3612-9c27-87590fee54b3 | -10.3498 | -48.92789 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d86a512-d736-3fd3-8dc7-c02cfe408531 | -11.2161 | -49.71881 | 2025-11-19 04:31:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9279bb58-98a5-3523-a312-13cd31c878b6 | -10.0475 | -54.33856 | 2025-11-19 04:31:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cf0b163-253e-3225-8812-5e2c94c1f845 | -12.52886 | -48.75249 | 2025-11-19 04:31:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fbcd8b6-5758-32b8-b08c-a82dc178d7a8 | -10.41105 | -48.83158 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcc8c178-dcea-3a1f-a3ab-e6c3eb1b4479 | -9.38565 | -48.43148 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a1c84b69-7c52-3857-84a8-656bd0d64580 | -10.84609 | -47.62183 | 2025-11-19 04:31:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ceb0c86c-e65d-3029-98e3-93c282bca5df | -10.82816 | -48.02839 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ac0d6d1-1bc2-38ae-922d-5352c667a330 | -11.28211 | -48.86857 | 2025-11-19 04:31:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 574edfc9-4570-35e3-8e2e-ff511ab2f229 | -10.34883 | -48.91249 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e55a2f13-7077-39d9-83e5-b09c46578c6a | -10.41045 | -48.83528 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42907f1a-f965-316d-a728-9a863411a982 | -12.40377 | -43.15547 | 2025-11-19 04:31:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| aa2a6f86-7b3c-31de-9b6e-d4531e31f2d8 | -13.89082 | -47.4505 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33a27680-4f94-37f2-b0a0-2ed385620560 | -10.06787 | -47.91175 | 2025-11-19 04:31:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc8bfe21-5d15-35ea-905b-25886c7306aa | -12.00009 | -49.26682 | 2025-11-19 04:31:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74597c4e-5eec-3379-bb01-f24d49d0b568 | -10.35224 | -48.91306 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb55bd48-ab7e-3f04-a770-931d5f7101c4 | -13.36951 | -44.05362 | 2025-11-19 04:31:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 108ccc87-70bc-3e9f-801d-28e680aa5b79 | -11.85984 | -46.96295 | 2025-11-19 04:31:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e9ee225-695f-3e89-a134-99b055dca755 | -11.61888 | -43.90964 | 2025-11-19 04:31:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0fa4425f-7b26-36a3-ad97-a069702eb268 | -15.42882 | -48.06359 | 2025-11-19 04:31:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b526a4ae-f461-36f9-9de0-8fc7896b66ee | -13.8814 | -47.4672 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeffdb1d-2a59-3199-9331-1f83e3195552 | -13.91957 | -47.48047 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc7e69b6-b9ca-38e2-a537-c7492145141c | -12.60335 | -48.87694 | 2025-11-19 04:31:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abe32d3e-0da9-3c9f-b8b2-2cffc655a3f6 | -10.09856 | -47.89135 | 2025-11-19 04:31:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df8bb8c9-579c-3eb0-a449-e94d30b62c54 | -11.67059 | -47.96622 | 2025-11-19 04:31:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1902b46f-4cd9-34bf-b951-606c342cfd5e | -9.35373 | -50.74092 | 2025-11-19 04:31:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2bc93cb-3a99-321a-a2d9-48c3a05ce86d | -10.68848 | -44.26249 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55aae976-782a-3e7b-8c61-cba181a456b9 | -9.38904 | -48.43204 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae6885c7-1b8c-331f-a59e-d56ab6d68dba | -10.37057 | -49.89023 | 2025-11-19 04:31:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1911119f-2672-398e-98b4-5e6a12b5b79b | -13.20607 | -48.31702 | 2025-11-19 04:31:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README16.md)
