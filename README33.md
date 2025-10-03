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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f205d65-6731-344f-8c73-7ee073521df0 | -15.83569 | -42.6231 | 2025-10-03 03:45:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 04b0f16a-6398-38ed-913b-f51a5ce6bcdf | -11.67149 | -44.27465 | 2025-10-03 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c75e9d6-eef2-3118-a892-1ae50f4b5422 | -13.14813 | -47.89869 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33341b42-3f32-3e86-bac6-5d3eb50e294f | -11.09257 | -47.86653 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84229b20-9705-3e49-bc22-e7a7b505fa45 | -12.12389 | -43.44092 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f8ae1fac-241c-3226-b50c-0ed9e045fafe | -12.38753 | -46.51707 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 403bd055-9cd6-396d-9093-60d6e582a491 | -13.77935 | -47.57992 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e5b474a4-99c6-3133-8051-f215d1927980 | -14.2271 | -46.1 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9406e422-804e-31a0-a182-45c3bb78c96a | -12.39301 | -46.5182 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 162dfd55-a415-380a-a362-afba9ed84fc3 | -10.89446 | -46.713 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 65950bc9-1cbb-3e85-bad8-c35bc426b615 | -14.36057 | -46.14431 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a109024-03eb-3e79-85ac-51270253663e | -11.48431 | -43.5018 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f641efc-d4aa-3149-b986-5e184ad3bf42 | -10.89524 | -46.70901 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 02a64065-7bda-33d8-942b-3716bf82cdde | -8.64885 | -47.71277 | 2025-10-03 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69862b0d-2a7e-328c-9c4f-36e387475908 | -13.5265 | -47.2506 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4060d2a-a18d-3794-91a2-8f60d8e49c74 | -14.88743 | -46.8509 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd6247c3-cbc8-3b68-9a61-ee2ed6af5f18 | -13.24672 | -47.34856 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c6170d3-3250-3d05-84bc-b7197abaa47e | -15.35438 | -47.06301 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b8863a6-db04-392d-96ab-f4ac88f57213 | -11.07939 | -47.7073 | 2025-10-03 03:45:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f018c68-4f32-32c5-b47a-d335ad7de049 | -15.71647 | -46.26712 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50ce71e9-66c4-3288-b600-a2c8ce40661a | -11.53741 | -49.82343 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0f681e8c-ee7c-3b43-a997-6326af860e08 | -10.86896 | -46.66214 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7244f70d-3752-3aaf-983c-724c39e12f8a | -9.91404 | -43.73216 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b627f2a9-e9d7-32ad-8d61-3dcd806068f5 | -11.86445 | -44.97658 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ffca968-f5f1-35de-b39b-2c5c84a4f7f3 | -11.91968 | -46.28429 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 7b7131fc-8fad-3e9a-b6a4-eebdc85dee20 | -12.92858 | -46.37928 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b33d27d-6273-3320-89a9-b44ba5d406c7 | -14.72301 | -48.11808 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2197a5c-946f-3dd6-aa46-b152745b9c6e | -12.9299 | -45.09175 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc5369f6-8b5b-36c9-b237-d6579a138e89 | -11.47101 | -45.03573 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e61f60a-ac07-3a4f-9b76-6c94996d9bc6 | -11.91304 | -46.2846 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 349c4494-bef5-30ab-aac0-49c610eb772c | -14.60409 | -46.72084 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| deaeacf7-e100-31c4-a5cf-ffb12597602c | -13.30117 | -47.82905 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0759896-b3a2-3bfe-905f-a9929b9eba94 | -11.55665 | -47.6663 | 2025-10-03 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ed7711ea-caee-3ea7-8c67-0cbdedf06bf4 | -9.94648 | -43.74362 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 60150178-349f-329e-8e40-cf179e13aebf | -11.80994 | -45.02139 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4081f6c3-1592-3578-a933-d651c2a91ed3 | -14.87198 | -48.30497 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5ce935a0-c37d-3e39-9f99-a0fea7c5aaab | -14.36029 | -43.83672 | 2025-10-03 03:45:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d8d70e4-f129-3a7b-a75d-2e31c068911d | -11.13915 | -47.18277 | 2025-10-03 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c6b5657-e685-3bb7-9c5b-c9c6e492c12e | -15.6595 | -44.49809 | 2025-10-03 03:45:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c8488e25-7b8e-3e85-9b3c-5a1b6400ddd3 | -15.94278 | -46.22324 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7e748a9-1682-3869-8490-ebe1d41b27f5 | -14.60015 | -46.71274 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28941724-b4e8-328a-91c3-acbbc9880a52 | -14.97845 | -49.957 | 2025-10-03 03:45:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16ad65f7-f79a-3fff-a33e-9de3d28df47b | -14.89917 | -48.29163 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 946b01c2-d498-383b-978a-bd26038e63fd | -13.52087 | -47.24942 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ee3a67f-1120-3100-8059-8e8dae779401 | -15.32491 | -46.29987 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cbd6f02-2a48-3f26-b90c-f9c2c8290cc5 | -10.88146 | -46.71161 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f50fbac2-d244-3754-9c04-7322619d2543 | -11.28904 | -47.83777 | 2025-10-03 03:45:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8710f9d5-988b-3a71-a5ad-a0793e88c7ea | -13.31543 | -47.5803 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0c25bac-2d5f-311c-8d9b-4c124877668b | -9.94653 | -43.57526 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 216ebe56-4d75-3ed5-a9dd-8c3c8523ca94 | -15.11839 | -46.68144 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c557c70-01e3-3dbd-85da-cd8a7a4044bf | -12.61207 | -46.97145 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| aab7a064-4688-3254-b94f-aafecfa70f25 | -12.91217 | -46.89397 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4af5fb4-31dc-3450-b484-8eb622e1a64f | -15.92966 | -43.07209 | 2025-10-03 03:45:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca6cf4b7-a1f7-3622-9366-4a4cf597a634 | -14.30863 | -46.0192 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2da289ef-c6f3-340b-9e1e-31702cc0b10f | -11.47861 | -44.96712 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91a6aa8a-a48d-3d41-a5a3-ed9f4f6f0782 | -9.90644 | -43.71989 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 9cc99a32-ce55-3cd6-856e-1fa4c0599088 | -14.2964 | -45.97321 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea5c89fd-d2ba-3693-ba87-f0829f9240f0 | -9.37995 | -45.85199 | 2025-10-03 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1828dbb6-df95-348d-b13c-bf4b4963623f | -11.09916 | -47.86518 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fcdbe577-387b-3fbc-a9dc-887e255bd100 | -13.56762 | -47.5839 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b7980e33-64cb-355e-90f1-10d756965221 | -14.91365 | -48.33122 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 74916379-5a21-3da7-aa76-01c3c5df4b23 | -9.05864 | -46.64658 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c909fef-c509-3017-9a58-77869961bdd9 | -11.09198 | -47.86933 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31320504-ddb2-3f69-8b20-0e2667e692e9 | -13.75692 | -48.0812 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 48078c3c-4e24-35e9-b3c8-5d9cb9bbda49 | -14.29957 | -45.98408 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5daa80ad-65a4-3d95-be78-a1f891fc72a2 | -9.92578 | -43.72135 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 389f8e3c-324d-31a5-badf-c94638a4332c | -11.55072 | -47.66486 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6fcb3ea0-677e-345b-b004-f1a51cf5f572 | -13.57126 | -47.27522 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc159446-b02e-3d20-82c4-04b4be50c1c6 | -13.33195 | -47.79742 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27b54a6b-74e6-3f60-a2e7-e433bd694e01 | -11.47378 | -45.0209 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 145a95b3-ed19-3d0f-aa96-6131ac27ffb5 | -14.35646 | -43.84939 | 2025-10-03 03:45:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cc16780-813f-3642-988a-c13d405bcc8e | -14.35733 | -46.13364 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33a99300-4e6d-395e-9eea-0f5739a93918 | -13.75111 | -48.07952 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8d9879c5-78ef-35ab-af42-fb3efa191cea | -13.58315 | -48.19212 | 2025-10-03 03:45:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9064b492-feec-34a4-9691-28f955d328e0 | -13.35416 | -47.33279 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 881e5908-96ac-3d61-9072-f5d8dd8692d4 | -13.77061 | -48.06293 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dc302d07-cf1c-394f-b17e-baa9c1948983 | -15.52624 | -46.81142 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90926c73-89fc-3b7f-a69f-26253663efeb | -10.64307 | -39.92984 | 2025-10-03 03:45:00 | NOAA-21 | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 305cab07-6ec5-3d37-8cb6-5076c6ae30a4 | -13.77522 | -47.57092 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b7fb9e33-d18a-388c-b668-5050504c178e | -12.93071 | -48.42907 | 2025-10-03 03:45:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50041306-5bef-3adc-a14a-46cc56fd31f6 | -11.30476 | -42.79911 | 2025-10-03 03:45:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 77e65f1d-018c-386d-8a51-89e4063ac3d9 | -14.97813 | -49.95873 | 2025-10-03 03:45:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c694586d-d221-3fa3-b33c-266ade4357c4 | -14.01435 | -44.96456 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dd191c3f-85da-3e39-ad52-a945afde20a9 | -16.43194 | -42.40986 | 2025-10-03 03:45:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6199130-6ea6-3124-abe2-5073c2ff69da | -12.20204 | -47.78851 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4ef56cf4-f8ae-37cf-984e-6dec1e674af8 | -13.55083 | -47.30509 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| edfff655-1906-33e2-bb40-1424f1542d2d | -10.22608 | -48.24398 | 2025-10-03 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6610d7c3-bb94-3b77-b4c7-f61bae0044c0 | -11.85173 | -44.96165 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0d03ede-a1fd-3b6e-9793-d5736804a48d | -14.89408 | -46.98444 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f76721f-07a0-3efe-a3c2-aefe3d349fbe | -11.57119 | -47.65545 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bd5b4e57-1a13-3208-9e30-ad05ed9fa200 | -14.3556 | -43.85394 | 2025-10-03 03:45:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5fcfbba-6813-33c8-b0b1-cfa3b76fa379 | -11.4975 | -45.00606 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80b73822-4c7e-3c42-90d1-6202ede5e4cc | -13.34576 | -48.11167 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcb0b990-6a90-31b8-8cba-36ed37088a22 | -14.66994 | -48.26302 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2080e223-24dd-3bb9-aa88-a403085890de | -12.37591 | -46.51817 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55637b48-db82-3ebc-acbf-d0334a49b5d3 | -8.91086 | -45.04358 | 2025-10-03 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab647d72-8f5d-3de4-9aa8-a11b8fbded53 | -11.6763 | -44.27554 | 2025-10-03 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17d38b1b-62fe-3c41-9814-99f0cc1e8a41 | -14.38098 | -45.94796 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32be76e1-07b4-3ba4-a61a-cf57177f27ea | -9.9177 | -43.766 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9c3dc17e-44e0-31de-bcaf-7b23e7b6a996 | -9.43429 | -45.46683 | 2025-10-03 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README34.md)
