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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 262ee584-01ce-370e-adff-ec63ba6c903c | -17.83384 | -44.24133 | 2025-08-18 03:57:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9d8b18c-ee1b-385d-8d24-94a2883f21ee | -14.97391 | -54.78575 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7635700b-bf50-3023-b954-ebbae57f7603 | -19.84522 | -44.09383 | 2025-08-18 03:57:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 477678d5-28b9-3f7a-ba58-9596c89f5e25 | -20.40562 | -54.69345 | 2025-08-18 03:57:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59f8fa1a-6cd4-3ad3-ae50-f3fa52285fa7 | -18.64288 | -49.97063 | 2025-08-18 03:57:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e01cfe5d-e06e-3685-a399-ef5ceb557602 | -19.15292 | -47.03432 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e10ae580-1382-36e2-9e8d-863b0a5f22ac | -23.69554 | -47.4553 | 2025-08-18 03:57:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 802f7757-98df-3b2c-bf15-4c23ec4b1a15 | -21.64965 | -44.08009 | 2025-08-18 03:57:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c8fe470-1422-3878-a15e-9e0bf3c6defd | -19.43595 | -43.72916 | 2025-08-18 03:57:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a387ec0-9d50-3dc0-95cc-4bcdacb2643a | -14.99195 | -54.7888 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b1920e8e-ac82-38e9-9fe3-5de645ac5364 | -20.28878 | -42.21164 | 2025-08-18 03:57:00 | NOAA-20 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 48d50465-69f0-31b1-b6ee-fb208c70d7a4 | -20.22038 | -47.0275 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e7e848c-2e5c-3eec-a653-66c7b897ce38 | -17.90447 | -44.41936 | 2025-08-18 03:57:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e8ea266-5321-335f-99b2-7868731cb259 | -17.09159 | -49.87779 | 2025-08-18 03:57:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dff30674-23f1-3601-a01a-68cc94ac52f0 | -18.59887 | -44.41904 | 2025-08-18 03:57:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43d83493-03c8-3c99-8b9f-60d4e1a8a5dc | -20.21757 | -47.04219 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e87649f4-c928-3e37-87b5-c4f34089fbb3 | -20.25512 | -41.95648 | 2025-08-18 03:57:00 | NOAA-20 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ec18741f-130a-3b6e-97ae-b0d85a7807db | -20.00441 | -46.15286 | 2025-08-18 03:57:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4060de5-c400-3aab-af76-3df777422d12 | -14.96651 | -54.76992 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c624695-dfa0-3fa0-a754-d3c50ae3d688 | -18.60243 | -44.41977 | 2025-08-18 03:57:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 247aedbb-cb17-373d-b3fe-35ddbbaac5e0 | -22.19918 | -56.04514 | 2025-08-18 03:57:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d579f1d1-3b25-3629-96e5-62e882ec17b5 | -19.3819 | -49.05938 | 2025-08-18 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4f6e40e-d870-38a2-94eb-5ed1c9f8ab4e | -14.9756 | -54.77843 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ee134b21-dc1d-3d40-a224-b69afc7cdd16 | -14.98843 | -54.78718 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 12b3d640-87d7-365b-aae7-e7eaa2736ef3 | -13.219 | -50.7566 | 2025-08-18 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e7e5b0fd-d3ac-3b95-92e4-fdf8d88e2bb4 | -3.9819 | -42.5396 | 2025-08-18 04:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 8498cfae-25b9-3916-9d68-918674b7fbc7 | -6.4335 | -44.7822 | 2025-08-18 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 265d4674-3c9a-3fdf-acf2-7458402e45e3 | -25.99813 | -52.05809 | 2025-08-18 04:00:00 | NOAA-20 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8333d846-9e41-3bed-9f83-9f8b90f84458 | -28.83336 | -54.08856 | 2025-08-18 04:00:00 | NOAA-20 | JÓIA | RIO GRANDE DO SUL | Brasil | 4311155 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| e1d29b09-c574-3d3d-8a59-7d3faac8f968 | -25.99949 | -52.05196 | 2025-08-18 04:00:00 | NOAA-20 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b4beb3b7-4780-300e-9a7b-0efcadedaf1e | -28.0595 | -48.67239 | 2025-08-18 04:00:00 | NOAA-20 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 17a32f8e-8e0b-3686-9013-8eb3a17b63c3 | -24.48785 | -50.22521 | 2025-08-18 04:00:00 | NOAA-20 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c22d89e-80fc-30fd-8ee9-1dca73f8a1ff | -13.219 | -50.7566 | 2025-08-18 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 887ca396-c543-342a-b615-19ed5011bdc8 | -9.4956 | -40.3586 | 2025-08-18 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.9 |
| 6f7e7e7a-7402-359c-9735-10493368e225 | -17.0842 | -49.8677 | 2025-08-18 04:20:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 49.0 |
| ec121b7e-a2c5-3f9d-ba13-3fffd20ec944 | -6.4335 | -44.7822 | 2025-08-18 04:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 63fa3b28-89ce-31c0-be8a-ee088da75e4a | -17.1036 | -49.8865 | 2025-08-18 04:20:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 4e5e6ba5-afa2-3de8-a11e-c02a69f620e1 | -17.0838 | -49.8899 | 2025-08-18 04:20:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 4899ddd2-327d-3116-b811-5f19301d5a19 | -13.219 | -50.7566 | 2025-08-18 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 9594b2ec-2903-342b-af3b-a1a1b0b15cb9 | -17.104 | -49.8642 | 2025-08-18 04:20:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 237b3802-6e69-38f4-be6f-c22475ea9b70 | -14.9815 | -54.7743 | 2025-08-18 04:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 23996f34-185e-3394-af04-d76dead5f4ce | -13.2193 | -50.7351 | 2025-08-18 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 79ac90ef-24cf-3279-a03c-67c706d9d44d | -14.9815 | -54.7743 | 2025-08-18 04:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| a85d6a2c-3b84-3564-9301-85c1e934f2f6 | -13.2186 | -50.7781 | 2025-08-18 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 1b994f8e-60c9-3803-a532-6491779b88c8 | -6.4335 | -44.7822 | 2025-08-18 04:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 9be75217-a305-343d-8add-4ceda6582e2a | -13.2385 | -50.7326 | 2025-08-18 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d9c0a56c-c4db-3f0b-a476-5add284ea6d0 | -13.2382 | -50.7541 | 2025-08-18 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 1b752620-86d0-3ae8-8408-83f6028ce91f | -13.219 | -50.7566 | 2025-08-18 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 279.7 |
| 7d134023-bdd1-3649-a835-941046250a64 | -17.104 | -49.8642 | 2025-08-18 04:40:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 893ef201-8fe2-38c2-b104-a7d1e717ee68 | -13.2186 | -50.7781 | 2025-08-18 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 1da84831-7b30-3556-8367-4a54f443f13f | -13.1998 | -50.7591 | 2025-08-18 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| b4844deb-c856-3748-8b02-e9e5d01f1f87 | -6.4335 | -44.7822 | 2025-08-18 04:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 3a184b2a-edf5-30d6-a709-ab5d2611b203 | -13.219 | -50.7566 | 2025-08-18 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 340.4 |
| 2ea2bdd6-4038-3af5-9dec-47f0e43446ab | -13.2382 | -50.7541 | 2025-08-18 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 82d7e1b3-165f-3eb3-b394-0dbfbdef97e0 | -13.2193 | -50.7351 | 2025-08-18 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 38f5bf21-ae4c-36cd-97c2-5e7c341bde54 | -13.2385 | -50.7326 | 2025-08-18 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 0e9208d8-6285-3370-8eb7-9b27b9dd8f4b | -4.29836 | -48.06403 | 2025-08-18 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 644770df-67ac-38dc-9051-3dcb0ff258c0 | -5.15928 | -37.9851 | 2025-08-18 04:44:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 32142ce0-2808-359f-b9fe-f73de7214003 | -3.98039 | -42.52785 | 2025-08-18 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 23de02d2-2e7d-3e3a-a590-5d7d0180e19a | -3.79386 | -41.00353 | 2025-08-18 04:44:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| cf6dc0bf-ef7c-3338-9cb8-3ef39447b33d | -3.3838 | -47.60655 | 2025-08-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ad01b07-7d72-3d79-80b5-a567cc411281 | -3.7949 | -40.99639 | 2025-08-18 04:44:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 16eed3b7-acd2-3bf3-992c-7997846914b9 | -3.98537 | -42.52863 | 2025-08-18 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cc0838ba-05b3-344f-b503-e9f5808973a5 | -3.73496 | -51.80238 | 2025-08-18 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 735f8e03-bbda-30ca-bc6c-3e3043af7b9c | -3.38317 | -47.61059 | 2025-08-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c671b07f-a191-390c-97c9-594d736b3006 | -3.59146 | -47.52703 | 2025-08-18 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afc21679-43c1-3ae8-ab4c-3c7728c7bdd7 | -3.12584 | -52.00342 | 2025-08-18 04:44:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a5e722d7-e680-3dbd-9935-9b71d15ee918 | -2.90237 | -51.47663 | 2025-08-18 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ff4de0f-d053-3775-9d25-e5177e8cde4d | -3.23265 | -50.80331 | 2025-08-18 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d3098e4-35ad-3e81-8384-f7cdfb412598 | -3.22132 | -46.81203 | 2025-08-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a7c4290-be1f-3e14-806b-4f6d49ed8c8a | -3.97956 | -42.53354 | 2025-08-18 04:44:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f7ad428f-1812-3a58-8cd2-cb90c13465c3 | -3.66212 | -48.31845 | 2025-08-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85c58696-0895-304c-a9bd-f01cbb5cd3f9 | -3.59505 | -47.52757 | 2025-08-18 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d1f4903d-058c-3239-b9a0-0cd586bc8ea0 | -4.91522 | -43.23798 | 2025-08-18 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f90422fd-7b65-39ce-a679-55f85e6edb43 | -2.95795 | -49.06858 | 2025-08-18 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c505c8ce-e75c-38d8-b296-62065a978ab2 | -3.22065 | -46.81646 | 2025-08-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a31775b-0e01-3d43-9100-2e5e23b51311 | -3.98578 | -42.52579 | 2025-08-18 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1a8faafc-1cc7-3094-a5f2-d1e73b3f4f36 | -4.91444 | -43.24321 | 2025-08-18 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e90439dc-0bf6-3eea-8943-61f7887f99e0 | -4.91913 | -43.24084 | 2025-08-18 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0450a2d-03b9-38c7-bb8e-0f9d602e10a4 | -2.30022 | -48.14365 | 2025-08-18 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74592de8-ca4c-3577-b527-82fb106009b7 | -2.98655 | -49.30529 | 2025-08-18 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2901684-e220-3449-b5bd-898614ea1ccf | -3.7383 | -51.8029 | 2025-08-18 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55e0865e-ddc4-36c2-982f-74b136c58d3c | -4.92004 | -43.23864 | 2025-08-18 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6e3a96c-727e-3fe4-b978-fa795e667c2a | -4.91987 | -43.23558 | 2025-08-18 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eeba612f-0a14-3a10-bc05-59413bded8dc | -2.54981 | -47.70488 | 2025-08-18 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3627b3d8-ce13-3fa7-8370-0bd739749ae0 | -3.16201 | -47.54106 | 2025-08-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62614040-d6f5-3d29-b057-b888a6db2474 | -4.13111 | -47.64542 | 2025-08-18 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82672d14-06a9-3a81-b88c-c33096c6065f | -3.05182 | -47.38404 | 2025-08-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b2a0194-f023-3145-884f-16bc73f61fb3 | -3.66394 | -50.21946 | 2025-08-18 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa95cc1b-1ef2-37c9-b0fc-6c7c965c9763 | -3.66506 | -50.95231 | 2025-08-18 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf1389e0-7642-300a-ae1c-18f0ae1cf6c8 | -3.04761 | -47.38756 | 2025-08-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e34b377-0760-3cdf-bed0-aef213d10c32 | -3.98454 | -42.53431 | 2025-08-18 04:44:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| bfe955e9-81c2-3189-80dc-0b0edb72d1b1 | -4.91431 | -43.24018 | 2025-08-18 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b26b1941-8cbe-3db3-950b-7e54fa2a98b0 | -4.13471 | -47.64589 | 2025-08-18 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 357e53a1-122a-3db8-917d-ed88af2aec8c | -3.78888 | -40.99902 | 2025-08-18 04:44:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e23263b3-ea9e-34c8-a559-7c6b6210f942 | -4.30188 | -48.06457 | 2025-08-18 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc04252c-0cc0-3d62-9d1e-c4423ee3110e | -3.98121 | -42.52218 | 2025-08-18 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4f620939-6b32-3461-b5dd-4ee5cde8677a | -3.96498 | -47.63823 | 2025-08-18 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd70beb8-11df-369c-8e4c-033bab11e945 | -3.79437 | -40.99997 | 2025-08-18 04:44:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 974a5cd0-eb35-3aff-a09c-ae37b845e98a | -3.98496 | -42.53147 | 2025-08-18 04:44:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README17.md)
