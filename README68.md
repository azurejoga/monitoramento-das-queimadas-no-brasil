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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2a9e094-1001-3e03-b013-102c954caf41 | -12.66072 | -54.66694 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 559811db-8ff8-3575-ae4f-deddc5e33f8b | -10.96504 | -49.56799 | 2025-09-14 05:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c3ef4c8-c8ef-30c0-bbfe-52c49f565d3c | -11.27396 | -51.10776 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4adc8a36-ea3f-30ef-be20-b0fb1ea717d2 | -12.68867 | -54.70377 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 81996952-230f-31f7-aa64-9ba3c71385b8 | -12.68628 | -54.68029 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| c316af9e-53b2-301d-90c3-ea766809f06c | -12.91839 | -54.74305 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7e1e1e0f-4123-3f84-ad2c-bb1e2e495230 | -11.48501 | -50.77369 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c85c3ec0-fe1c-3ee2-a07d-a63b505d3fba | -10.97617 | -68.49865 | 2025-09-14 05:29:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a1bf84f-880d-3703-b5d7-70090e5d6ca4 | -12.93923 | -54.74545 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db336714-34cc-335e-ac0d-a05d4fcab2db | -14.61999 | -52.02188 | 2025-09-14 05:29:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7ac0c4a1-413f-3b0a-8915-b56069e81f12 | -12.94002 | -54.73909 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 81c4949a-7016-3b50-b9e3-a8d5a7ee1b50 | -12.67744 | -54.66601 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1a457ea9-a89a-3d2f-a0d2-e7ecbcaf4cb9 | -12.94043 | -54.73589 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d7ec4913-80cb-3c9b-9bf9-f054866d4687 | -15.20193 | -52.49635 | 2025-09-14 05:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f36f6c6-39f8-3f29-9187-2a96954d0c9a | -12.6558 | -54.66985 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83f159b2-b57b-365e-884f-11577665eafe | -12.70272 | -54.67568 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89e0210b-e932-33cc-9faa-6f5d9d84f27a | -12.69991 | -54.69838 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 26d19831-d35f-315a-8d5f-90637c5e374e | -12.69349 | -54.70751 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f7fa1e98-16c9-3b27-a430-f53c027846b0 | -12.6871 | -54.71654 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 67dfe386-8fc4-326d-ac1d-3ff7875e9f01 | -12.87037 | -62.09871 | 2025-09-14 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 773f980d-21d1-3817-aa96-72120aa6110a | -12.69271 | -54.71385 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b11eec40-b415-3afb-9df5-d05657fe2b0c | -11.28866 | -51.14767 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf634e29-5b10-3283-b674-83579b617848 | -12.70432 | -54.70539 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9d66fed-9573-3da1-b816-43c51e794523 | -12.68828 | -54.70697 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9e7672e2-66d1-3c53-a2f0-b36ce5171ea8 | -12.68305 | -54.66338 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b88a4c7-acbe-347c-b118-a000011ba7cc | -11.43832 | -50.47339 | 2025-09-14 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77143eb7-a0f8-3bad-99f2-443c2fddbe7e | -11.28748 | -51.10394 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 227e5ca0-23df-3700-8420-3c19d59de6bb | -12.68707 | -54.67379 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67883303-ce9b-33e1-887d-17c725cd91b0 | -12.92439 | -54.73724 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cad8e33d-050d-3a9e-a732-a958306a8347 | -12.70232 | -54.67891 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 7c200a41-011e-383a-a512-b472a3077a1a | -12.70111 | -54.68863 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| a69a00e4-7270-3ce4-8bf6-43506eaf577b | -12.9292 | -54.74108 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 593e13f5-6d0a-309d-b14f-33f883536741 | -12.69792 | -54.71439 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c20c8f7b-5d72-36f1-bc2d-4279ea8afaa4 | -10.23132 | -67.34544 | 2025-09-14 05:29:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef4b5ca3-78fc-3077-8eb1-2c8e47825285 | -12.66582 | -54.67451 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c9ffc99-966d-34ab-a7aa-400142e0ec95 | -12.68268 | -54.70959 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67264367-5827-3648-bf22-e585a0e06593 | -12.65541 | -54.67308 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 78e3cc02-b6cc-3884-a606-2c67bd16f0c2 | -12.70472 | -54.70218 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 08b8c10b-0b7d-3502-a9e5-8f8017a5dd87 | -12.68028 | -54.68605 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| c551a2b4-8951-35cc-ae3c-0567034356c8 | -11.28765 | -50.82337 | 2025-09-14 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f5f5f98d-ea67-3ae1-882c-a3d67bd8310a | -11.28202 | -51.10579 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 068f5b08-bbbf-30b6-afb9-836b128502bb | -12.6867 | -54.71976 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bf3ca0f3-1ba3-3b75-91d2-55d4a9af7b06 | -12.69832 | -54.7112 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 63431d4c-9db4-32a2-96fa-eff080f030d9 | -12.45786 | -57.78455 | 2025-09-14 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d42b356-f73d-3ce7-a53c-010886a4723d | -11.40505 | -55.35987 | 2025-09-14 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bc6e289-3750-3ee1-b5bd-044b5841185d | -12.45727 | -57.7855 | 2025-09-14 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e85e6b32-3e02-3589-b514-b9905cd216b0 | -11.28141 | -51.11112 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ad191b5-3502-320b-abcd-2fb9d4ab3b6a | -12.68189 | -54.71601 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 003f2926-3f32-3b30-81fd-dcfd814995eb | -12.9296 | -54.73786 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 00645c63-3b9e-3ced-a1b5-88e37ba7d845 | -12.67064 | -54.67836 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a0110b6-027a-3e44-9c57-3d386e807484 | -12.68228 | -54.7128 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ef9e99d-f071-3144-878c-e5a95552fc7e | -12.69428 | -54.70109 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cbc048db-c5ff-34a0-993c-3b241538da0b | -12.69388 | -54.70433 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 10f1827f-0e11-3dc5-aac5-95c3883becaf | -12.68749 | -54.71334 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8cec2e6-f739-3158-a81a-54ce582fa0aa | -12.66424 | -54.68753 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0c0dd202-38ff-32aa-b05a-4219336113d5 | -12.67988 | -54.68933 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6857e8ca-51aa-3e5d-a419-a805e117bf0c | -12.70874 | -54.71233 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d891b141-4b9a-31a0-a672-1734a990c4b8 | -11.44123 | -50.47912 | 2025-09-14 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f413861-b4f6-3bbb-9641-1892ef2ec918 | -12.6931 | -54.71067 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6efe6ab5-f592-3a56-b2a0-1b7efce78f70 | -14.1726 | -54.06169 | 2025-09-14 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 40b12fb3-ede7-3a0b-a334-bdfd72c37f29 | -12.6979 | -54.67182 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d294fac7-aa49-3f70-9f57-6d45ee34ef2f | -12.65659 | -54.66334 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23c31a42-4d63-34c0-bf19-071bc96b0aa3 | -12.93001 | -54.73462 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e0c91ab1-1420-3ea4-a39d-9c3772c2160d | -14.36509 | -52.93695 | 2025-09-14 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89a021c7-3c14-3c93-b484-494de5eb2df9 | -12.69469 | -54.69783 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0765ca7a-2200-3989-bfcd-9521276ce288 | -12.65593 | -54.66301 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ad758c5-b449-3c4b-acdd-26a612ddf1fa | -12.70234 | -54.72133 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4838c8f5-6239-3515-ae53-9e4f1eb627d3 | -12.69549 | -54.69131 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| df8155f7-a555-38e0-bb0c-d8e05d69a742 | -12.65469 | -54.67273 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39f8def3-4723-31e2-bc26-15f75a87985c | -12.66101 | -54.67057 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb6f6b55-b23f-3f23-bb8a-f0183a45355c | -12.67104 | -54.67513 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 595a1bdd-d67b-3d9a-87ca-3f82dd7b9dde | -12.70914 | -54.70914 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78fcd0f2-949d-3578-aa9e-72ccf9b3a7fe | -12.93962 | -54.74227 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7e96874c-5323-3ac8-9b28-f48fdf1d31fc | -12.66866 | -54.69468 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea83b06f-ae6e-3349-820f-50d08a77ea0f | -12.68508 | -54.69005 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8a5ff6e4-1b35-326d-ae62-00f1ee5ce4b7 | -11.4725 | -50.76642 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a3bad8d8-de91-3788-81d0-bbfcb2217a18 | -11.28932 | -51.14231 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcf23ade-f500-34a4-9d2e-4b86c392f967 | -12.87269 | -62.17438 | 2025-09-14 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1173fbc-083a-39f4-ae53-322ce5ba0e0f | -12.88221 | -62.1119 | 2025-09-14 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 702df12c-8020-386c-85a9-d1aeb45c245d | -12.45307 | -57.78487 | 2025-09-14 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 885a878d-0554-3a9e-9448-0f0c616f461c | -12.67346 | -54.69858 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ba563a2d-e2dd-31fd-acdc-48ae4a15d199 | -10.97206 | -49.56879 | 2025-09-14 05:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3804fd2f-8d26-32c7-b12b-e1a464394ea1 | -11.47842 | -50.77291 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d910d7e-1223-37d1-af56-aba3e5a4ff82 | -12.68787 | -54.66726 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e72ccfff-24dd-3e4d-9bd6-8a6e925ebb5d | -12.93521 | -54.7353 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ce478ee3-6e92-35ea-9000-26378b6756ad | -12.69871 | -54.70805 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 065a1131-6bd9-3cf5-bf6c-02d3201700c4 | -11.43162 | -50.47256 | 2025-09-14 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1041dee0-5425-3806-9407-951701d1cb3c | -12.68307 | -54.70638 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4315ce9a-a246-3041-aec5-d4d345e09b7b | -12.65947 | -54.67669 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e77e4e8-1259-31c7-bc33-79398181eda9 | -11.39642 | -50.45573 | 2025-09-14 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 67786f1a-029e-31fa-a081-e322f9f9039f | -12.45672 | -57.78941 | 2025-09-14 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3cff7ff-1c60-38e4-a67f-83cad9a8b091 | -12.67467 | -54.68872 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 457d89c0-d865-3e33-8e85-73677be39f4a | -12.68948 | -54.69725 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3c794c3e-e8b6-3520-8c0f-78f3fee88726 | -12.6959 | -54.68807 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 63319a6f-96c5-35dc-a998-9a157caa1c6c | -15.19622 | -52.4912 | 2025-09-14 05:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0357f7d9-79ba-3100-ba95-dccdda6db944 | -12.6963 | -54.68481 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 0a53c8a8-e057-38c7-b9be-668bd390cfdd | -12.9124 | -54.7487 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 19c679f7-0141-38c7-a82d-43c33f1da311 | -11.29055 | -51.14504 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a5742de-b4a2-3f87-a11e-0982dcdd9da6 | -15.14913 | -52.47067 | 2025-09-14 05:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d9162e7-e806-33a4-bebd-e1b1e7f7928c | -15.18315 | -52.31652 | 2025-09-14 05:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README69.md)
