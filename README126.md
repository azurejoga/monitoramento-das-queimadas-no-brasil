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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 689cf79f-71c0-3f1f-bd35-c2541053759c | -17.13869 | -57.37238 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8c531551-c961-380b-a24e-de253d68dbec | -17.12636 | -57.39357 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 034b78d9-22f7-329f-8bf5-76f7ffa4b939 | -17.12366 | -57.38512 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 7f9a109e-fcd1-3545-80f0-2874f4c5aec0 | -17.12297 | -57.38893 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 2136c85d-2661-32d2-8391-a8122a3f09a5 | -17.12227 | -57.39274 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 0ecb6589-4870-396b-a3d1-0b02e2111037 | -17.11958 | -57.38429 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 1dd39a8e-3ebc-32be-8f41-fcc8428e1072 | -16.84953 | -57.45934 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1e9a6bbf-e653-3218-a37e-ff6c4274581e | -16.84881 | -57.46321 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6613a9d0-f318-3ab0-8a4e-c216ba4e1b9d | -16.8481 | -57.46708 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 41a5f9ed-63b7-3272-adc6-3a049715ead2 | -16.84469 | -57.46238 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a4cd12f1-0ef0-3cc3-b10a-33ab143ee05d | -16.84397 | -57.46624 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b73416eb-607b-3fe5-9198-84a82e58cf2a | -16.84056 | -57.46154 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 21d1092c-0a3c-3ffb-88d5-fb6327f40e4d | -16.83985 | -57.46542 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c70b2b05-57e1-3a4b-9909-9908ca18454b | -16.83644 | -57.46071 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 236ce597-1d53-3bec-b741-2a8f092b53b1 | -16.83232 | -57.45987 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a1e8b18a-a028-37e1-b48f-e7338d50ad14 | -16.83159 | -57.46375 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 8d6275fe-9ab7-394f-a6d8-22d30389f3e4 | -16.82942 | -57.47539 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 48bfffe1-9176-370e-b3eb-7c65d8180461 | -16.82819 | -57.45904 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f402a7e1-f71b-3ae6-af13-834c881ed1d8 | -16.82747 | -57.46292 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| d976d54a-bdbf-347f-8b8b-08c8fd07a1b9 | -16.82334 | -57.46209 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7498e03b-0334-34ff-a861-00a2d1823dc9 | -16.81995 | -57.45737 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c5e45ee8-f6b3-34f3-b739-e89fb228fbda | -16.81922 | -57.46125 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5b5973a8-e870-31cb-be19-e5f6ad1833c4 | -16.81582 | -57.45654 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 54ce7662-2305-3b48-b7f8-2f6cf8cacd43 | -16.81509 | -57.46043 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fc956232-c315-3b7b-9c78-a670babb9563 | -16.78896 | -57.47631 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8d73e862-9b99-37c8-9d11-7fe222dd2e1f | -16.7871 | -57.43959 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5c6c9d90-d4ef-30b1-ae24-4c25bae99f19 | -16.78554 | -57.47158 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 75b3afda-b5a4-3d9d-a46f-f3f302c85832 | -16.78298 | -57.43876 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 85e6f20d-3ad4-32d1-9f8b-0678614e2077 | -16.77998 | -57.47853 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 750d1f32-0dfe-39bf-98d7-079cce30e99b | -16.77927 | -57.48243 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b936888f-6d6f-395c-a5d9-be95cf678900 | -16.77529 | -57.45737 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0132b39c-9840-3730-8d62-9acee9ee4ecb | -16.77514 | -57.48159 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 888d7aea-2d15-36eb-9613-facc5eb6b9c4 | -16.77259 | -57.44874 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| cfe3f1f2-09cb-3a4b-a467-568b089758af | -16.77117 | -57.45653 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| fef5c6dc-09f5-3f8d-8bd7-9aae27c88d97 | -16.771 | -57.48075 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bec10535-0cc2-3a8b-8d72-98fac3107b1b | -16.77045 | -57.46042 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2907dc1e-43ee-37e3-94f0-38081d561f19 | -16.76918 | -57.44402 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f18cc302-e8f9-35c1-ba8d-6b341a11b52b | -16.76902 | -57.46822 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 043044fd-7ebe-3564-abe6-89923bf5db88 | -16.76847 | -57.44791 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 55d827ea-cbf9-3774-b671-5f2ce4435182 | -16.7683 | -57.47211 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d76bc68a-d283-3470-9471-b1f311152dd1 | -16.76759 | -57.47601 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 732ad2bf-e946-3396-86c8-653f584e7902 | -16.76687 | -57.47992 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 24a76124-b5b4-3118-89c7-22b07ae50375 | -16.76577 | -57.43931 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 80000ec4-260c-3c45-8bda-079a91312a47 | -16.76417 | -57.47128 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 479bffca-0c69-3788-a92e-5f83db64b891 | -16.76201 | -57.48298 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| edf2eb25-2ad4-3d69-a781-6dac046e2a6f | -16.76147 | -57.46264 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 016516be-99ad-35c3-9a83-191c6d1dfc6f | -16.76076 | -57.46653 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a9f36ef1-cd76-3dc1-8057-dd33a9f01616 | -16.76004 | -57.47044 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 95c364c5-e17e-32a7-b516-95a8d5a9e544 | -16.75734 | -57.4618 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 54b161da-6914-3784-b4bb-cfd6feb92dcc | -16.75662 | -57.46571 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| dd38da79-deca-3b12-bf07-734fc4f9b18a | -16.75249 | -57.46487 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| fc3ff5a8-d7af-355c-a943-643a0915b5d1 | -16.73865 | -57.47015 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 17c2c69e-ca5c-30e5-9e17-90bae453aaa2 | -16.73793 | -57.47405 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bade6110-00bf-3411-b2d5-8e3be184624f | -16.73742 | -57.45374 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| af8e8d0e-fe00-335e-a84a-40ce32e709a7 | -16.73524 | -57.46542 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| eafcb5dd-a03f-3876-a950-b27eb24307ae | -18.6679 | -57.28096 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| b30e1754-1bfe-3d28-a487-aa0baf635029 | -16.73452 | -57.46932 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7b132b7f-3000-344e-8fa2-111c6d1306f6 | -16.73379 | -57.47322 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2874af35-bf11-3c76-bcce-9e7fd4ddb4fd | -16.73184 | -57.46069 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 318dab94-f67a-34c7-9664-5a407fd66f6b | -16.73111 | -57.46459 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c11c089d-698a-3d28-b745-dea663ccfb18 | -16.73038 | -57.46849 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 2da1ef29-7ab1-3125-8c2e-75b6fb2cb5a0 | -16.72698 | -57.46375 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0facee85-2ce6-3873-a8d2-1bf0307b5f56 | -16.71458 | -57.46125 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e1630f0b-9c29-33f0-9ca0-7c1baf9478e6 | -16.71385 | -57.46515 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 51fa1167-4fbf-3a47-95ca-4aa5f9cd15e6 | -16.71045 | -57.46042 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 610fe683-1cba-3386-b449-2c50e073d8c4 | -16.70972 | -57.46431 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ee6af668-142a-3838-80ba-35ff8b5368cf | -16.70899 | -57.46822 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b5a570d9-51d7-3703-9e7b-53a5b157fbef | -16.70485 | -57.46738 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 230bc825-8512-365a-9ea0-a4f94a62678d | -16.70071 | -57.46656 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0e36fcc2-bdf1-3832-a4ad-448c642959b6 | -16.69998 | -57.47046 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5bc6e17d-cfbe-376d-91b2-6b435ce35ea1 | -16.69894 | -57.46659 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 50e76be0-e209-35e5-bd91-f4cd4e3eb12b | -16.69823 | -57.4705 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8e518d71-f5c4-370a-89a8-b2bc588edf60 | -16.69732 | -57.46182 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2d896709-6b37-317a-ae65-22e9c436e77f | -16.69658 | -57.46572 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 05d0b17d-9d31-3968-b864-00581266df62 | -16.69551 | -57.46184 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d11457d5-318b-3ac5-98f1-fdbb9f309ccb | -16.6948 | -57.46575 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8aefe6f5-9ed5-3467-85a2-ba75bfa95830 | -16.69318 | -57.46099 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bb7dcaaf-6eb6-3f1b-97f4-b0e7c812c60e | -16.69244 | -57.46489 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bbe46bbe-aaf8-3227-84ee-72a6e0a6890a | -16.69138 | -57.46099 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2b759010-99ec-3214-bc12-a5b42241498c | -16.69067 | -57.4649 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bbdfb92b-8230-3aa5-ab78-5964e0b487fc | -16.68724 | -57.46016 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 37da358b-8df5-393e-aef5-693baa78a6c4 | -16.68653 | -57.46406 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 351ef9cd-fb30-3692-8d8c-0e2a1b7f373a | -16.6824 | -57.46322 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| e7e1bda1-4b85-35d2-b2e8-b4840f846b19 | -16.68168 | -57.46714 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a1f7bae2-b013-343f-b550-7abd7374b827 | -16.68097 | -57.47105 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1a8ea776-9e3a-38e9-9e22-9fdb3fc2e35d | -16.67826 | -57.46239 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7f62507c-c353-394d-9070-4718fa0218b7 | -16.67755 | -57.4663 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ffd38ce8-80d6-33ea-a08a-da79bd53a023 | -16.67413 | -57.46155 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 43997cc8-d1ef-30af-96d7-7c3b4f1ca2e1 | -16.67341 | -57.46545 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e22cf01b-42cd-3907-ab14-ef1ddd58dd63 | -16.67269 | -57.46938 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| efb07910-b844-3399-bf5a-234c56874b57 | -16.67198 | -57.47329 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e84f8590-7505-3aae-8d02-5d9deccb6e04 | -16.66999 | -57.46072 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4c099742-adda-3efa-9722-a03d82d7d28e | -16.66927 | -57.46462 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 3f78d056-3fa7-3bb4-a739-389dbbdbee2b | -16.66856 | -57.46854 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4c50785d-69b6-3ad4-91aa-c99cb4026b81 | -16.66442 | -57.4677 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7bbbb2e5-4ec9-36d7-a690-064359c6f0d3 | -16.86271 | -56.72895 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a6939b1e-29af-3eca-a4b6-8ee0faf09bb3 | -16.81071 | -57.38027 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 34a5f8cd-dadb-3fbe-8514-f4e4d3c0c643 | -16.81001 | -57.38411 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cac90cc2-fb4b-3126-9274-2d90bd4e167d | -16.79628 | -57.38932 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d6074b93-0743-3281-8324-a84395dfddbe | -16.69463 | -57.16418 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README127.md)
