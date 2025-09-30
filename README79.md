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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c223612-5472-3d0d-b9a2-820499700923 | -14.71139 | -48.2402 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 038a2459-5b7d-3992-aac9-e2b71d35a980 | -15.29233 | -46.41074 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b0746d9-0cb6-3b70-884c-1d8a2b30ba51 | -14.54239 | -48.4907 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 80493596-490b-3e0b-b0e8-c4e57c352848 | -15.13259 | -50.109 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59ea33ca-9a3b-393d-b11f-5b25eed5785a | -15.69317 | -46.26359 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 104a1a4a-24bf-388f-90b1-ceb9e8298718 | -19.54887 | -44.24245 | 2025-09-30 04:42:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d4485b5-7d69-3e18-ade9-ea52d6ec60fc | -19.85829 | -43.81533 | 2025-09-30 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 14cddfe3-36bd-32db-9a3e-8168afce3f4b | -14.69129 | -48.13741 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4f4b13c8-4993-3320-a5f5-052544c59926 | -15.17622 | -46.41048 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 184efa03-81f2-3658-ac0b-2dacac686e13 | -16.42837 | -47.01194 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4fc6608a-ddf7-3d82-ad73-fe6934f70f4d | -15.28998 | -51.4333 | 2025-09-30 04:42:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2075100-2a3d-32d2-b406-5339425f6e83 | -15.14848 | -46.43512 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ac2ed80-0598-3b55-b582-891a98f14bcb | -14.58018 | -48.22019 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f3f67a6-aced-3ab3-8d6c-87b6df2db178 | -15.47098 | -47.93705 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8333c6e5-8294-3543-aae4-5fdd1c7ff6a4 | -15.25421 | -49.72029 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3bb47fe-ad1b-368a-b24e-027988cb4cb5 | -20.62455 | -46.1748 | 2025-09-30 04:42:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e70adefb-5289-3f01-8e43-f2d6efc1137e | -14.54189 | -48.46733 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a275976a-eb70-37e2-a8e7-a81dcbe1084d | -14.6547 | -46.96624 | 2025-09-30 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| afb4f636-a85f-3dce-9df2-e2db1a86e117 | -17.87529 | -49.39445 | 2025-09-30 04:42:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4411252c-8c90-3a7b-9f92-5c4efb319990 | -15.25476 | -49.71654 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b5eef1e-699d-374a-be85-042dde6b5d01 | -16.84361 | -48.90155 | 2025-09-30 04:42:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f850dce-963e-37f6-9e96-a4a8c1449cec | -14.71092 | -48.16482 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1e674166-2602-3320-9be8-c089cad2b16d | -19.77358 | -48.96737 | 2025-09-30 04:42:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5489671b-14fe-3ba0-9020-2d3c4f6d4b43 | -15.1277 | -48.38713 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff6845d9-cf20-3b61-897b-bdea60a9265b | -15.26158 | -49.71737 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9d1cd593-fd36-33ee-bc78-62e901a8f7e8 | -20.06514 | -46.79492 | 2025-09-30 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3c6f637-cd99-3779-a04c-21c9b61dac87 | -19.34989 | -43.96856 | 2025-09-30 04:42:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f125ad9-dcdc-30ec-95f0-ec03df2b10df | -15.25078 | -56.79781 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83152408-1fec-3e63-9c5e-703bbd963520 | -19.3358 | -43.81293 | 2025-09-30 04:42:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20ff2c6e-2f6e-3350-84e1-fc93e7d76658 | -15.28786 | -46.41364 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ee271ed-bd5a-343a-b5dd-01d725376428 | -16.41001 | -43.72474 | 2025-09-30 04:42:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f115db7-bf6d-3a36-a8c6-6058b16d8ac8 | -15.24796 | -49.71546 | 2025-09-30 04:42:00 | NOAA-21 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40ce9700-95fa-352f-be23-f92b18982ce8 | -15.62794 | -46.25359 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7eb97d95-d3e1-31f8-bdfc-c045c927d131 | -16.4095 | -43.12076 | 2025-09-30 04:42:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93d1ce4f-64d3-3c4c-b7e8-54c6820570ed | -14.79211 | -48.30703 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03f5aac7-d64f-3318-a3ce-6b691d08ce9d | -15.28058 | -47.85172 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 423daa6a-d26f-3437-a7f8-17fe13f4bb9f | -19.30557 | -46.24445 | 2025-09-30 04:42:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1fe5763-61d6-312a-a959-c0c294b5c253 | -15.03649 | -46.97842 | 2025-09-30 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e46e92cc-c2d6-3e00-8b98-3444c4ddf17b | -16.66179 | -49.53258 | 2025-09-30 04:42:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ff2a495-1778-37b5-8dab-879901631416 | -15.00664 | -47.41845 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 305544f9-f3e7-3b03-b998-eb79f29fda13 | -15.28624 | -49.26468 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85dfe0a4-28a4-359f-a2d5-8a1c7dcecfc9 | -16.42053 | -47.01059 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e6e5218-02e7-38db-883b-0d4679b93835 | -15.42394 | -50.24891 | 2025-09-30 04:42:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67cea733-4e05-3611-92b0-2ed0f371abbb | -17.39517 | -47.14025 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7648bd3c-8374-32ac-a658-fb10502a9972 | -15.37571 | -47.07016 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 137fee75-7787-3958-9adc-40e346140476 | -15.27141 | -48.77565 | 2025-09-30 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42075417-5dda-3892-912b-6868f759c346 | -15.23363 | -50.09171 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aff998e9-9cf0-36ca-9b8b-514fc3da89f5 | -14.69411 | -48.23244 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 04b91206-6fe6-3f7a-a8ec-b4833d7d6777 | -15.28735 | -47.85733 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d030fa22-4a03-3f43-863a-ebab2d8ac040 | -15.38791 | -47.06744 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9171926-8959-3701-8b29-3839fe2f2731 | -15.27407 | -49.2513 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 317262a1-d11a-3381-b72c-e6f66c6a9777 | -15.52108 | -50.04879 | 2025-09-30 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a08b398a-62a5-3452-9e42-6cbeaa1eb686 | -15.25246 | -49.7085 | 2025-09-30 04:42:00 | NOAA-21 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc99eb25-958e-3e39-9369-a4a7d99ce2b4 | -15.85923 | -46.2286 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24810f68-6315-395a-9acd-e140727a9282 | -14.81172 | -48.75251 | 2025-09-30 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4747870f-5d69-3f03-afd9-0e2d1c071113 | -13.03238 | -56.89763 | 2025-09-30 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a9b99b5-b885-3a0f-baae-b42bfb89c915 | -14.53656 | -48.22891 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bdc5143-ffee-3f78-824e-26e332d2ef70 | -14.72501 | -45.66809 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7efbfb4f-010f-333c-9642-7c72be15199f | -14.71463 | -45.6726 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02366f27-e390-3d9b-8b72-a6785a36a9d6 | -15.73506 | -48.894 | 2025-09-30 04:42:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44cdc418-d0d1-3f4a-87c9-3614cab0398f | -15.26008 | -56.79223 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04dca915-e61f-3065-bd93-b7ca33ac7e85 | -16.43019 | -47.0284 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 97886775-c84f-3671-a7ad-e6734f1426a9 | -15.84605 | -54.03166 | 2025-09-30 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b47f1e4f-9ba4-3338-8c8c-7088e49ac1c7 | -15.12923 | -50.10845 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2429a0f-4a0e-362b-a73c-7a4203fc00c7 | -14.72552 | -45.66408 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 14696354-7796-3e71-90ee-6e96b7c2bb04 | -15.3841 | -47.06652 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5aa8e5d2-88d6-3bf1-9e13-eb9c962d7969 | -14.7102 | -48.24863 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ff1ba5a-63c3-35e9-a1b3-c4f5e324dac2 | -15.32772 | -46.2667 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 043825ad-e17c-346b-b4ba-61ff5f7515b9 | -14.70312 | -48.1679 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19fe178e-cf42-310f-8493-16fca0c67269 | -15.27906 | -47.89515 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 893f37a9-f30e-3606-a017-e93eee3d93f7 | -18.61781 | -50.71247 | 2025-09-30 04:42:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6d3aaa2-2803-3827-be44-e74d24c749bc | -14.54364 | -48.25618 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3fd19eb0-3afd-3a0e-bd54-b1fa08e5e232 | -15.92905 | -43.30883 | 2025-09-30 04:42:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00fc8376-0bae-38cd-bcb4-120c96cd595d | -20.18873 | -49.12298 | 2025-09-30 04:42:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80d58a1d-913c-31e8-a8bd-8b924b16ae87 | -15.272 | -47.88708 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6a70666a-fe2c-3337-9449-479748b0becf | -15.90933 | -46.22899 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a6337b1-39c6-3e3d-8047-0958c8607014 | -19.58901 | -43.87071 | 2025-09-30 04:42:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 102102d3-8c98-3a35-9907-3f8ce6d1a996 | -14.53009 | -48.47564 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 76b40bfe-7796-35b8-a4a1-2aad530f50aa | -17.70633 | -46.65998 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f16da0ec-ad45-3f6f-a450-c060321af9e0 | -14.71264 | -48.23124 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51a9f26e-5c08-3504-9182-8475867a7552 | -16.11434 | -48.40925 | 2025-09-30 04:42:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 157ebec5-7ee5-34d3-a453-8baeabeeac03 | -14.79268 | -48.30293 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2373228e-c977-3f78-a6c5-f717281d8156 | -15.85471 | -46.23129 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a4a89f0-62a8-3de7-9099-f30946a4767b | -13.76013 | -54.72656 | 2025-09-30 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78fab0b4-9dff-371e-aa96-bfae10d4c83a | -16.23131 | -41.73283 | 2025-09-30 04:42:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b4cdc180-4135-3c60-818b-df39a6946c60 | -15.34196 | -56.64352 | 2025-09-30 04:42:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e696691-c0be-374a-aa19-37c3ee65b506 | -17.79795 | -50.11799 | 2025-09-30 04:42:00 | NOAA-21 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 348cc121-e7da-398b-b92f-2b81c1b3a2bb | -14.7428 | -45.6624 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33273866-ec3d-3af2-bcf6-ac6882d53ae9 | -15.14806 | -46.43835 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bd3170b-9c3f-3400-aa78-45e0cd57bcac | -16.49994 | -46.03936 | 2025-09-30 04:42:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65fc7b0e-a984-3dc9-b784-53e099f7c589 | -14.5171 | -48.44017 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed532320-b25a-3985-bea6-36cc28c1a1b6 | -15.25136 | -49.71603 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23b4606e-1c8b-39a5-a5cf-2b17daa05cd1 | -14.59037 | -48.27821 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 683656f3-945a-3ee2-b3df-4190ca60fcaa | -13.75867 | -54.73524 | 2025-09-30 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 068de060-d543-3cd7-b381-4022c4b7c6c3 | -15.25817 | -49.71696 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a10e7960-aae0-334e-9bab-2ca35a8c3634 | -14.54657 | -48.48568 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d17b15ef-4421-3db7-9fdc-0506f9adcd57 | -15.84476 | -54.03948 | 2025-09-30 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0aa2861d-f5bd-330a-a366-e772af89924c | -17.41306 | -47.1269 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47b7ee53-c8de-3c0c-940a-14201be06c36 | -15.24979 | -48.74907 | 2025-09-30 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 101a5932-6344-332c-a67e-a6519714e7f5 | -15.85364 | -46.23962 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README80.md)
