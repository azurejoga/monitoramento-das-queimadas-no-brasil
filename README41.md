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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dd27b8b-1b10-3c26-a438-cd67439e7933 | -14.50168 | -59.33276 | 2026-08-17 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 66605140-dc82-3858-8d3a-812a8cf1981a | -18.81039 | -46.73642 | 2026-08-17 04:59:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8043e05c-fccb-35c3-a199-6f86d933c6e6 | -15.91295 | -56.47502 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49a74a88-c680-3974-b507-7e3377237903 | -15.81673 | -55.52835 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a1c79f8-85a1-30df-8b83-885fdefad7c6 | -15.86104 | -56.32618 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f41365be-a62f-382b-94d5-7f69ba2e9ef2 | -15.85529 | -56.33809 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6ed5c54-c44e-3950-8db4-51f804967b8a | -14.08627 | -58.45115 | 2026-08-17 04:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7103275b-a03d-3668-a58b-b625348d8d6b | -16.21457 | -57.63774 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2091e93e-a5b3-3bcf-91d5-3b287b65c8c0 | -15.92314 | -55.53914 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e39884f5-90b6-31b1-9a56-22f2ec6c2231 | -16.30013 | -53.18219 | 2026-08-17 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a95ee80-5ecd-38c4-8b40-f777e61eddc9 | -15.6967 | -53.81071 | 2026-08-17 04:59:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a29f3f9-4d16-32e3-b828-348359f75232 | -15.92697 | -56.48447 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27c175a8-abe1-3b98-84a1-ff9aa92adf96 | -14.09179 | -58.4443 | 2026-08-17 04:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 70ea8f8a-7c77-3104-b9aa-8882fa69507c | -19.27614 | -44.97409 | 2026-08-17 04:59:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f1ab4272-4a45-3733-b333-12b4adba9adc | -15.94749 | -47.84367 | 2026-08-17 04:59:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba863895-1fc1-3f1f-a176-773a71f45f81 | -14.49457 | -59.32273 | 2026-08-17 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8c49242-5247-3eb9-91bf-6a6a1b9fa6e5 | -15.90577 | -56.47366 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86ace237-4993-3bc2-9e1b-0846015b1f56 | -15.85674 | -56.32972 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45ed4f65-a3ea-37c1-afad-dff90fa43fde | -14.50324 | -59.32434 | 2026-08-17 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2487ffc6-4866-3709-9f45-83e6a3d6dbad | -15.91581 | -56.47994 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1db3b9e0-646e-3ba8-902c-8e716a66eaf3 | -15.90248 | -55.53498 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9e41e68a-f10f-3cc4-a4e6-70b576ca32ab | -15.90722 | -55.52801 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| a9b1981c-1514-38d2-ab72-5efe3f45281b | -17.32967 | -54.92728 | 2026-08-17 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ff14a2b-cf02-3c12-b480-eb0d3732ef2c | -15.9128 | -55.5371 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d85c3499-5a7a-356c-9422-915e8f5c400c | -15.91904 | -55.54233 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 75215a07-64dc-3dc6-9db6-5fc0571d6ded | -16.76359 | -49.36143 | 2026-08-17 04:59:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 087cc00a-11ba-3c20-bd5c-5fb50b280a7c | -15.03255 | -52.67854 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a30f795-5233-3488-9b5c-eb8ba6f639d5 | -17.32843 | -54.93483 | 2026-08-17 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5c48bd24-0073-37d7-a64c-b0370aad1034 | -16.22799 | -49.70815 | 2026-08-17 04:59:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c79f0d79-dd43-3b38-9d1a-dfb1ba9cc677 | -16.61144 | -52.59385 | 2026-08-17 04:59:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8deed2a6-c08a-3feb-b1ed-06891919faec | -16.24864 | -48.99505 | 2026-08-17 04:59:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e80d14a6-f0aa-3fa4-9735-c061785ff57c | -15.9115 | -55.54484 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| fe7f859b-3cc0-3946-8413-62e0329d6f1a | -16.60752 | -52.59697 | 2026-08-17 04:59:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94026f0a-0710-3b65-82a8-3cf6afc37b7f | -15.94699 | -47.84755 | 2026-08-17 04:59:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dd9e8d0-df28-3c54-8050-4c0accd8b652 | -15.41436 | -52.98376 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25bd749b-fe3e-351a-b1db-fa68151abf6a | -14.0973 | -58.43745 | 2026-08-17 04:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 59f1420c-626d-376e-bd34-50947a15e46d | -16.71904 | -49.13113 | 2026-08-17 04:59:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63ddd83c-dba6-3504-8efe-5798cabfe88f | -16.67158 | -49.44311 | 2026-08-17 04:59:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59032c5c-a427-3f46-b1e8-fbabf90c1813 | -14.0966 | -58.44127 | 2026-08-17 04:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 5aaa5f22-f40d-382d-8f9d-0485e60190e8 | -15.24087 | -56.47059 | 2026-08-17 04:59:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0589dd78-691e-3fb4-bdcc-f857f1a2864b | -15.8174 | -55.52441 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef15979d-ec24-3b48-afd8-7bf74626a150 | -15.93056 | -56.48515 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecb64fc6-db4a-3e94-9b8c-e6ec09c3edb0 | -16.29461 | -53.17386 | 2026-08-17 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58246db0-25de-327a-8d35-d6f7479f57df | -16.20316 | -57.63571 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6d8604f6-2ab0-3224-9a50-401053f19726 | -14.39215 | -56.4033 | 2026-08-17 04:59:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30fbe8d2-f6fc-3c92-a202-75a88307e6c2 | -15.26781 | -52.90789 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 024f5edb-0305-315b-8c4c-50952f08bf63 | -15.30605 | -50.52102 | 2026-08-17 04:59:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b14d276-57fe-3dd1-b4d7-666027a626a3 | -15.86882 | -56.345 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85b60d12-4d05-388a-9b26-3d684c82c91b | -15.82042 | -54.19527 | 2026-08-17 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae92786a-0dc5-340c-ab8b-cfa9441cf63f | -15.27113 | -52.90844 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e35c0fc-d061-380b-b0e2-73957c2fda75 | -17.53189 | -49.21384 | 2026-08-17 04:59:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a3b735a-fdba-33ed-88a0-c55bfae754bd | -15.78728 | -55.5761 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ba21dba6-9a6f-31a9-8d19-3cb462bc7709 | -15.94799 | -47.83982 | 2026-08-17 04:59:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24d5fdd0-3854-33f4-a384-baf2769c218f | -14.49734 | -59.33196 | 2026-08-17 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 29306cda-292d-3d8b-b82b-f1b84b1507c4 | -15.22809 | -57.6508 | 2026-08-17 04:59:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b13287df-cfea-308b-99a1-b7d01edc50d9 | -14.10211 | -58.43439 | 2026-08-17 04:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6961e9c4-fb70-3155-aa40-4db9755189a8 | -16.21664 | -57.64818 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a860ff8a-3b94-3c68-8971-ba267372b8cc | -15.9194 | -56.48062 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 566b1a0b-946a-3d42-96f6-81cbfe07f6ab | -17.32506 | -54.93422 | 2026-08-17 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 986d672e-3e1f-3641-8b24-5e65c5025729 | -15.9459 | -47.84489 | 2026-08-17 04:59:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe0c2239-f868-3369-9026-d995e06a91ea | -16.29681 | -53.18163 | 2026-08-17 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90b1b384-89a6-3df4-869e-125927d3e8f0 | -14.10142 | -58.43822 | 2026-08-17 04:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 77a7e7e0-6aee-3489-aa1f-e8f72903378c | -16.76741 | -49.36197 | 2026-08-17 04:59:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b701a315-c985-3c14-a71c-7a696cd300af | -18.4446 | -49.73106 | 2026-08-17 04:59:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 829fb0b3-c71e-389c-80cf-7df1d772311d | -16.21077 | -57.63701 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 52828bd2-5cdb-3c67-870e-735765c8b748 | -15.90183 | -55.53881 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| b5912a43-cb3a-39f9-9a85-34fb7077fab1 | -15.17744 | -50.07455 | 2026-08-17 04:59:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbe8c95a-4c9c-32f4-b608-0f8d1512784e | -15.88383 | -56.34344 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ee3ec36-05c7-3d7b-a57a-08d147028518 | -15.91067 | -55.52867 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| bc046950-daba-39de-a72f-8e676c7ed95d | -19.8196 | -46.93528 | 2026-08-17 04:59:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c3e7942-23de-318f-b8e3-7b787291a43a | -15.90647 | -56.49125 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b794849-fecf-3d7b-8ec0-98b4df4fc890 | -15.4099 | -52.97603 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55d47223-7d03-34ad-a4ec-048d30ffc31b | -17.32445 | -54.93798 | 2026-08-17 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 21563a66-d3f2-3da6-8f9b-2f5e54764c25 | -18.46439 | -49.72884 | 2026-08-17 04:59:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 52e1de51-917c-33c9-9ce5-4d53f2e23f6a | -15.91559 | -55.54166 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| b69b20a1-0c76-3a4d-9f5a-d3a3b71edc8b | -15.91694 | -56.47823 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9671720e-f75d-3a8f-8b62-5c2985f48f85 | -15.91001 | -55.53254 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f523430-eedc-3fa4-9101-152a34dfdc76 | -16.22426 | -49.70766 | 2026-08-17 04:59:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4dca0b6-1f58-3f4d-bc96-7a6cd4628ffa | -15.03144 | -52.68568 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15b82f67-03e4-321d-bbc8-dcf63195b616 | -16.22314 | -49.70456 | 2026-08-17 04:59:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c115f1a6-6911-3783-b32f-bf7b3010585c | -14.09109 | -58.44811 | 2026-08-17 04:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 90af0626-3e50-3463-96ec-7b99f4a6acd2 | -15.85812 | -56.34298 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19294282-bb05-39cf-a62d-a7cead331430 | -19.27585 | -44.97005 | 2026-08-17 04:59:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b89c804-f2bf-38b3-97de-90aecd6a1056 | -15.79211 | -55.5687 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bebd63fc-d11f-3c9a-ac38-e4fe2b311de5 | -15.78797 | -55.57203 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d4b5bdb-def0-3499-b067-c34c326eecf6 | -15.8464 | -50.10191 | 2026-08-17 04:59:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbc569c9-bda4-3317-8a2a-5c2796c8f34b | -15.02196 | -52.72449 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32699965-911e-30d7-99a2-512d29abec6a | -15.92053 | -56.4789 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8479e97d-09fd-32d0-9610-05a3385af929 | -15.92771 | -56.48024 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ccb1283-3bb2-3df1-9d51-44520b4040b2 | -15.90788 | -55.52413 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 048f2565-95e6-32c2-94f0-147fa9fb0d6b | -16.231 | -57.65577 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8690dc2a-4557-37e0-9ae8-bff1cf31777f | -15.1609 | -52.8355 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f9e7565-dbbe-3fa9-ba29-178d55bcd3f2 | -15.92658 | -55.53979 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7fa33b3-49b9-3ffa-9f6e-78eeb126cf0e | -17.53578 | -49.21448 | 2026-08-17 04:59:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86be64ce-705b-3954-a566-4d30a5daa03e | -19.28074 | -44.97421 | 2026-08-17 04:59:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4ed28670-9a11-39aa-b5cd-eefba91c7de6 | -15.91969 | -55.53848 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a936e1ac-dc7f-363a-b28c-4a445daa8554 | -19.2755 | -44.97342 | 2026-08-17 04:59:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 09c34cd5-ef3c-3337-8b12-016f3135f165 | -16.22426 | -57.64948 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7bc7d552-0224-3d85-899c-a8d6c3be062a | -15.45964 | -53.04279 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aeac1f16-7ae2-33f2-85a6-cdc670bf3fda | -17.32781 | -54.93859 | 2026-08-17 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README42.md)
