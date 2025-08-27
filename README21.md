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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6050cdcc-4453-3b9b-9232-d39417d45acf | -10.32128 | -46.77385 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e05c2536-24ba-3c3c-bb13-5d829b11995f | -11.24483 | -44.99171 | 2025-08-27 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee666c3d-168e-38a8-b300-663881490088 | -13.623 | -48.21393 | 2025-08-27 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cf3c9def-070a-3eac-b821-ec9a0e19fd02 | -13.50063 | -46.87506 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9c6b8824-786f-36a1-8d2f-895aee9b2e82 | -12.49918 | -47.23477 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3aa94695-4d03-329e-a814-ac43dcf05875 | -13.49081 | -46.86145 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11ca6e31-580f-3263-b8fa-b6267f180b74 | -13.62534 | -48.20321 | 2025-08-27 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 876da80c-62eb-32fa-84ea-0c17ab55d97c | -12.41173 | -40.46848 | 2025-08-27 03:38:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2abaeafa-894f-38a2-a786-3339b6fac376 | -6.8412 | -58.9746 | 2025-08-27 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 77b8a449-677e-32ec-907d-fab97a6fa4c5 | -6.8413 | -58.9552 | 2025-08-27 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4e761e48-3ad1-3df5-bfb6-2302a841c991 | -9.4065 | -60.4941 | 2025-08-27 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 59adebac-eb7b-3a7f-bd03-0e4f58bcd84a | -9.4062 | -60.5326 | 2025-08-27 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| fab4c755-3742-3715-8f94-26687a822542 | -9.4064 | -60.5133 | 2025-08-27 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 07bce504-a68c-3fd5-b9e0-163ee76693bd | -6.8228 | -58.9753 | 2025-08-27 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 03341223-1a35-36c5-bd19-8bd0f98ea77d | -9.1715 | -59.5599 | 2025-08-27 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0ae0d3e9-7175-37d2-8273-aa439f07abeb | -17.79381 | -44.47852 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 234f8834-be01-3622-8860-832e3a9783eb | -18.20041 | -45.56375 | 2025-08-27 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c097e12d-b446-3fef-9be9-7dbc6fa310ea | -20.48063 | -40.65924 | 2025-08-27 03:40:00 | NOAA-21 | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a47697e1-921e-365c-9e72-325864d533d8 | -17.80642 | -44.51148 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70c70672-b01a-3781-aee5-0520a97d417f | -18.07851 | -44.05987 | 2025-08-27 03:40:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5af970a3-c4db-341f-b4c9-9f28d9311e75 | -18.15118 | -44.42501 | 2025-08-27 03:40:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d309ec6d-ad65-32f0-97c7-e70966d7453b | -18.72388 | -43.81528 | 2025-08-27 03:40:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b54f466-fdb3-31a6-82b2-b0c102561a35 | -15.52112 | -47.39103 | 2025-08-27 03:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f950af3-878b-398c-acdc-8eeeb2b2ae7f | -19.52962 | -40.15975 | 2025-08-27 03:40:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8853742b-ba3f-362c-bd3d-a278078d5887 | -22.16213 | -47.07596 | 2025-08-27 03:40:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1e36b32-7c33-347b-91a1-88c6c670fc92 | -18.22015 | -44.52699 | 2025-08-27 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 92c927f2-8c30-3a53-9aae-eef770ec8f4f | -16.6046 | -40.99127 | 2025-08-27 03:40:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 26f7bc9a-9ed6-3889-80d7-7b31a4f83057 | -18.76075 | -40.12262 | 2025-08-27 03:40:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 86e24148-604d-321d-99c1-cf7c28eab9b2 | -21.69988 | -44.4503 | 2025-08-27 03:40:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e58ccdb9-e417-3e09-8bf2-9768afab5d75 | -17.77832 | -44.47749 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83c2779b-5831-331f-a60f-0e975d0ebd4b | -22.1957 | -43.2184 | 2025-08-27 03:40:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 277bb9b1-2377-388f-a990-d8e32fa0a0af | -20.06206 | -42.6128 | 2025-08-27 03:40:00 | NOAA-21 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f04918b2-926f-3fd6-b14d-3faa5440760f | -20.40087 | -46.7261 | 2025-08-27 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d0b996c-2d03-3adb-a10c-930e80351ab2 | -21.58017 | -47.48428 | 2025-08-27 03:40:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ae645895-e839-34a2-bc3a-9a4c055eb1ba | -17.26322 | -44.88472 | 2025-08-27 03:40:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0783faa1-acb3-361d-b170-ce855ae46b98 | -20.99182 | -43.30667 | 2025-08-27 03:40:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 44c420dc-8618-321b-b2b0-b627e8664ccc | -21.1285 | -45.88279 | 2025-08-27 03:40:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 4f4242f5-e598-30eb-badb-5eca683a6764 | -18.28559 | -40.99575 | 2025-08-27 03:40:00 | NOAA-21 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1837ffa4-5fef-388e-b6e5-81fcf39eb1e0 | -17.77231 | -44.48242 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18f7894a-9e03-3cea-8dc3-1740f75cea80 | -21.66278 | -42.34646 | 2025-08-27 03:40:00 | NOAA-21 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6171aa09-34e8-3f10-844b-ee9e6f5e0876 | -18.15578 | -44.42673 | 2025-08-27 03:40:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14013ec9-c900-3c94-b732-47a332deadfe | -17.77369 | -44.47934 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b90b5732-87e8-3eef-81db-b754e0104443 | -21.78942 | -43.29909 | 2025-08-27 03:40:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3ea4b1b0-292c-3b60-8bce-2d3c47484dd0 | -20.04819 | -46.09695 | 2025-08-27 03:40:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cf3302f-f03b-3194-be68-af3a74cc3279 | -21.38365 | -41.99666 | 2025-08-27 03:40:00 | NOAA-21 | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 974d9e3b-1b34-3804-9472-1526f9e335d6 | -20.1164 | -44.33683 | 2025-08-27 03:40:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 82be0bc9-4db7-3c37-9524-0b61aad77111 | -16.74174 | -47.59765 | 2025-08-27 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 386e80da-e8cb-3a81-8b5d-a9d7ce55554e | -19.70659 | -41.67633 | 2025-08-27 03:40:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| df721b17-190c-38cb-b1aa-c0a6a57dabad | -20.11367 | -44.3266 | 2025-08-27 03:40:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e38cab0c-27da-3e67-a03b-e6263611b6f3 | -17.78512 | -44.49749 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4b2f9bf-9159-3fc3-a2f7-14fd46415e47 | -15.09384 | -48.62855 | 2025-08-27 03:40:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 144b54ef-4219-3d6d-a8cf-07263e672c98 | -21.72238 | -46.80847 | 2025-08-27 03:40:00 | NOAA-21 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b5df3a81-5fda-343d-9d2d-5d9e8c83e73f | -19.40237 | -46.15851 | 2025-08-27 03:40:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b523f56d-b51c-35af-8bd4-d64eb3fda6d7 | -17.17423 | -48.68167 | 2025-08-27 03:40:00 | NOAA-21 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92879e23-4ed6-3a88-99f8-75e1c326b8b4 | -20.06348 | -42.60526 | 2025-08-27 03:40:00 | NOAA-21 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 739c9b31-14c2-30e9-8fc8-ffc50fe1ddbf | -21.32347 | -42.81078 | 2025-08-27 03:40:00 | NOAA-21 | DONA EUSÉBIA | MINAS GERAIS | Brasil | 3122900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ad39209b-073f-3bb4-ae3c-c928cff04d2b | -18.83526 | -45.22771 | 2025-08-27 03:40:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a314c16-1864-3dcd-926e-9ec29272612d | -21.36099 | -44.227 | 2025-08-27 03:40:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6d308099-12d1-3f1b-8b0d-cf03897fc6bb | -20.15169 | -44.21004 | 2025-08-27 03:40:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9aa19271-9ba7-38d0-96a7-ef4276935a41 | -18.28941 | -40.99649 | 2025-08-27 03:40:00 | NOAA-21 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| aa688296-83a8-3916-bcb4-1b192e0a965d | -17.25884 | -44.88068 | 2025-08-27 03:40:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 959c2cc1-e130-331c-bfe9-117642102a75 | -17.17304 | -48.68702 | 2025-08-27 03:40:00 | NOAA-21 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94405f9e-3ea3-333b-9348-104d04bab9b2 | -22.68535 | -46.8365 | 2025-08-27 03:40:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e278bd92-a844-35a1-a742-11a16325b094 | -20.48884 | -42.97014 | 2025-08-27 03:40:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3e82f047-f786-3214-a4f1-041906c90f96 | -15.08736 | -48.62707 | 2025-08-27 03:40:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31fe347a-a6c5-3898-9db4-850c68045857 | -22.25653 | -47.51912 | 2025-08-27 03:40:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fbaddd27-6462-3c60-aa26-3b3c1b3c49e3 | -21.00671 | -44.17945 | 2025-08-27 03:40:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 815122bd-b0d2-3b03-9902-b0f311903ea8 | -20.02575 | -45.55423 | 2025-08-27 03:40:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cec243d9-fa0b-38c9-9539-3edfa3e414c3 | -16.91504 | -49.44563 | 2025-08-27 03:40:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a769c9d-52ba-30e1-ad33-7d3c7fa2612c | -21.38206 | -46.93999 | 2025-08-27 03:40:00 | NOAA-21 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 4992ccd6-a850-3c1e-8c34-b074524ed708 | -19.07598 | -48.14575 | 2025-08-27 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 465e3463-8cc0-3643-a320-20d6c0b384f5 | -17.97123 | -48.05431 | 2025-08-27 03:40:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 55acffaa-d36b-31e9-bf5c-be3a32a3d48c | -16.92048 | -49.44207 | 2025-08-27 03:40:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81fb4129-290c-3f41-9e69-a8898f7d28f5 | -18.08201 | -44.05674 | 2025-08-27 03:40:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b02b64a-d0d6-33f6-aad3-af8449dc4e96 | -21.09819 | -48.84746 | 2025-08-27 03:40:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 19a2389f-d6c8-3b7e-adf9-28112ed01034 | -19.90939 | -41.58683 | 2025-08-27 03:40:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 61d5d8ef-d0ed-39bf-befa-a0e5a1081560 | -18.08311 | -44.0611 | 2025-08-27 03:40:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f0bedb7-fee3-34a2-9b43-c23ebfa69cad | -15.66534 | -48.23808 | 2025-08-27 03:40:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c68a588b-3aeb-31d2-8951-5a5bd0d462f6 | -19.0603 | -41.90758 | 2025-08-27 03:40:00 | NOAA-21 | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c0ace454-f36c-3462-a036-829f80f37545 | -17.97712 | -48.05594 | 2025-08-27 03:40:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 37a910e8-a26a-32d7-979b-270313096b1b | -17.55191 | -46.62154 | 2025-08-27 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 763fe92f-cf50-367c-96b7-4774040d1355 | -18.25181 | -45.36222 | 2025-08-27 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fde5e33c-c211-3827-a5a1-ab84ca98f545 | -16.70836 | -50.40928 | 2025-08-27 03:40:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36ee8f8e-0e2c-3375-b186-3a722b0a2c4a | -16.37412 | -43.03865 | 2025-08-27 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ede96a5-658e-308a-8205-c4a9fe8c8420 | -16.94678 | -39.36615 | 2025-08-27 03:40:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 99dcb6d0-3d6d-324e-8dd5-f8a9953d2abf | -17.97233 | -48.04927 | 2025-08-27 03:40:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c6736e81-940f-3752-8fc7-04a7f16d2600 | -17.78036 | -44.49627 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5681b911-abde-3d8a-9483-761719296d3b | -20.98533 | -40.95258 | 2025-08-27 03:40:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d30b9d59-48d5-3948-8d8f-602b5ef92808 | -17.77245 | -44.48564 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 39b9b0c5-2d74-339f-b3a9-113f1f1daa3f | -16.74269 | -47.59323 | 2025-08-27 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d93cf0a4-fcc1-3558-97a6-bb5557dcdccb | -19.0789 | -44.32461 | 2025-08-27 03:40:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27d595ba-89a8-33d6-83b7-54929ed7507e | -15.08856 | -48.62521 | 2025-08-27 03:40:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51e2fd15-2757-3b70-9960-aeca6165bb26 | -17.31651 | -46.59958 | 2025-08-27 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6a78b51-b393-3038-939d-306cf1adb46f | -20.51825 | -42.27036 | 2025-08-27 03:40:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7fc7ee99-cc0d-3f73-a01d-200c6fdaf567 | -17.78836 | -44.50177 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65a2f88d-7d67-3840-a1d0-da53d7fcf120 | -19.08006 | -48.14542 | 2025-08-27 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f42fa49-7ac7-3311-b509-0f616d1facd4 | -17.55487 | -46.61065 | 2025-08-27 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff6412b5-38d7-3cc0-a50a-c13789e0480c | -20.50423 | -42.22367 | 2025-08-27 03:40:00 | NOAA-21 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 1d68dc8a-840b-354e-919b-369651e6dbe1 | -20.39807 | -46.71365 | 2025-08-27 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90ab244d-bcde-3a23-9456-aa624d7b07ad | -20.40011 | -46.72958 | 2025-08-27 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README22.md)
