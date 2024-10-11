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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d103853-479c-3d7d-9764-108bde468544 | -9.94207 | -58.11241 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51222585-70e4-3f9e-9862-98932e9f2a8e | -9.93867 | -58.10075 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f7e5c68-3786-3eaa-b45c-73fac087be3a | -9.93793 | -58.10619 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e736320b-4f0c-3f44-b95e-b65c6046f3a2 | -9.9147 | -58.13061 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 886cb8b8-3fc9-3643-975a-86ba003a26ef | -9.90188 | -57.06474 | 2024-10-11 05:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6d4491a-4278-33ae-926f-69815e58bcea | -9.89675 | -57.06426 | 2024-10-11 05:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 29ccfe30-9c5a-375c-adc0-4843e7bdfd85 | -9.89632 | -57.06741 | 2024-10-11 05:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d62762bc-da89-3ec8-834a-5f20dd95f13e | -9.8962 | -57.0674 | 2024-10-11 05:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25fc5454-69cf-3ed8-8fba-eb9762373490 | -9.79571 | -57.38459 | 2024-10-11 05:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee38ba66-dcf9-3633-83c9-488c2a433dc8 | -9.66054 | -56.95743 | 2024-10-11 05:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50f36c95-ffe2-380e-baa3-45139afa6787 | -9.65613 | -56.95017 | 2024-10-11 05:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce798491-8998-318d-9c23-a9edee32b974 | -9.6557 | -56.95345 | 2024-10-11 05:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fde95d53-e5dc-3e5d-bda2-28484bcb1bae | -9.65485 | -56.95987 | 2024-10-11 05:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1087465-7d23-3eaf-8c27-a5200de9f53a | -9.64972 | -56.70987 | 2024-10-11 05:42:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a997925e-8756-304f-93ba-3de7ea073ba0 | -9.64436 | -56.70912 | 2024-10-11 05:42:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73cae5c0-cd1f-3077-a53c-e406c2136c9e | -11.03255 | -57.2118 | 2024-10-11 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88e2b83b-0391-3136-86d8-dc2903708b1d | -11.03212 | -57.21511 | 2024-10-11 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67771f12-0f88-344d-9f14-823ea13c180f | -11.03109 | -57.21113 | 2024-10-11 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16a6ed86-4446-3cca-bd02-60d18f254b6a | -11.03068 | -57.21446 | 2024-10-11 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8433faa-7b49-3282-bd0a-257a11459c05 | -11.03028 | -57.21774 | 2024-10-11 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e59e0709-c9b3-32ae-8d14-d678888f0dda | -9.3057 | -59.28704 | 2024-10-11 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92109e12-1a00-3b94-a7ba-2981efe5eddf | -9.30509 | -59.29145 | 2024-10-11 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 884c7d09-3010-3536-923d-41665ceec0ab | -8.11558 | -58.03773 | 2024-10-11 05:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98b91554-0740-30b2-b092-f209daf880e6 | -8.11488 | -58.04275 | 2024-10-11 05:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b1d7855-2b37-3171-9503-40bef434625f | -8.1101 | -58.04203 | 2024-10-11 05:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7c268eb-841a-3be1-82db-3f568247d2d3 | -9.88848 | -59.50787 | 2024-10-11 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2844fdb9-e9c2-34a9-9cff-51ee4242f2e4 | -9.77374 | -59.26682 | 2024-10-11 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 76295db2-282f-365f-99aa-9adc4cdd628d | -9.77309 | -59.27146 | 2024-10-11 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e16cc8b-5c91-3e2e-a38e-404991698314 | -9.51753 | -59.50175 | 2024-10-11 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad7dd0e4-891b-3f59-924d-b08cd3dadd8a | -11.72197 | -59.28283 | 2024-10-11 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2053f4c5-af73-3d47-b2f1-1f242cfbb9ac | -11.72132 | -59.28765 | 2024-10-11 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b605962-1c7c-3aee-b5e9-a676d8be9ef4 | -11.72067 | -59.2924 | 2024-10-11 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8b1e9a8-73cd-3022-b71d-81633bb16d2b | -11.72052 | -59.28429 | 2024-10-11 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8424e54-78fa-330c-abab-96d7a3469604 | -11.7199 | -59.2891 | 2024-10-11 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06a834de-d41f-33b3-8690-bcd931e0c409 | -11.7193 | -59.29384 | 2024-10-11 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 430d7faa-1edf-3d7c-a6af-429bae10481b | -11.71799 | -59.27732 | 2024-10-11 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eb67a34-316f-304e-8c9e-cb7c21b2e0f6 | -11.71734 | -59.28216 | 2024-10-11 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2bbb4fa-931d-3002-beae-c2d348833488 | -11.71669 | -59.28698 | 2024-10-11 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8d88e70-6cbf-3025-b8ba-f6ab51cd7460 | -11.71604 | -59.29175 | 2024-10-11 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e75b3490-ac5e-3883-8638-643d6aa9fc13 | -11.71271 | -59.28149 | 2024-10-11 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2847c7f-5afd-3841-aafd-f2414c093f2b | -7.1405 | -59.30449 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5aa079c-29e8-33ac-9b5f-cf202e0a2f96 | -7.13435 | -59.37887 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49389530-1e77-3225-b86a-3d0e31c3f9ff | -7.10534 | -59.29564 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8916d319-c4b9-33c2-86c0-78de50b689e8 | -7.10474 | -59.29976 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cafd0d9-5885-32db-8ff2-a9310ba59229 | -7.10101 | -59.29501 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b04a567e-b560-3463-a8b9-e6bec3994664 | -7.10041 | -59.29913 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd4ec49a-66d8-3c5c-bfa4-c106bb8dde37 | -7.09669 | -59.29438 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e99963ad-ef63-3f1d-b368-202437e0bacd | -7.09288 | -59.41028 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 961672d9-8ca9-36ac-8b23-f6d5382424a5 | -7.08918 | -59.40562 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92cb79ab-ab06-3194-b28e-44530d244b24 | -7.08859 | -59.40965 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 481a87b7-88ab-3fa3-ac8e-d8a660800cb6 | -7.08489 | -59.40499 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 517a9096-fa86-3ecd-a4aa-6ea9e8290e48 | -7.08429 | -59.40903 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffd9705a-5df4-3a4b-9bb3-c87025145c4e | -7.08417 | -59.25889 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27d68484-dba3-3894-b315-4202a445d4d0 | -7.08356 | -59.26305 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69a1091b-c085-3a94-a8fa-9f8e78b3a5f6 | -7.08059 | -59.40438 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6bffd99-e5b4-3fd2-bfff-65899cf978ab | -7.08 | -59.40841 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c409f2b0-1526-3e37-8aa5-c1a8e864bce0 | -7.07923 | -59.26244 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f2d23ac-aa00-3b85-b609-8ff32e6fd497 | -7.07863 | -59.26658 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7458843-6a6f-3c7b-9daf-79f063f532c4 | -7.0763 | -59.40375 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e45a72e1-e33d-3e86-a173-980d994ee761 | -7.07571 | -59.40778 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe17a9cd-4f10-3e29-bf77-d8b6f6276b6f | -7.07513 | -59.41179 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f99ff9f5-ad33-3230-8df6-074ec8a04e18 | -7.07429 | -59.26598 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2189a526-11de-32e2-8e36-61b99295726c | -7.0737 | -59.27011 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c298039-0796-3a4d-b4df-ced23a034efa | -7.07201 | -59.4031 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ef7d1f2-b668-3f6a-b3a9-5336da663963 | -7.07143 | -59.40713 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2a0874c-48c6-31a7-8ced-c01cbbb3c4db | -7.07084 | -59.41114 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 714fcbb8-00cf-321f-90f8-43da23acd579 | -7.06996 | -59.26536 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93ae14c0-6c41-3f57-bac8-82a5430ccc02 | -7.06714 | -59.4065 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fed3e743-0c36-35a8-b07c-7e4a28fc44ce | -7.05253 | -59.4166 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e19a1f07-3916-303c-8b14-0c1859a7e7a0 | -7.05093 | -59.36692 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02ea551f-7426-3e26-8a83-4aaa14834a29 | -7.04882 | -59.41195 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f325c49e-9c49-3345-8a98-b7441e1f5132 | -7.04824 | -59.41598 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b617a16-3f63-3817-a66b-61659d0ddce5 | -7.04766 | -59.42001 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ea9f644-74ce-3b50-a43e-7682130403ff | -7.04663 | -59.36631 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac9e605b-f837-3f47-af32-7963655daca2 | -7.04454 | -59.41133 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a23ab97-b1d2-34ad-afd0-d0f0043a2c1a | -7.04396 | -59.41535 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2e5707d-86db-39b8-9f93-86c91acc166a | -7.0429 | -59.36167 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d50aa79-1185-3167-9ad7-6e89074b10c7 | -7.04232 | -59.36568 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d85b3ef5-b26e-36d3-9efd-1839236edc0b | -7.04175 | -59.36968 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f44bcfb7-d60b-3b1a-9d02-bda64fa9e6d9 | -7.04025 | -59.41068 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 897190d7-eabc-308b-a485-94b1dc208005 | -7.03745 | -59.36904 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf19c427-cf6f-35f5-bdde-663abea82e0e | -7.03308 | -59.43013 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4247dae4-fcb5-3030-8353-9c534baf0357 | -7.03251 | -59.43414 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb5096aa-c224-3de1-904d-b85ee75bbbc7 | -7.02938 | -59.42547 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4f4370b-b985-36f3-83c5-328547b44b28 | -7.02509 | -59.42485 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39c7cc4f-4095-30aa-bf97-8784cf02f212 | -7.02452 | -59.42888 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d54a6cf-fa44-3633-ae1e-6ea8e280d557 | -6.97169 | -59.47155 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adaa0369-2a7b-3e50-8435-1cfd0d38f394 | -6.97111 | -59.47549 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9c8bb64-0160-3a89-9a18-600f288ea2da | -6.96743 | -59.47089 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd9115b6-a7ad-3dc1-acb6-ad6a385d4a36 | -6.96685 | -59.47484 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0ea88a2-7501-370f-9e1a-786f07926b03 | -6.96259 | -59.47418 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8f954d8-acae-3355-87d2-ee3b9090c5bc | -7.35064 | -59.93412 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b916b04-674a-392f-9b92-42a35bb5b408 | -6.92053 | -59.78895 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81f35647-b4c5-3636-aea7-cc2dee975a7a | -6.91691 | -59.7846 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 997cb6e8-8631-3da0-86d5-fd5aa17c5fe2 | -6.8927 | -59.80442 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95b14c77-36bc-3fb8-97b1-087de9272003 | -6.91634 | -59.78844 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34e2f6f2-e204-3739-a66a-e18e3bb155ff | -6.89742 | -59.80124 | 2024-10-11 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c45ff5ac-e88c-3f41-b5e2-7efd15f357d0 | -9.22037 | -59.77634 | 2024-10-11 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbb536ad-aa6b-3dcc-b595-f778f074c66f | -9.2198 | -59.78045 | 2024-10-11 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a865fd8-0648-31b5-bfa7-98f32d810030 | -9.21605 | -59.77572 | 2024-10-11 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README111.md)
