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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed1ab9d7-0215-384c-9ef6-328d6544b4ac | -19.77059 | -57.9857 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c53a8efb-7f09-3661-bda1-0e3948292e50 | -20.21021 | -56.61794 | 2025-11-12 05:25:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 082f1268-c2d8-3b55-8985-16a453f7601f | -19.78864 | -57.97619 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 57a3ec7c-c83c-3741-a435-862dee8cc4c5 | -16.88463 | -51.65771 | 2025-11-12 05:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ee48149e-55eb-3403-bc29-b5824f66ff0f | -20.22538 | -50.90402 | 2025-11-12 05:25:00 | NOAA-20 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5f9b3469-9eff-3d4d-bc33-b255e18c9d4a | -19.74648 | -58.01031 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 55c4d657-e96b-312f-b80c-c1aade1a9a5f | -19.76084 | -57.99635 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 744b47f5-d4f9-3e83-877a-74bc671795ec | -19.84431 | -58.01895 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9329aa19-c9d3-3c41-8bc6-efb4701587a7 | -19.75159 | -58.00304 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6329984a-89b9-3910-bfda-d46f06170719 | -19.80836 | -57.98697 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d9d4889d-3dc0-3cf4-abba-17ac5a405d33 | -19.76498 | -57.99693 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ab5bc15f-3475-3b80-a5e7-6477366adfcd | -19.72611 | -58.03927 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f3d418a9-a501-3687-8dda-08a7fe262cd8 | -19.76961 | -57.99357 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 49b34ab1-1cc7-3847-9b4f-aeced05136b8 | -16.46299 | -58.15821 | 2025-11-12 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e322ee7b-f6dd-36b1-99f0-40823bce4c41 | -20.89151 | -50.10112 | 2025-11-12 05:25:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 544fd122-0983-391c-8a91-8f7fa0160683 | -19.85404 | -58.0083 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 32b71bea-5252-370f-afd0-f6e882231b05 | -19.8125 | -57.98755 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 34950843-2629-351c-a0aa-e5b05c8e098f | -19.75208 | -57.99911 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ffc64eed-f6f7-39aa-85cc-3d7b31f5c866 | -19.84114 | -58.0105 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 76940a86-9209-3931-987b-35e8241844c8 | -18.47951 | -53.40218 | 2025-11-12 05:25:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c467e7ab-1103-33ca-9b14-09d0e8d0ab8f | -19.85039 | -58.00378 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| fabc3b96-6d0e-3680-8948-bf7879fdafcb | -19.72659 | -58.03537 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 67c6128e-f1bd-31e9-98cc-28a26f8cfec2 | -19.79279 | -57.97677 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| daa70ea1-307f-3c7b-8f7c-9f5b991a35b1 | -19.8499 | -58.00772 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 68696b93-b55f-3294-8aab-a098aedc4a6e | -19.72198 | -58.03869 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 58cfe501-aabb-34a1-85d9-7ac6a06f7d6d | -19.7701 | -57.98964 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8d7337c0-ad5e-3e81-a336-3aa2af78f2a1 | -18.47404 | -53.40125 | 2025-11-12 05:25:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fb20293-3972-3920-a849-bd30dec987e5 | -19.83749 | -58.00598 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 014f098b-0a5b-31fc-8323-7fc5d78c406f | -19.80371 | -57.99033 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0cbc4e8b-f88a-3f48-aca3-8ffa4a571f9d | -16.89108 | -51.65428 | 2025-11-12 05:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b5ae49f-e657-3c21-ae9c-248725f0fe2e | -19.84577 | -58.00714 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 04fefbe0-7f3f-35ce-9ead-c0e5370797e9 | -19.76035 | -58.00027 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2058edd8-52e4-39ea-8f2b-fcb2e9909f43 | -19.81664 | -57.98813 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| a546405b-6032-35f7-9d82-15568fe85321 | -19.76911 | -57.99751 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8bba6e84-1db7-317d-b9d0-4ff0ebf8df4d | -19.75621 | -57.99969 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 27be7ad7-12dd-33b9-8f7c-7e06a5e5455a | -16.87911 | -51.6522 | 2025-11-12 05:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79dff6b0-86af-3215-8ee6-94e48d2a74ef | -19.79693 | -57.97735 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| ade0d8a9-050f-3d88-a03b-530a348f4217 | -19.74746 | -58.00246 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 84b98088-a8dc-3f8f-9bb2-8f2bc525d917 | -20.21069 | -56.61869 | 2025-11-12 05:25:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b1a2105f-de03-3297-80cb-3cc9781de1ec | -19.83287 | -58.00933 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| feda23b0-2c34-35a3-a73b-d02cccad1cb8 | -19.837 | -58.00992 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e83b96ac-7d26-388c-b39b-ce66365e0c06 | -17.24137 | -56.02151 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 37f19074-faf0-3a4a-9383-c7f8a3bdcb4a | -19.746 | -58.01423 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 839e5aa8-f6a2-32df-80f7-d945b6c511dc | -19.813 | -57.98361 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 0ba3fc69-00a5-358e-bda4-4bb5b42efcd6 | -19.74551 | -58.01814 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d9c91a26-798e-32f2-91ae-c71f8d0acc18 | -16.88509 | -51.65326 | 2025-11-12 05:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b852161f-d53d-34db-aabb-ca58acbe234b | -16.45928 | -58.15549 | 2025-11-12 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f918e0f6-6e13-3f65-bee8-819ed154f0c7 | -20.21124 | -56.61382 | 2025-11-12 05:25:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 60178456-7eb0-3772-a0b9-782acc5aa85b | -20.89096 | -50.10815 | 2025-11-12 05:25:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7a260c29-8fb7-3d31-a7ed-c05050d204ef | -19.84163 | -58.00656 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e8225f7f-2a54-3515-a5b5-efc6be7066f7 | -19.78815 | -57.98013 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7f341a06-02d7-389a-9847-4e5e6625304c | -16.46319 | -58.15607 | 2025-11-12 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 770da1a2-0bea-3acf-abcc-5380022599a5 | -20.22488 | -50.90979 | 2025-11-12 05:25:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 27622192-cfe2-3477-8edf-b4488eb0979b | -10.52995 | -47.99488 | 2025-11-12 05:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a68ed08-9987-3cbc-9356-9f89227f728b | -4.0976 | -48.0144 | 2025-11-12 05:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9d420b74-c236-38f3-9fa3-237aca3babef | -4.1161 | -48.0136 | 2025-11-12 05:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| a74e4465-7f01-3146-b7a0-f456a4075181 | -4.0976 | -48.0144 | 2025-11-12 05:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 0b1ad5ee-015a-323c-b4b6-dd28865880ff | -4.1161 | -48.0136 | 2025-11-12 05:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 80f2fb99-06eb-340d-9d7b-3010890b3699 | -4.0976 | -48.0144 | 2025-11-12 05:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d9d28e2e-2136-3d67-9862-07a82e8124d9 | -4.7853 | -42.6796 | 2025-11-12 05:50:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 00563252-d470-3d4b-bca3-c15c925e508d | -4.1161 | -48.0136 | 2025-11-12 05:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 2c63f10b-880d-364d-b5d2-e254aa6a3ef6 | -4.1161 | -48.0136 | 2025-11-12 06:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f4d9dfc0-94e5-3718-86b1-b911d5692726 | -4.0976 | -48.0144 | 2025-11-12 06:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| eb7ddf68-7017-3c34-864a-8266b599fe15 | -4.93718 | -44.29197 | 2025-11-12 06:01:00 | AQUA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c19769b5-1d88-3dfb-a0d5-c7fb915bf328 | -3.08494 | -49.26651 | 2025-11-12 06:01:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1781dfb1-8f31-3be6-89ac-63ca41ab76a7 | -4.11166 | -48.01353 | 2025-11-12 06:01:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c09f0778-512c-3a4b-a34f-c28bc3bc4e93 | -4.10254 | -48.01221 | 2025-11-12 06:01:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 78acbb9d-f466-3fe1-a4e2-0e0fb4387312 | -2.8693 | -51.46709 | 2025-11-12 06:01:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 489054ec-93a0-37ff-a986-8bb5fd622db0 | -4.45737 | -44.55001 | 2025-11-12 06:01:00 | AQUA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ec46bbc0-08a5-39f5-b988-16d170bd6b98 | -3.14342 | -45.24673 | 2025-11-12 06:01:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 27.8 |
| d821f97f-467a-3a43-9ed6-422c23183a19 | -4.26271 | -49.01493 | 2025-11-12 06:01:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 58415646-2ea7-3d68-aec4-5fe111821831 | -3.97984 | -47.2971 | 2025-11-12 06:01:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 13d54cc2-b459-38e2-b30f-e44b4445a35d | -4.1102 | -48.02305 | 2025-11-12 06:01:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f5d28722-c58c-3a44-aa54-4d423e7d2a42 | -2.94806 | -45.55789 | 2025-11-12 06:01:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c64e2621-017b-3385-9d70-3c9a19806553 | -4.7824 | -42.6752 | 2025-11-12 06:01:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| af296be3-fefc-3f91-b7b2-46d12ecef1c5 | -4.10108 | -48.02168 | 2025-11-12 06:01:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ac9eee21-95c8-3f7c-9df7-d9a18412c41b | -4.77026 | -42.6861 | 2025-11-12 06:01:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 54e7660c-63be-3288-a697-ddebaa119806 | -4.09851 | -48.88096 | 2025-11-12 06:01:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11753f5b-f8ac-3ea3-868b-bbc2c361a487 | -3.84672 | -50.05745 | 2025-11-12 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2a3ba3dd-b4f4-315a-8657-029bb340edee | -2.63544 | -49.19065 | 2025-11-12 06:01:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f52ffb90-7a77-344c-8599-fb549e41549b | -2.94938 | -45.54911 | 2025-11-12 06:01:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 03186201-36b0-3872-8f41-681c9c44fd81 | -4.75359 | -48.83233 | 2025-11-12 06:01:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f501a13-9227-30dd-a27d-0dee74584de3 | -4.11312 | -48.00407 | 2025-11-12 06:01:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 5a88f0ba-2f88-38d8-8e1e-d992aef3e604 | -4.78059 | -42.68751 | 2025-11-12 06:01:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 65969e5f-f3e0-3478-9d40-58a2e8183a32 | -2.86674 | -51.48362 | 2025-11-12 06:01:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 64532ca1-5a67-3c70-8bf9-56c0218b9a84 | -2.63367 | -49.20208 | 2025-11-12 06:01:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 48ceaf72-3b6a-3b8d-bde0-418f34b34f6e | -4.77206 | -42.67379 | 2025-11-12 06:01:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 911e6c03-10ae-39e2-bd0d-b481e2c506c7 | -4.10399 | -48.00278 | 2025-11-12 06:01:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8205ea14-a813-3f68-bb6d-794f030802c9 | -3.09486 | -49.268 | 2025-11-12 06:01:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35390067-85cf-3e6f-af9b-ddae4045cfa9 | -12.00705 | -46.76264 | 2025-11-12 06:03:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9fb9066b-1788-31df-8ef8-f5330ea51ba0 | -7.45461 | -44.74512 | 2025-11-12 06:03:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 61da4f1d-4f6f-36d8-ae60-70943b41786a | -10.49894 | -44.93573 | 2025-11-12 06:03:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 0d21c4f8-e0a2-3af4-8617-21a2522a4115 | -6.54145 | -43.03421 | 2025-11-12 06:03:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 74402a67-65be-3462-b0bf-576d116f52cc | -10.53071 | -47.99049 | 2025-11-12 06:03:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f6cbfe6b-3306-3d96-b296-3bbbc8115fa2 | -14.40656 | -44.3735 | 2025-11-12 06:05:00 | AQUA_M-M | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7eab0992-b025-3c6a-a989-9a3584b25509 | -20.89447 | -50.10101 | 2025-11-12 06:07:00 | AQUA_M-M | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 8655bce1-8572-3063-a7e6-16b8c0239750 | -20.94048 | -48.45173 | 2025-11-12 06:07:00 | AQUA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 20b29ee3-267a-3936-90fd-37294ba7bbf2 | -3.1655 | -45.1594 | 2025-11-12 06:10:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6e14bc67-f0a9-3d88-9dca-3cffa2ac1dd4 | -4.0976 | -48.0144 | 2025-11-12 06:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e47d412a-1b60-3d92-9360-6045eb0d3818 | -4.1161 | -48.0136 | 2025-11-12 06:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |


[Clique aqui para ver as próximas entradas](README20.md)
