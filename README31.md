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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d06d3770-3a3c-3db5-9e7b-93d1c8f20f6f | -7.02402 | -59.42194 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 928ff4d7-cb57-3c33-86b0-e2e31e490d08 | -6.97033 | -59.47861 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e639f808-735a-325f-abb9-2f2a6dd71546 | -6.80938 | -59.14221 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ffa64496-363c-317d-94cc-a3858878af9c | -6.78339 | -59.32312 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ba6ff6af-e32b-3679-a1bb-a0c450089bd8 | -6.78156 | -59.3109 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 2183f9b2-bd5a-3a17-8089-1d6873c9c2a1 | -6.77315 | -59.3247 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 9240e20e-0b75-3254-a3a7-ebee8d4dd753 | -6.77131 | -59.31251 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1961bf62-d3d2-3786-adb2-413ea813eb36 | -6.76596 | -59.33174 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| fd4e33e0-9caa-339c-bf35-415dda84625c | -6.76421 | -59.3196 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 3bd1de1d-d000-3813-9981-00fd60dea623 | -6.76289 | -59.32621 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b3cc77cf-352e-3abd-ab3f-fd14839728eb | -6.76106 | -59.31411 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 44417f4e-d3e7-30cb-be88-24b7375b1371 | -6.75571 | -59.33324 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 235fedb7-1422-3c1a-a535-77be70af5e9b | -6.75396 | -59.32116 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 2d97086a-ebec-3f26-8d75-0d88e06ca699 | -6.74547 | -59.33488 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c8ad5a3d-c9c3-3136-8475-9a11a4acbb4b | -6.71959 | -59.30145 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 02117e4b-d846-3289-8a16-fe2179d6e7d4 | -7.99884 | -61.32246 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0367ac4a-f9dd-3773-819b-1f269c66afb7 | -7.9975 | -61.31313 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 11b8b419-a5c3-3710-8cab-a3766429916b | -7.9898 | -61.3238 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dd23e06f-7976-3bab-a7d9-924383310cb6 | -7.98846 | -61.31448 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 67c88ccb-8d3d-3dcb-bac3-6757b6aaf33f | -7.93877 | -61.61062 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65469587-3f3c-31d2-a351-e5006a8b847d | -7.93761 | -61.28018 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 77132e3a-2370-3a5d-aa20-3417de977d8a | -7.93628 | -61.27082 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aa2ceb12-d94d-335d-a970-2758b18ecd28 | -7.7969 | -61.58749 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e8e071e-823a-3fce-bf59-5bbfacd4de05 | -7.7956 | -61.57833 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c9c2d55d-c23b-34e2-a4b7-5cc37aa1d19f | -7.78215 | -61.35345 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a8bada9a-1777-3332-8b81-e43d630c9ad4 | -7.7731 | -61.35478 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 13b74c4d-d7e0-36ef-a639-4ba20c71597a | -7.77178 | -61.34545 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 30fd3e9c-ea9d-3c08-99e5-cc56a54592ce | -7.64141 | -61.20794 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 80e9950b-057b-3e26-afb2-30a64032136a | -8.16338 | -61.37726 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3183458f-7a26-3521-a846-977ccdacdd44 | -6.27387 | -62.4897 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 15fcd549-8e31-324e-a7be-0726fd1dc241 | -6.27262 | -62.48079 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7e4ec859-95a7-3d97-82f8-39a052c0874e | -9.12559 | -61.27206 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ca592c42-3d36-3dc8-a4cb-f408566062d6 | -9.1166 | -61.2734 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 309.8 |
| 548d163f-58ca-332d-b3e8-e53326ed2874 | -8.56838 | -63.41327 | 2024-10-10 01:54:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74cc4491-96cd-382e-9545-7d846f1f40a4 | -8.65141 | -63.4141 | 2024-10-10 01:54:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9d69c657-3fc3-32f5-b681-29ece8a52518 | -8.69012 | -63.08976 | 2024-10-10 01:54:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4b0d77ff-b74b-3728-b8ab-d1734d52d197 | -8.69135 | -63.09872 | 2024-10-10 01:54:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 84174a36-3053-326f-a1ee-75720c2c12ed | -8.77084 | -63.21568 | 2024-10-10 01:54:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6e2476f8-bd08-3de2-80a8-01224f544a8d | -8.77209 | -63.2247 | 2024-10-10 01:54:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 4e2d7b53-b6e9-35f0-9d34-2a6bbfe542ff | -11.33244 | -61.62972 | 2024-10-10 01:54:00 | TERRA_M-M | MINISTRO ANDREAZZA | RONDÔNIA | Brasil | 1101203 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d9a3ff21-5f1c-32d3-a0e4-84a3a17baa62 | -9.48344 | -62.37523 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2364684e-e866-39bd-8418-cd1ae9bef547 | -9.58077 | -62.13984 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57758465-5a5a-3a63-bee9-66172f04646b | -9.58202 | -62.14875 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e4bedac-366d-3b00-be72-a7f2fb7aa45f | -9.81534 | -62.70932 | 2024-10-10 01:54:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8e2277d5-c629-31e3-a922-826ab7822531 | -8.23554 | -61.17349 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 46b50fc6-b9ca-30a8-972e-75484cb0407c | -8.2369 | -61.18288 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 92c573ba-2ad5-3b2a-8110-b5a9352be162 | -8.99852 | -61.61121 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8f328fbf-6600-31f6-aa6c-c6ac9e45b050 | -8.99216 | -61.63063 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4c6733f0-2407-3678-85f4-0d2685773371 | -8.99088 | -61.62158 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| af154dc1-13f2-344a-9cfe-b419a89c66d0 | -8.91145 | -62.3676 | 2024-10-10 01:54:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b70a213f-ffc4-37d7-94db-3450df4727b4 | -8.91021 | -62.3587 | 2024-10-10 01:54:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 0a9c4d93-460a-397c-a1f9-bf87d29cb7ec | -8.90262 | -62.36888 | 2024-10-10 01:54:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3adb9b3f-3dc2-3fca-a939-bf50b0fa8397 | -8.90138 | -62.35999 | 2024-10-10 01:54:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 7be56706-2f74-3b2e-8e20-b7253b122f58 | -8.90013 | -62.35109 | 2024-10-10 01:54:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 96c1b12a-9247-3e68-b896-4d9c0bd449a8 | -8.81838 | -61.70538 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8505804f-f70c-3fcf-9fd3-0902bf3b9c9d | -9.1269 | -61.28129 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| f035342d-5926-355f-8bdb-cb4ffe81bce2 | -8.23825 | -61.19226 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 5ed5c33f-2cb1-3d3e-bd43-1deda0a7e668 | -8.23961 | -61.20164 | 2024-10-10 01:54:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3fc89ed3-d89d-3286-a281-55de7ef6b33c | -9.12055 | -61.30104 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b32c4607-b779-3b58-a754-3bc877853464 | -9.06592 | -61.37132 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e534567f-bacc-3145-95e7-c26322ab9f0f | -9.06982 | -61.39885 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 601f39cc-e180-38be-ae64-204a80d4203d | -9.07749 | -61.38836 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| be9bd932-47ec-3afa-a869-625dc39a2092 | -9.07864 | -61.13695 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1ab5dbf6-8b17-37e1-8674-8ef1c44467ab | -9.07879 | -61.39754 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 0925007f-4c64-308c-a658-6bd419ee51bd | -9.08008 | -61.40672 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e390c4d3-d616-3ee7-abe7-90b6c999d4b1 | -9.08767 | -61.13562 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8ecba450-a644-3e40-b5fc-a44bd20c2c41 | -9.08774 | -61.39621 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 6dc54c9a-bde5-39ed-9f51-9266b7cb3a0d | -9.08904 | -61.40539 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 27f9eb94-ecee-3976-80eb-ad14d42a57de | -9.0967 | -61.1343 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8602fecb-7d80-37bb-ba51-64a5f6309ecb | -9.1002 | -61.35101 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9b819a79-16fd-3462-9cf1-c95796824411 | -9.10152 | -61.36021 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 02c0fb07-3f1b-30c9-9063-b2785ca3261e | -9.11792 | -61.28262 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 191.5 |
| 0d9703da-57d7-329f-a12b-6b672d7607aa | -9.10283 | -61.36936 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b3f37d88-7e9f-3df2-bbd7-82a0c1bfc3f0 | -9.10761 | -61.27472 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3e2d3ae5-2866-382b-8ac2-2d5379ef85d1 | -9.10893 | -61.28394 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7b15a4f2-ef05-3a0a-a3f7-f3f37367b9a1 | -9.11923 | -61.29183 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d67b4d59-da2e-3b87-aab8-f06360384766 | -13.19185 | -51.72755 | 2024-10-10 01:54:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 22aef653-d77d-3746-9d8e-bfb5954614c1 | -13.1813 | -51.72279 | 2024-10-10 01:54:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 543ac56e-bf74-3f5b-a261-64943ce9d9eb | -12.58238 | -53.06819 | 2024-10-10 01:54:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ec4df184-1bd9-3fb3-838b-445b3b922827 | -12.58043 | -53.06297 | 2024-10-10 01:54:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 77279b13-c56a-35ef-8ef0-108c9a8326aa | -8.61951 | -54.61636 | 2024-10-10 01:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| a2e04c64-d16e-3c00-9489-55f434b13f1e | -8.61517 | -54.59021 | 2024-10-10 01:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| c9a7b231-493f-358a-893b-777e1937ef22 | -8.6133 | -54.59614 | 2024-10-10 01:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7add5fef-c386-3cc6-9551-6f9ce8de077b | -10.22244 | -54.31041 | 2024-10-10 01:54:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a5bf9237-99b3-3334-a90d-3e0abe7e840c | -11.35664 | -55.42589 | 2024-10-10 01:54:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8eb019d5-d29b-31d4-b3b4-19599579a114 | -11.17228 | -54.78345 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 1e6498a3-de34-3166-8cab-8be41941eb1d | -11.1346 | -54.00768 | 2024-10-10 01:54:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 95211adc-f13c-3376-ae46-61cb57f7fa6f | -13.42934 | -54.6793 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2ac2619d-2f28-3f9b-8c80-5ccb5518c84d | -12.67441 | -54.71589 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 33.0 |
| eb36360e-ffda-3239-b51f-d95cfb741052 | -12.67031 | -54.71091 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 37.8 |
| c26301f3-4a5e-363b-908c-9b91f5af63e4 | -12.60004 | -55.22517 | 2024-10-10 01:54:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 0a5a1f5e-9462-31bf-bbcb-0151cb60b3c0 | -12.4151 | -54.59324 | 2024-10-10 01:54:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| d167e778-3987-3b6d-984e-3657073217b0 | -12.41128 | -54.57064 | 2024-10-10 01:54:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 6744326c-0dfa-303a-acb3-f060530d4c3b | -7.95563 | -54.77665 | 2024-10-10 01:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 0e2a13eb-611f-3b68-9970-29100f255e7f | -9.58006 | -56.47489 | 2024-10-10 01:54:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d199b271-e14c-3c92-bbd3-537fc4ce2f47 | -10.6318 | -55.90508 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d159485c-5f5d-30be-8361-98f2e63cd194 | -10.62879 | -55.88621 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 54c84018-a61c-3895-b514-bedcc2926d0f | -10.48038 | -55.61637 | 2024-10-10 01:54:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 57afabf7-e67e-3bf9-9ec2-331b8982fda4 | -11.89704 | -56.21434 | 2024-10-10 01:54:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 47c4119d-73a4-36b1-887f-0c2860acc730 | -11.88883 | -56.20458 | 2024-10-10 01:54:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |


[Clique aqui para ver as próximas entradas](README32.md)
