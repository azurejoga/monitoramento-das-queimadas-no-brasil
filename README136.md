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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35335b2c-ee1e-3a88-a4cf-e60d50bb6801 | -9.87977 | -64.81812 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d2adec0-32e9-3193-a3a7-714422cc62bd | -9.8 | -64.47095 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9390083b-aabc-3dd4-9478-5a7042b037be | -9.79363 | -65.05325 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0e4d2e3-b2a7-399f-8699-e048d0efa262 | -9.7934 | -65.05573 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25ec4b94-abdb-3603-9f52-50fd3f22b548 | -9.79284 | -65.05782 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd87ef1b-e6a7-37ec-826f-0a32f8575fa4 | -9.77461 | -65.05241 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eca1089-4c45-34b7-b3e9-dd67392a4c82 | -9.64872 | -64.94872 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f19f2b3b-e259-361f-812c-d161d69a39a3 | -9.5654 | -64.62091 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ab4defc-f533-37b0-bfcc-a84fa78d354d | -9.56467 | -64.62524 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7253c30e-1273-31f3-bf3d-d4c2d9c4c776 | -9.53994 | -64.57722 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cab897f6-1aaa-3c6a-86e3-5931786de347 | -9.53627 | -64.57658 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd9acb55-bb8d-37ad-9322-4f59252d43f5 | -9.49452 | -64.66837 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37fea612-4126-33d0-be25-486c6ee64cfa | -9.49082 | -64.66778 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68e53341-dfb0-3d99-a1e0-d72e648bcaf1 | -10.06175 | -64.93262 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee0b2425-f400-3457-9e45-26964e30a55c | -10.06099 | -64.93712 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c05a1c9-19b0-3df0-9129-03702077d765 | -9.6474 | -65.73927 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7d638bc-0fe0-3305-b88d-ba72633a542e | -9.64347 | -65.73859 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 392b6150-4520-3af9-9b7d-ff86c7dee227 | -9.40392 | -65.59024 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37f27434-9e5a-357f-80cd-8e1b0e0d1ee2 | -9.36144 | -65.74267 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d661634-92e4-3875-8b2c-ba3b1db6c8b8 | -9.36137 | -65.7501 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3c46bc57-6674-341e-bffb-0ea149d4d4e7 | -9.36057 | -65.74765 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d60453a-95c7-3514-9b53-6ca517722374 | -9.36053 | -65.75515 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f91a060-6375-3209-9379-32024ac050e0 | -9.3597 | -65.75267 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1061ed7f-930e-3036-8c9f-4eebf0cd4b86 | -9.35909 | -65.7394 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a5aaedb-38a2-3169-b15e-9c458a866820 | -9.35826 | -65.7444 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bc3e6f66-72ec-3399-a874-e12c8e39d9ba | -9.3575 | -65.74198 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70caec4d-4333-3f4b-a0cc-fb128776603f | -9.35742 | -65.74942 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 44055dc7-7618-3d4c-8cc1-1e920e5ea7b4 | -9.35663 | -65.74698 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fb473fa-1cc9-3734-a076-72d06f4be828 | -9.35658 | -65.75447 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7de63d6e-d2a0-3454-9843-c069f7e4d630 | -9.35576 | -65.75201 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cd7a9a1-ab18-38ef-8d95-81770bd15acd | -9.35432 | -65.74372 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ce9fb42-87eb-3e6e-89c0-d0d0b2d2b7f9 | -9.35356 | -65.74131 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c03344fa-e171-319a-b31c-3376e0c322a9 | -9.35348 | -65.74875 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d39632b-c04f-3ee5-9531-6154b3822f2e | -9.35269 | -65.74631 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7bbbede-6387-351b-bdb9-5dd3fc23ccba | -8.61743 | -69.73137 | 2024-10-12 05:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5c11df5-dd09-3557-8519-5d5c7a453281 | -8.61282 | -69.72715 | 2024-10-12 05:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 643f202c-0562-39bf-8732-ddfec5654e72 | -8.61225 | -69.73032 | 2024-10-12 05:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51ca88f6-52c2-3376-abfe-74c7f4501dea | 2.82248 | -51.10971 | 2024-10-12 05:44:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 318bc851-b636-3070-8703-5e8eb4628484 | -0.42181 | -52.06072 | 2024-10-12 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f35eb2b-ba31-32a9-9b70-8f2d979b3263 | -0.42076 | -52.06742 | 2024-10-12 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a22a4204-cef0-3cde-b81d-9d44bf8df4cc | -0.41586 | -52.05293 | 2024-10-12 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a99e5cb6-b63e-3b1b-99d5-d3b271b029df | -0.41479 | -52.05978 | 2024-10-12 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed32104d-2356-3bcc-b215-9c01ccf6526b | 1.97101 | -60.9131 | 2024-10-12 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4a4b2db-e357-3fd9-8f35-6d97c3f35ed0 | 1.96722 | -60.91369 | 2024-10-12 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d93f4ce4-1865-380c-b85d-15e165e85384 | 0.83373 | -60.57725 | 2024-10-12 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f001718c-9031-36ba-ac64-71391954a57d | 0.83294 | -60.57225 | 2024-10-12 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 660e28bf-55cb-3a22-b747-e92e375bc42f | 0.83213 | -60.61843 | 2024-10-12 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51825032-e9f0-3edd-9cbe-3df531055eb3 | -2.10304 | -54.70374 | 2024-10-12 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| efd4bc5e-4747-31b3-abdd-af9b4eac7d1b | -3.23662 | -64.40143 | 2024-10-12 05:46:00 | NOAA-20 | MARAÃ | AMAZONAS | Brasil | 1302801 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a1cf48c-a4b4-3c56-a3c8-1fbfc8ad1f09 | -3.51539 | -64.52572 | 2024-10-12 05:46:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22e8a226-165f-31ed-a27d-46e70f6fe665 | -6.44829 | -64.26373 | 2024-10-12 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f55d38a-89cf-38b0-b7a8-00317a79a844 | -5.98773 | -64.82462 | 2024-10-12 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c75768f-6c74-3dde-873b-0bc7aab327ce | -5.98488 | -64.82037 | 2024-10-12 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68a004b1-b57c-3438-aa93-965341ff5420 | -7.34596 | -64.6883 | 2024-10-12 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e11ba19-2a63-3cdb-97b9-efecebf1b103 | -7.34538 | -64.69215 | 2024-10-12 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c04a7d2-078f-3322-9993-e0eb18db2488 | -7.29956 | -64.66544 | 2024-10-12 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b28ab64-76a0-354a-bf7c-2aae2f4083af | -7.29608 | -64.6649 | 2024-10-12 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e6944fe-ae08-3de2-90fe-314840811891 | -7.29432 | -64.66503 | 2024-10-12 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8c5c530-e1b9-35c7-83d2-62a1f7614a2d | -7.29144 | -64.6721 | 2024-10-12 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4533e61-7134-36fb-abd7-8761cddb9c9d | -7.28965 | -64.67222 | 2024-10-12 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4883a8c-788f-38eb-b435-c5f18b98a3fa | -3.42632 | -68.91651 | 2024-10-12 05:46:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97b1d3c1-965e-3190-8af2-9866c77fb03b | -4.90342 | -65.32783 | 2024-10-12 05:46:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d01b309b-a87e-31f5-b7d9-2b371ab330cd | -1.59484 | -53.34544 | 2024-10-12 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 857fba20-3d4c-31cd-8406-a16baf0d3412 | -2.98182 | -52.90388 | 2024-10-12 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 595c1ece-83ff-3377-a33d-30277f4cac9a | -2.98173 | -52.90574 | 2024-10-12 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e3c2f4f2-8e37-3900-9289-643115fc5f11 | -2.98082 | -52.91058 | 2024-10-12 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9801bb22-566c-3f77-bdd9-f84c1a0bb3ea | -2.98078 | -52.91242 | 2024-10-12 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5527ad51-f784-367c-8bcf-3651257bf2f7 | -2.97392 | -52.9096 | 2024-10-12 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4462660-856d-3e87-8864-c802664ccb49 | -2.96698 | -52.9089 | 2024-10-12 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1635a081-e36f-3f01-84d1-22e831e5a34d | -2.96004 | -52.90811 | 2024-10-12 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67fb8e31-0aea-397d-9b68-f62f755de901 | -2.67665 | -53.34335 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a50dbdc2-6f6d-3041-98b5-f494fb282a6a | -2.67576 | -53.34929 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2c68114-34a0-3627-999d-2d4ce919b4de | -2.66907 | -53.34827 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 584df33f-0195-30ac-9c0c-526e2e9cd8d2 | -2.66819 | -53.3542 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01936c97-a5fb-3ca1-97ca-b7abf8f08844 | -2.66238 | -53.34729 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2603285c-df40-35e2-a123-305a070e4330 | -2.6615 | -53.35323 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 634db44a-a523-3460-8ae9-cb7c0425f2ba | -2.6548 | -53.35224 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e82d684d-8ad5-34d1-a6f3-0a9ed97b6d47 | -1.91404 | -54.58711 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 186ac320-3ca6-3aa5-ae20-e51fddf2bfba | -1.89506 | -54.63055 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a79f00e8-5aa1-3d1b-894b-8c39b821cfe6 | -1.89452 | -54.42779 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2746c65-0138-3d92-b084-b0e11a64a404 | -1.8945 | -54.63193 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d99b2aac-3606-3076-9ed7-494e6ce02d7d | -1.89378 | -54.43265 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3fd698f9-cf1e-3ea4-acd9-cb7d93fb7380 | -1.88907 | -54.42195 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 613e8c8d-7f5c-3457-9662-b29b3614e24a | -1.88832 | -54.42684 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c65a34f-7d75-3fe1-ba4c-cb99069bd5c9 | -1.88758 | -54.43166 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 331cd9c8-464e-31de-95de-3a49cc88d9e3 | -1.88214 | -54.4258 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8296626-29f9-3936-8816-c313b008b10e | -1.8814 | -54.43065 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4f8a8a3-59c0-35bd-bd2a-cd5986c444a6 | -1.88066 | -54.43551 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab9c261d-f708-3917-9b60-dd87c481d9e9 | -1.87992 | -54.44034 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24489c79-e02a-31aa-a221-8a8d9966d1fd | -1.87521 | -54.42968 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0023687-fd95-3bce-8d40-13734f45852b | -1.87446 | -54.43455 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a9d8e53-4cb7-3c6f-aa84-9a8035e5c1ae | -1.59398 | -53.35109 | 2024-10-12 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 409d2b13-1447-33f1-b2c6-c05c459f0b0f | -1.26679 | -54.67838 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ac67b19-9216-3f83-bd67-fdff8db00bce | -1.26613 | -54.68276 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87373cc3-8536-36e5-a26c-50f1182469ea | -1.26548 | -54.68702 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7131d416-5fbb-3139-9d37-a0dbb1c80085 | -1.26491 | -54.67933 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f9c7aa4-90bd-3290-bb4b-09a4a0692726 | -1.26423 | -54.68361 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c90f4bb7-ef1a-387b-866b-2d14f8e3e2c6 | -1.26356 | -54.68784 | 2024-10-12 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcfea87d-305e-323b-9f0f-d5eec544dd2f | -3.25549 | -54.18836 | 2024-10-12 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71a615ae-744a-3946-ad41-7b6792fc313b | -3.25471 | -54.19375 | 2024-10-12 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README137.md)
