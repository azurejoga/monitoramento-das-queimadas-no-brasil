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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f29c372f-90f8-3539-9926-596dd3c98e2b | -7.91942 | -61.73433 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e8fa815-81a8-331f-b93e-f9a3ba2d18f7 | -7.57226 | -60.88632 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e3a3a85-721a-3d55-90c4-268c4e946f7c | -8.57517 | -54.72938 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 8bc83c54-2b3d-3a5f-9fba-21b63ba852aa | -12.3992 | -54.96067 | 2026-08-18 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db097e88-8946-3b23-8f02-01ea574a07a9 | -7.87998 | -61.79406 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bb38e4a-ccc2-3e94-98cd-fd77170cc31e | -14.03081 | -53.68973 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8c32fc21-45ad-3e61-a693-9d342097ec3e | -7.87845 | -63.76365 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 017a53e3-336b-37d9-937a-29758d9b4c04 | -8.90209 | -60.59444 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abd8254e-28d9-30a2-824f-4a3cc79d2d3d | -8.90281 | -60.56025 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a216f709-b95f-3e27-b1be-8acabb453f48 | -8.98057 | -60.50583 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f793fd0-3d92-3655-bf63-ecce44cf9d00 | -7.56572 | -55.56174 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b18eb02-c047-30c1-93aa-779c65b50bdd | -8.56535 | -54.70933 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a7833e26-64eb-3ad9-8000-e56b9a6a23f6 | -9.5898 | -60.50703 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9de3f613-4722-3c7f-b75b-0baeac984700 | -9.16833 | -59.67677 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e7b18de-cd70-3594-b372-d8386bbabda1 | -14.03852 | -53.68303 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5a064a36-f1ac-323a-80a9-1d528e8b19f0 | -8.58543 | -54.69746 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a4d3674-3984-38d7-af7d-cb53eb58986c | -7.6175 | -55.62752 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6603ad1e-ede0-358d-a29e-8a023ec833c8 | -8.56772 | -54.69065 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8441ec7-9e02-3a51-930d-dedaaf4fa975 | -8.96031 | -60.52973 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e5ecc70-87b2-3f50-aa2a-67a3b970b443 | -8.96136 | -60.52221 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80273034-92f2-3437-ad7a-cdc73211e3d7 | -8.58672 | -54.73572 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| a5ffb955-998a-308c-85af-7a180f78908d | -9.16423 | -59.70704 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66ed3e40-410d-3722-b97a-45dadf8db13f | -9.83293 | -65.06647 | 2026-08-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e7d7bea-0e45-3d0d-9af2-cc90d1050ef5 | -7.87559 | -63.7594 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3fa7a8e-31a4-392e-ad7e-955f7c61e994 | -9.12913 | -61.60341 | 2026-08-18 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 489d2f2e-e8de-370c-b548-73ff85885faf | -8.89637 | -60.60505 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 396c2ddb-5995-30fa-8657-f9d1ce7ed297 | -9.4283 | -60.4537 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3d4433fb-e24c-3740-9c44-9669689a9f25 | -9.08247 | -65.37304 | 2026-08-18 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af236e08-b196-3ffa-bd87-d66227d65a52 | -8.57143 | -54.71024 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 8377094c-977f-33d0-bc22-fab18631b488 | -8.22215 | -55.03938 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| b6c3fc9f-8e93-3aae-aa97-cc646d6122a6 | -8.73486 | -62.90693 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf8792a7-895f-3bdc-a58b-7cd956bd8cea | -13.42056 | -57.04548 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1cacfc0-4d22-301c-aa47-c93bacf87a48 | -7.61244 | -60.94449 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82324b4f-032e-3b53-b4f4-d04abdf7136c | -7.61886 | -60.95588 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a667347e-a42c-3704-ba14-be0a2f7f225e | -7.60776 | -60.94902 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 189a2f07-7e56-3625-9408-fdad5d1bf748 | -8.96189 | -60.51844 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d2c0c07-1302-3d6f-9a39-a936cdaf2604 | -7.5538 | -55.56427 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5614c668-2f58-36c6-8faa-449a4779b526 | -8.90317 | -60.58697 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d0418c3-0e87-3980-a703-cf624d2d6042 | -8.56907 | -54.72874 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| e95961b4-3864-367e-bd4d-325a5a8a43c1 | -8.22158 | -55.04375 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 49fa4a7e-d973-32f5-a925-dde045fa1d55 | -8.90121 | -60.5714 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68ea4f8e-2563-37e9-95a9-1bfa3e51b4d2 | -9.42844 | -60.42217 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fa0ce28a-bf00-3435-823f-44aafa55992d | -8.22272 | -55.03505 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f3001aaf-ad4f-3c79-96f7-3bc623642509 | -7.91498 | -61.73835 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34ab1205-22e9-3fcf-bb4e-846e304db25b | -8.58969 | -54.71254 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2dede4d4-5af2-3dfc-9d36-1b0feda5ce8c | -7.56848 | -55.56131 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9fdfb72-d31c-3e10-8596-83bb2739abe1 | -7.56797 | -55.56521 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e2525fc-5926-3b6b-a09a-89ae1caf593f | -7.91053 | -61.7424 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f60cc07-6d9e-346d-b3e3-09be082c14a3 | -12.46724 | -54.19785 | 2026-08-18 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 027b5e09-82f8-3919-80b9-58643765216f | -7.8893 | -63.76149 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b26ca96-eb15-36a2-85f2-fb29c03032de | -8.51647 | -70.27004 | 2026-08-18 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 020e51d9-fea8-3454-b193-ece5416a04c8 | -11.2029 | -54.82109 | 2026-08-18 05:44:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| abc63710-7973-3dfa-9a3b-20a1a8c341cf | -8.56476 | -54.714 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5a7f89c1-436d-3d86-a938-5a4c18c579ca | -8.57813 | -54.70621 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b343cbf8-9333-3a67-aca6-5f3f0ddecaf4 | -8.56417 | -54.71869 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7c5a0ce0-afa6-303c-ae02-238e57814a08 | -8.21251 | -55.02057 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5737d9cb-9202-3d77-bb06-63c3b4c90561 | -13.41589 | -54.38176 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 97150a36-659e-39c2-a2dd-a619f2880188 | -8.90175 | -60.56767 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89d8379e-adc0-39fe-820b-8002e704feba | -9.26578 | -56.89785 | 2026-08-18 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cddb6c65-8cf0-3011-b15c-2f17f68e2d61 | -7.63857 | -55.64231 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d90d17b6-01c6-34af-abaa-0fd0dea7590d | -9.43006 | -60.41058 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 326ac5be-9dbd-30c5-8712-6d15ccc20280 | -8.5542 | -55.3032 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea0f32ec-642d-38fd-b8f7-3536c97c13ee | -9.05896 | -71.25564 | 2026-08-18 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be9f7c0e-01ed-39b8-8f88-6b46fcb09d9b | -8.94535 | -60.51595 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3189f4e-604a-3de6-aba1-6fe55b1c7e96 | -9.39288 | -65.95832 | 2026-08-18 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e019f0c1-fb27-358d-85c2-5ca013938893 | -7.64168 | -55.64082 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6cd68789-f980-35d1-8c99-25426eeb2de8 | -12.75677 | -59.76845 | 2026-08-18 05:44:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4ee7feb-86fa-336c-a18a-161ef77f8a86 | -8.55259 | -55.3161 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45dafdf2-a81a-3d94-9c0f-5d15796ba420 | -8.95671 | -60.52534 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba6ee006-cfba-3920-abb5-ad4af48dfc60 | -8.58482 | -54.70224 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c4838c7-a4a5-3209-8705-c62ba008705e | -8.94896 | -60.52033 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b9f587c-aff9-3755-b805-0516c7032748 | -7.90364 | -61.73669 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| feb779c0-6b83-3201-a366-e772492a521e | -8.08582 | -61.35965 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00643694-f458-314e-8ade-5e070ed9637b | -13.41757 | -54.37799 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 71498eff-80a7-38c3-aab4-c7baa959146e | -9.42952 | -60.41445 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3df22a2b-c5ff-3953-ab11-efff98d78118 | -7.61097 | -60.95475 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d17d8339-0d95-39ed-bf64-02acfc4b6a71 | -8.94996 | -60.54343 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96590da5-442b-3491-895d-1936aaec79dd | -7.60171 | -61.23761 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 319a8cdf-caa1-3848-91e7-3f751fee67fb | -8.58113 | -54.68264 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 749dcd68-ce93-385f-b25d-a6fcad0b511a | -7.62264 | -55.63223 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ba522f7-7a5c-3329-be29-2c8961894fdf | -14.03211 | -53.67722 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 23e45cab-ad56-30c5-aff3-03855e8a767f | -13.42777 | -57.07116 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d8c82c5-8303-31b5-a949-1ebd06327d44 | -8.57262 | -54.70082 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| bf0d1427-c92c-31fd-8e01-9d0f0ba7721a | -13.421 | -57.04174 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aacc19e-1393-3de9-888e-b5b8f9ca0f6d | -7.57361 | -60.88498 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f19c178d-a3a2-30d9-9809-19c483171c88 | -14.10319 | -58.43106 | 2026-08-18 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25a3dba9-953b-3c07-aab9-874981076fd0 | -8.96445 | -60.53035 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ade2f36b-b138-3af7-8b96-8c64bf21a4c3 | -7.88987 | -63.75775 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32fe2b40-e049-3106-aa86-d30efe4b291d | -8.90388 | -60.5528 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c388fb7e-4141-3eec-96b6-721056197cd4 | -7.55841 | -55.57283 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 773bba85-199b-385c-8506-bfa41d72f884 | -7.62933 | -55.62535 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f95e6af-9262-3a36-8657-38144681b814 | -8.09253 | -61.34053 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f2cfbef-77a0-3f63-8b51-2477618050a3 | -10.07412 | -60.49707 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13134d1f-2c9e-3082-9b11-a9ea88b4c6c6 | -14.03225 | -53.67574 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c78bde96-3e7a-3e24-a129-8a4d84bdf6fa | -9.59869 | -60.50439 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff32fd0e-32fb-39a3-891b-48c822bfaeae | -8.56024 | -55.30957 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dce48b6e-b8be-33f5-a7cc-d73b177b585e | -7.13301 | -59.64261 | 2026-08-18 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2954682a-a862-3b33-aab1-11c4116ae66e | -7.60882 | -60.82869 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 382c21c4-150e-32e6-b80f-e8ee5dbc0a2c | -7.56178 | -55.56836 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bfd53b5f-bbec-38d7-9af9-b860cbe781dc | -13.41589 | -57.03704 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README55.md)
