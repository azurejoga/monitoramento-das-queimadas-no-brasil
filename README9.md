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
| a7f4e7fd-bf5f-334e-b591-d5a76b38c5fc | -2.641 | -46.1849 | 2024-11-15 02:40:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8a28e475-7058-3e0d-ad1a-1b6af1a5b671 | -17.6263 | -57.5486 | 2024-11-15 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| b3cec155-8c65-3c8e-ac5e-b412b394121d | -17.5882 | -57.4711 | 2024-11-15 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 7165fd0b-b0f6-374c-9347-5e0d9648b990 | -17.646 | -57.5463 | 2024-11-15 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 4b518d84-55a3-3090-afaf-0e40972d689e | -17.235 | -57.4516 | 2024-11-15 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| d78ab3ff-7c44-3a49-95dc-58d48113dcdf | -17.2347 | -57.4721 | 2024-11-15 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| b3c43094-01b7-3ff7-b852-7eb6de9f6324 | -17.5672 | -57.5557 | 2024-11-15 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.4 |
| dd1910c7-2e14-3e29-a610-b2a8ab46af76 | -2.6596 | -46.1843 | 2024-11-15 02:40:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| dfdc594e-57ed-31da-9eb7-beda4392808f | -17.5668 | -57.5762 | 2024-11-15 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 636da32c-8daa-3f5b-bc47-48f0fcc34245 | -17.2543 | -57.4698 | 2024-11-15 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 142.5 |
| f143cb03-92b4-3518-9261-a4f86ea7b648 | -17.5879 | -57.4917 | 2024-11-15 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| e2f7eb54-5088-3dc5-bb00-f0dde93f5431 | -17.7048 | -57.5597 | 2024-11-15 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 741438b1-c6ad-3aea-91da-76d8b1206273 | -17.5675 | -57.5351 | 2024-11-15 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.6 |
| 2885cc50-8095-3711-9d99-e39c677253c2 | -17.274 | -57.4675 | 2024-11-15 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 2fc130bb-5301-3ca9-ad40-27661fcc0f40 | -17.274 | -57.4675 | 2024-11-15 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| fec7060b-1f54-3ad2-b2c2-f968028ef3b0 | -17.2547 | -57.4493 | 2024-11-15 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.2 |
| 8d9b0f00-5b25-3c71-be48-3c8ac8dfc960 | 1.3035 | -60.4074 | 2024-11-15 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| eccf7c8d-e23f-3087-aabb-f6838e27d6a5 | -17.2543 | -57.4698 | 2024-11-15 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.5 |
| 7568ae84-961f-3b9f-84f0-b201b210fad6 | -17.7048 | -57.5597 | 2024-11-15 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| a8641ca0-2397-3324-a97c-4037e3ff1041 | -17.5882 | -57.4711 | 2024-11-15 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.0 |
| cb435774-fb5a-3bb3-9d45-5be0f8b976f8 | -17.5879 | -57.4917 | 2024-11-15 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 874cb447-768e-328e-a273-3ad1cea1777b | -17.2347 | -57.4721 | 2024-11-15 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 292a0f42-377a-314d-a76e-af24d024b0bb | -17.7052 | -57.5392 | 2024-11-15 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| b7e49e05-5f05-3d7b-a9ee-7faa7f7fa073 | -2.6596 | -46.1843 | 2024-11-15 02:50:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a7476338-0692-3360-9f9c-505fd8cfe988 | -17.235 | -57.4516 | 2024-11-15 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 8e7db650-cca2-3412-9d72-991b33701f90 | -17.5882 | -57.4711 | 2024-11-15 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 47b810cc-4efa-363c-8d32-3cd562bfd0d7 | -17.2547 | -57.4493 | 2024-11-15 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| c9734f81-6e27-358c-88c1-24ad5e2bcab3 | -17.2347 | -57.4721 | 2024-11-15 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 42bfa266-5449-3d3c-bfa5-b56970277876 | -17.5879 | -57.4917 | 2024-11-15 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 3a53eb49-a478-3f42-acfd-89e7ccc0130e | -17.2543 | -57.4698 | 2024-11-15 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.3 |
| 18bba17e-b16e-34b3-90c3-25c170067ea1 | 1.3035 | -60.4074 | 2024-11-15 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0cca8d53-022c-310f-a4d6-0cc83db2ce15 | -17.235 | -57.4516 | 2024-11-15 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 792a6249-3b32-3b14-bd0c-708d7dc357d5 | -2.641 | -46.1849 | 2024-11-15 03:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 5c332e25-26f1-3f2c-ab85-ec8bedb13892 | -2.6596 | -46.1843 | 2024-11-15 03:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| cfa90fdd-561e-35c2-bdcb-dfec78ff7ef1 | -17.7052 | -57.5392 | 2024-11-15 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 826bde97-77f3-3a7e-b40f-3c0df42ed5a0 | -17.7048 | -57.5597 | 2024-11-15 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 30a028ee-d908-33c2-a585-5db87027451e | -7.51723 | -34.86312 | 2024-11-15 03:04:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8f6fe055-979e-3d5f-acaf-d1eaa3fcea66 | -6.92753 | -35.03336 | 2024-11-15 03:04:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 999e5769-d8cb-348a-bb45-c40b93ba5bae | -6.97524 | -38.37707 | 2024-11-15 03:04:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6500b27f-25bf-38a4-a198-3a8ec587f9e6 | -7.16131 | -35.02145 | 2024-11-15 03:04:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| cbb6bf1b-2414-31d9-910b-6521dd63675b | -6.97413 | -38.38298 | 2024-11-15 03:04:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a1bad0f-0dd8-34fd-a29e-8bfde0d6f9c6 | -9.4136 | -35.52514 | 2024-11-15 03:04:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3c456a72-4de0-301d-a21e-41ad293824f8 | -9.40825 | -35.52407 | 2024-11-15 03:04:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bffc191b-d182-3ecf-91cd-5367030a94be | -7.15593 | -35.02044 | 2024-11-15 03:04:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 530cae63-fcda-3b62-a4be-eda88f7c039a | -6.92689 | -35.0369 | 2024-11-15 03:04:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a4c403ed-a1c8-34bc-a3a5-62cb85ba32de | -6.93298 | -35.03411 | 2024-11-15 03:04:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6e3d2074-3619-3bae-a3a4-5380d18161df | -8.52306 | -35.37136 | 2024-11-15 03:04:00 | NPP-375D | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 9f1ecd7a-44a0-3871-b4f3-613b920bf28d | -7.26524 | -39.85432 | 2024-11-15 03:04:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 508dfffe-c2b9-3bf8-97ba-a8d7e7fab90c | -7.12867 | -35.23537 | 2024-11-15 03:04:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3cf8ca92-a5be-3804-be47-6f0639e1a26a | -7.16192 | -35.01805 | 2024-11-15 03:04:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| cf0d4206-1821-3012-880a-0185d7f0c76f | -7.12929 | -35.23191 | 2024-11-15 03:04:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 25e5ae3c-0bf6-3892-b0ea-94ee54c098c5 | -8.52369 | -35.36783 | 2024-11-15 03:04:00 | NPP-375D | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2a48b242-3205-37ab-99a3-7f6d43705ab2 | -17.5672 | -57.5557 | 2024-11-15 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 89fd695b-51c1-3542-a730-8535ce266972 | -17.5865 | -57.5739 | 2024-11-15 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 245.6 |
| 2f1a054b-f01c-3714-96ca-659281d23eff | -17.274 | -57.4675 | 2024-11-15 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| d9076dae-bc39-3e78-a608-246296156214 | -2.6596 | -46.1843 | 2024-11-15 03:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| c853d870-b4c2-3e3d-94d0-8e75689d6d66 | -17.5869 | -57.5533 | 2024-11-15 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 223.6 |
| 02f0eaec-a4cb-343a-bf56-396b0ee40780 | -17.5879 | -57.4917 | 2024-11-15 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| df084a64-d846-3ebc-8d76-3a7a44b11385 | -17.7048 | -57.5597 | 2024-11-15 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 16fa54dd-2a35-3ef4-b57b-a5f78077a44f | -17.7052 | -57.5392 | 2024-11-15 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| c709ebc7-45f7-352a-87b9-d30da9747dd4 | -17.2543 | -57.4698 | 2024-11-15 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.2 |
| a72d0d40-c632-334d-b8f6-e3b2463c9dba | -17.646 | -57.5463 | 2024-11-15 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 1a52cb06-15aa-3534-a826-635a4d91c961 | -17.2547 | -57.4493 | 2024-11-15 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| 11448c3f-0e2c-3965-a7e8-1807b5cd1575 | 1.3035 | -60.4074 | 2024-11-15 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 33a45fcb-021a-3b06-bb9c-38b50100d605 | -17.2347 | -57.4721 | 2024-11-15 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 997d8f25-4ee2-3e5f-bb93-75a0e86c0898 | -17.5882 | -57.4711 | 2024-11-15 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.8 |
| ce76667c-017c-3fd6-b044-c6633faa3724 | -17.6263 | -57.5486 | 2024-11-15 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| f7e56b8c-71d5-3395-9d2b-cc071ba8b50e | -17.5678 | -57.5146 | 2024-11-15 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| fe0c4dd1-2f71-3380-8d99-d69479e51302 | -17.5668 | -57.5762 | 2024-11-15 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 1de8a751-f9f7-3eb4-9f29-7edb2a6b59f4 | -17.5675 | -57.5351 | 2024-11-15 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.5 |
| d8c64421-3b18-38f5-afaa-7603c528c6ec | -17.235 | -57.4516 | 2024-11-15 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 6fc8956b-12fa-30aa-af4d-cb411aca976d | -17.7052 | -57.5392 | 2024-11-15 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.0 |
| d8efbb17-f3cb-39bf-9d32-c677615b9aa8 | -17.5882 | -57.4711 | 2024-11-15 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 180587bb-5f0f-35f4-823a-f2f80fc93c0f | -17.2347 | -57.4721 | 2024-11-15 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| b2568576-7937-315e-b23f-77b87b08d001 | -17.2543 | -57.4698 | 2024-11-15 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.5 |
| de77a7e9-a515-3ab9-b7d5-ea051a144484 | -17.5879 | -57.4917 | 2024-11-15 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 21d42626-1e40-3817-8ae1-3d254bb0c553 | -17.274 | -57.4675 | 2024-11-15 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 2373109e-3308-3af3-b072-3328d929af77 | -17.7048 | -57.5597 | 2024-11-15 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 1539ec0c-0e88-3205-911d-fea9dd0dfa3a | -17.2547 | -57.4493 | 2024-11-15 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.1 |
| cd382902-1b0c-3461-858f-31c92af23c1a | -17.235 | -57.4516 | 2024-11-15 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 89524b8d-3570-3cc2-a6ee-0b0b30210d56 | -4.01589 | -38.24926 | 2024-11-15 03:25:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 71aa941c-a6b1-34fb-bd7e-2308214e10f0 | -4.01967 | -38.25462 | 2024-11-15 03:25:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| a8757ae1-78d1-3c0b-b478-ba3e69f9db4d | -2.99879 | -40.28293 | 2024-11-15 03:25:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 91c0ee21-c38e-3d85-a12d-371fc3795c4e | -4.02043 | -38.25004 | 2024-11-15 03:25:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0de239da-8435-3731-9b4d-731e09114146 | -2.99824 | -40.28621 | 2024-11-15 03:25:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 519a2601-3f74-3e52-8a4d-088b0666675e | -7.25916 | -39.85735 | 2024-11-15 03:27:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e0cf1c75-fb47-3926-bf6f-62f23c1e72ce | -6.92906 | -35.03384 | 2024-11-15 03:27:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 738a5c44-d287-31e3-94a8-0ecd3394b27e | -8.55846 | -36.4966 | 2024-11-15 03:27:00 | NOAA-20 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c62576fc-7412-3454-978c-1af5be926762 | -7.21334 | -35.17723 | 2024-11-15 03:27:00 | NOAA-20 | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4fc207dd-4859-3c90-8b4f-0e710eb21804 | -4.19798 | -40.68378 | 2024-11-15 03:27:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c722a734-1c52-3850-90bc-474ee96935e1 | -3.70906 | -41.69359 | 2024-11-15 03:27:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 825feceb-73cb-3be0-be48-42a58a0e4451 | -3.8827 | -43.15361 | 2024-11-15 03:27:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b00a4c4f-97d6-3688-9ef3-038cdbfff70e | -6.79175 | -36.05744 | 2024-11-15 03:27:00 | NOAA-20 | BARRA DE SANTA ROSA | PARAÍBA | Brasil | 2501609 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e1b9217d-ce70-3df7-acf7-2bec43e513fe | -7.26005 | -39.85593 | 2024-11-15 03:27:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e9ccf210-5670-3fc5-b1d7-dcbe9fcff9fa | -6.64496 | -39.1495 | 2024-11-15 03:27:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8ace8d47-1511-327d-bbfb-b6110575ddb1 | -5.97496 | -38.32353 | 2024-11-15 03:27:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 36ecb1b2-c9ba-3515-8e3a-2b071886c9ad | -7.83471 | -34.85928 | 2024-11-15 03:27:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d7b2317e-38bc-323b-95a8-56a5d5323802 | -6.97248 | -38.38116 | 2024-11-15 03:27:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d23921ca-540b-3e64-87e0-5d5243e6b6eb | -6.16133 | -41.15868 | 2024-11-15 03:27:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f02811e7-3202-3a5b-aead-652054174872 | -6.16383 | -41.15741 | 2024-11-15 03:27:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README10.md)
