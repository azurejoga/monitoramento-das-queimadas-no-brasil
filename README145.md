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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16bcfbec-f931-3335-8671-2d1928c9a6e0 | -13.798 | -44.576 | 2024-10-10 10:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 375ee47d-95da-3063-9958-5f2d8e6eafc6 | -13.817 | -44.5961 | 2024-10-10 10:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 68862cc2-24ec-3f8a-808f-368f46e632f8 | -13.8374 | -44.5455 | 2024-10-10 10:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 67590a76-365e-3af5-8ddc-a9b89d5cee40 | -13.8179 | -44.549 | 2024-10-10 10:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 359.0 |
| c77d16ca-032b-3cdd-9741-e37163b6980c | -13.8175 | -44.5726 | 2024-10-10 10:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 277.9 |
| c05c46ba-9ed1-34fa-87df-6a03cc5ddd5d | -13.8374 | -44.5455 | 2024-10-10 10:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 252.7 |
| bc12aa77-f098-3586-af42-449b013c0100 | -13.8369 | -44.5691 | 2024-10-10 10:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 635f385e-2c63-3847-9fe9-67d903011b25 | -13.8179 | -44.549 | 2024-10-10 10:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 466.8 |
| ba1db357-6ce4-39d7-a4e2-0c2b87a01b52 | -13.8175 | -44.5726 | 2024-10-10 10:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 286.4 |
| 3a7b85de-2825-3b56-8fdd-c8c508e62d22 | -13.79 | -44.58 | 2024-10-10 11:04:06 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 399efdde-607e-3d6a-9ab1-08e22611d832 | -13.82 | -44.59 | 2024-10-10 11:04:06 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ad1b3e7-37d0-366e-8dfd-78b92a349289 | -13.82 | -44.54 | 2024-10-10 11:04:06 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be6b6f81-8e37-3e5e-a045-3bdf567d310b | -12.2893 | -43.7258 | 2024-10-10 11:06:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| b87084de-3f42-369c-b248-e33f004f72f8 | -12.9734 | -46.1931 | 2024-10-10 11:06:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 126ccedf-6440-31a0-9bba-f71c207a8b6b | -13.8175 | -44.5726 | 2024-10-10 11:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 222.7 |
| 7891f845-7faf-30fa-8a3b-26dae07066c4 | -13.8374 | -44.5455 | 2024-10-10 11:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 2b30fc1a-7486-3838-ace2-6ad20b0dd47d | -12.1892 | -50.6053 | 2024-10-10 11:16:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 253ae544-4d80-3d43-9e81-734f74fc150d | -13.8374 | -44.5455 | 2024-10-10 11:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 59980dba-f7ea-3fa6-8d40-191251c679e5 | -11.2894 | -51.0484 | 2024-10-10 11:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 2a3ac547-9eff-3659-8753-a459bf94bec7 | -12.2893 | -43.7258 | 2024-10-10 11:26:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 955a44ef-3763-3e2e-a16e-00ba65eaa6cf | -12.1892 | -50.6053 | 2024-10-10 11:26:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 3aefa2b3-9c6a-3b5c-94e2-1fa28dc347ef | -12.1895 | -50.5838 | 2024-10-10 11:26:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 47fc6b53-dcb5-3623-b041-53a59dbe4306 | -13.8374 | -44.5455 | 2024-10-10 11:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| a7f39a6a-9645-31c7-912c-78b70bddee9b | -10.3116 | -53.7085 | 2024-10-10 11:36:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| f82af1d1-b039-304b-ac1a-cc0f258463b0 | -11.2894 | -51.0484 | 2024-10-10 11:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 29205c1f-297e-3cb4-b5b6-af6335fec56f | -11.3084 | -51.0464 | 2024-10-10 11:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| d0fc7675-5e12-3c6f-8901-beff5b9ba730 | -12.2893 | -43.7258 | 2024-10-10 11:36:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 3fae7bae-9cbf-3194-ac31-3bd22cda4754 | -12.1895 | -50.5838 | 2024-10-10 11:36:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| da9f3115-9ebb-3ba3-a6f3-9d86f908418b | -13.8374 | -44.5455 | 2024-10-10 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| c440ab8d-3e65-3efd-97a3-ea29bec559d9 | -13.8175 | -44.5726 | 2024-10-10 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 255.8 |
| 46da49ad-dc34-3f66-9bea-968af09df647 | -13.8379 | -44.522 | 2024-10-10 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 99a9bf37-79e6-3d2e-9a38-4a70dfad098a | -10.3116 | -53.7085 | 2024-10-10 11:46:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 78e8f756-e581-359e-ae54-589e6d62a327 | -12.2893 | -43.7258 | 2024-10-10 11:46:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 2a969b10-b2cd-31aa-a365-51c6e0084c93 | -9.5659 | -44.4178 | 2024-10-10 11:56:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 4a07900c-4fb4-31f8-9f25-8172380818b2 | -9.5655 | -44.441 | 2024-10-10 11:56:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 8321bdb3-72e4-377a-9349-ffb8e38ccddc | -10.3116 | -53.7085 | 2024-10-10 11:56:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 6fa22b62-a94c-38fc-968a-fd2d771cff7a | -11.3087 | -51.0251 | 2024-10-10 11:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| abde1c7e-ef54-30a0-930b-42ab1adfbc50 | -11.2894 | -51.0484 | 2024-10-10 11:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| d1effd95-cb53-3879-af5a-3ee833f07234 | -11.3084 | -51.0464 | 2024-10-10 11:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 8ac88657-3016-3f62-a413-f9ce363dd8de | -12.1892 | -50.6053 | 2024-10-10 11:56:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ea58ba8d-253c-36e5-8ff0-61176a983928 | -13.8374 | -44.5455 | 2024-10-10 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 260.3 |
| ee2bcd6f-c650-355e-aead-144e28d37a2f | -13.8384 | -44.4984 | 2024-10-10 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 70aa06cf-160e-38d6-881d-f7cd1fbcea3a | -13.8379 | -44.522 | 2024-10-10 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 230.8 |
| 8d8fc87c-1009-31ea-b649-076dbc427867 | -13.8369 | -44.5691 | 2024-10-10 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 4d9ab639-e0e9-391c-bbfb-88d9c348f3ba | -13.8574 | -44.5185 | 2024-10-10 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 83962ce5-72e6-3d9b-a588-c07dc1dde18c | -13.82 | -44.54 | 2024-10-10 12:04:05 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8530ee0-5db6-3df1-b73e-427ccec72f58 | -9.9037 | -50.0845 | 2024-10-10 12:06:03 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 1bb95f2a-50c4-3e61-9ca4-9d3248d52e2a | -10.3116 | -53.7085 | 2024-10-10 12:06:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 153.4 |
| c87822f5-65df-3cf9-a130-b91ffb62f32d | -11.3084 | -51.0464 | 2024-10-10 12:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a9674d22-0648-3915-91a1-92f2a6c178db | -11.3087 | -51.0251 | 2024-10-10 12:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| a3eb7442-a22f-3c34-89b3-598391453d39 | -11.2894 | -51.0484 | 2024-10-10 12:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| e8152901-4cb9-3b02-98ae-19422392d7d8 | -12.1895 | -50.5838 | 2024-10-10 12:06:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 21f14524-5cfb-3324-a69a-68789dec67be | -12.2893 | -43.7258 | 2024-10-10 12:06:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| ca173573-ffa1-38fa-b8d8-d87d1a5d6903 | -13.8369 | -44.5691 | 2024-10-10 12:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| ff85283b-c855-3adf-8206-6a5439af7048 | -13.8379 | -44.522 | 2024-10-10 12:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| fab7e52d-afce-3251-9bf1-609b6a815d44 | -13.8374 | -44.5455 | 2024-10-10 12:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 179.6 |
| bff8d5b2-9b63-3c52-803e-ee1d7cfadf6f | -7.0786 | -59.4087 | 2024-10-10 12:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 5135960d-4087-398f-ba1f-46e318a4d6be | -9.5659 | -44.4178 | 2024-10-10 12:16:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 7ee404b1-fda5-36f1-adce-7c42018911f0 | -9.5655 | -44.441 | 2024-10-10 12:16:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 2df06f83-dacb-3fba-a874-e1ecac0f28a0 | -10.1447 | -46.3102 | 2024-10-10 12:16:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 71075b4e-2261-3bf1-89aa-b8597bd23995 | -10.2052 | -42.4504 | 2024-10-10 12:16:04 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 8f8eac5d-9d47-36f0-aafc-8c7292e17ae9 | -10.3116 | -53.7085 | 2024-10-10 12:16:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 169.2 |
| 3ce336e2-a9cf-3ef6-872c-78d34048afc3 | -10.6084 | -48.2995 | 2024-10-10 12:16:06 | GOES-16 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| c1f03fd2-8924-3719-adc2-39ddfa2e71d6 | -11.3087 | -51.0251 | 2024-10-10 12:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 151.1 |
| a345181c-5941-3d37-97fa-f9fa62110d91 | -11.2894 | -51.0484 | 2024-10-10 12:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 3824e081-0959-3502-9f4f-5e7930263edb | -11.3084 | -51.0464 | 2024-10-10 12:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 6d94842c-f487-3829-9724-31c392926885 | -11.3286 | -50.9592 | 2024-10-10 12:16:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 80748957-553b-312b-9ccd-ba2c3cd6a1ba | -12.2978 | -45.3112 | 2024-10-10 12:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 5ce9407a-1ee8-3547-8456-22be1edf20a0 | -12.3086 | -43.7227 | 2024-10-10 12:16:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| d6121b12-ddb0-367f-a729-5ce83afaffd6 | -13.8384 | -44.4984 | 2024-10-10 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 524ad8f1-c223-33eb-8cb2-c17ccb50820f | -13.8374 | -44.5455 | 2024-10-10 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 7cbd3df6-b470-378d-9a7d-7a9751d0b58e | -13.8574 | -44.5185 | 2024-10-10 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| c6e61efd-d901-3f10-a304-04f40021664d | -13.8569 | -44.5421 | 2024-10-10 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| ee41557f-60cc-3caa-964d-1ca08f936753 | -13.8379 | -44.522 | 2024-10-10 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| c5434646-9a13-364b-95a7-9250b6efdcb4 | -9.5659 | -44.4178 | 2024-10-10 12:26:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4ad88c2d-7157-3bf1-b722-6167ab242eb7 | -9.5655 | -44.441 | 2024-10-10 12:26:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 28a5cbf0-0c3a-3e17-855d-4c485dc8b578 | -10.2052 | -42.4504 | 2024-10-10 12:26:04 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 111.2 |
| e465d56f-3841-3351-8f61-17be2ce9f272 | -10.3116 | -53.7085 | 2024-10-10 12:26:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 193.6 |
| 4fc0b67c-c058-3ad6-8516-fce6fe6d3458 | -10.6084 | -48.2995 | 2024-10-10 12:26:06 | GOES-16 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 250c5f06-3fdf-39b8-bdc1-c9437c7fc362 | -11.309 | -51.0038 | 2024-10-10 12:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 60202b25-09ce-360d-beff-59ad017e316a | -11.29 | -51.0059 | 2024-10-10 12:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| f51b6b62-22b8-3281-9a16-f48d4caad2ab | -11.2894 | -51.0484 | 2024-10-10 12:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 3712066e-f28b-3d75-8b66-99ee0e37999a | -11.3084 | -51.0464 | 2024-10-10 12:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 139.9 |
| f653ee39-bc34-3451-952e-08743c021802 | -11.3087 | -51.0251 | 2024-10-10 12:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 280.8 |
| d7f2fe5b-910c-3715-a804-299592698f78 | -11.3286 | -50.9592 | 2024-10-10 12:26:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 941db36d-c233-3f7a-8f3e-3f03d3686cf4 | -12.2978 | -45.3112 | 2024-10-10 12:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 876a5670-a38b-3a22-bf72-306adf682283 | -12.1895 | -50.5838 | 2024-10-10 12:26:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| e9f57ecb-5c0d-342a-b318-819b1a2d1ab2 | -12.1892 | -50.6053 | 2024-10-10 12:26:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| c0e4c047-719e-3109-9f2d-21066a1ea218 | -12.9919 | -46.2359 | 2024-10-10 12:26:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 117.1 |
| b400f93b-6758-3300-93d2-b074d5243779 | -13.1276 | -51.6649 | 2024-10-10 12:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 7e0bad81-34f9-3b00-9fef-480a0b7866a3 | -13.8374 | -44.5455 | 2024-10-10 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 223.0 |
| 21cb480c-5946-3938-84c7-3676131719ab | -13.8574 | -44.5185 | 2024-10-10 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 7dda0a77-f91d-34ee-a11b-91132bf1b303 | -13.8569 | -44.5421 | 2024-10-10 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 5560e0c9-fda7-3905-8087-52cf54a477e2 | -13.8369 | -44.5691 | 2024-10-10 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 5c6b4d7d-5aaa-3f47-a2b7-26ba3eb8cbbf | -13.8379 | -44.522 | 2024-10-10 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 174.9 |
| ac6db330-554c-305e-8083-658854fd48a7 | -9.3067 | -45.3212 | 2024-10-10 12:35:59 | GOES-16 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 574f8d6f-d712-3841-8dfb-f517c39364f3 | -9.5659 | -44.4178 | 2024-10-10 12:36:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c25fd33f-15c3-3810-ad14-a1cc2f614bbe | -10.2052 | -42.4504 | 2024-10-10 12:36:04 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 128.7 |
| 881caf9a-f22a-303e-a3bb-69865efb21fb | -10.2243 | -42.4476 | 2024-10-10 12:36:04 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 94.8 |
| d4813b56-ac0b-3f1c-a415-e8c9de77d0d7 | -10.3116 | -53.7085 | 2024-10-10 12:36:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 179.9 |


[Clique aqui para ver as próximas entradas](README146.md)
