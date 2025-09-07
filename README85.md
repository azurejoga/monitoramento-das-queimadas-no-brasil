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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d1ebba1-3f76-310b-a05c-9b7605d92092 | -11.264 | -46.4617 | 2025-09-07 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 353.9 |
| a55c3648-48f8-3a08-aec4-4b5386cff432 | -5.9899 | -44.1528 | 2025-09-07 12:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 160.5 |
| cbf968d2-ef11-32c8-a472-36b104ef547f | -12.948 | -54.7724 | 2025-09-07 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c38fbd0a-6ada-3793-ae57-7787dc504ae8 | -11.586 | -47.7613 | 2025-09-07 12:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| e39518a8-2758-3cca-873e-98e37e903db0 | -11.5669 | -47.7638 | 2025-09-07 12:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 3fab7cc5-3d77-3819-a1aa-832504827b85 | -5.8216 | -44.1196 | 2025-09-07 12:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 18df3df0-43b4-342c-866e-7504f18517ba | -10.4632 | -53.6132 | 2025-09-07 12:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| d7d30b0d-d03c-31da-b335-7410e5818ec5 | -11.586 | -47.7613 | 2025-09-07 12:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| c83cf0f1-89fb-3e30-8773-c94bcfc54c90 | -9.1834 | -46.0377 | 2025-09-07 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| edd9acc2-f6dc-398a-942e-00a46c35e414 | -9.0954 | -46.9871 | 2025-09-07 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 26c31f8f-b4ae-3092-8640-985b62fc4bb2 | -8.161 | -44.875 | 2025-09-07 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 52774a0a-826a-3647-96ff-97b7f70a2410 | -11.4093 | -43.5573 | 2025-09-07 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 9fbc1040-b9b2-3077-8b8e-ee1b7ab428b5 | -11.2636 | -46.4843 | 2025-09-07 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a5e6f985-230f-30b6-a88d-7dedc7fef58f | -9.6115 | -47.9049 | 2025-09-07 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 1eeade57-2cc4-3662-8a4d-93d8ba2b8120 | -5.9711 | -44.1542 | 2025-09-07 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| d8b4283b-708f-376d-b3cb-2545933dcf99 | -14.1946 | -53.3483 | 2025-09-07 12:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f38704f6-1a44-33f5-9490-ebe6af9d4ac6 | -6.192 | -42.6442 | 2025-09-07 12:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 866cd71e-9596-3db5-baf2-33c03d123fd5 | -13.9153 | -54.007 | 2025-09-07 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| cdbad2f3-d1fa-3164-b306-04e7fa19c4af | -6.1923 | -42.6205 | 2025-09-07 12:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 29922647-57ec-3adb-bf59-075c7009fe1f | -5.8216 | -44.1196 | 2025-09-07 12:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| cd0979be-6d0c-3572-923f-1c5703f9444f | -12.8248 | -48.0155 | 2025-09-07 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 3dcd8697-a1ee-3f11-a767-9411b86639d5 | -13.0542 | -48.0716 | 2025-09-07 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| eca388dd-6f30-3257-904d-5f6d5aa44501 | -12.7641 | -52.9498 | 2025-09-07 12:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 14c70213-8728-34ba-a6a8-3e0b6732df41 | -11.5669 | -47.7638 | 2025-09-07 12:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 28ff47ba-dbb6-3b15-9746-f6e3919e9849 | -15.0639 | -50.087 | 2025-09-07 12:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 1341fb24-b9cf-3d21-9770-cb48e841e8c0 | -8.1421 | -44.8769 | 2025-09-07 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 00f8c97a-2b72-3212-b92f-8d07c0c63157 | -13.9342 | -54.0256 | 2025-09-07 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d42ef0aa-19fa-3137-91ca-7fdddd497188 | -6.2108 | -42.6426 | 2025-09-07 12:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 44ea6a12-6273-39dd-b959-7bb07c2185f2 | -11.1575 | -48.3883 | 2025-09-07 12:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3b131d6e-0213-3937-91b2-3f0f7256f57c | -12.948 | -54.7724 | 2025-09-07 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8e79d333-c0b2-3f06-a319-abe01c0ca93b | -5.9899 | -44.1528 | 2025-09-07 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 153.7 |
| ca61f802-b3ea-392a-a91a-fe063318bc6f | -12.3016 | -47.2416 | 2025-09-07 12:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 36f0a768-c97a-36b3-923a-7a199932c2ee | -12.8252 | -47.9932 | 2025-09-07 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 664160c2-1859-3c74-b93b-9cc831c84117 | -11.264 | -46.4617 | 2025-09-07 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 0db523db-234f-3385-bef1-c80f2112444b | -11.5669 | -47.7638 | 2025-09-07 12:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 6ff0d029-7b91-3e18-a934-0f2b8e351673 | -6.192 | -42.6442 | 2025-09-07 12:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| b2f80061-f56c-3d98-bef7-c636ad53dd95 | -6.2315 | -42.4515 | 2025-09-07 12:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 148.8 |
| f46599a1-c212-34b5-a313-22320f32c6bc | -12.2824 | -47.2443 | 2025-09-07 12:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ff48de60-5ce8-37a6-a5aa-36d49a662062 | -11.264 | -46.4617 | 2025-09-07 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 9f1bc644-6efc-3cba-ac52-4217b830c276 | -12.8248 | -48.0155 | 2025-09-07 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| a0f79980-41bf-3dda-ae4f-df1d3dadf2c8 | -5.9899 | -44.1528 | 2025-09-07 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 227.9 |
| bf9783ee-99bb-3fa9-a26f-347f6ce86b0f | -8.1421 | -44.8769 | 2025-09-07 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 1d1c540c-bd56-3635-8d54-b39b86e841bc | -8.161 | -44.875 | 2025-09-07 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 290.9 |
| 81c37cf7-d09c-3d13-b9e7-a592132448bf | -12.8055 | -48.0182 | 2025-09-07 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5411d8ab-8ca3-3c0a-9887-256b5e638165 | -6.0086 | -44.1513 | 2025-09-07 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 313f6fa8-a627-3908-8983-fc19fac7e182 | -6.1923 | -42.6205 | 2025-09-07 12:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| a64c728c-488e-34f0-87cd-46e907739164 | -12.8059 | -47.9959 | 2025-09-07 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d09c9339-68c9-3d89-b29f-39141bebb709 | -11.1575 | -48.3883 | 2025-09-07 12:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 503f4243-9d5a-3c8c-932d-85e63e9e45fe | -12.744 | -45.103 | 2025-09-07 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 6aba5f02-2d32-3d37-a6d0-e5e56f9c47e3 | -12.3016 | -47.2416 | 2025-09-07 12:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 24fd4d76-eb3e-3216-a86e-c0839d987d0d | -5.8403 | -44.1181 | 2025-09-07 12:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 2ebde7e0-931a-37f3-a924-4f7e27d725bd | -13.2404 | -51.7997 | 2025-09-07 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 2294dfc5-a7e8-3897-ad8a-90aa41b4d249 | -13.8606 | -46.2337 | 2025-09-07 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 19429fd0-7032-3791-bde5-345bbbc3cb09 | -13.896 | -54.0092 | 2025-09-07 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 31f24b4a-bcd7-3486-bc2a-7c26537d5e21 | -6.3991 | -44.4648 | 2025-09-07 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 2652f18f-b9f5-3998-8134-734679514ae4 | -5.9711 | -44.1542 | 2025-09-07 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 66176192-c7ac-3ebc-93c4-554d130af65d | -6.2127 | -42.4532 | 2025-09-07 12:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 222.6 |
| c74a305a-214c-31d2-a6df-d7fb84000eeb | -6.2108 | -42.6426 | 2025-09-07 12:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 12b4676e-5211-3d78-9260-422c42fa13fe | -11.5672 | -47.7416 | 2025-09-07 12:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| f46e90a2-3069-32f3-96b6-d77736928ede | -14.1946 | -53.3483 | 2025-09-07 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 1213d31e-a18a-3548-853a-accd7cf91e70 | -11.586 | -47.7613 | 2025-09-07 12:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 963237fc-8c47-3851-abd8-a8388ab45a42 | -10.5869 | -48.4772 | 2025-09-07 12:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 49b08383-4af6-353b-b0e3-98ecc6ecaac9 | -12.7832 | -52.9477 | 2025-09-07 12:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| e316cebf-80be-3217-bfeb-87248f9c9050 | -19.4898 | -47.7646 | 2025-09-07 12:40:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 6e33dd54-e051-3bc5-ae20-667744376846 | -14.4882 | -48.7671 | 2025-09-07 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 212.4 |
| fbf51775-88a8-3481-bb8f-27125796691a | -11.2636 | -46.4843 | 2025-09-07 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| a2225541-59d8-332c-bdc7-688f1615854d | -14.5076 | -48.7641 | 2025-09-07 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 157.6 |
| a0bc3324-2cab-3e29-bdd4-6b36ed6921af | -5.8216 | -44.1196 | 2025-09-07 12:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 5541fb3e-3a6b-34b8-ac05-56a9453d6916 | -6.2125 | -42.4769 | 2025-09-07 12:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 114.1 |
| 8e8b8b5f-b7fa-308c-9031-5f696db8f8a3 | -13.0542 | -48.0716 | 2025-09-07 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2ff32939-5b90-31e6-a351-ff2bbc7e7393 | -13.9153 | -54.007 | 2025-09-07 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2925f70f-c91f-3d55-841a-ee94efcfcd3e | -5.9901 | -44.1297 | 2025-09-07 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 085822b2-2826-33c0-a05b-540f0266d542 | -12.7641 | -52.9498 | 2025-09-07 12:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 173.9 |
| a9411e84-6f0d-3bf3-abe9-557c2acdb3fc | -15.0639 | -50.087 | 2025-09-07 12:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 7b3075d1-86a1-3472-874a-70fae8f1f14f | -13.0349 | -48.0744 | 2025-09-07 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 8ca0b603-0658-3c3d-9b0f-ceb67d60c7a6 | -19.4891 | -47.7879 | 2025-09-07 12:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 50cb98dd-96fd-3714-b81c-f2cbc8ceb320 | -12.8252 | -47.9932 | 2025-09-07 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 400ed71b-57cc-39f1-adc0-e8fe7c533664 | -12.9289 | -54.7744 | 2025-09-07 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9b7b7095-4916-3892-a071-f390692423e8 | -5.9901 | -44.1297 | 2025-09-07 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 57a0bb45-165a-38a2-8c52-10ed5be66faa | -6.2108 | -42.6426 | 2025-09-07 12:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| b0f27b90-937a-3ca0-88ca-83031d11539b | -12.948 | -54.7724 | 2025-09-07 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| fa81d064-2cd4-3163-99f1-8e408771cd07 | -5.869 | -45.0986 | 2025-09-07 12:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ffca37f7-5b34-3c13-96a4-7a96fa9acb1e | -6.192 | -42.6442 | 2025-09-07 12:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 120.1 |
| 4c2c5253-2865-3f89-a5f8-5b134c6400bc | -13.8606 | -46.2337 | 2025-09-07 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 6956f1c1-358b-38ec-abd5-c88aad9cdfec | -11.1575 | -48.3883 | 2025-09-07 12:50:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 6f0d463b-844d-3281-81c1-99530d127b20 | -7.8154 | -45.4329 | 2025-09-07 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 575ee17e-6b28-32cc-bf5d-f849d789b52e | -12.8248 | -48.0155 | 2025-09-07 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 548d4751-43ae-3aad-b1ca-49d91ca841b1 | -12.9477 | -54.793 | 2025-09-07 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 6419c258-a27a-3614-933b-7085ce5217a6 | -14.4882 | -48.7671 | 2025-09-07 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 79274d10-0567-388d-9291-5ea47ab55434 | -6.2125 | -42.4769 | 2025-09-07 12:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 147.1 |
| 3f02505e-bd5e-3d0e-8623-3d3caf8154d1 | -11.586 | -47.7613 | 2025-09-07 12:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 244e426a-0cf2-3bcc-b0de-5c26f1646ed7 | -12.3016 | -47.2416 | 2025-09-07 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 6ab20ae3-9009-3a17-b68f-b83794fff775 | -5.8403 | -44.1181 | 2025-09-07 12:50:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 3d74a102-6cfe-3516-9994-aac06ffe01db | -13.9342 | -54.0256 | 2025-09-07 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 478001c9-8033-375b-9cf3-814485dc2174 | -12.7641 | -52.9498 | 2025-09-07 12:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 56b30b8a-3871-334b-837b-67b7ee6e1052 | -6.1923 | -42.6205 | 2025-09-07 12:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 16d12a03-16ee-3304-a273-891742feebb9 | -10.5869 | -48.4772 | 2025-09-07 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| e0a5fb83-331a-33cf-a00d-2986cc208090 | -19.4891 | -47.7879 | 2025-09-07 12:50:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 196fb785-aae7-30a0-87e5-a3ba867fa707 | -12.7832 | -52.9477 | 2025-09-07 12:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 30399a25-e8e9-3144-a0d6-4ba96cc70b53 | -12.8059 | -47.9959 | 2025-09-07 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |


[Clique aqui para ver as próximas entradas](README86.md)
