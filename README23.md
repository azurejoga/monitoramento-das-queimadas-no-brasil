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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8410067-6749-3334-8a85-13e5a3f8526d | 1.05822 | -60.59523 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6496a1bf-49c4-3b6b-a204-a443c3aa86d0 | 0.62008 | -60.08752 | 2024-11-12 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 172ec2bb-60cb-3f3b-bc78-c6867b95b28d | -2.12803 | -50.69648 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2898e39b-6957-353e-bdfb-73b89c1e8221 | -2.12909 | -50.68964 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e92c4a95-59ca-3ab6-8842-908a28e502b6 | 1.08747 | -60.59479 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4276707-e840-3b3b-a9ee-339266cbea9b | 1.05171 | -60.60037 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d55f1bf-ba35-3832-8660-89d310246fd7 | 1.13877 | -60.59499 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf193c81-dedf-334f-aea7-c20be7a7335a | -2.13264 | -50.69594 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07197382-a506-3467-b749-2a431f44e2b0 | -2.629 | -54.28966 | 2024-11-12 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93f5b92b-1893-3d4d-a46a-3efdf783eda8 | -3.34173 | -53.21309 | 2024-11-12 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fdb0986-c2c3-37b7-b12d-36e0d893c6e8 | -3.52892 | -54.08588 | 2024-11-12 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b272959e-85eb-3065-b44d-2a86db897363 | 1.06244 | -60.59872 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c44b1bc6-8431-35b2-9970-b869c5910e35 | 1.05757 | -60.59118 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a545533a-cc80-3e52-b289-90526a9fe21a | 1.13748 | -60.59577 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6eba400-3abe-3627-8791-381878675c70 | 1.05464 | -60.59578 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b71743b3-d39f-3f27-ad70-2922c16a8807 | -2.1185 | -50.69375 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8221a321-afea-3e32-a101-9d73e9cb4221 | -3.09592 | -54.29962 | 2024-11-12 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bffd0ab-efb7-3179-89f8-d1fb52239423 | 1.52566 | -60.67455 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3f30127-011a-3164-9a0b-ea1447afcdee | -3.34331 | -54.18603 | 2024-11-12 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5afdf1f-9f0c-3e30-9c03-fc340c1f74b7 | -2.12096 | -50.6954 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9b4fc756-6633-30ba-ad9b-7dcc4e0db38d | -9.3593 | -61.99349 | 2024-11-12 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12a6b558-5d48-3cb5-9628-32b9e721bba7 | -9.85282 | -62.14859 | 2024-11-12 05:42:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86db468c-6506-33f5-9a57-b0570aa72802 | -10.52289 | -67.79546 | 2024-11-12 05:42:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f60d1d4c-0ec6-309d-9f41-725666dda0c1 | -9.51593 | -63.45306 | 2024-11-12 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17831a72-03ee-3f35-9c0e-c98c6dfb3471 | -8.79842 | -63.24514 | 2024-11-12 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fba55f28-0a36-3ac4-a966-b056f8e424c7 | -9.17072 | -63.2093 | 2024-11-12 05:42:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db7955b9-59a7-3f0e-90db-3b740b02f520 | -9.36732 | -61.82971 | 2024-11-12 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93f5f766-9575-35a4-b80b-21fedc3a7b84 | -9.36883 | -61.82787 | 2024-11-12 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9fcbb56-41cb-336d-a4b5-b7f3e9d1b1fd | -9.16416 | -61.68991 | 2024-11-12 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59c0609b-203a-33fe-a92e-99efa11b302e | -9.16719 | -63.20877 | 2024-11-12 05:42:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a97a023-daf9-3941-a384-13dadbe96046 | -8.7399 | -63.49013 | 2024-11-12 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2366fc1b-4748-3bb1-91e7-0e7e3513b33c | -8.74048 | -63.48629 | 2024-11-12 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62d144de-d6b2-3809-893f-8c4829c18eb1 | -8.99244 | -62.10358 | 2024-11-12 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80b3a405-65f0-31ba-84fc-251a90f845ba | -9.51243 | -63.45255 | 2024-11-12 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05051bb9-305f-3ae4-a3b4-7d26f4ff19eb | -8.99617 | -62.10413 | 2024-11-12 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7cb80d3-33f8-3f0e-bb7a-9b363b7e4ca7 | -9.36503 | -61.82731 | 2024-11-12 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ae0156d-1779-3a81-9297-065badd19272 | -16.00749 | -59.37272 | 2024-11-12 05:44:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca0aab3e-8377-3856-a0de-822b73d1d50a | -16.00463 | -59.3774 | 2024-11-12 05:44:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e704500-15b8-36f5-992e-c6b1d026401a | -16.08485 | -60.10539 | 2024-11-12 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e39b674e-e187-3ecf-b689-4d5a28b110ca | -19.4652 | -56.74313 | 2024-11-12 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d7906dc8-4040-3d77-8465-2bd26b0b7c93 | -15.99482 | -59.37629 | 2024-11-12 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a398b9ff-6b59-3835-9bc5-00498d0d49de | -16.08952 | -60.10601 | 2024-11-12 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de4282bc-82d5-3446-9e36-6c6f90629915 | -16.94367 | -57.64603 | 2024-11-12 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0d1ff9f2-1b77-3075-a3fd-8e59e3766d8b | -19.45871 | -56.74718 | 2024-11-12 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 47a136fe-c1d7-31ff-8a42-a2712caeeea5 | -16.0889 | -60.11104 | 2024-11-12 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f8f1134-36e9-34c4-8190-84686cdb03a7 | -16.00192 | -59.37794 | 2024-11-12 05:44:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 151e3440-99ba-38ab-a48c-a05181a8974e | -15.99972 | -59.3769 | 2024-11-12 05:44:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5df72db7-933e-3c12-97d7-e5048bdb72a9 | -21.32156 | -53.92561 | 2024-11-12 05:46:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 593a8433-05b4-30b1-9e9d-930d3c633fef | -21.31427 | -53.92524 | 2024-11-12 05:46:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d648451f-018e-31a7-9b83-698c38eba1b6 | -3.1096 | -54.3066 | 2024-11-12 05:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| b4193131-63ed-3f72-a455-873a977d990f | -3.9668 | -48.1932 | 2024-11-12 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 38b72427-6bf4-33cc-a8d1-c069da489214 | -3.1097 | -54.2865 | 2024-11-12 05:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 8acc22f4-ac4c-3ae9-b207-d5eb9a4b346b | -3.0504 | -50.3332 | 2024-11-12 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| bb84e1a3-c72d-3fbf-b78a-dad9fbd304d7 | -2.1087 | -50.6916 | 2024-11-12 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 126eae57-1e4b-31cd-bd35-b91373711699 | -3.9669 | -48.1716 | 2024-11-12 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3242b8a4-2cfc-3b2c-bb71-eae642d06e79 | -2.1271 | -50.6912 | 2024-11-12 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 6b5d9d89-e63d-37d1-8c9b-75be132eb489 | -3.9482 | -48.194 | 2024-11-12 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a9a91ee5-61d3-3227-89a9-bd0ad7d945d8 | -2.1271 | -50.7121 | 2024-11-12 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 3afeed82-fffa-3718-b0f2-cd969b773cf1 | -3.9483 | -48.1724 | 2024-11-12 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 56270074-1b9c-39e2-88d4-e866335a67ca | -2.81788 | -54.71353 | 2024-11-12 05:54:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ea134747-2f77-3c89-accd-93bf77a0cbc9 | -3.67257 | -50.21412 | 2024-11-12 05:54:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 38cca316-b0bf-3264-bd77-70e5a57f8662 | -2.32383 | -50.67639 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| e32ee544-120f-3eac-9993-e53cc7cc188b | -3.05984 | -50.34237 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 552a46c7-4aa3-3cb1-9344-5a35646a859b | -2.05815 | -52.08071 | 2024-11-12 05:54:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9989bbbc-554b-32e9-989d-f91cb0308c59 | -3.26585 | -53.69765 | 2024-11-12 05:54:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9f3af18-593b-3628-9fab-76b684678391 | -2.12898 | -50.67982 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 31782b1d-cce5-359f-bdc2-ae4d5449963f | -3.28645 | -50.04851 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1a4aa83f-c1d1-366d-9321-92452453d227 | -4.42775 | -49.7115 | 2024-11-12 05:54:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 49df815d-c778-31c3-a021-3a0c31fdc2e2 | -2.32492 | -48.42614 | 2024-11-12 05:54:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 66cfd285-66c9-3296-846f-6e5e83c9289e | -3.79422 | -50.08838 | 2024-11-12 05:54:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 9d981419-c155-3d12-8319-4992734fd30b | -3.43412 | -50.30136 | 2024-11-12 05:54:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 41e023aa-8285-3a3b-980a-541e8ac514b3 | -3.11121 | -54.30605 | 2024-11-12 05:54:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 48bfd2f3-7436-3014-a1e5-05a9982aef67 | -3.63268 | -54.7035 | 2024-11-12 05:54:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b9f0d59f-1fbf-358e-9238-910326666487 | -3.79241 | -50.10068 | 2024-11-12 05:54:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 563b922f-e8f1-34a9-9f9f-2bfad3dbb3fb | -3.2486 | -50.31058 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8ca2be67-fe48-3738-969e-ead389e912da | -3.10367 | -54.29583 | 2024-11-12 05:54:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 9ee1cbc6-7936-3ff0-a7f8-1f455e100457 | -3.05147 | -50.32932 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c132b993-abf1-380a-a8fa-058bcb8ea225 | -2.76817 | -49.33187 | 2024-11-12 05:54:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 12ebfee6-738b-3933-b61c-b47ff3f44bdc | -3.74902 | -50.18155 | 2024-11-12 05:54:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e17e809c-bd54-354d-9fc7-24f0e8cdacf0 | -2.13707 | -50.69188 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 91c5a35b-6ca6-3efd-8c19-17f54a3aa0cc | -2.32223 | -50.6871 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d9fac776-218a-331e-a943-2005eef6ee82 | -2.12579 | -50.70116 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4e4fff95-9920-3aeb-907c-3b9308671167 | -3.95933 | -48.16352 | 2024-11-12 05:54:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ba7d611c-6543-3bb9-bd10-cde125818e2e | -3.66234 | -50.21265 | 2024-11-12 05:54:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 30cfdf65-c5ef-3587-a3dd-1f649cfb7e8e | -2.1177 | -50.68911 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| abfe0f10-416d-32a1-9c18-d2924f6d138b | -3.16809 | -50.4454 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4de35d32-1d45-3019-8ba2-d0601b537802 | -3.06152 | -50.33078 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 507e310c-bec1-339e-8586-da7114811aaa | -3.10233 | -54.30474 | 2024-11-12 05:54:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 6e61f725-6bcd-3256-9220-9782a19baa59 | -3.44425 | -50.30282 | 2024-11-12 05:54:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a39dd7df-d47b-33c6-b786-38808d8b31a8 | -2.73227 | -51.82843 | 2024-11-12 05:54:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f7cd901f-4924-38ca-8a66-7f75e723d91d | -2.62477 | -54.27953 | 2024-11-12 05:54:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| af240f0c-220d-3fa0-b205-dfcfbd35902f | -2.79169 | -54.03524 | 2024-11-12 05:54:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b88d6e2-7c15-36b7-a238-62149f86a13d | -3.2906 | -53.66309 | 2024-11-12 05:54:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 029c0634-5448-3d4c-8180-6830025705c4 | -2.12738 | -50.69049 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 2bc34990-4c3c-39fc-ac60-b7671d69a6c5 | -4.42587 | -49.72482 | 2024-11-12 05:54:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f590188d-ff18-3182-8b43-bcc09fa45682 | -3.95684 | -48.18083 | 2024-11-12 05:54:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 87730bb6-0e82-3ad5-9f72-0d9714320a32 | -3.06319 | -50.31924 | 2024-11-12 05:54:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 56f01f6d-e9a3-3b74-b973-3196a56b7049 | -3.11256 | -54.29713 | 2024-11-12 05:54:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| e9997ba7-bab1-3ca3-b9b8-b5ea78a301c0 | -3.41391 | -50.37008 | 2024-11-12 05:54:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 46ba29bc-4072-3fb7-abe9-a43d436d4471 | -15.30699 | -56.50008 | 2024-11-12 05:57:00 | AQUA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README24.md)
