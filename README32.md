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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 274c83af-b1e1-3b77-a10a-a1b6cbe98d83 | -18.03096 | -45.57404 | 2025-08-27 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 274b8fdd-1f39-3c40-afdf-f5c95145814c | -20.52244 | -42.27225 | 2025-08-27 04:06:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 079c2777-26d3-3626-864e-f6e2899d4d4b | -17.78674 | -44.49747 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f1d0620-4ed0-36a1-86b3-1dbfb647ce89 | -20.06401 | -42.6092 | 2025-08-27 04:06:00 | NPP-375D | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f5bb1a40-55d6-3c65-964f-e9c554ed81da | -16.37806 | -48.80912 | 2025-08-27 04:06:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e3ebc68-9fdb-3447-ae18-e406abd44dfe | -17.3146 | -46.59563 | 2025-08-27 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33adecd0-d832-3cb5-8524-c87c82409e95 | -19.16193 | -41.50588 | 2025-08-27 04:06:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7bea51d3-a010-3946-afcd-0cc9a377d922 | -17.97227 | -48.05675 | 2025-08-27 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c71ad4d-de55-3833-9728-ef211dec9124 | -16.74297 | -47.59492 | 2025-08-27 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 009ce964-e736-3efa-a62d-795d4a898d13 | -19.12407 | -46.44641 | 2025-08-27 04:06:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a618389c-3e5e-3070-bcfd-f0161adc3ae7 | -18.03453 | -45.57476 | 2025-08-27 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c121c2d-fe39-387e-9869-d1032b73b022 | -18.28659 | -40.99849 | 2025-08-27 04:06:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| aa25c8cc-1960-3663-9c5c-269bb55a8703 | -18.05724 | -45.1657 | 2025-08-27 04:06:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1021dc3c-c0a1-31c6-b9ec-f08b59da6e6c | -20.05792 | -42.60434 | 2025-08-27 04:06:00 | NPP-375D | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ed3f81b8-83cc-3223-9bb4-02a628acc8c4 | -16.38159 | -48.81459 | 2025-08-27 04:06:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d4b2ebe2-adc3-39f4-96ac-95c0b787b141 | -16.95339 | -49.21669 | 2025-08-27 04:06:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 394e13ee-5099-3ce4-ac1f-6dde82cb76e9 | -19.84499 | -46.09655 | 2025-08-27 04:06:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2402b86a-b11d-32ae-a03a-614c08ca2654 | -17.36618 | -49.17945 | 2025-08-27 04:06:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dab33650-11af-371f-a5a8-440cc98117c8 | -18.14886 | -44.43946 | 2025-08-27 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdee2526-8b7a-3648-bb06-ca40674b4874 | -18.14002 | -44.44997 | 2025-08-27 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a9e70b7-e0a2-33ee-a7d6-737fed730296 | -20.50251 | -42.22281 | 2025-08-27 04:06:00 | NPP-375D | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4701a588-8e86-31b7-baaf-f417c2f71ce5 | -18.15567 | -44.44092 | 2025-08-27 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13948b69-b6bf-3968-bf44-634c4605c1be | -17.973 | -48.05285 | 2025-08-27 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7fc95b37-e2ab-3068-ad7f-aa9be8cf5a57 | -19.77275 | -41.95956 | 2025-08-27 04:06:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 749f2abd-087d-387f-915e-bd7e6d63896a | -15.65725 | -52.7319 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6022aa36-68d7-322c-ba3e-0d8570bf6d3e | -20.64957 | -42.44996 | 2025-08-27 04:06:00 | NPP-375D | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6a5235fa-598f-3635-8bce-86654c8e4876 | -20.03461 | -42.11853 | 2025-08-27 04:06:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d4dcf5f6-2edb-34b1-a39d-d9915f935ac2 | -20.02277 | -45.55565 | 2025-08-27 04:06:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b8bb724-5e30-3bfc-8da4-e8a22c5307d3 | -16.74228 | -47.59862 | 2025-08-27 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31a565a9-ce2d-3c26-8b59-0583d0db21a6 | -18.25122 | -45.36221 | 2025-08-27 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0badd4a-ab14-3ecf-bc32-3faa9ee4e2a8 | -16.38603 | -48.81542 | 2025-08-27 04:06:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a14ff659-1b47-371e-a671-5b16eb7e3394 | -16.83805 | -43.85218 | 2025-08-27 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eeefdfe9-ccfd-391b-9e6f-502faf394640 | -20.05459 | -42.60375 | 2025-08-27 04:06:00 | NPP-375D | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 093feeb2-6cc0-36c1-bdea-ed42726a2107 | -17.31612 | -46.59853 | 2025-08-27 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f3c2ca8-2078-3401-90f2-e3f976a69a43 | -15.61702 | -52.72269 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bf498da-22b3-31ba-8fa5-c2ad0ecde7c7 | -17.80562 | -44.5042 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e3d646b-019f-3f52-b905-9d96a1a6bee2 | -20.535 | -43.96702 | 2025-08-27 04:06:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7fd23383-c287-3c32-b84f-84d652b7502d | -19.17909 | -44.51551 | 2025-08-27 04:06:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e670f4f8-27c3-3dfb-ad4b-b6f3190d478a | -19.52403 | -45.32207 | 2025-08-27 04:06:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f336a70-9b19-3728-b598-7c8df70ff7ed | -15.6188 | -52.71426 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b838b5bb-1996-3ea8-8c12-31fd374ef392 | -17.77573 | -44.47835 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33ee132e-525f-374f-8cd3-11e51994a8f1 | -17.97709 | -48.05376 | 2025-08-27 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 210aee2a-c477-36c5-bb78-e8dbdc1bf8f3 | -20.35482 | -42.25863 | 2025-08-27 04:06:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 43903a28-5927-3624-982f-525fa4f22096 | -19.08001 | -48.14224 | 2025-08-27 04:06:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b217145f-2fd6-3914-8f43-3d35981b31c8 | -19.07723 | -44.32745 | 2025-08-27 04:06:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ffdfd8b-9ca5-3e5d-8838-a1ef14285ae9 | -18.28715 | -40.9947 | 2025-08-27 04:06:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ac79c81f-a067-3464-881b-3a3bb6b0c8d2 | -17.77506 | -44.48234 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec23c93a-f86e-386e-86d6-cdcb38ae936e | -20.02698 | -45.55222 | 2025-08-27 04:06:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| badff17e-d6e7-3f3f-abac-335003aadb4b | -16.70484 | -50.41152 | 2025-08-27 04:06:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb505b91-e29b-38e6-b685-7c10e3ddcd4a | -19.64469 | -43.98522 | 2025-08-27 04:06:00 | NPP-375D | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| daac2296-dea8-3cdb-b7de-25bd54bb1cf6 | -17.55506 | -46.60939 | 2025-08-27 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67416e85-9525-352d-a719-a80010f0fbe4 | -19.53027 | -40.16279 | 2025-08-27 04:06:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e1f69e4d-6b69-32dd-a662-bc9c3660444b | -17.84299 | -47.74215 | 2025-08-27 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afc05817-d070-3e3a-ad0a-e7385fec687b | -17.55418 | -46.61421 | 2025-08-27 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c953236-332f-3825-94ba-25516e946857 | -18.15701 | -44.43297 | 2025-08-27 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02a4e202-264f-3e84-8ee9-2f58f0b444cb | -18.75964 | -40.12627 | 2025-08-27 04:06:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3cddc769-2055-32ed-b6f9-391c593f1795 | -16.77883 | -47.56033 | 2025-08-27 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84189927-2c5c-3cdc-b754-ae7fca40bb3e | -16.7829 | -47.56107 | 2025-08-27 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7080cb15-eef1-3aab-8923-dc05e727980a | -20.04726 | -46.09692 | 2025-08-27 04:06:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6925d60-dab8-3b0b-9d32-00ec8761c170 | -18.1951 | -45.55896 | 2025-08-27 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a6c0e8d-2906-3cd6-801e-2692fc589386 | -20.02627 | -45.55632 | 2025-08-27 04:06:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3332d44a-a2e7-3629-8ae7-eda3fd632905 | -20.48826 | -42.96997 | 2025-08-27 04:06:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 03786ac4-736c-36b5-b1b6-d22349a8dd1c | -19.28236 | -43.74077 | 2025-08-27 04:06:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2477b3fb-5da2-3214-b0ce-669905aaa721 | -15.62099 | -52.73245 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cfa8956-5ea1-33aa-8f21-f64ea5ae1938 | -19.12489 | -46.44186 | 2025-08-27 04:06:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5d061ff-fa09-3ef0-9e8f-7fd5a9635709 | -19.4071 | -46.15978 | 2025-08-27 04:06:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7775933-abc2-3551-92fa-8ad4b0a970a7 | -18.05511 | -45.1781 | 2025-08-27 04:06:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02150736-52bd-37ba-be42-aa757af68208 | -19.24878 | -42.05206 | 2025-08-27 04:06:00 | NPP-375D | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0b6f0337-e045-3d14-8f6d-a07375dc6888 | -17.40835 | -44.77348 | 2025-08-27 04:06:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d997f8d-c2b8-3c1a-be92-6b8c5bc6b7b0 | -16.38248 | -48.80999 | 2025-08-27 04:06:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9991be05-4425-35cd-a513-1c543377e1d7 | -18.27431 | -42.12758 | 2025-08-27 04:06:00 | NPP-375D | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a62de9b-ee79-3203-97fc-f276675d7df8 | -20.06459 | -42.6055 | 2025-08-27 04:06:00 | NPP-375D | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f359be9d-7d0e-3fba-b7e2-6701f8848acb | -17.23562 | -43.23653 | 2025-08-27 04:06:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9ffaf8f-d8f8-32cd-abc7-e2b3e7b1431f | -16.70974 | -50.41247 | 2025-08-27 04:06:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7819d6b-1e62-3dec-914f-6218de543757 | -20.00992 | -42.13683 | 2025-08-27 04:06:00 | NPP-375D | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| d4d045d4-d93c-3634-9944-a3f54d7e7db7 | -16.91945 | -49.4444 | 2025-08-27 04:06:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d042d691-6169-3848-b666-a83941770bcb | -18.19793 | -45.56385 | 2025-08-27 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c602730b-89e9-3cbe-91c3-cdbf6737bb2c | -19.69807 | -42.11113 | 2025-08-27 04:06:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c8bec08c-1393-3d86-b065-156b216cd0ac | -17.32802 | -41.68674 | 2025-08-27 04:06:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| bcd655d0-0956-39c0-88ab-dcaf5072dcb5 | -18.72426 | -43.81817 | 2025-08-27 04:06:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 002c2424-acbb-3e21-b7aa-0a07ee812a39 | -18.05795 | -45.16153 | 2025-08-27 04:06:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ace4f27-551d-3b09-8123-5599e4d077d0 | -16.37929 | -48.81119 | 2025-08-27 04:06:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b0f9e0f-e0d8-38df-b8c5-a2fab015e93d | -17.17525 | -48.68573 | 2025-08-27 04:06:00 | NPP-375D | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17c29893-c3a6-3d22-bdac-d17100b40c9c | -15.66213 | -52.73738 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91be3811-93bf-3115-b3be-b147ff9c4ed0 | -20.51966 | -42.26798 | 2025-08-27 04:06:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6e864622-3c23-3c76-904b-425ebebeec5d | -19.52983 | -43.63582 | 2025-08-27 04:06:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be063c53-fd0d-313b-ae8f-31506fa6fff5 | -17.54864 | -46.62312 | 2025-08-27 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12a18785-11b8-343b-b6a8-8a61b940c6ff | -16.70647 | -50.413 | 2025-08-27 04:06:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 991c30ef-837f-371d-ab13-10a4cbbfa998 | -19.46434 | -44.18584 | 2025-08-27 04:06:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0b94f79-7fb7-356b-b807-4d46325ebcd0 | -20.98283 | -40.95608 | 2025-08-27 04:06:00 | NPP-375D | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3781ff50-2b66-3ddd-8577-5faf55e3f664 | -20.00657 | -42.13624 | 2025-08-27 04:06:00 | NPP-375D | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| d281627a-65a5-3092-a25d-007f1ebb2bb6 | -19.07528 | -48.14509 | 2025-08-27 04:06:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3012fd60-6c03-39bf-98e8-b35f6b93b0e5 | -17.79354 | -44.47775 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa79a455-d64f-375a-81c5-00cab96a6f26 | -20.98631 | -40.95664 | 2025-08-27 04:06:00 | NPP-375D | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3559a262-21fd-307a-81e1-1d03fd9e8e38 | -16.77951 | -47.55663 | 2025-08-27 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee6b3c6e-6887-3d01-9f9c-fa0ecc563a19 | -18.1665 | -42.63992 | 2025-08-27 04:06:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 87bc6872-139a-37b2-873b-f34644e74bf3 | -15.61793 | -52.7184 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 667380af-bd4e-3883-b85b-db11863e96e6 | -18.21936 | -44.5247 | 2025-08-27 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dde253e4-5b90-3991-bfa5-d6bc374c3c8e | -17.8043 | -44.51198 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0f96e4b-b67f-32af-91f8-a94aad4aaedd | -17.55243 | -46.62385 | 2025-08-27 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README33.md)
