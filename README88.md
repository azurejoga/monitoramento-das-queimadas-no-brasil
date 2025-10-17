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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f9a05d9-1d2d-3a27-bfae-ac83ee2a254b | -9.7122 | -44.55842 | 2025-10-17 04:51:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30421514-f1ad-32f5-b72e-d5317e3bbd71 | -9.21561 | -61.54419 | 2025-10-17 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ec0e9e5-1685-3428-a7a4-06885b7e7b7f | -8.123 | -45.54776 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bdb0de7-43ff-31a8-8a54-7130605b48e3 | -8.15485 | -47.98513 | 2025-10-17 04:51:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1597a504-0bc3-3715-9234-d455a877013e | -9.27049 | -45.27007 | 2025-10-17 04:51:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b02245bb-43a8-3742-9468-6ac8d991a515 | -14.34143 | -51.46068 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| bda039ae-5d70-3f14-9fbc-21ccdf69eb77 | -8.12358 | -45.54373 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc0d093c-6f24-336d-9a2a-dc20ea211284 | -8.47163 | -50.10526 | 2025-10-17 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c991b730-f1dd-36da-9ba4-20ff8a448564 | -10.11508 | -44.55531 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6770f135-0e4e-322b-8342-8b5b94963ff1 | -9.97859 | -47.01289 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6c5b567c-b9ef-3980-8510-c01b23481fcd | -10.95374 | -49.76443 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| d145bbb7-215f-3e26-a9d2-56db49b3fa97 | -10.65155 | -45.2475 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 429d1498-9417-3dd8-85fd-b897994637f8 | -8.12241 | -45.55177 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 668ef8a7-eb0e-30ab-926b-cdb6e5831e21 | -10.49957 | -43.40858 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05936e44-8f8d-357f-aad1-5a2f4c0a2eed | -14.91976 | -46.72994 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d4748236-27f5-3aa3-915a-6d28723f502b | -11.40144 | -44.23431 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 86a1b117-5ddb-33e7-aa05-cc72a61e5d81 | -9.1395 | -46.59962 | 2025-10-17 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 953454d8-1e73-3644-82a0-4d2d41c8852c | -9.30581 | -47.67377 | 2025-10-17 04:51:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d57e7b1b-8a05-3a46-b89e-03b212c3b580 | -10.95196 | -49.77614 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8d4ff884-844a-3c85-8f92-f622218b6709 | -10.17736 | -44.78872 | 2025-10-17 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acd229fa-b2ea-3ab9-9edd-cb79e8e04b36 | -9.88428 | -47.68205 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee2eff46-8221-34c6-9227-271527509d54 | -6.60271 | -55.53924 | 2025-10-17 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dfc43bb-fc1a-3c55-9e30-ac91763eaadf | -12.17086 | -45.06604 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f3a8706-46d5-3843-a768-2f611a8e711f | -9.88496 | -47.67732 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c88f14c-1999-358d-944d-2b5174ada464 | -11.96874 | -46.55539 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cff12ec1-4e72-3b6c-868d-84527544efaa | -8.41251 | -46.27959 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a18b7ef9-ebbc-3b04-820f-2dbcfdf68a4c | -13.4241 | -48.57272 | 2025-10-17 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a25996c-9370-3f1d-b261-da1bf6d423f1 | -8.44698 | -44.17713 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9d38a91-c964-36e8-813f-d485b2297d1b | -13.93892 | -48.6913 | 2025-10-17 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9e15d63-dd48-3b30-8820-49c4e5d1d2dd | -10.2296 | -49.86731 | 2025-10-17 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 838d9def-f4af-34ad-a082-94a0d63cd96c | -9.43387 | -47.90108 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1029f61c-e912-3082-afcf-b7fc2c50f967 | -10.64477 | -45.29883 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6443c25-5e4f-37e6-b2c2-b0c962a90a93 | -8.39602 | -46.24817 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f74236f-10b6-3a28-89cc-683ee6659b12 | -10.29096 | -44.02629 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c87c7727-95be-3895-8ae0-39179a0c04ec | -9.34841 | -46.92409 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f436373e-2ce7-3f1d-ac78-86e915611622 | -12.92512 | -48.59739 | 2025-10-17 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ef3c1e7-51a8-38db-ab2e-d80c7699894e | -11.62278 | -50.67926 | 2025-10-17 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34a57ec0-a44e-3b0d-8f17-27dc803213f2 | -12.15823 | -47.93663 | 2025-10-17 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15f5b3ee-a954-3efe-9897-13e5a99d78b2 | -8.58595 | -48.63602 | 2025-10-17 04:51:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 980d3336-1a39-34e1-88ae-d47aeea0aa6d | -10.62191 | -42.31414 | 2025-10-17 04:51:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 686f80eb-f683-3792-88b9-e28966934036 | -11.32851 | -44.93673 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2799f40-6c84-3b77-8b39-0fbf5626b589 | -10.72196 | -47.58651 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a712458-f593-3f6c-8a3a-67eafa26c91a | -8.45057 | -44.18002 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 81924c8c-0ac6-345c-a614-255ca9e501d9 | -9.88196 | -47.6836 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 481899c7-61ce-3ad5-999d-e5f10c9522c9 | -11.37768 | -44.18544 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64d24447-227a-3125-8e56-5a5a9d077090 | -13.43416 | -47.95064 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02c85ff4-dd37-3265-91a9-eec1ef9c31f6 | -8.45186 | -46.24018 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f9647903-c2ca-3154-96b1-be8b8516ea71 | -11.47341 | -45.08006 | 2025-10-17 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24936d7a-c92f-36c8-9ba5-2b11f4feb0bc | -11.47848 | -44.19417 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 3cb7814b-a3ae-3670-b25c-876ff6bc6672 | -9.13826 | -62.29959 | 2025-10-17 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f51e8d03-f26a-3da9-97f3-d2ccaaf23fa7 | -11.58059 | -48.56371 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3eb725fa-fda9-37c2-920d-0425d952acb0 | -14.23722 | -54.90201 | 2025-10-17 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ee232d9e-1621-3e4f-80ce-72e56f862a6b | -8.25387 | -44.02517 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 942f65d3-0a64-3fc5-b5e2-a23f2b618381 | -11.58199 | -44.05748 | 2025-10-17 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3eb9d854-d437-362f-8d61-c45f2e662529 | -7.85751 | -49.65219 | 2025-10-17 04:51:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebe39747-b016-347a-a0d1-5c3ec5f550c7 | -11.09423 | -45.87761 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eae787a7-0247-3667-8d49-8c7e343b340f | -12.16488 | -45.06236 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0180a0f-a7fb-3312-9b37-76ad3ca692a3 | -13.27316 | -44.48414 | 2025-10-17 04:51:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de382a89-9353-3cff-a839-4c224c08b9f9 | -11.4827 | -44.20048 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| f460a312-0609-3fb2-baa7-f2ee078b0745 | -9.88054 | -49.11939 | 2025-10-17 04:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44b01e07-c3a6-3e18-91d8-e8d1023294aa | -8.56402 | -44.58608 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3490104-0f31-32fc-820c-ceed666a6d4c | -11.57771 | -44.05104 | 2025-10-17 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1ddb0357-cb3c-3b43-8ebf-080819c6048a | -10.18589 | -49.50913 | 2025-10-17 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fab19c2-769e-38fd-af3a-77fecc8dd6a6 | -9.4001 | -47.60374 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5206bed2-340b-35ba-b359-3cd174667937 | -10.28196 | -44.02596 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d45f844-8875-38fe-a69b-426c3a9f4e08 | -9.64522 | -47.1306 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e59f5dcd-2d14-3538-883c-755d24ef8087 | -14.93453 | -46.71939 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2fd45fce-3149-3252-8765-6175e4724977 | -8.72604 | -43.87562 | 2025-10-17 04:51:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b9242ea-0fbf-35bb-96e9-a58023c5b36f | -13.45391 | -44.28888 | 2025-10-17 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67329880-2ffa-398e-b6c7-5368f51b643d | -13.01411 | -43.83915 | 2025-10-17 04:51:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53b8717a-8a56-3baf-bcb8-d225ee48ffe7 | -14.33349 | -51.42136 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19354e09-3e29-326c-882f-62dfe61640b8 | -11.59553 | -44.07107 | 2025-10-17 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c35d1ba8-aebd-313a-86a1-e23341ab396a | -8.4017 | -46.23785 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 492289ae-a995-3735-adf0-ccd17ed1588e | -8.33632 | -46.2352 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2472e2c3-43b9-3a4d-a80b-96b369e8e71d | -14.32505 | -51.47705 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f43067f-d10b-34f9-a56f-ff37bd5df1e1 | -12.04559 | -54.24347 | 2025-10-17 04:51:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a047af91-6809-3683-938c-886cc35474ac | -10.9425 | -49.47947 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7f3d692-b9e7-35e9-bc74-ed3b15140abf | -10.94847 | -49.7756 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 637f2531-c037-3b07-ba4c-ae348a12efe7 | -9.97933 | -47.00761 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac9b218e-88f2-334e-a312-adad41f9c8f1 | -10.65561 | -45.28682 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6b50ab28-abd2-30e8-8eea-17c951f80dfd | -10.28523 | -44.03144 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1c4b6f42-f774-3bac-bc8f-04ccb5006731 | -12.43038 | -51.30284 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6419f981-9938-3f05-8189-8c7118c3a310 | -9.12918 | -46.64225 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 042c4446-5a98-37f9-b6fc-fdf9d112b25f | -12.42926 | -51.3101 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8630699c-ccb7-3902-9dc2-96f931483c88 | -10.98183 | -47.91556 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eff30a6f-2d1f-3f63-9ca6-d249a9fd51c9 | -12.78037 | -44.88572 | 2025-10-17 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2801ad57-3cf9-306a-8453-3975799760e6 | -8.55941 | -44.58536 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b3a73ff-d2b7-36b5-9df2-b6166a89ec26 | -9.27583 | -45.29729 | 2025-10-17 04:51:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aae6e29c-204b-30e0-951a-01a8869b2cc2 | -14.33974 | -51.47181 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f909b364-744a-3c5c-bd91-5168012d5035 | -9.24684 | -44.36576 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 780ac48c-a76d-3d47-b5b5-b72894bf294e | -11.50119 | -44.05803 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3d87a24-976e-36d2-b9f5-9de4dbcf8ce0 | -13.25351 | -47.13549 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 332f46db-b138-3524-b56d-9939e2ead292 | -9.34672 | -46.90792 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b5adbf8-c673-3a7b-9266-b1826d7ec402 | -10.50222 | -43.42852 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e333d8bb-004c-3447-bd25-ced12076f603 | -8.48904 | -49.04448 | 2025-10-17 04:51:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7135b9e5-e304-3ec7-bd64-70caa535809f | -8.83843 | -45.97646 | 2025-10-17 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2633eb47-0dac-3f9b-b7cf-344d7ff6e95f | -10.50751 | -45.03886 | 2025-10-17 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0e9fac8-1abd-3e5b-a1d5-3b54dcfdbb10 | -14.32841 | -51.43197 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 792cbf14-d08f-39ae-b4ca-a9bd353af84c | -10.43147 | -45.01693 | 2025-10-17 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 48544a0e-c7dc-35cc-84be-0a6a96365c03 | -11.7124 | -44.26762 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README89.md)
