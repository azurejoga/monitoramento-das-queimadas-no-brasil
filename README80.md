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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa5716dc-3d86-336e-b05b-5c0e788a390f | -9.9976 | -50.1179 | 2026-09-28 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 2fc35766-3750-3039-aceb-5608e781a22a | -10.6035 | -49.9913 | 2026-09-28 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 281304e6-1409-3e02-9f6f-9bc3b25b0729 | -10.4232 | -53.8219 | 2026-09-28 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| faf67694-122d-3dd1-8c19-324b0d162846 | -13.3436 | -51.3401 | 2026-09-28 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| db67553e-f78c-34ed-a2ec-7addbf13e219 | -13.4201 | -51.3517 | 2026-09-28 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 329e02c6-9498-3d50-8b70-f01d5288c3ff | -9.4813 | -46.3646 | 2026-09-28 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| de57e73a-6423-38ec-b63b-236898c8afd9 | -13.161 | -48.5437 | 2026-09-28 14:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 043d417a-d100-3295-8a8a-2b91ebb1d41e | -11.5352 | -47.3678 | 2026-09-28 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| d57647f0-ae46-3ea8-9a46-56f145bf9ea5 | -10.2254 | -50.0093 | 2026-09-28 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| b5bfcc74-31d2-3cd5-8c98-1ab893c4f5bf | -9.481 | -46.3871 | 2026-09-28 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| f631ccd6-faa5-3b32-bde3-ffc29e998c9d | -7.0361 | -42.8508 | 2026-09-28 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| f7a6ad11-4bfb-383c-a126-6fe3b1cd8972 | -9.4328 | -50.1086 | 2026-09-28 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c5bea697-9780-3b4c-9c80-d899b282eb2c | -12.8059 | -54.0255 | 2026-09-28 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 3ef65477-d39b-35d6-8009-0f5de9bdcf02 | -12.8847 | -44.8015 | 2026-09-28 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 2a7c44c6-bf12-36a0-94dc-03368572d339 | -10.8189 | -57.1993 | 2026-09-28 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 9ab208b0-ed9c-36ad-8b57-717d2358be74 | -8.6451 | -45.3489 | 2026-09-28 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| cea5f54b-2d6c-3096-b863-2dd2b5bd021a | -9.9692 | -45.3565 | 2026-09-28 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 194.3 |
| e975f778-f371-3b15-beef-ca35843fc5c1 | -15.1451 | -43.6088 | 2026-09-28 14:40:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 152.3 |
| 842c7c72-1733-3106-95fc-a8886fd12be5 | -7.7037 | -54.7722 | 2026-09-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 8b356dcf-e320-3f74-b8a4-dd04c3a246d6 | -10.4232 | -53.8219 | 2026-09-28 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| bc826bdc-8716-3fa9-bb14-9f9d925d04de | -9.1871 | -45.7663 | 2026-09-28 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| f654cd3c-7ff5-3b7c-a737-37eeaf8a0882 | -20.1966 | -48.5773 | 2026-09-28 14:40:00 | GOES-19 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6e440fdc-22ed-36f1-a698-bc2efb5cd08a | -11.3735 | -43.4209 | 2026-09-28 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| c6773f6d-ccf1-3be0-bce2-1a2460165ec1 | -7.4974 | -55.0256 | 2026-09-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 3e0bfd3f-b62d-3092-9aef-a56a9140526c | -16.6424 | -48.4724 | 2026-09-28 14:40:00 | GOES-19 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| fa47ba89-1ef9-3ec4-a3a1-1db01ea6cbfd | -15.1847 | -46.141 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 831ab9d5-34ad-3598-92e3-7b2c305623eb | -10.7916 | -48.7377 | 2026-09-28 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| f5c21bf0-1409-3761-b001-81f44467e698 | -7.4492 | -44.5786 | 2026-09-28 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 301dd63d-5d37-3421-b178-90c91cb21373 | 1.6018 | -55.8643 | 2026-09-28 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 410814b0-06cc-3ddb-9565-8eaad71ffe72 | -10.6094 | -53.9902 | 2026-09-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| db48eafe-2240-3ed3-860f-ebc7291f46fb | -9.206 | -45.7642 | 2026-09-28 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 3cb9a1cc-8410-36c9-a7ce-57b3b1ec6916 | -12.2057 | -50.7745 | 2026-09-28 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 7a8a2801-9362-33e0-95f5-cc642a27f3ac | -9.1584 | -61.4082 | 2026-09-28 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 82cf9f7d-7505-3af2-acd7-3d154a29f968 | -12.7028 | -47.3189 | 2026-09-28 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 17d33d80-f306-3921-8c7d-2d9cd8efc0cd | -10.2065 | -50.0113 | 2026-09-28 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| f7c517c3-4185-3c97-a263-62138247a795 | 1.62 | -55.8838 | 2026-09-28 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 33141af3-cf87-36a3-bd31-8c9a29628eab | -12.2897 | -50.2712 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 8c1cb125-2e7d-3a22-b2d4-351dd719ba72 | -10.4229 | -53.8424 | 2026-09-28 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d50d9df8-b929-3a5d-9363-3a173df9bf18 | -8.3608 | -45.4695 | 2026-09-28 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| af46d00c-f28b-3028-af88-55d742e521cc | -10.872 | -54.0899 | 2026-09-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 6f8dba93-7c91-3b4a-be94-98f356464988 | -10.8052 | -60.7257 | 2026-09-28 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 4965e745-576e-31f8-a454-47d6d1f94f78 | -9.4328 | -50.1086 | 2026-09-28 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 56186293-772a-3139-acf8-e4691ecb60a5 | -13.161 | -48.5437 | 2026-09-28 14:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 74c30e74-6591-3523-b799-de395c08793f | 1.6566 | -55.903 | 2026-09-28 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 4965377e-b569-35b3-bf54-37d7ff5e46fc | -10.2067 | -49.9898 | 2026-09-28 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 87bd3e98-621e-38e2-a594-06b7b86c350e | -11.7837 | -50.9939 | 2026-09-28 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3f00b4c7-c172-3dcb-bb67-ae048757e311 | -11.7828 | -51.0578 | 2026-09-28 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3638a903-7d83-32fb-963b-231759ff211a | -10.7064 | -44.4317 | 2026-09-28 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 2273ec5c-2ea8-3df3-a5f3-f531d238cf0d | -12.6878 | -45.0192 | 2026-09-28 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |
| d73d41af-bef8-34ba-a21a-e343f0e73513 | -9.1771 | -61.3882 | 2026-09-28 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 9c0b2e85-70ab-3dc1-abb9-779f94c1067e | -12.1869 | -50.7553 | 2026-09-28 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| fffec555-673a-3aa7-aa7a-c8fc3cdb17c1 | -11.5628 | -50.5069 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 656f96dd-9b60-38e7-9bd2-d9562e82dc15 | -12.2894 | -50.2927 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8fe110a0-f8c1-3e17-80e1-7c1263200f90 | -12.6836 | -47.3217 | 2026-09-28 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 140.8 |
| c2e3d077-b346-31ba-b691-e4355cc1345c | -11.7322 | -50.6158 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d5bbcb8a-7b63-3f0a-a304-9c1aa3eed295 | -11.7135 | -50.5966 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 68008fe9-eeac-34c9-9b09-6723073e21fc | -11.5818 | -50.5047 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f7d24fff-9000-3dc5-a572-ff9860b48f22 | -8.2291 | -45.4602 | 2026-09-28 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 154.3 |
| a61211a8-e2ad-383f-a462-78a1da24fa9b | 1.6749 | -55.9225 | 2026-09-28 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 40adec38-25b4-3938-badc-82aaf6dbc8b7 | -10.2653 | -44.6298 | 2026-09-28 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 7f9e662e-9b1b-3327-8b99-7c290a175b27 | -10.4043 | -53.8236 | 2026-09-28 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7a1f5417-aec0-37c9-a4e3-f08aa5b28528 | -13.1606 | -48.5658 | 2026-09-28 14:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| acace53e-205f-3cd3-8ea3-68e013013b71 | -11.0764 | -51.3885 | 2026-09-28 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 162f4f92-e507-3e17-b0c3-40e7ebcd33b3 | -11.0235 | -54.0354 | 2026-09-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 77d59533-cc4a-3865-8833-19eefa250cb8 | -11.5625 | -50.5283 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 2e1d9bb5-fb6a-37d7-ade8-5e499459b473 | -10.6035 | -49.9913 | 2026-09-28 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| b07b1d8c-cb53-332d-ac51-377ddb847871 | -15.0153 | -49.5904 | 2026-09-28 14:40:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 6732c21f-b935-3fe3-97d9-561be95b5d11 | -10.0164 | -50.116 | 2026-09-28 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 10777631-15e3-3e28-a8ab-a413750f5cf6 | -12.2063 | -50.7316 | 2026-09-28 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| afed4b46-9a63-32a1-879c-7174d43540cc | -12.7868 | -54.0275 | 2026-09-28 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 9ba59af5-5ab9-3d5c-b405-2d73ea602c55 | -15.3998 | -47.9261 | 2026-09-28 14:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 31299f64-244e-386c-9ad1-2c079b4c6241 | -12.3085 | -50.2904 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 4fed56f9-47b5-3a41-80fa-88e7f20c8224 | -12.1075 | -45.2248 | 2026-09-28 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 54d21164-8684-3ac9-941b-6b5a7fc61e1d | -12.2703 | -50.2951 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 6d62f02a-c94e-33ff-bfdb-876b57a92954 | -11.7129 | -50.6394 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| d381eae5-6f4a-3494-ad7d-4968041639c6 | 1.6565 | -55.9818 | 2026-09-28 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 95d4be5c-67d6-36bb-8f69-7cc41c7a2997 | -12.0618 | -50.2127 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 18e220eb-0458-31eb-8919-faf7e0315f26 | -10.11 | -50.1708 | 2026-09-28 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| d4f1f26b-6b8a-3739-8d68-5e1911b39cbf | -7.468 | -44.5768 | 2026-09-28 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 42251a14-1146-3ba7-9031-4abd78852399 | -9.9695 | -45.3336 | 2026-09-28 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 332.1 |
| 071f3372-352e-3e24-b1c6-f1c660aee4a9 | -10.2154 | -53.9011 | 2026-09-28 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 8ff87767-2d0c-3e5e-a392-2aed46091bb2 | -8.5982 | -54.6341 | 2026-09-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 767cc690-f9bb-3ec5-a645-1814d9ec21f5 | -12.0352 | -50.709 | 2026-09-28 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 272496cc-e87d-3706-b02c-b2738bfcc46c | -8.2293 | -45.4375 | 2026-09-28 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 118.5 |
| fb750b6d-26c7-3d4a-aa19-af7ef5035d10 | -11.2307 | -54.078 | 2026-09-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 903128b2-6580-3e64-a0d7-f8f2e2ffb275 | -8.5984 | -54.6139 | 2026-09-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| bd8ffeed-142e-396e-a0aa-bcf65189f6f8 | -12.0615 | -50.2343 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 393e17ef-af74-39ab-a99b-9063f9657783 | -12.1362 | -50.3328 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 702dbf56-4c01-3e7b-8b70-b14fa91162cd | -10.7343 | -48.7661 | 2026-09-28 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5d746462-29f3-3074-ad6c-f88c0fce0431 | -11.373 | -43.4446 | 2026-09-28 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 580a8a43-cf17-3344-aa12-6a4c80a8fa41 | -10.8723 | -54.0694 | 2026-09-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 2ecd1e13-4d49-3b76-9873-c3af16bfc446 | -11.764 | -51.0386 | 2026-09-28 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 30f0f0fa-a863-34cb-870e-bdbd78ea3e34 | -12.1678 | -50.7576 | 2026-09-28 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ba694ef5-33fa-3eb3-84e2-00311689bc0b | -12.8059 | -54.0255 | 2026-09-28 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.0 |
| ef3a79b4-d771-3003-97c6-2a4a3e09ad28 | -11.9806 | -50.5443 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d3d2fbd0-831e-30b2-a0e1-8f3cf1d1054b | -10.4046 | -53.803 | 2026-09-28 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0c57fa67-ba98-31c0-a1db-226670e779ab | -11.7643 | -51.0173 | 2026-09-28 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| afd3c08e-340b-3c86-a6de-d5868974704b | -11.1966 | -44.7805 | 2026-09-28 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 555.4 |
| 1c90dfad-8997-3943-86bf-4e5567dc9adb | -8.6169 | -54.6328 | 2026-09-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c491fdbf-2192-368b-a2ee-79b8d1643ace | -10.7115 | -60.7312 | 2026-09-28 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |


[Clique aqui para ver as próximas entradas](README81.md)
