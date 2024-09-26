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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5ac2ccf-205e-3611-9df8-4a5471b78d20 | -9.18027 | -40.86819 | 2024-09-26 04:06:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd1a6f64-0d67-3854-841d-dd35914e17b3 | -8.95753 | -40.57662 | 2024-09-26 04:06:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 10b44243-5248-3e97-a6e5-2cf3e8caef6e | -9.36938 | -40.35939 | 2024-09-26 04:06:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6b7952a3-e21e-3b60-8536-9a6bb76b27b5 | -9.1667 | -40.53851 | 2024-09-26 04:06:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90647e67-38fc-370b-9095-d572ed29bb49 | -8.44012 | -40.54564 | 2024-09-26 04:06:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c48f85fe-f1cf-3c3c-996f-1fe4bf697c09 | -9.20679 | -40.2526 | 2024-09-26 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 98b7ea3e-4533-3946-a1cb-602ff2880bea | -8.51842 | -55.19748 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3be46c98-956d-3fdb-8ba4-420f0527bfb1 | -8.51715 | -55.20411 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2a07b2b-abbb-36cd-a2e9-b5c165210261 | -8.51305 | -55.18934 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41bfdabd-4121-3d4d-bb50-06fb97b0fae5 | -8.51177 | -55.19576 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d419081d-5bf7-3110-8d4f-a5c1875a4cbe | -8.51163 | -55.19583 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4f5e52b-6caf-3b03-b9a5-b496d504264c | -8.3187 | -55.01382 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 60ed326a-cf77-3d7a-9543-ac44c0c8a20a | -8.31432 | -54.99986 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 411b13ef-6054-3e93-b6ef-e7230c923547 | -8.31312 | -55.00612 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| cab3a60a-c218-307b-b4de-3657ed9f1b62 | -8.3119 | -55.01248 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4fff01e6-4c4a-3fae-b6ad-7665313d384d | -8.11724 | -54.8029 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18f7dfd7-4c48-3249-a59a-ef2a6a752c4f | -8.11605 | -54.80909 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fb8312b-d9f1-3071-915a-f581162a55a4 | -8.11166 | -54.79554 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9ed2ceb-7e39-3df3-a050-3fb92436eda6 | -8.11051 | -54.80151 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8739aad5-6333-33b3-81cd-80f1fbdeb12c | -8.09599 | -55.39067 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b4e41a3-37a4-3bb7-a427-48b6b61b9f2b | -8.09474 | -55.39708 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cf4fa2e-f53b-39d8-b764-0c09601e08ac | -7.81533 | -54.73992 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f78bf70-b187-30b2-b775-552f97a6fa5e | -7.8087 | -54.73798 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b27a1b23-d819-353f-9ac1-49639b4cbd85 | -7.80207 | -54.73607 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 277c2a67-34b8-399e-821a-f1972ac6a95e | -7.79891 | -54.71605 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ca23592-b2aa-32ce-9278-ba884e5a549e | -7.79783 | -54.7217 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9b5c912-0f87-3b64-bf51-c3f5e179bfc3 | -7.61266 | -55.35631 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41ecd01f-86e1-3b95-ba45-1ff6fcaadfa9 | -7.61138 | -55.36303 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 94c38f30-894a-3ae6-b9be-daf8a57f1ed5 | -7.61043 | -55.35502 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9ac4984e-3843-3abf-894e-cd92434c6995 | -7.61016 | -55.29332 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5b3bbbe-a7a6-3c50-845f-65bfd052f3e9 | -7.60911 | -55.36172 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 24964762-dd3c-3434-b288-886163493983 | -7.60568 | -55.3548 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 349fa2f5-80b3-3736-aa0b-4bc1f0bf4f17 | -7.6045 | -55.28505 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff1a79c7-b098-34b2-9499-5d6e19c1bcee | -7.60439 | -55.36152 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 96f06702-0bc6-3969-8656-609d32a7cc57 | -7.6032 | -55.29182 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a30c5c95-b3a6-3aa1-bb62-8c7fdce8f5ec | -7.59475 | -55.18551 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ae2f079-78d7-3bfb-b7b4-b50aa7176625 | -7.59349 | -55.19203 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a412ecb-bf7d-3823-b6b8-fb22b298d70b | -7.56831 | -55.17325 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55b47853-7a4c-3fdb-961c-349129ca6cbf | -7.56274 | -55.17058 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9f9d5874-1946-3098-b7e2-04bf298bfc18 | -7.56134 | -55.17204 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1eb81032-3041-34d2-8555-08703031d22a | -7.55714 | -55.1621 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9512e164-0d0b-3343-a7cf-420a3bdd3406 | -7.55714 | -55.1567 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48c4780d-9b63-3d9a-9cb5-57697314c828 | -7.55579 | -55.1636 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1528b343-bc4f-3cf9-87ba-5eed94b4ab4d | -7.55154 | -55.15371 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24f45cd5-a617-3e7a-bd56-639296daa170 | -7.55032 | -55.16014 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d732d84-e4ef-3842-b8bd-71903aa72e16 | -7.55021 | -55.15534 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3468b0b3-d4f4-340d-ba8a-a184eaec285c | -7.54901 | -55.16147 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fd85b1c-58fd-3b41-95c4-c4b2c98917ed | -7.38152 | -55.11474 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f496d01-42d2-3d3f-8b66-1d7465bc7847 | -7.38082 | -55.11276 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a5a6536-a2de-3004-9f72-6c4c743774dd | -7.38029 | -55.12135 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9e931fe-7db6-3181-b77f-922078ddb13a | -7.37953 | -55.11946 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59ee496f-3040-35fe-8bd8-0b71a45a50a5 | -7.17665 | -55.0267 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 93fbd92a-a792-3a4d-b650-8a85ad5b46bf | -7.17661 | -55.03163 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb564911-3e41-346a-b9b0-7fd60cfcbb5d | -7.17539 | -55.03328 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80460001-1999-3f0e-bd89-0fcfdd8c266f | -7.17086 | -55.02394 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e73de04f-f937-312c-9a01-05796bc7b1ab | -7.16962 | -55.03061 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7b465e2-0713-3513-beca-c912644044f8 | -8.51987 | -55.19082 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a38a8a7-1ed3-3414-95a6-8701bb6e4c4b | -8.51969 | -55.1909 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1246bbfe-67f4-3c32-8b8e-8afca485184d | -8.51856 | -55.1974 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a70ab6d-10fa-379b-b99f-e9e77a2b30b4 | -10.2563 | -68.2673 | 2024-09-26 04:06:05 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 56.1 |
| b2c5dcba-9393-39fc-bade-a4a49bfb1718 | -11.222 | -45.536 | 2024-09-26 04:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 15cf8df7-caf8-34fe-bbec-9cc9eedf6701 | -11.2029 | -45.5387 | 2024-09-26 04:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| e394ed91-659e-3072-8fce-9c042803e877 | -11.212 | -51.1627 | 2024-09-26 04:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| a86f3171-3d02-3839-9007-826a6db1a8a4 | -11.2123 | -51.1415 | 2024-09-26 04:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 96870cfd-94a3-3116-8725-3cb3e332a9d4 | -11.2413 | -65.2809 | 2024-09-26 04:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| ed503635-856d-3cd4-9cde-f455a2fa9f09 | -11.2599 | -65.299 | 2024-09-26 04:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 426.8 |
| 4a04dcfe-5fad-3d72-a117-6e83ffb8ec53 | -11.26 | -65.2801 | 2024-09-26 04:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 423.5 |
| 22a46162-3506-3c9a-a668-165feea1b078 | -11.2786 | -65.2982 | 2024-09-26 04:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| c3039343-44dc-3211-85ab-3e481c4f8ba9 | -11.2788 | -65.2793 | 2024-09-26 04:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.6 |
| c1882b08-542a-3bd0-9bf9-fd8296cb7699 | -11.2412 | -65.2997 | 2024-09-26 04:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 5b74ad57-cc4e-39bc-82d7-63167a9ab07c | -12.2367 | -45.5045 | 2024-09-26 04:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| d5c942a9-a42c-395a-ac0b-46f24ef102c9 | -12.2363 | -45.5276 | 2024-09-26 04:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7766a9a2-d219-3b3d-9ba6-50f41c2d8a5c | -12.2175 | -45.5074 | 2024-09-26 04:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 212.8 |
| ecc66ee8-a3c6-3f65-af0a-126a0f1cf8ac | -12.217 | -45.5305 | 2024-09-26 04:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 3a402510-a1a6-376c-88ce-7287060e69fb | -12.5023 | -48.9418 | 2024-09-26 04:06:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| cbeadfdd-83ed-3f66-8704-53ed3aaa3f5f | -12.5026 | -48.9198 | 2024-09-26 04:06:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 5adf9d47-c8f5-3667-aa6b-fdab627252b6 | -12.5218 | -48.9173 | 2024-09-26 04:06:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 60612617-8a27-39df-a57b-c89e2af134fc | -12.822 | -62.7078 | 2024-09-26 04:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| a862b0ba-4903-3f7e-a4b0-592c6189ae15 | -12.8222 | -62.6886 | 2024-09-26 04:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 939a476b-d30c-35ae-bde2-6d9a5b138bf6 | -12.841 | -62.7067 | 2024-09-26 04:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| cff95ed4-e1e5-3d93-8f20-fcdf019a633a | -12.8411 | -62.6874 | 2024-09-26 04:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 91f4b264-91d4-3886-ab82-c7a61939ac6d | -14.8828 | -51.4777 | 2024-09-26 04:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 327.3 |
| 58d9054a-786a-37ff-a64b-b3c59a3be70d | -14.9022 | -51.4749 | 2024-09-26 04:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| b7e64eac-23c7-357a-962c-9a2355160b65 | -14.863 | -51.5019 | 2024-09-26 04:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 238.5 |
| 4f9b8d82-e8d3-3d14-985d-1166ab223b82 | -14.8634 | -51.4804 | 2024-09-26 04:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 180.6 |
| ea59ab61-de05-320e-9983-6a5bfd48e77f | -14.8824 | -51.4992 | 2024-09-26 04:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 321.5 |
| a8891f02-50ef-3833-aefc-13fafecde90f | -14.9018 | -51.4965 | 2024-09-26 04:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 544fdcd7-53ec-350a-a2f6-f37328417fc6 | -16.1176 | -52.0082 | 2024-09-26 04:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| b1cf7f2f-d68d-3c9c-a3c3-087f8f4c5f00 | -16.118 | -51.9867 | 2024-09-26 04:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| c6bf87ee-c59e-318a-a45d-a72b0a497bfe | -16.098 | -52.0111 | 2024-09-26 04:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 8307de86-33f3-33da-b4bc-a528f248a723 | -16.0985 | -51.9896 | 2024-09-26 04:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| cee7dcc6-b153-38fc-9cd6-4ade7a783d2a | -20.6074 | -51.5209 | 2024-09-26 04:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.8 |
| 2dcf35f8-337a-3456-b485-f224ff39bb47 | -20.608 | -51.4986 | 2024-09-26 04:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.8 |
| 259caf32-bdfd-3eec-b695-c69a078055ab | -21.9374 | -48.5688 | 2024-09-26 04:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 934d63fa-d399-3550-b67f-b1af39e5f411 | -21.9381 | -48.5453 | 2024-09-26 04:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 271e9ba6-3c43-3040-8d03-f612b414124b | -22.2162 | -47.5603 | 2024-09-26 04:07:08 | GOES-16 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.4 |
| ddaf4bdf-3102-3947-a6de-836711c09f6d | -18.38321 | -42.79521 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3c61f2a6-837c-3045-8e0b-0c2cdd9dcccf | -18.38265 | -42.79892 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5e99b64d-e267-37a2-be1b-4d8d7fbdcf0a | -18.37985 | -42.79462 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 54ffa985-99ee-3ab6-af39-fc1f218e0374 | -18.36622 | -42.53724 | 2024-09-26 04:08:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README68.md)
