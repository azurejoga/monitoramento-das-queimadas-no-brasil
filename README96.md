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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 285cbf0a-fcf3-30ee-bec1-983832a36102 | -11.40679 | -60.39994 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61e910fd-d581-3462-9a23-83793ef844a3 | -11.40624 | -60.40344 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a34b3c4c-93ca-326f-afe1-fd333575159d | -11.40568 | -60.40695 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad762165-0b52-33e6-b550-1820eb3dab63 | -11.40512 | -60.41046 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9724458-6e7c-360f-9812-c643f85994c5 | -11.40404 | -60.39591 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10d06bd8-1d37-3283-abd1-7fe232c1016a | -11.40349 | -60.39941 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09e437af-83dc-395a-95b9-41c100de4abd | -11.40238 | -60.40642 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10e54e45-b132-3716-9012-5c8d1cfaa356 | -11.40182 | -60.40992 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 931087fd-7692-32e3-9dcd-3954682793f4 | -11.40127 | -60.41343 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71ae3b3f-5034-39c7-ad94-4b80e67d8072 | -11.40071 | -60.41694 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0eb9d66c-42a8-3452-8d7e-8c50cfccc6db | -11.40018 | -60.39888 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dc4d770-b528-3f5e-b2de-9cf61377f62e | -11.39741 | -60.4164 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaa5999a-5bc6-3286-bcb7-e43b9861c9f7 | -11.39685 | -60.41991 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8c41c79-4acd-37d7-a924-6199278f5524 | -11.3952 | -60.40528 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13de946d-a0f7-3026-85ef-83933f3ec039 | -11.39354 | -60.41578 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 851a458a-6653-3cb6-a12b-3447c8706620 | -11.29881 | -60.43638 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebca6682-b84d-3e1c-90c8-7b2ae648d448 | -11.29826 | -60.43989 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d44b3d7-8164-3fbc-9c81-a112089828d1 | -11.29551 | -60.43586 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 095530b6-ab8a-39ce-9315-2e21a0b59a0a | -11.27805 | -60.43655 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0aa915a8-2e5c-339a-ba72-066c3ba681d7 | -11.27369 | -60.37836 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c3a10c3-edd7-3486-9c2c-9499417d945b | -11.27257 | -60.40692 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e4b875b-3c01-3472-815e-081bd0cbcebb | -11.27201 | -60.41043 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e1661bc-a702-378a-899c-1c9e220519ac | -11.26926 | -60.40638 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0bbb9fa-f372-39de-a8aa-f91b2b153cf4 | -11.26871 | -60.40989 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0809ee73-caaa-312f-8987-72f5354ce236 | -11.26541 | -60.40936 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44d0f99c-3481-375b-b533-464e934c48ad | -11.26266 | -60.40533 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 737ad844-563e-351f-9692-404543564b23 | -11.2621 | -60.40884 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2713b1d-f5c5-390c-97a8-b8acee9c3ad2 | -11.2588 | -60.40832 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdc7e148-d752-3825-854a-c99517237511 | -11.25605 | -60.40428 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07139611-b025-33a3-ba65-cb377fa24c9a | -11.2533 | -60.40025 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b1727b2-55a3-3747-bb6d-63425001f909 | -11.25274 | -60.40375 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96e6bdfb-fc57-3535-a3d8-7817bfa79d39 | -11.24999 | -60.39971 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fb27117-c0af-335a-9ce8-02d10e987b82 | -11.24115 | -60.4342 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af60c670-2d13-3913-89ec-844eaa8e7953 | -11.23137 | -60.23887 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5a878e2-2aff-365b-82a4-444085a7ac27 | -11.21542 | -60.23271 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 140a19af-ca7f-3229-9926-5fb09c337f67 | -11.21487 | -60.23621 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7501b7c-11e9-3ecf-a3d7-5857c09eca07 | -11.18607 | -60.43966 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7e4ecc9-5273-3f89-9fd4-a0f40f049300 | -11.18551 | -60.44316 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04ece707-dcd5-3bbf-97d5-d83ce3fc076b | -11.18221 | -60.44263 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 146a940b-020f-3dbc-a227-5c75e1c75baf | -11.17887 | -60.46365 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b76940ac-7c17-3e47-96d0-59cb0060ab99 | -11.17834 | -60.4456 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ba209e9-94d0-386a-bcf9-b960aca2f8e9 | -11.17779 | -60.44912 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 721dd303-5f9a-3cd1-94db-24108de8eeea | -11.17668 | -60.45612 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c739bcf5-022a-3a73-962d-fd1da77f05dd | -11.17556 | -60.46312 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40e87faf-65fb-3faf-b83d-952119afe1c2 | -11.15709 | -60.23357 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19f2dbef-b086-3f17-99f2-d8cf11d6c42f | -12.14829 | -60.74525 | 2024-10-11 05:21:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1184a334-710d-33a8-86d7-d3ee9d62fb29 | -11.35044 | -60.55983 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a50e390e-6759-3f30-b29c-52d983d7c99f | -11.34989 | -60.56334 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89f8dd68-2206-37b3-94ad-80d684cc5ff7 | -11.34658 | -60.5628 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92ca128f-cbcf-3128-bb39-be0c584e6d48 | -11.34603 | -60.56631 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b93db2ad-6024-3710-97f0-edb7b8798301 | -11.34328 | -60.56226 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd3da77c-06a1-370a-b483-9617c679581a | -11.34272 | -60.56576 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a90bb6c4-15c8-38d2-8b29-1157c7efb81a | -11.3345 | -60.53204 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 815cf286-ad53-3c33-a53a-0b3fded1eb81 | -11.33394 | -60.53556 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8eeb3cc-f68b-3c82-944d-0ad2968dccd9 | -11.33339 | -60.53907 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4d48a12-440d-364d-a13d-6f5a9cd134a2 | -11.3312 | -60.53151 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e6bb0d45-0cea-3bc1-b9b7-d0414f649f0b | -11.3036 | -60.55581 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04ed0db0-4b20-3036-b669-f291b8a095f4 | -11.29643 | -60.55826 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db4c3e43-ef9d-3536-80e6-38809e136aa1 | -11.29145 | -60.56825 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88c4c816-ae86-3590-9a9a-bfe9f4ea4a3e | -11.2887 | -60.56422 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcb32860-0255-3e0c-b3cc-89b78d2a8acc | -11.28647 | -60.57825 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d055788-2722-36c4-b3c4-99f062d95de2 | -11.28113 | -60.4838 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 144b5a95-1a02-367d-80e5-b3accc3f1dd2 | -11.28058 | -60.48731 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b114eaa7-0490-3a98-af90-764200ddb8fb | -11.28002 | -60.49081 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c212dfea-e54d-3d46-a221-a18afb079782 | -11.27946 | -60.49432 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a616cd6c-3a84-3c8a-8b3c-e9900ac2235f | -11.27783 | -60.48326 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4abfee29-416d-3af4-afb5-d60888dd5907 | -11.27727 | -60.48677 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7bd41e3d-4983-3215-a4a3-92de40127f8b | -11.27672 | -60.49028 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 617bb31e-61b5-3e20-89f8-5026c498bc25 | -11.27616 | -60.49378 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad59cb5f-32b2-3328-b053-e1a7f0d412da | -11.2756 | -60.4973 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf8532cc-cddf-3f47-9764-b566f045d5d1 | -11.27361 | -60.48612 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b889b6d8-5a1b-3931-a506-bd9b1d5c3b2c | -11.27306 | -60.48962 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f67e418-3c39-3bd2-8ad4-3227ead75953 | -11.2725 | -60.49313 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce8e422d-2c6a-3622-9ad1-c7dd54632ef8 | -11.27195 | -60.49662 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3463d427-e407-33bb-a51a-fb4c8254a657 | -11.27139 | -60.50014 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f12cb046-ed07-37b9-881d-ed77b5ab39d1 | -11.27031 | -60.48559 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32ce266b-4c0e-34ea-a092-d2fe0b0b8245 | -11.2692 | -60.49259 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae8d43c3-6df3-3c25-9328-97e7e1dfb6bf | -11.26865 | -60.49609 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8aca9d5e-80f7-316a-a074-7e737042678e | -11.26809 | -60.4996 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ed3fd8a-6d1a-38a3-9f30-a507fa6ce886 | -11.26754 | -60.50311 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dcad536-08a2-3a7e-898e-c01f13b5b185 | -11.267 | -60.48505 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae4d028a-2c29-3667-9c6c-f00475072e92 | -11.26589 | -60.49205 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0be3a4a1-55e8-36e6-8e9b-c238a83d33c2 | -11.26534 | -60.49555 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e47f3a6f-abcc-32e4-8824-d2fef18741ed | -11.26479 | -60.49906 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6d12943-b1a9-3766-90b8-c0c218ec69ee | -11.26423 | -60.50257 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 799d2fd3-35f9-3b89-a758-3bb481866149 | -11.26093 | -60.50202 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90437a8b-266e-3f67-9021-f1b2cca7a37c | -11.26037 | -60.50554 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbbf4915-a836-3bce-a86e-3b32c9893bcf | -11.25707 | -60.50499 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4d641c8-32c7-3108-b48d-d974356bee2a | -11.25646 | -60.55173 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a00ee678-c55a-3ae1-bcf7-4430a96f49b1 | -11.25591 | -60.55523 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94e1457a-4996-3beb-99c0-61ac13462371 | -11.25376 | -60.50445 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9672a8f-8bb6-3b90-be62-f08aa338d21d | -11.25315 | -60.5512 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c91ac2e3-1c42-31aa-99cb-721c2172438e | -11.2526 | -60.5547 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a516f041-5d62-3f72-8dc1-af43e3480de1 | -11.25148 | -60.56174 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d10d10f0-6e19-3f0c-986b-217b49bd26b0 | -11.24873 | -60.55769 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 842e9acf-bef8-3c1d-80c8-f3c43efa3265 | -11.24818 | -60.56123 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2eefd4cf-b390-3929-a517-8757d4b3cdd3 | -11.24762 | -60.56474 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cf77c2c-9679-3633-914c-200e31cf1054 | -11.24376 | -60.56771 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdc62b4d-7a1f-381f-98eb-b88df4083aee | -11.22777 | -60.56152 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 776c29c2-7c44-3134-9203-80e4f278d50c | -11.22499 | -60.57908 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README97.md)
