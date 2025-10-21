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
| 3719ea59-9104-3654-a81a-e2d39803af4b | -6.70048 | -43.40688 | 2025-10-21 04:44:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e9cf278-405d-3360-85c1-be593a759d53 | -3.44097 | -51.61622 | 2025-10-21 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2ffd3cf-0d6f-3a97-a0c4-86cbd604700a | -6.90506 | -43.58944 | 2025-10-21 04:44:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 361c908d-3350-3723-a73a-9b8756f6d53a | -4.29931 | -49.65937 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 881e3a4c-4b53-3920-8957-4148375f9dc6 | -3.21865 | -50.21704 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f03f5f55-2c93-3474-9e53-1b80694df530 | -3.14903 | -50.16051 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b01ed603-4433-354e-bb51-83b241579236 | -3.14129 | -50.44705 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36e5abe2-f2b0-3f05-8f84-b395ca55e030 | -3.97347 | -48.06071 | 2025-10-21 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8b9d5f2-5ff3-3426-a847-2060c3f38ac1 | -2.8683 | -50.73479 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbaefc87-8629-34ec-8cb4-c8240b7ff06a | -2.9078 | -48.98156 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71101725-b7a3-33ed-9978-3a3cddb59985 | -2.16773 | -53.48527 | 2025-10-21 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13cb6029-16dc-3013-882e-c513b64010d2 | -2.10253 | -50.58281 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d0a83c7-c484-322d-a9d0-16305de04856 | -4.55158 | -49.65593 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6021b0e3-51e7-36cd-a541-4bbc8ecd3e0c | 1.70589 | -55.72446 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4364f463-a414-361d-b76d-0f2565af21ba | -3.49769 | -45.81996 | 2025-10-21 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7df7bbb2-72f1-34ce-8c2d-ac56122dd933 | -2.93235 | -48.30408 | 2025-10-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 39611f72-da03-37ae-8662-651029ee53b0 | -2.87154 | -50.71412 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1084927-d005-3cac-a128-c627d2efe212 | -4.65712 | -50.74652 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12264668-0ae1-3a23-88b0-086c17c3ad16 | -3.25031 | -48.76853 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b397ddcf-19e1-3828-a1d2-3e3d577ba73f | -3.06535 | -45.04576 | 2025-10-21 04:44:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6abaa17f-bb18-3bcb-9416-c18d33201262 | 1.71797 | -55.71354 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9bfd22a-7b93-3de2-ad26-124a5cb9a987 | -4.4743 | -49.09856 | 2025-10-21 04:44:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8f94720-36ad-3701-ab57-bf01a9eea0fa | -2.79968 | -48.8885 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ab4dc6b-fe2a-3a36-9162-0c65086af9b0 | -2.18755 | -54.47451 | 2025-10-21 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b823b9c-706c-3585-85b9-4e5e930a124c | -4.3427 | -56.06357 | 2025-10-21 04:44:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 049c03ab-693b-384e-963c-48ea3db0f1f9 | -4.49107 | -46.4744 | 2025-10-21 04:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7e50ecb-cbf9-36ce-8550-bbce0ca525f9 | -2.20586 | -56.89025 | 2025-10-21 04:44:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b2c71d0-bb13-3123-96ec-72440f9c4a82 | -2.86776 | -50.73824 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e87f3d7e-12e8-3f9e-a946-fbff20b1b15b | -2.26159 | -47.8769 | 2025-10-21 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6224ce9a-827e-3d92-9241-ab9d7f66ddcd | -3.61517 | -52.28821 | 2025-10-21 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 264c6d19-f10f-3b2f-976a-04b41eddba2f | -2.22729 | -48.36937 | 2025-10-21 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9e69579d-07d8-366f-a8e3-5e1e70ddc474 | -5.94504 | -49.44032 | 2025-10-21 04:44:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b504556-f879-34fb-810d-2d64e7478dbc | -3.59295 | -43.04518 | 2025-10-21 04:44:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d765968-ac1f-37bd-b071-a7ea03e8abe6 | -2.86337 | -50.74463 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 769f881c-ee97-3111-a985-1b777b34f4d0 | -3.33692 | -53.22991 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d63f56d-1443-342e-8005-65ee7fb73f3c | -3.1409 | -44.43384 | 2025-10-21 04:44:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d92e202-9582-3d97-b5bc-74b8559c10de | -2.72004 | -48.34311 | 2025-10-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0e091dc-9915-3908-b7cb-815f01968364 | -3.84382 | -51.67202 | 2025-10-21 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9fa579a-56ee-3636-a921-c35cc9a06079 | -2.25202 | -51.91161 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 123e5685-2028-3cd8-8988-fc2e539d8baf | -5.52748 | -50.05386 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fc70a0a-5a25-3295-8c35-35de0e724f5b | -7.01987 | -46.43322 | 2025-10-21 04:44:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 414d3660-e45e-3c5f-9052-e63b455452d4 | 1.69886 | -55.72809 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f3b3cdb-a6b5-3f64-9a60-a72959d43610 | -3.66448 | -51.95154 | 2025-10-21 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 200d4386-6001-35a4-be3e-b61d1288b2ed | -4.3925 | -49.75978 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b76d3131-4727-3713-8dc2-13c7d2ec96b9 | -2.85784 | -50.7367 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bae7990-950b-39d7-a785-65f2fd65a914 | -2.85038 | -49.54727 | 2025-10-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c09b2bb-e2ad-3a1e-a17a-9f3b55239fc6 | -3.52128 | -52.89545 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44b43304-cb3a-3193-8b77-d7cdeb311ed1 | -6.6479 | -43.43224 | 2025-10-21 04:44:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b99e012-ac74-368f-907c-8c333870d58c | 1.67929 | -55.74937 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a823f935-5a68-3825-840c-b6558db40bbf | -5.22339 | -49.60214 | 2025-10-21 04:44:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f7d18d1-59aa-311b-9bba-bd52a4161bde | -4.33897 | -42.56188 | 2025-10-21 04:44:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 179b7c28-cfa9-3ac7-8ce6-749c68ba6bc9 | -4.65396 | -50.6159 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33b628b6-b25d-3ea6-926c-665b67a986b9 | 1.70454 | -55.71542 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2729bf0d-1279-3044-8179-18e36d9b4e20 | -3.39975 | -54.0637 | 2025-10-21 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 658ff164-2e7b-34ac-957c-bdac3ccb879c | -6.23892 | -47.31855 | 2025-10-21 04:44:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5218b0d-62de-32e9-ab8a-6907c05bb47b | -3.21723 | -50.59254 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56d31ff8-6934-3822-81a1-75f04c3a26c9 | -4.16159 | -44.55259 | 2025-10-21 04:44:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e0d96bf-72ce-3667-b2ab-dd598abe6317 | -4.93344 | -48.29955 | 2025-10-21 04:44:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 800d7855-1f20-3d8e-99f6-63d7dcb2c2fc | -2.7172 | -48.33893 | 2025-10-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d455bbd-0dbc-38f6-92f8-c967141c6555 | -2.7206 | -48.33945 | 2025-10-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93ddbed5-5574-3983-bce0-f2de40a02296 | -7.20798 | -45.31346 | 2025-10-21 04:44:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d2fedb2-eb63-3631-a627-b8e4ea1dcb22 | -6.24196 | -47.31697 | 2025-10-21 04:44:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d220086-e551-3142-a179-7db0207bda94 | -6.46589 | -43.85557 | 2025-10-21 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 533e6e69-79f0-38de-95b8-2df770521fea | -3.39784 | -52.59641 | 2025-10-21 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52b2c7f5-477c-3848-8bd1-e0abb480f1d6 | -6.58331 | -47.54068 | 2025-10-21 04:44:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 42cf60a1-f8d0-3d52-9507-61c8fe37c812 | -8.07394 | -41.07424 | 2025-10-21 04:44:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 205f5024-c745-37a5-9103-b83c5250d77a | -2.85838 | -50.73325 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 312c855f-578a-3cb3-b098-569251b3599e | -3.29929 | -43.49909 | 2025-10-21 04:44:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dbe64dc-2edd-3792-83c9-0e9ef00e111e | -2.87046 | -50.721 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43ac3bae-2e85-302c-8dcf-632111eceea6 | -5.24375 | -50.14791 | 2025-10-21 04:44:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5828cbaa-e259-3b7e-a4c9-d34e90a62bfa | -2.55514 | -47.65973 | 2025-10-21 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b26785b6-528c-3d5f-b0fc-a735f90438b4 | -4.00783 | -46.96499 | 2025-10-21 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cf4d38b-8d3b-3e92-b959-88c4644b3183 | -6.70036 | -43.4072 | 2025-10-21 04:44:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2c7c649-ad20-30ce-85d9-dc9be642dd31 | -4.5549 | -49.65643 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 672fa03c-b50a-3149-8601-0eb1ecc48899 | -5.45141 | -50.03873 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aadec75-3fda-32d1-b773-f352af16fe87 | -2.45076 | -47.18731 | 2025-10-21 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bb75ff7-e3fa-332a-905d-3a2247ee0e35 | -1.62711 | -47.05104 | 2025-10-21 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 216d04ac-7516-3b3b-853f-88b90cbb4e9b | -3.12289 | -45.27203 | 2025-10-21 04:44:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 40.8 |
| d2310a6a-d7d8-3d12-903d-6488a7af6409 | -4.35964 | -49.68706 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb207636-d4cf-3a29-b533-1f58b0e3a856 | -3.50547 | -45.82115 | 2025-10-21 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e0e6f742-30b5-3455-a8b8-4e5467b4f49f | -4.65384 | -50.74597 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b545b956-1d5d-35fd-a735-adf2e8738033 | -3.1159 | -51.28278 | 2025-10-21 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8478a842-4934-3abe-a49e-2677756d2888 | -3.08801 | -49.50659 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8eb7f85-1e0a-31de-a94f-f2d88df05fd3 | -2.86007 | -50.74411 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c04946f-e5a8-3bdc-b644-129727c4e107 | 1.7135 | -55.71421 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15df91ad-fed1-369a-9bd1-484c92e13d4c | -2.86668 | -50.74513 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c03adce-0ba2-3199-8baf-c395d0cabbac | -5.66964 | -49.79403 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d5f4c9e-dbb3-3c5b-a00b-15f7cc4b35d3 | -2.871 | -50.71756 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae2e6861-8ff4-3e01-bca4-839de4addce8 | -2.87239 | -45.25141 | 2025-10-21 04:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34852d5a-313c-3147-8263-9f3a806e83cf | -3.21484 | -51.69008 | 2025-10-21 04:44:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| def6dff4-012f-30e8-a033-905d33b80498 | -3.33008 | -50.74458 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c906c53b-d34c-31b7-8917-9ba9c7b2c4ff | -4.88972 | -48.97014 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ac68c421-b025-3b17-ba19-f5c6a4e3c5da | -5.2909 | -50.56513 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e51a235-1cce-3303-b43b-0ca97c6aba6e | -5.30953 | -49.57204 | 2025-10-21 04:44:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 745d905f-178c-3755-bf65-f70dff67d92d | -2.72345 | -48.83337 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48da27a3-5243-3dd7-87cf-ddbeb3b76afa | -2.86445 | -50.73772 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0779eb6e-fd84-37a8-9520-3e386c631f46 | -3.59988 | -48.98993 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c11431da-b688-385e-8bc1-aed91f911bfa | -3.04071 | -49.43831 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bfe57562-8ccd-3bc5-afa8-8bf055d35624 | -2.92895 | -48.30355 | 2025-10-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| a290d918-b136-37d0-866c-85e054e7e0ff | -2.81047 | -48.66415 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README13.md)
