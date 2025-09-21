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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5429d103-2191-3995-885d-1533c4b3a2c7 | -12.4361 | -45.1052 | 2025-09-21 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 213.9 |
| a4355f0f-0a43-38c6-9ccd-9d03da6c896a | -10.0314 | -46.2786 | 2025-09-21 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 09768d24-2a5f-361a-b192-213bae64a088 | -12.7114 | -46.8454 | 2025-09-21 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 211.8 |
| a84c4c62-ea5f-3dd3-bff4-ee35c130b8e9 | -11.5045 | -43.59 | 2025-09-21 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b15e7e0c-c095-3f60-bae3-a9cf41096ae5 | -5.5771 | -42.1493 | 2025-09-21 12:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 8ad63f76-7232-3f15-a653-28c31b13c8d6 | -5.5583 | -42.1507 | 2025-09-21 12:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 815e338d-f03b-3c46-80bc-1c3c82bbb91b | -12.6921 | -46.8482 | 2025-09-21 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 16a80063-8b3c-3859-8c1e-a8e7f2a66842 | -12.4357 | -45.1284 | 2025-09-21 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 4a23e89b-0e52-38f8-890c-6ada43c8276d | -14.8479 | -45.4846 | 2025-09-21 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 2a652ffb-4747-37fd-bd63-9c6ef749ca59 | -10.0317 | -46.2561 | 2025-09-21 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 06c8c244-7592-3148-bbc6-e22e5ce0e977 | -11.4862 | -43.5456 | 2025-09-21 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 45f14377-a361-31e9-acd0-fcec9f1b58b5 | -10.0128 | -46.2583 | 2025-09-21 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 27cfa2df-a2ea-34f3-ab2b-a709eb2f3917 | -12.7118 | -46.8227 | 2025-09-21 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| a1e01ed5-7d41-3daa-9f58-2617976c02ae | -11.4857 | -43.5692 | 2025-09-21 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| b4081d23-4266-35ec-85a7-928aa062d864 | -23.1523 | -47.6245 | 2025-09-21 12:30:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 204.0 |
| 510db81a-70b9-3012-9ba1-f0dd569b19cb | -12.6088 | -45.1244 | 2025-09-21 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 637.9 |
| 2f507081-1acc-34dc-bf69-3cc0ba0874e7 | -12.5895 | -45.1274 | 2025-09-21 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 073b7e69-5aa3-3c02-ac2e-9d4ddd2424c1 | -12.711 | -46.868 | 2025-09-21 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| c10fe353-7c88-31b1-bf24-a2d7a83d177e | -12.4357 | -45.1284 | 2025-09-21 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 81ed6798-9ed0-3c01-b7ee-f013e13e3825 | -23.1523 | -47.6245 | 2025-09-21 12:40:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 210.8 |
| 6b7c918e-d833-3422-a761-f76280f38d8d | -17.1173 | -45.9491 | 2025-09-21 12:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 99eed957-98d3-3f8d-9321-1a398d041635 | -11.4853 | -43.5929 | 2025-09-21 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 42825ab9-1899-39b9-bab0-96ea2dc346d3 | -11.4857 | -43.5692 | 2025-09-21 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 2ec9514a-ff49-36ee-ac09-7261b883a2b2 | -14.8479 | -45.4846 | 2025-09-21 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| ad5eda5b-e781-38de-8752-526ea18b03fd | -5.5771 | -42.1493 | 2025-09-21 12:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 2d0efbac-63da-355e-80c8-c26d955f5041 | -12.6921 | -46.8482 | 2025-09-21 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| def1f6f6-02f0-3eea-a7f5-b0ed5bf50082 | -7.714 | -44.4612 | 2025-09-21 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| e513b0c5-d609-3676-8599-84af37785c5c | -10.0317 | -46.2561 | 2025-09-21 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ac0334ba-bd4f-3adc-801d-3868c57ddc2b | -12.2794 | -45.2679 | 2025-09-21 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 5f7c27ae-1371-301d-ac96-0bb4f79625e0 | -5.5583 | -42.1507 | 2025-09-21 12:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 7653348a-73b6-3522-99e9-210f699d229b | -12.7114 | -46.8454 | 2025-09-21 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| aa39b8fb-d8c6-338a-a956-4abca4d8d2ad | -7.9471 | -43.8828 | 2025-09-21 12:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ec0c0f63-2ffe-3bef-afc6-4e0baee63e32 | -12.4361 | -45.1052 | 2025-09-21 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 4edd0c6d-2419-330e-9dda-93f6902a5a32 | -11.4862 | -43.5456 | 2025-09-21 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 098ce936-56eb-3b52-83ae-a3d373161fc7 | -11.5045 | -43.59 | 2025-09-21 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 3775326c-a95f-3edc-adc4-f8dbf7de69f5 | -14.8675 | -45.481 | 2025-09-21 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| c457ef07-49fc-3351-9444-470465f116cc | -11.4862 | -43.5456 | 2025-09-21 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 1cd3d76f-ab5e-31b7-b669-a040caeb61ae | -12.4357 | -45.1284 | 2025-09-21 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 306.1 |
| 0c2c72d2-7991-38fc-84f9-7b4ae7ffdab6 | -12.7341 | -47.7168 | 2025-09-21 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 0872d423-9f25-3eb2-bec0-df4a6fbba907 | -17.1179 | -45.9256 | 2025-09-21 12:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 9079c826-6cd2-3142-a885-7a9b26401b5e | -11.4857 | -43.5692 | 2025-09-21 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 1311d83c-07d8-37b5-b405-6ceb38702f21 | -12.711 | -46.868 | 2025-09-21 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d7c1ae81-7b1a-3bd4-8657-60c34dfee91c | -7.714 | -44.4612 | 2025-09-21 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 416d6cc2-1bbe-3b28-bb3f-c6a13586919c | -12.6088 | -45.1244 | 2025-09-21 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 492.7 |
| 636dc285-2d5e-3ba4-8f83-bffd5c7cabb4 | -5.5771 | -42.1493 | 2025-09-21 12:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 1c9fbe43-a70a-3400-ab10-2dcf4936b543 | -12.455 | -45.1254 | 2025-09-21 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 276.6 |
| ff1d8450-e571-307d-ae54-7d678c031877 | -17.1173 | -45.9491 | 2025-09-21 12:50:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 5dd52dfe-0a72-3032-8a88-b6157ba4f399 | -12.4361 | -45.1052 | 2025-09-21 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.6 |
| e2dbefee-68ad-3eda-9a47-d0b80fd13fb2 | -12.6093 | -45.1012 | 2025-09-21 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 373.6 |
| 38664165-0055-3936-a2f9-e626621cc913 | -12.6921 | -46.8482 | 2025-09-21 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 9ad3e553-0aa0-349d-aa3e-3b7a23574449 | -23.3981 | -49.1427 | 2025-09-21 12:50:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 196.8 |
| a2d999d8-fd78-3cb6-9f44-669be58f725a | -8.3517 | -44.6947 | 2025-09-21 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 9d279f57-af9e-3ab9-98e5-df8cf4593685 | -12.7114 | -46.8454 | 2025-09-21 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 74591eba-80bd-3e9d-8522-d987970711cb | -12.4164 | -45.1314 | 2025-09-21 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| dc4194b8-661f-3459-8f95-f94cc6f9750a | -5.5583 | -42.1507 | 2025-09-21 12:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| a97e41bd-6166-3d0d-a44c-638dc52ef013 | -5.5959 | -42.1478 | 2025-09-21 12:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 9ff66933-3005-31fe-9077-918ae535c971 | -12.1344 | -44.8042 | 2025-09-21 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 26c1e58d-c5c7-322c-a51e-570922ba561b | -12.4554 | -45.1022 | 2025-09-21 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 3b5186f3-228c-3028-bad1-05db2b50bbe2 | -14.8479 | -45.4846 | 2025-09-21 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| a78393a5-3fc1-3d52-a6ec-4d6f482b7968 | -23.3989 | -49.1191 | 2025-09-21 12:50:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 185.6 |
| de799257-abc3-395b-9542-19439da818a0 | -12.4357 | -45.1284 | 2025-09-21 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 772.9 |
| fb5cc3f9-fe97-3eab-8c3f-2c41c0d96a54 | -14.8479 | -45.4846 | 2025-09-21 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 9a6bb462-88fb-3966-bd81-59205c91c28e | -14.8675 | -45.481 | 2025-09-21 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 186.5 |
| fa1fdf51-7047-3b96-97a9-5d8801c87844 | -23.3989 | -49.1191 | 2025-09-21 13:00:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 755.8 |
| 8374653f-f17c-396d-bffc-82e5477eeded | -12.7118 | -46.8227 | 2025-09-21 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7e2ab929-5c45-34d6-90c5-777116dedbef | -12.3399 | -44.0946 | 2025-09-21 13:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 78e68125-38c1-33e4-8214-e4b1a109b622 | -6.704 | -44.0017 | 2025-09-21 13:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| f1fef7aa-5d23-3aec-bbad-d579f34d6da3 | -5.5583 | -42.1507 | 2025-09-21 13:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 9f818fa7-8727-33e1-b1ec-1115b2801956 | -12.455 | -45.1254 | 2025-09-21 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1055.2 |
| b46e3079-a0d8-390b-8c05-95523ee42ab6 | -12.4361 | -45.1052 | 2025-09-21 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 267.6 |
| 17271072-d8b8-3a04-959d-255e9c395224 | -11.4857 | -43.5692 | 2025-09-21 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 6c5b3b08-1d4d-3306-8119-c2c811b185e4 | -12.6925 | -46.8256 | 2025-09-21 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 956a5f48-bee7-32ae-8d99-e86be93f76a3 | -12.6921 | -46.8482 | 2025-09-21 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 69a092e9-eb12-32f1-bdb6-d524cd185036 | -5.5959 | -42.1478 | 2025-09-21 13:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 124.1 |
| ab1387ad-98b5-3eed-ac76-20d2e7027443 | -7.714 | -44.4612 | 2025-09-21 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 179.4 |
| d4e2e1cb-0247-3f1b-8c20-dbca14e7abd0 | -11.4862 | -43.5456 | 2025-09-21 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 5a7533fb-b871-33a3-b166-9307ee30efd3 | -12.7306 | -46.8425 | 2025-09-21 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f8a20a43-6d05-3ff8-bf15-d9a39f502db7 | -11.6377 | -50.5839 | 2025-09-21 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 2b9ba620-a9c7-3bb8-b6a2-4465a42601b9 | -10.0317 | -46.2561 | 2025-09-21 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| bb75ff12-9e82-3c98-a7b7-9a30dce07447 | -16.0011 | -47.2757 | 2025-09-21 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 68761b9c-506b-3f81-add4-a9f1844afd00 | -23.3981 | -49.1427 | 2025-09-21 13:00:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 952.6 |
| 89c19fc9-7ad3-3a26-915a-abb11726a17a | -12.7114 | -46.8454 | 2025-09-21 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 151.8 |
| f22d6c68-b2c3-393d-ade6-efece7e43a41 | -12.7341 | -47.7168 | 2025-09-21 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 65d55ce6-7f7a-376e-af0e-b0d3e81a9613 | -11.4853 | -43.5929 | 2025-09-21 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 2e3425fc-9cb0-3400-be49-da9e7285526d | -5.5771 | -42.1493 | 2025-09-21 13:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| cd731262-f28c-38a0-9c7e-9fec68d7de0f | -11.5045 | -43.59 | 2025-09-21 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 06c5bdff-54dd-3a35-8e11-ec3b238b7b01 | -12.4164 | -45.1314 | 2025-09-21 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| abf037f4-f9da-3d14-a88d-4efcd192243e | -15.9783 | -59.4069 | 2025-09-21 13:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 336be01a-0592-3a9a-8bd2-4347e0cc0a91 | -10.0131 | -46.2358 | 2025-09-21 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 4752acd2-beb7-3f9f-bf1e-904013ecc1b3 | -12.711 | -46.868 | 2025-09-21 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 9bcccfe3-c4d3-32c2-8749-2d66e05eec93 | -7.5272 | -44.3413 | 2025-09-21 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a7f54c2c-1032-32cc-8b18-7ffecc29c840 | -11.4862 | -43.5456 | 2025-09-21 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 72b11d53-b015-3a21-aba1-2c6764013bde | -12.711 | -46.868 | 2025-09-21 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 920f0393-54f2-3c08-8a8e-75edb134036a | -20.8809 | -49.6179 | 2025-09-21 13:10:00 | GOES-19 | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| 3d32e9a8-e479-33a6-afd2-76a6d675cb06 | -8.3082 | -43.6813 | 2025-09-21 13:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 954bc34c-c762-348f-a159-b6282de01f8c | -12.7114 | -46.8454 | 2025-09-21 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 22dd6f6c-b06f-3e8a-add7-384be8061235 | -12.6925 | -46.8256 | 2025-09-21 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| e9c86d3e-698e-3eb5-bf45-f4d67c545c2c | -15.8829 | -47.2973 | 2025-09-21 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| cfe7d582-d5da-3b36-9b48-81816d6d835b | -12.2983 | -45.2881 | 2025-09-21 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| fd64a389-a94a-3eac-8b97-f320cbd95439 | -10.0317 | -46.2561 | 2025-09-21 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |


[Clique aqui para ver as próximas entradas](README51.md)
