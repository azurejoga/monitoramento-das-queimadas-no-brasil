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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0df960bc-f426-39b0-88fa-0b98a9e5036d | -12.1125 | -50.6358 | 2026-08-24 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f0ade199-fed7-3236-a9de-c7a00649f060 | -12.0934 | -50.638 | 2026-08-24 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 5a8c18a4-d6cb-3ee1-8353-4e1f95d306df | -12.1128 | -50.6143 | 2026-08-24 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 201.9 |
| ea1c060b-4266-3426-a5fd-716b0e6e9860 | -7.3603 | -45.8136 | 2026-08-24 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 5e43cc65-78bc-3828-827e-463dddc02259 | -12.1132 | -50.5929 | 2026-08-24 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b5a0bcc5-df0d-3315-8b51-19fe34d80633 | -17.4236 | -48.8462 | 2026-08-24 03:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9e83fa4b-fbb3-36e2-a8db-eb24e64fc1b1 | -12.0941 | -50.5951 | 2026-08-24 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| fbe9ba40-f358-3512-9d56-71878b5d80f8 | -17.4435 | -48.8425 | 2026-08-24 03:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 5c0812c9-5d6e-349c-8ce7-fefd486c6c26 | -7.3603 | -45.8136 | 2026-08-24 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a3fdc994-ba0c-306d-af09-6c7533b93fec | -17.4236 | -48.8462 | 2026-08-24 03:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 0c2c41c9-f357-3fd1-a0cc-243eca1fc285 | -17.4241 | -48.8236 | 2026-08-24 03:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| d31fe254-fa48-35b7-95b9-aca99f22738a | -8.9876 | -65.3819 | 2026-08-24 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 6d47aa26-442d-32cc-ae8e-f48935a3eea0 | -17.4435 | -48.8425 | 2026-08-24 03:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 5fe5e9ef-acfe-3fd8-85a0-fb25a6ab959f | -9.0061 | -65.3813 | 2026-08-24 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 85384799-d4a1-39bc-93f2-85f44ba0ae5e | -17.444 | -48.8199 | 2026-08-24 03:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 15917483-ea27-3de1-a3f9-e80604793556 | -17.4241 | -48.8236 | 2026-08-24 03:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 3342c3a2-7953-320b-8cec-742c27471b42 | -9.0061 | -65.3813 | 2026-08-24 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 87f16ff7-a333-3b5a-ac4f-682d1c40f348 | -7.2443 | -49.8654 | 2026-08-24 03:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ad8d6537-83c4-356c-9798-9f9836d78b47 | -17.444 | -48.8199 | 2026-08-24 03:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| cfb74db2-2e33-3de1-9625-9e2304f14d52 | -17.4236 | -48.8462 | 2026-08-24 03:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 92c114a2-d9bb-339c-b7ae-e0693fc4c294 | -17.4435 | -48.8425 | 2026-08-24 03:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 11fa3341-1dfa-3273-9356-8ce7559ea466 | -8.9876 | -65.3819 | 2026-08-24 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e905ca6e-8336-34b0-bc60-040ed4b7ddf4 | -7.3603 | -45.8136 | 2026-08-24 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| b9edbe88-cbcb-3f2d-a4a4-690997b7fbba | -22.9454 | -51.7768 | 2026-08-24 03:40:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 46.7 |
| b13469c2-76e8-3cdf-9422-41e82c6e79ca | -3.53309 | -48.18511 | 2026-08-24 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 1363d26e-5709-3cea-81c6-d1cbfe43844c | -4.83336 | -37.26864 | 2026-08-24 03:47:00 | NOAA-21 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 65fedd8a-bdb1-358c-bd8b-3e0c067a59e8 | -3.53949 | -48.18602 | 2026-08-24 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 804d144c-95b5-36f5-9f24-ec0fe7b2f3b0 | -3.59505 | -41.37337 | 2026-08-24 03:47:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 97ffa68f-9484-37a7-93ca-d4d784786cc1 | -3.54039 | -48.1808 | 2026-08-24 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 05774b78-9ec4-3999-80c0-cd169a5f2d8b | -5.15175 | -43.07597 | 2026-08-24 03:47:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04dbe458-131d-3957-a9ab-a44f28111cdf | -3.53398 | -48.17992 | 2026-08-24 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a28c1757-1c7b-31e6-83ff-941a3f45ef1d | -5.2416 | -37.89528 | 2026-08-24 03:47:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 38ffb35d-99e6-3b06-99bc-5f8ca54f9f93 | -6.81305 | -34.93923 | 2026-08-24 03:47:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 409a280f-f940-3c97-9a81-c5d608f0ca83 | -4.00224 | -38.98647 | 2026-08-24 03:47:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ebf25a59-92d7-3c3d-8d16-4fc33dea9e56 | -4.93631 | -45.79799 | 2026-08-24 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da2166b0-82f5-3675-b4ae-cd13b64ad298 | -6.56468 | -35.20898 | 2026-08-24 03:47:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| bfd91578-1e01-3f85-b41e-67570b7b522d | -4.15171 | -38.48137 | 2026-08-24 03:47:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 759348cd-b731-394a-96f1-c4a1da8c49ce | -4.93688 | -45.79457 | 2026-08-24 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae5acc48-1d54-302d-ac19-d6c45997caa2 | -3.99871 | -38.98595 | 2026-08-24 03:47:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 69999c84-344c-31b0-9a11-a21f38e0b59e | -4.18287 | -49.40436 | 2026-08-24 03:47:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f7d09f01-3cd9-352f-af94-d4e29824f075 | -6.81648 | -34.93977 | 2026-08-24 03:47:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ae0e95a1-aff9-36af-a839-c662cb719ea3 | -6.56808 | -35.2095 | 2026-08-24 03:47:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4508524b-b871-326d-8d1c-730f11d26910 | -3.2662 | -49.52858 | 2026-08-24 03:47:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b596cbac-5a97-316f-91f5-5190e6944b42 | -8.10483 | -47.48719 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32a454ed-a254-3fae-9bb3-7c1deaeccfe1 | -7.83389 | -47.65003 | 2026-08-24 03:49:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e47d471-464c-3a54-a111-2b57fba399b3 | -7.0991 | -43.37483 | 2026-08-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b7ced5b7-fb2e-3768-9c88-36ba8549cdb8 | -10.29616 | -48.20557 | 2026-08-24 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03b92dbc-1285-3919-acac-bfe8269f84a0 | -10.04532 | -46.43191 | 2026-08-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a714d9c4-ad18-3e58-9b12-deed9efe64fd | -9.30323 | -40.21929 | 2026-08-24 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1bf01ecd-40d0-3aaf-81c5-859a550b7dca | -8.10978 | -47.4921 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4d46e5dd-c2bc-3381-9185-1d7f9555d0be | -7.27285 | -45.36699 | 2026-08-24 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2763594a-c22b-304f-b2a7-42a0b2eafd05 | -10.02047 | -46.82528 | 2026-08-24 03:49:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a2ddf457-31e9-324a-8ed1-4e1f95cb3409 | -8.31407 | -47.58582 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ead35c5-ec1a-3ef6-9d67-0d88288a5c39 | -8.09749 | -47.48254 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 888f8497-5c4f-3751-9847-82d9b9e22f64 | -7.26735 | -45.36898 | 2026-08-24 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed2b6727-7dde-3629-9ae2-2dc59cbd176c | -8.31618 | -46.89764 | 2026-08-24 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4379080-7e37-3d16-a8c2-e23360972919 | -5.63327 | -48.42361 | 2026-08-24 03:49:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1d56547c-c795-33d0-a397-5a3b0cb16908 | -7.75656 | -46.15521 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 994f0246-dff1-3dd1-94e8-6d182c6721a4 | -7.31141 | -42.98238 | 2026-08-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 513b2b56-da0a-3cd1-8b48-ae5d92ab3218 | -7.97256 | -43.93028 | 2026-08-24 03:49:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86de6c19-cc44-3a7f-86ff-7d947bff7ec2 | -7.26555 | -49.92901 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4c13ae7c-aa6b-3225-b8ac-9f340a631442 | -7.16979 | -42.74169 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 986dadfa-b5b1-338e-a3bd-ec7852b00c06 | -12.28171 | -44.82646 | 2026-08-24 03:49:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d4c9934-f472-34a2-8532-d0f20977e43e | -13.09483 | -43.35713 | 2026-08-24 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c174cf3a-2082-323b-866a-5a799942a050 | -11.36025 | -40.0602 | 2026-08-24 03:49:00 | NOAA-21 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fccaf263-b427-3369-8906-47e1639b9493 | -8.31223 | -47.58453 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c208fe83-eac1-3c33-bcbf-d3a989b55243 | -7.65363 | -42.73761 | 2026-08-24 03:49:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1fa73a39-369a-3db5-b69a-3bfb33964d27 | -11.23972 | -39.41085 | 2026-08-24 03:49:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7c3854a4-b450-37ed-85ee-b36ce3968e0e | -12.75132 | -46.44947 | 2026-08-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c3f49f67-0ecf-3657-b544-6de03f73031c | -7.1866 | -42.74437 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dae7cc3e-1d47-3a20-a524-d740faec6088 | -12.41477 | -42.90442 | 2026-08-24 03:49:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a67301f3-ba8c-3951-a82f-2c451aea057c | -7.15709 | -42.79148 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f1b6b7ea-1746-3351-a679-dab724c2f0db | -7.26041 | -49.91964 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ddf39518-cdd3-3002-a8d6-b61ddfb71baa | -5.57742 | -45.29194 | 2026-08-24 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4bd6200-f5a9-3101-aaf3-40c5548f3b93 | -8.89008 | -36.96524 | 2026-08-24 03:49:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7be6623e-1996-372e-a7af-99b02323a794 | -11.98471 | -45.50601 | 2026-08-24 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6c01d42-6cf6-3a50-a8de-784c3585c0b7 | -8.59155 | -49.99793 | 2026-08-24 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62803f99-e6ae-320e-9ed9-29c7eb68f44c | -7.89944 | -46.32201 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd1d8942-9cf3-37f8-8f88-47d83d7be4e2 | -7.14091 | -42.78472 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52967a4d-cbdf-3dd7-a36a-2222108ffe28 | -7.37055 | -45.8038 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d1d76199-65b1-32ff-83b1-35ad17508f47 | -7.24967 | -49.8673 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 114a9c01-8805-36f4-b614-1cd1a98b2d98 | -7.89892 | -46.32906 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07607c4b-0488-38b3-a227-a3a533d94c8b | -7.29873 | -43.00519 | 2026-08-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 38e4e5fd-4f30-3504-821d-02b92ddd79cf | -12.05963 | -50.57487 | 2026-08-24 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 271c1383-b3ce-32ff-8e65-63f60beec74f | -12.22678 | -43.17581 | 2026-08-24 03:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c620fd09-a06a-372d-8855-3d47fc59be40 | -11.58818 | -46.93334 | 2026-08-24 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45278c6d-c659-3da9-8402-824df0836eb7 | -7.29446 | -43.0045 | 2026-08-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b389eae0-7196-3ea3-8291-3d490329e6bf | -7.01393 | -37.26504 | 2026-08-24 03:49:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d9551f3f-1aaf-35d9-bbd6-9ab6a63a216f | -7.15078 | -43.09093 | 2026-08-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d63fbd9c-b5aa-3d06-9038-acdbe77255b4 | -11.5442 | -46.9603 | 2026-08-24 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69bdf9f8-e924-3a2a-b9ca-620ba0836ed1 | -7.09969 | -43.37334 | 2026-08-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d7f1b25b-b890-313d-b309-1a18bd1881ed | -7.26289 | -44.19527 | 2026-08-24 03:49:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00d54190-d668-33d8-89bb-88aa35d6f9b2 | -13.43261 | -39.88553 | 2026-08-24 03:49:00 | NOAA-21 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3d37f3bf-b92b-3784-8cd5-a7681df8a29a | -12.28038 | -44.82897 | 2026-08-24 03:49:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6909249-d24a-3689-9365-e4795fef61c2 | -10.80687 | -50.94459 | 2026-08-24 03:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e52ccdde-a16b-3c49-a234-e96a4e92cb75 | -10.86094 | -50.98692 | 2026-08-24 03:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47ea3715-f94f-3345-98be-9c2b48f312a7 | -9.05194 | -50.77314 | 2026-08-24 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99794688-f36b-3e64-b02d-fce1da092d4d | -12.4149 | -42.90162 | 2026-08-24 03:49:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c3bcd2be-8eeb-337c-b023-39d8a879c0c8 | -6.87405 | -38.36649 | 2026-08-24 03:49:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9095de42-adbf-35a9-b49c-6b0c9f63b231 | -10.04357 | -46.41296 | 2026-08-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
