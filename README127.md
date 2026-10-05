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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc491956-c88a-3e01-9f63-f69e2964edd9 | -3.00618 | -57.74556 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 257801d4-0478-3c1d-b763-b81ee624d0f8 | -1.613 | -55.11409 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 1b4edb89-5c26-317e-8989-13de9d25b8ee | -2.22455 | -53.71508 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 096506a1-4b48-3fcc-b96e-289831c91569 | -3.6323 | -59.3226 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e91253c-b1c4-315e-bdc5-a7441af113b3 | 1.90947 | -55.71798 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2492ab35-f521-3ec3-ab26-e925cef47e85 | -2.04399 | -54.30494 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f7e181d1-35d5-3c42-acbc-f63cc918e159 | 1.849 | -55.80328 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3fe1e21d-0fcc-3864-adf3-582cff501409 | -1.63403 | -55.53428 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 24adf242-fc1f-34db-9881-c329d1446bc5 | -3.35358 | -58.29099 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 5325846d-9153-3a4f-8fd2-e4af27807c1f | -3.68074 | -60.54636 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bce1da72-87c2-37fd-ba70-416a65e08f63 | -1.9731 | -55.67502 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 03d490d5-8b86-3aba-b8f2-0235140fbd8a | -2.93837 | -58.32214 | 2026-10-05 17:17:00 | NPP-375 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a7af8db6-a471-3bda-aac3-79f07854a446 | -2.9219 | -53.9466 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 1b302d0d-b2d4-3e61-a7d8-72e5fd49d22c | 0.44343 | -60.53719 | 2026-10-05 17:17:00 | NPP-375 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 7e750999-66a6-3eb4-b9c3-b07fc07899ce | -3.66882 | -64.23083 | 2026-10-05 17:17:00 | NPP-375 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c7074f72-4268-322f-bbfd-7293610a7dbb | -1.61912 | -55.10963 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b6bff227-9b58-30da-899c-94a25c448168 | 1.83747 | -55.81212 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9e5cab20-c20f-3616-babf-291e04e00445 | -3.51097 | -58.44091 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9c693b92-2acc-3673-85d1-5d13d401593b | -1.68835 | -55.67588 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d5681b9-c0c5-3fdf-abd0-37304f0ae562 | -2.84022 | -54.07311 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fbb857d8-b39a-33fc-8e03-938303b679ef | -3.67369 | -59.67593 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9cc7d7a1-8017-33c6-bd10-7c715ee9f0ff | -2.09584 | -48.8419 | 2026-10-05 17:17:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 8a6adc6e-37ee-3489-8f33-859bada85037 | 1.8637 | -55.77376 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7a1d29fa-5392-3a0f-b60d-787668e99592 | -1.35709 | -55.98057 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| be83736e-b9ae-30e7-9ab7-8ef93996f819 | -2.9338 | -54.12952 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 05ca3910-67b7-3ee2-b921-4b5a8318f977 | 1.45929 | -55.65354 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 27e94d70-ada2-3a6a-a446-660411e6f062 | -1.17556 | -49.24553 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 33f363c5-408f-36cc-9b6d-60f69e85dbdf | -1.21748 | -54.53775 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 159746ed-da7f-3968-89d6-447b7bc46992 | 1.86807 | -55.76738 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce1c66ca-8c27-3427-ae28-aeeb9e6ca5a2 | -1.42364 | -55.09057 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fedb54da-bc39-3c6f-b5ac-2fe18eadba07 | -1.51326 | -54.81252 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3ba3d9fe-2324-3061-9d28-793df9ee64b1 | 1.73617 | -55.6132 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd8d5715-f66a-3123-a398-9b9cedb0c954 | -2.93048 | -54.13002 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| e25ffd62-5919-36e3-afd5-306275ad6809 | -0.73625 | -57.97958 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3bd491c3-aaf1-382f-bf0e-7fdbbd3236e2 | -3.18395 | -60.05118 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bdc998eb-80d2-37e3-b768-b273663c5fa5 | -1.73852 | -56.07479 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c1fc6292-dff6-334d-bdfd-3be51543cb3d | -1.60028 | -47.42232 | 2026-10-05 17:17:00 | NPP-375 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 11870fd3-8fd6-303c-b437-f9a5aca1fd79 | -3.07728 | -58.4256 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 753cb5aa-8bcb-351d-9732-5a6db1e09e25 | 0.69983 | -51.43178 | 2026-10-05 17:17:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 072acd4d-8f5e-3cc5-acba-fb848c8bc5b1 | -1.32803 | -55.28271 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6d833bdb-3366-3d3d-a40e-9fd56da1f523 | -2.56143 | -54.72484 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6edebd55-4dd8-3dcc-9b1e-0023b6c46f3c | -3.43308 | -59.62283 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6d300695-e315-3bbd-8fe7-58d8ea084e2d | -3.70657 | -59.6863 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00ea806c-63de-3deb-8f01-890ebf7691bf | -3.53505 | -59.39574 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 242ca70f-2c99-3f08-afa4-06c285e95191 | -1.19111 | -49.26276 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| f4e1fddd-d87d-3923-a0eb-757b03a8bd02 | -3.53663 | -59.40657 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4100a4c5-b3ab-3a1c-bcd3-0aa97843f044 | -2.06116 | -56.88286 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 967bd976-f92e-3ba5-b149-42d62b7734de | 1.88118 | -55.74821 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72f0c332-89c8-3ca9-b719-df95421089e3 | -2.93607 | -54.12211 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 813d0ca4-8fe4-34bf-904e-825409d2e9e3 | 1.51425 | -55.64853 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0abe381e-29e7-3b68-aa39-6bcc4dda1f56 | -3.64461 | -60.92146 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1933b38f-ca9f-365e-9e3e-790281fbcbbb | -3.6334 | -58.9422 | 2026-10-05 17:17:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 104aa290-b003-3077-a01c-a740f2ee2a2e | -2.87856 | -54.12376 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 983837d4-93ae-341d-83f5-a270aa290346 | -3.10303 | -60.19965 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 647df92c-2204-3c6b-94b7-7c5dc525285c | -1.63542 | -55.14959 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9279b691-aac6-35e3-bb18-78eca5b8039d | 0.31228 | -50.99475 | 2026-10-05 17:17:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5b20bbd5-62db-3795-86c5-0395f7391e48 | -2.95201 | -54.16471 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d9379968-fb27-3e87-a7b8-1629b3d3d189 | -2.09323 | -56.61922 | 2026-10-05 17:17:00 | NPP-375 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 73e5ea1c-0f87-3bee-adbf-f0b18dbc140b | -0.68616 | -57.99501 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b40d6b99-b42b-3f86-aaa2-e96b3a420c16 | -3.85274 | -61.39208 | 2026-10-05 17:17:00 | NPP-375 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 7dd80605-442d-3016-9ca5-752379af0585 | 1.8539 | -55.79345 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 397542a1-4933-355a-b838-925f97d6e4f2 | -3.13364 | -59.0178 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aa6482f5-cc74-3fee-bbff-d3016a318122 | -1.12287 | -54.12048 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c25033d9-088c-350b-8899-fd9e31ccd695 | -3.7279 | -60.56775 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 1907a300-43e3-357c-9bbe-8f4d3e520aae | -3.70246 | -59.62943 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c1db1c53-b81a-3938-a1e1-f0fa24a0c7e4 | -3.65337 | -59.15742 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d9934ca7-d9ee-3594-aa2c-843e94bc1d73 | -4.32274 | -63.44205 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4d236d83-d163-3a1a-b073-0474dcd061b4 | -2.96678 | -54.10595 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| fbbc63e0-4304-3887-bf05-f9f6280a3924 | -1.37756 | -55.18937 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 272af1a7-4dba-34de-bdeb-e07c0a7da804 | -3.62771 | -59.31963 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 303b2c4b-39e1-35c9-811a-847f16d8867e | -3.47631 | -59.5562 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 60a7ce6b-4323-30b5-aaf7-59c881834d2a | -1.33083 | -55.27876 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 2b6d90c3-6d45-3f17-87b1-8527a9e18a6f | -1.49228 | -55.67381 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7dc4b5fe-83c5-371a-9828-efc4cf9a5d28 | 1.85285 | -55.80034 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b59db65a-4abb-3f3f-a0e2-a27ff79bfe47 | 1.84953 | -55.79984 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1775a33e-ca92-3e26-8903-65cfa60695d7 | -1.42564 | -55.34859 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b886e397-66dd-30ae-8d6d-d8e910ec2edc | 1.45598 | -55.65304 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5d4e4247-1873-337a-a0b7-807d6addb1ba | 2.35031 | -50.75284 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5bc9738-15d5-3542-9853-fe384bf2f8ea | -3.71964 | -59.68823 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c215cb66-cde7-3e83-9d23-0fc42de4894c | 1.91715 | -55.7121 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d9c1ca8-9883-3ba1-8158-ae5eeb0ed1a9 | 2.08717 | -50.73353 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ea19c0e0-8c15-3b35-91f4-fdb902f63b8b | -3.75091 | -59.28638 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c2a5af32-9838-34b7-a1e0-ef02ade1157a | -2.55707 | -65.87396 | 2026-10-05 17:17:00 | NPP-375 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 420b11d4-cae8-377e-a137-a4ec80252d14 | -3.00984 | -57.74501 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a64da0ec-b702-3778-ae37-e0f104afe538 | -3.62777 | -58.61419 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 78114ed5-aeef-3102-860a-5d33dd9900f0 | -3.67632 | -60.54698 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a9dd3b92-c24b-30f9-872c-be51f10beab3 | 1.47324 | -55.67327 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ff9789b7-9e2e-334c-be2c-0ddab1af55c2 | -3.18313 | -60.05251 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c3947de6-c423-3609-bb67-5e5bc43499b6 | -1.80676 | -53.75545 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| f6c48238-c2e3-383d-a002-d0457eded4d4 | -2.06048 | -56.8712 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c0c67065-2c8d-32ee-b3e0-7d60e25c9840 | -3.25719 | -59.55924 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c8273203-ad3b-3c15-9774-b70684985ad9 | -0.83717 | -48.62813 | 2026-10-05 17:17:00 | NPP-375 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 18e1abef-543c-3009-b8c3-8e860d282430 | -4.28463 | -63.41293 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| f7cdaec5-ec9b-3c39-9762-ed6098199616 | -3.62792 | -58.93265 | 2026-10-05 17:17:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 366c2052-77a7-3c7d-8aee-66173f16b4ff | -3.62125 | -64.34476 | 2026-10-05 17:17:00 | NPP-375 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| a16276c8-b262-3a7b-8eed-891caa7341a6 | -2.97674 | -54.10444 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c244b508-2323-385e-a6cd-a53ff6bce4a0 | -2.06347 | -56.87473 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e51e98b0-a5a0-3c83-aa80-e61ea3735c72 | 3.48163 | -51.49648 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1def405b-3a82-35d1-b19e-164237437c31 | -2.92966 | -54.169 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c71fbfd-9f41-3895-88ce-d8383c8f4f30 | 0.82279 | -51.96038 | 2026-10-05 17:17:00 | NPP-375 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README128.md)
