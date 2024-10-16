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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df2b4a09-6f30-3591-bd95-19518893d5a9 | -12.47977 | -64.01983 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a020136-1837-37e5-a08e-833231a2837d | -12.47661 | -64.01451 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ded2a0ba-8a2d-3ce8-943f-615919a8ee46 | -12.47595 | -64.01926 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42e18fb4-b2fa-3545-9d01-3991ae71730c | -12.36199 | -64.49365 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa85a81f-48f9-3d55-9598-475337c62b56 | -11.72208 | -65.22994 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 27678138-a1ad-3adc-b32a-68eaeaad7b73 | -11.71914 | -65.22536 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4a6e5ce0-6326-372e-8010-af82bb338407 | -11.71853 | -65.2294 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 26f95c33-1450-334d-8af4-4349f487b182 | -11.71558 | -65.22481 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 645f7605-1d4d-38a7-b516-9d4318bffc44 | -11.71203 | -65.22427 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4b0c3d7-3b3f-373a-9293-e4904c3483a6 | -11.71143 | -65.22831 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bf228b0-999e-3025-9c36-e626d0783db5 | -11.70848 | -65.22373 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60a90ddd-cd7e-3831-8fe4-540ae25207dc | -11.70788 | -65.22778 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b21a82e-ff96-3865-b8d6-248d4a4f929d | -11.70728 | -65.23183 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8633677b-a9fd-3cfd-8573-1865e9391797 | -11.70673 | -65.21102 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92e8bed6-0388-32cf-a5e5-6d3fbd21c0b6 | -11.70668 | -65.23589 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62f22672-1f2e-3f33-b996-b1638aef284d | -11.70613 | -65.21508 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9040d095-eab7-304a-b7d6-ddad61621874 | -11.70493 | -65.22319 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d05e9323-5e29-35dc-9613-0fb550395871 | -11.70433 | -65.22724 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d419c8e3-f372-3267-91e8-10b2e35e31f6 | -11.70373 | -65.23129 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a6352b4-3604-3723-8904-37695b539b29 | -11.70313 | -65.23534 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e92dfa9-4468-3e3a-8585-3bdb5f25c79b | -11.70253 | -65.2394 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03682a9b-741d-331e-8cd6-d80346877440 | -11.70138 | -65.22265 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f616a317-9f16-36d2-808a-481a1abdff52 | -11.70078 | -65.22669 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81467106-f885-3630-9370-c19b002a45dc | -11.70018 | -65.23074 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42f6b717-3b76-30f2-a7b9-11e41d895936 | -11.69958 | -65.2348 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 469b796f-2ff4-30b3-b9be-290976e3a60a | -11.69898 | -65.23885 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51657e90-529f-388a-9b89-8951e90c8252 | -11.69723 | -65.22616 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e714dab8-2e97-379c-bb59-3b61530ff625 | -11.69663 | -65.23021 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7005ed02-0732-3bc8-ae27-6df1d5c6212f | -11.69603 | -65.23425 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e85ba2f8-8eaf-3c98-945a-30664d4dffcd | -11.69547 | -65.21345 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6189a27-eb3d-36db-86ee-25570420be76 | -11.69543 | -65.2383 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39360d80-72aa-3adf-b9a1-5c71844523cf | -11.69192 | -65.21291 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2941367e-d32d-3d2e-9a31-b280ce016824 | -11.69188 | -65.23777 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2044cea4-5e03-37ea-a89b-ff34a8450824 | -11.69132 | -65.21696 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2e8f1b7-3457-3460-afc2-37c63a2f2b8a | -11.68836 | -65.21238 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c93baff3-66de-3539-a9ba-0930710606e4 | -11.68777 | -65.21644 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ace7cac0-5aaa-3d82-8f79-b073e47b48de | -11.91637 | -64.87572 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c089b1d8-21f3-35e2-89b2-80c829cfbb57 | -11.91516 | -64.88417 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb4ab0c8-8a0d-36b1-b513-d829345f0167 | -11.91394 | -64.89262 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b562f04-f9dd-31d2-92d5-581e33e7e538 | -11.91093 | -64.88786 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9c95b9e-ad98-361f-a567-65723beb2a09 | -11.90365 | -64.96414 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6aae182-1443-3adb-add3-2618cac9cd16 | -11.89867 | -64.93925 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 851ac8ba-7e84-38d7-941f-ed4d49706162 | -11.89586 | -64.94144 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b04fb948-b19f-303d-8fc4-c8e655a7dfb8 | -11.89586 | -64.91569 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cfc7692-7531-371a-a845-69299e471553 | -11.89526 | -64.91989 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02283194-5312-39de-b8cf-896027beed87 | -11.89506 | -64.93871 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebe9744f-1127-3a16-8e0b-627755118219 | -11.89457 | -64.9172 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85f920d1-3067-362e-b751-e224955456d3 | -11.89395 | -64.92139 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e78f11d3-cf7a-371e-b37d-470ddc22e3d5 | -11.89285 | -64.9367 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a15b9b31-62a1-34d9-9885-69eef0cc9833 | -11.89207 | -64.93398 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a175a3e-3fa4-329d-899b-91d99a1de8bf | -11.89034 | -64.92085 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b44bfb53-8c9c-3811-a601-58913d754847 | -11.88971 | -64.92505 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 049f3ded-99d0-3ffd-a3fb-a283cdc18daa | -11.88909 | -64.92924 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c16bf31e-8dc4-3a2b-84cd-86e83310040a | -11.88847 | -64.93343 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a176fd59-8983-3351-8116-c3e54e8f57da | -11.88548 | -64.9287 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1084e4b-e4af-3353-821c-be04dc753a1e | -11.82127 | -64.83723 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b29ba79-8a6f-3255-9c65-80713174484a | -11.82062 | -64.86732 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4237934b-9a13-36a5-ad19-0956cbfed8e4 | -11.81704 | -64.84089 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 874ba54d-2db2-3bac-bfe3-26b7b7b637be | -11.817 | -64.86678 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c90d2a9-fff7-32b3-bf99-4ad9cd79f4a4 | -11.75023 | -64.81543 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 051aa625-febc-3523-9a38-cea1d02e4a12 | -11.74785 | -64.80639 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0a6c0a0-ec14-3c54-b55c-f8e47947ca3a | -11.74723 | -64.81065 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0dcfde9-1378-3de1-a236-e8ab7a758f85 | -11.74599 | -64.81913 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5443624e-b853-3b90-8561-a4cef4af2dd1 | -11.74422 | -64.80585 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b0b13c3-4f28-328d-a729-827187296461 | -11.7406 | -64.80531 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd7bdf41-2f19-3a85-8161-6783f6e98ee1 | -11.73697 | -64.80476 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9b411ec-a178-32f7-a65a-734ee6ea9d70 | -11.73273 | -64.80847 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec885a15-4543-31bb-aff7-0bd1554b5b6a | -11.73211 | -64.81271 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f4912dd-1c27-3d5e-ad25-bae13114b22a | -11.72849 | -64.81216 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db31e5c0-6532-3b7f-a71d-5b29d7a45e07 | -11.72693 | -64.97478 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcddc49b-64f1-31b0-901b-af7a487587d1 | -11.66237 | -64.82904 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 448b4746-bfbf-38d6-91b8-e4c89d3ab24d | -11.66176 | -64.83324 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da3b581f-7556-38d9-8125-2ea519a703d9 | -11.65814 | -64.8327 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 409536a9-f7dd-332d-bca9-26a3f26a1d19 | -11.65576 | -64.82374 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c609741c-f716-39e8-b791-b61aa38154f8 | -11.65452 | -64.83215 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01764ee9-79af-38cb-892d-d66827206e5f | -11.65152 | -64.82739 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76ac7230-2840-3589-9114-4634012a0856 | -11.65091 | -64.8316 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 208e69ff-bf31-3f2d-9ec5-cefdca39e535 | -11.9575 | -64.84727 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 230b1e1d-25fb-3743-99da-651efc49b8f8 | -11.95388 | -64.84675 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c605a1de-065b-379c-a29e-dc7bf424ac6e | -11.95025 | -64.84618 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3f739b3-0a88-3809-8033-bb3d1df61c0f | -11.95019 | -64.87208 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d21049a8-3e1b-36ad-b802-06a4f7a1f7da | -11.94663 | -64.8456 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b9bdbfb-852c-36cd-b9cf-c3daca75a029 | -11.94595 | -64.87579 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f07c5225-6358-37a7-951b-7575fdf012bf | -11.94534 | -64.88003 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89201779-18b5-39ec-9f67-7ea2c95cc4cc | -11.94294 | -64.87104 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a65c46ea-4bc4-3ed8-8b6a-2c19dda42491 | -11.94233 | -64.87527 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1282667e-da44-3910-9083-be232f565bfb | -11.94171 | -64.8795 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18fd99da-4bc0-3601-88cd-362fa29dc77a | -11.9411 | -64.88372 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 384ce94e-b92a-398d-9352-5e1e70e1c844 | -11.93993 | -64.86628 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36f003e4-9ac9-393b-a3e6-90d849ab4532 | -11.93932 | -64.87053 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10cade90-4d32-3dea-92cc-ba55cf703102 | -11.9387 | -64.87476 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 736ed3d1-9ba5-3a00-8e9e-bf9323cfa9c6 | -11.93809 | -64.87898 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73eac6b5-d058-3157-b091-10050c8a3d40 | -11.93748 | -64.88319 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7b63483-6186-3413-a7d9-9267b7c613dd | -11.93742 | -64.90908 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20231eb6-aab8-30c9-9416-55e030ca4bf5 | -11.93569 | -64.87 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd46da40-960c-3815-9cb1-07fb9ab4639c | -11.93386 | -64.88265 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0af7eef-c600-35b1-81fc-1c2a3f69076c | -11.93207 | -64.86945 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95de12e7-b9d9-33a2-a845-be30a4c913e1 | -11.93146 | -64.87368 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4bf081e2-18c3-34d9-a6a3-16692cdd4209 | -11.92784 | -64.87314 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5ba1c28-16a0-3eb5-9dca-e53cb0979f23 | -11.51502 | -65.12178 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README71.md)
