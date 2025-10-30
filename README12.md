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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5eaf20ba-250f-3fd6-bb69-f7e78591bf7f | -4.83055 | -42.73445 | 2025-10-30 03:34:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3075519f-9254-36df-9626-193b6658b0c7 | -4.83121 | -42.7329 | 2025-10-30 03:34:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa430256-b378-32b2-bea8-40bc30bb2ae3 | -4.84528 | -45.8479 | 2025-10-30 03:34:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| da7dc41f-eb50-3649-aff2-4fda6d6b9749 | -2.76778 | -45.39423 | 2025-10-30 03:34:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0ecb7845-e17b-3935-8fad-c8177adc291c | -4.04853 | -44.26471 | 2025-10-30 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea699151-e37f-340f-a434-ca80573a505a | -5.91875 | -41.91538 | 2025-10-30 03:34:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4f37e422-1813-341c-ae17-e46e8f149566 | -4.05551 | -44.26092 | 2025-10-30 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ddd15c6-57d7-3882-b2da-51640d55ead3 | -5.45531 | -40.87629 | 2025-10-30 03:34:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9bee00be-1f57-3c37-8d3e-4ce77cdb5334 | -3.78887 | -43.90676 | 2025-10-30 03:34:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 93a1db32-fd6f-340d-8bc8-93aed25a3996 | -4.43481 | -38.88282 | 2025-10-30 03:34:00 | NOAA-21 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8799826a-aade-3382-9b32-903011760fdf | -5.03053 | -44.8159 | 2025-10-30 03:34:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 484165a1-2c31-30a4-8e1c-601aa3adb063 | -5.48559 | -44.10752 | 2025-10-30 03:34:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21e7c0ba-8196-3020-8cc7-f635478ecf0d | -5.72991 | -39.03569 | 2025-10-30 03:34:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| cd7ec92d-27db-3263-9a75-ae5fb40fe7b0 | -5.06022 | -45.32297 | 2025-10-30 03:34:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4c7e35c-309b-308c-b1ad-0c47cdbef7e1 | -4.05631 | -44.25634 | 2025-10-30 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a1ff0eb-7e63-3a2e-a09e-d02e48957734 | -5.81116 | -40.83602 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fc77f76b-796c-306b-90eb-383697374795 | -4.84079 | -45.42678 | 2025-10-30 03:34:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 715756a4-8b48-3b4b-b6cb-5995f576280b | -5.8834 | -35.2561 | 2025-10-30 03:34:00 | NOAA-21 | PARNAMIRIM | RIO GRANDE DO NORTE | Brasil | 2403251 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 197d9a82-93ab-3551-bf74-d7f2267f932b | -5.29797 | -35.97952 | 2025-10-30 03:34:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d7da3ebf-4202-3580-b9fd-497fbe0adbb0 | -4.82509 | -42.73554 | 2025-10-30 03:34:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17a08a5d-544f-3d33-a88d-6b0458e48447 | -4.48572 | -43.43425 | 2025-10-30 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da212a3d-93a2-3b87-af82-e7f94d33298c | -5.653 | -41.83662 | 2025-10-30 03:34:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5f5302e8-eb12-32e8-ab7f-46efa2de2887 | -4.48988 | -44.02081 | 2025-10-30 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27384469-c188-3c21-b3a3-988eeac6342a | -5.57726 | -42.17455 | 2025-10-30 03:34:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e812d1d6-7a34-3e47-8161-2b5a5f6916c6 | -4.69039 | -45.59428 | 2025-10-30 03:34:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dfcacb32-b9c8-3572-9d13-7d76c1e6c7e4 | -4.46776 | -45.75959 | 2025-10-30 03:34:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 83e0ec5d-4f3b-36b1-ad08-8a77da4c62e8 | -5.7907 | -40.81232 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 86ad79dd-46e0-3a4f-869d-ed6911bf8d6e | -5.65891 | -41.10167 | 2025-10-30 03:34:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0b14f13d-c525-326c-8ad9-e408ba0ea556 | -4.25939 | -43.70742 | 2025-10-30 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 249a3e00-2b65-30c0-9358-bbd852fb046e | -5.51639 | -41.2476 | 2025-10-30 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8061e18a-1a6a-32ec-81cd-d1ff44518640 | -5.5202 | -41.23838 | 2025-10-30 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3796de83-a6af-3dff-b328-342ce68a10fb | -4.04936 | -44.25998 | 2025-10-30 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7ec9819-11d1-3623-8e2f-e778fa56ccf1 | -5.8023 | -40.8078 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6e808d0e-7e08-33f7-a4c6-b89c11fccd98 | -5.793 | -40.82776 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 593695ab-e6be-3165-aa80-ffd70865d912 | -5.80676 | -40.83833 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 617d9f4a-5244-3bfd-84c0-ef63930330ea | -5.80839 | -40.82891 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9e92c8d6-6479-3af9-877c-ebb9d650f2bb | -3.79644 | -43.89882 | 2025-10-30 03:34:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 92a6a80a-c7e3-3ad4-8fd8-ec370e4d9633 | -3.64374 | -39.37677 | 2025-10-30 03:34:00 | NOAA-21 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dc5838bc-6d13-36f3-9013-b26b56f3527b | -6.2818 | -35.50954 | 2025-10-30 03:34:00 | NOAA-21 | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3890230a-d7c2-3f64-8191-a78bafae1667 | -3.79724 | -43.89422 | 2025-10-30 03:34:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cb1f7b19-0621-3926-83fa-5e9f52fa2bfb | -5.46079 | -40.87299 | 2025-10-30 03:34:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1d713c06-b3c1-30fc-89e4-d02cf4429c31 | -5.33422 | -35.54885 | 2025-10-30 03:34:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e46b91d-e875-383c-8de3-50c2083ff708 | -5.80758 | -40.83357 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6e30cb81-a3e2-3122-b412-fd278da9650d | -5.22671 | -46.14179 | 2025-10-30 03:34:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 273db6ed-8782-3928-a5a2-841e1d2855b1 | -5.79975 | -40.82244 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 058bee4d-8d42-3e2f-85ef-a8bbd260c299 | -4.98503 | -45.52038 | 2025-10-30 03:34:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c2a6204-f900-3ec1-ab0f-b27864f0b755 | -4.4728 | -43.44343 | 2025-10-30 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b06942e2-96c4-364c-865d-8013e99813e1 | -5.63964 | -41.08908 | 2025-10-30 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0cd78966-3c3d-3938-a55f-98b67324a7f3 | -4.84835 | -45.42196 | 2025-10-30 03:34:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9f642e46-f3d3-32c1-8dad-e8e4a9684816 | -4.82572 | -42.73194 | 2025-10-30 03:34:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9589a3db-76de-3d3a-af25-49e7fdd0a6d3 | -5.79548 | -40.81293 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c06daf25-db53-3ca2-9b4d-d18296208178 | -4.82506 | -42.73347 | 2025-10-30 03:34:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65e63208-22f2-3b86-851b-5cbe8520aa6d | -5.7968 | -40.81136 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 309c1e42-e6e0-3447-9bfd-3c3a1ac34c8a | -2.77452 | -45.39512 | 2025-10-30 03:34:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3b0f158-00ff-3bd7-811d-1b624dde411d | -5.44164 | -45.09825 | 2025-10-30 03:34:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9594d844-0f22-3a98-baf6-19ce7f593b7e | -5.41784 | -44.83607 | 2025-10-30 03:34:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eda561e8-6167-3182-b6e5-5402799640d7 | -5.03999 | -45.16771 | 2025-10-30 03:34:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 532c460a-70e7-317f-92af-aff6be69804e | -5.52317 | -41.23722 | 2025-10-30 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 025b50c5-a414-3fdc-827b-3553541e0441 | -4.26456 | -43.71263 | 2025-10-30 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 210bf4ea-f6e6-329c-856a-c17dd62833f6 | -4.68427 | -42.72867 | 2025-10-30 03:34:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5e0b646-ee26-3643-8783-6d8a6d8810a7 | -5.41692 | -44.8411 | 2025-10-30 03:34:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8941fe6c-b88e-3732-8eaf-d3c4115cbf17 | -5.06113 | -45.31785 | 2025-10-30 03:34:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce7614e6-eac3-3303-83e5-85c968bf2b4b | -5.79117 | -40.81565 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8996b0a3-7c86-362c-936b-a842ec986f76 | -5.20487 | -35.47738 | 2025-10-30 03:34:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 56a2122e-36a3-3f10-bddc-552a8efb068d | -4.43415 | -38.8868 | 2025-10-30 03:34:00 | NOAA-21 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cc7d12fd-8f3a-3da8-b119-fb769f42f096 | -3.80321 | -43.8955 | 2025-10-30 03:34:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c18acfbc-87a8-37d1-bc80-32300e1c77e1 | -5.7938 | -40.82295 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d3291717-a82f-368a-9c76-635f397549e5 | -5.82384 | -40.79611 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 60195067-40d6-3be4-b1f0-cefdf96e3d6a | -5.80643 | -40.8351 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dea44725-2fa2-39de-8b62-b052b207a661 | -5.30669 | -44.32378 | 2025-10-30 03:34:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03e7b56a-2adc-3f25-afaa-b9f2fd39e698 | -2.77145 | -45.39342 | 2025-10-30 03:34:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57c3c55e-cbda-3d1e-aa28-7dea2413d2b9 | -5.8006 | -40.81755 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9311129b-bb25-315f-a4f7-2541d157321a | -4.48584 | -43.43704 | 2025-10-30 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8d669ee6-57d4-3448-8e97-c440191fb11c | -5.23667 | -44.29763 | 2025-10-30 03:34:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1918a90-f740-3a09-a65c-bfa846f4da89 | -4.83963 | -45.35816 | 2025-10-30 03:34:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b69879a9-bd86-3ae1-8a59-7d7a370f97f1 | -4.99149 | -45.52188 | 2025-10-30 03:34:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 157885cf-3d0b-3792-9d10-3f56bdd1d397 | -3.43067 | -42.46304 | 2025-10-30 03:34:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0115b217-d59b-3c6f-8b44-25027ff00898 | -5.57271 | -42.17278 | 2025-10-30 03:34:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 79cd7caa-7093-30c7-a568-ec0e595852c4 | -5.79852 | -40.82391 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ac957133-3645-31b0-b024-094418a9b399 | -5.80559 | -40.84013 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5fc49783-3a51-3f42-87b0-7a9a390126be | -4.47204 | -43.44475 | 2025-10-30 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ca926fad-9a09-338b-81b8-7c9951db6690 | -5.79593 | -40.81634 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 421b1266-e0c9-37c7-bb7b-7f74d16a3f71 | -5.29831 | -35.97861 | 2025-10-30 03:34:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7ffed020-4710-3077-914d-59b800b35de5 | -5.3025 | -35.97518 | 2025-10-30 03:34:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2d35ba73-8bcd-385d-aa47-7131a2dfdd19 | -5.45532 | -40.87476 | 2025-10-30 03:34:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ac14b9d-0a7e-3b7b-a156-0306dfeef1af | -4.15235 | -43.88171 | 2025-10-30 03:34:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 57b22f4c-e43f-3f0e-8fa9-7b223af27a9a | -5.57327 | -42.16964 | 2025-10-30 03:34:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8fbf5780-4e58-3b28-8ce6-bb13da6a60e9 | -5.80798 | -40.82575 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 86ba6955-dcd6-3309-926d-5fdf68d4ba58 | -4.30547 | -41.43754 | 2025-10-30 03:34:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5414806c-326a-3c26-90fb-68395baf3f53 | -4.05467 | -44.26576 | 2025-10-30 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55d65096-9f91-3003-b5e6-129afd85d67c | -5.46005 | -40.87589 | 2025-10-30 03:34:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53dffef9-0e40-3ae5-8282-ba31a9d5f977 | -5.80719 | -40.83051 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d3110deb-cd12-3a48-bed9-ed6b4f5b8c4a | -5.23748 | -44.29306 | 2025-10-30 03:34:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea4d7896-1e76-3f9a-b346-65eefdac2213 | -5.79932 | -40.81911 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 29201b34-01c4-31ca-8b34-00d42787f177 | -6.13458 | -41.70579 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e09882b7-b8e2-363b-914f-93c75cafdfdb | -10.86418 | -47.62426 | 2025-10-30 03:36:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af5c0a25-60d4-347e-bd56-cc60193bdb3d | -11.17357 | -45.22309 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ee9745a-dc1a-3810-9853-89c9bdf8e5c5 | -10.27744 | -44.57107 | 2025-10-30 03:36:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82daf8c8-e832-3196-b4dd-7db9e5a05a32 | -8.90707 | -47.64589 | 2025-10-30 03:36:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0e25defb-b62c-3ec0-97d1-ced597067162 | -7.79192 | -46.41555 | 2025-10-30 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README13.md)
