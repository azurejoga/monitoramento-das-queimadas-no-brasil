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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e8a85cf-4679-3a8f-9810-8fe4ffa03be8 | -16.13091 | -46.87495 | 2025-08-03 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d164f66a-e910-300d-aa3e-dee36aebb215 | -17.02435 | -47.17954 | 2025-08-03 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23cbb883-c1d9-3f96-89cc-577eec223979 | -17.02831 | -47.17624 | 2025-08-03 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ccd81f3-27cf-300a-848b-661fafc5e470 | -19.9944 | -45.78008 | 2025-08-03 04:29:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e782052-6f87-3c80-804e-3f68e22dfab7 | -20.08593 | -43.99623 | 2025-08-03 04:29:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 90bdbab7-cd7e-38f0-96d9-682cab6cbd23 | -15.59373 | -48.50768 | 2025-08-03 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 99326e5d-8675-3d69-af8e-6a5c6a734f3a | -15.10857 | -55.251 | 2025-08-03 04:29:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b13116bb-575e-31ce-b48d-676c77f0f958 | -15.60087 | -46.52768 | 2025-08-03 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54e37b2c-286a-37d9-8d74-804582fdca79 | -20.45127 | -50.01083 | 2025-08-03 04:29:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45f1ada7-e9fb-320a-8fd3-c02ec2011ef3 | -16.70264 | -49.38947 | 2025-08-03 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 233ed6d2-b718-3209-83db-4ffcf5e09e08 | -18.54675 | -48.90476 | 2025-08-03 04:29:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 150ea400-4fcf-345c-a179-ecb63a9c5316 | -15.60487 | -46.52434 | 2025-08-03 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6840771-088d-388d-9d72-94b5e75d8e85 | -15.55204 | -54.27637 | 2025-08-03 04:29:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2506f189-4600-390d-bfa4-d9b0efd898bf | -19.98895 | -46.84123 | 2025-08-03 04:29:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38e1d31a-f09f-36ca-b634-41d33711bc77 | -15.54375 | -54.27477 | 2025-08-03 04:29:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17b9f5c5-9e95-3bdd-8619-c6d495d63726 | -19.13588 | -43.57886 | 2025-08-03 04:29:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10b13bdb-007f-32fc-b8b1-62fc948900f6 | -16.68353 | -41.36224 | 2025-08-03 04:29:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5a2e40a2-5762-39fb-be62-b5be09af65f3 | -19.73791 | -45.26132 | 2025-08-03 04:29:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54f6ca68-21c1-31e8-919e-9f910bb09c98 | -18.2107 | -44.70839 | 2025-08-03 04:29:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 717c225b-f014-329e-bb1e-79c08e8a7920 | -17.87518 | -51.68958 | 2025-08-03 04:29:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4e0b7ff-88d6-3c80-96ee-7452e212f0bb | -18.84175 | -46.4492 | 2025-08-03 04:29:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| dd635e32-3178-3d41-865a-97e4c16146d8 | -18.83819 | -46.44868 | 2025-08-03 04:29:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c10e73f5-9e2e-30b4-b234-c01d8626f53e | -15.67447 | -48.09621 | 2025-08-03 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d111323-6bc4-31a4-94fd-d23d1f81cd10 | -16.72185 | -49.41864 | 2025-08-03 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16645650-9346-329a-ad4b-dd2310de3801 | -18.50715 | -45.67668 | 2025-08-03 04:29:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7684e6c0-e8d9-34a0-86a0-395d91c9926c | -15.55134 | -54.28024 | 2025-08-03 04:29:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38d1ced6-ca8d-3c75-b780-37b602dc7677 | -16.72128 | -49.42224 | 2025-08-03 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eddcf5b0-375e-39f8-81f0-89b5c3b78628 | -20.71929 | -47.29353 | 2025-08-03 04:29:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dab0a2a-bbb9-3c99-b959-a9b07bcf8be8 | -20.08177 | -43.99591 | 2025-08-03 04:29:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 1cd27f5d-ffb3-3645-a13d-e41d197d894a | -19.99248 | -46.8418 | 2025-08-03 04:29:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 805a4372-916e-34e9-be98-0f1f065bc6ee | -15.67393 | -48.09978 | 2025-08-03 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71d14fd3-4bde-3d57-a497-7df37bd259e7 | -16.83202 | -42.87026 | 2025-08-03 04:29:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dcdc71ed-2309-3403-bdf0-8493be857d67 | -16.72459 | -49.42281 | 2025-08-03 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5d5f620-fd06-3f3f-8dc5-a3cababd129f | -18.93076 | -46.79272 | 2025-08-03 04:29:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b032c00-c4b8-370f-b5c0-9893b9620392 | -16.52972 | -39.46181 | 2025-08-03 04:29:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5b5ffe28-dc0d-3f47-80c5-b20a35b57ab4 | -19.73871 | -45.26006 | 2025-08-03 04:29:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a562c31-6c63-33c5-9f90-d25f8c66fdef | -16.72402 | -49.42641 | 2025-08-03 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ba4e62a3-7e62-3c05-8f55-d510bd63de62 | -18.78109 | -47.46708 | 2025-08-03 04:29:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ac0a58f-cb6a-317e-aede-60faaf6c65d1 | -16.68098 | -41.36381 | 2025-08-03 04:29:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 82dc1dca-8654-3edb-b048-b5bf8032466b | -21.36414 | -44.89892 | 2025-08-03 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 100e9299-67f6-3532-917c-ab9a4a39b59f | -19.99648 | -45.77842 | 2025-08-03 04:29:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 819ca10b-2479-3b91-8c6d-8fe6bb38fa09 | -20.79363 | -41.23476 | 2025-08-03 04:29:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 58acf7c6-6da8-3433-8905-77b7cd32fe13 | -16.7197 | -49.4207 | 2025-08-03 04:30:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| cfeadfc5-dd4c-33b7-a5b1-e4caed209f95 | -12.6402 | -44.4913 | 2025-08-03 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| a67eb971-c203-31d0-95ae-0b9266cf9811 | -16.7395 | -49.4172 | 2025-08-03 04:30:00 | GOES-19 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 343f4127-b472-35d1-8568-882e010d1ac7 | -6.6144 | -59.9656 | 2025-08-03 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7c86631c-b555-3ab5-98d5-ec3d979f2d2b | -7.9934 | -43.2005 | 2025-08-03 04:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 09740db1-e546-3c78-abd5-67c7046ddb0b | -4.5684 | -44.2036 | 2025-08-03 04:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| eac63164-f2fe-36ff-9f12-c1d8e24ac1f4 | -22.89345 | -46.42305 | 2025-08-03 04:32:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8a1f632e-744f-3a95-b827-fabc0eeee4e7 | -23.71923 | -47.35666 | 2025-08-03 04:32:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 68345b78-ebe4-3da0-b1fb-230e0e55193f | -26.19425 | -53.0124 | 2025-08-03 04:32:00 | NOAA-21 | RENASCENÇA | PARANÁ | Brasil | 4121604 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ff68ea8c-70e8-3a03-84db-be25ae90cea5 | -22.72806 | -44.74624 | 2025-08-03 04:32:00 | NOAA-21 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 67414991-70b7-3d8a-a354-c31035c92162 | -22.58326 | -46.37568 | 2025-08-03 04:32:00 | NOAA-21 | BUENO BRANDÃO | MINAS GERAIS | Brasil | 3109105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 363e854b-7e7d-3b0c-917a-dc1363f56a1d | -23.83194 | -45.38894 | 2025-08-03 04:32:00 | NOAA-21 | ILHABELA | SÃO PAULO | Brasil | 3520400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a888ac98-f6ce-35db-8c61-55e74e14c206 | -24.23333 | -48.4659 | 2025-08-03 04:32:00 | NOAA-21 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 763be6d3-a332-3568-aea7-8ba066698940 | -23.83416 | -52.95586 | 2025-08-03 04:32:00 | NOAA-21 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f03b2625-8858-3096-8aba-acfad70892c7 | -22.2215 | -55.15754 | 2025-08-03 04:32:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9913bdb4-e72f-3d1f-944b-8892ec0e9e7d | -21.83371 | -47.30065 | 2025-08-03 04:32:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 13e63936-b998-3f89-affa-e18a85adc3aa | -23.48809 | -47.27693 | 2025-08-03 04:32:00 | NOAA-21 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 467cae06-453b-3261-8d06-c8731c6a079a | -24.31675 | -51.97501 | 2025-08-03 04:32:00 | NOAA-21 | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 84a062c3-1857-3646-871e-3b1efca42312 | -23.5635 | -54.28876 | 2025-08-03 04:32:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9bdd8c77-a3c4-3240-be28-1c0737b805cb | -25.61366 | -49.72965 | 2025-08-03 04:32:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0e7af49a-a35a-36df-8246-f3f627162899 | -26.4664 | -52.75608 | 2025-08-03 04:32:00 | NOAA-21 | NOVO HORIZONTE | SANTA CATARINA | Brasil | 4211652 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 39c98774-0f2a-3591-ae6a-c2fa55c8f993 | -22.72455 | -44.74075 | 2025-08-03 04:32:00 | NOAA-21 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 504bd6bd-42a1-3c27-8992-9534b65083c4 | -26.76786 | -52.52591 | 2025-08-03 04:32:00 | NOAA-21 | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 14eba836-378c-37b0-9a70-20d8dfaf16f7 | -25.61701 | -49.73026 | 2025-08-03 04:32:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 93e80866-2d3e-3699-b833-fb59ca0652b6 | -21.44925 | -55.10628 | 2025-08-03 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 28c7e094-3248-3a34-8114-375a3472f0f1 | -25.61643 | -49.73415 | 2025-08-03 04:32:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1d79fa09-0923-3bb4-8039-ac4e0b0fde2d | -23.26049 | -45.42757 | 2025-08-03 04:32:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 634f8f86-c97c-3199-8088-68c01824b6a2 | -22.28528 | -53.83665 | 2025-08-03 04:32:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c7ce10ea-8c21-3b43-bd6d-734d9ab5231c | -23.6526 | -48.05064 | 2025-08-03 04:32:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e185dd0-e471-3ca8-a1ad-6a77c6ee1735 | -27.1616 | -51.21123 | 2025-08-03 04:32:00 | NOAA-21 | IBIAM | SANTA CATARINA | Brasil | 4206751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b9b69754-f231-37d8-8319-ba7c5cc4f8d5 | -24.22307 | -51.86169 | 2025-08-03 04:32:00 | NOAA-21 | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8636ffe8-009f-3309-b0cd-c46bb5dfa3b7 | -24.3134 | -51.97436 | 2025-08-03 04:32:00 | NOAA-21 | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ff6aba0e-96ca-3c1d-96e8-24e1963fd7ba | -21.45085 | -55.10487 | 2025-08-03 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a164f69-22d1-3893-8458-04883c9f3ed7 | -21.4469 | -55.10402 | 2025-08-03 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0df97ff0-8fb3-3e99-9fac-0f34cfa036be | -23.1932 | -46.3142 | 2025-08-03 04:32:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d981fe7b-0bd6-3565-96d7-a050182eee96 | -21.71084 | -47.69139 | 2025-08-03 04:32:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6610e850-60e7-30ac-86e2-71ab0c69ad90 | -24.23676 | -48.46652 | 2025-08-03 04:32:00 | NOAA-21 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 608bdd5d-6a0c-35ae-abd3-13018f53fd78 | -22.66825 | -53.37942 | 2025-08-03 04:32:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 33fcac48-87af-30bf-90c2-396fa1d515c1 | -23.65319 | -48.04649 | 2025-08-03 04:32:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d458fc4-8c52-31e4-abf4-463bf4fb84e9 | -22.63761 | -46.3812 | 2025-08-03 04:32:00 | NOAA-21 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e09d6ccb-f1b6-37bb-811f-8b78e033277d | -26.73282 | -51.58418 | 2025-08-03 04:32:00 | NOAA-21 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d043b134-2789-315c-bfe2-88d16e0f9831 | -23.56717 | -54.28948 | 2025-08-03 04:32:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e97ceb09-9185-3da0-8ed7-fac876b358da | -23.83463 | -45.38546 | 2025-08-03 04:32:00 | NOAA-21 | ILHABELA | SÃO PAULO | Brasil | 3520400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a0130b80-c60a-331b-994b-df9242b2f430 | -24.08693 | -52.35911 | 2025-08-03 04:32:00 | NOAA-21 | CAMPO MOURÃO | PARANÁ | Brasil | 4104303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| abf4938f-f19e-3cfd-854d-04781448a9e2 | -25.6183 | -49.73328 | 2025-08-03 04:32:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 778bfb48-9efc-39c1-a899-8d1fa4348655 | -22.22251 | -55.15222 | 2025-08-03 04:32:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b271c355-6d87-3407-b6c3-08e5a2ec67d8 | -24.1742 | -52.92388 | 2025-08-03 04:32:00 | NOAA-21 | GOIOERÊ | PARANÁ | Brasil | 4108601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e01ab2d3-7013-31f0-b7e9-69e930867323 | -22.7285 | -44.74257 | 2025-08-03 04:32:00 | NOAA-21 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0529b683-0ab3-37b9-9610-ff0163bc01dc | -26.73857 | -51.5694 | 2025-08-03 04:32:00 | NOAA-21 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1cf6be6a-3e13-3422-aa84-c73a7796ee0c | -21.71431 | -47.69193 | 2025-08-03 04:32:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1eba50ef-bb13-3bd1-8b45-319f8a5e84f4 | -23.56382 | -54.29116 | 2025-08-03 04:32:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cbeb5f00-9a5d-305b-82b5-9d0bf5776a71 | -22.89408 | -46.41825 | 2025-08-03 04:32:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ccb50c92-337a-3b55-9800-5a6d468df15a | -27.52015 | -52.99935 | 2025-08-03 04:32:00 | NOAA-21 | TRINDADE DO SUL | RIO GRANDE DO SUL | Brasil | 4321956 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1fd02a45-789d-3f7e-83bb-1d9c546cc197 | -26.19763 | -53.01311 | 2025-08-03 04:32:00 | NOAA-21 | RENASCENÇA | PARANÁ | Brasil | 4121604 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e714d903-6dc6-30e6-86e7-27bf014c28a1 | -21.64391 | -49.75332 | 2025-08-03 04:32:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4d3349dc-2384-37c5-afbf-55968b7f097f | -26.93048 | -50.67835 | 2025-08-03 04:32:00 | NOAA-21 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2f350dfe-9096-3ce1-abe6-75d53200d5f2 | -26.55095 | -48.85317 | 2025-08-03 04:32:00 | NOAA-21 | SÃO JOÃO DO ITAPERIÚ | SANTA CATARINA | Brasil | 4216354 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 302b206a-6220-361e-85d0-4b124fe7b80c | -25.30789 | -49.28858 | 2025-08-03 04:32:00 | NOAA-21 | ALMIRANTE TAMANDARÉ | PARANÁ | Brasil | 4100400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |


[Clique aqui para ver as próximas entradas](README21.md)
