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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb7ba562-72a3-3029-87f4-5d226da472e3 | -16.7063 | -57.4718 | 2024-10-02 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.3 |
| 14c50836-b1a1-3767-b984-d1972f94a345 | -16.7108 | -57.1852 | 2024-10-02 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| ea6b306c-0c59-32d4-a32d-ce49e75c61d8 | -16.7265 | -57.4287 | 2024-10-02 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 7d7f3a53-99b7-307c-8dc7-a603d14754d1 | -16.7452 | -57.4878 | 2024-10-02 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 460ff771-5095-3bba-a55b-611b5f6c4b65 | -16.7461 | -57.4265 | 2024-10-02 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 92db492f-59b6-3316-a5f1-e38c41816187 | -16.7647 | -57.4856 | 2024-10-02 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| cbbd7db2-a852-3dfe-be7a-33f1f96bf3c5 | -16.8292 | -55.9152 | 2024-10-02 03:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 83266c90-9bbc-3e02-b1b1-83680f0797c0 | -16.8295 | -55.8945 | 2024-10-02 03:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 8a3de6e0-37c9-3183-9ad9-71049f70b239 | -16.8386 | -57.7628 | 2024-10-02 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.3 |
| 4d9e92a9-5881-3e15-b000-ac83d1daf6f2 | -17.0695 | -56.7733 | 2024-10-02 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| e675ec9b-d719-3297-91af-4306587f7bd2 | -17.0892 | -56.7709 | 2024-10-02 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.5 |
| 02bd3c98-ad8d-3db2-99ce-998eee8d7bce | -17.0895 | -56.7503 | 2024-10-02 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.9 |
| a1c21f15-2648-3a1b-86e5-c76ba4c4b961 | -17.1088 | -56.7685 | 2024-10-02 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 65cefce7-e77e-32c5-80a4-9574cef35b2a | -17.1091 | -56.7479 | 2024-10-02 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.7 |
| d9ae5b06-0e65-31c4-9357-2b2e925cbbe9 | -17.1288 | -56.7455 | 2024-10-02 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 47f2510b-3d0d-34e7-8dec-3fecb7ebc330 | -17.1971 | -56.1795 | 2024-10-02 03:46:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 890b6b28-2728-35b4-915d-7dcb0bed8a57 | -21.3456 | -55.6841 | 2024-10-02 03:47:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 78.7 |
| b3910371-6264-3f05-b360-2206eabe6424 | -21.3656 | -55.7022 | 2024-10-02 03:47:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 78b7b271-2ab8-37f0-8814-e98b0efd419f | -21.3661 | -55.6807 | 2024-10-02 03:47:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 9dfe40a2-abb7-3392-a1e0-cd762252265c | -22.9006 | -45.1029 | 2024-10-02 03:47:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.6 |
| 4c31877e-b611-386e-8ccc-c10bd00e08af | -22.9014 | -45.0779 | 2024-10-02 03:47:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.6 |
| 95e5e52a-9cc8-3c7a-81e8-36aef8821285 | -3.21276 | -46.79108 | 2024-10-02 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 890c59cd-d455-397b-a7dd-2d1e79206ec1 | -2.90443 | -47.11315 | 2024-10-02 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fff75c48-0a65-3943-bb30-62c5903001f4 | -2.9038 | -47.11686 | 2024-10-02 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb0a9221-27da-37ab-8007-9f37417c7cc2 | -2.62138 | -46.91099 | 2024-10-02 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc8102cb-f2ce-3584-ac36-31dea00929cc | -2.62078 | -46.91453 | 2024-10-02 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6c57136-f723-350c-8f88-40a5a42ed4c5 | -3.21388 | -46.78432 | 2024-10-02 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 296e0b25-caa6-373c-b567-140122311f5b | -3.21332 | -46.78772 | 2024-10-02 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 83a9d478-12c4-3564-8f70-39c25719f260 | -4.07843 | -46.21552 | 2024-10-02 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| daf86298-3cff-3b4e-99e4-5f212f805941 | -4.07791 | -46.21865 | 2024-10-02 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edccedf2-6cf6-35c5-a79e-cb1fbefb733f | -4.07333 | -46.21461 | 2024-10-02 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63d7e241-7d93-381e-a3c6-28fc039d43e3 | -4.0728 | -46.21778 | 2024-10-02 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96069cef-1b26-3d92-8611-3b19ff1426e3 | -3.69885 | -47.6006 | 2024-10-02 03:51:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eee511ae-b9a6-3484-90f4-850d09130f87 | -3.6982 | -47.60439 | 2024-10-02 03:51:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a794b9f1-a800-3cb9-8c9e-5d12a42a4cce | -3.69756 | -47.60816 | 2024-10-02 03:51:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68897923-fa6d-3296-a8e9-875c6306be6a | -6.28138 | -46.9942 | 2024-10-02 03:51:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1d0a3cb-512d-3c28-b8cd-5031ddc7aee7 | -6.27563 | -46.9965 | 2024-10-02 03:51:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 892ecafc-f1ff-3d23-b997-b9ac8dabf1d8 | -6.11953 | -47.27055 | 2024-10-02 03:51:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 569fce41-05d6-33ad-88a3-152b75ebadfb | -6.11895 | -47.27383 | 2024-10-02 03:51:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ba886e2e-0abe-3199-9a40-89b476215cc4 | -6.28082 | -46.99737 | 2024-10-02 03:51:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b72c850d-352f-3dee-9c78-61fc6c71d911 | -6.12425 | -47.27476 | 2024-10-02 03:51:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6dcb854-7d85-3b98-a55f-fb9e6eebb207 | -6.11837 | -47.2771 | 2024-10-02 03:51:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e8dbb377-a901-3d35-ab07-ef00106e1c14 | -3.46653 | -47.66882 | 2024-10-02 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d11b113b-106e-3247-82f4-740333be80e4 | -2.95664 | -48.00662 | 2024-10-02 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55d8e486-1749-3a51-be77-4d8f1f70c69a | -2.95586 | -48.00591 | 2024-10-02 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45db87be-000d-34fb-a019-c1489dae1ba7 | -2.9508 | -48.00556 | 2024-10-02 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc16a514-eedc-30a6-8fc4-d6811c16699f | -2.95002 | -48.00486 | 2024-10-02 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff89ef85-d738-3f06-bf79-4f9f908021a9 | -4.57728 | -48.01419 | 2024-10-02 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a66870b-d442-30e7-90c1-6d53b3ef5d7c | -4.57659 | -48.01814 | 2024-10-02 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37bb65f8-ead4-338a-8cf4-6c929318fa41 | -4.57613 | -48.01134 | 2024-10-02 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90129a6a-0a0a-3e3a-9953-e75e9f285c08 | -4.57547 | -48.01529 | 2024-10-02 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e7f3d1c7-c35b-3343-ba84-86295491a9e6 | -4.5748 | -48.01926 | 2024-10-02 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e330654c-29f9-3d6e-a19e-a7a0c684aedd | -4.57089 | -48.01714 | 2024-10-02 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c41660de-c7a7-31ca-8503-4059c11975ff | -4.55903 | -48.0083 | 2024-10-02 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 086c1e5a-61c5-3c69-bf78-bef4831df3d9 | -4.55836 | -48.01228 | 2024-10-02 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d02d7ed0-dd11-3390-b9d6-3e641023a679 | -4.28549 | -48.07673 | 2024-10-02 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70973a77-fbd5-34e7-b10c-d67786379639 | -4.28044 | -48.07168 | 2024-10-02 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6032cf3c-fbe2-3b6a-9a06-53f32be7c203 | -4.1928 | -48.23325 | 2024-10-02 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd683152-a2bf-35aa-bd9a-322297c384d9 | -4.19273 | -48.23581 | 2024-10-02 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ae53d54-fe56-3947-a62b-f18d5e8433ee | -4.19206 | -48.23746 | 2024-10-02 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d545ceff-1a17-37eb-b43c-ed0d30e3a8c8 | -4.17655 | -48.78354 | 2024-10-02 03:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26ccc534-7083-38bc-bf37-8f08f24cce6e | -4.17052 | -48.78248 | 2024-10-02 03:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d8eb299-146f-31ef-8287-7b48cb17a0c8 | -4.14015 | -48.40412 | 2024-10-02 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f6170682-4677-3588-91f6-6f7aca320ece | -6.41902 | -48.27198 | 2024-10-02 03:51:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61e34862-6d28-31c7-a98a-c7182c94ba58 | -6.41341 | -48.2709 | 2024-10-02 03:51:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cdced07-9e0d-3218-b83e-da9627c661c8 | -5.2208 | -47.95889 | 2024-10-02 03:51:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e73b79db-20ab-39be-baa1-e78f799088f3 | -5.22012 | -47.96271 | 2024-10-02 03:51:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| afbaf88c-75f1-3590-af9c-1839d6684701 | -3.14053 | -49.41907 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 17800baa-37cf-3f81-b57d-af3fe59987b3 | -3.13964 | -49.42418 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 1cf20292-7a56-34b8-a555-bcfb529e1091 | -3.13902 | -49.416 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 90a5e98b-e5ad-39f4-9434-102792da104a | -3.13875 | -49.42933 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 7bbf31e7-f3bb-3ba4-a284-bedf4e510410 | -3.13818 | -49.42105 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c0756942-67e1-34bb-8586-2c072fbd8357 | -3.13782 | -49.43468 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c68c0b7-7caf-31d4-996c-a0e919c475b9 | -3.13732 | -49.42621 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c321d624-a910-3a01-9387-8ae5fbcc5f00 | -3.13691 | -49.43991 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1e25cf2-641f-32ea-a2d8-97d697a8e4b0 | -3.13644 | -49.43144 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| fde5b408-5cbd-3b41-a6d6-7f44ace119b7 | -3.13555 | -49.43678 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb30eac9-950d-3f0f-9176-5d76d6f7d25b | -3.13503 | -49.41301 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 31a658a3-a109-3c43-be03-de4138d39485 | -3.13416 | -49.41801 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 359dac27-f5aa-32be-9e29-c8543a1766ba | -3.13327 | -49.42309 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 20c4300f-9152-300c-baf6-b5c4d4ca5dfa | -3.13264 | -49.41499 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 29b3b8c5-1a7e-310b-b89e-a26a20291436 | -3.13238 | -49.42822 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 16a3b551-e73a-3854-afc9-15a1eae12439 | -3.1318 | -49.41997 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2c936bd6-77c9-3c76-a1e8-e7e7fa9cf8eb | -3.13146 | -49.43351 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d215d254-d032-3d46-98d9-75f65e0e411d | -3.13095 | -49.42508 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 8aa14eb3-add1-3106-b7c9-7dff58c0ba64 | -3.13054 | -49.43879 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b767a79-3b42-3c37-a3aa-4751049fef62 | -3.13009 | -49.43024 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 1d91a324-69f3-32a8-8050-253524b83c24 | -3.12919 | -49.43557 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7331c24f-d036-3d83-8dd1-0bedd420cd05 | -3.12689 | -49.42206 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5fa12fe-9fb4-3ef2-ba64-0ff8af82af73 | -3.126 | -49.42716 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3ea52a1-482f-3aed-b2b7-5154d497e4f8 | -3.12509 | -49.43238 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af585b1b-91e7-32b4-8db7-95c6f60f209e | -2.96002 | -49.36689 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14bcee58-6f28-334f-b84c-dbf5a5fa3f08 | -2.95602 | -49.36391 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2e9db737-a997-36d4-9bee-cd2a3440a26c | -2.95513 | -49.36906 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ee82a5e0-52bf-3e21-be44-a912019487cf | -2.95364 | -49.36586 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa8ff23f-63fb-31f7-ab7e-bf672b985ea2 | -2.87878 | -49.15283 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61d796e0-c5d9-3cbe-87a3-38e1efca4834 | -2.87593 | -49.15102 | 2024-10-02 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f03fa360-17a8-338c-85af-68dc1ec7f3dd | -5.52173 | -50.04915 | 2024-10-02 03:51:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62fc87ef-14fb-366c-9f94-14efde11af26 | -5.5153 | -50.04827 | 2024-10-02 03:51:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 141aca05-8547-3ce3-9dfc-605d86436ae1 | -6.94093 | -43.40334 | 2024-10-02 03:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README60.md)
