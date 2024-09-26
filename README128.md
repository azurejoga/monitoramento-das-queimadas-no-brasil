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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38c9ffc6-3259-3efa-a517-aeb50ddf28c0 | -11.20808 | -54.77875 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 97fa3d6b-f2b2-3c0e-ae9a-ae0353b9ea39 | -11.20758 | -54.80383 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddb38456-ce0e-336e-865a-e6ab747a167a | -11.20754 | -54.78226 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| aeb1c659-2914-3845-9dbb-52f715bf2066 | -11.20699 | -54.78577 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 3f2d22e2-d788-35e3-adac-f79ce0416534 | -11.20695 | -54.76421 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 679dd006-7ae7-3911-ae5b-bee98a3fa3f5 | -11.20645 | -54.78928 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| fc3fee40-8c7d-33c6-baef-ce99a39fd206 | -11.2064 | -54.76771 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d413ab16-abf7-31f0-8a2c-12799db5c57d | -11.2059 | -54.79277 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16760de7-8af5-3670-8822-a98d0f4b7318 | -11.20586 | -54.77122 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f51d6ee5-caf7-387c-87b1-d360b8fe4462 | -11.20536 | -54.79628 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 180967ea-43a0-3196-a1c5-585e24c17f1f | -11.20531 | -54.77472 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 0fa4222f-8d0e-33fe-8e28-28436a0e1fb0 | -11.20481 | -54.79979 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ac75c1d-be2c-3dc3-946d-ce0b220e4186 | -11.20477 | -54.77823 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| ea55aa47-0b22-38ce-afae-8631937be9db | -11.20427 | -54.80329 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb0e4559-0c10-330c-a7b3-3657a8926913 | -11.20423 | -54.78174 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 23b7559f-f0c6-32d3-b05a-2d3c38d2e38d | -11.20418 | -54.76017 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16dcb7f6-d3ec-3944-be13-627d22369e59 | -11.20373 | -54.8068 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5767f610-52e8-34df-9c63-4440055f9fa8 | -11.20368 | -54.78524 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 2d77b315-1c0b-3d0e-b6a3-89e23bab6155 | -11.20364 | -54.76368 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec0f0e7f-1662-31f1-aab3-adba6f522f59 | -11.20314 | -54.78875 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| b7f96636-662b-37c4-ad3c-1371bfb08534 | -11.2031 | -54.76719 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ec18160-d6ed-3653-8767-6cbba217e2c8 | -11.2026 | -54.79225 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 276e018f-0aa7-3f46-b03a-51f414eba17e | -11.20255 | -54.77069 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 8a7c92ae-85ae-3074-951c-a9f30dda3d71 | -11.20205 | -54.79575 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f65c0fda-bd0d-3b5a-8f4c-1a74d17320bb | -11.20201 | -54.7742 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| bc9cb8db-925b-3aca-92e9-bdf39a7dbde7 | -11.20151 | -54.79926 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e06e939-fa35-3445-9d36-2d220be74ed4 | -11.20146 | -54.7777 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 06671087-d6ca-36d9-83f5-f1f5f91355ec | -11.20096 | -54.80277 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed081132-fc54-3af1-b81f-66430ede36e6 | -11.20092 | -54.78121 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 20438c36-51c5-317f-8a99-4ce06ad598cd | -11.20088 | -54.75964 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bf58a58-a5ac-34f2-bdb9-d3f292dab690 | -11.20042 | -54.80627 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1459d20-e58d-3505-ad82-081d716d87c7 | -11.20038 | -54.78471 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 9ac90615-26fa-3d08-a32c-a9b89b1aee92 | -11.20033 | -54.76315 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d5aca08d-0ee1-3f7e-94cd-7f5ef2fec57d | -11.19983 | -54.78822 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| df8991b2-e9a5-374a-9fcf-2b650f69a6d2 | -11.19979 | -54.76666 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1d6c7886-5838-35b2-9e2f-a67100335fcd | -11.19929 | -54.79173 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 083ba35a-cb14-3636-a7ba-4209634c872a | -11.19924 | -54.77017 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 971e8d8d-0e80-3d9e-bb4b-81fcd9c152de | -11.19875 | -54.79523 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3952622f-8ef6-3f3d-ad25-64c236c6a443 | -11.1987 | -54.77367 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9515a06d-e727-3c98-9f65-0ee50d0c7e4e | -11.19816 | -54.77718 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7501319b-06c5-3089-8ab9-c92cef0db065 | -12.67766 | -54.6647 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c21c75c-1d55-315d-8191-61a5be1fad9f | -12.67711 | -54.66828 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d89df91b-7dbf-354c-ad1a-9e903b71a236 | -12.67657 | -54.67185 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4ea8beb-9e9d-3453-bf92-c34f682cd029 | -12.67602 | -54.67543 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06a906f6-a3c3-3044-a79b-16cbc52a263e | -12.67547 | -54.679 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e90fa824-e4eb-3980-b7da-94e8b407a09e | -12.67489 | -54.6606 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e499977-bcda-3c22-bf95-46a9c80e7917 | -12.67434 | -54.66418 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1bdb9bd-90a7-35be-b7d0-63d0b2db3fbc | -12.67379 | -54.66775 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5779b769-18f1-3d0c-b6db-e91fa57c394f | -12.67324 | -54.67133 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d02c3a11-6bf2-3543-a275-c82babbfed00 | -12.67269 | -54.6749 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32a71937-7026-3e4a-aeb5-0d15f7246dee | -12.67214 | -54.67848 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49817715-1eaf-3913-baf4-24606ef1f0c6 | -13.98152 | -54.58181 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2f0976a-61ce-3809-9026-9de3cf56c1b7 | -12.67159 | -54.68205 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fbc65d8-2daf-3417-8c69-d52d1e81bd7b | -12.67101 | -54.66365 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a22bd2af-d375-38e2-8070-dcc8e9f2c95e | -12.67046 | -54.66722 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 465469ce-eeb9-3462-ae32-e110afb32f43 | -12.66991 | -54.6708 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e36eb4fd-d873-3fa7-9c05-5bf78e3e673f | -12.66936 | -54.67438 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a9f04e0-aa14-3e1d-8726-4251acad8dd5 | -12.66881 | -54.67795 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e80d2c54-0818-3ac7-b7ed-e9428e4d4845 | -12.66826 | -54.68153 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7448a01d-88e8-3f6b-b11c-9c2df7557fbf | -12.66713 | -54.66669 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b3d4386-596e-3b73-bde2-2918f04ddeca | -12.66658 | -54.67028 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a82bae6a-cf19-3d7b-ace0-167023300b27 | -12.66603 | -54.67385 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2457f33-da8e-38d5-bfdd-5038bf3b2fef | -12.66549 | -54.67743 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 433bac00-2f3a-3316-a4bb-5c5dc6e96bc9 | -12.66494 | -54.681 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d5e48cb-e336-3a9a-bcac-bfdb6a3a67c9 | -12.66439 | -54.68458 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3e7f9c3-cbfa-3321-8b76-d218311edc51 | -12.6638 | -54.66616 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d6d6bd8-90f8-3fc4-ab4c-3c83ccecdd7a | -12.66326 | -54.66975 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfc93847-9acc-37ed-a4a8-c643c0b80b3e | -12.66216 | -54.6769 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af1d581d-5ab5-3ab5-befa-e50d41c0ffb8 | -12.66161 | -54.68048 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30554ea3-796f-3db8-8629-0919f8a79fd2 | -12.66106 | -54.68405 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba9b9186-56ff-3c74-81f4-394c64f8a43b | -12.66051 | -54.68762 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bf08dcf-711a-3ba7-9f2a-7e13a375dadf | -12.65993 | -54.66921 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57761269-8540-33c8-802e-f48f6cb63ff5 | -12.65828 | -54.67994 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79254522-671e-3432-8d49-3f22feb7526d | -12.65774 | -54.68351 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ab02b4b-5969-348d-abd5-ebec463d8082 | -12.65719 | -54.68708 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97136b97-db11-3e72-88a3-769515cd3b05 | -12.6566 | -54.66868 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 289c4750-7bc1-3674-b2d8-cc3aa7f275aa | -12.65496 | -54.6794 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 439f10bb-4339-3cc9-8961-e34b5ab5ed6b | -12.65441 | -54.68298 | 2024-09-26 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75c9859f-932b-3843-9508-9c51f80db4bc | -13.98488 | -54.58235 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aa47984-f045-3fb3-a045-bd807264dd07 | -13.98097 | -54.58546 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f628d88f-36c0-3760-abfa-8449c1e29d3e | -14.47425 | -55.49351 | 2024-09-26 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 620eec84-b200-3390-a6c0-56231f6d66e2 | -14.1249 | -55.74931 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5d46ce5-679c-3b36-be4d-73a3c6b78b8c | -14.09904 | -55.71969 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cf35ccc-8399-3f13-9083-2f481a978361 | -14.09574 | -55.71915 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16c04ccf-fa4e-3f1f-833e-02b01164225d | -14.08914 | -55.71807 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a591132-0fb6-360a-a3e4-401c3bf4cfda | -15.19654 | -55.96548 | 2024-09-26 04:59:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69a2c47a-d05d-3cd9-8890-29f661726436 | -15.19324 | -55.96493 | 2024-09-26 04:59:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8e5aa47-f908-380e-8fe7-8320a717927e | -9.83313 | -56.30873 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 774a4252-8223-3c53-976a-67e869c6c3ce | -9.83256 | -56.31235 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 321d007c-ab70-30b2-8aa2-59827ca2488d | -9.8292 | -56.3118 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02fc0d3f-b7c6-32e7-a430-c0bd6d251714 | -9.70449 | -55.53437 | 2024-09-26 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ab84661-98b0-3810-b3cb-fb7b603c7855 | -9.70174 | -55.53032 | 2024-09-26 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bbf828f-4e69-37dc-81ed-6b2a86a142e4 | -9.70118 | -55.53382 | 2024-09-26 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af6ca7a9-5578-3b9e-9f3d-8ffac50a69b5 | -9.70065 | -55.51579 | 2024-09-26 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5726a584-f2a1-3971-ad4f-6260f249a949 | -9.6979 | -55.51174 | 2024-09-26 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9cc589d-ee15-313c-9871-a071711e7af3 | -9.69734 | -55.51523 | 2024-09-26 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 189e73db-d585-30aa-93c5-765d68dc791c | -9.69348 | -55.51818 | 2024-09-26 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca3fecc6-cd67-3199-9a67-95959700732d | -9.68046 | -55.1686 | 2024-09-26 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0ec1c1e-e44c-32d8-a1be-4bc213a7c6cb | -10.76701 | -56.38403 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70395fb5-498a-317e-b8ca-bb4c3c6681ad | -10.76644 | -56.38762 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README129.md)
