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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4372f0c6-f3fa-3b2a-8440-975ab1ea2492 | -17.00659 | -55.04292 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c6481ac9-3248-3df1-a7d3-f9e9597c41c9 | -17.00607 | -55.07124 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e0473563-78fb-3e0c-9d7b-964bccfbd41e | -17.006 | -55.06696 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| b292bc22-02e3-382d-a888-aef5db6bd227 | -17.00561 | -55.04416 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| b19e7527-a2f7-3a2c-947b-aff16de107cd | -17.00553 | -55.04837 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 60646f4a-0f10-393b-91ad-f03485f573c0 | -17.00489 | -55.07241 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8f419e1a-3988-34d8-81b6-971fa52f31ec | -17.00452 | -55.04959 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| cacb4620-eec0-3722-88c7-3ae02d7a1173 | -17.00235 | -55.06473 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 8a2d0580-70d6-31ab-bc5f-bc26e902fff7 | -17.00181 | -55.04189 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1926a32f-c47b-3329-9039-c340e38b516f | -17.00129 | -55.07019 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 26.2 |
| a198f548-8c2d-304c-82e1-fd62cd7a4222 | -17.00122 | -55.06592 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| bf63a7ea-1635-39b3-b32c-2e507c0ba530 | -17.00012 | -55.07137 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 32c14aa6-cbf0-38dd-a022-fe295780ddfe | -18.90055 | -54.53129 | 2024-10-06 04:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5a0d2bc-81e0-327f-9de8-405a073da1fc | -18.87955 | -54.5434 | 2024-10-06 04:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 856f6b2e-c82e-3a0f-9cef-13821e79c1bb | -18.87858 | -54.54832 | 2024-10-06 04:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32a0d3c0-e173-3384-881c-9470674ade31 | -18.87722 | -54.5317 | 2024-10-06 04:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ab8fb955-08f8-320a-b922-72515eaecf64 | -18.87412 | -54.5473 | 2024-10-06 04:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7d9340e-2744-3320-b70e-3e8dad19af6c | -18.86968 | -54.54624 | 2024-10-06 04:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d11ecc74-9a90-31ca-9641-474348c7ae3a | -18.86835 | -54.5434 | 2024-10-06 04:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 997ae18d-2717-3782-a8b2-710a22e359d1 | -18.86736 | -54.54859 | 2024-10-06 04:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8877038b-d649-31e5-8db9-ff59d6465cec | -18.85956 | -54.46825 | 2024-10-06 04:21:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85bd98e9-2409-3ad5-8287-e22c310899a5 | -18.85076 | -54.46587 | 2024-10-06 04:21:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aa330f94-1e2b-3e00-807a-2b95c55e0fce | -20.77854 | -54.82975 | 2024-10-06 04:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2874fccd-6a23-3ecf-9d04-90c83d29b047 | -20.58007 | -55.74781 | 2024-10-06 04:21:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f7e3908-3edb-366d-8153-860d9896ac78 | -22.5052 | -55.21161 | 2024-10-06 04:21:00 | NOAA-20 | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 90307109-353a-3fbc-8808-7be01626be34 | -25.19125 | -49.32631 | 2024-10-06 04:23:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 91e58491-9c70-3a35-8801-5ec389128fea | -28.05985 | -48.67192 | 2024-10-06 04:23:00 | NOAA-20 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 51a42755-d26f-3296-8fae-d4661fa32d34 | -27.13477 | -48.62966 | 2024-10-06 04:23:00 | NOAA-20 | ITAPEMA | SANTA CATARINA | Brasil | 4208302 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3f0ad3fc-9296-3f5b-931c-aae6cb4563a0 | -30.16096 | -50.21035 | 2024-10-06 04:23:00 | NOAA-20 | CIDREIRA | RIO GRANDE DO SUL | Brasil | 4305454 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 40d40158-ff9c-3c0c-9d3c-ae1dd302ad4f | -29.81315 | -51.17786 | 2024-10-06 04:23:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 206cc73f-cda3-31d9-b989-fef85b548ffd | -24.97998 | -51.84684 | 2024-10-06 04:23:00 | NOAA-20 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7756c820-517b-37b8-9ce6-d2297ae3412b | -24.55637 | -50.88044 | 2024-10-06 04:23:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2a189974-85f2-3604-b6ff-0a3b3147aa51 | -23.68416 | -53.31487 | 2024-10-06 04:23:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 987acc32-3242-3916-a844-efeb5c0bc5b8 | -23.68194 | -53.3161 | 2024-10-06 04:23:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b4c4d35-bd01-383f-8e5f-7364dd7f522c | -27.0986 | -53.00711 | 2024-10-06 04:23:00 | NOAA-20 | ÁGUAS DE CHAPECÓ | SANTA CATARINA | Brasil | 4200507 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f12d2a96-d3c6-3a7a-88b1-7255ea5bf4fe | -25.01756 | -54.08249 | 2024-10-06 04:23:00 | NOAA-20 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7a193431-a5de-333d-a7cb-d45b1d6c3728 | -25.01647 | -54.08824 | 2024-10-06 04:23:00 | NOAA-20 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a744ddeb-c482-3d53-aa6f-0ec358a5d67e | -25.01369 | -54.08152 | 2024-10-06 04:23:00 | NOAA-20 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 773fdac7-1759-3e50-a2ba-9de5dcc05f68 | -23.89319 | -54.22243 | 2024-10-06 04:23:00 | NOAA-20 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0f906cf7-620a-39e0-93b3-7a597dacb2e6 | -23.89245 | -54.22628 | 2024-10-06 04:23:00 | NOAA-20 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9fc7ec25-d531-3263-815e-59199ffed756 | -25.49143 | -54.52545 | 2024-10-06 04:23:00 | NOAA-20 | FOZ DO IGUAÇU | PARANÁ | Brasil | 4108304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5fed0acc-f56a-3f7b-b43f-7e20a2488315 | -30.15084 | -52.02603 | 2024-10-06 04:25:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| e820cb45-fa98-3837-98ac-aaa8027a0a48 | -2.8166 | -48.6867 | 2024-10-06 04:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 098e5c83-6a2a-33d7-b93d-56cbc47a9d8f | -3.233 | -50.8296 | 2024-10-06 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| a9d029b8-cbe9-35a8-8f3e-840fbfa0ae1b | -3.1315 | -48.591 | 2024-10-06 04:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 92605223-f6a9-3e4f-8974-45f1951ca992 | -3.1314 | -48.6125 | 2024-10-06 04:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| df9742ba-73f9-3759-aa6a-aabe728db194 | -3.113 | -48.5916 | 2024-10-06 04:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| cf251947-6f81-39f4-bb88-e845186c15ea | -3.1129 | -48.6131 | 2024-10-06 04:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| af297321-b7f1-31b2-a568-b9649094d02e | -3.3084 | -50.451 | 2024-10-06 04:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 41eb9952-b5ec-33f6-a604-0aad9b75ad8e | -3.8465 | -46.4492 | 2024-10-06 04:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 3202b43a-538a-3f1d-a63c-169df3c219ac | -6.9699 | -59.0658 | 2024-10-06 04:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| f536e6e8-9987-35f7-ada4-9855ceff4057 | -6.9514 | -59.0666 | 2024-10-06 04:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| ad0e649b-882c-33bb-85d3-e5a51a05b910 | -9.347 | -46.514 | 2024-10-06 04:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 17640b9a-e413-34c8-9eab-7665c9fba6c6 | -9.3467 | -46.5365 | 2024-10-06 04:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 184.1 |
| c7cd4c93-ca6d-3b17-84e7-2632f519deda | -9.3278 | -46.5385 | 2024-10-06 04:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 2197fdb4-8f33-3720-979d-1ce6ee212156 | -9.1574 | -61.5611 | 2024-10-06 04:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 59887adf-a372-3321-b5ee-e2521cfb4f2e | -9.6883 | -47.8088 | 2024-10-06 04:26:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 11b3f599-17e9-33b4-bd73-ba2e5e7f71f7 | -9.6965 | -64.6262 | 2024-10-06 04:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 4a0367e0-5bec-3bdf-885b-f40a7dd1d170 | -9.6779 | -64.6269 | 2024-10-06 04:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 9388c799-704a-3038-a7ad-f8b65b1007db | -12.6092 | -53.1129 | 2024-10-06 04:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 0ea81b03-a5cb-36ef-a5ed-b2cf199504b5 | -12.6089 | -53.1338 | 2024-10-06 04:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 46069961-d547-3818-bd4d-f9be7823bec0 | -12.763 | -50.5352 | 2024-10-06 04:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 188.9 |
| e06efb9b-c78b-30d5-b21c-644f4e9eaa76 | -12.6283 | -53.1108 | 2024-10-06 04:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 102da274-2324-33c3-8232-ab9852d4bd7d | -12.7825 | -50.5112 | 2024-10-06 04:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 35bd82e7-8679-3678-a4a8-cac9f179edff | -12.7822 | -50.5328 | 2024-10-06 04:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 4d3668e1-170d-33b5-99f1-547055f39d64 | -12.7634 | -50.5136 | 2024-10-06 04:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 239.2 |
| 6b456fe0-d344-36d1-b72a-57cc8fb561ab | -12.9377 | -62.4697 | 2024-10-06 04:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 33.4 |
| d59fb18f-195e-388f-905f-5f8369a691ae | -13.3978 | -61.9376 | 2024-10-06 04:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 91f53347-513b-3d0c-b05e-e153c2cce9b9 | -13.3976 | -61.957 | 2024-10-06 04:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 6deaadc8-1235-38b3-a924-42acadac089c | -13.3788 | -61.9388 | 2024-10-06 04:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| a5875620-b00c-3526-a58c-de88a49c0a51 | -13.3786 | -61.9582 | 2024-10-06 04:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a0d31fb9-b5a2-32fd-b575-9975deb5a4d1 | -16.3764 | -57.3663 | 2024-10-06 04:26:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 05e609d6-4491-3ab9-9e5d-62ebf29c68d6 | -16.5544 | -57.2032 | 2024-10-06 04:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 1d826f54-5c70-3e2c-b1dc-e0eeb2dd893b | -16.8238 | -57.4584 | 2024-10-06 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 6d95e546-013d-3f15-8869-7c871cca44da | -17.1185 | -57.3834 | 2024-10-06 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| b81e7c2f-58bf-356c-a6b6-0049e8e273c6 | -17.1182 | -57.4039 | 2024-10-06 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.2 |
| f7173780-b5ba-3527-a73b-9d730f7c344a | -17.0207 | -55.0371 | 2024-10-06 04:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 236c78f4-13c7-3bc7-8c7f-ef558e024f15 | -17.0203 | -55.0581 | 2024-10-06 04:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 1506dc53-a43a-31d6-a4d3-0b20f31531c9 | -17.001 | -55.0398 | 2024-10-06 04:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 734ead85-be70-3a23-8e86-aa9de6654a08 | -17.0007 | -55.0607 | 2024-10-06 04:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 1664e897-39d0-3544-9410-9e0a29680238 | -16.9717 | -56.7646 | 2024-10-06 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| fad0718d-8be9-3eea-95a4-91102fcdde9b | -17.1375 | -57.4221 | 2024-10-06 04:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 43184f44-a458-367d-a3c0-fbcbc4ba09ba | -17.8323 | -53.7616 | 2024-10-06 04:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b10de19e-104f-338f-ade1-a890d720e025 | -17.8319 | -53.7829 | 2024-10-06 04:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 45864bdb-03c5-3dc2-999c-70d27c41bd54 | -17.8125 | -53.7645 | 2024-10-06 04:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 966e45d6-3d00-3d6d-b71f-8dfe33847e6a | -17.812 | -53.7859 | 2024-10-06 04:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 136.1 |
| e648638a-d35e-3af1-b398-f730fad8ec3d | -18.659 | -57.2552 | 2024-10-06 04:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| f2891011-bbbc-324e-8c2a-de6629c2df21 | -18.6391 | -57.2578 | 2024-10-06 04:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 17d06111-87e7-347c-b1f7-d0a1f151ae79 | -18.6387 | -57.2785 | 2024-10-06 04:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.7 |
| e2780dbc-04da-3381-a5d5-044ad4af1d05 | -20.4712 | -51.2806 | 2024-10-06 04:26:59 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.2 |
| 2eec8ea4-9f80-3c46-a805-47b7b1da6344 | -20.4508 | -51.2846 | 2024-10-06 04:26:59 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.7 |
| 93c80a38-96d5-3caf-9009-fd1e0aaace98 | -20.582 | -49.3635 | 2024-10-06 04:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 43d52276-f110-3dc3-a6df-bbaedbeb3ed3 | -20.5813 | -49.3865 | 2024-10-06 04:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 542.1 |
| cbc62cec-3b16-342a-8412-9f5ac1572779 | -20.5807 | -49.4095 | 2024-10-06 04:27:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 2b79b47a-fe60-37dc-8e01-80de6a53211b | -20.5609 | -49.3909 | 2024-10-06 04:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 34a95433-8dc1-32d4-bc44-aa42db97512b | -2.847 | -50.4648 | 2024-10-06 04:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 00b08a08-dadd-31bc-97db-193fb7ff5ad7 | -3.1315 | -48.591 | 2024-10-06 04:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e1ceab2c-620c-36c5-9ecb-a7ac7f0c9ebf | -3.1314 | -48.6125 | 2024-10-06 04:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| cb05425f-787a-37d8-866f-94730cf0e26c | -3.113 | -48.5916 | 2024-10-06 04:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 3f3811d2-d024-374d-91cf-41f465251688 | -3.1129 | -48.6131 | 2024-10-06 04:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |


[Clique aqui para ver as próximas entradas](README95.md)
