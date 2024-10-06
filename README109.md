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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f23045f8-a110-3d1b-a19c-b64d12c07b90 | -11.70854 | -58.84226 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b67b99ec-1231-3061-894e-89c17d883bdc | -11.70524 | -58.84174 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 795cbb51-614e-3919-a954-57cbaaae3534 | -11.70194 | -58.8412 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00eea3f1-708e-310e-b555-92eb59380a6d | -11.49286 | -59.19224 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cf0c802-7190-30e2-926f-3f6880af8e21 | -11.48755 | -59.09743 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 477a004e-9041-3e84-925f-a495967bd5dd | -11.25753 | -59.06725 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ef9aa20-8bb4-3c4e-8885-bf5ce53f7cb0 | -11.25422 | -59.0667 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| baae32a9-e37b-3c5c-8c5f-ba51713ce859 | -7.36326 | -59.65763 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0717d0cd-4baa-3724-b097-03203039ad98 | -7.2276 | -59.49808 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caa98427-66d5-396e-ad40-04c9672bac36 | -7.22418 | -59.49754 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65c17ae2-c51c-3e87-96ce-b0e4e49d1129 | -7.22357 | -59.50126 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63ecad12-c2a4-313e-be12-a93c5bd5db37 | -7.12702 | -59.4892 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32013133-f038-36b0-820c-c1a083e588b0 | -7.12421 | -59.48492 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ed5c89b-062a-35b2-bae5-40c694941020 | -7.08174 | -59.48605 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58df8359-2676-3f40-84aa-c9fa6ae443b4 | -6.78911 | -60.10786 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f100e3d-5bc8-3a45-bd79-0a1e7510b452 | -6.78848 | -60.11179 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3374661-bb9b-34d6-8b66-a73ce2675c54 | -6.78722 | -60.11966 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6384e289-af8a-3f6e-95e5-f99abc6a8c36 | -6.78623 | -60.10338 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cff522f-931e-3331-b9ab-cb8cfdd0fa44 | -6.7856 | -60.1073 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a804872a-c7fe-314e-936d-79075c2c2fa9 | -6.78497 | -60.11124 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ae4e9cf-1749-3225-a4c8-427a65e9a815 | -6.78433 | -60.11518 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bafe5a56-308d-3d21-a9a3-210049199c7f | -6.78335 | -60.09887 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69bfb579-e8a6-3b0d-a2aa-3498eda29e22 | -6.78271 | -60.10282 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd68dfe5-458f-3cd0-8968-36260468dc8f | -6.78208 | -60.10676 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cec6e18-dfef-32dd-9d54-7f2fd5ac46e7 | -6.77984 | -60.09832 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3026b7b-5715-320a-b6d2-678b080fefae | -6.7792 | -60.10226 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4fa2047-018c-3e03-b6af-ec0495bbc700 | -6.77857 | -60.10619 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed6ffda5-abbc-36b6-8f4b-7f0cbc7260a5 | -6.71056 | -60.10314 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b62cc56c-7df5-32d5-8753-e9ba99bce9ca | -6.70991 | -60.10713 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92820d38-b46b-39aa-b626-6068ae612f27 | -6.68617 | -59.84748 | 2024-10-06 05:12:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d189133-9d79-3b96-a31c-18f5c9e8c709 | -7.15809 | -59.384 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf4512da-10f3-3110-ab97-6e35189e2206 | -7.15528 | -59.37976 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f768f6b3-94b2-357e-847e-fb8f026313e2 | -7.15483 | -59.29657 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f74baaf-8b11-31d2-a525-74ab61969223 | -7.15469 | -59.38343 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ea97687-c0e8-34fc-b2fe-75d2f9967e96 | -7.15424 | -59.30024 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f772cecc-3ab0-3e61-85a4-5b8022cea80c | -7.15189 | -59.37918 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4cac99d7-cf8a-3a8b-9ff8-bed5f108a169 | -7.15144 | -59.29603 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d242ab88-25ed-3a79-a365-6875609f8228 | -7.15084 | -59.29969 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cf7481a-f33f-3e66-a9b6-ebad0d979649 | -7.14805 | -59.29549 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 756d5c4b-de0e-37e5-9f78-45aadac48ad3 | -7.14745 | -59.29916 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca0c85f4-3603-3de8-a165-56a234bcef02 | -7.14465 | -59.29495 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cd907a4-cd34-3576-8ac2-f69b9db204e6 | -7.14406 | -59.29861 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a81a29cb-a275-3da7-b226-fe4d562ac2f8 | -7.14368 | -59.29501 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 277d7a59-59a1-3ba3-93d6-92aa60ee563b | -7.1431 | -59.29868 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f055beb-375c-305b-a4ea-d50cb973b7e6 | -7.13971 | -59.29814 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a3fbadc-f92c-3659-b377-5135adf2c74e | -7.13912 | -59.30181 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f79e0f94-3d48-3d22-99ff-1e303e388a46 | -7.05926 | -59.30034 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3a2e1e9-ce18-3cf1-a963-84b03786e482 | -7.05239 | -59.23536 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1340d632-1a24-3b26-b8e5-8e3114d16883 | -7.05179 | -59.23902 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fe6dffa-ae92-390a-89fe-e3bb510985ac | -7.049 | -59.23482 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7396082-c182-3c5b-ac7e-07490130422e | -7.03511 | -59.40624 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c478c72a-b00e-34b5-b720-adaec83c49aa | -7.0329 | -59.3983 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb9f89eb-237e-349b-8f0c-9a3f436988bb | -7.0323 | -59.40199 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9910a1f0-17c7-3c68-ba5d-a9f07929fae2 | -7.0317 | -59.4057 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeb6300f-bf08-391b-bb17-e0f4a0b2dc3f | -7.0311 | -59.4094 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96e13918-7258-3e52-95ec-46ae6336722d | -7.02949 | -59.39775 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a75fb6e-1ad1-318c-ab32-ce57ef1e7b40 | -7.02889 | -59.40145 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c96c2620-a5e8-3e29-80c9-c3eb7f4848f8 | -7.02829 | -59.40516 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48816b40-7cc0-3f1d-a64b-996e4415b96c | -7.02769 | -59.40886 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bacf230d-8f69-3b28-941a-09d02501bb84 | -7.02709 | -59.41257 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bbf0ae9-be8a-3fca-91e7-9141e4730eea | -7.02549 | -59.40091 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85dfc5e7-2022-3222-931d-b580fc464f74 | -7.02488 | -59.40462 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57ddfd49-8a05-3409-a5f5-64a31e5aeed5 | -7.02208 | -59.40037 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae827959-52d9-3816-bb05-c24f62d8f91f | -7.02147 | -59.40408 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 634f9e75-6a63-3d5e-8964-14ee4be8c416 | -7.02107 | -59.35885 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ee675c6-1488-315c-ad75-e55aaff9e48f | -7.02087 | -59.40778 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0571dac-59ee-3ee1-8bd8-8a29c31cde39 | -7.01867 | -59.39982 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a4d96c2-777e-3a3a-9272-62ac58e88bb5 | -7.01806 | -59.40353 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d992d11-4588-38f1-ab57-81beddbd0120 | -7.01799 | -59.40012 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 846324a1-17c0-374d-a1a3-b3aac6eb0c8f | -7.01766 | -59.35831 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d3e4abd-730e-38e8-970b-b7e10d709e54 | -7.0174 | -59.40384 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0345c78f-75b3-34b0-937f-01d110bc113d | -7.01708 | -59.36201 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7294a0a2-1bd6-33e9-b87d-7cae72231b77 | -7.01459 | -59.39957 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b05f0bf-6b48-3c39-9d20-1892fe15de34 | -7.01426 | -59.35777 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3983707b-b37b-3464-9270-6d31a6db4c88 | -7.01399 | -59.4033 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c057479-bfa3-30fe-9d60-4f8030f66e55 | -7.01118 | -59.39903 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21df8f86-1956-3fd2-a7ee-a09d4f563ec7 | -7.00673 | -59.38311 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 575c9775-478b-32f6-86da-d3afa1f6fce0 | -7.0045 | -59.37517 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c092e53f-2dbe-30e0-a417-2b8c54e49842 | -7.00391 | -59.37887 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28211321-2128-3378-97c1-5cf8e1626295 | -7.00332 | -59.38256 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 793a4851-412d-3dbb-bece-558a96e24311 | -7.00273 | -59.38628 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3280888-57ff-36f3-a881-5fdbae69818c | -7.00109 | -59.37463 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30e68db3-196c-32e4-a853-dc74bff9302f | -7.0005 | -59.37833 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25fd2668-d487-3066-9a13-637399f8007c | -6.99991 | -59.38203 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34c1bd9d-7ab4-3faa-9792-17d45653ea59 | -6.99932 | -59.38574 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37702c69-1d9e-3de4-87f3-48d2475c1e79 | -6.99873 | -59.38944 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82912f41-a65f-3781-8f76-320655a79423 | -6.99769 | -59.37409 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1499ec01-aed2-37ad-b3d6-8412e277302d | -6.99709 | -59.37779 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d332ab8-4d8a-3162-9c2f-c68bb55f405d | -6.9965 | -59.3815 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0612d61d-7c7a-32c5-a851-6d1dd465316b | -6.99591 | -59.3852 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c0590ff-9931-3ae9-b94d-65ffb51f4653 | -6.99369 | -59.37725 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba10c5e9-9f59-36f3-aef6-7d0e85ee481c | -6.99309 | -59.38096 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3d44217-cdc2-34e1-bf5f-c46031bd0df6 | -6.98969 | -59.38041 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef533969-253c-386e-a97d-fcf7db4e15f4 | -6.90439 | -59.40826 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b55dcbc-79a3-3019-8b7c-702d22f87e39 | -9.27493 | -60.82968 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81a7395a-bfff-34bb-9421-7aec1b1df067 | -9.27205 | -60.82507 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dac6a251-3a85-3b4e-8597-2ce0dab0f9d1 | -9.2638 | -60.50229 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3915519-29c2-3b38-a376-b64c9647b5bd | -9.25335 | -60.50055 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9db688a3-2edc-3e36-af95-2c39ac559a4e | -9.24564 | -60.43933 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 278f05a8-eb1e-363d-9f3d-822193ff0f4f | -9.24499 | -60.44324 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README110.md)
