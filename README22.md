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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb8584c9-115a-31ec-a06e-f6e57542045f | -4.5616 | -47.9925 | 2024-11-19 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b2f5da88-83a8-38a8-bc23-d32017d703a2 | -23.95 | -54.1191 | 2024-11-19 04:20:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| 5afd4f60-b157-3574-af59-a23d25ed3583 | -4.5613 | -48.0358 | 2024-11-19 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| b1df6ccf-16d9-3f3a-927a-79cc00293fe4 | -4.5614 | -48.0141 | 2024-11-19 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 165.0 |
| b5253057-4ce7-34db-a9ab-f206c05f4866 | -23.9706 | -54.1372 | 2024-11-19 04:20:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| a3a2ceda-762d-3eed-bdc9-780d140977c9 | -23.9711 | -54.1148 | 2024-11-19 04:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 87.8 |
| 813144a9-dd12-3f54-a1e5-3b886674adbe | -5.9788 | -45.3621 | 2024-11-19 04:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 809aba59-7ed0-3bc5-87f6-e8c1ae88aae5 | -4.5429 | -48.0151 | 2024-11-19 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 50128499-f1c9-3eaa-97c0-e312d6962f93 | -1.424 | -52.4368 | 2024-11-19 04:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 51186ecf-e8ed-3390-9f40-23b2c249bd4d | -4.5429 | -48.0151 | 2024-11-19 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| a8031c80-a9cc-33d3-b6da-89449c94109b | -4.5616 | -47.9925 | 2024-11-19 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e9904a98-cf8b-395f-95d1-372b3cfd0c73 | -4.58 | -48.0132 | 2024-11-19 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0b5eec58-f236-3480-987a-330d667745b8 | -4.5614 | -48.0141 | 2024-11-19 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 18f52fd5-5c8c-3c2c-8c56-06c2940059c3 | -5.9788 | -45.3621 | 2024-11-19 04:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| eb2e1a6d-9098-38de-b4fa-d872fe4fd12d | -3.5126 | -50.2133 | 2024-11-19 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| b71ba90f-640c-3c63-9c7b-57f7a32f5eaa | -4.5614 | -48.0141 | 2024-11-19 04:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 10bc4825-da1c-3c90-91c1-7e0ffe5ae993 | -5.9788 | -45.3621 | 2024-11-19 04:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 460cef43-9b26-3679-8f83-daf1e8e63c05 | -23.9706 | -54.1372 | 2024-11-19 04:40:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| 00cfe7e1-068f-3897-8d78-5bc90a0d27f8 | -4.5429 | -48.0151 | 2024-11-19 04:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 984b5c60-cdac-3601-b63e-c3bd724518bb | -1.424 | -52.4368 | 2024-11-19 04:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 42bbb91c-b7b7-3753-9285-35aa2b67e480 | -3.5125 | -50.2343 | 2024-11-19 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| f65dd2c1-8c7a-3e54-99f4-6cad302d75bc | -4.5616 | -47.9925 | 2024-11-19 04:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 1f517206-1037-3369-be3d-a7bfa4f903d1 | -4.58 | -48.0132 | 2024-11-19 04:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b045313c-a8f4-3f9b-b2fd-a0428932c74d | 2.58545 | -50.85059 | 2024-11-19 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5240501-e5f1-307b-adc6-bf4308ecb321 | 0.97122 | -50.19924 | 2024-11-19 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2155a2ac-8dfe-3230-9640-e684098cee1d | 0.85116 | -51.37106 | 2024-11-19 04:44:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dc50ea3-fbaf-3a7d-83c8-dfd1b120705f | 0.6356 | -50.57804 | 2024-11-19 04:44:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffbb2d53-0816-3e4c-b57f-02c34d6d259d | 0.69435 | -51.44323 | 2024-11-19 04:44:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac8a747c-6a82-37a8-af19-9623f373af85 | 0.63893 | -50.57754 | 2024-11-19 04:44:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb98c39b-5db0-3cbf-9af4-df531c65358d | 0.9044 | -50.14253 | 2024-11-19 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf6794a9-0e64-3c56-bf6a-f7fc85e8695d | 2.586 | -50.85421 | 2024-11-19 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03bc749a-2e99-30e5-af5f-e6d8a9a5395b | -2.75344 | -54.06422 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c6f7ab96-4d04-3308-a710-0347c1dda028 | -0.95067 | -51.72443 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30f75264-8b12-33fd-9ef9-5b6cf5b8162d | -1.38106 | -51.5582 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23e73491-7819-3ff1-a315-e2713d1267b5 | -1.34626 | -51.39269 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b48287b6-c086-3ff7-bdb9-adec5b908214 | -1.70637 | -52.14431 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 598a1547-a63a-39c0-b616-cd6480d144b2 | -1.04559 | -51.74633 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad27ca22-fd03-3426-9cf3-74be903509ad | -1.40118 | -52.61681 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d2e77cc-a8c1-3378-944c-d51e17592a55 | -3.99543 | -49.91368 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e40aead6-b6ce-315e-b7a3-79ebe8afb495 | -2.45002 | -53.68654 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ef81b3f-822a-3dc5-adc9-98e5947cdb85 | -1.70295 | -52.14378 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77bdd859-e996-3752-a6d2-a82f5a31c465 | -4.52792 | -50.66582 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fea8d11a-164b-39a9-a8e5-48482989a5d9 | -2.31808 | -45.64958 | 2024-11-19 04:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f87866c-c2eb-3549-b3cf-bd76cabada67 | -5.95311 | -39.67318 | 2024-11-19 04:46:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b9cede12-457b-3a4b-b4d5-3e86903a996b | -3.29656 | -45.21393 | 2024-11-19 04:46:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 054b1dc6-f412-3951-b3ff-79a36c71736a | -0.34126 | -51.4679 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20de8dd0-8697-36fe-a25a-29cb757ef545 | -3.36504 | -54.10712 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 145f0593-8f2e-370b-b932-2e8ad3ff15d4 | -2.95081 | -48.32204 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fc9f135-48c3-39c0-a3a4-16beb29e32e2 | -3.49513 | -51.68084 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d90ee150-1afb-3b35-a5ce-a70142e024ee | -3.86249 | -52.32262 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fec7bd6-4001-3a24-8a91-0bd155fb4a1a | -0.93722 | -51.63338 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d81c22e3-9e74-35a1-865c-11ecaf34b6a3 | -2.99936 | -51.45906 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8326caa6-6ca2-3545-a215-14c2e60cf9df | -1.20782 | -51.76047 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e386457-97f6-31af-9f4d-5ef490f080c9 | -4.19649 | -50.89616 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea97f136-f336-378c-a10c-6d49b7f96c08 | -1.62589 | -53.29488 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 826d3381-ac02-3129-a113-762583f54334 | -2.53994 | -47.33407 | 2024-11-19 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7f17001-8c51-3fa5-9681-5d02af643c33 | -3.77046 | -50.15938 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3578f8aa-9bc9-33e5-bd6b-3a0a2da5d084 | -1.19864 | -51.97971 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64137eeb-dac7-334f-8d38-0f8563756991 | -3.55241 | -51.53163 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4417fe2-b5c0-3e96-aaba-a32dea078654 | -2.85973 | -51.8463 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 163a3dd5-4c27-3d96-9076-f88ff37f1b80 | -1.22927 | -51.78594 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac8374b5-22fb-31e2-80c9-4634fbb57ecf | -1.24519 | -52.03977 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 327b279a-fa1d-330b-867a-922ea59ec57a | -3.09959 | -51.31741 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d30e4912-6097-359e-9aa6-cf16594fdc45 | -3.49579 | -51.17778 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 046956d5-d1f9-3e80-94ea-2bb39cff466c | -2.92951 | -49.11574 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5afbf493-6cc0-37a4-b4b6-184d2fa9e337 | -2.3471 | -53.90834 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40541c97-3cd6-3839-aa95-1060c54788c3 | -2.5701 | -48.0364 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52161a63-2c09-35a1-8211-6e82dcccacac | -7.47331 | -47.17942 | 2024-11-19 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58a92050-3940-308a-a495-11dafd54e26c | -2.73761 | -54.1158 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e5ec066-49f6-3422-90ca-e8f3ade0125a | -2.75692 | -54.04239 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a17c88a-3adf-3589-90bc-d49a789f474b | -1.58701 | -50.4402 | 2024-11-19 04:46:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 137e4628-af6f-37e1-ad42-0d9597387eb8 | -3.30131 | -51.05145 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f18fac7e-c9cf-3d91-9051-ed24baedc23b | -0.29721 | -51.55 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64666bd7-ad00-3b61-8dbe-3c0b4446ccb5 | -3.14102 | -53.91352 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72f6cfd0-0521-30b5-addd-725eb6713d08 | -5.45685 | -46.56036 | 2024-11-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93a101b8-0987-304d-9ec2-18ab75ed6654 | -1.13562 | -51.69003 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52968c65-b580-3db8-8dff-20b07b3de97e | -4.56026 | -48.02113 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1edaa9c-6ff8-3374-b6b0-54584146847b | -0.01213 | -49.95895 | 2024-11-19 04:46:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34caa214-47cd-390b-b67e-b09fdb5cbaf8 | -1.45355 | -52.34268 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c44d53c-11fd-3e08-8039-eee9cbed1406 | -1.78967 | -53.59221 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e33497c9-e90e-3d4e-8711-96e7193a96fe | -2.7649 | -52.59964 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe4ff662-60e0-37af-beea-267f976489a8 | -2.76431 | -52.60339 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a17c966b-136f-396a-9da4-abca7dce6b4a | -1.70236 | -52.14748 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4032bfb3-2ea6-3ba2-9311-889170e51928 | -2.35418 | -48.94008 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6652f3e7-f321-3056-a1ab-f0ab9f882cb4 | -6.3388 | -46.3733 | 2024-11-19 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6252aa1d-41e4-35bc-ade0-1050de0f3411 | -4.58311 | -48.49293 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1a4293a-bf0d-379d-9328-31a2d501270b | -1.62553 | -52.61855 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 093b40e0-6e5e-3645-92a5-e97a77181507 | -0.1196 | -51.42688 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daca1e86-8cd2-3261-9c85-70f0fc78e11e | -3.77288 | -51.037 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 423e7a57-8620-3ac1-9712-f9ff6c815e74 | -3.88172 | -46.429 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fefd10f3-7364-3792-8068-8d6082901a8d | -3.66486 | -50.44287 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4d60d17d-72da-31a7-82f3-13b414cae313 | -3.9877 | -49.91963 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eccb5665-c64b-3bd6-bc36-30d6e1fe0dbf | -0.9406 | -51.6339 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8758f19f-15f9-3b54-a493-bf492981363c | -1.24989 | -51.61162 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12bce3bb-36cc-3578-922c-32f76bafb826 | -6.8825 | -45.48462 | 2024-11-19 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28ebb6a7-6a8a-348a-ac5a-1061d8906ea3 | -3.82282 | -52.25736 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77b25099-6279-31b6-8eaa-c3e6eebf6a8f | -1.64993 | -52.76915 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a342b6c-d63d-3d8d-a4cc-1c1226685346 | -1.62145 | -52.48454 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e36bec14-7a06-3099-9d17-5664347fa550 | -3.33411 | -54.06757 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98206ec0-0000-36a9-9c8c-1a1b29f8067a | -2.59295 | -51.72815 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README23.md)
