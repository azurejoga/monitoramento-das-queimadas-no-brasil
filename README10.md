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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af611fc1-3cfe-3079-8a84-a7129437ff34 | -12.08536 | -54.57488 | 2025-05-15 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78a63cec-bcd3-3e05-a2ae-3f26289b41ba | -10.52422 | -59.38291 | 2025-05-15 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7cb94e3-b1e6-326b-abce-6e7776b55c0d | -13.66767 | -53.93357 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e10971cf-8b7b-338b-a2bc-54165404d0b2 | -13.16177 | -53.27648 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f966ddb0-7cb5-35e6-8ad5-d618f583208a | -11.6589 | -54.94908 | 2025-05-15 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3554dafa-3151-39a2-8dc2-676b802c7d65 | -13.26494 | -45.41732 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dcdb1f0f-dc97-328a-bc7e-60921cf8b99f | -13.07329 | -52.01671 | 2025-05-15 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95430fca-ed9a-3c1a-9098-2df96d38f5a3 | -13.28055 | -45.41938 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ccf91d9-0525-3819-960e-0035dda418ad | -12.14795 | -48.0104 | 2025-05-15 04:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95e0a0b5-333c-31b8-bff5-ef559e39386b | -11.66168 | -54.95325 | 2025-05-15 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd85b16c-47bb-3924-b34d-af9d24db3e93 | -11.56383 | -47.43489 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d45f820b-5815-37d4-9e04-16bde2355bb8 | -13.06982 | -52.01617 | 2025-05-15 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18d6e97c-ad72-3b09-bd77-fc76c38935eb | -13.04167 | -53.71971 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96ca0a30-0149-3bec-8783-b0b1daa43f6f | -13.27014 | -45.41808 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 145c56ff-e4e2-376d-b26d-266479a62ee1 | -13.27053 | -45.4149 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c9e8a99-b1bf-334e-bd20-9908e0ecae36 | -11.69602 | -48.81737 | 2025-05-15 04:53:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ae48742-f47d-3c24-90d9-05b6fef0749e | -12.87001 | -55.06055 | 2025-05-15 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 553c6f87-4425-31ac-b44a-b307495911d8 | -11.01093 | -50.75835 | 2025-05-15 04:53:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d34bf15a-5cdf-3a5b-9294-698d4138cee7 | -11.42286 | -54.33555 | 2025-05-15 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 627cc53a-8058-3513-a176-92a140eb6ab4 | -11.8714 | -56.41662 | 2025-05-15 04:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22b3c904-f9e9-3198-8c1c-a3fff524f317 | -12.72451 | -54.97002 | 2025-05-15 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d89f6ea7-a6e7-324e-9bec-5050dd9c1673 | -13.26975 | -45.42125 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0a76279-a96d-3e0a-852b-b1a78b235c76 | -11.78159 | -47.35056 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c781cf4a-e34f-30c6-9e42-0800acefec8f | -11.87491 | -56.41723 | 2025-05-15 04:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 440eb116-14bd-3d3d-ae06-ec701b7410cb | -11.65022 | -48.10974 | 2025-05-15 04:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0d284f34-e077-3579-bc8e-f6835599caed | -11.78606 | -47.35113 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea4c0120-3c73-35e8-b157-35789ff5a487 | -12.08479 | -54.57844 | 2025-05-15 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6aa1e722-a951-36ea-9157-370e67c061e4 | -11.91654 | -54.40535 | 2025-05-15 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 957d6e37-e0e3-3d1f-8973-eadc66d36d61 | -12.14741 | -48.01445 | 2025-05-15 04:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cfd0f64-70af-30c8-9530-8a094ab1325f | -13.52887 | -52.79087 | 2025-05-15 04:53:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 485901ee-6b3a-3157-beb1-79e1cfb3a9f5 | -11.40278 | -48.69936 | 2025-05-15 04:53:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98b3080a-0184-3ce8-940c-ffe9e1ff1fc7 | -13.26936 | -45.4244 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e13a559f-db48-3889-ab5a-5ceecfb70aa6 | -12.68511 | -58.13756 | 2025-05-15 04:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3da482a9-5e1a-3d8e-802b-f1016329fd39 | -13.287 | -45.45248 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7deb5271-5ad9-3547-9e31-683c31c80044 | -10.66689 | -57.63506 | 2025-05-15 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6b58620-ae63-3a9a-be5a-8f1c1d21c4c8 | -10.68458 | -57.60014 | 2025-05-15 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7babbc4a-c269-344c-82dc-ef663b212ad0 | -11.93776 | -61.9922 | 2025-05-15 04:53:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 160c504d-b857-3229-8f94-b7919f493c8b | -11.56325 | -47.43932 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e863ec2a-5c8b-3298-a994-362742bc4e63 | -13.28379 | -45.43589 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1267e88-0fa5-3c17-8f44-b88dbfdcdd6f | -12.09921 | -49.30521 | 2025-05-15 04:53:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c01778b-cbbf-3d58-bba3-f19836d8279c | -13.03833 | -53.71917 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e591b9b0-83f0-3a05-a4dd-9e08f86d0754 | -12.12131 | -54.66086 | 2025-05-15 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a994f345-deaa-3d82-8a8f-d8ce0812c72e | -11.65311 | -58.26222 | 2025-05-15 04:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aa992dc1-734e-3b3f-8264-9c369abd8b02 | -11.94267 | -61.99309 | 2025-05-15 04:53:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77540575-e56f-34bd-9f34-dbe62018bf7a | -13.27858 | -45.4353 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f42aaa06-79a9-3f12-b0af-9a82d7c86a2b | -13.04611 | -53.71312 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f806f856-d772-381a-8fbd-5fd6d5539735 | -13.27417 | -45.42826 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78469eaa-c665-3952-8227-83ed2c6b4a72 | -12.18555 | -48.68152 | 2025-05-15 04:53:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b1d6dfd-bb62-3982-93f4-dc1d95001dc7 | -11.78835 | -47.35368 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f94f31f3-d1d7-3f0f-b4c1-f8e0d9d87337 | -11.56767 | -47.43998 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e78d9a5b-a1e2-3b5e-8721-55d7e46e5198 | -11.68295 | -44.84778 | 2025-05-15 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7207e426-0469-30f7-8428-609f5479f7d4 | -11.39873 | -48.69869 | 2025-05-15 04:53:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03ac02dd-55c0-3ad2-9653-49603ba5751a | -12.10561 | -44.7478 | 2025-05-15 04:53:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65642080-1a16-39bc-87c1-921dffe9d2e7 | -13.27456 | -45.42511 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bccd9979-c4cc-3917-a7e4-9ff682ccbaf9 | -13.04501 | -53.72025 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c2e20b44-5d3d-3807-9578-ab7e787a25bc | -11.79192 | -47.37453 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec0408ce-2e34-3684-9771-3508cec3b1c0 | -11.78992 | -47.35616 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6160ffc5-3521-3dee-9ca7-211e83044282 | -10.68537 | -57.59557 | 2025-05-15 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3562ba9b-86bd-37d7-a0e6-1dcc84d764eb | -11.7947 | -49.32195 | 2025-05-15 04:53:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb818a6d-a0fb-32df-8fc8-3238e7ed70ec | -12.76245 | -48.92666 | 2025-05-15 04:53:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3f9b309-a3ff-39a0-b7bc-be3446633e24 | -13.22712 | -56.56304 | 2025-05-15 04:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 462718aa-e77f-35b4-8a7f-70a13ab4f046 | -11.59702 | -58.96012 | 2025-05-15 04:53:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 268e05f7-6345-3357-81c6-fb82ab22c07a | -11.89027 | -56.41175 | 2025-05-15 04:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6a51518-9e79-3263-8914-a6a6f29bd281 | -13.59726 | -47.37848 | 2025-05-15 04:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d4ce197-6cac-3fb7-9773-a8f9094edf39 | -12.29138 | -52.4721 | 2025-05-15 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 058bf170-ca93-383c-8787-36816b041364 | -11.00673 | -50.76197 | 2025-05-15 04:53:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa3d69a2-963d-3d7b-831c-cfebee1be0f4 | -11.42343 | -54.332 | 2025-05-15 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f050f4e0-b527-37c3-8c15-e0ceba3b9ac8 | -12.49513 | -54.39805 | 2025-05-15 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eff6fc59-111f-3584-bad5-002eaa63b5c5 | -13.66489 | -53.92945 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 507d39e1-1d61-35c7-b06b-716a05210a2a | -11.24397 | -49.49261 | 2025-05-15 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e88a4d36-7058-36d8-82ab-e0424ad555a8 | -13.68689 | -47.76572 | 2025-05-15 04:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01edeada-7c28-3526-b2df-1a836f3ae9cd | -12.87163 | -55.0719 | 2025-05-15 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84eac506-6e82-37e0-afb8-9b4ac1c5813a | -11.56822 | -47.4423 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5b0d8f33-764d-3e85-a744-46bb89db8e31 | -12.19844 | -55.2172 | 2025-05-15 04:53:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ccba2a3-d9cf-323a-8687-d4c53f6b56f7 | -11.55305 | -47.61829 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 320aaee5-4626-3a7c-bd70-96d67e4514ac | -13.59211 | -47.38222 | 2025-05-15 04:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c3cb50d-9ba0-3ec7-90d5-ea60de9628ce | -11.16671 | -48.67301 | 2025-05-15 04:53:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b22a591-b44a-318b-99ba-4607fe5d7e41 | -12.87279 | -55.0647 | 2025-05-15 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87ad6ef1-66c5-382a-9c60-13770d8cfeb1 | -11.05229 | -56.10979 | 2025-05-15 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee3adf3c-e77c-3007-ac14-3912beaf57a2 | -11.62935 | -48.47195 | 2025-05-15 04:53:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 786fa118-0236-3258-bf2c-43c44adf254f | -11.91321 | -54.4048 | 2025-05-15 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adb0b486-5943-3f51-9d5e-2aa338453bce | -11.56441 | -47.43726 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 46ff9068-4ee6-36fe-963a-25b7e854fd6b | -11.55798 | -47.61472 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d979059c-3e4c-3e7b-9e00-2a94240f497e | -10.69598 | -59.11828 | 2025-05-15 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2340d058-6803-3152-880d-4586655f4cb2 | -11.78388 | -47.3531 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c1d0a9e-efdf-3ac9-bbfa-b2256e05b962 | -11.55742 | -47.61892 | 2025-05-15 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c80826a2-e7b5-34b1-a8d2-bb29a876c1c4 | -13.07516 | -47.81191 | 2025-05-15 04:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8235b201-5e06-32b6-8612-d37f645a7920 | -9.78869 | -56.1313 | 2025-05-15 04:53:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e6e7fdb-487f-3d71-812d-ec611df2672a | -13.66822 | -53.92999 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 545e2e86-8e48-3fb6-9348-b58095fbda82 | -11.89443 | -56.40839 | 2025-05-15 04:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57e849d4-c78e-3d77-af4c-778cb5399d5e | -13.16232 | -53.27287 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 933af99b-d004-3994-a261-620c8b4f1578 | -13.2882 | -45.44288 | 2025-05-15 04:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dee2d765-74a5-31ed-9131-097c3d7986a7 | -12.12074 | -54.66442 | 2025-05-15 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d89e5579-115a-33bf-af29-dabbf29edc7e | -11.4262 | -54.33609 | 2025-05-15 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| deddcbc2-17c2-3926-b403-4d99251be56e | -13.04222 | -53.71614 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f87e668-a87d-3fe1-8167-473787527add | -10.43465 | -52.12101 | 2025-05-15 04:53:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dc97dfa-e2cf-3f76-9255-753e1b3a70b1 | -10.66608 | -57.63973 | 2025-05-15 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fac6d73-80e4-3486-9f5a-07edbbf9776d | -11.30515 | -54.01542 | 2025-05-15 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a93cf389-fa64-3767-8f06-5d2c07cff23e | -11.78719 | -47.36258 | 2025-05-15 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6895fa18-aea0-3eaf-b76a-eec3496ee387 | -11.15455 | -48.67121 | 2025-05-15 04:53:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README11.md)
