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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35735c2d-4c6d-3b27-9deb-663fd491bdbc | -11.01388 | -47.87663 | 2025-10-24 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cce48cd-5af1-31f8-a7bc-44e8928c736b | -15.13771 | -47.92684 | 2025-10-24 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8dffdc77-fc05-37ff-a6df-17878c1521d7 | -14.253 | -44.09108 | 2025-10-24 04:40:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a47b768-9f87-3c79-a1cd-1a27804ffaaa | -11.01901 | -49.83063 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2a405db-3fb5-3bd8-8be4-1454a3a3251a | -14.38421 | -51.51793 | 2025-10-24 04:40:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d85a8a5-00d1-3f61-a31c-e5c8b290d4b5 | -13.89079 | -48.35763 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce6ac7f3-4849-3fc7-b51d-d17285c837f4 | -12.81816 | -48.67072 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bd32726-9bc5-3495-b2f8-7301843caaa8 | -17.59586 | -46.62505 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6df0300d-1595-34a6-8b0d-9372b56135f1 | -13.29973 | -47.45181 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b847a624-a486-34aa-ab29-41e5d8f2a927 | -13.91121 | -48.39044 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25cddf86-f2e7-358a-8221-86f236dda1a1 | -13.0366 | -48.70723 | 2025-10-24 04:40:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db8940bd-81a4-3a41-b017-6a14b3bf043e | -13.90362 | -48.39325 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc98d624-5471-37c5-a103-3e0a6100e6e2 | -13.28016 | -47.48454 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 820d1343-40d3-3259-b6ba-d1a331ae548a | -14.47272 | -47.90702 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ddb18a5-8079-39fc-9140-b57bfdd098b7 | -16.64251 | -49.31402 | 2025-10-24 04:40:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90e228d5-7eae-32c7-aab7-029efbe408c6 | -13.35983 | -47.96371 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c402b78-eb8d-39ae-9898-cb35bb69be58 | -12.81856 | -50.93584 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a02f38d2-8465-34f3-ada4-03402ed83e97 | -14.48222 | -47.91777 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6c0fe274-1c0c-333b-bbe4-71e37ad53325 | -11.02728 | -47.90616 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23e4a9ee-9e2f-362a-ae00-7fb24496b0bc | -10.99251 | -49.54444 | 2025-10-24 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f67d4b77-e59c-3be6-a54f-25b9e415f997 | -13.90418 | -48.38937 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fab9d43-9b4e-308b-82b8-c4a5c8b8a283 | -10.39188 | -51.52924 | 2025-10-24 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79d81a1e-ac4e-3c17-8bac-f3f480cbc9d8 | -13.02732 | -48.58001 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b04e6267-4105-355e-9907-ae3196d74b70 | -15.83244 | -49.09735 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6747f52-1550-353f-a0c7-512ef0944fa9 | -11.0127 | -47.88445 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47b7095d-459e-3f66-8fa2-1a73a7b1d823 | -12.82933 | -47.24842 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0b47adb-e1ee-34e0-a9e9-5598c361ed13 | -11.74568 | -45.35232 | 2025-10-24 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e279ed3-16a3-3eec-8c6b-76f44a051e28 | -14.46432 | -47.91401 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7507220c-5585-3527-a76f-14f771631409 | -12.38962 | -57.52264 | 2025-10-24 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cf1f3be-6177-3329-ac14-8a2b7b9a00cb | -13.89958 | -48.34654 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b553df1-414b-3041-a780-f49da62bfb5a | -12.72878 | -46.95846 | 2025-10-24 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ce7feca-3244-3e0d-b2eb-2781921380e0 | -14.43591 | -50.95467 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f48d2fb3-e1d7-325e-a3a9-a774da17d74a | -11.48482 | -54.02079 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81f0dcfe-aa92-31f8-8c52-23beb693262a | -13.25852 | -47.89029 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d20a6814-4669-3582-9267-1429be60c448 | -17.31489 | -43.60391 | 2025-10-24 04:40:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a368de6b-8de5-30bf-b606-0eeb3ad5d9f4 | -14.2721 | -48.06327 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5629bbae-55b8-3d2a-9d71-1b0e9dff8841 | -13.88594 | -48.38671 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cb75e319-46b0-3337-9734-ad419930378d | -11.89441 | -51.52882 | 2025-10-24 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00d67e6d-aea1-3d16-a289-62d5553a178d | -13.91533 | -48.38681 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5805786-1c41-3d57-95da-9ecd306df1f9 | -12.82505 | -48.67176 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5af60a16-8437-3a23-baa4-51561611bb01 | -9.75552 | -55.34604 | 2025-10-24 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d04364e7-f4ab-3435-92bf-df3c64138012 | -12.25273 | -47.46415 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c48468c-ad13-3f48-8953-3e7715f8d4cf | -12.87157 | -48.59683 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d09de334-90c2-3608-aa4e-a06ef0a29835 | -17.6532 | -46.65966 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8b3c3ff-7bec-3806-8f2d-1adce639215f | -11.02787 | -47.90226 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15827b69-71ed-33d9-8eed-f81e0333ac2b | -15.28924 | -50.77285 | 2025-10-24 04:40:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea38fde7-ca40-34fa-b447-f3a84f32a851 | -13.58961 | -51.38598 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cdf2dfc-9a42-3a04-8683-100808686120 | -12.29216 | -47.45651 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 460700ba-2875-3bd4-9ab8-7b8836092e86 | -11.36982 | -45.92881 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d33a60a9-b725-3f03-b4b9-2e2a71dd97f5 | -14.74589 | -46.60578 | 2025-10-24 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc31b961-2ea3-3ce7-b061-03c3be0ce0f0 | -12.83067 | -48.63421 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 904b2210-2250-31a5-8f51-79b60975bc93 | -16.48688 | -47.81955 | 2025-10-24 04:40:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2648a8b0-2337-3ac5-8f72-8cea7bdbe4a0 | -12.0571 | -46.41567 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ab7cb13-3afb-30ea-a9b4-991724fa3890 | -13.74618 | -43.97043 | 2025-10-24 04:40:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e8b9766-b7b8-3ed5-8406-a9381ac6502f | -14.74916 | -46.61091 | 2025-10-24 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3e3914e-7957-3543-ae5b-0d46519017ab | -12.17417 | -49.42971 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e861613-b1aa-3a9b-8d95-7daa51326b69 | -10.91224 | -50.1657 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 257b36c1-8ec2-3a19-9da6-953e4df69158 | -11.55094 | -54.5138 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bf5081f-0415-3242-b946-3ea34d14e22f | -11.48129 | -43.24382 | 2025-10-24 04:40:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ce8009c3-66ea-3fa8-a3b9-7c729ff10d41 | -10.99334 | -54.2561 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcc058a6-fecb-3b86-ba23-cc1e91ddb9d2 | -11.43885 | -54.09599 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3010a9e-d98a-3969-9972-71447540abd1 | -15.49891 | -50.44859 | 2025-10-24 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ed41deb-60a4-3b2f-ac46-c11a88d4304e | -12.29158 | -47.46058 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78528144-49bb-355c-9359-6cbbb98f1313 | -15.1364 | -47.93586 | 2025-10-24 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 155b962e-e3e7-38f6-bbce-4a6e32d1519d | -17.59539 | -46.62877 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| debf0fb2-2866-3d2c-a4c5-1fd00fb3be37 | -11.99107 | -43.32554 | 2025-10-24 04:40:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b668040-8827-3bbb-a870-79c134d912b2 | -13.33432 | -47.96398 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ead869b-b4ef-3829-8da8-4fc602496d04 | -10.66492 | -54.31079 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9789c36c-41de-3445-84f9-b99f45816854 | -12.81409 | -50.96404 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 450032e4-b417-39d0-9d5c-d45e48fc633c | -13.20988 | -47.73389 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4346e70-7041-355c-8c3e-26a327b3004f | -16.48043 | -46.47602 | 2025-10-24 04:40:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04dd7251-71ad-3e95-a220-f05b97a5427e | -14.51593 | -48.35209 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b79b062a-28df-319b-aa3b-0ec396d29e74 | -17.09445 | -46.1887 | 2025-10-24 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 331d6ae4-6910-3ac9-a4a0-a18e152fdbd4 | -14.43204 | -50.95767 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c6cc65b8-e744-3afb-a0e0-d8ac6fe0877a | -10.43243 | -55.64008 | 2025-10-24 04:40:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8df4cf13-cbb2-30b8-8742-27d9f52af8f2 | -12.25453 | -47.45183 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e383e030-445e-3ccf-a77c-6d1a5ba0ee00 | -13.04332 | -47.21304 | 2025-10-24 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7e77913-89f3-368f-8e59-a4924abf8a76 | -11.57097 | -51.46785 | 2025-10-24 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 262390dd-ab3f-3fc7-9f97-231c64261ecd | -13.63886 | -59.785 | 2025-10-24 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2699be85-e8d1-3795-89f5-cd748264e31e | -16.87398 | -49.21297 | 2025-10-24 04:40:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 079b2725-6875-3405-8a34-889201efc59e | -15.83879 | -49.10244 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0eb959cf-324a-3c62-bb49-c7468cf2c621 | -12.79973 | -48.62899 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b45f952-9d35-3682-b54f-47ba4835b58e | -17.0991 | -46.1854 | 2025-10-24 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9b42f47-0c8e-3b4b-b47a-9012fed74068 | -14.92526 | -43.44776 | 2025-10-24 04:40:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 64d4bc59-3856-3395-b930-95c95d7d1f20 | -12.02902 | -46.53154 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d510e7d5-a905-3e18-b3c3-d4f8ff77f473 | -11.04331 | -47.90277 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb33f86d-2316-3da6-b70d-6ffe01811b35 | -17.40642 | -52.01858 | 2025-10-24 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 531c2234-811b-3320-8e53-328d57ec5aac | -11.33402 | -56.20789 | 2025-10-24 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 833cfc24-b9fb-3ba6-9112-917d25bc1238 | -12.05887 | -46.43055 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae0a4bab-c03d-3673-8734-b01a59005997 | -12.82037 | -48.63238 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6505d38-9766-3730-ba26-39e531a3d876 | -12.53599 | -49.61164 | 2025-10-24 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 857231cb-e494-3b2e-9b2a-37cc6aaa6506 | -14.27149 | -48.06757 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f2abf46-4e50-3496-bbe4-eccc4dee5369 | -13.33137 | -47.95925 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6a85f44-9a78-3e51-8112-b41e6dbb183a | -17.99983 | -51.22016 | 2025-10-24 04:40:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cdc2ba3-af3c-34e7-ac5c-b6ae7d722c1c | -13.88546 | -48.36581 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b7ce5e5-50a3-390e-a8bc-0678adbe30d0 | -13.89717 | -48.38816 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b08cdd38-a93a-399a-8102-c08266257010 | -17.03658 | -51.49848 | 2025-10-24 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe9e4253-28aa-3bbb-9885-c25abe5082fa | -11.03019 | -47.91046 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0c4f98c-c6af-3e60-a3bb-b2ddf1580a5c | -13.82607 | -48.50036 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d5fed94-ffc0-3822-893c-1d703d6ac9fc | -14.27328 | -48.13155 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README45.md)
