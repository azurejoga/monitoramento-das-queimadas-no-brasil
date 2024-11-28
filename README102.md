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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfb59855-8bee-35ed-8bf2-319cb196ee40 | -22.6352 | -47.53477 | 2024-11-28 12:40:00 | TERRA_M-T | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 4107f5b6-4b63-3888-b8a9-525c98c8d427 | -23.72015 | -50.55678 | 2024-11-28 12:40:00 | TERRA_M-T | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| d35517a5-4ba7-3b93-8027-3e26c38bce51 | -23.37084 | -47.05229 | 2024-11-28 12:40:00 | TERRA_M-T | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 31ccc99e-c337-3894-9179-6c295b3ca8b5 | -4.6564 | -42.4048 | 2024-11-28 12:50:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 987986c7-235f-30d1-83bc-f7d49c6bbc2f | -3.9166 | -47.1949 | 2024-11-28 12:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ac26dd06-dd9a-311d-9316-88be52d8f0aa | -2.861 | -46.8406 | 2024-11-28 12:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 5dd9cb2f-07b1-3533-9661-2f40ab96d494 | -4.4845 | -42.8631 | 2024-11-28 12:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a82061b0-5c94-3808-82b9-f00ef8d5916c | -4.6753 | -42.3799 | 2024-11-28 12:50:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| 209925a4-1b90-30a5-96ef-7fb944c60282 | -3.4615 | -42.0459 | 2024-11-28 12:50:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 724a8b85-b42b-3184-9c47-e9449ac58c13 | -5.4548 | -43.2426 | 2024-11-28 12:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| ad663085-2b78-3e4e-91a4-e1d258fb8c98 | -2.8609 | -46.8626 | 2024-11-28 12:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| d142ff79-7216-3c66-b12f-14ff9efdf5ca | -4.6565 | -42.3811 | 2024-11-28 12:50:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| 7155b9cd-6de8-321f-a772-bd255149581c | -5.4546 | -43.2659 | 2024-11-28 12:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 39ab7555-816d-347c-b793-f75622e60584 | -4.4845 | -42.8631 | 2024-11-28 13:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 662f2fee-564a-3ba4-b1ea-b701ebbb6ca0 | -4.6753 | -42.3799 | 2024-11-28 13:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| 919726e6-4165-38d7-95a3-87db1067f487 | -5.4548 | -43.2426 | 2024-11-28 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 89bfb97c-f0a7-3784-af4f-17368a058412 | -2.861 | -46.8406 | 2024-11-28 13:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 7722b38c-b158-37a8-ada0-04a6a13ee5b3 | -4.6564 | -42.4048 | 2024-11-28 13:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| 106e2163-a103-3870-92ca-8e6e65ba1216 | 1.2354 | -55.9666 | 2024-11-28 13:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d651b287-26f1-3e16-8bb7-a8487ee2eca6 | -5.4546 | -43.2659 | 2024-11-28 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 7b67b239-976b-3bbe-a2bf-7d32621aa023 | -4.6565 | -42.3811 | 2024-11-28 13:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 173.0 |
| ee49603a-fa4e-3dd0-a349-447ac03b4465 | -3.62 | -41.85 | 2024-11-28 13:00:00 | MSG-03 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 565db78a-8046-3e14-a404-5336be991697 | -9.1824 | -44.7404 | 2024-11-28 13:10:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 44591d0c-a02e-3aeb-a0c5-ce8cc3ad285b | -4.6565 | -42.3811 | 2024-11-28 13:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 147.2 |
| 0a285923-96bd-3b95-bf95-8f11d920e7ba | -5.4548 | -43.2426 | 2024-11-28 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 664a0e7a-16d0-3e87-8abc-f27d55b8d11e | -2.8795 | -46.84 | 2024-11-28 13:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 840a1ee1-09ad-36d8-9c11-1c4e57290bcc | -5.4546 | -43.2659 | 2024-11-28 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| d007a4c3-a075-3c4d-a6d5-0ae0e1a74cbe | -9.1827 | -44.7173 | 2024-11-28 13:10:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| a472be43-d692-33d5-ac3d-7f619eb47ec6 | -19.3272 | -46.3302 | 2024-11-28 13:10:00 | GOES-16 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 85.9 |
| f8d33613-bb45-32d9-ba63-cf43c3d4574d | -5.9788 | -45.3621 | 2024-11-28 13:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| a20bbcaa-3613-3609-b65b-e58b7c43ba47 | -2.0305 | -45.6896 | 2024-11-28 13:10:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| ee1bbcca-a640-34b9-a1da-34944c995c32 | -2.8794 | -46.862 | 2024-11-28 13:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 51c4352c-dc0a-3ddf-b132-8968e652b700 | -6.3687 | -45.6709 | 2024-11-28 13:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 1f0652a8-7f77-3f62-a1fe-42205a5062c5 | -4.6564 | -42.4048 | 2024-11-28 13:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| f3b713ac-3185-3ae8-87be-bb7431272ceb | -4.6753 | -42.3799 | 2024-11-28 13:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 154.1 |
| c7e5317d-c9a8-35c5-a570-b45189f3c9ba | -2.861 | -46.8406 | 2024-11-28 13:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 9ff412f5-89e1-3d40-b384-c5f031ae6537 | -5.4546 | -43.2659 | 2024-11-28 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 68f23440-879a-3d5c-96af-f82c6fc63fd0 | -6.3687 | -45.6709 | 2024-11-28 13:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| eefa1dbc-fda1-3491-9edd-45f6297e8808 | -2.861 | -46.8406 | 2024-11-28 13:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 7eaa0e9f-8298-3410-91db-adf45a303bce | -9.1827 | -44.7173 | 2024-11-28 13:20:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 936bb0af-0237-3eac-b377-d076a716af75 | -5.9788 | -45.3621 | 2024-11-28 13:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| ec063e8c-5e35-3cb5-a465-7b8714af2848 | -4.6564 | -42.4048 | 2024-11-28 13:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| 6ec78ce1-5390-3ebf-948f-ca9e0ee89cb3 | -4.6565 | -42.3811 | 2024-11-28 13:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 159.1 |
| 8834f1bc-f3f6-35ee-9cac-9b6924cb1bb1 | -9.1824 | -44.7404 | 2024-11-28 13:20:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1b67cf13-9f14-3171-bcb7-b0e21b1d5ef3 | -5.4548 | -43.2426 | 2024-11-28 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2c5392b6-f591-355d-ac0a-af6e6e2e8349 | -2.8795 | -46.84 | 2024-11-28 13:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0840130d-f747-3870-93d3-96848258eccd | -4.6753 | -42.3799 | 2024-11-28 13:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 176.6 |
| 81e7f153-bb35-3dd6-964d-2dd9d957936e | -17.626 | -57.5692 | 2024-11-28 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| a1ee2e5e-803b-3ead-90ed-7297c313a16c | -2.0305 | -45.6896 | 2024-11-28 13:20:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 871b9c0c-87df-30a5-9cec-02b9a1afdeb5 | -3.0673 | -42.3955 | 2024-11-28 13:30:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 64f31a3d-ec4e-3243-b0b9-9c84d9396810 | -2.8794 | -46.862 | 2024-11-28 13:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| a1f6858a-8e73-3125-8a87-91a80944fb1b | -5.4546 | -43.2659 | 2024-11-28 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 353c3098-3c8d-3661-b241-30b3126188da | -4.6753 | -42.3799 | 2024-11-28 13:30:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 126.7 |
| 3a3b5d49-e499-3bd7-9292-c55279f40b97 | -3.4612 | -42.0934 | 2024-11-28 13:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| fd001ded-adc4-392a-8d58-1e368443e505 | -4.6564 | -42.4048 | 2024-11-28 13:30:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 123.9 |
| ccf78e66-fecf-3490-b58c-aa7c5d270e43 | -6.3685 | -45.6934 | 2024-11-28 13:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 44d389e7-0475-3e1b-8004-d7a7d198405e | -3.4474 | -44.6039 | 2024-11-28 13:30:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 83b4079e-09f1-3e3d-915e-a18ccae29e51 | -9.1827 | -44.7173 | 2024-11-28 13:30:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 6655c35b-a834-3e77-a743-763b8d70839a | -5.9788 | -45.3621 | 2024-11-28 13:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 319d1fa4-25e7-3475-a13f-9a5d6314ed7f | -3.9675 | -48.0634 | 2024-11-28 13:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1099a5be-3a90-36cc-8136-c40b8950121a | -5.4548 | -43.2426 | 2024-11-28 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| bc795c45-7574-3392-80a1-b1f19d8eb337 | -6.3687 | -45.6709 | 2024-11-28 13:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 1746bb48-130b-3244-904b-a60fc26461a6 | -3.3255 | -46.6699 | 2024-11-28 13:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f1df268f-9d22-3e15-887f-5c44945dd063 | -4.6565 | -42.3811 | 2024-11-28 13:30:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 177.9 |
| 835a8596-c506-3d64-a587-d26b854357b3 | -2.861 | -46.8406 | 2024-11-28 13:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| a88b4489-1bb4-3820-834c-abbf2987462e | -3.4717 | -43.5466 | 2024-11-28 13:40:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f5793580-52e3-3ac0-af91-1970f1eabb66 | 1.4917 | -56.0034 | 2024-11-28 13:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 4a6a05db-d67f-37ad-8fcd-5a25dfdaf8b2 | -9.1824 | -44.7404 | 2024-11-28 13:40:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d81a032f-8378-3427-912e-7c5a154aa78c | -17.6457 | -57.5668 | 2024-11-28 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 99f2520f-5ecf-3030-9fdc-088b56c281d1 | -4.6564 | -42.4048 | 2024-11-28 13:40:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 117.7 |
| f1c19be4-2a82-3b01-9c74-3549f98c7b3b | -4.6565 | -42.3811 | 2024-11-28 13:40:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 158.0 |
| 93f0b84a-678d-31a9-96fb-985f702f01df | -9.1827 | -44.7173 | 2024-11-28 13:40:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| fa40caf6-a443-3c00-9095-c5527db414ce | -2.861 | -46.8406 | 2024-11-28 13:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| acc8596e-363f-3d7b-b498-fff8432e4cf4 | -3.5587 | -44.69 | 2024-11-28 13:40:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 231a4968-b6b5-3f0d-a32a-d71b417b0bdd | -2.2331 | -46.13 | 2024-11-28 13:40:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 5479e174-75c3-30c6-9897-10c0c0e29a42 | -3.9488 | -48.0859 | 2024-11-28 13:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d21fdbe5-a655-3054-8f83-1d650df3a1be | -2.5824 | -46.9811 | 2024-11-28 13:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| dc4aef62-0ce9-325e-96de-5cc5376100fc | -5.4548 | -43.2426 | 2024-11-28 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 44290cbf-80c2-3b12-9666-0c946ecda663 | -3.9675 | -48.0634 | 2024-11-28 13:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 7b92522a-0d2f-3864-8bf5-25d3c3ce1952 | -3.4473 | -44.6266 | 2024-11-28 13:40:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 9a64f923-3a04-389f-b8a0-48d8b9aa044b | -2.0305 | -45.6896 | 2024-11-28 13:40:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ae3b172d-febb-31b7-b7c1-f9598f157659 | -5.4546 | -43.2659 | 2024-11-28 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| ca767360-d24f-3577-8177-246499be775a | -4.6753 | -42.3799 | 2024-11-28 13:40:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 162.3 |
| cd350560-2882-381c-9608-6209eb65088a | -17.626 | -57.5692 | 2024-11-28 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| b55d3114-5f62-3481-bbda-a983a26a9fd8 | -17.6453 | -57.5874 | 2024-11-28 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 767ee704-050d-3fee-9985-3a0867132b10 | -5.4548 | -43.2426 | 2024-11-28 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| f83247fc-a691-3e2e-9e24-ad621f2e30d0 | -3.9675 | -48.0634 | 2024-11-28 13:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 3b8f0c08-7c02-372c-8784-a8b19046f53a | -3.5587 | -44.69 | 2024-11-28 13:50:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| c12d56b2-9881-3ecc-a99e-c61659069dc0 | -17.6453 | -57.5874 | 2024-11-28 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| c0a5469c-2b37-30c2-a950-2d811ed62c73 | -9.1827 | -44.7173 | 2024-11-28 13:50:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 54e7edf4-abc8-3fd9-b530-0fd6addef919 | -0.3593 | -49.9584 | 2024-11-28 13:50:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 977b1694-8a77-38af-bb0f-bd513d15727f | -3.0695 | -41.9451 | 2024-11-28 13:50:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 80532b49-ae4a-30f1-acb8-1f20ebc68ce3 | -3.3909 | -44.72 | 2024-11-28 13:50:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 0fe6975e-2cda-37b2-86f4-cd0f17ec70f8 | 1.2354 | -55.9666 | 2024-11-28 13:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| c95ea90f-ad62-328f-bcba-4a8287332320 | -4.6565 | -42.3811 | 2024-11-28 13:50:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 344.4 |
| 66882cd2-9ad3-3d63-81aa-76ad31536545 | -17.4054 | -57.8408 | 2024-11-28 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| fd916d90-a175-34a1-b0b7-db5eb937f3f4 | -2.861 | -46.8406 | 2024-11-28 13:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| cdf64dc6-993a-3f61-82a0-5184e3521bac | -4.6753 | -42.3799 | 2024-11-28 13:50:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 308.9 |
| fdf54114-b29b-3700-b0f5-c1d43becc191 | -5.4546 | -43.2659 | 2024-11-28 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| ae606838-bd0e-3769-b9be-cfd6996dc709 | -2.5824 | -46.9811 | 2024-11-28 13:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |


[Clique aqui para ver as próximas entradas](README103.md)
