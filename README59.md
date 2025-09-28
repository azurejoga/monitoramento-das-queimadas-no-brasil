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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71ac1d21-fd85-3e83-9b62-fc9a608d568e | -7.0547 | -45.57195 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a625b75d-21df-3b96-9067-c6a5b84f3f71 | -10.97052 | -54.09775 | 2025-09-28 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2308729e-bfbe-3ffc-9b6c-4a451658f412 | -6.0163 | -46.45164 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7106b88-a6e2-311a-bedf-002e9a4b8cbc | -5.89897 | -43.29114 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6e1f987-2742-3476-8db8-68d451882ff1 | -11.61315 | -44.40538 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0105807-47f5-34e8-8eff-431bef97cddf | -11.97783 | -47.88823 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af1fa066-3c7f-3669-94ba-2d5636a97fba | -11.84752 | -48.25548 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ce76333-6382-3b45-a1a0-0f835b90a3e5 | -6.58176 | -44.43672 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fbe0ae3-b49d-3dbb-9b5a-7fc1399461be | -6.15436 | -44.1643 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8018d709-d63a-3cdc-b0ee-b0468a246e38 | -11.66984 | -44.29501 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 017afdc0-56bf-3069-8bdf-cf4db77d4258 | -9.06642 | -45.53629 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 976334ec-f54b-3c61-a3c3-4e82e5982d14 | -7.7527 | -47.00666 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19017aef-e87d-3695-b12c-2c980a0288cc | -9.98037 | -43.60302 | 2025-09-28 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e811f19-87e2-3b85-ab5c-636b9df1e5de | -10.41489 | -48.14475 | 2025-09-28 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 796e07ec-db4f-363b-ba11-4feda4148815 | -6.51355 | -54.87887 | 2025-09-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edd4e22f-522b-32a2-b590-ec05324855f5 | -11.69175 | -44.43275 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a218d912-abc5-324d-9409-ceff74814de0 | -12.0168 | -47.91979 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e3631ab9-e521-3ca8-9a6d-53fbc972f1f4 | -6.27788 | -43.62917 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8355b896-9e41-3f5d-9001-0713e911320a | -8.47432 | -46.91127 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbe5c831-3ec9-3f6e-bf27-029e70139f5a | -11.36253 | -44.94429 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab0fd7b8-2dad-3b1c-b284-1ebe2fac0f32 | -6.68958 | -44.57694 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b66868f2-7170-3275-9bc3-dfccd79a439d | -11.9948 | -47.8872 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68c677a7-a436-312a-bc73-b6eabe6be03c | -6.58102 | -45.10186 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ed83cd3-afac-3615-ae24-ef0a71356593 | -11.40538 | -44.90568 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5861f3c-dead-3e93-8e9e-565270efe718 | -7.7549 | -45.74216 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41daa124-ea40-3dde-a5e9-72d5b58303a1 | -7.15049 | -45.5043 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 814e0628-8c69-38dc-aeff-29e94e55f285 | -8.94653 | -48.66096 | 2025-09-28 04:25:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f30e783-dc4c-36b1-b74f-b54f038c6783 | -11.4464 | -44.98841 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b00e0317-7f86-3652-a816-86cf080606b7 | -6.27848 | -43.62518 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5c3c6e2-b156-3336-9597-4ebfee2aaeb2 | -5.64877 | -44.92097 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98a46e07-10d8-3670-a50c-2bf84b2e6237 | -5.87976 | -43.20163 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 812ae4f4-2af1-30f2-8c59-0c3ee1e370e6 | -8.68408 | -47.06646 | 2025-09-28 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0f37e43-184d-3a3e-a96c-6b2d5b8c52ee | -7.54608 | -46.09894 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25d9c25d-23e6-36b0-857e-b485ebcd76d3 | -8.16723 | -46.4033 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7b2288ac-ae59-36ef-a375-ac4b0452f7ec | -12.97427 | -46.28767 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2e89cb15-ca8f-30da-a753-c5f743e8aa99 | -7.87361 | -44.55014 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5737d4fe-a81e-3a0b-a6e4-5e2b0cffaf07 | -10.71351 | -47.99609 | 2025-09-28 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8af1bfcb-be73-31b2-9803-589403f9cf11 | -10.53943 | -43.63393 | 2025-09-28 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95e9f053-58db-3cfd-9521-ba80220508da | -6.07192 | -44.06467 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f599aa72-d8ff-30bb-b732-ce030b290f37 | -6.83033 | -44.09046 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad9303e6-0c94-35a9-be75-1acea9f3af0a | -6.64648 | -39.50503 | 2025-09-28 04:25:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 79e40174-e37e-3668-912a-ff710632aef1 | -11.99755 | -47.89127 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7189b9bc-592a-3022-8e60-879b060d75c4 | -11.95329 | -47.97834 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16667dbf-a7a4-3d1f-bde9-f77fcf427470 | -11.37576 | -44.93724 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93a4c743-adcd-34bb-9d1a-306aec11da5a | -6.22376 | -42.79765 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f588142f-929a-3b59-b5bd-c01fe21c1eba | -11.68818 | -44.43221 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a873523-6c6b-39c3-bc0e-80f15c7e792f | -11.8559 | -48.24591 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a115ab39-3899-30d0-8776-87ad638e5602 | -12.95301 | -46.38153 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e8b21437-7127-3fde-89e7-b16da04ba20a | -5.8059 | -45.87013 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59493e0a-ed50-3f9e-be1c-8331d9e9264c | -8.45251 | -49.56886 | 2025-09-28 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5abba14a-8dc1-326f-bced-6ca5221477e0 | -10.42184 | -46.15992 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6dd1333d-0485-3f18-9b21-429003f2c5cf | -12.73661 | -46.81665 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c18f4231-4949-30b6-858f-5627a4d51515 | -7.62199 | -43.7984 | 2025-09-28 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c01097e5-2361-34f3-8694-d6280f7e41f1 | -12.88736 | -47.09216 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12a235e0-1eed-35bd-9204-f4e70d843ce8 | -9.29549 | -45.68114 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfdaf456-bcad-343d-9775-94fb854d6860 | -11.98003 | -47.89582 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4704e4a4-ae5f-3441-a439-6dfa17973bde | -11.20913 | -47.74388 | 2025-09-28 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36bc9a0f-7dea-3ac7-9528-ddedc0a68f7a | -9.30178 | -49.10259 | 2025-09-28 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d307179c-2665-39ed-b01c-d15445b0fc09 | -10.77029 | -49.02969 | 2025-09-28 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a648ebc3-f278-3701-b8a3-e2e10cf0553b | -6.25437 | -42.47042 | 2025-09-28 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb6e7605-897d-3e14-bb50-a8c51ec9d364 | -6.80699 | -46.39335 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0842b77-8b76-3ff4-af4c-9f54b140a658 | -11.42623 | -44.95695 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a3c8fac4-510b-35d8-bbeb-fafc9a84d654 | -11.35014 | -45.00245 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b60c9d88-65a5-3d19-b803-88806d594a03 | -10.99054 | -57.06458 | 2025-09-28 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa2f5577-2b94-38c3-bdc9-3ddb5809f0ae | -9.92046 | -54.87525 | 2025-09-28 04:25:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ed2dde3-d673-33c7-8cdd-0e991b613996 | -6.1826 | -42.94666 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bc5e41d5-6026-3614-8a60-da43f9e1de0b | -12.0154 | -47.04643 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4ef656b-7eae-3d0c-a03d-a80a03c6b0b6 | -8.63783 | -44.83986 | 2025-09-28 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45559f11-0a60-3103-86ab-af485f535d73 | -12.89744 | -45.17025 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 77631fc3-3e0f-39ff-869b-bc3cbc593489 | -11.99277 | -47.8798 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 534278e9-6cc3-3238-888e-b138aaf327c4 | -11.61846 | -44.41884 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de991732-01c7-3b69-956d-e3c292d3db3b | -11.35729 | -44.95541 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7df79c80-1ba8-3908-8060-61cc5e19a47c | -6.51302 | -54.88185 | 2025-09-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6d327b0-966d-329f-b1f8-48297cdba091 | -12.01568 | -47.92685 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1926a213-2b82-32ce-b05b-0a650587c87f | -6.39196 | -43.96421 | 2025-09-28 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fce407a0-4e24-31ee-a5dc-41f7fb0fe1b4 | -8.2867 | -45.46277 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f095273-b1a5-394a-acd9-c91f100541e2 | -6.42552 | -43.51265 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fb0858e8-ab28-32e8-a80d-0db9b202437d | -8.4947 | -44.72344 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9f69ceb9-7a62-37e8-912b-8967291017cb | -11.99001 | -48.00232 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b17987d9-f9dd-3ea8-8692-b0bfff84b5e6 | -6.81507 | -44.10458 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52739547-24a0-3db4-8f6f-9e787b8b84ee | -7.86221 | -44.57901 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf3591d7-07d9-3956-996d-63d370c53bee | -11.66624 | -44.29447 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9efa1af-be08-3fac-8802-0cdb818e06f9 | -5.90213 | -42.94294 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ccb265ef-6686-3807-949c-90cde6a2019b | -9.00576 | -47.83912 | 2025-09-28 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d59f5a1f-40f2-39b9-b379-f8db6bb59bd3 | -6.89965 | -44.75763 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 10742924-8972-3c46-83d4-1d296de88657 | -6.53219 | -43.82887 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f07a5492-c63f-379e-b02c-45e19d60ff8b | -7.30756 | -42.94531 | 2025-09-28 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dbbd8b8e-54be-3005-9e86-fea4e80c0662 | -11.42276 | -44.95636 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1533ccc0-d34e-3df6-a790-99cc7ee5b275 | -12.02125 | -47.91328 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7414e8f5-3f1d-3013-a8a2-afab6762b070 | -10.45539 | -48.20595 | 2025-09-28 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 72ab0346-2cd9-3f21-81ab-aa706d58974a | -12.89919 | -45.15836 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a0a2ac48-bb90-36b9-95f5-3d33bfbc374d | -12.98357 | -46.84479 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97a56fd1-4775-3f7c-9027-74cab0a82c7f | -11.38776 | -46.93505 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a84942bb-dd29-3141-b57d-5d927d9aecba | -12.00159 | -47.0695 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dfb58d8-55bd-3837-9e36-a28c47cbf60c | -8.43392 | -46.86618 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e44c20f1-5c5c-3cfd-959e-3d1a85acfa7c | -6.53626 | -43.82561 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a059d86f-18df-35b6-87f8-ce471c935373 | -11.84534 | -48.24781 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93376f75-aea4-3e53-8eed-436306817b36 | -7.59374 | -43.05318 | 2025-09-28 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3e6c3d2-7d97-36df-a0d6-0281512a0f6a | -7.20753 | -44.53425 | 2025-09-28 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7aeb246e-285c-39b3-add4-0412ef767477 | -6.83724 | -44.09152 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README60.md)
