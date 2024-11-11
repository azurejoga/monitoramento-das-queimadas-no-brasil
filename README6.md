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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d558437-10af-36f5-8e79-b59f81d40231 | -2.2997 | -48.4648 | 2024-11-11 00:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 3674689e-5260-30e6-a1b1-454f690aff70 | -3.2352 | -50.3065 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bf205878-61d7-3108-96a6-aa6e2fcf6bfd | -2.1891 | -48.36 | 2024-11-11 00:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 888fc1cd-0e23-3981-a911-41566de5df10 | -17.5889 | -57.43 | 2024-11-11 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 3260bc40-b436-3bb9-98d5-350161ef25d4 | -3.7149 | -54.6504 | 2024-11-11 00:30:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f41b2ee9-6edb-3b90-b573-5343438ee3ac | -3.2603 | -48.7368 | 2024-11-11 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d35bc635-5f12-3779-b441-58d670ad20c6 | -3.5322 | -49.9599 | 2024-11-11 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9d3ece0a-677f-35c4-ac23-565951e45583 | -5.0997 | -45.5344 | 2024-11-11 00:30:00 | GOES-16 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 2a8185a7-8887-3b48-9e1d-f405b8afc66a | -3.0111 | -50.982 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 03e6ff79-91eb-3750-9116-8f11b0554263 | -3.6859 | -45.2502 | 2024-11-11 00:30:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 8f38bead-aa1b-3163-b68e-fbc60a0880f2 | -3.6789 | -50.2074 | 2024-11-11 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 698fe991-45eb-311a-8e47-68d8dfd084ce | -2.8323 | -49.4325 | 2024-11-11 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 3ad2faa0-9428-32b9-9da1-416a69035c93 | -3.0214 | -53.2404 | 2024-11-11 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e78d4551-63d3-3cab-8244-a30e00f9a9a1 | -17.2933 | -57.4857 | 2024-11-11 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 158.2 |
| f45f99ff-5574-3df1-b2e8-59340520497f | -3.2536 | -50.3059 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3e503eda-cadf-3066-9539-0ec3a4c3de73 | -3.048 | -50.981 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a6e94d31-0176-3c9e-bae7-e96839e09b80 | -3.0111 | -50.982 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 69d05aea-225e-3efc-988a-e6bb3afa2d4d | -4.1246 | -43.5833 | 2024-11-11 00:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| aec36842-f344-33b9-85ce-c8a0e092315b | -3.2168 | -50.2861 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 498eb582-4ca0-3523-81aa-3cf6b86a86ae | -17.5889 | -57.43 | 2024-11-11 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 2eacfbcf-2817-34b9-8d5f-563848e03755 | -17.313 | -57.4834 | 2024-11-11 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 4e8f00d5-c3ef-33cc-a5cc-a581a34a4bc0 | -2.8508 | -49.4108 | 2024-11-11 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c82df45d-ee8b-339d-9dad-f0af72f6bf5e | -3.2244 | -53.0524 | 2024-11-11 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7a3aaf04-e8a1-3513-a6e0-2385c10555ba | -4.1286 | -49.088 | 2024-11-11 00:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| bab6afe7-604f-3810-a6e1-1b5d6d5503d5 | -3.5331 | -42.5864 | 2024-11-11 00:40:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 7997db54-226b-32f3-a557-4a7e15649485 | -5.9601 | -45.3635 | 2024-11-11 00:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 004391bf-3ebe-3cb0-901f-6f8064947a8e | -2.9792 | -45.2567 | 2024-11-11 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 121.1 |
| af0f301c-9623-3adb-bd2a-a175dcfdef00 | -2.1891 | -48.36 | 2024-11-11 00:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 3cc1f2f6-0037-3b8e-a416-1d027011ca9f | -3.2948 | -45.3346 | 2024-11-11 00:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 96.6 |
| b6e73066-03e9-36d9-bad7-34cc9be8a2a5 | -3.686 | -45.2276 | 2024-11-11 00:40:00 | GOES-16 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 64ae1693-a2c6-3873-8826-c2ae3d3a1d0a | -2.6662 | -49.3948 | 2024-11-11 00:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| dab86f84-bddb-3f0e-9db9-778e9957d5a2 | -1.5164 | -52.1491 | 2024-11-11 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| fc7d536c-e9d3-3c64-bedf-7d2181ec1e01 | -3.1423 | -50.4352 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| f92a9713-49b0-3b52-9d10-107741d9beb3 | -17.2936 | -57.4652 | 2024-11-11 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 259ccd85-27e0-3192-98e4-9c8ea090e64f | -3.0138 | -45.8161 | 2024-11-11 00:40:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 24a3d240-26b9-39ac-9bd0-8d4635fa02b1 | -3.6789 | -50.2074 | 2024-11-11 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 45995d86-1b16-33a4-828d-751c44c8d7d9 | -2.2075 | -48.3811 | 2024-11-11 00:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| d61c747a-a163-3b08-8167-f090c2267d32 | -3.0111 | -50.9612 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6885fe9b-702e-35cf-8dc0-a2d92fe4712f | -15.9982 | -59.3649 | 2024-11-11 00:40:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 94fc4b63-d786-3072-8375-ca0ee907feec | -3.6859 | -45.2502 | 2024-11-11 00:40:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 9ad0252e-be15-3fad-9a9c-394d62c4337b | -3.1029 | -51.0834 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 777fc1a9-be53-358b-b46e-b0afa7d1d76e | -3.2588 | -53.6994 | 2024-11-11 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| db1fb9eb-fa77-3052-92a1-3d89d5dcb68f | -3.1458 | -54.4659 | 2024-11-11 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| cc6789b9-96b8-3b43-8c54-1d2c1772b162 | -3.0845 | -51.0631 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 051f634d-f0ca-3a63-8384-8a2c6ea583bd | -2.2504 | -46.5282 | 2024-11-11 00:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| f64e65b0-aeae-3294-9e66-a56a5461477d | -3.0137 | -45.8384 | 2024-11-11 00:40:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 2add5742-e8fa-3111-a6b9-883a11ef8441 | -1.2201 | -53.6364 | 2024-11-11 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6f78961f-6adb-358c-9a38-c37e8966a438 | -5.9788 | -45.3621 | 2024-11-11 00:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 49f5fda3-2910-388d-8985-16096632d65a | -2.2504 | -46.5061 | 2024-11-11 00:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 2baaaa00-925f-3114-ad1a-8694fbbc1488 | -2.8323 | -49.4325 | 2024-11-11 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 12a4aa98-a32b-3bcb-942f-625f5ff447da | -3.2352 | -50.2855 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b5851378-fc5f-3f90-a5ea-e008ecd850f1 | -3.0296 | -50.9607 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| e2aba691-e025-397e-acdd-61a91e2dfa6b | -3.3836 | -50.1336 | 2024-11-11 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 24e1c74a-da93-3a74-b056-aeb43f3d1503 | -3.5137 | -49.9606 | 2024-11-11 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8ecb4413-3650-3f41-9443-8224293eb8ec | -3.1984 | -50.2657 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| b047acf6-e3a7-3433-85ea-46d748743ee6 | -2.8692 | -49.4314 | 2024-11-11 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 7549a872-a1cc-3883-96dc-26ec070f713c | -3.103 | -51.0626 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7257ca0d-cf40-3ff4-b863-9a78c281a365 | -3.5346 | -45.7061 | 2024-11-11 00:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| d441f54a-f91b-303e-bf4d-100df91ce14f | -15.9793 | -59.3267 | 2024-11-11 00:40:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 423f722d-df61-3522-85fe-8e6a37dc9cfc | -3.6604 | -50.2081 | 2024-11-11 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 9bfe6ed2-6365-39c7-bbbf-52369773b1b4 | -4.0294 | -46.9484 | 2024-11-11 00:40:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| deb2dcf0-8a52-307d-9728-4ee5599131be | -3.0324 | -45.8154 | 2024-11-11 00:40:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 322.5 |
| cfed93d9-66ed-30f5-a344-ee43591086c5 | -3.6954 | -50.6262 | 2024-11-11 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 481b2434-0c86-3751-b5b1-57a0604c068e | -17.2737 | -57.488 | 2024-11-11 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| bf947d39-95f3-32ef-b990-0295a25bba9e | -3.2428 | -53.0519 | 2024-11-11 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| d1af8f18-9fdb-382a-a846-7c135f531520 | -2.2997 | -48.4648 | 2024-11-11 00:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0cd32f22-eab5-32a2-8d31-349017d7b97d | -3.1458 | -54.4859 | 2024-11-11 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 2778aff8-614f-35d8-bf22-49ba44fcde11 | -4.1285 | -49.1094 | 2024-11-11 00:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 85ca3e07-5abe-355f-b40a-12fb13de5c54 | -3.0325 | -45.7931 | 2024-11-11 00:40:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e82328d3-339e-3da2-82d4-8a6a3e1ed4e6 | -3.7149 | -54.6504 | 2024-11-11 00:40:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2c6e2689-c88a-3751-aa3f-f81c99ec25ea | -3.0295 | -50.9815 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 9c31e633-f675-3a95-8df2-d0d8c7830adf | 0.4509 | -50.9618 | 2024-11-11 00:40:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 4382b89b-8887-31d8-be3a-786e3c9ec9ea | -1.4057 | -52.3758 | 2024-11-11 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 370f8e1b-ff73-33d0-a0a7-18fd83c3de3a | -2.189 | -48.3815 | 2024-11-11 00:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 161.5 |
| 978290ca-52eb-3994-825f-ad7ea50d3f59 | -3.2352 | -50.3065 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9f1e6a63-1b57-3499-8feb-05a2d349bc2f | -3.048 | -50.9601 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0b954975-1ae6-3795-becf-5a67a641e36d | -3.2427 | -53.0722 | 2024-11-11 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 9c9bd327-e1a2-3550-92e1-56657970ad48 | -4.0293 | -46.9703 | 2024-11-11 00:40:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ee1a5176-68ef-38c5-a5a2-46800f0f0e48 | -2.4551 | -51.9476 | 2024-11-11 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d94af4a1-d22f-354e-b803-3c7f8603f39e | -3.0323 | -45.8377 | 2024-11-11 00:40:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 98725818-110a-3f58-b198-2b11d2bb5de7 | -3.1983 | -50.2867 | 2024-11-11 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| cefa7bf1-86fc-39de-a738-748d4321362a | -17.6086 | -57.4276 | 2024-11-11 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.0 |
| 3811c073-13ac-3f10-a4de-1353465a0d4a | -3.5322 | -49.9599 | 2024-11-11 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 790eaa0c-2764-3d99-91d4-022d44a829b3 | -4.11 | -49.1102 | 2024-11-11 00:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 397972da-93d1-3170-828a-9286d1aa4052 | -4.1101 | -49.0888 | 2024-11-11 00:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 068b10a5-f293-362f-ac05-f720ef01ead7 | -2.9978 | -45.256 | 2024-11-11 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| f2e71e17-19d9-3e7e-b16f-ea108a747337 | -2.8508 | -49.432 | 2024-11-11 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 2cb80592-f04f-33c2-b79e-033a6b6e043e | -2.8324 | -49.4113 | 2024-11-11 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6e9b159f-e33c-34b6-8f97-8aa567e4a9cb | -3.6954 | -50.6262 | 2024-11-11 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a1e312a3-7d3b-305f-a635-3f29892849db | -17.2936 | -57.4652 | 2024-11-11 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| fddb4fe4-ac60-3469-b8fe-ea6ad91042eb | -2.4367 | -51.948 | 2024-11-11 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| c7c3dbe4-4cca-3508-8fbb-b02952a1f1b0 | -2.9978 | -45.256 | 2024-11-11 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 9b01717f-2565-3d08-9321-8276af3adec7 | -1.4057 | -52.3758 | 2024-11-11 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 67e4e0d0-d38b-3037-805e-a76977ac6fb6 | -4.0293 | -46.9703 | 2024-11-11 00:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| be0f510e-6284-362e-b4af-71db778c79ec | -4.1101 | -49.0888 | 2024-11-11 00:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 62e5680a-b75a-3931-b4cc-fef7ba34c1cc | -3.0324 | -45.8154 | 2024-11-11 00:50:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 295.7 |
| f9c29e6a-7ced-367b-92a4-396bb3b7a3d4 | -3.2588 | -53.6994 | 2024-11-11 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 144e7d5d-0eb2-3ffa-95d3-6b43f3dfbbba | -2.189 | -48.3815 | 2024-11-11 00:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 9d9560a2-5217-36b7-b44f-ebdf739c50c0 | -3.2428 | -53.0519 | 2024-11-11 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f42b3865-c7bb-30d3-8668-603404a748cf | -4.1285 | -49.1094 | 2024-11-11 00:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |


[Clique aqui para ver as próximas entradas](README7.md)
