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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02c4c55d-3fc0-35b4-b77b-c2683ab07dda | -9.0642 | -45.0749 | 2025-07-23 01:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 33e5d8e5-2984-3e9d-b49b-2e8ec65ff619 | -7.7569 | -44.0183 | 2025-07-23 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| fbeefa4f-6847-3246-80ae-83d9c7757628 | -3.1832 | -49.4642 | 2025-07-23 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 9e21cc76-4b8c-3e0d-910e-bbc3dc728cbb | -7.1966 | -45.3313 | 2025-07-23 01:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 7bbc786c-3a5d-3970-affd-f6df3b369ddf | -9.0646 | -45.052 | 2025-07-23 01:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| d3761b4f-a718-34f5-b133-de2832931c1d | -3.1648 | -49.4648 | 2025-07-23 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| ded175ca-be81-31f0-ac43-42e7feef2db6 | -3.1649 | -49.4435 | 2025-07-23 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 8d6c111f-e9d1-3f70-9c81-3ac810f19bb6 | -3.1832 | -49.4642 | 2025-07-23 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| b68a356a-a2df-3cdc-bd9c-96edc5b010f6 | -7.7569 | -44.0183 | 2025-07-23 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 3646bd8a-b174-38e7-837d-6391b042186e | -3.1649 | -49.4435 | 2025-07-23 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 9ea5d8bc-88fb-3db3-ab22-6ff2e4937855 | -3.1833 | -49.4429 | 2025-07-23 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 95477837-8ec4-3658-82b9-0fea548dd4e7 | -3.1648 | -49.4648 | 2025-07-23 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 176.9 |
| 08f25b16-8cda-3f62-9b71-c40b502ac304 | -3.1648 | -49.4648 | 2025-07-23 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| b649e2c8-8c84-3741-855d-298a90c6e5fb | -3.1833 | -49.4429 | 2025-07-23 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 64d1571d-29ae-395c-bab3-ff90cb25f6e6 | -3.1649 | -49.4435 | 2025-07-23 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| cfb2f00a-0abf-383a-a87c-268829702387 | -9.0646 | -45.052 | 2025-07-23 02:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 94de5bb3-0d4d-3457-b581-af778c1989dc | -7.7569 | -44.0183 | 2025-07-23 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| b26bdecd-a882-3987-b7cd-606660c11876 | -3.1832 | -49.4642 | 2025-07-23 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| ed5e37ab-e134-32b8-8ff4-0b8e230061c4 | -9.0646 | -45.052 | 2025-07-23 02:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 73b2e6d5-68bb-3433-a54c-9431df8d44b0 | -3.1833 | -49.4429 | 2025-07-23 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 8542e3de-9c90-3e74-b539-a99ef5ecc544 | -3.1648 | -49.4648 | 2025-07-23 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 62f6968b-10a8-3254-87d7-f29c31b390d4 | -7.7569 | -44.0183 | 2025-07-23 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| e5052acb-a53e-335c-b8c2-631deae2ec2b | -3.1649 | -49.4435 | 2025-07-23 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 202d2465-09ba-3c96-a761-483556bb6641 | -3.1832 | -49.4642 | 2025-07-23 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| b23e5d5a-5ce6-34c2-b0cb-3f120439ac65 | -3.1648 | -49.4648 | 2025-07-23 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 9cda837a-11ed-368f-8d73-f53b94f2740c | -3.1832 | -49.4642 | 2025-07-23 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 1b9eb49e-6b13-394a-8d51-92d53e104b8b | -9.0642 | -45.0749 | 2025-07-23 02:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| c6b5c0c8-dc19-39fe-8c6e-b1f697bd3507 | -9.0646 | -45.052 | 2025-07-23 02:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0a3d971a-b721-3cde-9d7f-3457c536cbe4 | -3.1649 | -49.4435 | 2025-07-23 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 248187ba-4313-3448-a324-b75fb1b8fab1 | -7.7569 | -44.0183 | 2025-07-23 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 7df5278e-e044-3dd1-85d2-4a338b1befe4 | -3.1833 | -49.4429 | 2025-07-23 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| f7738ec1-8359-3e2f-95a0-aeb5c2a53ff7 | -3.1649 | -49.4435 | 2025-07-23 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 918851d5-442b-3d57-8f3d-f0278976eff3 | -3.1833 | -49.4429 | 2025-07-23 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 1b50d103-706b-3161-bc7d-e0e7f87e3ae5 | -7.7569 | -44.0183 | 2025-07-23 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 0c9a1977-1a7d-33eb-a348-4ffa84f2efeb | -9.0646 | -45.052 | 2025-07-23 02:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ee6c4129-ee4b-36ea-b38a-505313b240d9 | -3.1832 | -49.4642 | 2025-07-23 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| cf0e958d-53a9-3de9-87f7-e45fb713810e | -3.1648 | -49.4648 | 2025-07-23 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 7288354c-0829-387b-b472-68a0cee9106c | -3.1832 | -49.4642 | 2025-07-23 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| aa06ba6c-e0dc-35f9-9668-f00ccfd48370 | -9.0646 | -45.052 | 2025-07-23 02:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 7a17bfe3-9f67-36c8-92b3-45bf430221b0 | -3.1833 | -49.4429 | 2025-07-23 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 7fdcea54-3788-398e-8f7c-4926ed426da1 | -7.7569 | -44.0183 | 2025-07-23 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 2928a72e-462f-3a44-a35d-328a96846059 | -3.1649 | -49.4435 | 2025-07-23 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 340e30cb-4f62-33ba-8df5-07ab929201bf | -3.1648 | -49.4648 | 2025-07-23 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 439dc198-2b11-34be-bed3-50b4e2c745d5 | -3.1832 | -49.4642 | 2025-07-23 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 967dca19-5dec-30b3-be96-bbf5ebea2775 | -3.1648 | -49.4648 | 2025-07-23 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 71ba7dfe-6ccd-3b9c-b0b4-c4b819e2ca0d | -3.1833 | -49.4429 | 2025-07-23 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| e723e7e7-275f-3281-83a7-6dcb2d73b2e0 | -9.0646 | -45.052 | 2025-07-23 02:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 0e9cc205-b402-3be8-a4a3-8d123cb73bc8 | -7.7569 | -44.0183 | 2025-07-23 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 78e4f946-e5bf-367a-9dd2-063a31d0f217 | -3.1649 | -49.4435 | 2025-07-23 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 14f4bfdf-3ac8-3fff-b0bb-2b6c0d123442 | -3.1833 | -49.4429 | 2025-07-23 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 8d7197f0-870d-3101-9529-f6c6a4affb0b | -7.7569 | -44.0183 | 2025-07-23 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 98f7bc95-a1b8-376c-9c13-916e3ba361f6 | -3.1832 | -49.4642 | 2025-07-23 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 259dd9b7-7dce-322e-838f-83d3548d9f18 | -22.8016 | -52.482 | 2025-07-23 03:00:00 | GOES-19 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.8 |
| 91fb8dba-1a33-3d77-a06d-b2126d310fa9 | -3.1648 | -49.4648 | 2025-07-23 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| e2385e6c-b667-3eeb-8f93-33614ee3889c | -22.8225 | -52.4776 | 2025-07-23 03:00:00 | GOES-19 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.0 |
| 4ef49761-a7e0-3eb0-890d-ae6edb8c9be6 | -3.1649 | -49.4435 | 2025-07-23 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 8bb9c240-0dd6-365e-984b-4c897014b39a | -3.1649 | -49.4435 | 2025-07-23 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 69904235-2c7e-36aa-9275-01270d3e23b2 | -7.7569 | -44.0183 | 2025-07-23 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a4a2efcf-3e81-3be7-9db0-5141fbc8b122 | -3.1832 | -49.4642 | 2025-07-23 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 5ba21e8b-d2f5-3e9e-ab61-c753df6a0ffd | -3.1648 | -49.4648 | 2025-07-23 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| c82586c5-4e5f-31cb-9700-7b9ea97bc0dc | -3.1833 | -49.4429 | 2025-07-23 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 72863924-8b20-304b-821e-3028e4d45534 | -4.58006 | -38.2993 | 2025-07-23 03:17:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2a0beb79-e743-365e-bf2f-e5041fb26213 | -5.36093 | -36.89524 | 2025-07-23 03:17:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 967158b8-b754-38c6-9048-8f1819ec2921 | -4.25489 | -39.22845 | 2025-07-23 03:17:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5f055582-bce0-3ab6-8800-e59c0776effa | -5.36041 | -36.89819 | 2025-07-23 03:17:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c1f4849d-f729-36ee-b5ac-c6c763675bdc | -4.5857 | -38.30024 | 2025-07-23 03:17:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dafb3836-521d-39e1-803b-83562c335a72 | -9.6544 | -40.59278 | 2025-07-23 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4bcf6293-932b-3675-9af6-a80de70983b1 | -13.5438 | -43.71136 | 2025-07-23 03:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2895157-b7fb-3300-8511-933e9fb65fc4 | -6.60807 | -42.41026 | 2025-07-23 03:19:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 2e58c284-2620-316a-9388-fc2fa4e9d1db | -9.65527 | -40.58826 | 2025-07-23 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9e534d5-a751-3644-85cc-97629a89e8ef | -6.60734 | -42.40288 | 2025-07-23 03:19:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 9004b889-83cf-3cfc-ac85-0d95d983d634 | -8.01126 | -37.0745 | 2025-07-23 03:19:00 | NPP-375D | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 74cb1d4a-eed1-39e8-a817-2494547da231 | -8.01284 | -37.07639 | 2025-07-23 03:19:00 | NPP-375D | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bcbb0151-beaf-391c-bbb1-5680b31cd8fe | -6.60602 | -42.40977 | 2025-07-23 03:19:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 14a1a59f-1d9e-3198-8418-4b4b987a0b29 | -13.53709 | -43.70984 | 2025-07-23 03:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a80f260-d2a8-3c1b-b129-25454ffb69ae | -6.60934 | -42.40337 | 2025-07-23 03:19:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 643d46a2-584e-3baf-8bb1-35bd9e8041a9 | -3.1833 | -49.4429 | 2025-07-23 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 18731d46-5bd2-3083-90a4-bc154860f8c2 | -3.1649 | -49.4435 | 2025-07-23 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 0e3b77be-ddec-3cef-af4c-5d02413821b8 | -3.1832 | -49.4642 | 2025-07-23 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| ed54f297-8b85-3801-8359-0e01362e1d94 | -7.7569 | -44.0183 | 2025-07-23 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f214a03c-bf5b-33e5-8e2a-4507fd8e2462 | -3.1648 | -49.4648 | 2025-07-23 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| b30ac489-29cc-3ef0-b380-e2f3f0faac1d | -17.50934 | -39.94612 | 2025-07-23 03:21:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f760587a-befb-3d0a-8981-585dcefa0680 | -15.57394 | -41.07143 | 2025-07-23 03:21:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c9988b7c-9f1e-3441-a941-59589423a0b7 | -15.57473 | -41.06765 | 2025-07-23 03:21:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1e6fcb9c-a725-3663-88c4-f13820cb0343 | -17.51056 | -39.94022 | 2025-07-23 03:21:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a95713c4-8096-3afc-a150-9e820636d4be | -16.09931 | -42.28033 | 2025-07-23 03:21:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c71c4eea-9413-3989-971b-987fe352bc49 | -17.51024 | -39.94614 | 2025-07-23 03:21:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 540f9d59-5892-3dda-9b3e-643332206949 | -3.1833 | -49.4429 | 2025-07-23 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 80a35850-81e8-3fd6-b00d-e39544d4689a | -3.1832 | -49.4642 | 2025-07-23 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 7a0926c3-127b-3beb-84d4-f6fb64bf88fd | -3.1649 | -49.4435 | 2025-07-23 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f6e6f252-67ea-38ff-bdeb-1248bdd2e3d4 | -3.1648 | -49.4648 | 2025-07-23 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 4b119a23-f721-3477-ba44-3015311771c7 | -7.7569 | -44.0183 | 2025-07-23 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 57c6c94e-b620-3f0e-8c0e-91a2f48a692e | -3.1649 | -49.4435 | 2025-07-23 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b578373a-aba8-3299-85ad-7c57ee91b885 | -3.1832 | -49.4642 | 2025-07-23 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| dbd85c9e-fd07-3646-8fe6-142e4fde801c | -3.1833 | -49.4429 | 2025-07-23 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| aed7f0c6-293d-352a-b60e-fa8f855c6e70 | -3.1648 | -49.4648 | 2025-07-23 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 4d7934f5-a441-3159-9a24-7654a531b9a4 | -4.58383 | -38.29685 | 2025-07-23 03:40:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7b4c8d41-3164-3ed2-a6f2-6fd911bdfafc | -4.09397 | -46.92617 | 2025-07-23 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 662ba970-328e-3304-b3ac-f4b4d1df2720 | -4.04949 | -42.52107 | 2025-07-23 03:40:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| b774e99b-538f-3b60-be85-657422db458e | -3.8227 | -43.02161 | 2025-07-23 03:40:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
