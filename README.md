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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a3fc539-b12d-3efb-b902-2b396bccddfc | -7.3397 | -49.6454 | 2025-07-05 00:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| f9a888cc-4c5f-3655-9013-fffda8495feb | -7.3584 | -49.644 | 2025-07-05 00:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 27a78e7a-d8b7-3fda-b745-5e4ad9a20b7f | -7.3399 | -49.6241 | 2025-07-05 00:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| bf198fc3-0a8e-3383-9c0d-b0e4e560b5b3 | -10.5983 | -46.4347 | 2025-07-05 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| c5135cd2-6991-3a6a-9bc3-a7e23c313142 | -7.2405 | -43.0899 | 2025-07-05 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| d355458d-d1bb-358e-a272-2cb055ada86e | -10.6177 | -46.4098 | 2025-07-05 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 33536452-6248-35e9-af80-6709681612be | -10.5987 | -46.4121 | 2025-07-05 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 2f2dce9c-da05-3f3b-9540-084425fdca4c | -7.2594 | -43.0881 | 2025-07-05 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 6ca9a9ac-5c3d-3619-b938-b27f68e3cada | -10.5586 | -49.1337 | 2025-07-05 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 08b1631f-7115-303c-8973-d51745df21c6 | -10.5776 | -49.1316 | 2025-07-05 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| abb96280-b0aa-3c82-8f0d-0a61437b1f4f | -7.3586 | -49.6227 | 2025-07-05 00:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a8836579-8011-3222-8a99-a8458eb1aa7b | -7.2594 | -43.0881 | 2025-07-05 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| e4319a87-184b-3986-a5b2-652d319d0d35 | -7.3397 | -49.6454 | 2025-07-05 00:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a0e7f749-1890-3ae2-a4cb-44413fd9d39d | -7.3399 | -49.6241 | 2025-07-05 00:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ef3ce9ae-8686-34a9-b5ef-b8156930863b | -7.2405 | -43.0899 | 2025-07-05 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| f04a8bda-c62d-3fc0-97f1-38fe3c9322dc | -10.5586 | -49.1337 | 2025-07-05 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| d4da6d1f-59fb-3d38-b234-494254dcae7d | -10.5776 | -49.1316 | 2025-07-05 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 10e79490-e3f5-3999-be88-5601377be343 | -12.7576 | -44.402 | 2025-07-05 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 68150d47-7e09-3f43-824d-8f5c627461f1 | -10.5586 | -49.1337 | 2025-07-05 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| dd699c53-3259-38f4-9670-50b8d03e1f27 | -7.2594 | -43.0881 | 2025-07-05 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| 5bea5ac9-e203-39cf-816c-4af96d1db94b | -7.2405 | -43.0899 | 2025-07-05 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 20a547c0-e037-307c-a52c-c5c3439233a8 | -7.3397 | -49.6454 | 2025-07-05 00:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ffa2052b-8ec4-3f39-aa50-df4d6e4968a9 | -19.25793 | -44.43213 | 2025-07-05 00:39:00 | TERRA_M-M | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6c94e2cf-609b-33c4-9ee3-c85f5b1372f8 | -18.84637 | -47.49257 | 2025-07-05 00:39:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f3736a91-f2a5-36b4-abc1-781fb336745e | -21.4284 | -48.64533 | 2025-07-05 00:39:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 127f0847-2d85-3c59-860a-17d8f6b2c9ca | -18.85522 | -47.4912 | 2025-07-05 00:39:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| df4477dc-1d0c-3b67-8498-cbd5f27abf88 | -21.2102 | -48.66873 | 2025-07-05 00:39:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 8daf96ce-4206-3949-aed3-8fb4bdb8e4a4 | -21.20624 | -48.63797 | 2025-07-05 00:39:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| f1f0e2d9-5ced-3fea-8f17-a85d8d5a3458 | -18.84509 | -47.48327 | 2025-07-05 00:39:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c2724eeb-11d3-3ce2-b013-2517af30003f | -21.21544 | -48.63665 | 2025-07-05 00:39:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| fbc1783b-356f-3d56-8b6f-e24709a18c8e | -10.5586 | -49.1337 | 2025-07-05 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 40101277-7f76-3cf9-aed1-496f65ac7107 | -7.2405 | -43.0899 | 2025-07-05 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| d94af49d-8d23-3e01-acd7-6c15d3bb2d09 | -10.5589 | -49.1119 | 2025-07-05 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 1284e660-47a7-30d7-bd67-58289e8809a0 | -11.94077 | -48.4276 | 2025-07-05 00:41:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 68fe619a-bf5e-37ed-b624-1b11899d72e7 | -11.44822 | -45.10827 | 2025-07-05 00:41:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b422e43b-bb6e-3db2-8714-53387de547f8 | -10.64035 | -46.39547 | 2025-07-05 00:41:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 20b84513-ad28-357d-a6c1-7a3378f095ce | -10.61727 | -46.39372 | 2025-07-05 00:41:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e50a28f7-9605-38a1-ba07-115c1555ea5b | -18.46196 | -51.24352 | 2025-07-05 00:41:00 | TERRA_M-M | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7b90b752-c39b-3bb1-b315-0cf1b4f09f09 | -11.4398 | -45.12268 | 2025-07-05 00:41:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 040211ca-eb32-30f4-b3e1-94fa9c59bea2 | -18.33572 | -52.04869 | 2025-07-05 00:41:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| f176b265-217b-3c88-8066-5282d08581b4 | -10.36904 | -46.98771 | 2025-07-05 00:41:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| de7e490f-cb5c-3bd4-9f77-7b46ce26d60a | -10.57377 | -49.12911 | 2025-07-05 00:41:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d01542aa-6d85-3acd-a056-8c9968a8f454 | -10.56618 | -49.13933 | 2025-07-05 00:41:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6821c383-6270-3b8a-a4d8-0826da168644 | -15.92316 | -43.51653 | 2025-07-05 00:41:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| df1f86a2-5727-3a0b-b074-976a877c449b | -12.42793 | -50.03471 | 2025-07-05 00:41:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 8efe77db-206d-38e5-a48a-68e19e2956cb | -10.57501 | -49.13804 | 2025-07-05 00:41:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7aba5a33-1d96-384c-bb6b-eecf86509de3 | -10.65003 | -46.394 | 2025-07-05 00:41:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 647cf94a-f4dc-3b2a-a9dd-98c5c4eb81ee | -11.87089 | -44.86206 | 2025-07-05 00:41:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 959ef00d-796e-30c9-8a24-24432078fa8c | -10.82905 | -49.71091 | 2025-07-05 00:41:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ec58a06f-aed0-3635-ac94-0f9f91d5da57 | -11.10444 | -48.90557 | 2025-07-05 00:41:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e63dd454-cbde-3553-a86c-983e4455c867 | -18.45338 | -51.23732 | 2025-07-05 00:41:00 | TERRA_M-M | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ddf35ecb-cdb3-3025-b9f5-e10f5f5607d7 | -11.52512 | -48.95677 | 2025-07-05 00:41:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7dadf1af-983e-3f06-bb42-46a136275142 | -10.5637 | -49.12146 | 2025-07-05 00:41:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 95a4e754-bf89-3d4f-b2aa-bae8671f11c7 | -11.87298 | -44.87535 | 2025-07-05 00:41:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3bec0e5c-b2aa-3a2f-8b74-8ed60a726e93 | -12.01089 | -47.75741 | 2025-07-05 00:41:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d71bbdd9-7b18-3e39-949d-6b44a38466d7 | -12.01352 | -47.77601 | 2025-07-05 00:41:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 967ff618-b615-3166-ab14-b0880b24e0e0 | -16.29678 | -45.10797 | 2025-07-05 00:41:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e3ade36e-f461-31d2-81dc-ff57fb150237 | -10.37053 | -46.99785 | 2025-07-05 00:41:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 5c5a69b7-f9f6-3a46-bb46-82af02968844 | -16.29509 | -45.09684 | 2025-07-05 00:41:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 35304ad3-e90a-302b-a354-8a8ef02a9621 | -11.33508 | -51.44488 | 2025-07-05 00:41:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6bf48f8d-df21-3b90-a6dc-5a12d48361db | -10.56494 | -49.13039 | 2025-07-05 00:41:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 06e6b2d4-72ba-342f-94ff-9c08ea65abad | -13.65304 | -46.80927 | 2025-07-05 00:41:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 76e1d39c-7571-3935-b595-322afce85404 | -11.44242 | -45.11543 | 2025-07-05 00:41:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| ccef1227-93bf-3dcf-85d1-ab8b3ef9108d | -12.34018 | -49.31587 | 2025-07-05 00:41:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4eba1087-6c22-3ebf-a27d-4476e5ae9499 | -12.43696 | -50.03344 | 2025-07-05 00:41:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 824c04d3-184a-3667-b1a7-c76ceeff0f4c | -12.75507 | -44.41021 | 2025-07-05 00:41:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| d9d8e5b5-3b44-3226-b72b-ac98209853ef | -14.66717 | -45.37645 | 2025-07-05 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bd06ffef-87f3-312a-b1d2-7ff0dbc6f650 | -10.83028 | -49.71994 | 2025-07-05 00:41:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8c7dbc6a-5f29-3b44-a7fc-5c9e7cf82149 | -18.0336 | -46.05444 | 2025-07-05 00:41:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 494b66d9-02d3-3056-adb1-3bdc9112eec0 | -12.0122 | -47.76671 | 2025-07-05 00:41:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 9742b586-b7cf-3a1c-a811-7d079637d4e7 | -12.75721 | -44.42384 | 2025-07-05 00:41:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 536e7519-8c03-3f5d-8921-081569db5d47 | -11.4502 | -45.12099 | 2025-07-05 00:41:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6582e2c8-0c13-304f-828b-1d2f980e4fb0 | -11.43781 | -45.10995 | 2025-07-05 00:41:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| ffaccabc-4937-3c20-9d86-d5359079949c | -7.24904 | -43.09695 | 2025-07-05 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 6305e498-ff9f-37b8-b7e8-d61f63b9e3c5 | -7.19286 | -45.31945 | 2025-07-05 00:43:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 33de12d6-46f9-3034-b2a4-f68e81a8e616 | -4.39157 | -48.94317 | 2025-07-05 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5b859321-9286-3ff1-9e55-efa7f3335576 | -10.5561 | -49.13168 | 2025-07-05 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 53416785-3e42-3208-b96d-f364e827db2b | -5.72238 | -49.10097 | 2025-07-05 00:43:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 438c0957-8beb-3e03-8811-763b3996fa1b | -6.84445 | -42.79763 | 2025-07-05 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 7469221f-9291-3dca-89f5-1b9bf4071f65 | -9.0005 | -47.45705 | 2025-07-05 00:43:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7a75e0e1-3561-35e2-bf80-684c34d81ca6 | -8.90559 | -48.01838 | 2025-07-05 00:43:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 26cacf9c-78ff-362e-8a49-020a8e4248e7 | -7.89935 | -55.41893 | 2025-07-05 00:43:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 9bdb4f1a-d6f6-3166-8218-221288c44e92 | -9.57494 | -49.10469 | 2025-07-05 00:43:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1d01dc14-fa0e-3435-bed2-2bd1e784c9ee | -8.99907 | -47.44706 | 2025-07-05 00:43:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 9b71872d-f728-3237-8a0f-facb8fa5b438 | -7.24554 | -43.09074 | 2025-07-05 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 11557d42-e46a-3015-a09b-e5b15884baee | -9.96177 | -48.57747 | 2025-07-05 00:43:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 049b82ee-a1e3-3c4f-b82c-4c196420e41f | -5.60762 | -45.17856 | 2025-07-05 00:43:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| eb758d59-073a-3101-b2d2-8e0e6431c24a | -5.06294 | -43.73612 | 2025-07-05 00:43:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| d7ee4833-0d30-396d-93c7-10c756196164 | -4.11449 | -47.94363 | 2025-07-05 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 02f9c44e-6772-3633-8b19-da5d16fcbcbd | -7.30356 | -45.36833 | 2025-07-05 00:43:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 74da3af1-b804-3549-9d02-eb55dea57149 | -10.36012 | -48.72477 | 2025-07-05 00:43:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 6a225994-3d7a-3f2d-9206-16973b1be46e | -8.80689 | -45.97999 | 2025-07-05 00:43:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 969d1ac3-1969-3928-b01d-99f174ac51d3 | -5.06544 | -43.74155 | 2025-07-05 00:43:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 9749ae6f-6bec-309d-a38d-bdb06d54e609 | -4.28513 | -48.19213 | 2025-07-05 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d5de8997-944e-3ab5-aaa5-328dc322e27e | -9.61906 | -49.01908 | 2025-07-05 00:43:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a80af139-3d1c-3447-8aab-992e82e1031c | -7.23586 | -43.09907 | 2025-07-05 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 21e24a28-194e-3929-8e80-61861bacf2aa | -7.34648 | -49.64179 | 2025-07-05 00:43:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 879a39ea-7093-3f5e-8676-3de3699373d0 | -7.24579 | -43.0757 | 2025-07-05 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| a54dc9e4-a263-3057-a88e-a4417e6f9bab | -8.01138 | -49.72106 | 2025-07-05 00:43:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 691bc4d1-d10a-3b8a-a1a7-4429de1c30c2 | -4.1159 | -47.92618 | 2025-07-05 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README2.md)
