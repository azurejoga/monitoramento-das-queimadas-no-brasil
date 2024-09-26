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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b482764a-e265-3981-9042-874ff8553bed | -10.00672 | -48.8963 | 2024-09-26 04:57:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abb18b60-96dd-3b2c-89c1-e24c7207ef3b | -10.69298 | -47.96898 | 2024-09-26 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15a1544e-42f9-39bc-8434-1ed6428a5a24 | -10.68903 | -47.96319 | 2024-09-26 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b28aa975-c052-3076-9b52-4d2559a6b4ef | -10.6884 | -47.96798 | 2024-09-26 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a52aba4f-1dd2-3049-86d2-ad69fa4f86f1 | -10.53035 | -48.0667 | 2024-09-26 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8f5042f-1ee7-393e-be51-f5c01ccbd126 | -10.52984 | -48.07053 | 2024-09-26 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd8f6369-32a7-3ce3-9b91-38ba4c098fff | -10.52524 | -48.06993 | 2024-09-26 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e59eaae-2780-3316-beca-3cd4897dab97 | -10.52466 | -48.07299 | 2024-09-26 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bb8052c-2b80-3c14-8ee0-dc40d5cbadf4 | -10.52064 | -48.06932 | 2024-09-26 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44d98f12-d57b-3d1c-9390-c54bc0898a06 | -10.52063 | -48.06831 | 2024-09-26 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e67465a2-9122-3d98-bb60-bae7435e6ab5 | -10.52007 | -48.07236 | 2024-09-26 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b76ab875-cc9f-3a02-bd49-4ce8f422ce92 | -10.32888 | -47.82866 | 2024-09-26 04:57:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ece708d-2323-3d00-997a-92959614d2f8 | -10.32741 | -47.82934 | 2024-09-26 04:57:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94b70806-63a3-35c3-9789-8b4617b8a9ac | -3.70007 | -47.61621 | 2024-09-26 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 993db699-52f7-36e7-828f-46af3bc45842 | -3.32251 | -49.04256 | 2024-09-26 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 669c8396-e4f3-3b61-b6ca-91e2e87b8239 | -3.2168 | -48.92001 | 2024-09-26 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc0917a2-fa6a-342b-ac85-650281287b58 | -4.9469 | -49.24473 | 2024-09-26 04:57:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ed25956-873e-3ef7-8b98-afa14a106190 | -4.86844 | -48.384 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3bf40484-67ce-3d71-99c6-3cc123cac5a0 | -4.86621 | -48.65589 | 2024-09-26 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57e3fb36-de5c-3f02-9bb3-3b1cab6ef19a | -4.77306 | -49.20155 | 2024-09-26 04:57:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9baf3ff-cecb-36fa-ae2a-9a740378e76e | -4.66271 | -48.15412 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 5e4d514d-b946-31cc-aefa-95722cbd4a1a | -4.62998 | -48.53584 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dad32809-07eb-3fac-bea3-0597022ff960 | -4.61942 | -48.8316 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04c68a73-969b-3cd3-9a88-6a7e787db0e6 | -4.61891 | -48.83502 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da2e17e8-87b5-3c04-a3db-3418e2ce22b6 | -4.41863 | -48.11006 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc09a3e3-ea7a-3e9e-ac8a-6249f4cf1308 | -4.26747 | -48.22794 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a3fc5c4-c681-326d-91a3-40da5a8b2f97 | -4.26693 | -48.23158 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 770baf53-142e-39fb-9edd-ae2e806a6da2 | -4.21907 | -48.19495 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90dfc222-2163-37cd-aff3-9f9957e8b394 | -4.21851 | -48.19863 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aff4736-2293-3aa1-80e3-f04d63dc0ed3 | -4.20191 | -48.61473 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a40c3b84-963f-3cfe-9996-9198c16c1147 | -4.20139 | -48.61826 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91c9e6de-77fc-3c6f-94d4-76f11b634a78 | -4.20087 | -48.62178 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a140fcb-2a96-35df-b6b8-9cb570bd55a0 | -4.20036 | -48.62526 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5522c56-aa08-37ba-a3ed-1dd3af8719a4 | -4.19788 | -48.61419 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2401b4f-78ae-3b92-91c5-4856aa1c7956 | -4.19735 | -48.61773 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 817c771e-f433-3946-bb70-ddc1dda1ecb0 | -4.19683 | -48.62128 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc03c657-ad11-35f8-b119-c38b19de3e94 | -4.1928 | -48.62072 | 2024-09-26 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 615faafc-75fd-3b83-a63b-b5d485e06af8 | -4.05976 | -47.93605 | 2024-09-26 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbd7b520-7b9e-3165-8b23-e2eaa7190e9d | -3.80299 | -49.13693 | 2024-09-26 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4df1435-5f52-3f9f-8074-e41860db6f65 | -3.78494 | -47.6332 | 2024-09-26 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d4b2b53-ea35-3709-8446-0dc831ce81ca | -3.7224 | -47.72935 | 2024-09-26 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51474eaf-eeb7-3eb8-ac6a-92cd35536674 | -3.71816 | -47.7287 | 2024-09-26 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96c6532a-089a-33c0-88ab-18847e35d98e | -6.1564 | -49.48087 | 2024-09-26 04:57:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 273c69d6-8d3e-3591-8097-5ef7580edc3d | -5.88292 | -48.09308 | 2024-09-26 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fcb2f7f7-a804-3987-a99c-28117fba3348 | -5.88234 | -48.09719 | 2024-09-26 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 876326b8-af90-3c39-8352-a007ada67532 | -5.88176 | -48.10128 | 2024-09-26 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0837c21c-3c48-3d36-849f-6459829fb5cf | -5.87963 | -48.09436 | 2024-09-26 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 61dd8cbf-aad4-3324-9202-80e5cb1caa6b | -5.87901 | -48.09846 | 2024-09-26 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ddd5dcd8-da63-3834-ae2d-8780ffd9a5bf | -5.87866 | -48.09235 | 2024-09-26 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0329d938-93b1-382d-8d68-a3a0e4a89241 | -5.8784 | -48.10258 | 2024-09-26 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5d69b324-7987-34b3-bbbc-9638dd86386e | -5.87807 | -48.09646 | 2024-09-26 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 20a52bc4-fb99-3459-995e-4328df26b0aa | -5.87749 | -48.1006 | 2024-09-26 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 90d7e6fc-15d2-3b9d-adc4-6b323f432452 | -5.41253 | -49.08067 | 2024-09-26 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db2a836b-8793-3cd0-93b5-62dad9e55712 | -5.28499 | -48.83677 | 2024-09-26 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa010a86-1c9c-3b59-ae1f-b1e454e5b40b | -5.28446 | -48.84032 | 2024-09-26 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ed095f8-789d-30be-a31e-baced2e84faf | -5.28201 | -48.82904 | 2024-09-26 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f88568c-0c9b-3338-a067-09e752a10d32 | -5.2764 | -48.83911 | 2024-09-26 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d717d3f-0421-38e2-bf67-82b1c9a9cca8 | -5.25405 | -48.87906 | 2024-09-26 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69cd3dfa-e47d-3568-bcf2-f8e99b14ff36 | -5.22943 | -49.12859 | 2024-09-26 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93542c46-5f28-3a71-a476-fe4db4ce7a7f | -5.21911 | -47.96642 | 2024-09-26 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a33be86-36d6-3e39-8a5b-e77cfea39a96 | -5.21391 | -49.26016 | 2024-09-26 04:57:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ac0257f-a3a3-36c9-98a5-7691c45c2651 | -5.19128 | -48.98437 | 2024-09-26 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 593db885-0aa3-3751-a202-1be95e974c41 | -9.32164 | -49.41023 | 2024-09-26 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a088fb0-34a6-3633-8e9c-de1b7544d16c | -8.94329 | -49.7298 | 2024-09-26 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4f9d9a3-94b5-3a6f-9846-9f829953f05c | -8.91871 | -49.70094 | 2024-09-26 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66a338a8-7467-3cd7-b226-52b952c52fee | -8.79012 | -49.6426 | 2024-09-26 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d4ee0de-172a-3950-bf79-73b225a07ac2 | -8.78873 | -49.64232 | 2024-09-26 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6e5c728-d112-3803-9c16-2fe819fe3d4d | -9.95554 | -50.10384 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3197a39-de2b-3ea5-9b78-b8383222bd09 | -9.95157 | -50.10326 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1df35073-47dd-37fb-8a91-24c582c20395 | -9.95084 | -50.10843 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e53db161-5e11-33fb-81cf-fd8054bce8bf | -9.94753 | -50.16065 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4969559-56c5-32bb-a952-c2b936bf859e | -9.89822 | -50.13756 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48172f84-add4-3a5f-b5d2-2b832f0052dd | -9.8955 | -50.13578 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9521b375-a947-3ed2-a7f7-9a0e9d1f756e | -9.8824 | -50.17052 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2d92a071-7586-37d0-8228-ef8413b3933a | -9.88167 | -50.17562 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7abeee5d-bf24-3839-b8fb-6e29741161b7 | -9.76309 | -50.43751 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42078c79-c4fb-3143-b5a2-c4b2380d71fd | -9.60421 | -50.15178 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfce5154-e230-3576-8fb5-9e6909f25cef | -9.60098 | -50.14609 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f03dac9-6b91-39cc-9e82-c82981dcf5f5 | -9.60027 | -50.15119 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d73c12fd-68ff-3159-9321-6ca7e3a4af07 | -9.59955 | -50.15628 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ccc6353a-ea4f-390c-a860-c8cf580ee6cf | -9.59704 | -50.14552 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6628a469-2f18-337c-9d88-d1c84d28bac2 | -9.59633 | -50.1506 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7abc936c-efab-379e-86ba-868c688a0d42 | -9.59561 | -50.15569 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6b85f72e-479e-363f-a961-7f9cfcf052ee | -9.59239 | -50.15001 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c4db6bb-5bf9-39ed-8ff4-f77bc064e7a9 | -9.55405 | -50.19478 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b05d5847-d78c-35e5-a0e2-399a3318d3b5 | -9.55332 | -50.19983 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2e1ab63-73ef-3dab-a247-15ae950bee31 | -9.55259 | -50.20487 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97c88a4c-1211-33d1-9fac-3cdf17127195 | -9.55086 | -50.18914 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 005ec944-70db-3ff9-a390-cf10b93789a1 | -9.55013 | -50.1942 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83653250-4339-3d50-8777-0b80d0581fcf | -9.54867 | -50.20429 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3b2b2ff-9a6c-3a25-9109-0ebf7ce45666 | -9.54766 | -50.18351 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0a3736b-378a-390f-9740-c35bc355b692 | -9.54693 | -50.18857 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c96b6b14-8d53-3e02-83bf-c0626346226b | -9.51159 | -50.1833 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cb1f13f-4ceb-30d3-8307-2e2c67f098c6 | -9.40437 | -50.03479 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| efae733e-238b-3a2a-96c7-dc66f4b7b146 | -9.40041 | -50.03421 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| aab29ca9-ee5c-3a3f-b851-0076150847c3 | -9.39645 | -50.03363 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d427a32e-dbe2-31f0-9463-42d6e251ca2f | -9.3925 | -50.03304 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b58fdd0c-0f61-3916-b096-7b81f4a52087 | -9.38948 | -50.03144 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fce8fea-3adc-3672-a780-9ca91444d34b | -9.38926 | -50.0273 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91522a23-16cc-360c-8f59-39324870d1a9 | -10.19193 | -49.96044 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README91.md)
