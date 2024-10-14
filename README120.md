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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d689c6bb-4820-382c-a146-eae95484893f | -17.89329 | -57.30815 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ed29a271-01c3-324c-9f1b-9a1c6e3f76df | -17.89324 | -57.3114 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a47544eb-d599-3866-9ea6-1bf11c7d2833 | -17.89269 | -57.31226 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6af90b27-9e88-3de2-90ea-47f4e45ec356 | -17.89155 | -57.29529 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| f2364dc4-55dd-3cca-91db-2faa9bec1154 | -17.89096 | -57.2994 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 63fe3aa6-a6fa-3354-9cf3-1722a93a7c02 | -17.89036 | -57.3035 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 80f64c0b-e2cb-3df3-a520-5af8d8809fcb | -17.88977 | -57.3076 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| fbec0e51-c155-3c75-9494-3e892b1c6521 | -17.88923 | -57.28651 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 504.6 |
| 8015ddb9-d568-3afa-9c4f-adf7d680bea7 | -17.88917 | -57.31171 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 256cc747-a737-3923-87bd-5537aac37216 | -17.88803 | -57.29475 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 2acc9756-3bb4-368b-9a52-84458ba3247e | -17.88744 | -57.29885 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 27154b26-7e3d-366c-ac4e-f239f3a518fc | -17.88684 | -57.30296 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 99c4d424-2be9-391c-b7c5-ec642b9355bc | -17.8863 | -57.28184 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 65edfdcc-a3e1-3870-9cca-81e1b3de7c62 | -17.88451 | -57.29419 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| ec4548aa-5f6b-3f09-8df4-5504ac20c454 | -17.88392 | -57.2983 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 9b412ef7-2e1f-3ad2-9922-4976ec06bc95 | -17.88332 | -57.30241 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2992e224-1887-3620-8639-80418106e7a5 | -17.88273 | -57.30651 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 03865d12-91d1-38da-95b0-f3b39d488420 | -17.88218 | -57.28542 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.0 |
| e61b73aa-b086-3e0d-849d-ef161bc7362e | -17.88099 | -57.29364 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 305ab47d-c0eb-3cb8-bb35-70a584468ea1 | -17.8804 | -57.29775 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| ff8ff064-41fe-3580-abba-94baa1b8fa10 | -17.87981 | -57.30185 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d83da67d-ede7-36c8-a05e-fae04e47eaff | -17.87921 | -57.30596 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 26b36a08-26f3-3a52-b370-51fdf022e6b1 | -17.87862 | -57.31006 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f93b5a71-94a1-3155-8c66-5a2db64ffd58 | -17.87807 | -57.28899 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 35e7ccc7-ab44-39a6-850d-9ea552e1b7b4 | -17.87747 | -57.2931 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.2 |
| 8471e0af-15c9-36d0-a5bb-5d21389cd450 | -17.87688 | -57.29721 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.2 |
| 1c58d8c1-e5a4-3136-9fa1-3371b7bb5884 | -17.87569 | -57.30542 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 069e4a64-c1b1-3ec2-99af-0b2b68bd1aa6 | -17.8751 | -57.30952 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 306fc1fc-90a7-36b3-813b-c8bf88a2a503 | -17.87395 | -57.29256 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.2 |
| d5ef0cef-bbb1-3ba6-8ff2-5d593eef6df3 | -17.87336 | -57.29666 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.2 |
| 832b4cbf-5d22-39d0-a7d5-0d8effce9d50 | -17.87277 | -57.30077 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| ffabb0dc-e8c6-316c-9f1a-0ccafd51fff4 | -17.87221 | -57.27966 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9dc160f2-7809-3c3d-9deb-6dcad6fb9426 | -17.87218 | -57.30487 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 14016af0-ff07-376d-b356-105573aa1910 | -17.87158 | -57.30898 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| efb27572-5a6d-3e84-a719-56495f47224a | -17.87043 | -57.29201 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.0 |
| c97f0984-4694-3397-82da-f62ff8b006d9 | -17.86984 | -57.29612 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.0 |
| 755c7ed5-86bc-337b-a863-40631e3a8ef9 | -17.86928 | -57.27499 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| de2465ff-7a61-36a5-8476-4883706a0877 | -17.86925 | -57.30022 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 6a635689-bb6b-322f-bc12-a8d57fcf2c9a | -17.86866 | -57.30433 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d2ccc0ea-337e-3580-8ae0-83c67a5316db | -17.8675 | -57.28735 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.2 |
| 48f70453-5907-3394-9f60-3db85184e0fe | -17.86632 | -57.29557 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.0 |
| 3f5154c3-545c-3c93-ad8b-a49c9a0d2c00 | -17.86576 | -57.27444 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1533eeea-b55c-3147-a15a-ac6be41cb60c | -17.86573 | -57.29967 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| cfe0114c-3c26-33ab-810c-8a0b7c8dc03c | -17.86514 | -57.30378 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| cb37c134-a29d-3480-bef1-06997eba9c38 | -17.94016 | -57.28504 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e7fb94bb-43d8-32f9-b32b-85643bba68d6 | -17.92548 | -57.28696 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 325e11cf-2340-3ef4-9b0f-6ee3d1b5960a | -17.92254 | -57.28229 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 5c10c41e-2e9e-3361-afe8-33661819a1da | -17.91607 | -57.27707 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 954c1592-1fd3-395a-9681-74b9b30887b1 | -17.91432 | -57.28944 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 389.1 |
| 7c8328a6-5bb3-385b-810a-1ff4622918bd | -17.91254 | -57.27652 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 35927b65-ea2e-345f-a810-9275fa030ed6 | -17.91196 | -57.28065 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 250308ce-1cef-375b-bbbb-93ed8be2e067 | -17.90786 | -57.28422 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 33374696-1396-3e43-8541-005b0e3d798b | -17.90376 | -57.28779 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 283.6 |
| c686fa58-a768-33ac-81a4-94ccb6e1c0cf | -17.90197 | -57.27488 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b93635f0-b961-37cb-85a2-395e47342a91 | -17.90159 | -57.27579 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ac831bf6-18fa-3df4-bfda-1233212e8060 | -17.89979 | -57.28814 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 203.4 |
| d0cda8a5-7175-3df6-a94d-df0cd2b8e023 | -17.89844 | -57.27432 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 09e24a0d-d9d8-343b-9687-08311d63ddb1 | -17.89729 | -57.28257 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| b486ba60-7f1c-3ca8-b1fe-d6cf280572f2 | -17.89671 | -57.28669 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 218.3 |
| 7bb55329-a08c-38a5-8aef-1ba33109d1de | -17.89102 | -57.27415 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cd528c38-eeb0-38ad-acb3-d3db49a4393a | -17.88749 | -57.2736 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 40464862-ac28-3e0f-9d8f-10a7cabc2662 | -17.87985 | -57.27663 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c4bc60ad-44d1-3f7a-80c3-2f0e609703a3 | -17.87633 | -57.27609 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b795be5c-2be6-354f-a089-0a0df593bfd0 | -17.86869 | -57.2791 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4dcf34af-9336-36be-b5aa-f05d039ddff0 | -17.86517 | -57.27856 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| da707e2f-2f3a-3cf7-abf3-17c43cc55681 | -17.86457 | -57.28268 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| f75c6770-4965-354a-8ebb-c8aff900a097 | -17.86398 | -57.2868 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 9f4ac958-d20d-3177-90b8-22c2fc39d3a1 | -17.86223 | -57.27389 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 102368b1-2658-36a2-8ef5-c12a47e248d5 | -17.86105 | -57.28213 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 3170b006-a2e1-3677-b508-be7e3572af2f | -17.85635 | -57.28981 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.7 |
| 9419a841-3fe5-3c3e-8586-8c0529f691cb | -17.85283 | -57.28926 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.7 |
| 638c6037-56d5-32c3-b347-43de9e2e041e | -17.85049 | -57.28049 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2115a9be-5bb1-36cd-9c87-461266f06d54 | -17.84227 | -57.28762 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| db786e34-be21-3727-944a-a84a76424d52 | -17.90844 | -57.2801 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| e7ef4664-d9b6-3b3f-8882-8188fd8dd703 | -17.90433 | -57.28367 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 4cf313e4-5952-3c01-a4d4-f16cf3a32a25 | -17.90081 | -57.28312 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 7b80d53c-ecb6-39aa-8b37-8e8141bb9abb | -17.89687 | -57.28348 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 9f604693-0010-3d48-8dba-38b8d3fbbfcf | -17.89454 | -57.2747 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 80e91aff-ae1c-340a-bf29-648e76e236e9 | -17.8869 | -57.27773 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 42d6dfd2-b39f-3d00-9090-556a65061d72 | -17.88511 | -57.29008 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.0 |
| a018b5d9-b014-3388-96fe-577a12b08d50 | -17.88159 | -57.28954 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.0 |
| 706ac649-3a16-30fe-a22f-1415104d6ef8 | -17.87926 | -57.28075 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ceccdb89-6094-3df7-8557-8477b0088f8b | -17.87573 | -57.28021 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e49b02d6-2b47-3ce2-bed5-dab67e9c5883 | -17.87102 | -57.2879 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.2 |
| f4ba8c28-4d06-38c1-b7d1-f48c013b80fc | -17.86809 | -57.28323 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.2 |
| 66aeb93f-2360-3a6a-ac13-af6440b4c318 | -17.85753 | -57.28158 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| fed089ed-ff0b-318f-ba70-efcf27d422f0 | -17.84931 | -57.28872 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.1 |
| 7a403266-440d-3b59-a88c-8fda9e954a70 | -17.84579 | -57.28817 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.1 |
| 61e9c2b6-61d8-3371-bec1-f69d62d3a23a | -17.94309 | -57.28971 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 476541b2-3ee3-3ac7-981e-82b4e965e895 | -17.93252 | -57.28806 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 377fb39e-b537-3a2c-84d2-9205c6c38273 | -17.929 | -57.28751 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ad317d40-6c1d-3795-bfad-067d2f1ef2a4 | -17.92606 | -57.28284 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6ea6b77b-d811-3590-89c1-2f91bbcebe56 | -17.93957 | -57.28916 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5b1aec3c-9a21-3db1-a922-58c0321c2d2b | -17.93605 | -57.28861 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 15f43b36-26d5-3c03-9e68-d17b5373b548 | -17.93311 | -57.28394 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| efb33834-e6be-3d23-8756-081e341f0878 | -17.92958 | -57.28339 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 931f5228-b41c-3e35-a0fe-cf3ccf93084b | -17.91901 | -57.28174 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 71b084de-5281-3aa6-b002-c78494616502 | -17.91843 | -57.28587 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| b8c7916e-3823-3d44-a9fa-9dc07b298888 | -17.91784 | -57.28999 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 262.2 |
| dc7426c3-c942-36ba-968e-ee96ea864edd | -17.9149 | -57.28532 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |


[Clique aqui para ver as próximas entradas](README121.md)
