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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 944cbdf4-3235-39b8-8fb8-94829616cbe5 | -6.35037 | -58.17989 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f680dcd7-76a7-3a7a-855e-a9d45d0d80a8 | -6.34961 | -58.18446 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 815b5d6a-3274-387f-9d3c-d3859457c550 | -6.34814 | -58.17012 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d33f48dd-1b65-3e43-910c-5d98c4afa527 | -6.34737 | -58.17469 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a2e4788-a2fa-3054-887a-18c1d054f497 | -6.34661 | -58.17927 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d19eabbf-c9f5-3b66-89d0-6eb92194f99c | -6.34585 | -58.18385 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 002cfebd-b2fe-3cba-8ec4-964e93e8bb3b | -6.34361 | -58.17408 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1622fe8-37df-3818-a086-e3755e892808 | -6.34284 | -58.17867 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75b99672-c780-3619-95b2-82d402eee1f2 | -6.33482 | -58.31996 | 2024-10-12 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb6e1414-51b9-314b-8a93-98c8ba0676f1 | -6.33405 | -58.32463 | 2024-10-12 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08194523-850c-3526-895b-ead10ab0e439 | -6.20247 | -57.78195 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00ea5381-31cd-3bf1-b041-a4b7540fbaeb | -6.19879 | -57.78135 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c3609a0-9b00-3913-b5e9-5547bb4ab213 | -5.96952 | -57.67247 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7adac91-8e58-31b4-9dcb-f852b31b0109 | -5.96836 | -57.67517 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c886831a-7e01-3b79-872b-11de76585003 | -5.95936 | -57.68864 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c6bf1be-3289-36a8-95f5-4024459fd678 | -5.95867 | -57.69296 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10085fe5-f653-38c8-8620-7c65297ede96 | -5.94182 | -57.70362 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c92e75-fe7d-3609-9a37-3e5c5f9abf95 | -5.93744 | -57.70732 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d597f283-167e-3afa-ad4e-6a624077ae6f | -5.93674 | -57.71167 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73428491-ac2d-357f-b3f4-0005716d2760 | -5.84454 | -57.70218 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfd9ac2f-54df-3a5f-adc2-ccb6d9ef0049 | -5.84155 | -57.69728 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 657f6a3e-e323-37a7-b81e-de201425d7b3 | -5.83855 | -57.69238 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f259884f-7d43-351e-bdb6-2331cc542930 | -5.83486 | -57.69181 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a370823c-bfed-3719-ae96-22d1fe5a5d3d | -5.80564 | -57.73169 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b368742-2cb4-3d10-9101-d51787442958 | -5.80193 | -57.73114 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fc059ee-4bfd-3ea3-b765-6592d4ecfc4e | -6.52737 | -58.40053 | 2024-10-12 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ff5ce0b-d4a9-3a91-8c61-31ffa3057d4d | -6.52357 | -58.39988 | 2024-10-12 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bfacb4e-7793-37e2-9935-408c0eac749b | -6.52279 | -58.40453 | 2024-10-12 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b6bef1b-f868-3b9b-82ee-a3a9ab74e847 | -6.51899 | -58.40389 | 2024-10-12 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6242ca84-7af9-3327-92af-84e5d07d0475 | -6.48197 | -58.4678 | 2024-10-12 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ef9ac18-75aa-3ea5-beaf-d3469892e8a6 | -6.91184 | -59.03986 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1727aaae-8ed4-37f5-a25b-f1aad8f78cbb | -6.89354 | -59.05253 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68ae01c7-87cc-3beb-aed9-47bdd9719e41 | -6.8927 | -59.05759 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a42ec187-7e38-3dc5-b484-668075945732 | -6.86958 | -59.07463 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f58dceff-7ee3-303d-84c3-7165450f8419 | -6.86873 | -59.0797 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cce8e8a-e0a3-3d35-9f1e-24543c0c2958 | -6.86788 | -59.08474 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cad8d8b-65db-331d-99c9-f2fab73ad7bd | -6.86648 | -59.06894 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 78e586bc-1ff2-3011-9c8b-5ba36e7868ab | -6.86477 | -59.07909 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9552f8a9-6fc1-3d3d-a89a-a00e8149637f | -6.86393 | -59.08411 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3fc176d-ffc2-348d-a288-795006001bed | -6.86308 | -59.08917 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 343f3e71-35e7-301f-9aed-672b4bc8c21e | -6.85997 | -59.08349 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d760d15a-02ca-3723-9c5c-715c327f69b8 | -6.85912 | -59.08856 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c4e6b409-56a5-3f4d-b532-8752b8522b2c | -6.81572 | -59.0373 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0455d8f-6432-3f2d-9581-cb49358b181f | -6.81487 | -59.04246 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ff86928-2036-3915-8823-1081a83bc0f3 | -6.74993 | -58.87655 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2120b109-97c6-3af4-9bfb-0045c82ca6aa | -6.7491 | -58.88143 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0f4004f-610a-388c-b842-27979930e0cd | -6.74896 | -58.8792 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c6a9ef0-b6ee-3a19-be5e-6dfb11b211c5 | -6.74817 | -58.88406 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc24eaa5-5698-334b-b2a2-374f3c2396ed | -6.74604 | -58.87581 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5737bfd-de2c-369b-a4f1-4bb6d230ea89 | -6.74587 | -58.87357 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d0371a7-3cd0-3e20-82ae-f805f72db965 | -6.74521 | -58.88068 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ac9928e-8453-3ffe-b652-d313cfa753dc | -6.74507 | -58.87847 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9817618-67bd-3804-bdee-4d196d6f6ebe | -6.74427 | -58.88337 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebecbe13-6d6a-306e-b4fe-00527235798d | -6.74197 | -58.87288 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 112f5f63-f48d-34b7-9c69-fea67e4d7c4e | -6.74151 | -58.42213 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1be7425-d6b8-32e3-98fd-0fdcc661cc65 | -6.74115 | -58.87786 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b65867b-d5b9-3ff8-afd2-a47df0b22e9b | -6.74034 | -58.88284 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2aea5423-4a8f-3c50-bdcf-af06846f26df | -6.73773 | -58.42144 | 2024-10-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 527a9d37-2b2f-388e-b0f6-0d7f8f79a76b | -6.6733 | -58.78042 | 2024-10-12 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d636256d-d4a2-3fde-afbe-1f1e829bbb33 | -3.70351 | -58.54412 | 2024-10-12 04:57:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 746d8c5e-9dbc-3a67-9dd5-08d5ff5c012c | -3.66882 | -58.80791 | 2024-10-12 04:57:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd22d28e-912d-33fa-807a-826a6a6703d8 | -3.54107 | -59.48342 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ede40166-814a-363c-8e76-506067082e7f | -3.52447 | -58.6954 | 2024-10-12 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 700de176-1a79-3df2-baec-10b80da055ac | -3.47786 | -59.50188 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cbcb732-24bd-3e31-9e64-8e33bca2dd02 | -3.47721 | -59.50594 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 415eab2c-412d-318a-8068-6669b4cc320f | -3.44651 | -59.61394 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6799610a-080f-3893-827c-81853121957a | -3.44584 | -59.6181 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7871bcd-3733-38f2-8a5e-2c997f03567a | -3.44517 | -59.62222 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 739d673b-929d-37b7-9afe-5b4b3871eeb0 | -3.4422 | -59.61325 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1fa739a-bc0e-3cb3-a694-472591a5172c | -3.44152 | -59.61738 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc2ec2e9-d41f-3640-99f4-a9734800ecc7 | -3.44085 | -59.62151 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01e0a12d-5486-3437-9bb5-d0842519d8c1 | -3.43788 | -59.61257 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 904765bd-b0be-3607-bd20-7dae14af07e4 | -3.26509 | -59.59893 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e376329-a476-35de-aba3-187d70b6f6c0 | -3.26309 | -59.59955 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5aaf91d-209a-3455-a7f8-7739982ba724 | -3.21744 | -58.93871 | 2024-10-12 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 983a9a13-a984-3f1f-9e83-a4a497158335 | -3.2133 | -58.93806 | 2024-10-12 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9fcb66d-fc23-30aa-9a41-c09d445fd6e4 | -3.2127 | -58.94176 | 2024-10-12 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8f5315e-3151-3834-9e48-60aa5afa251f | -3.14572 | -59.14193 | 2024-10-12 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be230559-6afd-3f4f-ac96-a7e310ee5b5b | -3.09753 | -59.38076 | 2024-10-12 04:57:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4a72c4b-c326-37cf-a52b-5146821d9b8b | -3.09325 | -59.38012 | 2024-10-12 04:57:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f883cd94-fd7a-3d51-b3ad-0be94c86031e | -3.09259 | -59.3841 | 2024-10-12 04:57:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be84e861-080d-3faf-8391-46a42404e222 | -3.04983 | -59.35764 | 2024-10-12 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a31d6dce-2022-3fe1-a57f-a7fb59865b2c | -3.04919 | -59.36157 | 2024-10-12 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 182b6350-d348-33f3-8830-10e288ac6d7f | -3.77347 | -59.36444 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f7dcc25-e986-3adf-a1ef-693f6a611696 | -3.72732 | -58.47332 | 2024-10-12 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26db483a-f7dd-3ea1-8c68-c86a10f1e583 | -3.72677 | -58.47674 | 2024-10-12 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a39ff3b-a221-3438-9a26-423d531aa454 | -3.72334 | -58.47264 | 2024-10-12 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3d260af-1e5a-305c-aa3d-a2610308796d | -3.72279 | -58.47609 | 2024-10-12 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be443b91-6122-36fb-a295-13cfb06af1a1 | -3.71643 | -59.28783 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77e6bb35-51a4-3e2a-b643-789be44890f5 | -3.70752 | -58.54472 | 2024-10-12 04:57:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2ad274c-a2b6-3c98-a3c0-42ea36b1459a | -3.63549 | -59.09089 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d04466de-e4ca-3fbf-81c3-09625a7031e7 | -4.42406 | -59.52751 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa179346-c6cd-3923-9667-0eb619f470c7 | -4.37836 | -59.94038 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0258a614-401f-3835-ab0a-eaa6fe18ae64 | -4.2902 | -60.01262 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96636a5f-8197-3a34-bf70-af40d06b8ba2 | -4.28945 | -60.01365 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6bcacfd-94bc-3c47-9c0f-8bcff0a3b7ae | -4.28582 | -60.01193 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77bc7271-f9e9-3575-8a0a-7dabcb025b82 | -4.28507 | -60.01294 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68ac99c2-e386-333d-8b93-d1926550f58c | -4.27009 | -59.96704 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6717f87b-cf89-3c4d-94e0-91ab846bfe72 | -4.26964 | -59.99738 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2deaabdf-5521-3d6a-9380-5921875e2f0f | -4.26527 | -59.99665 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README64.md)
