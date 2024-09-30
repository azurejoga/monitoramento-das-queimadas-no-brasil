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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ae1abc3-cc16-3171-888f-87bafea5e367 | -4.38248 | -48.68598 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe92e698-e1eb-3406-93b4-5b5a56b6dffd | -4.38192 | -48.68954 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5e0e675-e12f-3861-a263-4ec489ecc15e | -4.27987 | -48.64809 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 96f6cd42-e656-3f54-a578-0f56dca4a23d | -4.27931 | -48.65168 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3d48442d-f165-386d-9020-8093edd0202b | -4.27874 | -48.65527 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7d00029c-efa4-3510-9233-4700012f6c50 | -4.27651 | -48.64757 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| ac0c2235-2882-340b-9e40-7f91bed886b8 | -4.27594 | -48.65115 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c42d1d4b-8c05-3218-ab60-4db7389f120b | -4.23631 | -48.57531 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcdf07e5-2548-3964-915d-c3199cd497e0 | -4.23296 | -48.57477 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc957183-5b87-388f-816a-ae59236b79b0 | -4.22709 | -48.57734 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42a704b2-5892-3393-bb21-41dd75766b91 | -4.22204 | -48.58753 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 87bd6314-1f0b-32cd-b7c9-149cda7da7d7 | -4.19452 | -48.63085 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3e4a2da-89d7-3ca4-a195-5c9640fb7d58 | -4.19173 | -48.62671 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01fe2379-d539-380b-8da2-e0d4a72cf03f | -4.19116 | -48.63031 | 2024-09-30 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d53babc-abfc-3f32-b2b9-a6b8e3d6c758 | -4.08722 | -48.27573 | 2024-09-30 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 634df528-c0a7-3cce-8f82-eda50544d47f | -4.08387 | -48.27521 | 2024-09-30 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61068afb-dfc6-3f82-82d7-e5d32b8d89cd | -6.24162 | -49.40816 | 2024-09-30 04:29:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc704e06-4923-329d-a64c-e56905637fdb | -6.23823 | -49.40762 | 2024-09-30 04:29:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b71d040-9a76-35b7-b6e5-9666310fdb4c | -6.09455 | -49.34375 | 2024-09-30 04:29:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 924770fa-6446-30f8-9f5e-4f7c7d179ea7 | -5.80458 | -49.18254 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd267ee2-ca13-31c1-a30b-6888900ed48e | -5.8012 | -49.18199 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56ad47d6-10e1-327b-852a-ee24be0b6d4d | -5.73781 | -49.2468 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e8ab910-48e6-3e2e-a2e0-b26e4141a83c | -5.73442 | -49.24626 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8989cb2-a5ee-3ac0-9dec-e7ed03f440ba | -5.72125 | -49.28533 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b28d4a0a-ef70-325b-bc2c-ad4e9d24e9f4 | -5.71844 | -49.28112 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc40f8d0-e4d9-3c9a-b7e5-63c614c80f08 | -5.66767 | -48.82924 | 2024-09-30 04:29:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc935cef-8d1a-39f9-a3c3-46dda1116134 | -5.66711 | -48.8328 | 2024-09-30 04:29:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62e39077-8530-320c-85d9-a028e7ec3678 | -5.58009 | -49.03197 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 870637ed-881a-38c6-a584-c10eb0cddce1 | -5.55005 | -49.01638 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f693732c-e1b4-396f-a109-eb5effcde6f5 | -5.54947 | -49.01999 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84684210-7602-3089-8bb0-0cb448231341 | -5.54495 | -49.02668 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0200acf-9f65-333c-9d1e-760d298870a4 | -5.54227 | -48.97826 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fe0699b-32cf-3b98-9899-2aa0cdb7ef3e | -5.54158 | -49.02615 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcf4bc33-c2a9-3691-b250-7f10df4cb505 | -5.52326 | -48.94581 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e23e538-c293-31a8-bf1f-f29649722808 | -5.52047 | -48.94169 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cef937a0-bd72-3c76-abcf-d26f610928ab | -5.51989 | -48.94527 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80720469-e443-383d-9836-887264bff0e6 | -5.43629 | -49.09143 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beeecf0e-2634-3fe9-9b84-272cb460ff0c | -5.23255 | -48.87442 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34d96130-9efc-3ebc-9968-8966a2de0266 | -5.23198 | -48.87801 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a97d25ce-a637-3c21-805f-45336ddb72a4 | -5.23141 | -48.8816 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67ea5bd5-4de9-389f-8049-1e189680920a | -5.22804 | -48.88106 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 06730753-549f-3305-8866-ea4dc7a907c5 | -5.22747 | -48.88465 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f250a3b5-06d8-3dc0-be7a-bd23c16a52bc | -5.22411 | -48.88411 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05a6e9bf-e351-3959-bcf5-945296b93dcb | -5.22354 | -48.8877 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dda944c6-25ae-3106-bbd4-39358003e9bb | -5.22017 | -48.88715 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cb9c7b3-ceac-3f3c-8e5f-3b629a1e0efe | -5.21655 | -48.97515 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c945e36-c21a-3ef4-8cc8-573fd33d078e | -5.21598 | -48.97876 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db442cbd-de11-364e-bead-bef2cdf3f323 | -5.21432 | -48.9674 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97f27555-411e-33db-9628-292b77705be5 | -5.21375 | -48.971 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c2bc5d4-cd9f-3133-9896-3653ecfb88d2 | -5.2126 | -48.97822 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f41449fa-20c3-3575-864c-e6edac6d52f5 | -5.21203 | -48.98183 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08f4a707-6d5b-30b4-838a-a905966ad7ca | -5.20866 | -48.98129 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d27b87-0498-3bb4-ab3d-31401c352108 | -5.20528 | -48.98074 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c359d5a-dfbe-3b2c-9d1d-b797a64aee89 | -5.15799 | -48.87749 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e25fe9bf-198a-3dd6-8aae-c89e73c6be67 | -5.15064 | -48.90215 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3e8201f8-2bdf-3b7b-8a68-1d7ef2a8f979 | -5.14784 | -48.89801 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16dc86b8-6eef-3be4-9eb6-9570576fc4dc | -5.14727 | -48.90161 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e91fddd-7ee6-3c71-af77-1ecfb5e99ee7 | -5.13208 | -48.91024 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 119e25d9-3257-384b-b0cd-fa4ded8b6d25 | -5.12928 | -48.90608 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcccba7d-75c0-3d11-8678-ec5a40d20cf5 | -5.11694 | -48.89673 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1853896-3b62-3d05-a717-c94700338272 | -5.11637 | -48.90033 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 733fbaff-4dec-3c16-b5db-56cd8d2e1b70 | -5.11425 | -48.84846 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c52b1b1e-7dbd-3130-9a8f-72323eebdc33 | -5.09844 | -48.88271 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 632d9bf3-0e84-3899-9fef-5e27927b286e | -5.09786 | -48.88631 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 531f919a-0a77-3b88-b61b-6a75b5336fa5 | -5.09507 | -48.88218 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1df32e0e-42df-33de-88ed-6f90d2121861 | -5.0917 | -48.88165 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e83c81df-fb80-3d79-a048-e019f4b012c7 | -5.08947 | -48.87392 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5405e084-c8ca-392f-96a0-2b10796685cf | -5.08725 | -48.86621 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c957e29-9abf-358b-ac97-5ee9bcc1538d | -5.08668 | -48.8698 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f874366b-efa0-30ec-a3d0-b53279299d71 | -5.08611 | -48.87339 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 194a3561-3584-3a03-9840-6c2f876e62b0 | -5.94444 | -49.6218 | 2024-09-30 04:29:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 962c91c8-56c1-30c5-84b7-c10f43fd8892 | -5.9416 | -49.61762 | 2024-09-30 04:29:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dd4be47b-c3b1-358d-8480-b0a5fe27d3f1 | -5.6477 | -48.42091 | 2024-09-30 04:29:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e076edb-6674-33a8-90ed-943052b6ff49 | -5.64715 | -48.4244 | 2024-09-30 04:29:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3f1ce49-c62b-3fd8-8bfa-ecb4f5498ae9 | -5.63938 | -48.43037 | 2024-09-30 04:29:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00bfed9a-9e51-3876-98ab-9027382092d9 | -5.63883 | -48.43386 | 2024-09-30 04:29:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ead5715-2bdf-3cb5-8d70-91cdd60df6a9 | -5.32682 | -48.66304 | 2024-09-30 04:29:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b84414f9-66fd-352c-a87f-5978c94917be | -5.21557 | -48.18818 | 2024-09-30 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d78a24c6-f80f-3859-a980-98ce3108e2ef | -3.39159 | -49.51768 | 2024-09-30 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0d74feb-db4a-3e36-b469-a92d867b3d5a | -3.37522 | -50.37545 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc6c2b4f-bbd3-3db9-84c0-1ad5a59dff12 | -3.37225 | -50.37063 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d04c1db-96ea-3cf7-9a5c-2be9ee3e0ff5 | -3.37158 | -50.37484 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1903cba7-1578-3e67-b08d-5e7507c09ada | -3.36862 | -50.37001 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7342cd0f-f223-36df-bfd9-75520e088f49 | -3.36795 | -50.37423 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0b4cf2b-2a0e-3896-903a-e63998384dc0 | -3.36728 | -50.37845 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5839d364-286c-3924-9b9a-53c70fa28fe3 | -3.36431 | -50.37363 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b97049b3-3229-3017-985b-ab899d5f93b5 | -3.36364 | -50.37783 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d95c54f-b533-3599-8e91-ac83366cc31e | -3.36 | -50.37725 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dcdb1d57-afbc-3263-b03b-494ff6fd1132 | -3.35636 | -50.37667 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 628be7f1-2c1f-3436-bfe7-cf5c905c6d8b | -3.29483 | -49.51107 | 2024-09-30 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f21e14be-fa4b-31b9-bc2d-6639898c223f | -3.29196 | -49.50659 | 2024-09-30 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ee46d61-b9af-3462-bbfd-72b7a91b279b | -3.39097 | -49.52156 | 2024-09-30 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7ef04af-a2f2-3243-802c-ff13119a8315 | -3.27693 | -49.13307 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 851bdf6f-ede1-321b-a47c-fee92848a1bf | -3.27349 | -49.13253 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dda35c66-6f30-324a-8c91-14e587a89199 | -3.13787 | -49.43172 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13c32b65-0100-3e17-8e00-68a13de9bd98 | -3.11282 | -49.40089 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d1e4eddf-f279-38d4-92c5-a8e04f79c4c4 | -3.11222 | -49.40475 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 64315640-fa2d-3c31-a94c-1957b1df182d | -3.10994 | -49.39648 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5695e08d-28da-31d6-b5df-4afdf40c82ed | -3.10934 | -49.40033 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1ed45ec0-d5ef-3743-8992-3b2e52d5f4d8 | -3.10873 | -49.40419 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |


[Clique aqui para ver as próximas entradas](README30.md)
