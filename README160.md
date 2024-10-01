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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bc80e85-90b4-31d4-8c6e-e7116b825ab7 | -17.1778 | -56.1612 | 2024-10-01 08:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 348ee1bf-b248-3a07-bd4c-8518a054a6f3 | -18.6011 | -53.0412 | 2024-10-01 08:36:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 44.5 |
| da7f99d4-3748-3cba-919f-7b4eb0a1c7a7 | -18.6973 | -57.333 | 2024-10-01 08:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 7eb9fe15-a090-3c41-af68-922f8cc14367 | -11.6555 | -64.9991 | 2024-10-01 08:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 158f6e75-4a6a-3000-8433-709f32df3df8 | -16.6316 | -57.2557 | 2024-10-01 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 5f1bfe08-cc5d-3802-975d-15db1e1b3d88 | -16.6319 | -57.2352 | 2024-10-01 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 578779ef-7fbb-38f7-a975-e9ae9de3654e | -16.6512 | -57.2535 | 2024-10-01 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| 1448ab1b-2234-355c-adff-ba29b729b578 | -16.6515 | -57.233 | 2024-10-01 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| c5344039-038c-3d89-b52e-72507c1edabf | -16.7079 | -57.3696 | 2024-10-01 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| e9cf086c-a826-3a0a-98cd-added77f3c25 | -17.0898 | -56.7297 | 2024-10-01 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 1dd12138-bf7d-3c68-8b81-136f11ae8d6c | -17.1574 | -56.2052 | 2024-10-01 08:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 3854392d-4c8e-3a04-8200-e26259646c3f | -17.1577 | -56.1844 | 2024-10-01 08:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 40e5af86-8487-3589-b14f-7eb7f41f4207 | -17.1767 | -56.2234 | 2024-10-01 08:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 5bff6454-f3fd-3e97-8415-06422d7c9f47 | -17.1771 | -56.2027 | 2024-10-01 08:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 112.8 |
| 3f213a2e-785c-3721-8916-f686bdbc255d | -17.1778 | -56.1612 | 2024-10-01 08:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 72bbc38b-7aa5-3ab4-81cb-f3232ac3f09e | -18.6973 | -57.333 | 2024-10-01 08:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| bc54dd52-c72a-35f8-8e6b-06fa2f6de2b2 | -18.6977 | -57.3123 | 2024-10-01 08:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 1dae0785-7f5d-35cd-a6db-f29fa206f80b | -11.6555 | -64.9991 | 2024-10-01 08:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 9185d6f1-fa6f-305a-89bb-2f4ada963c01 | -16.612 | -57.2579 | 2024-10-01 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.1 |
| c04a2051-389f-332d-9bfd-d4ebc4bb7225 | -16.6316 | -57.2557 | 2024-10-01 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| 9672004a-7c2b-3ce6-8ebe-38a9763b6b8b | -16.6319 | -57.2352 | 2024-10-01 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| 7838631a-093d-3278-950a-47c878215f57 | -16.6512 | -57.2535 | 2024-10-01 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 358a38d8-5e78-383a-bf55-9ad558053ee0 | -16.6515 | -57.233 | 2024-10-01 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.8 |
| eec694cb-9a94-30c1-9c60-4181bdd78cf2 | -16.7079 | -57.3696 | 2024-10-01 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| ef955697-9af0-306d-b167-3ee99caf8573 | -18.6973 | -57.333 | 2024-10-01 08:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 41dcb271-2bf7-3751-9102-0db91b8aa23d | -2.85 | -50.72 | 2024-10-01 09:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b20d387-dbb7-3d87-a476-7fd38ee03925 | -2.88 | -50.73 | 2024-10-01 09:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a572417c-5a9d-3212-ad3d-9602b8ba5ef4 | -11.6555 | -64.9991 | 2024-10-01 09:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 5b9032d7-8bd5-3dc7-98e3-cf7eb45b7064 | -12.8586 | -62.8596 | 2024-10-01 09:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 56455ff0-b2ff-3318-889a-3db395d8387a | -22.3707 | -49.3244 | 2024-10-01 09:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 150.2 |
| 7542fa74-f3b8-3c4c-9407-633ab17af455 | -12.8397 | -62.8607 | 2024-10-01 09:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7b8e2d59-0da5-3d26-94f6-3a0c6fd116e1 | -21.5871 | -47.8591 | 2024-10-01 09:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 587910cd-c8b6-3583-be47-5076934f6ef6 | -22.3707 | -49.3244 | 2024-10-01 09:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.4 |
| 99ad9a1c-58b1-329b-ac9e-a9f1196cceac | -22.3707 | -49.3244 | 2024-10-01 09:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 117.5 |
| 174dfb86-3d94-3f13-8531-7168a8e12694 | -17.1771 | -56.2027 | 2024-10-01 09:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 67aeb516-ca0e-3b5b-88a6-35704b6d5add | -22.3707 | -49.3244 | 2024-10-01 09:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.9 |
| ff79844f-2fc4-3ffb-8768-d6d8a2be39f9 | -22.3707 | -49.3244 | 2024-10-01 09:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.7 |
| f5cae340-1d27-3777-b98d-d54676ed9e03 | -17.1771 | -56.2027 | 2024-10-01 09:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| b2df0853-db84-37b9-a34e-5cf16c30fbe3 | -22.3707 | -49.3244 | 2024-10-01 09:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 127.3 |
| 6d288967-5d49-303c-abde-99c93d47c26c | -17.1767 | -56.2234 | 2024-10-01 10:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 6449bd14-ea86-3e4d-b44e-d2d3776cebda | -17.1771 | -56.2027 | 2024-10-01 10:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.9 |
| e743f2c6-8837-34da-9e84-9bb5976b9667 | -22.3707 | -49.3244 | 2024-10-01 10:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.2 |
| b24dfd37-ac00-33d3-b9f0-c973e66ea796 | -13.218 | -48.5797 | 2024-10-01 10:16:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| f252ccd8-feee-3e28-8ef9-0a50401165b5 | -13.2373 | -48.577 | 2024-10-01 10:16:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 8b290ad6-5aa7-3fbd-817f-c7a5c9e4de84 | -17.1574 | -56.2052 | 2024-10-01 10:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 5d511b5a-7940-361c-ac27-1d1e0555a659 | -17.1767 | -56.2234 | 2024-10-01 10:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 112.3 |
| bf180b0c-9b5a-328b-96d0-71531c695551 | -17.1771 | -56.2027 | 2024-10-01 10:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 0021f7d1-82c0-314a-84ca-8b48d7288a66 | -17.1964 | -56.2209 | 2024-10-01 10:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.8 |
| b63e3f54-9f39-3308-bb8f-59c2df434775 | -17.1967 | -56.2002 | 2024-10-01 10:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| ff0630e2-e663-3761-af3b-735751289947 | -13.2373 | -48.577 | 2024-10-01 10:26:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 854e01cb-d5eb-3710-a585-8ddaae232be8 | -16.7471 | -57.3651 | 2024-10-01 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 5819c4e1-27a5-39fa-91ef-07bc96670b97 | -17.1967 | -56.2002 | 2024-10-01 10:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| 13cc24a0-00f7-363c-8ef4-2376e0dea21c | -17.1574 | -56.2052 | 2024-10-01 10:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 7c7db477-6e28-3109-a207-6daf0682f480 | -17.1767 | -56.2234 | 2024-10-01 10:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| 4fc4b57c-b73b-3d54-a720-095eb7bedcbe | -17.1771 | -56.2027 | 2024-10-01 10:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 128.9 |
| 00ac6182-198a-3a96-a83e-b36d7141cd9e | -17.1964 | -56.2209 | 2024-10-01 10:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 114.8 |
| 75265463-31c6-3b75-ac86-ed5dd772f4ef | -22.3707 | -49.3244 | 2024-10-01 10:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.4 |
| 918361f8-8532-3b02-8e0a-d18085c91518 | -12.98 | -51.3213 | 2024-10-01 10:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| ad019b98-3008-3131-b6ba-75a99ccdf0cc | -13.2373 | -48.577 | 2024-10-01 10:36:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 7decc2cb-4a1f-3472-93a6-41011923a68e | -13.218 | -48.5797 | 2024-10-01 10:36:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| e21596b8-381b-33a1-87a7-0df0be4334a0 | -17.1771 | -56.2027 | 2024-10-01 10:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 193.4 |
| d9f32938-6388-3f3f-aa93-20205f58d698 | -17.1964 | -56.2209 | 2024-10-01 10:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 254.6 |
| 78e65d47-2e02-3a62-bcc5-cd4ed946945e | -17.1967 | -56.2002 | 2024-10-01 10:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 179.4 |
| 1ce200bb-9f10-3215-b6c8-d8814d12bc5f | -17.1767 | -56.2234 | 2024-10-01 10:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 251.6 |
| 327ea6fd-3a69-3d74-ae67-76ce0f1a783a | -21.5871 | -47.8591 | 2024-10-01 10:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 198.1 |
| c3b5c81c-a1b0-304b-bfb5-ea681520e768 | -21.5864 | -47.8827 | 2024-10-01 10:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 128.3 |
| baedf4a7-41a5-3f60-bd2d-ee03ac42c7e3 | -21.6078 | -47.854 | 2024-10-01 10:37:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 108.0 |
| f8ab70ef-192b-3703-a399-22e3044607de | -22.3707 | -49.3244 | 2024-10-01 10:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.0 |
| e3eb81c6-8ccc-3c32-a4a8-fd1fbb1abc8b | -12.9995 | -51.2976 | 2024-10-01 10:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 0652267f-bcc7-361a-89a2-29c350b7a12e | -16.7471 | -57.3651 | 2024-10-01 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| ac66574f-751b-3ba4-a070-3cae04fa2ec4 | -17.1574 | -56.2052 | 2024-10-01 10:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 2fab3648-9988-308c-968d-55dd5f63154d | -17.1767 | -56.2234 | 2024-10-01 10:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 226.2 |
| fb435be1-b000-39ca-a48c-1051d79738ed | -17.1771 | -56.2027 | 2024-10-01 10:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 180.9 |
| 522ebd9f-2bac-3319-bd3d-84c2fed920c2 | -17.1964 | -56.2209 | 2024-10-01 10:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 174.1 |
| 6244942d-66b1-3d7a-9185-a75611237c82 | -17.1967 | -56.2002 | 2024-10-01 10:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 123.5 |
| 114431be-5945-3946-919f-33a1f093f2d3 | -21.6078 | -47.854 | 2024-10-01 10:47:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 118.0 |
| a3972409-6b04-3c07-ad80-3fb9370fa03a | -21.5871 | -47.8591 | 2024-10-01 10:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 9ca072dd-402d-32f6-ac63-69e68002a1fd | -22.3707 | -49.3244 | 2024-10-01 10:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 156.2 |
| 5c0c8cce-faa3-349f-a8ab-bac32752b466 | -16.7471 | -57.3651 | 2024-10-01 10:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 0454b8e1-4c4f-3a83-90a4-0582f76d0588 | -17.1574 | -56.2052 | 2024-10-01 10:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 4bae1686-3aeb-3d27-b9b6-006c09435f21 | -17.1967 | -56.2002 | 2024-10-01 10:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| c87cd7fe-d927-3d61-b08d-bbed97028000 | -17.1771 | -56.2027 | 2024-10-01 10:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| f5a3c04e-30ce-3ded-926a-c7173c0c5497 | -17.1964 | -56.2209 | 2024-10-01 10:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 159.7 |
| 425902b6-a201-3383-8bca-5b3cfacd657f | -17.1767 | -56.2234 | 2024-10-01 10:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 120.2 |
| 0f6a073f-7b0c-380f-8b1c-95bd4055a2f4 | -21.5871 | -47.8591 | 2024-10-01 10:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 960ae891-3fa5-33a1-955f-0054af4369e2 | -21.6078 | -47.854 | 2024-10-01 10:57:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 851e7e68-fb73-35b0-ae86-0b6621bc3e57 | -22.3707 | -49.3244 | 2024-10-01 10:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.9 |
| bdc36891-d550-3b92-8abb-7dcc9a9abc5b | -12.9995 | -51.2976 | 2024-10-01 11:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5acf0b3f-bd02-3d43-a9d3-0897a50f7908 | -12.9803 | -51.3 | 2024-10-01 11:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 95a76b6d-af3f-3048-a515-980b0da6c5e3 | -17.1964 | -56.2209 | 2024-10-01 11:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 132.5 |
| 60afd3e6-4b99-3676-9fbf-e48cffabcbae | -17.1771 | -56.2027 | 2024-10-01 11:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 02fffa1f-c10b-3697-9a55-82329428fa9b | -17.1967 | -56.2002 | 2024-10-01 11:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| a83790d0-0753-30e8-88ce-3c3dcd5dd64d | -17.1574 | -56.2052 | 2024-10-01 11:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 9df6b325-325e-35bc-85ed-cc95967a3664 | -17.1577 | -56.1844 | 2024-10-01 11:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 813139fb-36da-308b-9544-3ae7e83b71ab | -17.1767 | -56.2234 | 2024-10-01 11:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| 632e06da-729e-339e-8f93-513a0322a4f1 | -21.5864 | -47.8827 | 2024-10-01 11:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 91f5c379-ac8f-3309-b9a8-675c9c21feb0 | -21.6078 | -47.854 | 2024-10-01 11:07:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 685dff3f-3f30-31e9-92cf-1b8cada8a779 | -21.5871 | -47.8591 | 2024-10-01 11:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 244.1 |
| aadb8195-82d1-3abd-b84b-f6a1d08ed23e | -22.3707 | -49.3244 | 2024-10-01 11:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.7 |
| 1e35729a-7be6-3c12-ab24-2e7be7ea70a9 | -10.996 | -46.5418 | 2024-10-01 11:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |


[Clique aqui para ver as próximas entradas](README161.md)
