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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62e8a0ee-0531-3135-bafb-19d9cc5fb12d | -7.6435 | -45.2609 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7099b075-700e-30b6-b612-fd01c014591f | -9.07365 | -60.42177 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e38982b7-a5bb-3108-909c-6bbb61a131e4 | -6.19685 | -53.51802 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ada413ac-2b9b-38f2-bc40-986bdf5e02ba | -11.97368 | -46.78161 | 2025-08-20 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a77e5b05-b9be-3bee-a00b-b2fc245ddb13 | -13.02658 | -46.80894 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a30e07eb-cd85-3e7b-80f9-f84487149de5 | -13.57638 | -47.02473 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b79ee55-bcc2-3226-bf6a-95746d4e8732 | -6.1902 | -53.51698 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ab1409ec-0bc2-3a6c-98b4-157e3a40baa1 | -7.39306 | -44.27491 | 2025-08-20 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 860bb641-5d0e-380a-a1ae-36c0fef09cfb | -11.12856 | -46.99179 | 2025-08-20 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f471e882-f20e-331c-aedd-23073507d188 | -14.16249 | -45.29046 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a81561cf-c2a0-3caf-90f7-315218446284 | -10.45773 | -64.4673 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 45a758f7-2c58-3036-88ef-470eb969f73a | -13.1759 | -46.89645 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 666adfbc-1969-3610-a0dc-412bdcc6ceb3 | -5.80356 | -59.22348 | 2025-08-20 04:57:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e79558ed-ccf4-3108-8ae5-ef3a9c101b14 | -7.22654 | -44.69876 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7c13269-c8b2-384b-baef-41c1e419ab59 | -8.96422 | -60.50151 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e997a3b2-c3aa-3063-b48b-41d1a4b2c9f7 | -9.17589 | -59.59375 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2bba130-3ba0-3eea-9472-77ef3045cf14 | -7.96804 | -55.29604 | 2025-08-20 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f5fa9d5-049d-3973-bb4f-6db201134de5 | -13.03174 | -46.80969 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b18d8c4-6a0b-39c8-9950-84e3a7fe3b61 | -7.22545 | -44.70648 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c8c443d-0829-338e-a0d3-89a3d32e351c | -12.91926 | -46.10302 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c6ad1b5-802f-30e4-bf35-960fb269fa48 | -7.53459 | -57.80399 | 2025-08-20 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cdb2f74-328f-3a6f-8011-3550bc0e871e | -8.2982 | -46.34705 | 2025-08-20 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c394e02-3b34-31a0-8790-79b77c590243 | -7.63962 | -45.28897 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9495f18f-10f8-33b6-b28e-d9134e24d5f6 | -13.14338 | -54.92735 | 2025-08-20 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b3ff773d-07eb-331f-a5dd-ef012661bed4 | -7.55213 | -63.85131 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00add0fa-fe43-3077-90fb-ae2f6ffa8433 | -8.29654 | -47.63039 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0d5bbc13-afaa-381a-83fa-0e00ad9702a8 | -13.58274 | -47.01591 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6516793b-ad5e-306d-add2-c4aeae1b8bf5 | -8.14401 | -49.51453 | 2025-08-20 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10438384-4470-35f5-a071-846aaa6e5a6a | -12.98843 | -45.20922 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fae75d8a-67f8-39e5-abd5-beeceda5bc6b | -13.5835 | -47.00968 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4919da4-9da6-3c15-b9c9-fa146aed3a5c | -12.99425 | -45.20991 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb82ea7b-6e63-3001-b92a-2cf2abb8d237 | -9.19644 | -59.63873 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5522c76d-ce81-3739-9e7b-d0df182f7746 | -6.92033 | -52.85579 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94375ef6-0a70-3685-90f4-c4d5006049c9 | -12.91968 | -46.0995 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a426e033-8158-3972-82ca-57d71d0a1c8b | -7.84462 | -45.10991 | 2025-08-20 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c69f1424-3965-3684-8c9c-d7bcc9bd037d | -6.1963 | -53.5215 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50cd097e-66d7-33d1-9e87-7fb6780cb494 | -12.89826 | -46.09222 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a42246dd-457f-34c3-9a4d-73239ec9a144 | -6.27662 | -53.68037 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 765df0f5-cc2f-3523-b080-3544c3566079 | -8.56707 | -66.95535 | 2025-08-20 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03f378ff-529b-3be1-8a24-03895f097aa4 | -11.18939 | -48.62133 | 2025-08-20 04:57:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ce98dbb7-4f5f-3843-af49-f58a1c86a44b | -12.98311 | -45.20432 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1877da9f-28a3-3f27-bbc2-2aba2eb54219 | -10.59804 | -48.59908 | 2025-08-20 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 741986d4-4b6b-3e48-ba5e-1f6547e71052 | -12.50865 | -57.78191 | 2025-08-20 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7193b0d4-56f2-33ee-af3e-f7bc83ffa967 | -13.02993 | -46.78199 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fae2d68-5e1a-3991-9f8a-104def54b1dd | -7.64104 | -45.27869 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c930fc0-e68a-3647-99de-c827c0ebcf48 | -13.33041 | -54.41354 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 99dc9052-2bfb-3fbe-9acc-9a78f4adb9a8 | -13.15172 | -54.9397 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08116163-a7ad-3191-9ad4-1e7a18f5e82b | -14.98767 | -54.81795 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5bd1764-de32-3bfc-8a7d-db75cdf4cdff | -14.61954 | -54.91895 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44a8f915-666b-374e-9915-ec3a4691d304 | -14.9989 | -54.81219 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bfe46568-33af-3fd0-8284-db41f98e325e | -15.87185 | -50.66257 | 2025-08-20 04:59:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af84f1f7-0cf7-3a4d-b470-e6a1aa321ff2 | -15.06217 | -54.8378 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e601eaa-fbc9-3072-b820-d1332b3af2e5 | -13.15115 | -54.92126 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7355a35c-fdd0-399b-a946-a674b78403df | -16.11511 | -46.82167 | 2025-08-20 04:59:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 611aa7ca-5ec3-3549-837a-259efa1fbf72 | -14.88722 | -48.08835 | 2025-08-20 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3deb233-2fb6-3045-a031-9e9f915e1c0a | -12.97766 | -56.88138 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f493353-aefe-3c04-a645-c01de42c02b8 | -12.97505 | -56.85497 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e756b9cf-5eda-39ce-be82-cadd4b0cfdb7 | -15.35225 | -49.61456 | 2025-08-20 04:59:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2db85725-5a90-3c9f-b5d4-f99d67b7ed12 | -14.46004 | -48.37416 | 2025-08-20 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8a7b0e2-3ed2-305e-8c7c-1e96a532e546 | -19.88489 | -49.83609 | 2025-08-20 04:59:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e9c5fb71-1c7b-3d59-afda-8c85c5708457 | -14.35929 | -52.00221 | 2025-08-20 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77a9ec79-3c10-3295-957e-4022a6fccb7c | -13.18062 | -54.95169 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbfc21f0-3af7-3804-a1fd-d7124c7b67cf | -13.34896 | -54.40517 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bfd49db-4dff-38f7-a78a-9abf1368e799 | -13.73675 | -52.01433 | 2025-08-20 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a69abe8a-d85b-3ae3-97c2-32b6c4bf7998 | -19.88019 | -49.83558 | 2025-08-20 04:59:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4079cfff-e316-31f7-bb90-a937b8dfabc4 | -13.15561 | -54.93666 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c3cbdc6-aa98-3c5f-94a6-043f43430817 | -13.14616 | -54.93147 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dcfaff22-62f4-3dbd-b74d-d5adb1e36578 | -19.44947 | -47.19588 | 2025-08-20 04:59:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07fb838b-d49e-3f18-b99c-a1975bb15d64 | -14.96042 | -50.12279 | 2025-08-20 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4731dab-265b-3ca2-ad31-a01c2445bccf | -14.99946 | -54.8085 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c318edd-1871-3d32-bd0e-e3fa1049210b | -14.99779 | -54.8196 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c579f5bf-ea41-3df7-a23f-65c8be98ca74 | -15.87656 | -50.65925 | 2025-08-20 04:59:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a877ddb-c497-351a-9c49-26e9b529fd18 | -14.64749 | -54.89341 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7b85df1-1e3f-3981-94b9-d3e41841d772 | -12.96836 | -56.85386 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ca97c82-cd11-32f2-85ac-a17378d39d41 | -13.14065 | -57.15485 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e752606-1be4-3947-aa8f-a170f664b836 | -15.02584 | -54.83959 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc7bdd61-67e6-3350-9f47-94077e49618e | -14.74828 | -56.02274 | 2025-08-20 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e07a4618-25c2-3ddc-a770-2b786ab05577 | -15.63865 | -56.29783 | 2025-08-20 04:59:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3043eea1-d5d7-3fe3-83f3-f694f00d666a | -15.42237 | -46.72112 | 2025-08-20 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45977fdb-9f6f-32d5-ab41-7adbb6a5ca86 | -14.61783 | -54.90744 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5aa73f95-51e3-3085-aef4-a984ad337b53 | -14.50138 | -45.95862 | 2025-08-20 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf014ace-2154-341c-b5a5-e325809c0f10 | -15.02641 | -54.83583 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80afe1e6-7be5-35b8-ba00-1b74e3d0266e | -14.50096 | -45.96243 | 2025-08-20 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8db77f6c-646d-3d9a-84cd-9a97c58de78f | -19.44987 | -47.19197 | 2025-08-20 04:59:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dac5dd68-706d-3cec-a14b-6ae9c4f2aace | -13.73641 | -52.01155 | 2025-08-20 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 43b37b4b-e8c6-3431-a505-1e82092906dd | -12.96778 | -56.85747 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4634e2a2-59f8-38bf-9a6e-6216bef756ae | -13.14894 | -54.93559 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0332d021-bfe3-39d5-803c-9620ecfd3df3 | -13.34952 | -54.40148 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 896ea766-5f0b-3e51-bf8a-21e795e6fa7d | -13.13669 | -57.15793 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba40ae82-7ddf-35ac-a1ae-da47776f69d1 | -13.34558 | -54.40464 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6685773-5b05-3595-b1e6-7ed94a764a4f | -18.17881 | -47.89735 | 2025-08-20 04:59:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d3a5d97-e0c1-3f2e-b1ca-3e79f7bab238 | -13.18562 | -54.96353 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71566e58-a29d-3222-a34c-4bcbed892b63 | -14.32202 | -51.99211 | 2025-08-20 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 329ef2c0-afb5-341c-b8a7-630874ecb9b0 | -14.61728 | -54.9111 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ad5537bb-8057-3ef9-a4e4-37c39cd73ac8 | -12.97723 | -56.86275 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a5d2d12-7b90-396f-b666-67e2cf33f873 | -15.55034 | -48.5656 | 2025-08-20 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab08a6d7-7c72-3734-a01b-826483d79009 | -14.89191 | -48.07602 | 2025-08-20 04:59:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb7d973e-5b8e-3586-aee3-64d9879d65af | -14.46069 | -48.36888 | 2025-08-20 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d23929e6-c481-3f60-af29-d3fb242104fc | -14.99667 | -54.82697 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f0692132-a1b5-3ace-a666-7a7ca4709658 | -13.03318 | -56.85011 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README50.md)
