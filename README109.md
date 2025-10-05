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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ade31325-13b4-34a9-8293-522b352e59de | -15.39646 | -47.95431 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 80083130-6b34-3530-82ac-3918a61e6e3c | -18.1729 | -53.36005 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a6c110d-95a5-3109-be80-629cd6d67a89 | -15.26058 | -56.76842 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b50f16f3-1606-3a94-8ee0-475e023dc052 | -14.67487 | -48.35706 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d45d92b8-63e0-32d8-86fb-249b7b4cf2fb | -14.67638 | -48.25613 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41fa0e29-d6d1-3b3f-8e1b-c2961e79dbee | -13.91639 | -48.1953 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43251efd-faee-38e9-9163-479a8cecae88 | -19.84599 | -46.52528 | 2025-10-05 04:49:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a33a8cc4-ee0e-3a36-bb0b-8bc10f3632a4 | -18.18669 | -53.35856 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86934fc7-84fe-364c-ac60-3c960d0ea702 | -15.618 | -49.1209 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c0e8b9c-e6ae-3351-b855-d8391514e943 | -17.88223 | -57.6423 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 5f18a1fe-5e5e-382e-9c92-8627876f919c | -14.61003 | -48.12353 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c7969fc8-9583-3ad4-9713-eb2fde9b7c5e | -17.95363 | -57.55219 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d505b276-847f-390a-a696-f78e81433d46 | -18.16082 | -53.32827 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 97124937-4b93-3b0a-a106-22ddb504a5a5 | -15.25694 | -56.76763 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 505e71ed-6c88-3c02-8061-d3852a909595 | -18.15785 | -53.32439 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 024cbed7-ed25-3957-8d7a-c02c1dbc0362 | -16.36175 | -51.45306 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb23412c-dc33-3534-b0bc-dd064a94ba31 | -15.39241 | -47.95383 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 855bb5f3-61d8-3bec-a695-51d936b61d49 | -14.32563 | -47.674 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| edc63232-44ae-30b0-a20f-e193efdad874 | -16.3657 | -51.4734 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a9ef8b2-e7ca-352c-bf10-2a0d793bc93d | -14.56623 | -52.47134 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5af8b971-6cd7-3264-bd76-7a931458af1e | -16.343 | -51.46188 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85652f6f-b9e3-397a-a9cc-6a416891079b | -15.57452 | -52.45952 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 555dd4a8-631c-3e61-b753-c08c74fcb24c | -17.87555 | -57.59284 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 24d4a4cc-925f-36c1-b9df-5f2e373e9f5f | -16.07224 | -51.08909 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bd42769-31ee-3851-8aed-23a52ef048f0 | -14.3353 | -47.69439 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee366ef9-f190-375f-8c3b-460622544a47 | -14.63207 | -48.22744 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 842dd8d4-12e0-32fc-8897-f24ba21a5979 | -14.97532 | -49.97048 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd028425-9e5f-3520-987a-06d14c283342 | -17.92883 | -57.6061 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a86a5778-2867-393b-bee3-f1a244400fa0 | -15.25329 | -56.76685 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eae251a3-a65f-3c24-b165-986a31ea916e | -16.35719 | -51.4603 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69822576-b89a-3088-8321-ff12ca1afdf9 | -14.88169 | -48.15443 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 245c34d6-1c30-30c6-8a97-5c7537739df2 | -14.84224 | -48.38784 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d8b0b00-dc6d-3bce-941a-443caf659403 | -14.67274 | -48.2837 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad8047a2-d55c-37bd-b042-a23cabb190d4 | -14.30147 | -52.92589 | 2025-10-05 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 674bfe80-69d6-338c-8421-ea2d63c2cdb1 | -16.34923 | -51.46693 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15bf56be-7fb1-3948-b6c6-b014aa56d774 | -16.04055 | -51.04045 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e7e4cbe-74ee-3f99-9f78-8cda6452e35b | -14.99558 | -49.98217 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68b09e32-4604-3822-94ec-7feaae238037 | -16.36014 | -47.05903 | 2025-10-05 04:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ee2c68b-b826-3aec-a5da-6cdb469ffdf7 | -12.90711 | -54.74507 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47ada05d-2c11-3362-9568-0030b1524970 | -13.91962 | -48.20085 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48bd29f3-74bf-3563-812a-746394203f67 | -15.12966 | -45.74699 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fd017bd-6773-35ff-9963-7c71337d86dc | -18.16959 | -53.35952 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c36aa65-f885-3f53-a2a0-55ac72af1122 | -12.92763 | -54.72453 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59fa27a5-602b-3a89-a55c-f953aefd2b8f | -16.07281 | -51.08521 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea0ca29a-8dd5-31ec-a142-6b139a717f6c | -14.68202 | -48.3629 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d56d6184-9aa2-3505-ab27-f9cdb3655fa2 | -18.17952 | -53.36109 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1bfcc81c-e7e4-3310-a0ed-aa8a2336b3da | -13.72827 | -48.07598 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e8cbac32-e90b-3758-ae42-ec76fc749d96 | -14.68859 | -48.34359 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff2005b0-950f-3cdb-a6a8-95bfe0e95704 | -18.14513 | -53.34087 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 921b9117-4223-37eb-b90c-12c8308d9efc | -18.20155 | -53.37218 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64788993-a59d-3944-b69e-08b2f6f16f58 | -14.57008 | -52.46834 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0a89f5d-5872-39e1-ad8d-844c12f3b6ac | -15.37684 | -56.98207 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 536221e0-e6f0-32eb-ae31-80130765f2f7 | -15.54714 | -46.8563 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f491cbba-2a7f-3c82-9dbd-aa9ee770e5e8 | -14.65756 | -48.33791 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9087c9c9-8641-3bfe-9723-5e97cfb98aa0 | -14.19745 | -46.67359 | 2025-10-05 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b219aeb-a847-3659-9d49-8921c9f9c213 | -15.39694 | -47.95061 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e0f55d9-db26-395a-9f62-9cac5363936b | -15.32205 | -46.37156 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d11440b4-e2d4-3979-83e1-331fbe8e2c02 | -14.27512 | -45.86204 | 2025-10-05 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fda509f0-6c0d-36fd-a528-c612cb5bc9ee | -19.01681 | -50.60402 | 2025-10-05 04:49:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a6af8211-f59b-3537-b652-325966d68d1b | -16.43617 | -52.15532 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dff2e6d3-4083-39f4-9dfe-af67b753387d | -18.24519 | -53.33126 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8dc1f168-6320-3497-bd00-e45b9e51200a | -16.38331 | -52.16497 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c6752d70-82e9-3883-990d-d05f5927ecce | -16.01439 | -50.95227 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 609bc92c-9980-3d40-a263-76560f0361b4 | -13.78115 | -47.80186 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94274d61-8656-3770-8070-24d43cf272ce | -14.66711 | -48.35573 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54b82a91-8383-366c-807c-1f70744e5c6f | -16.26829 | -47.10853 | 2025-10-05 04:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea98f3b2-86a2-31ab-a122-5137a848b751 | -16.3464 | -51.4625 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8f612a1-5db4-34af-b3ac-fec592274735 | -17.94968 | -57.59616 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7d09451d-8f37-38a2-afb5-cf888dc91768 | -13.69916 | -48.05353 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37b8ac72-6670-3dde-9a7b-f07a2d622abb | -16.91158 | -52.04432 | 2025-10-05 04:49:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccad6078-ad7a-36ef-9843-bd5ac0467a64 | -14.3955 | -45.94348 | 2025-10-05 04:49:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a4fa4bd-d633-3a3a-be57-c968f08a06dd | -15.36895 | -47.9763 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8dd6183c-7e74-3254-ab99-d12f2f3eeff3 | -15.23095 | -49.74443 | 2025-10-05 04:49:00 | NOAA-21 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8b51093-1fc3-3b59-a17b-23e08124f3bd | -17.94518 | -57.60005 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ff43fe5a-5264-308f-9246-1dea682973c3 | -17.84905 | -57.63501 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 49e7e734-b4fe-36a5-ba57-aec32bd00048 | -12.90305 | -54.74834 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41a513cc-f0d6-3498-83d8-9f716432e25f | -17.96114 | -57.57439 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6724d8e5-065c-3a00-be8f-13acfffc785d | -14.97415 | -49.97884 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a0c3027-ebd2-39a9-a134-c90c6467d1ef | -16.36514 | -51.47718 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 536dfde1-01cc-3ab4-8161-9956bc39326c | -19.94476 | -44.38818 | 2025-10-05 04:49:00 | NOAA-21 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 259e3f1a-157d-3c64-8a6f-0b9f081b61bd | -15.00144 | -49.96663 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17f85032-abb3-35a9-9bc2-65fc1b999ac7 | -15.35411 | -46.29964 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c88d7a11-f651-3394-88f3-e03d45aed837 | -17.88592 | -57.64309 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| f59d9f65-d5c9-3f04-bbb5-484a9689c7db | -16.3532 | -51.46364 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d2e1490-862d-346a-98fe-37c79a89f4e5 | -14.30203 | -52.92235 | 2025-10-05 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf9e6aff-3c3c-3f3b-976b-54b408e690e8 | -16.04623 | -51.00127 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2b9b023-9bf3-34de-b6f6-ea79f735df55 | -17.93334 | -57.6022 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 865fc9ba-34d5-3cf2-b794-e4d050a482ef | -16.01835 | -50.83629 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c891b91-b74b-33f6-9288-7a898bd0dfde | -14.60782 | -52.5332 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ec01b0c-11e8-3ea2-b1ec-33927a3e327b | -14.68382 | -48.29023 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 53a0103d-c586-3223-b452-b18aa91c3026 | -18.24407 | -53.33852 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ce080d8-ff3b-3cc4-889c-3851c939533d | -13.82693 | -48.05709 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13893860-cdaf-3b9e-91fc-c294ca6ce8d8 | -15.2337 | -49.29739 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a5ef734a-d049-3099-ad8e-cb8b4d4ff216 | -13.97408 | -48.12183 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ea15013-e246-3cee-8747-165db6be6a84 | -14.82702 | -54.76695 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0f7fcf9-2935-340e-8692-db94a3ca73b0 | -15.72105 | -46.25269 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ca75aeb-b91a-38bc-88d9-e6a3d7dbfc22 | -16.3515 | -51.47512 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03039a6c-1eb3-361a-9c1d-c04b7384155b | -18.33656 | -45.8883 | 2025-10-05 04:49:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4cf40721-8ed6-334a-a3d6-7a672169507b | -15.77011 | -46.26588 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe285f98-1867-3503-a1d0-7ad00029254f | -15.54918 | -46.84033 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README110.md)
