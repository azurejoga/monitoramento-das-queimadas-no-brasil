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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71dc8e91-0981-386a-88dd-c5a00ee932b4 | -7.63059 | -46.21894 | 2025-08-20 05:59:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fefd58d8-58d7-3321-9a4b-51bc4b7525c5 | -5.97813 | -44.14596 | 2025-08-20 05:59:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| e6d2df8c-d4e0-36fd-a05b-b22ff03511c1 | -7.58421 | -44.39128 | 2025-08-20 05:59:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| fe96d96e-7b80-305f-a4fd-c0db94bae721 | -13.1558 | -54.9151 | 2025-08-20 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 82cf0047-9d2a-351b-8390-ff5a6cf47b57 | -20.339 | -51.7062 | 2025-08-20 06:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 8eb9195b-680b-32e1-8e1e-e76cc9522e43 | -13.3346 | -54.4233 | 2025-08-20 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 74b65174-dd1a-323d-8931-723e02f3b099 | -13.1364 | -54.9376 | 2025-08-20 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 9267c29e-78c0-3f65-957a-59cc314bdfde | -13.1555 | -54.9357 | 2025-08-20 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| a7f6fdbf-0475-3e91-b3fb-f08cddd31ce5 | -13.1367 | -54.9171 | 2025-08-20 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| f574a9a5-9826-316b-ae0a-69ceb89f65e1 | -13.3349 | -54.4027 | 2025-08-20 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| c93ffdbb-d8b0-37d4-bc77-0204dd1933a0 | -13.57661 | -47.02242 | 2025-08-20 06:01:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| df95a324-d161-3724-83d7-3b683db830e3 | -11.74887 | -48.18512 | 2025-08-20 06:01:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 325ce555-3fb7-3cd5-be47-327f505eedf1 | -11.18597 | -48.62214 | 2025-08-20 06:01:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5888cc31-8189-3d9a-96d3-4cb800f51417 | -13.15358 | -54.91008 | 2025-08-20 06:01:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ec241965-8436-306b-9404-606b417bdc62 | -13.39951 | -46.36278 | 2025-08-20 06:01:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1dcaba56-b3c2-3a10-8e1a-3651f5452777 | -13.19355 | -46.90322 | 2025-08-20 06:01:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0e02bd3a-fa06-3def-87b8-8cede2088612 | -12.98917 | -45.19595 | 2025-08-20 06:01:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 373e3a9f-7d77-32ca-bb0b-06e0b4f6f804 | -13.02572 | -46.7859 | 2025-08-20 06:01:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8c17ba09-5214-30ae-b386-c28bc0cb3208 | -8.02123 | -47.66379 | 2025-08-20 06:01:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 8c35fb66-4ec0-35d7-ae8f-039b3c592b5d | -10.27552 | -46.76299 | 2025-08-20 06:01:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 5b7d2f51-64e8-392b-b18d-567a2d0f1c5c | -13.18835 | -46.86805 | 2025-08-20 06:01:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 070b2604-200c-3df2-a560-489f3854d3a2 | -10.82119 | -43.27811 | 2025-08-20 06:01:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 59.1 |
| eb9e7947-6367-3f9c-9ed8-1d30a4ce9ff3 | -10.27405 | -46.77327 | 2025-08-20 06:01:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| d2ddf912-b749-31de-82b4-1964b5b9ddbf | -13.13984 | -54.92332 | 2025-08-20 06:01:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| adbc3ffc-da4d-3171-920a-b216617c99ce | -13.33242 | -54.40172 | 2025-08-20 06:01:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 4f8192c3-59e0-3772-aa08-df7cc979e9d7 | -12.98825 | -45.19028 | 2025-08-20 06:01:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| de55a5a8-92ac-3706-b1b8-4e78e11aa76e | -11.12751 | -46.97845 | 2025-08-20 06:01:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7f5e579b-295e-3eb2-a89d-359f67ae1928 | -12.98627 | -45.20506 | 2025-08-20 06:01:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 2301abe4-adef-3de3-b7ef-537ac37491a7 | -13.3217 | -54.39998 | 2025-08-20 06:01:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 028b97b4-2078-3d7b-b3d1-67dd02adda9f | -10.69095 | -48.22088 | 2025-08-20 06:01:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8a371a45-adb2-3eb9-a938-1dbcfcba3834 | -10.69231 | -48.21161 | 2025-08-20 06:01:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5e2097f7-6906-3ba9-856a-10341336b9c2 | -14.89191 | -48.06816 | 2025-08-20 06:01:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| dc1eb10a-e3d6-3ddd-adc2-75ece99299a0 | -12.97302 | -56.86676 | 2025-08-20 06:01:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f0b734d1-e257-3702-a36b-022ad794bece | -8.78995 | -45.4776 | 2025-08-20 06:01:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 06dd0cfc-27f8-3e02-a3ee-8ad59f7bd4fb | -14.61178 | -54.90781 | 2025-08-20 06:01:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| cc0d6780-0333-311c-b1af-5719489b6fca | -13.57466 | -47.02694 | 2025-08-20 06:01:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e69692f4-604b-3af8-a5a9-17f2ca54c048 | -13.33013 | -54.41541 | 2025-08-20 06:01:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| c6e94c94-2015-3df6-a744-d23bc4818850 | -12.14318 | -48.01292 | 2025-08-20 06:01:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8d6606ef-931c-3b0b-94e6-d29fcf7fb599 | -8.29735 | -46.34565 | 2025-08-20 06:01:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 33f78720-dd6f-3f4d-a979-bddfc016b125 | -13.31941 | -54.41364 | 2025-08-20 06:01:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 7e950446-c367-34bc-919c-69571e8b872b | -11.18732 | -48.61301 | 2025-08-20 06:01:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8398dc6c-a404-3855-b339-e21d9972019d | -13.13728 | -54.93837 | 2025-08-20 06:01:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 43deb3ec-db5c-3927-b964-5bd460e39aa8 | -13.15102 | -54.92522 | 2025-08-20 06:01:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 9def53b9-6fd9-35b1-85a3-5533af9cdc7e | -8.01987 | -47.67296 | 2025-08-20 06:01:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d39c8c44-59cd-35f0-ae1c-5f0345ee7b2e | -13.02254 | -46.80886 | 2025-08-20 06:01:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a11cc0bc-80c8-3a84-ae27-3cba96b645fc | -14.99813 | -54.81414 | 2025-08-20 06:03:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 9bebcd25-3752-3cee-8740-c8fbfde8f9d0 | -21.74671 | -48.78631 | 2025-08-20 06:03:00 | AQUA_M-M | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5109c9b7-6a25-37e2-9712-15eea8e96a77 | -19.85843 | -49.82315 | 2025-08-20 06:03:00 | AQUA_M-M | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 8bd6e5a4-e014-361b-a193-c57591ba2b74 | -20.86817 | -50.11845 | 2025-08-20 06:03:00 | AQUA_M-M | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 215a12b2-19ff-3f58-aa3c-76d8e5134ca3 | -14.99575 | -54.82804 | 2025-08-20 06:03:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fc291675-c1fc-37d8-827a-375fbe09ad31 | -15.87123 | -50.65408 | 2025-08-20 06:03:00 | AQUA_M-M | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0c8b818b-4ac1-3d4b-b534-a9f56c42ebf2 | -19.85984 | -49.8131 | 2025-08-20 06:03:00 | AQUA_M-M | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.2 |
| f2e9ec55-2824-35d1-91c1-b074f15bec63 | -20.33919 | -51.71705 | 2025-08-20 06:03:00 | AQUA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e4727f0c-7ac4-31b6-a405-b20d50001107 | -21.00545 | -47.65344 | 2025-08-20 06:03:00 | AQUA_M-M | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| f8310442-2f09-31fd-8866-ff019847110a | -20.342 | -51.69839 | 2025-08-20 06:03:00 | AQUA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6a893766-8895-3c1a-a68c-985c4638b5f0 | -20.33179 | -51.70626 | 2025-08-20 06:03:00 | AQUA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1630eb2c-421e-3434-b79b-c935bfb38aff | -20.3406 | -51.70773 | 2025-08-20 06:03:00 | AQUA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 54.4 |
| d6c66c19-78a2-3740-9e31-7694066251cd | -20.86675 | -50.12846 | 2025-08-20 06:03:00 | AQUA_M-M | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| f5f29dcb-6323-3911-8fec-5f7f143a724a | -20.33319 | -51.69693 | 2025-08-20 06:03:00 | AQUA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| deee8207-7734-3aa3-9598-b5857496ff53 | -22.55375 | -49.77783 | 2025-08-20 06:05:00 | AQUA_M-M | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5f48870c-c5b9-3776-a96b-eda9a24624ff | -23.98792 | -48.55441 | 2025-08-20 06:05:00 | AQUA_M-M | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 44a162f7-6528-3fb4-9547-caf32bcae6e8 | -22.55522 | -49.767 | 2025-08-20 06:05:00 | AQUA_M-M | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a489f627-b982-3630-bbc7-448aef209645 | -13.3346 | -54.4233 | 2025-08-20 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 06961653-051a-336b-9882-a96da8f8375a | -13.1555 | -54.9357 | 2025-08-20 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| be9ef2dc-d84d-37de-b633-fdd4f352e4ce | -13.1364 | -54.9376 | 2025-08-20 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6d6f13bb-a60e-3c8c-abbd-2ee55a7c46dd | -13.1367 | -54.9171 | 2025-08-20 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| c78baa61-f1dd-3902-89f3-0b121a5f3c1a | -20.339 | -51.7062 | 2025-08-20 06:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c95ddd32-ee51-3ff8-919a-e9286098222e | -13.1558 | -54.9151 | 2025-08-20 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 39b4285c-4561-362e-99be-4efdc23f04ec | -10.7043 | -48.2226 | 2025-08-20 06:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 82d83d14-4b6f-3d12-bac3-f9cb66effa3b | -8.63421 | -67.26556 | 2025-08-20 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19acb4ec-049d-30f5-a9be-be6099c4a25b | -8.56755 | -66.94291 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6cbeb70-0b53-375d-b4be-acc6eda3bd51 | -9.2067 | -59.62149 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c755499-5efb-39f9-a4bb-d517b4cfabf7 | -9.18351 | -59.6351 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a802a64d-72ac-307d-b694-2420a46fb2e4 | -8.96914 | -60.50127 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d86a9820-0d87-3a60-ae4c-8809144e0df0 | -9.22841 | -60.33248 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f95dafe8-3140-3bf1-b649-3b9519bef5b8 | -8.34968 | -70.84807 | 2025-08-20 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f21c7e4d-273a-33ac-8d65-7bd40ad3640a | -7.5492 | -63.84853 | 2025-08-20 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb767e3b-1cf8-3289-adec-d0325c5f76bf | -7.78666 | -66.96377 | 2025-08-20 06:16:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cf8a642-8273-3e7d-8d6f-eabe9a845755 | -8.83344 | -71.0304 | 2025-08-20 06:16:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 733e3ce1-734f-38aa-bbff-bd451c9ba234 | -8.55792 | -66.94608 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 280c866b-bd29-3095-993f-8bbae59de3dd | -9.1903 | -59.63454 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61439a92-f770-3d27-b6d7-f7fbfd88881d | -8.30491 | -70.74417 | 2025-08-20 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a061696b-1bc7-3897-81bf-a90407385736 | -7.55469 | -63.84929 | 2025-08-20 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3e5b12f-6e6f-3521-83ac-85ea5245ac4b | -8.87749 | -62.40573 | 2025-08-20 06:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b29442ff-61c2-3db4-9664-efb1965c44c6 | -9.18261 | -59.64269 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9a68292c-6649-3c3e-a6ed-d72dc73e769a | -8.88362 | -62.4066 | 2025-08-20 06:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c42cd4a3-1604-30c3-8a24-2e829be81812 | -10.44633 | -64.40508 | 2025-08-20 06:16:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e17e894-8ba3-38ee-ad1b-660d681a0d4d | -8.63862 | -67.26618 | 2025-08-20 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e16d2489-2e21-318e-8f4d-32cbdc0200d4 | -8.56693 | -66.9474 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65382d41-9c11-3890-8f44-23a557ffcd03 | -8.56796 | -70.06149 | 2025-08-20 06:16:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| add396bd-ddbf-3a82-b69c-ee573b888e42 | -10.44542 | -64.41215 | 2025-08-20 06:16:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1159c7b4-60da-3baa-9d74-a5db8dfae1b2 | -8.34908 | -70.85208 | 2025-08-20 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9da2aa99-19a2-3754-aa54-ce4cedbdcebe | -10.25229 | -64.47922 | 2025-08-20 06:16:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0ad17b1f-3eca-384e-a531-e86620d7f83a | -6.93221 | -62.8809 | 2025-08-20 06:16:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e149d265-f24e-340a-9628-52ef8dd2ed7f | -10.25184 | -64.48286 | 2025-08-20 06:16:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 123b946f-852a-3001-8c88-2b37149ef310 | -9.19122 | -59.62715 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 747459ad-8479-33bf-8c4d-ee61971c0669 | -9.18215 | -59.64077 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f6e391b-e09e-39c3-8024-fe7abfe3279c | -6.93801 | -62.88175 | 2025-08-20 06:16:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bd1f25c-bde7-3047-8f3a-5cb96fbb08d0 | -9.19846 | -59.62836 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb0f7113-0c28-3781-af47-75f50bbd41f6 | -8.16438 | -70.76496 | 2025-08-20 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README57.md)
