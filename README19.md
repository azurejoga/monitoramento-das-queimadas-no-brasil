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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 403335d0-d2fa-3dc4-b26c-e57b8b7edf20 | -4.20005 | -40.67892 | 2024-11-15 04:44:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c8c9e981-b210-3e9b-8839-8b134b4f37bb | -2.56014 | -46.00803 | 2024-11-15 04:44:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53e0a04d-54af-3525-a02b-038335ea68ca | -3.17423 | -54.47186 | 2024-11-15 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42ff768a-627f-3aa1-89a3-c30fd91b5926 | -3.23502 | -54.16313 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47905087-d322-3889-ba7e-da8cea9c0bab | -4.19441 | -40.67847 | 2024-11-15 04:44:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7bcaece7-f476-3ec4-82ab-c8a7ad593bf6 | -2.67794 | -46.82668 | 2024-11-15 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d5b666a-9aae-3ed4-b38f-2e7506dd2a47 | -1.38269 | -52.07843 | 2024-11-15 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4aa215c1-556c-338d-bf52-013fd67817aa | -1.21455 | -53.56514 | 2024-11-15 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e58598fe-df80-352c-8202-77911586d806 | -2.32832 | -46.86817 | 2024-11-15 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 09f84739-1195-3504-83fa-611c50ff9872 | -6.04892 | -44.04005 | 2024-11-15 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cc00e19-184d-36a5-a757-467cfb4e4496 | -4.51351 | -44.07592 | 2024-11-15 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ef873ac-36a4-345c-b209-38920ccb4225 | -3.42714 | -53.97612 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ac8de64-aa03-3194-9d09-d7df9dbeae9e | -2.71443 | -44.77353 | 2024-11-15 04:44:00 | NPP-375D | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 175e21a1-e19c-32ba-a57c-90de6afc67f4 | -1.86929 | -54.68676 | 2024-11-15 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c084aeb-9e12-3b93-b4b6-6f746ee8c150 | -3.7942 | -43.91441 | 2024-11-15 04:44:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f771ee2-d47b-3c5d-a5ca-4b53db7c0d3e | -3.09752 | -45.97221 | 2024-11-15 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 047e320d-c960-3926-9e02-c76dd0a0e560 | -1.6865 | -52.68987 | 2024-11-15 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5abeb41b-abc5-3ea4-beaf-94b35d512492 | -3.26047 | -54.53263 | 2024-11-15 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fac0e9e4-074b-34bf-9c1b-ece8c02f6466 | -3.71953 | -41.69012 | 2024-11-15 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 33e50383-0ca7-3c26-8498-3e2791bd2a6d | -1.8529 | -47.82568 | 2024-11-15 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f148d5eb-941b-31c9-a46b-b73aa5d72f18 | -2.65937 | -46.18779 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42fdd7cd-51b4-30d3-951a-68249a847c68 | -2.23685 | -46.83721 | 2024-11-15 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5dca13f-3a1b-3b06-8725-f512d9dce7d5 | -2.66246 | -46.19287 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 237e75d6-7d05-3be3-88fb-61849731e7c3 | -3.18954 | -53.9884 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe6ecb0a-a409-3ddb-b99b-4417ca121a64 | -2.65401 | -46.17071 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c6f6a04-d63a-3439-b53b-36827d0aa0fa | -1.60967 | -52.4906 | 2024-11-15 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e7a741e-4dab-3ad7-a880-f7a41e2b92f8 | -2.65188 | -46.18435 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb39e67a-ddc4-3219-b586-55e00b30973c | -2.65941 | -46.1855 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8887802d-fba0-32dc-8b96-027e174d1e11 | -2.43486 | -46.28791 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b27123a0-2c41-39b9-a483-2d0e994d8487 | -2.98584 | -45.87061 | 2024-11-15 04:44:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbf560ff-3fc8-3475-a8c6-f5f9211dd0d5 | -1.38417 | -51.55696 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9ee393d-ed10-334f-96d8-20dcbbcd6962 | -3.6289 | -52.31142 | 2024-11-15 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bb19340-b64b-310b-a6c3-279ab6db8b51 | -2.14699 | -46.40515 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5804da59-7f07-36b0-bacc-d5269499a794 | -4.1051 | -38.74144 | 2024-11-15 04:44:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb7ebb85-349f-3875-bc66-67cd2340831f | -2.3885 | -54.6333 | 2024-11-15 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e99e236b-8bd9-3d55-9816-552384367c1a | -3.64801 | -52.27988 | 2024-11-15 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de7314e2-f774-38a9-ac84-62030f77a8bc | -3.1502 | -53.23905 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ac237909-805c-360a-98e3-af0aa734e5b9 | -3.58883 | -54.53274 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2501285-5f94-3b36-9a68-b3c7cd0ba8fa | -3.27831 | -53.01991 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 283b4463-1eb3-3830-b4ac-123874bc3f50 | -2.46165 | -53.97552 | 2024-11-15 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a30ed7d-db14-3af9-8a52-5d0b420f4fb0 | -2.62266 | -46.82418 | 2024-11-15 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bacc95e-c3f9-399e-819e-1ab59e914665 | -3.23574 | -54.15858 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51d3a23a-ef5b-37e5-9140-7bed9fade684 | -2.65492 | -46.19176 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 739ae532-db49-397d-84f0-4c3707a77f85 | -3.31436 | -52.86206 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d20b48e8-f831-3452-9d3a-c2421a939103 | -2.65801 | -46.19684 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec6f876f-33b3-31e9-90a0-09a5c82a0cb0 | -3.70992 | -53.7523 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 000c9128-6e22-3564-897d-1c280364fd6b | -3.55097 | -54.57089 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 398595c9-31ef-338c-82ce-2f7bc282a0d1 | -3.54358 | -54.32706 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77058614-bd27-327a-8a93-9e86a14a3fbb | -1.09424 | -53.17539 | 2024-11-15 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e7f3425-c157-35fb-a08e-5049c30e1fc6 | -2.65424 | -46.1963 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b2779fd-c8ca-3668-84e8-d4354d71a216 | -3.2478 | -45.92998 | 2024-11-15 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d76b9933-d991-3e13-a745-1cb00c4038b7 | -2.64875 | -57.10525 | 2024-11-15 04:44:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5940adde-2001-3989-a748-5f954ea59244 | -1.68878 | -52.69849 | 2024-11-15 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db2ac199-2ff2-33c3-9750-0614007d702b | -2.43704 | -46.28154 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 983ca48f-9982-3dfa-b6f6-6ee435ba7871 | -3.62949 | -52.30767 | 2024-11-15 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 126d06fd-0334-3ce6-9d43-9f80d0afcd72 | -3.06567 | -53.28086 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5cd87956-6ba6-3db5-8def-83b59aee2015 | -3.61677 | -52.32101 | 2024-11-15 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0519eb75-5709-339e-a9d6-5cb837363f0a | -2.6556 | -46.18721 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffa8c817-7fb9-3611-aada-2d61c4aa186d | -2.49629 | -56.49337 | 2024-11-15 04:44:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9512972-661a-3d2b-b737-ecafae492af9 | -1.09295 | -54.17582 | 2024-11-15 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91794c55-614b-3f7f-b5bd-7f955f96d45a | -1.8039 | -54.6604 | 2024-11-15 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 508cf64d-2a86-3e37-86bd-702548623fdb | -3.42185 | -53.96144 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6067ff24-dad0-3886-8f32-6d2624ec9f80 | -2.65707 | -46.17583 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eedc823a-56de-3dff-ab4f-d7d6a0d068a3 | -2.63915 | -46.19172 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8c44be6-e7ae-35b8-898d-7c6e557180c3 | -2.589 | -47.48037 | 2024-11-15 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 97474f6e-d8f0-34f7-85f1-43640bcd1090 | -3.24864 | -53.67132 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e04dc6e4-5d84-3f08-b520-4cddfdec49d3 | -2.32766 | -46.87233 | 2024-11-15 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef242b13-0fa8-360f-adbe-9e8170aaf3d8 | -2.66247 | -46.19059 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 642c00f6-f07d-33e5-b532-972062cdefa6 | -2.64789 | -46.16049 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5c50e1a-5144-3282-880c-ccdecab488fc | -1.56401 | -51.85334 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65130a99-2c52-3efb-91de-9cefa7ba36e7 | -2.63609 | -46.18664 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37d818b1-2f22-3da3-a9ba-e326f39a5ae6 | -1.38075 | -51.55641 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a6d68e4-0e3b-3e20-a4d4-674059a228d8 | -2.09473 | -46.32559 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9e350b6-df10-33bc-8f3a-86561649b210 | -5.53401 | -44.8346 | 2024-11-15 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb6c29b0-ff65-3437-ace4-1ed6ce4c2659 | -2.66389 | -46.18153 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ffab075-5c21-3421-bce7-11b25fadd3ae | -1.08988 | -53.17907 | 2024-11-15 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 960e748e-c95b-36e8-9ebf-5fd8a7538254 | -2.90774 | -46.85826 | 2024-11-15 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8ed4833-e54b-33e1-abd8-42e36e4b6e6a | -1.85635 | -47.82622 | 2024-11-15 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e56780fb-c38f-3524-9ee0-bdd67ea38396 | -1.68586 | -52.6939 | 2024-11-15 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc6701e2-542e-3241-8a6e-3794307a6de0 | -2.65564 | -46.18493 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59a88059-0cfc-3b7e-8247-2b5366ded323 | -3.06471 | -53.282 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68eab6b5-87c5-3304-a09a-eedacf76d898 | -2.43557 | -46.28345 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aa0b18c4-1156-35e3-8173-5b3463c099e2 | -1.98867 | -46.36434 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4a9fe9b-26f6-31ce-93f0-6a372791cdcc | -2.46069 | -53.93314 | 2024-11-15 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8060d177-5348-3b7d-97d8-0c7f4056e863 | -1.57458 | -53.80041 | 2024-11-15 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 97ff8505-0087-3465-aee4-7d4f0c49b9c2 | -3.23952 | -54.15922 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0436a42-1b6a-3c8a-9a28-b8e559034ee6 | -3.64516 | -52.2756 | 2024-11-15 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 393d0f54-dd13-3105-9567-40f941e89811 | -1.79991 | -54.65977 | 2024-11-15 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5c44ac0-5e0f-3915-9578-c8a8dca37318 | -2.33193 | -46.86873 | 2024-11-15 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e393b10f-a999-3b35-9b57-ac32dba1e951 | -1.09056 | -53.17478 | 2024-11-15 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3e9159a-403d-3b53-95d8-b91a27da6d82 | -2.65869 | -46.19232 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3e4034f-09e5-3a1c-b5b1-aecba95a4cb3 | -2.78796 | -45.95739 | 2024-11-15 04:44:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6258aa0-0c75-3701-884c-b62fde9b6987 | -3.27539 | -53.01534 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 620b4ac1-e4ad-36bc-9c8d-1d7e99bc9046 | -1.51724 | -51.55433 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b06d8d6-26ca-342b-ac46-efe033866c6d | -2.65045 | -46.19343 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c271ee1-834e-3a41-ab71-3e9eb67c0a71 | -3.09826 | -45.96746 | 2024-11-15 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e51d4044-2819-32d2-92f6-84eec893e891 | -3.71435 | -41.68937 | 2024-11-15 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 47ab3187-cb6e-32ae-932e-cdb1cf48950c | -3.42859 | -53.96712 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd12d02c-3ef2-3d62-b019-92d30cc08ae8 | -3.44944 | -53.46699 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 974dc5a2-c93e-3836-b078-6abcfa71cf0e | -2.68158 | -46.82729 | 2024-11-15 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README20.md)
