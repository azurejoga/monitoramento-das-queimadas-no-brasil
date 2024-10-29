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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09b43d3e-012e-32ae-87de-bf153fc0f7a2 | -1.29123 | -55.71939 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a713f46-024d-3746-b2ca-d6e1a10bbd73 | -1.29011 | -55.72647 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28605566-851c-3e55-bc05-91bbb6a48235 | -1.28955 | -55.75183 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 399334df-6322-30be-ae3a-d31bbdbc98ec | -1.2817 | -55.77971 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94b10e4f-1ce0-330f-bf0b-74692c8768e2 | -1.27666 | -55.74614 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed7ea26a-d457-300c-aabf-9a437b393a6d | -1.26142 | -55.90804 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2387190-c2f0-3cfb-bee6-30cf59228d6f | -1.26085 | -55.91162 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54273700-9fa6-3af8-834a-68c5d65b7970 | -1.26028 | -55.91521 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c6a4373-c582-3474-b178-77d67259d176 | -1.2586 | -55.90394 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17169d38-ea3b-3a7a-9a31-28a87ba4ba65 | -1.25804 | -55.90752 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5b48986-eddc-3853-bd2c-d798d89e5cb2 | -1.2569 | -55.91468 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72f95b3f-b601-3f14-81e4-dfadb3331bbf | -1.25634 | -55.91827 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04cb7746-720c-36b2-a204-b361b99602dc | -1.23273 | -55.89255 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01699068-9077-38c6-b32f-24d965d99d6c | -1.21517 | -55.86443 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ce83e019-ca83-3387-bff5-4e320e6015ce | -1.21179 | -55.86391 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 983602e1-0cb5-3698-9c74-85ad32b8a057 | -1.21013 | -55.89661 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91e85d62-19ba-3f60-b87f-2800944f5a87 | -1.20957 | -55.90017 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7213be50-ce84-3244-906e-56432973cbfd | -1.20901 | -55.90373 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f8c5bd9a-0fca-3831-9e8c-61459816c3a4 | -1.20842 | -55.86334 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5d66376-49b9-32c0-b00b-5f813129ef9a | -1.20674 | -55.87405 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e38122b9-7557-38a5-ade5-44e8b56ff829 | -1.20564 | -55.90316 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ecc33e38-9262-3e58-88c4-0f813508dae9 | -1.20337 | -55.8735 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc2dd83e-e25a-3343-845f-85d6d069a211 | -1.19833 | -55.92774 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2572cd5-1558-3379-9eb2-5ce95a908b61 | -1.19777 | -55.93131 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22c55d9a-3f98-38af-a709-1f21f7488e66 | -3.64743 | -55.50026 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f500e52-8f4a-3e41-8ecf-f3819c6b2be9 | -3.6318 | -55.44818 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52b5ed41-0329-3b3c-b81f-4ad66f9e5f72 | -3.62407 | -55.45405 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a08c08c-d5e8-3040-b4e3-aec24d88e041 | -3.62075 | -55.45354 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c40cb742-ffb1-33d1-9bac-d3d61f6eee6e | -2.46636 | -55.62461 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d8b30d4-a1bd-3535-b3ca-1b765022e58e | -2.38646 | -55.27765 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 463957bc-bd76-3274-8d48-f8a77331b932 | -2.38314 | -55.27713 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9eb7d7fb-69d6-312a-b413-62b0db9d4029 | -2.36645 | -56.51551 | 2024-10-29 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b084ba3-246d-384e-8bfc-7ce3d5b69e60 | -2.2793 | -56.42755 | 2024-10-29 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28e2f876-22c1-309d-a674-cfc1c3b726b7 | -2.27873 | -56.43119 | 2024-10-29 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e0a0e57-a40d-3a7b-9f14-c1e4fe1d42a1 | -2.25215 | -55.48806 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1632043a-fef9-3e79-834b-45459741ff84 | -4.85814 | -55.88931 | 2024-10-29 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74ef8030-1c56-353f-8b94-aa1124658135 | -4.85759 | -55.89278 | 2024-10-29 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee02ae8d-a936-384d-afcd-943458b5000b | -4.85482 | -55.88879 | 2024-10-29 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6aeef71-c684-3969-b694-c32edee86170 | -4.85427 | -55.89226 | 2024-10-29 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44519e0e-5059-3a25-af63-4b9ede0180a0 | -4.73451 | -56.05229 | 2024-10-29 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc1ef620-67be-34eb-9fcc-47b116c55611 | -4.72458 | -56.13675 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ecb7d87-77bb-3e38-82b1-27ef108cfacd | -4.72124 | -56.13621 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f0723f6-0f0a-37e2-8de0-9ca6672c6d02 | -4.65568 | -55.9077 | 2024-10-29 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d63e120-bfed-3e90-8595-7cf986d8930f | -4.65235 | -55.90718 | 2024-10-29 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 828e19aa-9c81-34cc-b5eb-3a9e136433a5 | -4.61401 | -55.86907 | 2024-10-29 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47acb443-ff3c-3ba4-b575-2f129527a475 | -4.61013 | -55.87202 | 2024-10-29 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3686d338-130a-313c-8ccd-bffc50604049 | -4.6068 | -55.87151 | 2024-10-29 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b33d9f5-7344-331b-8296-6b43927d1dbc | -4.57789 | -55.84559 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 155327e1-03fb-350a-909b-8427d2ef4f72 | -4.53332 | -56.12833 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89e6a078-bc69-3109-aec9-482f77cd7f30 | -4.50424 | -55.5811 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0592f5fd-9534-3871-ac9b-8e089bf74c0c | -4.32266 | -55.72337 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 935bca1a-2fdd-32ad-865a-e643bb2bfb2c | -4.3057 | -56.38131 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e86fe2a-fa23-334a-b882-f0be9829a53a | -4.30514 | -56.38486 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16d2a053-6c5e-3b3f-bff6-54bbd5e23f96 | -4.30234 | -56.38078 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d1d82ff-5f33-3ddf-8d89-d826778eb4dd | -4.24348 | -55.96428 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3706622-906a-3be2-bf90-c49c31a2efbc | -4.2001 | -55.64015 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a584d54c-6ef8-3d0e-b16a-41bd54494d13 | -4.17472 | -55.73577 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30aeb30e-3c0a-3647-b2c0-3f0e123ab1c0 | -4.13148 | -56.2236 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4132a281-dd20-3925-b861-2b8849c0b32e | -4.12868 | -56.21957 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0768991-85e9-39fd-bd02-e614385a7a48 | -4.12812 | -56.22308 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f26b5d4-ba58-3e6d-9be7-d3a4d6a44fad | -4.11529 | -56.19576 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 104c724c-4ca0-30c8-8778-b831e3c260cf | -4.10492 | -55.49416 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6787d588-e792-3102-a234-36384575849a | -4.10159 | -55.49364 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 690598be-a2f1-3edc-ac17-8532c11beb30 | -4.10105 | -55.4971 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a6f7fea-3bcb-355c-ba89-b1b106eaf10f | -4.1005 | -55.50056 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ad0de4f-1b4c-363c-a3d5-8c0c62a8ed97 | -4.08549 | -56.31788 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 960cda1a-9eb1-3b4c-b314-1411dce12af5 | -4.08024 | -56.25568 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79fcff63-0470-3a2f-aa0f-cb944216b06d | -4.05618 | -56.23382 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7e9a0ce-4898-3139-a330-a3f8547eb102 | -3.98928 | -55.43667 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c46b56c-4385-33a8-a8a9-9287dc27511a | -3.78244 | -55.58516 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a56ac558-2ea2-367e-964c-81e1b4a59394 | -3.72335 | -55.49089 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1418c7d-01f3-3bc7-bb88-b89b966d632f | -3.69032 | -55.96006 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 773b9dfd-9735-3fcc-ac80-f4f3a72d0199 | -2.09901 | -56.85912 | 2024-10-29 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4eeb4243-9b45-362b-ae84-afa827c53994 | -2.09072 | -56.68886 | 2024-10-29 05:01:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7128b64b-291c-3650-a61f-ed138695ec65 | -2.09012 | -56.6926 | 2024-10-29 05:01:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 953554b7-5a9c-3cf7-94dc-fd4aee1ed0da | -2.06045 | -56.64274 | 2024-10-29 05:01:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d877345-afe2-3276-90f3-57a7d2fac4a3 | -2.05853 | -56.86817 | 2024-10-29 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7ef0d7b-50d2-3d8f-8e5c-7e76c676b37f | -2.05567 | -56.86382 | 2024-10-29 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f890b60b-96cc-3c2f-aa71-e0ed35f96bc3 | -2.05506 | -56.86762 | 2024-10-29 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1120a270-d7a6-3c08-b244-4f7e6d4899d0 | -2.05221 | -56.86326 | 2024-10-29 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13270162-75ae-3bec-b1f2-9d8ce17faac4 | -2.05161 | -56.86704 | 2024-10-29 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85c7c86a-daf1-3295-b3de-6d94471b383c | -2.05132 | -56.63359 | 2024-10-29 05:01:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a7265c1-7f8f-3651-86f3-4967f0eb62c5 | -3.55894 | -57.68368 | 2024-10-29 05:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93ed5594-4c4a-3375-b917-2c3ce7fe94d5 | -3.55831 | -57.68762 | 2024-10-29 05:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f29f5475-f8fc-3f35-b76f-8a483b7c29f5 | -3.55477 | -57.68706 | 2024-10-29 05:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab6b14c4-936e-37ac-af8d-377ec7939267 | -3.49437 | -57.54557 | 2024-10-29 05:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7160593e-ac10-3dc2-987a-e51ebe917d43 | -2.89987 | -57.67475 | 2024-10-29 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 984872be-d25d-3f62-9772-14ad99984afc | -2.89923 | -57.67875 | 2024-10-29 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5839fde-9267-32aa-8729-a5f2b33e4f18 | -2.56025 | -58.11272 | 2024-10-29 05:01:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3441a176-9be9-3070-a474-848f89684a83 | -2.5566 | -58.11214 | 2024-10-29 05:01:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec654c68-ccb4-36cb-a11a-43f31c967b5d | -2.55593 | -58.11637 | 2024-10-29 05:01:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62bc3333-c06a-389b-8435-41cf927e827c | -2.34558 | -57.1501 | 2024-10-29 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7494242b-57ed-374e-9de2-442822d3d094 | -2.34497 | -57.15395 | 2024-10-29 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bebadc77-6611-3f90-8094-8713576c0f47 | -2.34208 | -57.14957 | 2024-10-29 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9575c33-b2da-3471-b3f3-1667de9b8487 | -2.34147 | -57.15343 | 2024-10-29 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccfc1d79-4781-3e3b-8a9e-4d8e80914758 | -2.34085 | -57.15727 | 2024-10-29 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b00451be-46a9-391e-ac60-e062b3bd2cba | -2.33797 | -57.15289 | 2024-10-29 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84994dc0-d64f-3222-8689-8dd7304c6722 | -2.324 | -57.15065 | 2024-10-29 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d29bcd5f-11af-33c2-98d9-eecea7a6a01c | -2.3205 | -57.15011 | 2024-10-29 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06e8b2f3-3b27-3986-987d-159d0f33b5ae | -3.0289 | -56.93944 | 2024-10-29 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README90.md)
