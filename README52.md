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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8e5cc7b-2386-345a-9ff0-420b3397b000 | -12.44762 | -50.80146 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1795607a-e65f-38f8-b756-da38e716d9a9 | -12.47022 | -50.8087 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb28b314-3288-3ade-9d51-cabfc86d27a0 | -12.45816 | -50.86444 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49f31853-6fe7-3110-b3da-434d3cedc973 | -12.46696 | -50.85143 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3cf7ef5-2a4b-3d63-be73-b2725b12fa54 | -15.47322 | -53.78271 | 2026-09-17 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce211da3-d314-381b-b826-a349c9147064 | -14.23673 | -48.63292 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bb7d9674-52a5-3607-9e2a-c47825549786 | -12.49056 | -50.76508 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d92c17cc-2590-370a-9075-a1357ebbda32 | -15.47945 | -53.78775 | 2026-09-17 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da8a772a-f284-3501-9ece-ee519c4d7f6f | -12.45097 | -50.84526 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19699122-ae3f-3cbc-af48-4e9120b5a7b4 | -12.46801 | -50.80113 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 991225a3-c004-3493-841f-f23adc673b94 | -12.43944 | -48.48784 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1760e35-de71-3d1f-8f18-069029e404ac | -12.99281 | -46.93413 | 2026-09-17 04:42:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5ebb29db-2da9-3ecd-82ae-eec07d690ab1 | -12.44212 | -50.81501 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f51e6f57-4e98-3f00-b7af-8da76dbae56c | -14.39389 | -47.27801 | 2026-09-17 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c21fa250-53e4-36f0-9116-ab0f039ef972 | -12.47623 | -50.77 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b183ac9-36fd-3d0e-b5c3-901f7ee304d1 | -12.45264 | -50.85634 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e78c5b0-065b-33e7-8584-09c434da4249 | -14.55353 | -39.64 | 2026-09-17 04:42:00 | NOAA-21 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e54903e0-dc2c-30b4-b52e-84d2186ee64f | -15.84228 | -56.19306 | 2026-09-17 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d16bd6f4-86a8-30cb-9dd7-bc5c5abac79e | -14.13543 | -44.0119 | 2026-09-17 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4fc23f93-537c-32e1-81eb-91b339965903 | -12.45535 | -50.81713 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c26509f7-299f-3c3a-a9db-e7f422524e92 | -12.44928 | -50.81255 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aae7e003-4759-346c-a528-6b22f6d7ab5a | -12.47019 | -50.78705 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 032f1221-dd13-3967-a442-9a4cecc9aa4f | -12.64392 | -54.7068 | 2026-09-17 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7193f247-298a-32f0-b8d4-b598ce40e535 | -12.44822 | -50.84121 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 044d9964-69ce-3aa4-9d2d-cbdb0c788d2b | -12.10919 | -57.19554 | 2026-09-17 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d2fd092-e701-30b8-bad7-b382a79f3308 | -12.11352 | -57.19629 | 2026-09-17 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af780a87-a3bc-348b-a21a-aeeb6bedc595 | -12.44434 | -50.82257 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 41846059-d3a4-35ae-b6c3-a6c494c7a08c | -15.48909 | -53.79343 | 2026-09-17 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8a7243ec-4954-381d-a9be-d6abb6929f02 | -12.44657 | -50.85176 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5fe1b3e-3428-3641-bd9a-0e73e3010470 | -15.64318 | -52.7353 | 2026-09-17 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61ae536c-a42e-351c-97bf-fff18f8e403e | -12.4642 | -50.84739 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 903c4053-491f-36a8-8ad4-274d2e3785f2 | -12.10485 | -57.19481 | 2026-09-17 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eec5a242-dbb6-3264-8c2a-5a516c67fa62 | -13.19979 | -47.02924 | 2026-09-17 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d931b18-bc27-3a3d-8573-356667f730e3 | -12.47136 | -50.84493 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6f3a6e1-d976-3583-a277-32e55f72af5d | -14.82561 | -59.5539 | 2026-09-17 04:42:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 712ac949-4e19-3b89-9f1f-59f5aef9284e | -12.4586 | -50.77437 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96607d8f-a4db-3e90-9322-eca167c1c4d3 | -12.44103 | -50.82204 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de2302d9-fbc4-313b-a2e7-efcf2968c3b3 | -14.17789 | -47.07929 | 2026-09-17 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a53eab2-2bfd-3ad7-8fb3-9f4246422085 | -12.87483 | -48.45315 | 2026-09-17 04:42:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3245709-e29c-3799-bf77-ae541b0e66ea | -14.14485 | -48.74448 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 30c26882-309a-3bf8-ba81-eabe4960eab6 | -13.39496 | -57.02037 | 2026-09-17 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 349a39ad-8e79-3c89-b126-d82124a40eaf | -14.08851 | -46.99974 | 2026-09-17 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15a8563b-cf5c-360d-b538-34b076c7bf4e | -16.09538 | -45.1324 | 2026-09-17 04:42:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6346d92c-3895-363c-ae77-45d3ef4a5587 | -16.99779 | -45.46824 | 2026-09-17 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4a75127e-84c1-3ce6-aac3-6c2f7a3a8763 | -16.30912 | -53.8514 | 2026-09-17 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1358aab5-e80a-3d01-a336-fd64b0db430c | -12.48118 | -50.75997 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d789a47d-4ca9-3031-96ec-798f5321740a | -12.47183 | -50.7765 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f889621e-9942-34c0-b6d4-105494166d5b | -12.20299 | -52.87058 | 2026-09-17 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cddb5829-d690-3fbc-97bb-b597d1197a53 | -12.45754 | -50.80305 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7a82220-259f-3cd7-acf8-b308bc0fec51 | -12.4647 | -50.80059 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8d47282f-975f-3ad6-a69d-b390d822d34b | -14.14955 | -48.76162 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 20b06b64-342a-30fd-b15c-a4f16fb164ec | -12.40507 | -48.47858 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4f4023e-31ea-3043-ac6a-74c9a9cf7a9c | -15.62692 | -52.75127 | 2026-09-17 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf75663a-68e8-396b-9fa3-8efc41c6f8c4 | -15.65476 | -50.92057 | 2026-09-17 04:42:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 447517b7-210e-31f1-9242-f084303bcb01 | -12.87132 | -48.45257 | 2026-09-17 04:42:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 597c07ea-a7bf-3d2b-8b14-b853bb5ef099 | -13.60178 | -46.94941 | 2026-09-17 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0da22fac-648f-3677-b590-95940f3902fe | -12.44931 | -50.83418 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fd198c3-452e-3ac5-888f-dc9df39e436f | -12.48558 | -50.82175 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38d8a7a8-636e-318d-88bc-ff40baa94180 | -12.95571 | -48.61825 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43260f65-a7c2-3bc6-9068-374187f4cbf3 | -12.48176 | -50.77809 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a732da91-2053-3d97-9163-d938c8957ca7 | -12.45368 | -50.80604 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b093734c-1765-3be1-b7f7-adc9e21d8b8e | -15.48287 | -53.78836 | 2026-09-17 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8cbd00a-5130-35c8-9c4c-44c9545578d6 | -12.45923 | -50.83577 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7811e053-78f0-37bb-9e6c-eda446a50e55 | -12.45863 | -50.79601 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04448c4e-33d8-3afe-94ad-ef8d69d9f06c | -14.18038 | -45.14834 | 2026-09-17 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d377c00a-8c19-32ac-ba80-7e3c6de3d5d7 | -14.2254 | -48.5122 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 17225575-7c6f-367f-aa25-e0c63131117a | -12.44824 | -50.86284 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3c85c6e-8fcf-3ebc-a2ae-5caf785401d2 | -12.46805 | -50.8444 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f7de4ab-d18f-376a-a6b3-637ec6d5304a | -14.56098 | -39.62961 | 2026-09-17 04:42:00 | NOAA-21 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f034e154-bb74-3953-a949-0c0381b20543 | -12.48339 | -50.76754 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb048af1-b727-3e82-b038-5c9a51229ad0 | -14.22896 | -48.51266 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a380134c-e237-3974-8343-980378d8991e | -13.74227 | -39.01904 | 2026-09-17 04:42:00 | NOAA-21 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f7732de0-5a22-3823-89c4-7b3a2ec1634f | -15.64434 | -52.72803 | 2026-09-17 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4295e35-63f6-3d74-86ab-bc0b5a4b3b28 | -13.29905 | -51.275 | 2026-09-17 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fdbe4cac-25a4-306d-ad5a-d85894aabd6b | -12.46967 | -50.81221 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 748ef95a-ad8d-38a8-a982-9a2f88bfbbdf | -12.49219 | -50.82281 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 326bbebe-054e-313b-963a-c8f42bd015f2 | -12.45478 | -50.799 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68609d26-cadc-3449-860a-2489f7bec94e | -14.13196 | -48.73425 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62660ca0-f713-3d40-9e70-3d33fba00991 | -12.46467 | -50.77895 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 99c6cd6a-0191-38ce-9418-291cfdb533c7 | -12.44879 | -50.85932 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fed481cf-8500-34e8-a02b-4f1aeaf030e6 | -12.46743 | -50.783 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b57da6e0-e2e0-3fd6-ba42-f6f779baba3e | -14.16124 | -48.75525 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e3dff175-29f8-3f9c-92fd-ff2937392602 | -12.44436 | -50.8442 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66501d68-8946-389c-a4fa-86d2ddc73d1d | -12.48126 | -50.8249 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34175f0a-b7c4-3f17-948f-e44cf255a28f | -18.03015 | -50.95153 | 2026-09-17 04:42:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6568e214-e569-382d-b4fd-3a2466bf8d72 | -12.46584 | -50.83683 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 398e003d-29c6-3854-91db-ed97cbcf2aa8 | -12.46641 | -50.85495 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf575efc-5ed3-3d91-9887-2784152ae983 | -12.45152 | -50.84174 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74ee1e37-aa8a-3ec4-8b5e-5cfe0ad0edee | -12.48009 | -50.76701 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 58cc4f20-8230-3e0b-96f2-3f522cafbde3 | -14.56722 | -39.6306 | 2026-09-17 04:42:00 | NOAA-21 | COARACI | BAHIA | Brasil | 2908002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 561898f7-3cf6-3317-93fe-cd0d8b66a5b0 | -12.46915 | -50.83737 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38ec913a-c7b7-36cb-8d4e-898313fa9b29 | -12.408 | -48.48302 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| daf77fb7-100e-3dd9-bc38-d078db46a280 | -13.74284 | -39.0136 | 2026-09-17 04:42:00 | NOAA-21 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 86532ab4-1009-325c-930d-aa29519c3d5c | -15.64072 | -53.811 | 2026-09-17 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea0b1c6e-26bf-3142-917f-fe094ceecbb6 | -12.45866 | -50.81766 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2db09444-2314-3651-bb28-415d5ef0aa8d | -12.46636 | -50.81169 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f89728f8-23ea-3232-8552-0264b72afc01 | -14.18257 | -45.13105 | 2026-09-17 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce6d69d9-cd1f-3b19-9068-4d1391fdacaf | -12.46525 | -50.79708 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fb6953ca-e7ce-32ca-8202-1522dc587880 | -12.40451 | -48.48247 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ba79ee8-cb53-327a-a1fc-adab8dbf13bb | -12.45699 | -50.80657 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README53.md)
