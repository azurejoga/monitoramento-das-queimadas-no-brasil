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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de70b408-0b39-3031-9d6f-502d1c0638d4 | -10.4551 | -57.9378 | 2025-08-29 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 3b707972-f1bd-3eb0-890d-133338892295 | -3.4254 | -49.0517 | 2025-08-29 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 10dfc670-fdb1-361f-a325-0cb99e1dfa18 | -12.4156 | -63.9183 | 2025-08-29 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 22d405b2-5db8-3235-9d9e-fd6ae02cbdb0 | -8.1758 | -61.3755 | 2025-08-29 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 497b3a8c-1b56-3b5c-8551-a243a626d841 | -13.1842 | -45.2633 | 2025-08-29 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| e9b42495-be45-3715-affe-9ca72eb324dd | -6.5358 | -43.9237 | 2025-08-29 00:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 5676705e-8c48-34b9-8dc7-c4f92ecb6156 | -11.3517 | -43.566 | 2025-08-29 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 54976e8c-b770-3318-8632-fa6ea5362d6a | -13.0151 | -56.9184 | 2025-08-29 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 8f4b34f2-83b6-3627-831e-0cddf209f6dd | -3.7509 | -54.8291 | 2025-08-29 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f9b8b047-62ab-3697-9656-fbcba3a2a5f5 | -10.3622 | -57.8456 | 2025-08-29 00:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d1a4058e-5725-37ca-97d7-a2fb3aeeecf9 | -10.3812 | -57.8245 | 2025-08-29 00:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 4e0e6615-008b-3628-a86e-5347e9ce7029 | -17.3643 | -42.6284 | 2025-08-29 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 312.2 |
| 2fb331ed-5752-3fc6-a896-8c3fae1dab6c | -9.462 | -60.549 | 2025-08-29 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| ffc86c22-9740-3bed-8ede-882440813192 | -5.6933 | -45.9667 | 2025-08-29 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| ff80c87c-05a7-3544-bd41-d0975fd0c555 | -6.5546 | -43.9221 | 2025-08-29 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 1ed29040-9bb8-3ea7-a3e3-565f6692bd53 | -9.4433 | -60.5499 | 2025-08-29 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| c82e2eb7-9d3b-35be-867e-99588b5978a5 | -12.9961 | -56.9201 | 2025-08-29 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 4a7ffd8c-7a71-344c-9abe-ee3c892e4685 | -12.0784 | -44.7199 | 2025-08-29 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 81cc1225-97e8-33bb-b2ec-d446f39922af | -12.4534 | -63.9164 | 2025-08-29 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 24999c5c-2a1a-31d2-a38c-708d64df822a | -9.2178 | -60.8689 | 2025-08-29 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 6836c695-82ac-3062-86e5-f410dac125ef | -10.4738 | -57.9366 | 2025-08-29 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| c55f6fc3-eeda-3df1-b9a1-c83840844824 | -17.3636 | -42.6532 | 2025-08-29 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 118.8 |
| ea7642d3-9e5a-3a91-a080-45ff7b4218b2 | -17.3435 | -42.6581 | 2025-08-29 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 155.8 |
| c517b92a-157e-3f1d-ada4-079e4f8587ae | -12.4344 | -63.9364 | 2025-08-29 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e8cba496-7b0c-32cf-ba31-4bb4f5dfd1bd | -22.6756 | -46.8439 | 2025-08-29 00:00:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| 6cd8b1f9-0cce-3dc7-ad54-c1df5115d626 | -12.4345 | -63.9173 | 2025-08-29 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 214.6 |
| dd94c43c-ff32-3348-beb3-675c55b3ea33 | -3.7693 | -54.8286 | 2025-08-29 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a028bd6e-d0bc-3528-9903-835040871a73 | -13.1837 | -45.2865 | 2025-08-29 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 327.7 |
| aaa7e264-2240-327c-8654-59566a87e557 | -9.4618 | -60.5682 | 2025-08-29 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 152.7 |
| dd9f6d3c-245d-380c-94ac-6ff365c3d8ee | -12.0976 | -44.717 | 2025-08-29 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 4bf7153b-a571-3038-8df3-0cde9dfefe52 | -13.2031 | -45.2834 | 2025-08-29 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 221.1 |
| 499b7c42-5987-3099-90a4-77d2f936c7ce | -9.4452 | -47.6364 | 2025-08-29 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 19f642e2-6c8f-3031-a3ac-ef0108ee8a4f | -17.3442 | -42.6333 | 2025-08-29 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 394.7 |
| aed7e96c-3095-3360-b15c-e05792c39c16 | -5.1702 | -46.0676 | 2025-08-29 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2202f010-12d1-3dd9-bc9d-ffadac8501f0 | -11.3329 | -43.5452 | 2025-08-29 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 5a35ac2d-24ba-3b32-a515-9c9b9d1b94f5 | -11.3325 | -43.5689 | 2025-08-29 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| a4e7b485-355e-32e4-9ce8-3386fc86737f | -9.4263 | -47.6384 | 2025-08-29 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 18101572-a6a5-372a-b1d1-dbbab5668ece | -13.2036 | -45.2601 | 2025-08-29 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 9455d8e9-ef70-3dd0-be32-826c05a57107 | -9.4432 | -60.5692 | 2025-08-29 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 3b6022ca-ba24-33f1-b3a0-80f16248def4 | -10.3624 | -57.8258 | 2025-08-29 00:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| ec47d25d-41d8-3588-8804-f95d81699e07 | -13.0342 | -56.9166 | 2025-08-29 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 328c1a50-d84e-3857-8e8f-bf757e6427f8 | -17.0399 | -45.8716 | 2025-08-29 00:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 15eb998b-2b68-3a07-b789-bf6cb748517c | -8.1945 | -61.3556 | 2025-08-29 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 273eaa17-04bb-3eea-9823-580b42d23dce | -10.3624 | -57.8258 | 2025-08-29 00:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| da0295b7-5188-31b4-9102-fa079f22055f | -13.2036 | -45.2601 | 2025-08-29 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 47d22606-e596-353b-8791-a2fd1a7408a4 | -17.3643 | -42.6284 | 2025-08-29 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 197.6 |
| 06fdc447-bba1-3ccf-a370-fce70fdaa4bc | -24.1861 | -49.5515 | 2025-08-29 00:10:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6ae09d76-9956-370a-b0c5-e5218b20d85c | -17.3442 | -42.6333 | 2025-08-29 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 246.0 |
| 689a533a-0d3b-39c5-8e9b-77e2fcb5e3eb | -3.7693 | -54.8286 | 2025-08-29 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 33f72cf1-15a7-3054-9191-67bad3765f19 | -12.9961 | -56.9201 | 2025-08-29 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 547e767d-1f09-30ef-8b70-fe5bc6d55a44 | -13.1833 | -45.3098 | 2025-08-29 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| aac1e05d-2955-39b3-8162-fa11712bf23d | -13.558 | -46.8745 | 2025-08-29 00:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 161.4 |
| dd85a379-4c03-3325-9a65-ef337866de72 | -8.1944 | -61.3747 | 2025-08-29 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 4142ca1a-40da-38b7-b8ca-99ecd6084136 | -9.4432 | -60.5692 | 2025-08-29 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 8af88fd9-f797-30c9-8211-54ce75676bcd | -13.0154 | -56.8982 | 2025-08-29 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 6f71864e-12c7-377a-a5a3-bc6597f028ad | -13.2031 | -45.2834 | 2025-08-29 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 199.5 |
| 32268a30-896e-3aaa-b638-b9398446ab42 | -8.2867 | -61.409 | 2025-08-29 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| acb90fce-6397-30f7-8b5d-07e70c10158b | -12.4156 | -63.9183 | 2025-08-29 00:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 2ee46b0a-4e59-38a0-98e2-1133ca13e0a6 | -9.4452 | -47.6364 | 2025-08-29 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 783ce33e-55ff-3c74-8408-23274e7c0d78 | -13.5584 | -46.8517 | 2025-08-29 00:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 130.2 |
| f623b660-714c-3994-bd76-445f8c5a809c | -13.1837 | -45.2865 | 2025-08-29 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 290.3 |
| 091b8673-e9c1-3f28-a82d-69e87b195780 | -17.3435 | -42.6581 | 2025-08-29 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 904c15bb-048c-312c-bc25-77b70a308dd3 | -24.1648 | -49.5569 | 2025-08-29 00:10:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 268bb1fd-7074-327a-8fdc-bd10975b419b | -10.4551 | -57.9378 | 2025-08-29 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 3886a139-cdc3-35c5-ac88-94dd22fa2b77 | -10.3622 | -57.8456 | 2025-08-29 00:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 48e613bc-7591-3ad7-8c69-0b64cd56566e | -11.3517 | -43.566 | 2025-08-29 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 8d889e67-10ca-3a51-b0cb-0322691dc180 | -6.5358 | -43.9237 | 2025-08-29 00:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| e937d697-5609-31a8-9c4a-c2d68add7c89 | -9.462 | -60.549 | 2025-08-29 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 27864f7a-6e49-3b7b-98ef-0d22a724df23 | -10.3812 | -57.8245 | 2025-08-29 00:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 5adc1e94-ee07-3e01-b48a-605febe9b01c | -12.4534 | -63.9164 | 2025-08-29 00:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a585ea4a-27ab-36a9-a9ee-169abd2d3ad3 | -12.4345 | -63.9173 | 2025-08-29 00:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 182.1 |
| 2151c2cf-2ec9-3a6a-ba9a-63bc5b5b94b6 | -13.5386 | -46.8775 | 2025-08-29 00:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 85af7f29-cc4c-3c99-829e-1080ec698bfb | -10.8608 | -60.7998 | 2025-08-29 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| bfbf5877-f85e-30e2-a865-a12b6ae27c4e | -6.5546 | -43.9221 | 2025-08-29 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 183.9 |
| e6c92267-97c4-3126-baf6-fb45e9610456 | -8.176 | -61.3564 | 2025-08-29 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2a62f2a2-fd8d-37af-83a9-c16128f2e6f3 | -13.1842 | -45.2633 | 2025-08-29 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| c5268bbf-42dc-3a6a-ab64-134700b1d06f | -9.426 | -47.6605 | 2025-08-29 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d0dc7ed4-00ba-39de-8b82-7fde51c0babb | -18.1452 | -50.2549 | 2025-08-29 00:10:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| ec26bc7d-70bd-3dec-9f95-dc738e527f61 | -11.3325 | -43.5689 | 2025-08-29 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| dc136e7d-6f46-37e0-8acf-0b263e31e17f | -9.7731 | -64.228 | 2025-08-29 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 3da39f97-a9cf-3369-9881-970bef7330e7 | -11.5726 | -46.2617 | 2025-08-29 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 059d1f3f-2bec-309f-a879-d9a4ba0ba03e | -9.7916 | -64.2461 | 2025-08-29 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 180b3caa-bb47-38d5-ba7b-599293ba8cac | -10.381 | -57.8443 | 2025-08-29 00:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 80210033-2ba9-328b-aef0-cab4c28961e2 | -9.4433 | -60.5499 | 2025-08-29 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| d58afba9-63a2-33ec-bac8-17fef9f78e98 | -7.0569 | -44.3623 | 2025-08-29 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 23210091-7096-300a-8e73-f3c6c739a403 | -17.3636 | -42.6532 | 2025-08-29 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 81.3 |
| fd47adf9-faec-3faa-b8ac-70bd2befb94b | -12.4347 | -63.8983 | 2025-08-29 00:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| f7cf70ba-64c4-3f3f-8a9d-486879b3dc49 | -13.0151 | -56.9184 | 2025-08-29 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 6d9f2d65-238c-3a33-8e75-9673ded1c6f5 | -12.0976 | -44.717 | 2025-08-29 00:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 1cdf87a9-a0bd-3f44-bb21-f3827ffdbee1 | -22.6756 | -46.8439 | 2025-08-29 00:10:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.4 |
| 3be6677b-915c-39e4-9cc5-a5587a9a3923 | -5.6933 | -45.9667 | 2025-08-29 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| e63a2fe6-19d5-3eaa-b4b3-dfe48f25c77f | -9.2178 | -60.8689 | 2025-08-29 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| ca683066-7449-3228-b161-3ed21f427d85 | -13.0342 | -56.9166 | 2025-08-29 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 2a38c730-93cd-30bd-a5b9-e436a8eea9c7 | -3.4254 | -49.0517 | 2025-08-29 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5b925918-088d-30b9-b33e-933794648754 | -8.3052 | -61.4082 | 2025-08-29 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 935f5b3d-0d8d-3d12-96f1-b8d3ad2ffcd3 | -9.5424 | -65.7002 | 2025-08-29 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| e4dd22d4-9817-3d31-99c6-26e4483fdc75 | -9.773 | -64.2469 | 2025-08-29 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 29e6b25b-94ca-380e-a1bd-46655261829c | -18.1257 | -50.2363 | 2025-08-29 00:10:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 09f37e55-cb84-33cf-ada4-6844450a93b3 | -8.1758 | -61.3755 | 2025-08-29 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 896afa4f-a2b4-386a-a0b3-529ff0d53879 | -12.0784 | -44.7199 | 2025-08-29 00:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |


[Clique aqui para ver as próximas entradas](README2.md)
