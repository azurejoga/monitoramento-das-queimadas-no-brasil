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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a51e092-7bfe-3bd3-baf5-99b07a73fb80 | -16.09835 | -57.54719 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0834da38-2898-349b-884c-5538ff21f791 | -16.09385 | -57.55009 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b93e3b7f-e114-3293-979a-832ac867df52 | -16.09335 | -57.55379 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2617aaa-9a4c-3217-8fae-16cedb55ccb0 | -16.09244 | -57.56061 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3182e7f-f255-37f4-97ed-0fa5e075901a | -16.08843 | -57.55988 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cbe5f55-5bbe-312b-8cec-71a2cfd9d90d | -16.04783 | -57.52516 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a289c78-0243-3fbb-82de-51a9ae7d9c28 | -16.04426 | -57.52103 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70a13bf8-a95f-334e-bcf1-0a137b86271f | -16.0438 | -57.52455 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6079f473-48c0-3064-befb-03de278bb2c0 | -16.04068 | -57.51694 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14e3cfc0-096e-3582-a015-6ccee82f26ec | -16.04024 | -57.52036 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d54e3d2-d9b2-37d8-bd7f-390f69d815cc | -16.03977 | -57.52391 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 433e18f5-6508-3ae4-ae6d-30b16a87f7d3 | -16.03664 | -57.51638 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f315dddd-a48a-3fed-8764-613a335e90f2 | -16.0362 | -57.51975 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b2bceaf4-9f24-3a0c-a5f1-8dc5186daedf | -16.03305 | -57.51237 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ead37bd-5478-3441-be79-06769ed63f4e | -16.55592 | -57.72419 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c24c26aa-34c8-393f-bf74-e4376e844878 | -16.55546 | -57.72778 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6958269d-4cd4-3fb1-9941-fd760ec24e93 | -16.55144 | -57.72726 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d897ae21-3417-39e2-af9b-0ba78ce09fd3 | -16.54836 | -57.71948 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 14aecded-6a2e-3a2a-a07a-b3922eda27f4 | -16.54789 | -57.72307 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ea75066e-65f8-3374-8200-288716914003 | -16.52563 | -57.70541 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| af80229e-6128-3f70-ba99-ce7e6f68de5a | -16.52519 | -57.70888 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6b54131f-eb71-3627-a83d-4db8a797ab45 | -16.52443 | -57.70564 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 37a7a629-d008-32e3-a893-156f1f2af7b2 | -16.51143 | -57.71099 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f64ebafd-4f2b-3ad0-95ae-20fa5cbb925d | -16.51096 | -57.71452 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 6d9c80d8-a3ac-3f6a-8034-e088b2dd49b4 | -16.49588 | -57.70492 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8aaa51cf-4841-35dd-b8f7-17734ec380e7 | -16.49282 | -57.69724 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 77600499-b1ff-3094-a8ad-d7c2097de1c7 | -16.48948 | -57.72226 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8ef05032-5d4c-3679-8837-3a067258b22a | -16.48854 | -57.72924 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 69f43553-da07-3446-b046-87891edf0375 | -16.48263 | -57.24612 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b4699944-b0b9-3091-9750-3482d802c7a7 | -16.47075 | -57.27201 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6110d726-bff3-349a-8fec-d14d2707289c | -16.44877 | -57.34261 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 6edefa88-d2b6-3a76-b0e4-049805d3e5e5 | -16.44466 | -57.34204 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 50cc998b-7530-3763-9660-e4f48363a0c8 | -16.43925 | -57.25591 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 90989101-115c-3f8d-b5c2-d68ae50d9aec | -16.43875 | -57.25973 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 11c42539-c38e-373c-b006-020a5e41d140 | -16.43645 | -57.3409 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e9289a44-fc23-39df-8325-c0b6366383df | -16.43512 | -57.25532 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e4f0bf80-4a47-35bf-aedd-ff074f31dd26 | -16.43462 | -57.25912 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0e5fbb2f-79f6-3f81-8edd-6b92b1e6c7f5 | -16.43284 | -57.33654 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d49966c7-6a59-3e18-9349-1de5ef36ff64 | -16.43234 | -57.34032 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 28d844ed-1a0f-3716-8e9e-e68ae05162b8 | -16.43099 | -57.25472 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f0db71bf-4c64-3bb2-8fd2-79883f4e990f | -16.43049 | -57.25853 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| aa7f59b1-ba03-339a-a745-9a7171bf0b86 | -16.42873 | -57.33597 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c58ab5c2-31eb-367d-9b82-b42a5cc0e86a | -16.42823 | -57.33975 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3b4ffd21-b166-3346-9720-3eda01062328 | -16.42462 | -57.3354 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5c62aa63-3cac-39c9-ac03-620242be687f | -16.4174 | -57.32666 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 48df5226-84d4-3e75-8b6e-932044d4eb21 | -16.41329 | -57.32608 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 07a361a1-f4fc-3ba4-a5be-b689be41bf86 | -16.38802 | -57.39195 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3101365a-bc89-30f6-821f-7cdf62d5d1e4 | -16.38462 | -57.69981 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 03b5f23a-d32f-326a-a0f8-005dbcb50ec1 | -16.3806 | -57.69928 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 39d3b513-a8c2-3fb6-8d04-3a65f9a38e14 | -16.65952 | -57.08597 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 529708a8-d6dc-30f0-9aee-97c082631818 | -16.64924 | -57.13287 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 5e4c5295-ebe4-3629-9277-af4d6149e358 | -16.64822 | -57.14074 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3ea22d48-5d60-386b-9935-780132c04554 | -16.6055 | -57.14281 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| aa507679-26e3-3aa0-bb3f-7290a3d8d8f7 | -16.59054 | -57.14974 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 59017c0f-d33e-39ee-a0ad-f3bafdc9d823 | -16.54556 | -57.74103 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9316c649-443f-38ee-a85a-ba687a9be67b | -16.5451 | -57.74454 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5f1b6400-3e88-308d-b641-623c222d7072 | -16.54247 | -57.7333 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8671b258-598a-3a30-9131-de02ea25eeba | -16.54109 | -57.74393 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b7449457-550e-37a8-a536-3cee9bb8ac4e | -16.53709 | -57.74331 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6b17555e-52b7-3fb4-8a48-ac7ebc693592 | -16.53355 | -57.73909 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ad730611-8bbb-3d15-a58b-058a97ff5aef | -16.53309 | -57.74269 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b7ab8eab-7aad-3036-97a4-e5dac8822487 | -16.52955 | -57.73847 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f1f3538e-29bb-362f-a422-2c73c4628618 | -16.52908 | -57.74207 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 165b1979-10d6-3981-974c-84b55172db6c | -16.52862 | -57.74565 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b54c0923-0935-372c-879f-5c72d1351ff3 | -16.52462 | -57.74501 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 18fc1a19-350c-391c-9968-438fcf7df9ed | -16.52366 | -57.74154 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7c00e4cf-831e-338e-b936-ba174e7d20db | -16.49462 | -57.74488 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 25d36bd4-c96d-36c4-a168-1e754710f18d | -16.49159 | -57.73702 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 74db6aba-b47e-39f0-9d7b-65089e59eac6 | -15.52614 | -56.89981 | 2024-10-08 05:23:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 928e2920-65b8-30f0-96e8-8e46aa7f2080 | -16.64873 | -57.13681 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 65d5cb52-1ca2-3688-9ad9-695060dc13cf | -16.62987 | -57.11813 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9fcc8313-0dc5-3125-af6d-3894ab8a1fd7 | -16.62619 | -57.1136 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5ffbb2c0-3bd5-3da3-a0b9-4faa63413726 | -16.62569 | -57.11755 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1012c5d4-75fb-326b-8edd-97fea0070aa6 | -16.60967 | -57.14339 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 19e7e53f-4136-3e25-8e78-9bc15cc8b5ee | -16.59002 | -57.15368 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| eecb1aaf-43b9-3cb4-9182-f376e0524fa3 | -17.7417 | -57.09543 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9de508f0-8a02-32e1-b092-fe04236d6554 | -17.73746 | -57.09483 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d0e6d4df-c2d7-3c66-b0f6-4b55e995a113 | -17.73154 | -57.07306 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 463ad8ad-d6c4-3ad4-b957-0e1f102f19d7 | -17.19375 | -57.34372 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d901fd16-fa5b-3176-9e9a-2de6d19aca76 | -17.16321 | -57.35134 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 02660331-f7af-3eda-8565-257c1ee89c9d | -17.1624 | -56.75292 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 64612299-12c5-3d7f-ae46-8c0a5418367a | -17.14449 | -57.43146 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 045964ce-19fb-303f-8aad-bbd18941ad34 | -17.14089 | -56.8187 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 68fb106c-188d-3496-ae77-779f1c737e76 | -17.1243 | -56.84631 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ff6f29e8-52eb-305a-b612-4426c098b83b | -17.12024 | -57.42414 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 504e326f-6826-3e0c-a054-edb1388321ab | -17.12002 | -56.84572 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 370d350c-b313-3cae-8832-2ce4a8a5e780 | -17.11975 | -57.428 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 700ebe55-0203-3dd4-9446-5909be89cbb4 | -17.11926 | -57.43184 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 370d2e1e-92cc-392b-af21-c96ca9de0231 | -17.11877 | -57.43568 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 581bb479-f287-3805-9134-467f16c728ed | -17.11611 | -57.42356 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e76471c1-f8d3-3f8c-b488-7c28a9c0c013 | -17.11465 | -57.43509 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| d77b8262-565a-3393-94e6-c89a2e24586b | -17.11199 | -57.42299 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c7051b9e-4ba0-3de1-ab7c-1e6712bb7c13 | -17.1115 | -57.42683 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| da87d7d1-1780-3deb-818e-320eb6a2331e | -17.11102 | -57.43067 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ed41f233-08eb-395e-923a-24b235d8f6b3 | -17.09988 | -57.36668 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3f350fed-6b7c-3638-b9d4-ed87aee35cb0 | -17.09937 | -57.37055 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 72575b6d-4845-3fb5-9b16-af8df0ac85f3 | -17.09861 | -56.84279 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8b7f934d-f82e-3a0c-bff9-a188ea630b18 | -17.09524 | -57.36996 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6a5223ab-11cd-333a-bd89-1766bff172b4 | -17.09473 | -57.37384 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 60c14b08-39a5-39e9-9eb2-b20265fe4076 | -17.09004 | -56.84161 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README117.md)
