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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4340351-43bb-3a92-9185-528dc13fe74f | -21.947 | -47.5578 | 2025-09-12 00:50:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 8f4fd65b-b391-3364-9aa4-007771d9b80a | -12.8649 | -62.1268 | 2025-09-12 00:50:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 8fa29ef8-6620-3429-98c2-c58290514eeb | 2.5246 | -61.0387 | 2025-09-12 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 25.8 |
| e6909f43-22ae-338c-b50d-ff8f098c5826 | -22.6404 | -53.0946 | 2025-09-12 00:50:00 | GOES-19 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 79.2 |
| c9d0b7e1-046d-3162-b33f-3d69cbf6a8ad | -11.9907 | -51.1405 | 2025-09-12 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 8d11a77f-a33d-3787-b935-c8dc2a152557 | -20.4052 | -49.1278 | 2025-09-12 00:50:00 | GOES-19 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| 3ee7e2f6-d5c5-3335-8e44-d5b67b4971d0 | -9.5137 | -54.6292 | 2025-09-12 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 27037bf1-c9f3-3b25-8ba2-c056aa4f72d8 | -12.8837 | -62.1449 | 2025-09-12 00:50:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 827c4cd6-97e7-3cb0-8b96-848df48dcf11 | -13.3238 | -44.0945 | 2025-09-12 00:50:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 92b3be1c-bf31-3f70-a0a9-73c8fbb01468 | -12.8647 | -62.1461 | 2025-09-12 00:50:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 58b3138c-57f7-33b7-a72e-a4d1f0360b4e | -8.8901 | -49.9236 | 2025-09-12 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 176d02c0-da53-3710-b97f-d85b6dcc20d8 | -11.702 | -46.5153 | 2025-09-12 00:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| f24b68ea-3ade-343c-b8e6-daf7745f08a5 | -6.309 | -42.2311 | 2025-09-12 00:50:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 205.9 |
| b4fb4114-c814-3a53-a445-b0c0f8ba873f | -9.2287 | -59.3823 | 2025-09-12 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| f30c1ad6-e6f1-3624-bb22-cda102f52b90 | 2.5064 | -61.0201 | 2025-09-12 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 1b792185-638f-3e5b-97eb-33bd6bac2202 | -16.5102 | -55.125 | 2025-09-12 00:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 125.3 |
| f7a0242b-cb66-35b1-bd56-75b257b10377 | -12.9292 | -54.7538 | 2025-09-12 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| d2009f15-7ce1-3a53-a52d-498d6ce5d2b2 | -21.9679 | -47.5525 | 2025-09-12 00:50:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 190.2 |
| cd08189c-530d-3331-8aba-d67255e94579 | -23.1146 | -47.4915 | 2025-09-12 00:50:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.1 |
| e96a3b33-85d5-3483-a22f-56da494d279a | -6.2902 | -42.2327 | 2025-09-12 00:50:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| a54b4e9b-3748-352a-974a-e1abb9cfc382 | -12.8651 | -62.1074 | 2025-09-12 00:50:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 9da6b8f2-0d5a-3f41-a288-dabc8916a3d9 | -21.9686 | -47.5287 | 2025-09-12 00:50:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 852a67e6-9766-37ad-af7d-9024c1ab5a6a | -11.702 | -46.5153 | 2025-09-12 01:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| beced74d-5177-34af-a775-a69ed94eabd5 | -12.9101 | -54.7558 | 2025-09-12 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f27b3afe-bb0e-3b20-b6e9-066c8bfc5e5d | -9.4578 | -40.3392 | 2025-09-12 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 217.8 |
| 26820c04-f699-3b6b-b4a4-30caa4e2ab56 | -6.2902 | -42.2327 | 2025-09-12 01:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 1b0d2ae6-cd18-3ce1-9202-fe9e6c837237 | -21.9478 | -47.534 | 2025-09-12 01:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 47666101-62a0-30d1-a0a4-6d4400f0bad5 | -16.5102 | -55.125 | 2025-09-12 01:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 95530111-6703-3923-96ac-bbb78f4247f9 | -15.1053 | -48.0209 | 2025-09-12 01:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| f7ade4fa-aa9b-3295-8914-cfcfe8df55c3 | -16.6133 | -49.7939 | 2025-09-12 01:00:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 39.5 |
| fec7f9d1-e45b-33e1-b9a9-7c2b30e6f562 | -13.3238 | -44.0945 | 2025-09-12 01:00:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 47cf01c8-248a-3d3c-88e3-ebea33c7503c | -9.5137 | -54.6292 | 2025-09-12 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5378092f-4fe1-318b-bf93-ceeae274b47a | -21.6291 | -53.9923 | 2025-09-12 01:00:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 95b93b6c-7016-3d80-ba93-df5e6ddb2db4 | -9.4769 | -40.3365 | 2025-09-12 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 155.4 |
| 90080f0c-429c-37cd-9099-8bde45c1776c | -12.8651 | -62.1074 | 2025-09-12 01:00:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 5dc5ac01-5085-3121-a72a-36497d617d76 | -22.6404 | -53.0946 | 2025-09-12 01:00:00 | GOES-19 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| 748769b3-6ee3-3f1e-b8a5-40a509ff48d3 | -15.5819 | -54.7637 | 2025-09-12 01:00:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 45b291d3-ddf4-37ef-be92-a523adfd012d | -9.057 | -47.0355 | 2025-09-12 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e23a174d-0b34-37c8-ad0f-90e0db9583fe | -11.9717 | -51.1427 | 2025-09-12 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 390b30ad-95de-386f-a68e-18aecee91f7f | -11.9907 | -51.1405 | 2025-09-12 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 958454e4-a427-359e-8c03-88144901cede | 2.5247 | -61.0198 | 2025-09-12 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 26.0 |
| df3ad47d-a21a-338b-b2b9-fa51de43b8d9 | -6.3092 | -42.2072 | 2025-09-12 01:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 120.1 |
| 77e307b0-e787-3840-995f-753122075e33 | -13.3243 | -44.0708 | 2025-09-12 01:00:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4ddd3195-f4f0-3861-97af-28deccdf67f4 | -6.309 | -42.2311 | 2025-09-12 01:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 257.9 |
| 12369680-c38e-3da2-821c-676774a247c1 | -16.5099 | -55.1459 | 2025-09-12 01:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 1b6b22c7-b22e-37e9-89a8-e54d9e71b477 | -8.8899 | -49.945 | 2025-09-12 01:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 43f23085-a324-30bc-b620-71903967c6bf | -11.6821 | -46.5632 | 2025-09-12 01:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 96dd8145-c049-3af3-bff5-06aae4514ee3 | 2.5064 | -61.0201 | 2025-09-12 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b632b87d-6f8f-32e8-b568-d5083a1568e4 | -12.9292 | -54.7538 | 2025-09-12 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 157.0 |
| e83d3101-8898-3e2b-bdf7-f840e185a48b | -9.4574 | -40.3641 | 2025-09-12 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 189.7 |
| db730d7f-d8c7-36d3-a5b3-1f3a59e2b7da | -10.1216 | -47.9154 | 2025-09-12 01:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| a5a8dc87-29f3-3e70-bb50-6beb5bda0e55 | -11.7012 | -46.5605 | 2025-09-12 01:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| ff60ec4f-25c3-30a9-bdba-8e21cb9e8e6e | -12.8647 | -62.1461 | 2025-09-12 01:00:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8e732874-5bbe-3a74-809b-ab3b89f32ac5 | -11.7016 | -46.5379 | 2025-09-12 01:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 339b4fd1-496a-3ee0-abe4-8b5121a9ee9a | 2.5246 | -61.0387 | 2025-09-12 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 23.9 |
| ffd275bb-cffa-3c39-90cf-b9e897230fe8 | -12.8649 | -62.1268 | 2025-09-12 01:00:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| ebe7f938-2515-3159-b5f2-bbe0cc25334f | -21.9686 | -47.5287 | 2025-09-12 01:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 104.9 |
| f4d030ab-ab74-38b5-9f27-7d48fbf035a0 | -21.947 | -47.5578 | 2025-09-12 01:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 5f228971-39f2-3d25-b87f-ae3215ee85d9 | 2.5064 | -61.039 | 2025-09-12 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 60ac72d4-8788-3c0b-b278-8c315a848f51 | -12.9289 | -54.7744 | 2025-09-12 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 8d6aea2f-f3b8-3ac7-be24-7ff3d14f3911 | -9.0313 | -46.1219 | 2025-09-12 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 074415cf-50a0-3c65-83a9-0662b1c3c81b | -18.9152 | -46.6593 | 2025-09-12 01:00:00 | GOES-19 | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 44159571-b3c2-34c2-8fc0-5a5a79f11ac7 | -16.3127 | -50.0868 | 2025-09-12 01:00:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 5e487117-f21a-3d74-ba99-2e6873901660 | -11.8757 | -58.8221 | 2025-09-12 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| fd652e8d-bfe4-3516-a648-c3c672b80d75 | -11.6825 | -46.5406 | 2025-09-12 01:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 281321ff-09ef-370a-921e-2fa6d2f9808c | -9.4765 | -40.3613 | 2025-09-12 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 135.6 |
| 14dea906-add7-3bf9-bf87-770e2c10b9f5 | -12.846 | -62.128 | 2025-09-12 01:00:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e26e1933-6172-3c37-8162-b6daca2a38cf | -21.9679 | -47.5525 | 2025-09-12 01:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 46c8d42f-81c8-3076-8847-b704025dc969 | -23.1146 | -47.4915 | 2025-09-12 01:00:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.2 |
| dec4e799-a35d-3fc7-bd70-d7a386637ff0 | -8.8901 | -49.9236 | 2025-09-12 01:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ada1250b-783b-3349-a5b4-bd4e57f6d618 | -9.0316 | -46.0993 | 2025-09-12 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 6cdb107b-9d2b-33e8-8c86-8f43b65fee6b | -12.8647 | -62.1461 | 2025-09-12 01:10:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 443dcc3d-1a45-3866-9507-788ef77f0d05 | -12.9101 | -54.7558 | 2025-09-12 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| c940580d-5685-3359-8fdb-a2693271696e | -9.0124 | -46.1239 | 2025-09-12 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 295.1 |
| 2d50f727-4042-30b3-9ebf-0ec731e99e02 | -16.5936 | -49.7972 | 2025-09-12 01:10:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 725c9d8d-ef87-30b6-aa8e-866fec6c9a00 | -21.9686 | -47.5287 | 2025-09-12 01:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 91b2d4e7-7949-37c8-8a44-f699bb56408e | -9.0313 | -46.1219 | 2025-09-12 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 330.3 |
| e3ffe20e-e844-3c49-accf-e9fc5e12992b | -8.8899 | -49.945 | 2025-09-12 01:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 39839e57-1e5c-3d37-82c3-4baeda13f7a0 | -11.8757 | -58.8221 | 2025-09-12 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8c635ccf-54fa-3702-9482-c3e4d01df916 | -11.0198 | -51.3733 | 2025-09-12 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| fe81fb1b-11fd-33cd-ba9f-2ac7351466ea | -12.9289 | -54.7744 | 2025-09-12 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b6a8443c-e997-3548-a787-c1f43fc84d3a | -8.8901 | -49.9236 | 2025-09-12 01:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f833c0c2-d366-37cd-babf-d973b372f41f | -23.1139 | -47.5156 | 2025-09-12 01:10:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.2 |
| d2452488-2bd7-3d32-9b3a-e053978e76dc | -21.947 | -47.5578 | 2025-09-12 01:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 274.5 |
| c8e32268-e70d-35b5-944f-f681df444749 | -19.1605 | -48.0207 | 2025-09-12 01:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 43.5 |
| f0dfdd48-acce-34d0-aeca-29c2c08cd89f | -21.9679 | -47.5525 | 2025-09-12 01:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 308.8 |
| 17de8225-815a-3f08-812c-5ae3e77718b9 | -11.0201 | -51.3521 | 2025-09-12 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 189.1 |
| d1c9a260-19cf-3da8-833b-07346d081c7e | -21.9478 | -47.534 | 2025-09-12 01:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 112.8 |
| b983a414-746c-3fb6-beaf-ebfb8655ff99 | -6.309 | -42.2311 | 2025-09-12 01:10:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 211.0 |
| d522bda6-f663-3e65-aa19-f23376b3b2ac | -11.0391 | -51.3502 | 2025-09-12 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 85f250fe-3df2-3b47-8e4b-a1ab1dd38579 | -11.6825 | -46.5406 | 2025-09-12 01:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 9aa61ce1-e1d1-3dba-a654-8ea4510c7a6a | 2.5064 | -61.0201 | 2025-09-12 01:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 962ea846-6b2b-3bd9-ab6b-ef78465a30bf | -19.1611 | -47.9976 | 2025-09-12 01:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 46.9 |
| f5ddb203-e730-342a-b0fe-55d1281ccc1d | 2.5064 | -61.039 | 2025-09-12 01:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 36.0 |
| d0b80f82-bad2-3418-9209-9cff53989318 | -11.9907 | -51.1405 | 2025-09-12 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 210d9e2f-6aba-3d5b-b80e-a768da32e7c0 | -12.9292 | -54.7538 | 2025-09-12 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 207.6 |
| d96d75dc-e296-3d3c-ac77-05269b99ffe5 | -6.3092 | -42.2072 | 2025-09-12 01:10:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| eeaea78a-a901-3d06-979a-586b3bc819bb | -9.0127 | -46.1014 | 2025-09-12 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 2d7c4e9c-b9e1-38b9-9877-36cccb737a04 | -9.5137 | -54.6292 | 2025-09-12 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| af0236f0-7faf-35e2-bcb4-a0dd6f94a227 | -12.846 | -62.128 | 2025-09-12 01:10:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |


[Clique aqui para ver as próximas entradas](README10.md)
