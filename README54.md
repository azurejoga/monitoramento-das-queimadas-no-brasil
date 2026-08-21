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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 709d3ee4-e878-34cb-a237-deea02d6315b | -3.5406 | -48.1889 | 2026-08-21 05:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| efaf84c6-438a-3f97-8ca4-3a9dcb9dd01c | -11.175 | -54.001 | 2026-08-21 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 04dea98b-8dd3-3dc7-abe2-c1a2716b7162 | -9.4071 | -60.417 | 2026-08-21 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 396.8 |
| 288b588f-1e95-3141-ba57-96bd14bdcf7d | -13.4117 | -54.3737 | 2026-08-21 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 2ea9327f-b7a8-3a23-94ed-f4bd6e73b933 | -9.4072 | -60.3977 | 2026-08-21 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 3940825f-1c0c-367c-89d7-66fcd03137f8 | -9.4257 | -60.416 | 2026-08-21 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 6de4522d-65a4-3f62-9046-5cd97173e695 | -6.8939 | -59.4356 | 2026-08-21 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4c7cb1ac-873c-3a0b-8db1-3c475a423c2b | -6.8203 | -59.4001 | 2026-08-21 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| d9c0a665-9775-32cf-a234-91a57bce5765 | -6.2156 | -55.6118 | 2026-08-21 05:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 73751a72-d615-36de-9415-3cc3ede6d3ea | -3.5406 | -48.1889 | 2026-08-21 05:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| eaf87551-f612-3700-9c44-f0089030df91 | -6.2341 | -55.6109 | 2026-08-21 05:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 7349de29-6c86-33c3-94a8-bbc0019d0278 | -6.857 | -59.4371 | 2026-08-21 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 9434d940-67ec-3abc-965c-cb8b069810e5 | -7.3603 | -45.8136 | 2026-08-21 05:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 84440cde-4228-3b1f-9ed2-c319d18e77ea | -13.3737 | -54.3572 | 2026-08-21 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| dad63427-1696-33bb-9c9a-77df17c8b71a | -11.1747 | -54.0216 | 2026-08-21 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| a28794e6-03b0-3fc9-b26a-a0ca6c8be5f2 | -9.4259 | -60.3967 | 2026-08-21 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 410005cb-3520-3f95-a7bf-1d0f9e52c011 | -7.3791 | -45.8119 | 2026-08-21 05:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6f7a5c80-b38f-38c1-96d0-e2bc1b2e1ee1 | -13.3734 | -54.3779 | 2026-08-21 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| bfd7c134-2d00-3a7d-a1ba-45ec4ec442a9 | -6.8755 | -59.4364 | 2026-08-21 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 16e2efb0-e964-3f48-b5b8-4c3f10a4735b | -6.8388 | -59.3993 | 2026-08-21 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 8272bd48-793b-32be-80ae-a2ad9431fbeb | -13.3923 | -54.3965 | 2026-08-21 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| fa38a8f4-de1d-3c94-ab9f-4b39c61019c7 | -6.8756 | -59.4171 | 2026-08-21 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 5bf7de91-e06b-3d69-a7ac-f339908821e6 | -13.3926 | -54.3758 | 2026-08-21 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 255.2 |
| 50d75772-e587-365b-92dd-5bafe166448d | -9.4069 | -60.4362 | 2026-08-21 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f8423cad-f766-3594-a222-beb18a6c2849 | -13.3929 | -54.3551 | 2026-08-21 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 16800f87-fc43-3d36-98e0-716efe346fa4 | -3.5406 | -48.1889 | 2026-08-21 05:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 88a6df03-a1e4-3d8e-8c08-cca8c9695feb | -13.3929 | -54.3551 | 2026-08-21 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6cf2033a-523b-37a1-b4ed-c28289daea0f | -6.8203 | -59.4001 | 2026-08-21 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| ac6e9480-6908-302b-8442-ae44862b1038 | -13.3923 | -54.3965 | 2026-08-21 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 69a881ec-219e-3381-a873-64d09846cb74 | -9.4259 | -60.3967 | 2026-08-21 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 026b741d-9d3a-380a-8d85-4a3f0466043d | -6.857 | -59.4371 | 2026-08-21 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 66121283-b6ac-35c6-b1b2-c15caa60dc73 | -19.7238 | -57.966 | 2026-08-21 05:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.3 |
| ec001b15-ae1f-38ff-a704-9d8e0af6b350 | -6.8755 | -59.4364 | 2026-08-21 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| bc0bb3be-c417-3371-bd6a-41477e4509c8 | -13.4117 | -54.3737 | 2026-08-21 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d36f8a60-2ac8-30db-a7b3-5ca12a2a60f4 | -13.3734 | -54.3779 | 2026-08-21 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 136.0 |
| a1db2fba-61a6-3db6-950d-d817053ee37b | -7.3791 | -45.8119 | 2026-08-21 05:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 2feb9cd0-1db1-3a73-a5ad-779780d6ea38 | -14.3153 | -51.8756 | 2026-08-21 05:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| a4e81007-cdb7-32e7-a2d1-e3c542d11b6c | -7.3603 | -45.8136 | 2026-08-21 05:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 9139bd6f-2ac7-3084-b408-ae9e3051cf16 | -13.3731 | -54.3986 | 2026-08-21 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 8a760088-8a1c-37d6-aeb2-0a582efff756 | -9.4071 | -60.417 | 2026-08-21 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 372.6 |
| f270a22b-ef49-3759-ada5-1d2a0f0d081e | -9.4257 | -60.416 | 2026-08-21 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| b0ba9e47-bec2-377a-acbe-eaefc8c99e7c | -11.1747 | -54.0216 | 2026-08-21 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 2d4a97c9-e4a0-34f0-ae9e-1885ddb02c07 | -9.4069 | -60.4362 | 2026-08-21 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| d41f6b2c-69f8-38eb-af6f-8d427b162802 | -6.8388 | -59.3993 | 2026-08-21 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 8f84b878-8729-3441-8aec-e50b6af03f17 | -13.3926 | -54.3758 | 2026-08-21 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 265.5 |
| ae407101-7d32-3137-bc43-566549adcdeb | -8.3903 | -62.6963 | 2026-08-21 05:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 6670b748-d9c7-32cd-b704-7447deee8755 | -6.8756 | -59.4171 | 2026-08-21 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b692f833-4209-3031-b828-6fa5c6ec9085 | -8.3718 | -62.697 | 2026-08-21 05:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 97ec299d-11ac-3dbb-8c12-93fb080c0038 | -6.2341 | -55.6109 | 2026-08-21 05:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| f54abcdc-9ac1-35b1-8255-3ea8b898e140 | -9.4072 | -60.3977 | 2026-08-21 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 1eb5f404-6990-318c-8c56-13af6341c5a1 | -19.7438 | -57.9633 | 2026-08-21 05:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 4c852b4f-520a-3c7a-8db2-b738f169d94e | -14.3149 | -51.8969 | 2026-08-21 05:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2b75820f-2eb4-3140-93f3-246094d070bb | -3.96876 | -43.10411 | 2026-08-21 05:21:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87ba4ab9-dc19-32c0-812c-ae6ca646d664 | -3.03522 | -48.41077 | 2026-08-21 05:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2417dde5-0bcd-32ff-960f-e6ecbca40f45 | -1.09994 | -48.05724 | 2026-08-21 05:21:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea29856e-24d9-3efc-8c37-988492fc979b | -2.7661 | -48.57215 | 2026-08-21 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9e17f221-50e8-33b8-914e-7e7bf095161e | -3.03477 | -48.41374 | 2026-08-21 05:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8f65172-cc48-3701-ad11-80c42aab0d45 | -2.76585 | -48.57431 | 2026-08-21 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 678b50ec-9fc0-35e3-8b1b-a1df52dda3c4 | -2.76522 | -48.57777 | 2026-08-21 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2a966637-0bd5-3325-8af9-667725767b0d | -3.95892 | -43.10352 | 2026-08-21 05:21:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 256fbae2-f5a7-3a67-8180-3c2f17f96850 | -3.03985 | -48.41449 | 2026-08-21 05:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ecf8ca8-5a2b-39fa-8d27-159b566fa12f | -3.96509 | -43.11166 | 2026-08-21 05:21:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4cadd2db-b990-3711-92cf-4d7349d3a95a | -3.96777 | -43.1112 | 2026-08-21 05:21:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11fc21c6-0f21-3068-be69-5ff16079c380 | -3.96612 | -43.10458 | 2026-08-21 05:21:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d64a40b1-2834-3798-9a15-004bd36f29f6 | -2.47482 | -49.41312 | 2026-08-21 05:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| adb1d7dd-af06-3267-8012-6a2635c5d0d4 | -3.95789 | -43.11062 | 2026-08-21 05:21:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fcda5f0-807f-34c4-989f-744f1293f230 | -1.42098 | -55.72337 | 2026-08-21 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edd84599-7467-34c3-8c53-a5a0386fcafe | -2.87585 | -48.69003 | 2026-08-21 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29fa34a9-f8bc-3e0f-b394-be9b9617a005 | -2.78954 | -49.52271 | 2026-08-21 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39068754-9f76-3c54-a2ad-546b1af48c03 | -2.48421 | -49.41452 | 2026-08-21 05:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 47d9de8f-d6b7-38a3-a486-ae87b1a171b0 | -2.80068 | -49.41828 | 2026-08-21 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63f1bb69-d08f-33c6-a878-b49fe25d72b1 | -6.89001 | -59.42836 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 027448cb-abed-3153-997f-169c735359c6 | -14.50463 | -59.82203 | 2026-08-21 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c528ddce-ac2d-31c2-b842-1fd96a415906 | -8.53989 | -55.32033 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 959c259c-3def-374c-8da4-c6c3b35cbe93 | -14.33483 | -51.91228 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bff08082-b717-394e-ac27-ea381b7fc645 | -13.38768 | -54.37447 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cce4d08a-65dd-381f-8a57-2bd45748e18e | -7.05507 | -59.83575 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e7f9b9dd-fa02-3d86-982c-265c031ded17 | -6.80158 | -59.58243 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b94fbb70-90b8-3eb4-a198-277b39a03d7c | -6.83428 | -59.40406 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 95ad4a52-2d87-3a12-8353-72d77f617b5e | -6.87411 | -59.41816 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a91a1e8f-fe16-312a-8307-37314df57708 | -12.93039 | -56.62452 | 2026-08-21 05:23:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50f9064d-8c18-3b94-b0f9-d2531369591d | -6.87171 | -59.43296 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d26ac116-d4d6-3c79-967f-34ca30b2400f | -6.87975 | -59.42668 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0516420a-0793-33d4-8096-ae752e7df6db | -7.77751 | -61.15728 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f4639d9e-fb12-37f5-bd9b-485ba88a032b | -2.70895 | -54.76043 | 2026-08-21 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 985ab712-e7c3-39e5-8c9c-88b6cbd27a28 | -10.73087 | -44.78274 | 2026-08-21 05:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0464508b-abd7-3bd0-ae9d-2ab539b0d6c1 | -10.52559 | -50.78346 | 2026-08-21 05:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1571d8b4-1cf1-3a24-87e7-33f8bc37afeb | -8.54168 | -55.30832 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7862e8da-8218-3156-8350-398a9cfde81e | -8.39321 | -62.69907 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c57bcc73-b567-3078-b4ec-d3c56c8d03ac | -9.06554 | -60.44256 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ebcd3b5-b521-3cee-85b2-6ad5b835eade | -6.43506 | -52.71487 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 114c87a6-1484-30e2-b9c7-b6015d793bb5 | -6.3644 | -58.33313 | 2026-08-21 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9608461c-618e-36af-a4e1-7f6b67435487 | -6.91676 | -59.34931 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ebe6748-408c-3ade-ac73-0f6ce294142e | -15.71162 | -47.79609 | 2026-08-21 05:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52902a45-fc15-339a-8877-ead6f5efb582 | -13.66546 | -51.80014 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 204b9567-2740-3cfe-8b83-f05e2b52952f | -6.01005 | -57.79691 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7415ac48-8a9c-3f2c-93a1-4bf01cfd058a | -6.5749 | -58.9804 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c7347c4-bea2-3f67-9f18-42cfd9d593f2 | -6.88941 | -59.43206 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d276309b-1c4e-3135-903b-add1ad9eab53 | -4.45021 | -55.38904 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef14e370-e0e3-3596-b7b8-44150e2397e2 | -7.35337 | -45.81696 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README55.md)
