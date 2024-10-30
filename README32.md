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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0489c0ff-6be6-3537-8914-f3a56429c077 | -3.9486 | -48.1291 | 2024-10-30 04:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 95964771-fdd6-329b-9db3-05ac0a808a23 | -3.9671 | -48.1283 | 2024-10-30 04:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| aac62ff6-00eb-3e1c-a250-31d747f26a4a | -4.0681 | -50.024 | 2024-10-30 04:15:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| c161db92-9e71-377b-98a2-c4f5a36c095c | -4.0682 | -50.0029 | 2024-10-30 04:15:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 279f300a-7ef7-3d6c-bdc4-f38731d30c15 | -4.2496 | -50.6677 | 2024-10-30 04:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6c7da2f1-cd54-3ebc-9cdb-fe2bdc9faabe | -4.2681 | -50.6669 | 2024-10-30 04:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 06444467-a4ae-3972-9d9d-bf720ba9f0d0 | -5.9788 | -45.3621 | 2024-10-30 04:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d71aae9b-4016-344d-aeb1-44bce23521cf | -6.4232 | -42.1017 | 2024-10-30 04:15:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| 12fb0845-854b-36d7-bb62-09efc19916a1 | -6.4235 | -42.0779 | 2024-10-30 04:15:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| e0845793-554b-3827-8bd0-ef38bd4abb5b | -10.7175 | -44.916 | 2024-10-30 04:16:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ed132b6e-72f2-3cfc-9de4-628d9749d7bc | -19.5862 | -56.7136 | 2024-10-30 04:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 131.7 |
| c5b69387-090c-33c8-baaf-93b59f3cd6c0 | -19.6063 | -56.7108 | 2024-10-30 04:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 129.4 |
| 83ff456a-298c-3f4f-b74a-98bdef29d41e | -19.6264 | -56.7079 | 2024-10-30 04:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 64f25a87-2f93-3402-9c24-a1d62605b0cd | 1.64914 | -50.89325 | 2024-10-30 04:17:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8f39068-8d3d-3196-bf25-b70a177abf02 | 3.55656 | -51.27152 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb5fffdc-77e2-337e-b073-e67ae43bf0fe | 3.55609 | -51.26831 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f8507cf-2e9f-33de-a20e-f2ec4bbaad47 | 3.55225 | -51.27869 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b1d552e-8c20-3bc8-aea2-1c1d60234268 | 3.55178 | -51.27548 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fcea612-194b-3bba-b850-832d35b542e6 | 3.55131 | -51.27227 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 659b6b9f-c941-36b8-9430-86db05addb02 | 3.54794 | -51.28588 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae9aca11-4e05-3176-ac0b-459e06eeb234 | 3.54747 | -51.28267 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1809c04-cfc5-3bb9-a19d-6869e0fd2676 | 3.547 | -51.27945 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ab12d8d-ab84-37f6-bbd2-ad5891e53a2c | 3.44997 | -51.24177 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dfd1ac0-4e04-3014-a9d9-3d7c9c40cc9e | 3.44568 | -51.24891 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f9074e4-a5be-3bc4-b776-1ad6150ee6b2 | 3.44521 | -51.24572 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45a14ac4-04d0-3436-8e51-ef15ab010252 | 3.44045 | -51.24966 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3da9061b-5090-3ce7-bb8d-bd363f02f2f0 | 3.31081 | -51.35452 | 2024-10-30 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3ddff9d-69f4-339c-969d-df170cc70042 | 1.68098 | -55.85542 | 2024-10-30 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a5e3f0b-ccd4-3d10-82b8-d6ae6ca15921 | 1.67508 | -55.8626 | 2024-10-30 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31b654d9-9dc2-318e-b9c5-610375867101 | -3.40291 | -41.63004 | 2024-10-30 04:19:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3e65aa21-ead4-3f7c-9b01-fc38ef0790e7 | -3.40233 | -41.63385 | 2024-10-30 04:19:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e2da7c96-20a0-393b-8e3c-372f02e9bbcc | -3.40047 | -41.63056 | 2024-10-30 04:19:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 917cae98-eae3-3ba7-ae01-45a1f1af8e8a | -7.02317 | -34.87836 | 2024-10-30 04:19:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5e817053-887b-30c1-88c6-cfc7588d203c | -7.01704 | -34.88145 | 2024-10-30 04:19:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5276683f-da51-36ce-802a-0b6d7813415d | -7.71797 | -37.43152 | 2024-10-30 04:19:00 | NOAA-21 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8aa42e22-0f50-3379-955d-eaa320c9145d | -7.76549 | -37.81052 | 2024-10-30 04:19:00 | NOAA-21 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3952d7fb-b5b8-35d4-9338-9e7d9d09fe2d | -7.76455 | -37.8081 | 2024-10-30 04:19:00 | NOAA-21 | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ae8335bd-66eb-30e5-bb28-68b278b076ca | -7.56706 | -38.7495 | 2024-10-30 04:19:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bd4a502d-6c2d-3cf4-abec-4ec23b0a361e | -7.56647 | -38.75367 | 2024-10-30 04:19:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19fa64ba-e834-34ef-8dda-b1b087b98ebc | -7.37984 | -38.70335 | 2024-10-30 04:19:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 31f11598-2fbe-3f50-9fc5-f8100dc21ba5 | -7.34754 | -38.04589 | 2024-10-30 04:19:00 | NOAA-21 | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0aee93a1-db4b-319e-b42a-936680a4b2e8 | -6.9291 | -38.17941 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b7c79947-09a5-3427-a91b-49a7150666e0 | -6.71211 | -37.49566 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0b50655-8e4e-318b-b9bd-2079eeaf9c2b | -6.70957 | -37.49375 | 2024-10-30 04:19:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dacef4cf-e08f-33bf-8a01-ed8b9c6838c4 | -6.7049 | -37.49311 | 2024-10-30 04:19:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fbcd7518-8567-3c5f-ade4-89e1aafad2e3 | -6.63854 | -37.49087 | 2024-10-30 04:19:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8aa3c4fc-396b-3850-a9d2-c5484a00dea7 | -3.7857 | -39.09467 | 2024-10-30 04:19:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2c17e68a-8d3d-3e72-a818-7e2f50a25bc9 | -7.69278 | -39.52916 | 2024-10-30 04:19:00 | NOAA-21 | MOREILÂNDIA | PERNAMBUCO | Brasil | 2614303 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49d51698-cf9a-38a2-9324-5d6a66fee79b | -7.17436 | -39.46127 | 2024-10-30 04:19:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f42bccde-d8fb-3046-bbd8-42b0ae28180a | -6.87106 | -39.374 | 2024-10-30 04:19:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b0e74243-da4d-3b3c-b2a6-c50d282c9a9d | -8.41136 | -39.96635 | 2024-10-30 04:19:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2aa74011-489c-31a0-9fc2-c1cbaeaf6300 | -3.04423 | -40.0682 | 2024-10-30 04:19:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| fa3b4e84-1d89-377a-9539-525e1861bd73 | -3.0405 | -40.06762 | 2024-10-30 04:19:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 495f527b-c61e-3204-83c8-3b152f9de49a | -3.03981 | -40.07209 | 2024-10-30 04:19:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 18570081-0c52-3c4d-93d5-afd2d99cc88c | -3.95804 | -41.47533 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e1915f47-d33b-3dde-a28e-6212d014e6f2 | -3.95393 | -41.47868 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 083afd03-0d48-3fdf-8f4d-1cea918804b6 | -3.95042 | -41.47814 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 128b5cd9-2cfe-3d58-ad89-b19ce48277f9 | -3.94982 | -41.48204 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1f4fdb6e-d016-314c-86b8-c97b3937ce74 | -3.94631 | -41.48149 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 68bbe490-9eba-3cdb-b54d-417c34379b8a | -3.853 | -40.70417 | 2024-10-30 04:19:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c254dcfa-5e1a-37d3-9989-5927421b6460 | -3.85234 | -40.70842 | 2024-10-30 04:19:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6c518ace-1ff8-3a5c-9ae0-670bcdc7ca04 | -3.84936 | -40.70362 | 2024-10-30 04:19:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72f069e8-f13d-37f5-974b-4a56059509b4 | -3.8487 | -40.70788 | 2024-10-30 04:19:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20a70990-c563-3583-9306-495cfb53b932 | -4.20844 | -40.00727 | 2024-10-30 04:19:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 55ed3c6b-1555-319d-807f-b241e544953a | -5.94362 | -40.89254 | 2024-10-30 04:19:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 21583e2a-fa45-3e67-8c73-c1515784f21a | -5.75819 | -41.76336 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a46e63a4-6ffe-37ec-a760-5dd5604c25bd | -5.6191 | -41.72702 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 66f7943c-a316-318e-8525-80ffae2efc8a | -5.61557 | -41.72647 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4362530c-faab-3948-9208-8b60daa85f41 | -5.61204 | -41.72593 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 975dbf8c-9bbe-39db-bf52-90bfb9631cb1 | -5.60851 | -41.7254 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f3b9e249-fa19-3da2-86d4-5eb0a4d09805 | -5.60498 | -41.72487 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 41756d9c-a1ce-383e-8f4f-c587506621b0 | -5.60123 | -41.60592 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af267dca-e158-3cbc-b3ad-8a798f46f196 | -5.56725 | -41.2552 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eec20231-f236-338d-b017-ed700492e2ec | -5.56662 | -41.2594 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c627a0d5-c744-3b44-802d-793be221e08c | -5.56365 | -41.25462 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 11089674-e570-3f1b-85ca-554e9cb7f32a | -5.56302 | -41.25882 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d48c30a9-6208-31b2-bc14-db773fbc8f42 | -5.40449 | -41.42094 | 2024-10-30 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 720ac0ee-dce8-3536-a319-f588ef559064 | -5.40152 | -41.41635 | 2024-10-30 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 51326aed-a42c-3da1-abcd-48354a0e9091 | -5.27958 | -41.02773 | 2024-10-30 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c566ed7d-e3d6-38a3-985a-5e70ba4619ba | -5.27385 | -41.23617 | 2024-10-30 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b67b8e18-ee80-32c5-82d6-93bb05bd2ea0 | -6.46932 | -40.79841 | 2024-10-30 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 79c0aa1f-b382-34aa-99f4-05848343ec41 | -6.37381 | -41.74048 | 2024-10-30 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 78e9339a-efa5-3cc6-a39a-6dddf8b596cc | -6.36315 | -41.56829 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7ae9171f-04bc-3ee6-8d5f-d1961b57816c | -6.35957 | -41.56768 | 2024-10-30 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30dd0540-978b-3269-a3f7-37864797e944 | -6.35181 | -41.57059 | 2024-10-30 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| db23d660-d678-3add-880b-2c0315eca5bb | -6.35047 | -41.60429 | 2024-10-30 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2feda1fc-be35-3749-a89f-91a4365a8c4e | -6.34823 | -41.57004 | 2024-10-30 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4a22e2b9-649e-3894-a4ef-9825b565b33f | -6.34762 | -41.57413 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ec69c898-73c4-375b-a986-1c2120f65729 | -6.34629 | -41.60783 | 2024-10-30 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2e2c4b0e-84af-30ac-9194-fb549f5bace3 | -6.33379 | -41.57769 | 2024-10-30 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 658dcfda-59a3-3acf-8e69-540a5320ec69 | -6.3302 | -41.57716 | 2024-10-30 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd4cc2a7-4057-30fc-a23d-b96efc724580 | -6.29199 | -41.89976 | 2024-10-30 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e6bef630-43b3-3508-b68b-c144768dd50a | -6.29142 | -41.90086 | 2024-10-30 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 51148777-379c-3013-b864-df96198ea595 | -6.27551 | -41.91055 | 2024-10-30 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2ddc4725-e074-3a9b-85fe-5b7e503ea422 | -6.22475 | -41.26394 | 2024-10-30 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 621c0d8e-4e67-3132-a9b4-7b694e6c2f1b | -6.22111 | -41.26346 | 2024-10-30 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e0af79f0-e45c-315e-9a39-e465528cf680 | -6.21195 | -41.27494 | 2024-10-30 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a9c64d50-82aa-346b-8240-8195656cc3d5 | -6.15928 | -41.86522 | 2024-10-30 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c0ae25a9-6f58-3b12-b4fc-06e519a0a963 | -6.15867 | -41.8692 | 2024-10-30 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bda54ecc-9819-354d-a784-830df1831cb8 | -6.15663 | -41.78776 | 2024-10-30 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README33.md)
